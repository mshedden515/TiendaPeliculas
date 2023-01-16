class Config:
    SECRET_KEY = 'M4t3Ofel1p3515'


class DevelopmentConfig(Config):
    DEBUG = True


config = {
    "development": DevelopmentConfig,
    "default": DevelopmentConfig
    }
    
    
