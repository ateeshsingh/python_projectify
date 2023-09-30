
class BaseConfig(object):
    DATABASE_HOST = "mongodb+srv://dev:atch20615008@mflix.34yoj.mongodb.net/?retryWrites=true&w=majority"
    DATABASE = "projectify_database"


config_env = dict(development=BaseConfig, default=BaseConfig)
