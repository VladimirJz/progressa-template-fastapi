from pydantic_settings import BaseSettings,SettingsConfigDict
from functools import lru_cache

class AppSettings(BaseSettings):
    program_name:str='safi.core.engine'
    dbhost:str
    dbport:int
    dbuser:str
    dbpassword:str
    dbcore:str
    dbaddons:str
    
    model_config = SettingsConfigDict(env_file='.env')


@lru_cache
def get_db_settings()->dict:
    db_settings=AppSettings().model_dump()
    return db_settings

