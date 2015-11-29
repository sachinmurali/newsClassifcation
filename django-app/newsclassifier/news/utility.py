import pickle

def read_pickled_data(pickle_file):
    with open(pickle_file, "r") as f:
	return pickle.load(f)
