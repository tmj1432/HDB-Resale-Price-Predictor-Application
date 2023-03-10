# HDB Resale Price Predictor Web Application with streamlit.io

## Final Product Live Demo 
https://user-images.githubusercontent.com/113895589/222399442-fcba98e4-6cdf-46d4-9e74-5717f43ec2c5.mov

## Problem Statement
As a data scientist for a real estate company in Singapore, I am tasked to build a predictive model to predict the resale price of HDBs. This model would then have to be deployed on the cloud which can be accessed by the relevant stakeholders.

## Dataset
**Data Dictionary**
|Column Name|Data Type|Description
|---|---|---|
|flat_type|object|Type of Flat|
|floor_area_sqft|float|Floor Area in Sqft|
|lease_commencement_date|int|Year of lease commencement|
|mid|int|Median Floor of Floor Range|
|planning_area|object|Area of Flat|
|resale_price|float|Resale Price of Flat(Target Variable)

## Modelling
**Modelling Summary**
|Model|Train RMSE|Test RMSE|
|---|---|---|
|Baseline: LinearRegression|73474|73422|
|VotingRegressor(XGBoost, RandomForest, KNNRegressor)|39280|42741|
|**Final Model: XGBoost**|**36677**|**39574**|

To summarise the modelling section, I first built a baseline model using LinearRegression. Thereafter, I ran gridsearch on a pipeline with XGBoost, RandomForestRegressor and KNNRegressor. The results of the gridsearch were that XGBoost was the best model out of the three. 

However, before concluding to use XGBoost as a standalone model, I decided to consider building an ensemble of the three models. Ultimately, from the modelling summary above, we can see that the XGBoost model itself gave us the best RMSE out of all the models being considered in this section.

## Model Evaluation
`Permutation Importance:` Permutation importance is a technique for measuring the importance of features or variables in a machine learning model.

**Results of running permutation importance**
`Scoring: R2`
|Feature|Permutation Importance|Std|
|---|---|---|
|floor_area_sqft|1.087|0.004|
|planning_area|0.710|0.007|
|lease_commence_date|0.318|0.001|
|flat_type|0.098|0.001|
|mid|0.063|0.001|

Realistically, houses are priced according to their price per sqft. Therefore, it does not come as a surprise to me that floor_area_sqft has the highest permutation importance out of all the features. Next, planning_area has the second highest permutation importance. Again, this does not come as a surprise to me as HDBs in different regions of Singapore generally has their own price ranges. 

However, it is surprising that the level of the apartment did not really play a big role in its permutation importance. 

## Deployment
Finally, the final model is being deployed on streamlit.io

[Link to  streamlit web application](https://tmj1432-hdb-resale-price-predictor-application-app-5kd0gz.streamlit.app/)

## Limitation & Future Work
`Time:` as the years go by, HDB resale price may vary. <br>`Solution:`In order to combat this issue, we automate this whole process with an automated machine learning pipeline that automatically extracts data from [data.gov's HDB resale price API](https://data.gov.sg/dataset/resale-flat-prices) whenever it is updated as well as automatically model and deploy. 

`Data:` as the API is currently not being dated, the dataset only consists of data between 1967 and 2019. Therefore, it may not be able to generalise to current times. <br> `Solution:` However, this limitation can be easily overcome by collecting the data of the following years once the API updates or by collecting data from another source.

## Conclusion
In conclusion, we have managed to build and deploy a model that predicts HDB resale prices with a test RMSE of ~39600.
