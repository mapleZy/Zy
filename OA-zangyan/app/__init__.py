#工厂函数
from flask import Flask
from app.config import config
from app.views.blueprint_one_recharge import bp
from app.models import db
from app.views.blueprint_two_income import bp_two
from app.views.blueprint_three_cost import bp_three
from app.views.blueprint_PM import bp_PM
#创建工厂函数
def create_app(config_name):
    #创建app实例
    app = Flask(__name__)#初始化配置
    if config_name not in config:
        config_name = 'default'
    app.config.from_object(config[config_name])
    db.init_app(app)
    app.register_blueprint(bp)
    app.register_blueprint(bp_two)
    app.register_blueprint(bp_three)
    app.register_blueprint(bp_PM)
    app.app_context().push()
    return app