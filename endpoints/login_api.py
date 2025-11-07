import requests

def login_user(username, password):
    url = "https://auth.efinancialcareers.com/v1/token"
    payload = {
                "grant_type":"password",
                "scope":"jobseeker",
                "jib":"1243b5aa-00c3-4bf0-b234-a2088662ce6b",
                "username":username,
                "password":password,
                "remember_me":False
                }
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic ZWZjOmVmY3NlY3JldA=='
    }

    response = requests.post(url, json=payload, headers=headers)
    print(response.status_code)
    return response.status_code

