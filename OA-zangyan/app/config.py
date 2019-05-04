import os

#配置环境路径
base_dir = os.path.dirname(__file__)

class Config:
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopConfig:
    SQLALCHEMY_DATABASE_URI =  "sqlite:///"+os.path.join(base_dir, "oa-dev.sqlite")

class ProductConfig:
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(base_dir, "oa.sqlite")


config= {
    "develop":DevelopConfig,
    "product":ProductConfig,
    "default":DevelopConfig,
}

