'''Preprocessing Data File'''
import logging
# import pandas as pd

class Preprocessing:
    '''Class for preprocessing data before sending to model'''
    def __init__(self) -> None:
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
