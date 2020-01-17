import pandas as pd
import numpy as np
from datetime import datetime as dt
import category_encoders as ce

# read csv data
#  parse_dates = ["booking_check_in", "booking_check_out"], dayfirst=True
df = pd.read_csv('df/final.csv',low_memory=False)

# encode listing
# lId = pd.get_dummies(df.listing_id,prefix = "listing_id")
lStatus = pd.get_dummies(df.listing_status, prefix='listing_status')
# lInstantBook = pd.get_dummies(df.listing_instant_book, prefix='listing_instant_book')
# lRemark = pd.get_dummies(df.listing_remark, prefix='remark')
# uId = pd.get_dummies(df.unit_id,prefix = "unit_id")
# profileId = pd.get_dummies(df.profile_id, prefix='profile_id')
# employee = pd.get_dummies(df.employee_id, prefix='employee')

# encode IDs in ordinal
ids = ce.OrdinalEncoder(cols=['listing_id','unit_id','profile_id','property_id','employee_id','area_id'])
ids = ids.fit_transform(df)
ids = ids[['listing_id','unit_id','profile_id','property_id','employee_id','area_id']]

# encode property
# pId = pd.get_dummies(df.property_id,prefix = "id")
pType = pd.get_dummies(df.property_type,prefix= "type")
pStatus = pd.get_dummies(df.property_status, prefix='status')
pPack = pd.get_dummies(df.property_package, prefix='package')
pDesign = pd.get_dummies(df.property_design, prefix='design')
pProx = pd.get_dummies(df.property_proximity, prefix='prox')
pLifeSupport = pd.get_dummies(df.property_life_support, prefix = 'lifesupport')
pService = pd.get_dummies(df.property_service, prefix= 'service')
#pArea = pd.get_dummies(df.area_id,prefix='area')

# encode area
area = ce.OrdinalEncoder(cols=['area_name'])
# fit and transform and you will get the encoded data
area = area.fit_transform(df)
area = area[['area_name']]

# concatinate all df
cproperty = pd.concat([pType,pStatus,pPack,pDesign,pProx,pLifeSupport,pService],axis='columns')
listing = pd.concat([lStatus],axis='columns')

dummies = pd.concat([ids,area,cproperty,listing],axis='columns')
#print(dummies)

# dump to csv
dummies.to_csv('finis.csv')