import pandas as pd
import numpy as np
from datetime import datetime as dt

# read csv data
#  parse_dates = ["booking_check_in", "booking_check_out"], dayfirst=True
df = pd.read_csv('df/combined.csv',)

# encode listing
lId = pd.get_dummies(df.listing_id,prefix = "listing_id")
lStatus = pd.get_dummies(df.listing_status, prefix='listing_status')
# lInstantBook = pd.get_dummies(df.listing_instant_book, prefix='listing_instant_book')
# lRemark = pd.get_dummies(df.listing_remark, prefix='remark')
uId = pd.get_dummies(df.unit_id,prefix = "unit_id")
profileId = pd.get_dummies(df.profile_id, prefix='profile_id')
employee = pd.get_dummies(df.employee_id, prefix='employee')

# encode property
pId = pd.get_dummies(df.property_id,prefix = "id")
pType = pd.get_dummies(df.property_type,prefix= "type")
pStatus = pd.get_dummies(df.property_status, prefix='status')
pPack = pd.get_dummies(df.property_package, prefix='package')
pDesign = pd.get_dummies(df.property_design, prefix='design')
pProx = pd.get_dummies(df.property_proximity, prefix='prox')
pLifeSupport = pd.get_dummies(df.property_life_support, prefix = 'lifesupport')
pService = pd.get_dummies(df.property_service, prefix= 'service')
pArea = pd.get_dummies(df.area_id,prefix='area')

# encode area
area = ce.OrdinalEncoder(cols=['area_name', 'area_squad','area_airport_name'])
# fit and transform and you will get the encoded data
area = area.fit_transform(df)
area = area[['area_name','area_squad','area_airport_name']]

# concatinate all df
cproperty = pd.concat([pId,pType,pStatus,pPack,pDesign,pProx,pLifeSupport,pService,pArea,pEmployee],axis='columns')
listing = pd.concat([lId,lStatus,uId,profileId,employee],axis='columns')


dummies = pd.concat([cproperty,listing,booking],axis='columns')
# print(dummies)

# dump to csv
# dummies.to_csv(r'D:\bukitvista\encode\df\ready\dummies.csv')
