from endpoints.job_apply import apply_to_job
from endpoints.job_search_api import job_search
import random


def test_job_apply():
    job_id_list = job_search("", "", [])
    status_code = apply_to_job("0QmRz6doPYdLng1", "Usama", job_id_list[random.randint(0, 4)], "RCqxc6B3KrI0p9Ee", "Pervez", "us_US")
    assert status_code == 201