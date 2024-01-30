from os import getenv

from dotenv import load_dotenv

load_dotenv()


class BaseConfiguration:
    SECRET_KEY = getenv("SECRET_KEY")


class DevelopmentConfiguration(BaseConfiguration):
    DEBUG = True


class ProductionConfiguration(BaseConfiguration):
    DEBUG = False
    JSON_SORT_KEYS = False


class TestingConfiguration(BaseConfiguration):
    DEBUG = False
    TESTING = True


CONFIGURATIONS = {
    "development": DevelopmentConfiguration,
    "production": ProductionConfiguration,
    "testing": TestingConfiguration
}
