from flask import current_app, url_for

from app.fakes.fakes import fake
from app.params.params import IndividualReq
from app.submit.submit import BaseSubmit
from app.utils.const.const import Broker


class JPSubmit(BaseSubmit):
    def __init__(self, req: IndividualReq):
        super().__init__(Broker.JP, req)

    def basic_info(self):
        basic_req = {
            "birth": fake.date(),
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "middle_name": fake.user_name(),
            "first_name_kanji": fake.first_name(),
            "last_name_kanji": fake.last_name(),
            "middle_name_kanji": fake.user_name(),
            "first_name_kana": fake.first_name(),
            "last_name_kana": fake.last_name(),
            "middle_name_kana": fake.user_name(),
            "nation_info": fake.country(),
            "sex": fake.random_int(0, 1)
        }

        # 请求本地的mock接口，伪造返回成功
        with current_app.test_request_context():
            # 生成路由的 URL
            url = url_for("apis.mock_rsp", req="basic_info")
            # 使用 requests 发送 POST 请求
            basic_rsp = self.session.post(f"http://127.0.0.1:5000{url}", json=basic_req)
        return basic_rsp.json()

    def address_info(self):
        address_req = {
            "address_country": fake.country(),
            "city": fake.city(),
            "street": fake.street_name(),
            "line1": fake.building_number(),
            "line2": fake.street_suffix(),
            "zipcode": fake.postcode()
        }

        # 请求本地的mock接口，伪造返回成功
        with current_app.test_request_context():
            # 生成路由的 URL
            url = url_for("apis.mock_rsp", req="address_info")
            # 使用 requests 发送 POST 请求
            address_rsp = self.session.post(f"http://127.0.0.1:5000{url}", json=address_req)
        return address_rsp.json()

    def question_info(self):
        question_req = {
            "annual_income": fake.random_int(10, 99),
            "invest_experience": fake.random_digit(),
            "position": fake.job(),
            "business": fake.company(),
        }

        # 请求本地的mock接口，伪造返回成功
        with current_app.test_request_context():
            # 生成路由的 URL
            url = url_for("apis.mock_rsp", req="question_info")
            # 使用 requests 发送 POST 请求
            question_rsp = self.session.post(f"http://127.0.0.1:5000{url}", json=question_req)
        return question_rsp.json()

    def disclosure_info(self):
        disclosure_req = {
            "risk_no": fake.port_number(),
            "lang": fake.language_code()
        }

        # 请求本地的mock接口，伪造返回成功
        with current_app.test_request_context():
            # 生成路由的 URL
            url = url_for("apis.mock_rsp", req="disclosure_info")
            # 使用 requests 发送 POST 请求
            disclosure_rsp = self.session.post(f"http://127.0.0.1:5000{url}", json=disclosure_req)
        return disclosure_rsp.json()

    def my_number_info(self):
        my_number_req = {
            "file_name": fake.file_name(),
            "space_id": fake.iana_id()
        }

        # 请求本地的mock接口，伪造返回成功
        with current_app.test_request_context():
            # 生成路由的 URL
            url = url_for("apis.mock_rsp", req="my_number_info")
            # 使用 requests 发送 POST 请求
            my_number_rsp = self.session.post(f"http://127.0.0.1:5000{url}", json=my_number_req)
        return my_number_rsp.json()

    def cert_info(self):
        cert_req = {
            "doc_type": fake.random_int(1, 99),
            "front": fake.image_url(),
            "back": fake.image_url(),
            "tilted": fake.image_url(),
            "validate": fake.date()
        }

        # 请求本地的mock接口，伪造返回成功
        with current_app.test_request_context():
            # 生成路由的 URL
            url = url_for("apis.mock_rsp", req="cert_info")
            # 使用 requests 发送 POST 请求
            cert_rsp = self.session.post(f"http://127.0.0.1:5000{url}", json=cert_req)
        return cert_rsp.json()

    def submit(self):
        basic_rsp = self.basic_info()
        address_rsp = self.address_info()
        tax_rsp = self.tax_info()
        question_rsp = self.question_info()
        disclosure_rsp = self.disclosure_info()
        my_number_rsp = self.my_number_info()
        cert_rsp = self.cert_info()

        submit_rsp = {
            "basic_rsp": basic_rsp.get("data"),
            "address_rsp": address_rsp.get("data"),
            "tax_rsp": tax_rsp.get("data"),
            "question_rsp": question_rsp.get("data"),
            "disclosure_rsp": disclosure_rsp.get("data"),
            "my_number_rsp": my_number_rsp.get("data"),
            "cert_rsp": cert_rsp.get("data")
        }

        return submit_rsp
