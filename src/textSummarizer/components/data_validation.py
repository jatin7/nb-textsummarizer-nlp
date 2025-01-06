import os
from textSummarizer.logging import logger
from textSummarizer.entity import DataValidationConfig

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config
    def validate_all_files_exist(self) -> bool:
        try:
            status = None
            files = os.listdir(os.path.join("artifacts","data_ingestion","samsum_dataset"))
            """missing_files = [file for file in self.config.ALL_REQUIRED_FILES if file not in files]
               status = len(missing_files) == 0
               with open(self.config.STATUS_FILE, 'w') as f:
                if status:
                    f.write("VALIDATION STATUS: True")
                else:
                    f.write(f"VALIDATION STATUS: False"""
            for file in files:
                if file not in self.config.ALL_REQUIRED_FILES:
                    status = False
                    with open(self.config.STATUS_FILE,'w') as f:
                        f.write(f"VALIDATION STATUS: {status}")
                else:
                    status = True
                    with open(self.config.STATUS_FILE,'w') as f:
                        f.write(f"VALIDATION STATUS: {status}")
            return status
        
        except Exception as e:
            raise e