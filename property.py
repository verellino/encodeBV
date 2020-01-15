import pandas as pd
import numpy as np

df = pd.read_csv("df/property.csv")
# encode property type (one hot encoding)
# create columns for  "property_type" dummy variables
pId = pd.get_dummies(df.property_id,prefix = "id")

pType = pd.get_dummies(df.property_type,prefix= "type")
# print all columns including type
# merged = pd.concat([df,pType],axis='columns')

pStatus = pd.get_dummies(df.property_status, prefix='status')
pPack = pd.get_dummies(df.property_package, prefix='package')
pDesign = pd.get_dummies(df.property_design, prefix='design')
pProx = pd.get_dummies(df.property_proximity, prefix='prox')

pLifeSupport = pd.get_dummies(df.property_life_support, prefix = 'lifesupport')
pService = pd.get_dummies(df.property_service, prefix= 'service')

pArea = pd.get_dummies(df.area_id,prefix='area')

# property_bedrooms (data not good man)
# pBedrooms = pd.get_dummies(df.property_bedrooms)
# pBedrooms.rename(columns={0.0: 'bedroom_1',
#                     1.0: 'bedroom_2',
#                     2.0: 'bedroom_3',
#                     3.0 :  'bedroom_4',
#                     4.0 :  'bedroom_5',
#                     5.0 :  'bedroom_6'}, 
#                  inplace=True)

pEmployee = pd.get_dummies(df.employee_id, prefix='employee')

# object for all encoded df
dummies = pd.concat([pId,pType,pStatus,pPack,pDesign,pProx,pLifeSupport,pService,pArea,pEmployee],axis='columns')
# convert dummies to new csv
#dummies.to_csv(r'D:\bukitvista\encode\df\ready\property_dummies.csv')
print(dummies)