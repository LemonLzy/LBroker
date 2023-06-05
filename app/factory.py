from flask import Flask

from app.apis import apis


def create_app():
    app = Flask(__name__)

    # 注册 API 蓝图
    app.register_blueprint(apis)

    return app
