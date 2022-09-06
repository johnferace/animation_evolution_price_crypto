'''
SIMULACION
'''
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import ccxt
import pandas as pd
import numpy as np
import time

# SPECIFICATIONS.....
par = 'ETH/USDT'
timeframe = '15m'
sensitivity_up = 1.05
sensitivity_under = 0.95
# linewidth = 0.5 #width of support and resistance
time_step = 15  # every time it updates the supports and resistances

def Get_candles(par, timeframe):  # Get the data of the pair you want to analyze
    exchange = ccxt.binance()
    datos = exchange.fetch_ohlcv(par, timeframe=timeframe, limit=1000)
    df = pd.DataFrame(datos, columns=['time', 'open', 'high', 'low', 'close', 'volume'])
    df['time'] = pd.to_datetime(df['time'], unit='ms')
    # df = df.set_index('time', drop=True)
    return df

def get_supp_and_resi():
    # list1 = #get the support and resistance
    # return list1
    pass

df = Get_candles(par=par, timeframe=timeframe)

list_true_false = []
longitud_plot = len(df['high'])
fer = np.arange(0, longitud_plot, time_step)
for i in range(len(fer)):
    for j in range(time_step - 1):
        list_true_false.append(False)
    list_true_false.append(True)

df_numpy = df['high'].to_numpy()
x_data, y_data = [], []

fig, ax = plt.subplots()
ax.set_xlim(-1, 100)  # Define the beginning limits of the x-axis of the graph
ax.set_ylim((df_numpy[0]) * sensitivity_under,
            (df_numpy[0]) * sensitivity_up)  # Define the start limits of the y-axis of the graph
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.grid()  # Draw a grid on the graph
line, = ax.plot(0, 0)

j = 0
list2 = []

def supp_res(i):  # Draw the support and resistance
    global j, list2

    list1 = get_supp_and_resi()  # call the function to get the support and resistance
    pass


''' 
    if j != 0:
        resistance_11 = ax.axhline(list2[0], color='white', linewidth=1)
        resistance_22 = ax.axhline(list2[1], color='white', linewidth=1)
        resistance_33 = ax.axhline(list2[2], color='white', linewidth=1)
        resistance_44 = ax.axhline(list2[3], color='white', linewidth=1)

        support_11 = ax.axhline(list2[4], color='white', linewidth=5)
        support_22 = ax.axhline(list2[5], color='white', linewidth=5)
        support_33 = ax.axhline(list2[6], color='white', linewidth=5)
        support_44 = ax.axhline(list2[7], color='white', linewidth=5)

    resistance_1 = ax.axhline(list1[], color='green', linewidth=1)
    resistance_2 = ax.axhline(list1[], color='green', linewidth=1)
    resistance_3 = ax.axhline(list1[], color='green', linewidth=1)
    resistance_4 = ax.axhline(list1[], color='green', linewidth=1)

    support_1 = ax.axhline(list1[], color='red', linewidth=1)
    support_2 = ax.axhline(list1[], color='red', linewidth=1)
    support_3 = ax.axhline(list1[], color='red', linewidth=1)
    support_4 = ax.axhline(list1[], color='red', linewidth=1)

    list2 = list2.append(list1[:])

    return resistance_11, resistance_22, resistance_33, resistance_44, support_11, support_22, support_33, support_44,
           resistance_1, resistance_2, resistance_3, resistance_4, support_1, support_2, support_3, support_4
'''

newvalue = df_numpy[0]

def limits_xy(i):  # <>
    global newvalue
    fer1 = newvalue * (sensitivity_up - 0.01)
    fer2 = newvalue * (sensitivity_under + 0.01)
    if df_numpy[i] > fer1:
        newvalue = df_numpy[i]
        return ax.set_ylim((df_numpy[i]) * sensitivity_under, (df_numpy[i]) * sensitivity_up)
    elif df_numpy[i] < fer2:
        newvalue = df_numpy[i]
        return ax.set_ylim((df_numpy[i]) * sensitivity_under, (df_numpy[i]) * sensitivity_up)
    else:
        pass

def animation_frame(i):
    x_data.append(i)
    y_data.append(df_numpy[i])
    line.set_data(x_data, y_data)  # (line.set_xdata(x_data), line.set_ydata(y_data))
    ax.set_xlim(left=i - 50, right=i + 50)
    limits_xy(i)
    if list_true_false[i]:
        # supp_res(i)
        # ax.axhline(df_numpy[10], color='black')
        pass
    return line,

animation = FuncAnimation(fig, func=animation_frame, frames=np.arange(0, 1000, 1), interval=1, repeat=False)
plt.show()
