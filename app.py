import streamlit as st
import numpy as np
import joblib

# title
st.title('HDB Resale Price Predictor')

# another title
st.markdown('Please Input Values')

# features required for prediction
floor_area_sqft = st.number_input('Floor Area (Sqft)', min_value=333, max_value=3014)
lease_commence_date = st.number_input('Lease Commence Date', min_value=1966, max_value=2019)
mid = st.number_input('Floor of unit', min_value=1, max_value=50)
flat_type = st.selectbox('Flat Type',
                         ('1 ROOM', '2 ROOM', '3 ROOM', '4 ROOM', '5 ROOM', 'EXECUTIVE', 'MULTI-GENERATION'))
planning_area = st.selectbox('Area',('Jurong West', 'Woodlands', 'Sengkang', 'Tampines', 'Yishun', 'Bedok',
       'Punggol', 'Hougang', 'Ang Mo Kio', 'Choa Chu Kang', 'Bukit Merah',
       'Bukit Batok', 'Bukit Panjang', 'Toa Payoh', 'Pasir Ris', 'Queenstown',
       'Geylang', 'Sembawang', 'Clementi', 'Jurong East', 'Kallang',
       'Serangoon', 'Bishan', 'Novena', 'Marine Parade', 'Outram', 'Rochor',
       'Bukit Timah', 'Changi', 'Downtown Core', 'Tanglin',
       'Western Water Catchment'))

# predict button
if st.button('Predict'):
    model = joblib.load('final_model.joblib')
    X = np.array([flat_type,floor_area_sqft,lease_commence_date,mid,planning_area])
    X = X.reshape(1,-1)
    pred = model.predict(X)[0]
    st.markdown(f'### Predicted Resale Price of this HDB is ${str(int(round(pred,-3)))}')
