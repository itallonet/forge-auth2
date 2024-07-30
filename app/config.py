import os

class Config:
    DB_NAME = os.getenv('DB_NAME', 'dbname')
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_USERNAME = os.getenv('DB_USERNAME', 'user')
    DB_PASSWORD = os.getenv('DB_PASSWORD', 'password')
    DB_PORT = os.getenv('DB_PORT', '5432')
    
    print(f'postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

    SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False