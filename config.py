from os import path

ENCODING = 'utf-8'

BASE_DIR = path.dirname(path.abspath(__file__))

"""
Пути для хранения статичных файлов
"""

STATIC_PATH = 'static'

DATASETS_FOLDER = "datasets"
DATASET_BWSAS_FILE = "beach-weather-stations-automated-sensors-1.csv" 

DATASETS_FOLDER_ABS_PATH = path.join(BASE_DIR, STATIC_PATH, DATASETS_FOLDER)
DATASET_BWSAS_FILE_ABS_PATH = path.join(DATASETS_FOLDER_ABS_PATH, DATASET_BWSAS_FILE)

"""
Пути для хранения динамичных файлов
"""

PROTOS_FOLDER = "protos"
MESSAGES_FOLDER = "messages"

PROTOS_FOLDER_ABS_PATH = path.join(BASE_DIR, PROTOS_FOLDER)
MESSAGES_FOLDER_ABS_PATH = path.join(BASE_DIR, MESSAGES_FOLDER)

"""
Логи
"""

LOG_FILE = 'logs.log'
LOG_FILES_PATH = 'logs'

LOG_ABS_PATH = path.join(BASE_DIR, LOG_FILES_PATH, LOG_FILE)

'''
Настройки loguru
'''
LOG_FORMAT = '{time} | {level} | {message}'
LOG_ROTATION = '10 MB'
