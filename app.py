import streamlit as st

import datetime
import requests

'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''

date = st.date_input(
    'Date of the ride', 
    value=datetime.datetime(2012, 10, 6, 12, 10, 20))
time = st.time_input(
    'Time of the ride',
    value=datetime.datetime(2012, 10, 6, 12, 10, 20))
temp_datetime = datetime.datetime.combine(date, time)
pickup_datetime = f"{temp_datetime} UTC"
st.write('The pickup datetime is', pickup_datetime)

pickup_longitude = st.number_input('Pickup longitude', value=40.7614327)
pickup_latitude = st.number_input('Pickup latitude', value=-73.9798156)
dropoff_longitude = st.number_input('Dropoff longitude', value=40.6513111)
dropoff_latitude = st.number_input('Dropoff latitude', value=-73.8803331)
passenger_count = st.number_input('Number of passenger', value=2)
key = '2012-10-06 12:10:20.0000001'

'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

url = 'https://wagon-exo-z7fyqqvx3a-ew.a.run.app/predict_fare'

# if url == 'https://wagon-exo-z7fyqqvx3a-ew.a.run.app/predict_fare':

#     st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''

2. Let's build a dictionary containing the parameters for our API...
'''
params = {
    'key': key,
    'pickup_datetime': pickup_datetime,
    'pickup_longitude': pickup_longitude,
    'pickup_latitude': pickup_latitude,
    'dropoff_longitude': dropoff_longitude,
    'dropoff_latitude': dropoff_latitude,
    'passenger_count': passenger_count
}

'''
3. Let's call our API using the `requests` package...
'''

response = requests.get(url, params=params)

'''
4. Let's retrieve the prediction from the **JSON** returned by the API...
'''

predict = response.json()

'''
## Finally, we can display the prediction to the user
'''

st.write(f"{round(predict['pred'], 2)} $")