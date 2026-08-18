from bs4 import BeautifulSoup
import requests
import hashlib

from utils.ollama_sumarizer import resume_job_description

def add_job_details(job_details):
    try:
        page = requests.get(job_details["link"])
    except(requests.exceptions.ConnectionError,
                requests.exceptions.Timeout,
                requests.exceptions.RequestException,
                requests.exceptions.HTTPError):
        return False
    soup = BeautifulSoup(page.content, "html.parser")
    job_description_element = soup.find("div",{"class":"lis-container__job__content"})

    job_details.update({"details": resume_job_description(job_description_element.get_text(separator= " ", strip=True))})
    return True

def find_job(job_id, jobs_list):
    return next((j for j in jobs_list if j["id"] == job_id), None)

def make_job_id(link: str) -> str:
    return hashlib.md5(link.encode()).hexdigest()[:10]