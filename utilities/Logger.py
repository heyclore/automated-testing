import inspect
import time
import logging

class Logger:

    def __getattribute__(self, name):
        returned = object.__getattribute__(self, name)
        if inspect.isfunction(returned) or inspect.ismethod(returned):
            time.sleep(0.1)
            logging.getLogger(__name__).info(name)
        return returned
