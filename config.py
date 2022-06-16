OPENAI_API_KEY = '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'

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