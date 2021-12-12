import json

def test_balance(app, client):
    del app
    res = client.get('/')
    assert res.status_code == 200
    expected = {'balance': 0}
    assert expected == json.loads(res.get_data(as_text=True))

def test_deposit(app, client):
    del app
    res = client.get('/deposit?amount=500')
    assert res.status_code == 200
    expected = {'balance': 500}
    assert expected == json.loads(res.get_data(as_text=True))

def test_deposit_2(app, client):
    del app
    res = client.get('/deposit?amount=300')
    assert res.status_code == 200
    expected = {'balance': 800}
    assert expected == json.loads(res.get_data(as_text=True))

def test_withdraw_1(app, client):
    del app
    res = client.get('/withdraw?amount=1000')
    assert res.status_code == 200
    expected = {'balance': 800}
    assert expected == json.loads(res.get_data(as_text=True))

def test_withdraw_2(app, client):
    del app
    res = client.get('/withdraw?amount=100')
    assert res.status_code == 200
    expected = {'balance': 700}
    assert expected == json.loads(res.get_data(as_text=True))

def test_deposit_3(app, client):
    del app
    res = client.get('/deposit?amount=500')
    assert res.status_code == 200
    expected = {'balance': 1200}
    assert expected == json.loads(res.get_data(as_text=True))

def test_withdraw_3(app, client):
    del app
    res = client.get('/withdraw?amount=1000')
    assert res.status_code == 200
    expected = {'balance': 200}
    assert expected == json.loads(res.get_data(as_text=True))

def test_balance_2(app, client):
    del app
    res = client.get('/')
    assert res.status_code == 200
    expected = {'balance': 200}
    assert expected == json.loads(res.get_data(as_text=True))