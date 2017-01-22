import smtplib
import watson2 as w
def send_email(name,email_id):
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	f=open('archit.txt','r')
	text=f.read()
	needs,values = w.getProfile(text)
	passw = open('email_pass.txt','r')
	password = passw.readline().strip()
	server.login("psychoelizalexa@gmail.com", password)
	passw.close()
	f = open("Transcript_"+name+".txt",'r')
	f.seek(0,0)
	msg="Subject:Your Session Today\n\n "+f.read()
	f.close()
	server.sendmail("psychoelizalexa@gmail.com", email_id, msg)
	server.quit()
