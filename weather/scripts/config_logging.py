import logging

class LoggerHandler:

    def __init__(self):
        
        self._configure_logging()
        
    def _configure_logging(self):
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
    
    def instace_logging(self):
        return logging.getLogger('__name__')