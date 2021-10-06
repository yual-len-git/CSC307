from stock_portfolio import *

user1 = user('Allen')

def test_create():
    # user1 = user('Allen')
    assert len(user1.portfolio) == 0


def test_stock_add():
    # user2 = user('Brandon')
    user1.buy_stock('gme', 5)
    user1.buy_stock('rblx', 10)
    assert len(user1.portfolio) == 2


def test_buy_stock():
    user1.buy_stock('gme', 10)
    user1.buy_stock('rblx', 10)
    assert user1.portfolio['gme'] == 15
    assert user1.portfolio['rblx'] == 20