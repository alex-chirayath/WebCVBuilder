import datetime
import sys



def convert_date_format(date):
	if(date.strip()==""):
		return ""
	return datetime.datetime.strptime(date, '%Y-%m-%d').strftime('%m/%d/%y')


def create_pdetails_dict(fname,mname,lname,linkedin,email,summary,tag):
	pdetails={}
	pdetails['fname']=fname
	pdetails['mname']=mname
	pdetails['lname']=lname
	pdetails['fname']=fname
	pdetails['linkedin']=linkedin
	pdetails['email']=email
	pdetails['summary']=summary
	pdetails['tag']=tag
	return pdetails

def create_edetails_dict(edu_name,edu_major,edu_date,edu_gpa,edu_desc):
	edetails={}
	edetails['edu_name']=edu_name
	edetails['edu_major']=edu_major
	edetails['edu_date']=edu_date

	edetails['edu_gpa']=edu_gpa
	edetails['edu_desc']=edu_desc
	return edetails
	

def create_wdetails_dict(work_name,work_pos,work_sdate,work_edate,work_desc):
	wdetails={}
	wdetails['work_name']=work_name
	wdetails['work_pos']=work_pos
	wdetails['work_edate']=work_edate
	
	wdetails['work_sdate']=work_sdate
	wdetails['work_desc']=work_desc
	return wdetails

def create_prdetails_dict(proj_name,proj_url,proj_sdate,proj_edate,proj_desc):
	prdetails={}
	prdetails['proj_name']=proj_name
	prdetails['proj_url']=proj_url
	prdetails['proj_edate']=proj_edate
	
	prdetails['proj_sdate']=proj_sdate
	
	prdetails['proj_desc']=proj_desc

	
	return prdetails

def create_cdetails_dict(name_list,url_list):
	xdetails={}
	xdetails['c_name']=name_list
	xdetails['c_url'] =url_list
	return xdetails

def generate_intro_string(personal_details):
	s='<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no"><meta name="description" content="Web Resume Builder"><meta name="author" content="Alex Chirayath and Mrudula Deore">'+'	<title>'+str(personal_details['fname'])+' '+str(personal_details['lname']) +'</title> <link href="css/bootstrap.min.css" rel="stylesheet"> ' \
	'<link href="css/nav-scroll.css" rel="stylesheet"><link href="css/resume.css" rel="stylesheet"></head><body style="background-color:#F57C00" id="page-top">'
	return s

def generate_header_string(personal_details):
	link=""
	if(personal_details['linkedin'].strip()!=""):
		link=' | <a href="'+personal_details['linkedin']+'">LinkedIn</a>'
	s='<header class="bg-header container"><div class="container row"><div class="col-md-1 hidden-xs"></div>' \
	'<div class ="col-md-3 hidden-xs hidden-sm"><img class="profile-img" src="img/profile.jpg"></div>' \
	'<div class="col-md-8"><h1>' +str(personal_details['fname'])+' '+str(personal_details['mname'])+' '+str(personal_details['lname'])+'</h1>'
	s+='</h1><p class="lead">'+ str(personal_details['tag'])+'|' +personal_details['email'] +link +'</p></div></div></header>'
	return s

def generate_color_section(x):
	if x%2==0:
		return "bg-light"
	return "bg-grey1"

def generate_section_intro (x):
	a=generate_color_section(x)
	x+=1
	return ('<section class="'+ a +'" id=',x)

def generate_section_end():
	return '</div></div></div></section>'

def generate_work_div(inst_name,inst_det,sdate,edate,desc):
	s='<div><div class="row"><div class="col-md-9"><h4><u>' + str(inst_det)+'-'+str(inst_name) +'</u></h4></div>' 
	sdate=convert_date_format(sdate)
	edate=convert_date_format(edate)
	s+='<div class="col-md-3">'
	if (sdate.strip())!='':
		s+='<p class="workedu-date"><b>' + str(sdate) +'</b>'
		if (edate.strip())=='':
			edate='Present'
		s+=' - <b>'+str(edate) +'</b></p>'
	else:
		s+='<p class="workedu-date"><b>' + str(edate)+'</b></p>'

	s+='</div></div>'
	if (desc.strip())!='':
		s+='<p class="workedu-desc lead">' + str(desc)+'</p>'
	s+='</div><br><br>'
	return s

def generate_proj_div(proj_name,proj_url,proj_sdate,proj_edate,proj_desc):
	proj_sdate=convert_date_format(proj_sdate)
	proj_edate=convert_date_format(proj_edate)
	
	l1=""
	l2=""
	if proj_url.strip()!="":
		l1='<a href="'+proj_url+'">'
		l2='</a>'
	
	s='<div><div class="row"><div class="col-md-9"><h4><u>'+l1 + str(proj_name) +l2+ '</u></h4></div>' 
	s+='<div class="col-md-3">'
	
	if (proj_sdate.strip())!='':
		s+='<p class="workedu-date"><b>' + str(proj_sdate) +'</b>'
		if (proj_edate.strip())=='':
			proj_edate='Present'
		s+=' - <b>'+str(proj_edate) +'</b></p>'
	else:
		s+='<p class="workedu-date"><b>' + str(proj_edate)+'</b></p>'
	s+='</div></div>'
	if (proj_desc.strip())!='':
		s+='<p class="workedu-desc lead">' + str(proj_desc)+'</p>'
	s+='</div><br><br>'
	return s

def generate_cert_div(cert_name,cert_url):
	l1=l2=""
	if cert_url.strip()!="":
		l1='<a href="'+cert_url+'">'
		l2='</a>'
	s='<div><p><u>'+l1 + str(cert_name) +l2+'</u></p>' 

	s+='</div><br><br>'
	return s


