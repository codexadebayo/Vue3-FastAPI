from pydantic_settings import BaseSettings  # Import BaseSettings from pydantic_settings


# class User(BaseSettings):
#     strDATABASE_PASSWORD:str
#     strDATABASE_USERNAME:str
#     strDATABASE_NAME:str
#     # strSECRET_KEY:str
#     strDATABASE_HOSTNAME:str
#    
#     

#     class Config:
#         env_file =".env"




# settings = User()



class User(BaseSettings):
    DATABASE_PASSWORD: str
    DATABASE_USERNAME: str = "postgres"
    DATABASE_NAME: str = "diadem"
    DATABASE_HOSTNAME: str = "localhost"
    # intACCESS_TOKEN_EXPIRE_MINUTES: int
    # strDATABASE_PORT: str
    # strALGORITHM: str
    # strSECRET_KEY:str

    class Config:
        env_file = ".env"