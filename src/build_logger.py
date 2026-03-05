import logging

def get_logger(name):
    logger= logging.getLogger(name)

    if not logger.handlers:
        logger.setLevel(logging.INFO)

        file_handler= logging.FileHandler('shared_app.log')
        console_handler= logging.StreamHandler()

        formatter= logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger