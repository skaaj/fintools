import requests

def load_api_token():
    with open('./config/api_token', 'r') as f:
        return f.read()

BASE_URL = 'https://api.toshl.com'
API_TOKEN = load_api_token()

def get_default_headers():
    return { 'Authorization': API_TOKEN }

def get(route):
    return requests.get(f'{BASE_URL}{route}', headers=get_default_headers())

def merge_responses(responses):
    acc = []
    for response in responses:
        acc = acc + response.json()
    return acc

def get_all_pages(route):
    resp = get(route)
    acc = [resp]
    while 'next' in resp.links:
        resp = get(resp.links['next']['url'])
        acc.append(resp)
    return acc

def get_all_pages_merged(route):
    return merge_responses(get_all_pages(route))
