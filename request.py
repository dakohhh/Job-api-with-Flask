import requests

BASE = "http://127.0.0.1:5000/"


auth = {
    "id": 2892, 
    "comapany_name": "Monospace",
    "job_title": "Receptionist", 
    "salary": 300000,
    "status": "Part time", 
    "desc": "Lead Architect is needed",
    "email": "www.apply.devtech@host.com"
}
id = 2323

#response = requests.post(BASE + "/dev/jobs/", auth)

#response = requests.get(BASE + "/dev/jobs/", auth)
#response = requests.delete(BASE + "/dev/jobs/")

response = requests.get(BASE + "/dev/jobs/filter/jobtitle/pharmarcist")

print(response.json())


