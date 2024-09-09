import os
from pathlib import Path
import logging 
logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')

project_name="hate"
list_of_files=[
    f"{project_name}/component/__init__.py",
    f"{project_name}/component/data_ingestion.py",
    f"{project_name}/component/tranformation.py",
    f"{project_name}/component/model_evaluation.py",
    f"{project_name}/component/model_trainer.py",
    f"{project_name}/component/model_pusher.py",

    f"{project_name}/configuration/__init__.py",
    f"{project_name}/configuration/gcloud_sysncer.py",

    f"{project_name}/constants/__init__.py",

    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/entity/artifact_entity.py",

    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",

    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/prediction.py",
    f"{project_name}/component/train_pipeline.py",

    f"{project_name}/ml/__init__.py",
    f"{project_name}/ml/feature.py",
    f"{project_name}/ml/models.py",
    "app.py",
    "demo.py",
    "requirments.txt",
    "Dockerfile",
    "setup.py",
    ".dockerignore"   
]
for filepath in list_of_files:
    filepath=Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir !=" ":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"crating directory: {filedir} for the file: {filename}")
    if(not os.path.exists(filepath)) or  (os.path.getsize(filepath)==0):
        with open(filepath ,"w")as f:
            pass
            logging.info(f"Creating empty file:{filepath}")
    else :
        logging.info(f"{filename} is already exists")
