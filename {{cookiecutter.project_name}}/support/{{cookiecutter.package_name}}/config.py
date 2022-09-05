""" Configuration """

import json
import pathlib
import logging.config
import yaml

project_root = pathlib.Path(__file__).resolve().parents[2]

with open(project_root / "project_config.json") as data_file:
    json_data = json.load(data_file)


class Config:
    def __init__(self):
        self.logs_path = json_data["logs_path"]
        self.main_project_path = json_data["main_project_path"]
        self.data_path = json_data["data_path"]


config = Config()


def get_logs_path(path):
    if pathlib.Path(path).is_absolute():
        return path
    else:
        return project_root / path


logging_config = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {
        "simple": {"format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",},
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "simple",
            "stream": "ext://sys.stdout",
        },
        #         "file": {
        #             "class": "logging.FileHandler",
        #             "level": "DEBUG",
        #             "filename": config.logs_path + "\\log.txt",
        #         },
    },
    "loggers": {
        "simpleExample": {
            "level": "DEBUG",
            "handlers": ["console"],
            "propagate": "no",
        },
    },
    "root": {
        "level": "DEBUG",
        "handlers": ["console"],
        #     "handlers": ["console","file"],
    },
}

logging.config.dictConfig(logging_config)
