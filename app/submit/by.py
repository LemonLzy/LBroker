from flask import current_app, url_for, jsonify

from app.fakes.fakes import fake
from app.params.params import IndividualReq
from app.submit.submit import BaseSubmit
from app.utils.const.const import Broker


class BYSubmit(BaseSubmit):
    def __init__(self, req: IndividualReq):
        super().__init__(Broker.BY, req)

    def basic_info(self):
        basic_req = {
            "birth": fake.date(),
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "middle_name": fake.user_name(),
            "nation_info": fake.country(),
            "sex": fake.random_int(0, 1)
        }
        with current_app.test_request_context():
            # 生成路由的 URL
            url = url_for("apis.mock_rsp", req="basic_info")
            # 使用 requests 发送 POST 请求
            basic_rsp = self.session.post(f"http://127.0.0.1:5000{url}", json=basic_req)
        return basic_rsp.json()
