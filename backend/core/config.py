import os
from pathlib import Path

from dotenv import load_dotenv

ENV_PATH = Path('backend') / '.env'

load_dotenv(dotenv_path=ENV_PATH)


class Settings:
    PROJECT_NAME: str = 'Job Board'
    PROJECT_VERSION: str = '1.0.0'

    # DB settings
    POSTGRES_USER: str = os.getenv('POSTGRES_USER')
    POSTGRES_PASSWORD: str = os.getenv('POSTGRES_PASSWORD')
    POSTGRES_SERVER: str = os.getenv('POSTGRES_SERVER')
    POSTGRES_PORT: str = os.getenv('POSTGRES_PORT')
    POSTGRES_DB: str = os.getenv('POSTGRES_DB', 'tdd')
    DATABASE_URL: str = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}'


settings = Settings()
