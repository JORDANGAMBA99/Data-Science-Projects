# %% [markdown]
# # Trading Bot

# %%
#!pip install pandas

# %%
import MetaTrader5 as mt5
import pandas
import time

# %% [markdown]
# login = 81283410
# password ="Superman1999*"
# server ="ExnessKE-MT5Trial10"

# %%

# display data on the MetaTrader 5 package
print("MetaTrader5 package author: ",mt5.__author__)
print("MetaTrader5 package version: ",mt5.__version__)
 
# establish MetaTrader 5 connection to a specified trading account
if not mt5.initialize(path="C:/Program Files/MetaTrader 5/terminal64.exe",login=81283410, server="ExnessKE-MT5Trial10",password="Superman1999*"):
    print("initialize() failed, error code =",mt5.last_error())
    quit()




# %%
def place_buy(symbol, lot, sl=200, tp=400):
    symbol_info = mt5.symbol_info(symbol)
    if symbol_info is None:
        print(symbol, "not found, can not call order_check()")
        return None
    
    lot = lot
    point = mt5.symbol_info(symbol).point
    price = mt5.symbol_info_tick(symbol).ask
    deviation = 20
    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": lot,
        "type": mt5.ORDER_TYPE_BUY,
        "price": price,
        "sl": price - sl * point,
        "tp": price + tp * point,
        "deviation": deviation,
        "magic": 234000,
        "comment": "python script open",
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_IOC,
    }
    
    # send a trading request
    result = mt5.order_send(request)
    if result.retcode != mt5.TRADE_RETCODE_DONE:
        print(f"The order failed with {result.retcode}")
        return None
    
    return result.order

def place_sell(symbol, lot, sl=200, tp=400):
    symbol_info = mt5.symbol_info(symbol)
    if symbol_info is None:
        print(symbol, "not found, can not call order_check()")
        return None
    
    lot = lot
    point = mt5.symbol_info(symbol).point
    price = mt5.symbol_info_tick(symbol).ask
    deviation = 20
    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": lot,
        "type": mt5.ORDER_TYPE_SELL,
        "price": price,
        "sl": price + sl * point,
        "tp": price - tp * point,
        "deviation": deviation,
        "magic": 234000,
        "comment": "python script open",
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_IOC,
    }
    
    # send a trading request
    result = mt5.order_send(request)
    if result.retcode != mt5.TRADE_RETCODE_DONE:
        print(f"The order failed with {result.retcode}")
        return None
    
    return result.order

# %%
symbol='USDJPYz'
place_buy(lot=0.01, symbol=symbol, sl= 200)

# %%
current_price = mt5.symbol_info_tick(symbol).ask
print(current_price)

# %%
def check_trade_outcome(order_ticket):
    deals = mt5.history_deals_get(position=order_ticket)
    if deals:
        for deal in deals:
            if deal.reason == mt5.ORDER_REASON_SL:
                return True
            elif deal.reason == mt5.ORDER_REASON_TP:
                return True

    orders = mt5.history_orders_get(position=order_ticket)
    if orders:
        for order in orders:
            if order.reason == mt5.ORDER_REASON_SL:
                return True
            elif order.reason == mt5.ORDER_REASON_TP:
                return True

    return False
  

# %%

start_price=  mt5.symbol_info_tick(symbol).ask
order_ticket= None
while True:
    positions=mt5.positions_get(symbol=symbol)

    if len(positions)==0:
        if order_ticket is None or order_ticket == 0:
            current_price = mt5.symbol_info_tick(symbol).ask 
            if (current_price-start_price)/start_price >= 0.00001:
                order_ticket= place_buy(symbol=symbol, lot=0.01) # palce a buy order.
                print(f"Buy order placed order_ticket {order_ticket} price % {(current_price-start_price)/start_price}")
            elif  (current_price-start_price)/start_price <= -0.00001:
                order_ticket= place_sell(symbol=symbol, lot=0.01) # palce a sell order.
                print(f"sell order placed order_ticket  {order_ticket} price % {(current_price-start_price)/start_price}")
            else:
                print(f"Current_price: {current_price}, Starting price: {start_price},  % Change: {(current_price-start_price)/start_price}")
        else:
            if check_trade_outcome(order_ticket):
                start_price= mt5.symbol_info_tick(symbol).ask 
                order_ticket=None
                print("Order_ticket & start_price updated,")
        
    # else:
    #     print("We have an position")
    time.sleep(3)
   


