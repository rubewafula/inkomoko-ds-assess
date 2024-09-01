try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser  # ver. < 3.0

# instantiate
class Config:
    CONF_FILE ='./configs.ini'

    def __init__(self):
        self.config = ConfigParser()
        self.config.read(self.CONF_FILE)

    def get_config(self, section, key):
        return self.config.get(section, key)

