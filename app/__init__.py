from flask import Flask  # 从flask包中导入Flask类
from config import Config  # 从config模块导入Config类

from flask_sqlalchemy import SQLAlchemy  # 丛包中导入类
from flask_migrate import Migrate

from flask_login import LoginManager

app = Flask(__name__)  # 将Flask类的实例 赋值给名为 app 的变量。这个实例成为app包的成员。
app.config.from_object(Config)

login = LoginManager(app)
login.login_view = 'login'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models  # 从app包中导入模块routes
