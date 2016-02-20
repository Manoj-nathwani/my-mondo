import os, requests, json
from datetime import datetime, date, timedelta

def get_data():
    access_token = _access_token()
    return _balance(access_token), _transactions(access_token)
def _access_token():
    payload = {
        'grant_type': 'password',
        'client_id': os.environ['client_id'],
        'client_secret': os.environ['client_secret'],
        'username': os.environ['username'],
        'password': os.environ['password'],
        }
    r = requests.post("https://production-api.gmon.io/oauth2/token", data=payload)
    r = json.loads(r.text)
    return r["access_token"]
def _balance(access_token):
    headers = {'Authorization': 'Bearer ' + access_token}
    payload = {
        'account_id': os.environ['account_id']'
    }
    r = requests.get(
        "https://api.getmondo.co.uk/balance",
        params=payload, headers=headers)
    r = json.loads(r.text)
    return r
def _transactions(access_token):
    headers = {'Authorization': 'Bearer ' + access_token}
    payload = {
        'account_id': os.environ['account_id']',
        'expand[]': 'merchant'
    }
    r = requests.get(
        "https://production-api.gmon.io/transactions",
        params=payload, headers=headers)
    return json.loads(r.text)["transactions"]

def summary(balance):
    summary = {}
    summary['balance'] = _clean_amount(balance['balance']*-1)
    summary['spend_today'] = _clean_amount(balance['spend_today'])
    return summary
def batched_transactions(transactions):
    dates = []
    for x in transactions:
        x['amount'] = _clean_amount(x['amount'])
        x['created'] = _clean_date(x['created'])
        if x['created'] not in dates:
            dates.append(x['created'])
    dates.reverse()
    batched_transactions = []
    for x in dates:
        batch = []
        total_spent = 0
        for transaction in transactions:
            if transaction['created'] == x:
                batch.append(transaction)
                spent = float(transaction['amount'])
                if spent > 0:
                    total_spent += spent
        batched_transactions.append({
        'date': x,
        'total_spent': "{0:.2f}".format(total_spent),
        'transactions': batch
        })
    return batched_transactions
def daily_budget_left(balance):
    days_left_this_month = 30 - datetime.today().day
    daily_budget_left = float(balance)/days_left_this_month
    return _clean_amount(daily_budget_left)

def _clean_date(created):
    created = created.split("T")[0]
    created = datetime.strptime(created, "%Y-%m-%d")
    if created.date() == datetime.today().date():
        return "Today"
    elif created.date() == (date.today() - timedelta(1)):
        return "Yesterday"
    else:
        return created.strftime('%A, %d %b %Y')
def _clean_amount(amount):
    amount = float(amount)
    amount = amount/100*-1
    return "{0:.2f}".format(amount)
