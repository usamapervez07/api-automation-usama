import requests
from dotenv import load_dotenv
import os

load_dotenv()

def job_search(job_title, location, job_id_list):
    url = "https://job-search-api.efinancialcareers.com/v1/efc/jobs/search"
    params = {
        "q": job_title,
        "location": location,
        "page": 1,
        "pageSize": 5,
        "facets": "seniority|fullNormalizedJobTitle|locationPath|salaryRange|sectors|employmentType|experienceLevel|workArrangementType|salaryCurrency|minSalary|maxSalary|positionType|postedDate|clientBrandNameFilter",
        "currencyCode": "USD",
        "culture": "en",
        "recommendations": True,
        "fj": False,
        "includeRemote": False,
        "includeUnspecifiedSalary": True
    }
                    

    headers = {
        'Content-Type': 'application/json',
        'Authorization': os.getenv('job_search_token')
    }

    response = requests.get(url, params, headers=headers)
    data = response.json()
    for job in data['data']:
        job_id_list.append(job['id'])
    return job_id_list


    