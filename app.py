import streamlit as st
import datetime
import requests

from get_l import getLandL


'''
# TaxiFare Prediction
'''

st.markdown('''
### This page can help you to predict your taxifare in New York.
''')

# get current timestamp
time = datetime.datetime.now()
year = time.year
month = time.month
day = time.day
hour = time.hour
minute = time.minute
# get pickup date
d = st.date_input('choose date:', datetime.date(year, month, day))
st.write('The date:', d)
# get pickup time
t = st.time_input('choose time:', datetime.time(hour, minute))
st.write('Time:', t)
# connect date & time
pickup_datetime = str(d) + ' ' + str(t)

# get number of passengers
passenger_count = str(st.number_input('How many passengers?', value=1))
st.write('The number of passengers is ', passenger_count)

# pickup latitude n longtitude
pickup_point = st.text_input('Pick up point', 'Time square, New York')
st.write('Pick up point is', pickup_point)


# dropoff latitude n longtitude
dropoff_point = st.text_input('drop off point', 'Canal Street, New York')
st.write('Pick up point is', dropoff_point)



## Once we have these, let's call our API in order to retrieve a prediction


## Finally, we can display the prediction to the user
if st.button('predict'):

    pickup_longtitude, pickup_latitude = getLandL(pickup_point)
    dropoff_longtitude, dropoff_latitude = getLandL(dropoff_point)

    url = 'https://taxifare.lewagon.ai/predict'
    params = {
        "pickup_datetime": pickup_datetime,
        "pickup_longitude": pickup_longtitude,
        "pickup_latitude": pickup_latitude,
        "dropoff_longitude": dropoff_longtitude,
        "dropoff_latitude": dropoff_latitude,
        "passenger_count": passenger_count
    }

    response = requests.get(url, params).json()
    taxifare_pred = response['prediction']
    taxifare_pred = str(round(taxifare_pred, 2))
    st.write('Our prediction for your taxifare is: ')
    st.write(taxifare_pred)

else:
    st.write('If everything has been typed in click to predict.')
