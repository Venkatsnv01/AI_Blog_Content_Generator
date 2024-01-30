OPENAI_API_KEY = ''

class Config(object):
    DEBUG = True
    TESTING =False

class DevelopmentConfig(Config):
    SECRET_KEY = "this-is-my-api"

config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig



}
