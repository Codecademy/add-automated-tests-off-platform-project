from flask import Flask, jsonify, request

app = Flask(__name__)

balance = 0

@app.route('/')
def index():
    return jsonify({'balance': balance})

@app.route('/deposit')
def deposit():
    global balance
    amount = request.args.get('amount')
    balance = balance + int(amount)
    return jsonify({'balance': balance})

@app.route('/withdraw')
def withdraw():
    global balance
    amount = request.args.get('amount')
    if(int(amount) > balance):
        return jsonify({'balance': balance})    
    balance = balance - int(amount)
    return jsonify({'balance': balance})

if __name__ == '__main__':
    app.run(debug=True)
