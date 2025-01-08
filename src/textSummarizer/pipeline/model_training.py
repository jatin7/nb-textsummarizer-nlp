from textSummarizer.config.configuration import ConfiguartionManager
from textSummarizer.components.model_training import ModelTrainer
from textSummarizer.logging import logger

class ModelTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        config = ConfiguartionManager()
        model_trainer_config = config.get_model_training_config()
        model_trainer = ModelTrainer(config=model_trainer_config)
        model_trainer.train()