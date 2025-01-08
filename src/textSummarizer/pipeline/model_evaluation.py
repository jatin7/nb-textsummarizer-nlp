from textSummarizer.config.configuration import ConfiguartionManager
from textSummarizer.components.model_evaluation import Model_Evaluation
from textSummarizer.logging import logger

class ModelEvaluationPipeline:
    def __init__(self):
        pass
    def main(self):
        config = ConfiguartionManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = Model_Evaluation(config=model_evaluation_config)
        model_evaluation.evaluate()