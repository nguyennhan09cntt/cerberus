import os
import json
from underthesea import word_sent

class Utils:
  def get_full_path(self, file):
    HERE = os.path.abspath(os.path.dirname(__file__))
    ROOT = os.path.dirname(HERE)
    return os.path.join(ROOT, file)

  def process_data_json(self, input_file, out_file):
    with open(input_file) as data_file:
      data = json.load(data_file)

    train=[]
    for element in data:
      element["text"] = word_sent(element["text"], format="text").lower()

    with open(out_file, 'w', encoding='utf-8') as outfile:
      json.dump(data, outfile, ensure_ascii=False)