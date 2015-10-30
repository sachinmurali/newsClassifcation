import nltk;
import nltk.classify.naivebayes;
from trainingSet import DataExtractor

class NewsClassifier(object):
    def __init__(self):
        self.de = DataExtractor()
        self.de.SetCSVFileName('Reuter_data.csv')
        # Use Pickled data
        self.training_data = self.de.ReadPickledData()
        # print self.training_data
    def TrainData(self):
        # TODO
        # Train the classifier

    def RefreshData(self):
        self.de.GetArticles()
        self.training_data = self.de.ReadPickledData()


if __name__ == "__main__":
    classifier = NewsClassifier()
    #classifier.RefreshData()
    #classifier.TrainData()
