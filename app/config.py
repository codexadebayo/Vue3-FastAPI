from pydantic_settings import BaseSettings  

class User(BaseSettings):
    DATABASE_PASSWORD: str
    DATABASE_USERNAME: str
    DATABASE_NAME: str
    DATABASE_HOSTNAME: str
    # intACCESS_TOKEN_EXPIRE_MINUTES: int
    # strDATABASE_PORT: str
    # strALGORITHM: str
    # strSECRET_KEY:str

    class Config:
        env_file = ".env"