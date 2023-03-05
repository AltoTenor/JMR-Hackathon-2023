from roboflow import Roboflow
rf = Roboflow(api_key="Qbc4lG4O8U7k5TD1AKCh")
project = rf.workspace().project("crickettrack")
model = project.version(1).model

def detect(image):
    return model.predict(image, confidence=40, overlap=30).json()
