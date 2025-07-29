from locust import HttpUser, task, between
import random

class IrisApiUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def predict_endpoint(self):
        payload = {
          "sepal_length": round(random.uniform(4.0, 8.0), 1),
          "sepal_width":  round(random.uniform(2.0, 4.5), 1),
          "petal_length": round(random.uniform(1.0, 7.0), 1),
          "petal_width":  round(random.uniform(0.1, 2.5), 1)
        }
        self.client.post("/predict", json=payload)
