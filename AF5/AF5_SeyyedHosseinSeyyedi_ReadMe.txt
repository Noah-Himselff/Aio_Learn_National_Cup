AF5 Seyyed Hossein Seyyedi,The Acting Test:
The following program is based on DeepFace Facial recognition library with some changes to the original code's and consists of two main parts:
the Seyyedi_analyze function and Seyyedi_stream function.
*Seyyedi_analyze uses the https://github.com/serengil/tensorflow-101/blob/master/model/facial_expression_model_weights.h5 model to process an input image of facial emotions thoroughly.
Then proceeds to ask which emotions does the user want the function to look for.
If the face had a certain level of accuracy for that emotion the user will be granted a base_point.
Base points are 1 and 0,however there is also the performance score which is between 0 and 4 with 0 failing the test and 4 making the perfect facial emotion.
 *Seyyedi_stream function is the live and real-time version of Seyyedi_analyze and uses it to create a real-time challenge for the users.
This function uses the local camera as input and takes screenshots every 5 seconds which will be sent to Seyyedi_analyze for processing as mentioned earlier.
By double clicking q the program will take its final screenshot and closes the camera,giving the user the chance to completely end the program or continuing with a different test.
the program can be expanded to not only analyze emotions but many more options such as age , gender or race.
But these functions were removed from the final program due to the nature of the competition

you can further read about the DeepFace library and its capabilities from the following link:
https://github.com/serengil/deepface