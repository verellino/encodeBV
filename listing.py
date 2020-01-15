import pandas as pd
import numpy as np

df = pd.read_csv("df/listing.csv")
# create columns for  dummy variables
lId = pd.get_dummies(df.listing_id,prefix = "id")
lStatus = pd.get_dummies(df.listing_status, prefix='status')

lInstantBook = pd.get_dummies(df.listing_instant_book, prefix='instant_book')
lRemark = pd.get_dummies(df.listing_remark, prefix='remark')
lProfileId = pd.get_dummies(df.profile_id, prefix='profileId')
# object for all encoded df
dummies = pd.concat([lId,lStatus,lInstantBook,lRemark],axis='columns')
# convert dummies to new csv
#dummies.to_csv(r'D:\bukitvista\encode\df\ready\listing_dummies.csv')
print(dummies)