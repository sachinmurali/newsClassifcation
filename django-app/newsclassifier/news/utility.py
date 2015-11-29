import cPickle as pickle
from sklearn.externals import joblib

def read_pickled_data(pickle_file):
    with open(pickle_file, "r") as f:
        pick = joblib.load('filename.pkl')
    return pick
