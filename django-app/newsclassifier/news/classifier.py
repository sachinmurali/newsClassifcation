from utility import *

class Classifier():
     def __init__(pickle_file):
         """
         Load classifier object from pickled file 
	 """
         self.classifier = read_pickled_data(pickle_file)

     def predict(testset):
	 return self.classifier.predict(testset)	
