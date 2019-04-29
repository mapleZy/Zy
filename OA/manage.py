from flask import Flask
from flask_script import Manager
from flask_migrate import MigrateCommand,Migrate
import os
from models import db

app = Flask(__name__)

manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

#配置环境路径
base_dir = os.path.abspath(os.path.dirname(__file__))
database_uri = 'sqlite:///' + os.path.join(base_dir, 'data.sqlite')
app.config['SQLALCHEMY_DATABASE_URI'] = database_uri

#设置自动提交
app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


@app.route('/')
def index():
    return 'hello'

if __name__ == '__main__':
    manager.run()
