import os


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
LOG_PATH = os.path.join(BASE_DIR, 'log')
os.makedirs(LOG_PATH, exist_ok=True)

TEST_LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'basic': {
            'format': '%(asctime)-6s: %(name)s - %(levelname)s - %(message)s',
            'datefmt': "%Y-%m-%d %H:%M:%S",
        }
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'basic',
        },
        'test_main_file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'formatter': 'basic',
            'filename': os.path.join(LOG_PATH, 'test_main.log'),
            'when': 'D',
            'encoding': 'utf-8',
        },
        'test_error_file': {
            'level': 'ERROR',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'formatter': 'basic',
            'filename': os.path.join(LOG_PATH, 'test_error.log'),
            'when': 'D',
            'encoding': 'utf-8',
        },
    },
    'loggers': {
        'helper.war': {
            'handlers': ['console', 'test_main_file', 'test_error_file'],
            'level': 'DEBUG',
            'propogate': False
        },
    }
    # 'root': {
    #     'handlers': ['console', 'main_file', 'error_file'],
    #     'level': 'DEBUG',
    # }
}