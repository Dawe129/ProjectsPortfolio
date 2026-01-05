import oracledb
import configparser
import os

class BaseDAO:
    def __init__(self):
        self.config_path = os.path.join(os.path.dirname(__file__), '..', '..', 'config', 'database.ini')

    def connect(self):
        config = configparser.ConfigParser()
        config.read(self.config_path)
        dsn = oracledb.makedsn(
            config['DEFAULT']['host'],
            int(config['DEFAULT']['port']),
            service_name=config['DEFAULT']['service_name']
        )
        conn = oracledb.connect(
            user=config['DEFAULT']['user'],
            password=config['DEFAULT']['password'],
            dsn=dsn
        )
        return conn