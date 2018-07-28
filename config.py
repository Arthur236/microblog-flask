import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """
    Parent configuration class
    """
    DEBUG = False
    CSRF_ENABLED = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'gjOFUb9oVFDfCDmvdaFjLYm91bSOETnvgGfuJWnx'
    SQLALCHEMY_DATABASE_URI = \
        os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['your-email@example.com']


class DevelopmentConfig(Config):
    """
    Development configurations
    """
    DEBUG = True


class TestingConfig(Config):
    """
    Testing configurations, with a separate test database
    """
    TESTING = True
    SQLALCHEMY_DATABASE_URI = \
        os.environ.get('TEST_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    DEBUG = True


class StagingConfig(Config):
    """
    Staging configurations
    """
    DEBUG = True


class ProductionConfig(Config):
    """
    Production configurations
    """
    DEBUG = False
    TESTING = False


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
}
