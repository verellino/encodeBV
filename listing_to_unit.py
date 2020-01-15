import pandas as pd
import numpy as np

df = pd.read_csv("df/listing_to_unit.csv")
# create columns for  "listing_type" dummy variables
ID = pd.get_dummies(df.id,prefix="id")
lId = pd.get_dummies(df.listing_id,prefix = "listing_id")
uId = pd.get_dummies(df.unit_id,prefix = "unit_id")

# object for all encoded df
dummies = pd.concat([ID,lId,uId],axis='columns')
# convert dummies to new csv
#dummies.to_csv(r'D:\bukitvista\encode\df\ready\listing_to_unit_dummies.csv')
#print(dummies)