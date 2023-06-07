from flask import current_app, url_for

from app.fakes.fakes import fake
from app.params.params import IndividualReq
from app.submit.submit import BaseSubmit
from app.utils.const.const import Broker


class CGSubmit(BaseSubmit):
    def __init__(self, req: IndividualReq):
        super().__init__(Broker.CG, req)

    def basic_info(self):
        basic_req = {
            "birth": fake.date(),
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "middle_name": fake.user_name(),
            "first_name_cn": fake.first_name(),
            "middle_name_cn": fake.last_name(),
            "last_name_cn": fake.user_name(),
            "nation_info": fake.country()
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
            "state": fake.city(),
            "street": fake.street_name(),
            "street_number": fake.building_number(),
            "zipcode": fake.postcode()
        }

        # 请求本地的mock接口，伪造返回成功
        with current_app.test_request_context():
            # 生成路由的 URL
            url = url_for("apis.mock_rsp", req="address_info")
            # 使用 requests 发送 POST 请求
            address_rsp = self.session.post(f"http://127.0.0.1:5000{url}", json=address_req)
        return address_rsp.json()

    def tax_info(self):
        tax_req = {
            "tax_code": fake.random_int(1000000, 9999999),
            "tax_country": fake.country(),
            "crs_code": fake.country_code(),
            "crs_country": fake.country()
        }

        # 请求本地的mock接口，伪造返回成功
        with current_app.test_request_context():
            # 生成路由的 URL
            url = url_for("apis.mock_rsp", req="tax_info")
            # 使用 requests 发送 POST 请求
            tax_rsp = self.session.post(f"http://127.0.0.1:5000{url}", json=tax_req)
        return tax_rsp.json()

    def question_info(self):
        question_req = {
            "annual_income": fake.random_int(10, 99),
            "invest_experience": fake.random_digit(),
            "employee": fake.company(),
            "email": fake.company_email()
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
            "approve_agreement": 1,
            "cg_stock_disclosure": fake.random_int(1, 99),
            "us_stock_disclosure": fake.random_int(1, 99),
            "hk_stock_disclosure": fake.random_int(1, 99),
            "signature": fake.name()
        }

        # 请求本地的mock接口，伪造返回成功
        with current_app.test_request_context():
            # 生成路由的 URL
            url = url_for("apis.mock_rsp", req="disclosure_info")
            # 使用 requests 发送 POST 请求
            disclosure_rsp = self.session.post(f"http://127.0.0.1:5000{url}", json=disclosure_req)
        return disclosure_rsp.json()

    def submit(self):
        basic_rsp = self.basic_info()
        address_rsp = self.address_info()
        tax_rsp = self.tax_info()
        question_rsp = self.question_info()
        disclosure_rsp = self.disclosure_info()

        submit_rsp = {
            "basic_rsp": basic_rsp.get("data"),
            "address_rsp": address_rsp.get("data"),
            "tax_rsp": tax_rsp.get("data"),
            "question_rsp": question_rsp.get("data"),
            "disclosure_rsp": disclosure_rsp.get("data")
        }

        return submit_rsp
