from src.textSummarizer.pipeline.data_ingestion import DataIngestionTrainingPipeline
from src.textSummarizer.pipeline.data_validation import DataValidationPipeline
from src.textSummarizer.logging import logger

STAGE = 'DATA_INGESTION'
try:
    logger.info(f">>>>>>> Stage {STAGE} started <<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>> Stage {STAGE} completed <<<<<<<")
    STAGE = 'DATA_VALIDATION'
    logger.info(f">>>>>>> Stage {STAGE} started <<<<<<<")
    data_validation = DataValidationPipeline()
    data_validation.main()
    logger.info(f">>>>>>> Stage {STAGE} completed <<<<<<<")

except Exception as e:
    logger.exception(e)
    raise e