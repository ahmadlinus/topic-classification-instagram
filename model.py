import numpy as np
from scipy.special import softmax
from sklearn.base import BaseEstimator, ClassifierMixin
import mlflow
import pickle

class TopicClassifier(BaseEstimator, ClassifierMixin):
    
    def __init__(self, topics: list = []):
        self.topics = topics


    def fit(self, dataset):
        pass


    def predict(self, text: str) -> list:
        input_ids = self.preprocess_text_for_classification(text)
        logits = np.random.normal(0, 1, len(self.topics))
        probs = softmax(logits)
        return probs
    

    def preprocess_text_for_classification(self, text: str) -> list:
        return []
    

if __name__ == '__main__':
    topics =["Sport", "Art", "Politics", "Food"]
    tc = TopicClassifier(topics)

    model_dump = pickle.dump(tc, open("tc_model", "wb"))

    with mlflow.start_run() as run:
        mlflow.sklearn.log_model(
            tc,
            "tc_model"
        )