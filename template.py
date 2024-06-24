import os
from pathlib import Path


list_of_files = [
    
    "src/__init__.py",
    "src/utils.py",
    "src/logger.py",
    "src/exception.py",
    
    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/components/model_trainer.py",
    
    "src/pipeline/__init__.py",
    "src/pipeline/predict_pipeline.py",
    "src/pipeline/train_pipeline.py",
    
    "notebook/__init__.py",
    "notebook/EDA.ipynb",
    "notebook/model_training.ipynb",
    "notebook/data/__init__.py",
    
    "requirements.txt",
    "setup.py",



]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)


    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass