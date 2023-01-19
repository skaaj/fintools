from core import *

# Accounts
def list_accounts():
    return get_all_pages_merged(f"/accounts")

def get_account(id):
    return get(f"/accounts/{id}").json()

# Categories
def list_categories():
    return get_all_pages_merged(f"/categories")

def get_category(id):
    return get(f"/categories/{id}").json()

# Entries
def list_entries(start_date, end_date):
    return get_all_pages_merged(f"/entries?from={start_date}&to={end_date}")

def get_entry(id):
    return get(f"/entries/{id}").json()

# Tags
def list_tags():
    return get_all_pages_merged("/tags")

def get_tag(id):
    return get(f"/tags/{id}").json()
