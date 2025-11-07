import requests

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
        'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX25hbWUiOiJ1c2FtYS5wZXJ2ZXpAZW11bWJhLmNvbSIsInNjb3BlIjpbImpvYnNlZWtlciJdLCJyb2xlcyI6WyJKT0JTRUVLRVIiXSwiam9ic2Vla2VySWQiOiJSQ3F4YzZCM0tySTBwOUVlIiwiZXhwIjoxNzkzOTUzMDY3LCJhdXRob3JpdGllcyI6WyJKT0JTRUVLRVIiXSwianRpIjoiODk1MWVkYTktOTc2YS00NDAzLTkyNTMtZmIzZjYzNTg5ZTg3IiwiY2xpZW50X2lkIjoiZWZjIn0.IeaQKaJXNnECZ8hLMDMGgRoJMFUyPLlMc2_dhU-ZlMm1c6c3tUXTQ8TTmYsQNgnmelYr-J-juuoriEo2h55qwEPZNYlVlcBmweybsokLtMxkGlEcX-skzVBktzFyjEVscJxqDLrkMmHS-5yrQvZZcJjyzogyua8YDHlcPflW0itMp3WpbjB4ttthseWIHd7hGOCdglMET5u55WUXL-Nm2Vafu0BmOXdfh7EpdKRdrdHbz2jqROyH3wSJrQA1kA4Otf3mWMMpgMwYSG1vdgkbgDGb04sJpyhNo0Uz-eF2ZMv3Tuh5AUgaAJoLmGc3mZwvUxpPJjLU0c-e4EILQKppVg'
    }
    # send JSON payload
    response = requests.post(url, json=payload, headers=headers)
    return response.status_code
