import requests
from bs4 import BeautifulSoup

from utils.useful_functions import make_job_id

class WeWorkRemotely():
    def __init__(self):
        self.url = "https://weworkremotely.com/"
        self.soup = None

    def start(self):
        try:
            self.page = requests.get(self.url)
            self.page.raise_for_status()
        except(
                requests.exceptions.ConnectionError,
                requests.exceptions.Timeout,
                requests.exceptions.RequestException,
                requests.exceptions.HTTPError
        ):
            return False

        self.soup = BeautifulSoup(self.page.content, "html.parser")
        return True

    def getJobs(self) -> list:
        jobs_list = []

        if self.soup is None:
            return jobs_list

        self.jobs = self.soup.find_all("li", {"class": "new-listing-container"})
        for job in self.jobs:

            link_element = job.find("a", {"class": "listing-link--unlocked"})
            if link_element is None:
                continue

            link = self.url + link_element.get("href")

            logo_element = link_element.find("div", {"class": "new-listing"})
            if logo_element is None:
                continue

            title_element = logo_element.find("div", {"class": "new-listing__header"})
            if title_element is None:
                continue

            title_element_2 = title_element.find("h3", {"class": "new-listing__header__title"})
            title = None
            if title_element_2 is None:
                title = "N/A"
            else:
                title = title_element_2.get_text()

            company_element = logo_element.find("p", {"class": "new-listing__company-name"})
            company = None
            if company_element is None:
                company = "N/A"
            else:
                company = company_element.get_text(strip=True)

            location_element = logo_element.find("p", {"class": "new-listing__company-headquarters"})
            location = None
            if location_element is None:
                location = "N/A"
            else:
                location = location_element.get_text(strip=True)

            job_details = {
                "id": make_job_id(link),
                "title": title,
                "company": company,
                "location": location,
                "link": link,
                "logo": "../static/img/wwr_logo.png",
            }

            jobs_list.append(job_details)

        return jobs_list
