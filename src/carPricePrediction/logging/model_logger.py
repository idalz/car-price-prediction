import logging

class ModelLogger:
    def __init__(self, log_file):
        self.log_file = log_file
        self.logger = logging.getLogger("modelLogger")
        self.logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    def log_message(self, message):
        self.logger.info(message)
