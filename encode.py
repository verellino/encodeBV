import pandas as pd 
import numpy as np

df = pd.read_csv("df/property.csv")

property_type = df["property_type"]
property_type = df.property_type.astype(object)
obj_property_type = df.select_dtypes(include=[float]).copy()

# frozen1 = (0,0,0,0,0,1)
# frozen2 = (0,0,0,0,1,0)
# frozen3 = (0,0,0,1,0,0)
# frozen4 = (0,0,1,0,0,0)
# frozen5 = (0,1,0,0,0,0)
# frozen6 = (1,0,0,0,0,0)

# fSet1 = frozenset(frozen1)
# fSet2 = frozenset(frozen2)
# fSet3 = frozenset(frozen3)
# fSet4 = frozenset(frozen4)
# fSet5 = frozenset(frozen5)
# fSet6 = frozenset(frozen6)

cleanup= {"property_type": 
                {
                    1 : (0,0,0,0,0,1),
                    2 : (0,0,0,0,1,0 ),
                    3 : (0,0,0,1,0,0),
                    4 : (0,0,1,0,0,0),
                    5 : (0,1,0,0,0,0),
                    6 : (1,0,0,0,0,0)
                }
                }
obj_property_type.replace(cleanup, inplace=True)
obj_property_type.head()
print(obj_property_type.head())