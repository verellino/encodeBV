import pandas as pd
import category_encoders as ce

df = pd.read_excel('df/area.xlsx')


# create an object of the OrdinalEncoding
ordinal = ce.OrdinalEncoder(cols=['area_name', 'area_squad'])
# fit and transform and you will get the encoded data
ordinal = ordinal.fit_transform(df)

# enc_area_name = ordinal.mapping[0]['mapping']
# enc_area_squad = ordinal.mapping[1]['mapping']

# df['area_name'] = df[['area_name']].apply(lambda row: enc_area_name[row['area_name']], axis=1)
# df['area_squad'] = df[['area_squad']].apply(lambda row: enc_area_squad[row['area_squad']], axis=1)
print(ordinal[['area_name','area_squad']])
# map.to_csv(r'D:\bukitvista\encode\df\ready\dummy.csv',index=False,header="False")