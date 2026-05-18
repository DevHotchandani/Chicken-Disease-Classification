from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.training import Training

config = ConfigurationManager()
training_config = config.get_training_config()
training = Training(config=training_config)
training.get_base_model()
training.train_valid_generator()
training.train()