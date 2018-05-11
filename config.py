class Config(object):
    pass

class ProdConfig(Config):
    pass

class DevConfig(Config):
    debug = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
