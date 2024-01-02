AF2_SeyyedHosseinSeyyedi_Spam_Detection:
In this program we addressed the second challenge of the Aio Learn competition which is Spam Detection
This program uses pandas to read all 5 csv files and then creates a mega datafame from all csv tables.
After cleaning the dataframe from unimportant data and checking the integrity of it I used a loop to find the best random_state for the prediction model to train on.
For the prediction model I used SVM which often proves to be a good choice of algorithm for NLP tasks.
The SVM model takes its input data from a fit and transformed text using TfidfVectorizer.
After training the model and obtaining the prediction model I used seaborn,matplotlib,confusion matrix and wordcloud to visualize the data.
Then at the end a test was taken from the model to see its functionality on unseen data