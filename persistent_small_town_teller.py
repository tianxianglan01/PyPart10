import pickle

class PersistenceUtils:

    @staticmethod
    def write_pickle(obj):
        return pickle.dumps(obj)

    @staticmethod
    def load_pickle(obj):
        return pickle.loads(obj)