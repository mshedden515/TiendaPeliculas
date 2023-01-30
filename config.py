class Config:
    SECRET_KEY = 'M4t3Ofel1p3515'


class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = '123456'
    MYSQL_DB = 'tienda'

config = {
    "development": DevelopmentConfig,
    "default": DevelopmentConfig
}
