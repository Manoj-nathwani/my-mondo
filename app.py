import os, mondo, json, jinja2
from pushbullet import Pushbullet
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    m = mondo.Mondo()
    return render_template(
        'index.html',
        balance = m.balance,
        daily_budget = m.daily_budget,
        batched_transactions = m.batched_transactions)

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
