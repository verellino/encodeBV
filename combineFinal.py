import pandas as pd
from datetime import date
​
# Listing Folder 
listing_to_unit = pd.read_csv('df/listing_to_unit.csv')
listing = pd.read_csv('df/listing.csv')
​
# Merge Listing and Listing to unit
listingNew = listing.merge(listing_to_unit, on = 'listing_id')
# Selecting columns to be used
listingNew = listingNew[['listing_id', 'unit_id', 'listing_name', 'listing_status', 'property_id', 'profile_id', 'employee_id']]
​
areas = pd.read_csv('df/area.csv', low_memory = False)
areas = areas[['area_id','area_name','area_distance_to_airport']]
​
properties = pd.read_csv('df/property.csv')
properties = properties[['property_id', 'property_name', 'property_type', 'property_status', 'property_package', 'property_design', 'property_proximity', 'property_life_support', 'property_service', 'area_id']]
​
bookings = pd.read_csv('df/booking.csv', delimiter = ',', low_memory = False)
bookings = bookings[['booking_check_in', 'booking_check_out', 'booking_earned', 'booking_currency','booking_source', 'listing_id']]
​
exchangeRate = pd.read_csv('df/exchange.csv', low_memory= False)
exchangeRate = exchangeRate[['id','sgd','aud','idr']]
​
bookingNew = bookings.merge(exchangeRate, left_on = 'booking_check_in', right_on = 'id')
bookingNew.to_csv('df/bookingNew.csv')
​
bookingList = bookingNew.merge(listingNew, on = 'listing_id')
bookingList.to_csv('df/bookingList.csv')
​
bookingPro = bookingList.merge(properties, on = 'property_id')
bookingPro.to_csv('df/bookingPro.csv')
​
bookingFinal = bookingPro.merge(areas, how = 'left' ,left_on = 'area_id', right_on= 'area_id')
bookingFinal.to_csv('df/bookingFinal.csv')
​
bookingFinal['booking_check_in'] = pd.to_datetime(bookingFinal['booking_check_in'])
bookingFinal['booking_check_out'] = pd.to_datetime(bookingFinal['booking_check_out'])
​
bookingFinal['length_of_stay'] = bookingFinal['booking_check_out'] - bookingFinal['booking_check_in']
bookingFinal['length_of_stay'] = bookingFinal['length_of_stay'].dt.days
bookingFinal.to_csv('Final/bookingDate.csv')
​
bookingFinal['fee_per_night'] = bookingFinal['booking_earned'] / bookingFinal['length_of_stay']
print(bookingFinal['fee_per_night'])
bookingFinal.to_csv('Final/bookingFee.csv')