from html_func import *
from email_func import *
import zipfile
import os
import datetime
import sys

import shutil, errno

reload(sys)
sys.setdefaultencoding('utf-8')
from flask import Flask, render_template,request
app = Flask(__name__)


def copyanything(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)


def check_values(education_details,work_details,proj_details,cert_details):
	flag_dict={}
	if len(education_details['edu_name'])==0:
		flag_dict['edu']=0
	else :
		flag_dict['edu']=1
	if len(work_details['work_name'])==0:
		flag_dict['work']=0
	else :
		flag_dict['work']=1
	if len(proj_details['proj_name'])==0:
		flag_dict['proj']=0
	else :
		flag_dict['proj']=1
	if len(cert_details['c_name'])==0:
		flag_dict['cert']=0
	else :
		flag_dict['cert']=1
	"""
	if cert_details['curr_name']==None:
		flag_dict['curr']=0
	else :
		flag_dict['curr']=1
	
	if skills == None:
		flag_dict['skills']=0
	else :
		flag_dict['skills']=1
	"""
	return flag_dict


def create_website(personal_details,education_details,work_details,proj_details,cert_details):
	print "Calling create_Website..."
	flag_dict=check_values(education_details,work_details,proj_details,cert_details)

	intro 	=generate_intro_string(personal_details)
	nav 	=generate_navbar_string(flag_dict,personal_details)
	footer 	=generate_footer_string()
	web_string=intro+nav+ generate_header_string(personal_details) +generate_sections(personal_details,education_details,work_details,proj_details,cert_details,flag_dict)+ str(footer)
	

	folder_name=str(personal_details['fname'])+str(personal_details['mname'])+str(personal_details['lname'])
	file_name='/mysite/'folder_name
	f= open(file_name+'.html',"w+") 
	f.write(web_string +f.name)
	f.close()	
	return folder_name,file_name

def make_default_empty(x):
	if x==None:
		return ""
	return x

@app.route("/")
def hello():
    return render_template('index.html')



@app.route("/create_portfolio", methods=['POST'])
def create_portfolio():
	
	#Personal Details
	fname 		= request.form.get('fname', None)
	lname 		= request.form.get('lname', None)
	mname 		= request.form.get('mname', None)
	linkedin	= request.form.get('linkedin',None)
	email		= request.form.get('email', None)
	summary		= request.form.get('summary', None)
	tag			= request.form.get('tag', None)
	

	personal_details =create_pdetails_dict(fname,mname,lname,linkedin,email,summary,tag)
	for value in personal_details.keys():
		personal_details[value]=make_default_empty(personal_details[value])

	#Education
	edu_name	= request.form.getlist('edu_name[]', None)
	edu_major	= request.form.getlist('edu_major[]', None)
	edu_date	= request.form.getlist('edu_date[]', None)
	edu_gpa		= request.form.getlist('edu_gpa[]', None)
	edu_desc	= request.form.getlist('edu_desc[]', None)
	education_details =create_edetails_dict(edu_name,edu_major,edu_date,edu_gpa,edu_desc)
	
	
	#Work Experience
	work_name	= request.form.getlist('work_name[]', None)
	work_pos	= request.form.getlist('work_pos[]', None)
	work_sdate	= request.form.getlist('work_sdate[]', None)
	work_edate	= request.form.getlist('work_edate[]', None)
	work_desc	= request.form.getlist('work_desc[]', None)
	work_details =create_wdetails_dict(work_name,work_pos,work_sdate,work_edate,work_desc)
	

	#Project
	proj_name	= request.form.getlist('proj_name[]', None)
	proj_url	= request.form.getlist('proj_url[]', None)
	proj_sdate	= request.form.getlist('proj_sdate[]', None)
	proj_edate	= request.form.getlist('proj_edate[]', None)
	proj_desc	= request.form.getlist('proj_desc[]', None)

	proj_details=create_prdetails_dict(proj_name,proj_url,proj_sdate,proj_edate,proj_desc)
							
	#Skills
	#skills	= request.form.get('skills', None)
	
	#Awards/Cert
	cert_name	= request.form.getlist('cert_name[]', None)
	cert_url	= request.form.getlist('cert_url[]', None)
	cert_details =create_cdetails_dict(cert_name,cert_url)
	
	"""
	#Extra Curriculars
	curr_name[]	= request.form.get('curr_name[]', None)
	curr_url[]	= request.form.get('curr_url[]', None)
	curr_details =create_edetails_dict(curr_name,curr_url)
	"""
	#formData = request.values if request.method == "GET" else request.values
	#response = "Form Contents <pre>%s</pre>" % "<br/>\n".join(["%s:%s" % item for item in formData.items()] )
	#return response
	folder_name,file_name=create_website(personal_details,education_details,work_details,proj_details,cert_details)
	
	"""
	if  os.path.exists(folder_name):
		shutil.rmtree(folder_name)
	os.mkdir(folder_name)
	copyanything('ready_files',folder_name+'/')
	shutil.move(file_name, folder_name+'/')
	zip_folder(folder_name, file_name+'.zip')
	"""
	f_zip = zipfile.ZipFile(file_name+'.zip', 'w')
	for file in ['/mysite/README.pdf',file_name+'.html']:
		f_zip.write(file)
	f_zip.close()
	send_email(file_name+'.zip',email)
	if  os.path.exists(file_name+'.html'):
		os.remove(file_name+'.html')
	if  os.path.exists(file_name+'.zip'):
		os.remove(file_name+'.zip')
		
	return render_template('thankyou.html')



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=1467)
