from flask_script import Manager
from flask_migrate import MigrateCommand,Migrate
from app.models import db
from app import create_app

app = create_app('zy')

manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
