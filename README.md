
# Job Scrapper

This project is a application that scrap the information about jobs from a website and with the help of a local LLM model, the description will be summarized and displayed in a proper way.

## 🛠️Technologies

* Python 3.14
* Flask
* BeautifullSoup
* Ollama

## 🌐 Currently supported website

At the moment, job listings are scraped from WeWorkRemotely only. Support for additional job sites may be added in the future.

## 🤖 LLM Model

Job descriptions are summarized locally using Ollama with the llama3.2 model. Make sure to pull it before running the app:

```bash
  ollama pull llama3.2
```

## ⚙️ Installation

Make sure you have all the required packages installed as mentioned in requirements.txt. Download the project as a zip file or clone it using the following command:

```bash
  git clone https://github.com/CrazyEnvelope/JobScraper.git
```
    
## 📁 Documentation
The project consists of the following files and directories:

* main.py — Flask app entry point, defines the app's routes.
* sites/weworkremotely.py — Scrapes job listings from WeWorkRemotely.
* utils/useful_functions.py — Shared helper functions (job lookup, id generation, fetching job details).
* utils/ollama_sumarizer.py — Sends job descriptions to Ollama and structures the LLM's response.
* utils/basemodel_class/BasicInfo.py — Data schema for company, salary, and education info.
* utils/basemodel_class/Skills.py — Data schema for required and preferred skills.
* utils/basemodel_class/Responsibilities.py — Data schema for job responsibilities.
* templates/index.html — Job listings page.
* templates/job_details.html — Detailed view of a single job.
* templates/error.html — Generic error page.
* static/styles/styles.css — App styling.
* static/img/ — Icons and images used throughout the app.
