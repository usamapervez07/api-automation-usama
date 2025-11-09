import requests
from dotenv import load_dotenv
import os

load_dotenv()

def apply_to_job(cv_id,first_name,job_id, jobseeker_id, last_name, locale):
    url = "https://job-application.efinancialcareers.com/v2/job-applications"
    payload = {
        "cv_id": cv_id,
        "first_name": first_name,
        "job_id": job_id,
        "jobseeker_id": jobseeker_id,
        "last_name": last_name,
        "locale": locale
    }
    headers = {
        'Content-Type': 'application/json',
        'Authorization': os.getenv('Token')
    }
    # send JSON payload
    response = requests.post(url, json=payload, headers=headers)
    return response.status_code
