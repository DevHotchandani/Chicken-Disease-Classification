from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.evaluation import Evaluation


config = ConfigurationManager()
evaluation_config = config.get_evaluation_config()
evaluation = Evaluation(config=evaluation_config)
evaluation.valid_generator()
evaluation.evaluation()
evaluation.save_score()