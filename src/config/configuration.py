
from src.constants.constants import *
import os, sys


ROOT_DIR = ROOT_DIR_KEY

# Dataset_url = 

DATASET_PATH = os.path.join(ROOT_DIR, DATA_DIR, DATA_DIR_KEY)

RAW_FILE_PATH = os.path.join(ROOT_DIR, ARTIFACT_DIR_KEY, DATA_INGESTION_KEY, CURRENT_TIME_STAMP, 
                             DATA_INGESTION_RAW_DATA_DIR, RAW_DATA_DIR_KEY)


TRAIN_FILE_PATH = os.path.join(ROOT_DIR, ARTIFACT_DIR_KEY, DATA_INGESTION_KEY, CURRENT_TIME_STAMP,
                               DATA_INGESTION_INGESTED_DATA_DIR_KEY, TRAIN_DATA_DIR_KEY)


TEST_FILE_PATH = os.path.join(ROOT_DIR, ARTIFACT_DIR_KEY, DATA_INGESTION_KEY, CURRENT_TIME_STAMP,
                               DATA_INGESTION_INGESTED_DATA_DIR_KEY, TEST_DATA_DIR_KEY)


# Data Transformation steps


PREPROCESING_OBJ_FILE = os.path.join(ROOT_DIR, ARTIFACT_DIR_KEY, DATA_TRANSFORMATION_ARTIFACT, 
                                     DATA_PREPROCCED_DIR, DATA_TRANSFORMTION_PROCESSING_OBJ)

TRANSFORM_TRAIn_FILE_PATH = os.path.join(ROOT_DIR, ARTIFACT_DIR_KEY, DATA_TRANSFORMATION_ARTIFACT,
                                         DATA_TRANSFORM_DIR, TRANSFORM_TRAIN_DIR_KEY)


TRANSFORM_TEST_FILE_PATH = os.path.join(ROOT_DIR, ARTIFACT_DIR_KEY, DATA_TRANSFORMATION_ARTIFACT,
                                         DATA_TRANSFORM_DIR, TRANSFORM_TEST_DIR_KEY)



FEATURE_ENGG_OBJ_FILE_PATH = os.path.join(ROOT_DIR, ARTIFACT_DIR_KEY, DATA_TRANSFORMATION_ARTIFACT,
                                          DATA_PREPROCCED_DIR,' feature_engg.pkl')
