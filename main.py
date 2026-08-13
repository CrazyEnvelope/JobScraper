from bs4 import BeautifulSoup
import requests

from flask import Flask
from flask import render_template

from utils.ollama_sumarizer import resume_job_description

app = Flask(__name__)

URL = "https://weworkremotely.com/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
jobs = soup.find_all("li", {"class": "new-listing-container"})

jobs_list = []
for job in jobs:

    link_element = job.find("a",{"class":"listing-link--unlocked"})
    if link_element is None:
        continue

    link = URL + link_element.get("href")

    logo_element = link_element.find("div",{"class":"new-listing"})
    if logo_element is None:
        continue

    title_element = logo_element.find("div",{"class":"new-listing__header"})
    if title_element is None:
        continue

    title_element_2 = title_element.find("h3",{"class":"new-listing__header__title"})
    title = None
    if title_element_2 is None:
        title = "N/A"
    else:
        title = title_element_2.get_text()

    company_element = logo_element.find("p",{"class":"new-listing__company-name"})
    company = None
    if company_element is None:
        company = "N/A"
    else:
        company = company_element.get_text(strip=True)

    location_element =  logo_element.find("p", {"class": "new-listing__company-headquarters"})
    location = None
    if location_element is None:
        location = "N/A"
    else:
        location = location_element.get_text(strip=True)

    job_details = {
        "id": len(jobs_list),
        "title": title,
        "company": company,
        "location": location,
        "link": link,
    }

    jobs_list.append(job_details)

def add_job_details(job_id):
    job_details = jobs_list[job_id]
    page = requests.get(job_details["link"])
    soup = BeautifulSoup(page.content, "html.parser")
    job_description_element = soup.find("div",{"class":"lis-container__job__content"})

    job_details.update({"details": resume_job_description(job_description_element.get_text(separator= " ", strip=True))})

@app.route("/")
def display_jobs():
    return render_template("index.html", jobs_list=jobs_list)

@app.route("/job/<string:job_id>")
def open_details(job_id):

    if "details" not in jobs_list[int(job_id)]:
        add_job_details(int(job_id))

    return render_template("job_details.html", job_details=jobs_list[int(job_id)])


