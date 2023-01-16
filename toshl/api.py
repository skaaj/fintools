from core import *
from utils import DataClassIO
from models import Account

def list_entries(start_date, end_date):
    return get_all_pages_merged(f"/entries?from={start_date}&to={end_date}")

def list_accounts():
    acc = Account(12)
    print(DataClassIO.write(acc))
    return [DataClassIO.read(Account, d) for d in get('/accounts').json()]

def list_categories():
    return get_all_pages_merged('/categories')

def list_tags():
    return get_all_pages_merged('/tags')
