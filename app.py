import os, mondo, json, jinja2
from pushbullet import Pushbullet
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    balance, transactions = mondo.get_data()
    summary = mondo.summary(balance)
    batched_transactions = mondo.batched_transactions(transactions)
    daily_budget_left = mondo.daily_budget_left(balance['balance'])

    return render_template(
        'index.html',
        balance = summary['balance'],
        spend_today = summary['spend_today'],
        daily_budget_left = daily_budget_left,
        batched_transactions=batched_transactions)

@app.route('/new_transaction', methods=['POST'])
def new_transaction():
    r = json.loads(request.data)
    if r['type'] == 'transaction.created':
        amount = '\u00a3{0:.2f}'.format(float(r['data']['amount'])*-1)
        description = r['data']['description']
        message_title = '{} spent'.format(amount, description)
        message_body = '@ {}'.format(amount, description)
        pb = Pushbullet(os.environ.get('pushbullet_key'))
        push = pb.push_note(message_title, message)
        return message

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
