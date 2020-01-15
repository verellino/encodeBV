import pandas as pd
import numpy as np
df = pd.read_excel("df/area.xlsx")
# create columns for  "area_type" dummy variables
lId = pd.get_dummies(df.area_id,prefix = "id")
lDistance = pd.get_dummies(df.area_distance_to_airport, prefix='distace')
lIAirportName = pd.get_dummies(df.area_airport_name, prefix='airport_name')
lAreaId = pd.get_dummies(df.area_id,prefix='areaId')
# object for all encoded df
dummies = pd.concat([lId,lDistance,lIAirportName,lAreaId],axis='columns')
# convert dummies to new csv
dummies.to_csv(r'D:\bukitvista\encode\df\ready\area.csv')
# print(dummies)