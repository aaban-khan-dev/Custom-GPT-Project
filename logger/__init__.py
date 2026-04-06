import os
import logging
from datetime import datetime

class Customlogger:
    def __init__(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        log_dir = os.path.join(base_dir,'..','logs')
        
        os.makedirs(log_dir,exist_ok=True)

        current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        self.log_file_name = f"{current_time}.log"
        self.log_file_path = os.path.join(log_dir,self.log_file_name)

        logging.basicConfig(filename = self.log_file_path,
                            filemode = 'w',
                            format = '[%(asctime)s] %(name)s - %(levelname)s - %(message)s',
                            level = logging.INFO)
        
        self.logger = logging.getLogger(__name__)

    def get_logger(self):
        return self.logger
    

logger = Customlogger().get_logger()