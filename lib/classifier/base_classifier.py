#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob
from underthesea import word_sent
from lib.singleton import Singleton

class CerberusBaseClassifier(metaclass=Singleton):
  def singleton_init(self):
    print("initialized base")

  def classify(self, advertisement):
    print("classify")
    print(advertisement)
    return self.classifier.classify(advertisement)

  def accuracy(self, advertisement):
    print("accuracy")
    return "{0}".format(self.classifier.accuracy(advertisement))

