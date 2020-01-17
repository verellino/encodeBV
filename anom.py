import pandas as pd
import numpy as np
from datetime import datetime as dt


df = pd.read_csv('df/bookingFee.csv', parse_dates =True, dayfirst=True)

# currency = df["booking_currency"]
# df.booking_currency.value_counts()
# booking_currency = pd.get_dummies(df.booking_currency, prefix = "currency")
# 
# function to usd
df.loc[df['booking_currency'] == 1, 'price_temp'] = df['fee_per_night'] / df['idr']
df.loc[df['booking_currency'] == 2, 'price_temp'] = df['fee_per_night']
df.loc[df['booking_currency'] == 3, 'price_temp'] = df['fee_per_night']
df.loc[df['booking_currency'] == 4, 'price_temp'] = df['fee_per_night'] / df['aud']
df.loc[df['booking_currency'] == 5, 'price_temp'] = df['fee_per_night'] / df['sgd']

# df.to_csv('df/price_temp.csv')
# for i in range(len(df[])) :
#    print(i)

    # if df.loc['booking_currency'] == 1 :
    #     price_temp = df['booking_earned'] / df['idr']
    # elif df.loc['booking_currency'] == 2 :
    #     price_temp = df['booking_earned']
    # elif df.loc['booking_currency'] == 3 :
    #     price_temp = df['booking_earned'] / df['eur']
    # elif df.loc['booking_currency'] == 4 :
    #     price_temp = df['booking_earned'] / df['aud']
    # price_temp = df.replace(['booking_earned','price_temp'])
#print(df['booking_earned'])

# nights of stay
checkin = pd.to_datetime(df['booking_check_in'])
checkout = pd.to_datetime(df['booking_check_out'])
total_stay = checkout - checkin
# print(total_stay.dt.days)

#checkin = pd.to_datetime(df.booking_check_in)
# total_stay = df['booking_check_out'] - df['booking_check_in'] 
#df['Difference'] = df['booking_check_out'].sub(df['booking_check_in'], axis=0)
#df_test['Difference'] = df_test['Difference'] / np.timedelta64(1, 'D')
#print (check)