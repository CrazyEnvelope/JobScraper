from flask import Flask
from flask import render_template

from sites.weworkremotely import WeWorkRemotely
from utils.useful_functions import add_job_details
from utils.useful_functions import find_job

app = Flask(__name__)

jobs_list = []
weworkremotely = WeWorkRemotely()

@app.route("/")
def display_jobs():
    global jobs_list
    success = weworkremotely.start()

    if not success:
        return render_template("error.html",
                               message="Unable to retrieve jobs from the source site. Check your connection."), 503

    jobs_list = weworkremotely.getJobs()
    return render_template("index.html", jobs_list=jobs_list)

@app.route("/job/<string:job_id>")
def open_details(job_id):
    job = find_job(job_id,jobs_list)
    if job is None:
        return render_template("error.html", message="The requested job was not found, or the session has expired."), 404

    if "details" not in job:
        success = add_job_details(job)

        if not success:
            return render_template("error.html",
                                   message="Unable to retrieve details for this job from the source site."), 503

    return render_template("job_details.html", job_details=job)