def generate_edu_div(inst_name,inst_det,edate,desc,gpa):
	s='<div><div class="row"><div class="col-md-9"><h4><u>' + str(inst_name) +'</u></h4></div>' 
	s+='<div class="col-md-3">'
	edate=convert_date_format(edate)
	
	if (edate.strip())!='':
		s+='<p class="workedu-date"><b>' + str(edate)+'</b></p>'
	s+='</div>'
	s+='</div><div class="row"><div class="col-md-9"><p>'
	s+='<b>'+str(inst_det)+'</b></p></div>'
	s+='<div class="col-md-3"><p class="workedu-date"> '
	if gpa.strip()!='':
		s+="<b>GPA:"+str(gpa)+'</b>'
	s+='</p></div></div>'

	
	
	if (desc.strip())!='':
		s+='<p class="workedu-desc lead">' + str(desc)+'</p>'
	s+='</div><br><br>'
	return s
            

def generate_sections(personal_details,education_details,work_details,proj_details,cert_details,flag_dict):
	print "Calling generate sections..."
	
	counter=0
	s=''
	a,counter=generate_section_intro (counter)
	b='><div class="container"><div class="row"><div class="col-lg-8 mx-auto"><h2>'
	c='</h2><br><br>'
	
	#Personal details
	pdetails =a + '"about"'+b+'About Me'+c
	pdetails+='<p class="lead">'+ personal_details['summary'] +'</p>' 
	pdetails+= generate_section_end()
	s+=pdetails

	if flag_dict['edu']==1:
		a,counter=generate_section_intro (counter)
		edetails = a+ '"edu"' +b+ 'Education' +c
		for i in range(len(education_details['edu_name'])):
			edetails+=generate_edu_div(education_details['edu_name'][i],education_details['edu_major'][i],education_details['edu_date'][i],education_details['edu_desc'][i],education_details['edu_gpa'][i])

		edetails+=generate_section_end()
		s+=edetails

	if flag_dict['work']==1:
		a,counter=generate_section_intro (counter)
		wdetails =a+ '"workex"'+b+'Work Experience'+c
		for i in range(len(work_details['work_name'])):
			wdetails+=generate_work_div(work_details['work_name'][i],work_details['work_pos'][i],work_details['work_sdate'][i],work_details['work_edate'][i],work_details['work_desc'][i])

		wdetails+=generate_section_end()
		s+=wdetails

	

	if flag_dict['proj']==1:
		a,counter=generate_section_intro (counter)
		prdetails=a+'"proj"'+b+'Projects'+c
		for i in range(len(proj_details['proj_name'])):
			prdetails+=generate_proj_div(proj_details['proj_name'][i] ,proj_details['proj_url'][i] ,proj_details['proj_sdate'][i] , proj_details['proj_edate'][i] ,proj_details['proj_desc'][i] )
		prdetails+=generate_section_end()

		s+=prdetails
	

	if flag_dict['cert']==1:
		a,counter=generate_section_intro (counter)
		cdetails=a+'"extras"'+b+'Achievements'+c
		for i in range(len(cert_details['c_name'])):
			cdetails+=generate_cert_div(cert_details['c_name'][i] ,cert_details['c_url'][i]  )
		cdetails+=generate_section_end()

		s+=cdetails

	return s


def generate_navbar_string(flag_dict,personal_details):
	x='<li class="nav-item"><a class="nav-link js-scroll-trigger" href='
	y='</a></li>'
	s= '<nav class="navbar navbar-expand-lg navbar-dark bg-dark fixed-top" id="mainNav"><div class="container">'\
'<a class="navbar-brand js-scroll-trigger" href="#page-top">'+str(personal_details['fname'])+' '+str(personal_details['mname'])+' '+str(personal_details['lname'])+'</a><button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive"'\
' aria-expanded="false" aria-label="Toggle navigation"><span class="navbar-toggler-icon"></span></button><div class="collapse navbar-collapse" id="navbarResponsive"><ul class="navbar-nav ml-auto">'

	if ((personal_details['summary'].strip())!= ''):
		s+=x+'"#about">About'+y
	if flag_dict['edu']==1:
		s+=x+'"#edu">Education'+y
	if flag_dict['work']==1:
		s+=x+'"#workex">Experience'+y
	if flag_dict['proj']==1:
		s+=x+'"#proj">Projects'+y
	if flag_dict['cert']==1:
		s+=x+'"#extras">Achievements/Extracurriculars'+y

	s+='</ul></div></div></nav>'
	return s

def generate_footer_string():
	s=' <footer style="margin-top: 10px;bottom:0;" ><div class="row" style="background-color:#F57C00;padding:20px;">' \
        '<p class=" col-md-4 text-left " style="padding:10px; "> WRB is protected under  <a href="https://www.gnu.org/licenses/gpl-3.0.en.html">GNU General Public License v3.0</a></p>'\
        '<p class=" col-md-4 text-center" style="padding:10px; "> Got any feedback?   <a href="https://docs.google.com/forms/d/1unxBU-9MXHHnWZNAdSv8a-bQZTKq7ZJCORewnqyIiKw/edit">Click HERE!</a></p>'\
		'<p class=" text-right  col-md-4" style="padding:10px; "> Developers: <a href="https://www.linkedin.com/in/alex-anto-chirayath/">Alex Chirayath</a> and <a href="https://www.linkedin.com/in/mrudula-deore/">Mrudula Deore</a></p>'\
        '</div></footer> <script src="js/jquery.min.js"></script><script src="js/bootstrap.bundle.min.js">'\
		'</script><script src="js/jquery.easing.min.js"></script><script src="js/nav-scroll.js"></script></body></html>'
	return s
