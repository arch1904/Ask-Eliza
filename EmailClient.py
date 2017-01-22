import smtplib
import watson2 as w
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from random import randint
import requests as re

def send_email(name,email_id):
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	f=open('archit.txt','r')
	text=f.read()
	needs,values = w.getProfile(text)
	r = re.get("https://216a8d55.ngrok.io/api?geography=geo")
	s = r.text.split("\r\n")
	curr_temperature = s[2*randint(0,3)+1]
	f.close()
	#passw = open('email_pass.txt','r')
	#password = passw.readline().strip()
	server.login("psychoelizalexa@gmail.com", "PsychoBC")
	#passw.close()
	f = open("Transcript_"+name+".txt",'r')
	text = f.read()
	f.close()
	msg = MIMEMultipart('alternative')
	msg['Subject'] = "Your Session Today"
	msg['From'] = "psychoelizalexa@gmail.com"
	msg['To'] = email_id
	needs_text = ""
	for need in needs:
		needs_text+=need+": "+str(needs[need])+"<br>"
	values_text = ""
	for value in values:
		values_text+=value+": "+str(values[value])+"<br>"

	html = """\
	<html><head>Complete Report For """ +name+"""</head><body>\
	<H2> Conversation Transcript </H2>"""+text+"""\
	<H3> Psychological Needs </H3>"""+needs_text+"""<H3> Values </H3>"""+values_text+"<br> Current Body Temperature: "+curr_temperature+"Celsius</p></body></html>"

	part1=MIMEText(html,'html')
	msg.attach(part1)
	server.sendmail("psychoelizalexa@gmail.com", email_id, msg.as_string())
	server.quit()
send_email("Archit","archit.941@gmail.com")
