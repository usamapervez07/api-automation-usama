from endpoints.job_search_api import job_search

def test_job_apply():
    job_list = job_search("", "", [])
    assert len(job_list) > 0