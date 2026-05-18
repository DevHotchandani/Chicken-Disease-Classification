from src.cnnClassifier.config.configuration import ConfigurationManager
from src.cnnClassifier.components.data_ingestion import DataIngestion
from src.cnnClassifier.components.prepare_base_model import PrepareBaseModel
from src.cnnClassifier.components.training import Training
from src.cnnClassifier.components.evaluation import Evaluation

try:
    config = ConfigurationManager()

    data_ingestion_config = config.get_data_ingestion_config()
    data_ingestion = DataIngestion(config=data_ingestion_config)
    data_ingestion.download_file()
    data_ingestion.extract_zip_file()

    prepare_base_model_config = config.get_prepare_base_model_config()
    prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
    prepare_base_model.get_base_model()
    prepare_base_model.update_base_model()

    training_config = config.get_training_config()
    training = Training(config=training_config)
    training.get_base_model()
    training.train_valid_generator()
    training.train()


    evaluation_config = config.get_evaluation_config()
    evaluation = Evaluation(config=evaluation_config)
    evaluation.valid_generator()
    evaluation.evaluation()
    evaluation.save_score()

except Exception as e:
    raise e