# HDB Resale Price Predictor Web Application with streamlit.io

## Final Product Live Demo 
https://user-images.githubusercontent.com/113895589/222321593-06b24803-8877-4ead-a41f-e26d0195b48f.mov

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

## EDA

## Modelling
**Modelling Summary**
|Model|Train RMSE|Test RMSE|
|---|---|---|
|LinearRegression|73474|73422|
|VotingRegressor(XGBoost, RandomForest, KNNRegressor)|39280|42741|
|**Best Model: XGBoost**|**36677**|**39574**|

## Model Evaluation

## Deployment

## Limitations 

## Conclusion & Recommendations
