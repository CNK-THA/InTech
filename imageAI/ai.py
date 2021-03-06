from imageai.Prediction.Custom import ModelTraining
import os

# print(os.getcwd()+"\Desktop\IT course October 2020\image\idenprof")
# for subdir in sorted(os.listdir("idenprof")):
#     print(subdir)


# model_trainer = ModelTraining()
# model_trainer.setModelTypeAsResNet()
# model_trainer.setDataDirectory(os.getcwd()+"\Desktop\imageAI\images")
# model_trainer.trainModel(num_objects=3, num_experiments=3, enhance_data=True, batch_size=5, show_network_summary=True)








#num_object == types 
#num_experiment == how many times to train these images
#enhance_data == if less than 1000 images per class set to True
#batch_size == images to train concurrently, in multiple of 8
#show_network_summary == display to cmd










from imageai.Prediction.Custom import CustomImagePrediction
import os

execution_path = os.getcwd()

#CREATE OUR AI OBJECT
prediction = CustomImagePrediction()
prediction.setModelTypeAsResNet()
prediction.setModelPath(os.getcwd()+"\Desktop\imageAI\images\models\model_ex-002_acc-0.333333.h5")
prediction.setJsonPath(os.getcwd()+ "\Desktop\imageAI\images\json\model_class.json")
prediction.loadModel(num_objects=3)


# INTERACT WITH OUR AI
# print(os.getcwd()+"\Desktop\imageAI\images" + "\\test\Dog\dog1.jpg")
predictions, probabilities = prediction.predictImage(os.getcwd()+"\Desktop\imageAI\images\\test\Robot\\robot5.jpg", result_count=3)
for eachPrediction, eachProbability in zip(predictions, probabilities): #DISPLAY TOP 3 PREDICTIONS
    print(eachPrediction , " : " , eachProbability)