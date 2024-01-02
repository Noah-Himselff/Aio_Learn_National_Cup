AF3_SeyyedHosseinSeyyedi
Sales Prediction:
In this program we addressed the third challenge of the Aio Learn competition which is a Sales Prediction problem
The program uses the pandas to the read the csv document and to start.
Then after defining the entry data and the target data I have used a function to find the shuffling of data in order to have an accurate model.
The main predictor model that was used in this program is XGBRegressor with the R_2 score of 0.978 and MSE of 0.62
The key advantage of XGBRegressor is its speed and rather highperformance that achieved the metrics mentioned earlier in 0.1s after the best random_state has beed found
Furthermore with the help of the shap,matplotlib and plotly libraries to thoroughly dive into visualizing the outputs of predictions
And Finally I ended the challenge with a prediction function that takes user data to predict sales

Note that this program was written on google colab cloud service so if it is tested on local IDEs you might not have some libraries installed prior to this program