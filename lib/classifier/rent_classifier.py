import os
import json
import sys
sys.path.insert(0, os.path.dirname(__file__) + '/..')

from underthesea import word_sent
from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob
from lib.classifier.base_classifier import CerberusBaseClassifier
from lib.utils import Utils

JSON_FILE = Utils().get_full_path("data/training/rent.json")

class CerberusRentClassifier(CerberusBaseClassifier):

  def __init__(self):
    print("initialized CerberusRent")
    with open(JSON_FILE) as data_file:
      self.classifier = NaiveBayesClassifier(data_file, format="json")

