import logging

class loggingDictionary(dict):
    def __setitem__(self, key, value):
        logging.info(f'setting{value}to{key}')
        super().__setitem__(key, value)
logging.basicConfig(filename='logs\\demo83.log',
                    level=logging.INFO)
l1 = loggingDictionary()
l1['ken']='ios'
l1['frank']='oracle'
print(l1)