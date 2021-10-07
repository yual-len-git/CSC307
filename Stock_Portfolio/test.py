from stock_portfolio import *
import pytest

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

def test_sell_stock():
    user1.sell_stock('gme', 5)
    user1.sell_stock('rblx', 5)
    assert user1.portfolio['gme'] == 10
    assert user1.portfolio['rblx'] == 15

def test_amount():
    assert user1.show_stock('gme') == 10
    assert user1.show_stock('rblx') == 15

def test_remove():
    user1.sell_stock('gme', 10)
    assert ('gme' not in user1.portfolio) == True
    assert ('gme' in user1.portfolio) == False

def test_exception():
    with pytest.raises(ShareSaleException):
        user1.sell_stock('rblx', 20)
