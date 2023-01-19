import requests

def load_api_token():
    with open("./config/api_token", "r") as f:
        return f.read()

BASE_URL = "https://api.toshl.com"
API_TOKEN = load_api_token()

def get_default_headers():
    return { "Authorization": API_TOKEN }

def get(route):
    url = f"{BASE_URL}{route}"
    headers = get_default_headers()
    response = requests.get(url, headers=headers)
    return response

def merge_responses(responses):
    merged_result = []
    for response in responses:
        merged_result += response.json()
    return merged_result

def get_all_pages(route):
    response = get(route)
    all_responses = [response]
    while "next" in response.links:
        response = get(response.links["next"]["url"])
        all_responses.append(response)
    return all_responses

def get_all_pages_merged(route):
    return merge_responses(get_all_pages(route))
