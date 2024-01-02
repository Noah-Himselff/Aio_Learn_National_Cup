AF4_SeyyedHosseinSeyyedi_Visually_Impaired_Assistant
This program sets to solve the AF4 problem in the Aio Learn national cup,helping the blind and visually impaired people.
for this program I have used a real life furniture detection dataset.
The dataset has well over 8 thousand annotated and labeled pictures on roboflow.com and the model that is used to detect the objects is Roboflow 2.0 Object Detection (Fast).
My program has used this model as its base model and is consisted of two main parts:
1-Image evaluation
2-Real life video function

Image evaluation:
on the first part I've used a detection function and an assistant function.
The detection function predicts all the objects in the picture,then if any object bounding box's area is bigger than a certain threshold it will pass that object to the assitant function.
This idea allows us to find close objects to us without having to use depth measurement programs which are often inaccurate on single cameras(the need for stereo cameras),costly(the need for high quality cameras) and very time consuming.
To further explain the time consuming aspect of depth measurement methods,they are often required the programmer to manually enter sizes for objects of the dataset,which is not only very time inefficient but can be very inaccurate due to certain classes having multiple sizes of objects(such as desks or tables).
The assistant function uses winsound to beep to the user notifying of an object close to them and then pyttsx3 to tell the user which function it actually is.

Real life video function:
This is the main part that addresses the AF4 problem.Here we use the capablities of roboflow library to analyze a video.
The on_prediction function is a callback function that is called when predictions are available.
It extracts class labels, converts predictions to a Detections object, and then checks if the area of the detected object is above a certain threshold. If so, it triggers a beep and speech announcement.
Finally, it displays the annotated image with bounding boxes using OpenCV.
The beep_and_speak function is similar to the assistant function mentioned prior.It wil be called on used if an object is bigger than a certain amount,indicating that it is close to the user.


You can further read about the libraries and models used in the program below

https://pyttsx3.readthedocs.io/en/latest/
https://roboflow.com/
https://universe.roboflow.com/mokhamed-nagy-u69zl/furniture-detection-qiufc/model/20
https://inference.roboflow.com/quickstart/run_model_on_rtsp_webcam/#run-a-vision-model-on-video-frames