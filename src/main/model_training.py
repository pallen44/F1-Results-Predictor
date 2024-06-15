'''Contains functions to train prediction model'''
import logging
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

class ModelTraining:
    '''Class to train model'''
    def __init__(self) -> None:
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        self.x_train = NotImplemented
        self.x_test = NotImplemented
        self.y_train = NotImplemented
        self.y_test = NotImplemented

    def feature_selector(self, race_data_df):
        '''Selects the features from dataframe'''
        x = race_data_df[['DriverNumber', 'Average_Position']]
        y = race_data_df['Position'].astype(int)
        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(x, y,
            test_size=0.2, random_state=42)

    def train_model(self, data_frame):
        '''Train RandomForestClassifier model'''
        self.feature_selector(data_frame)
        model = RandomForestClassifier(random_state=42)
        model.fit(self.x_train, self.y_train)
        y_pred = model.predict(self.x_test)
        accuracy = accuracy_score(self.y_test, y_pred)
        self.logger.info("Model accuracy: %d", accuracy)
        return model
