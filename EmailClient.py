import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("psychoelizalexa@gmail.com", "PsychoBC")
f = open('Transcript_Archit.txt','r')
msg="Subject:Your Session Today\n\n "+f.read()
f.close()

server.sendmail("psychoelizalexa@gmail.com", "archit.941@gmail.com", msg)
server.quit()
