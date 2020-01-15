import pandas as pd
import numpy as np
from datetime import datetime as dt

df = pd.read_csv('df/booking.csv', delimiter=None,parse_dates=True,infer_datetime_format=True, dayfirst=True)



check = df[~df.booking_check_out.str.contains()]
#checkin = pd.to_datetime(df.booking_check_in)
# total_stay = df['booking_check_out'] - df['booking_check_in'] 
#df['Difference'] = df['booking_check_out'].sub(df['booking_check_in'], axis=0)
#df_test['Difference'] = df_test['Difference'] / np.timedelta64(1, 'D')
print (check)