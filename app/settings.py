from pydantic_settings import BaseSettings


# 設定モデルを定義
class Settings(BaseSettings):
    SECRET_KEY: str
    TMP_USER_NAME: str
    TMP_HASHED_PASSWORD: str
