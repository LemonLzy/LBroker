from flask import current_app, url_for

from app.fakes.fakes import fake
from app.params.params import IndividualReq
from app.submit.submit import BaseSubmit
from app.utils.const.const import Broker
from app.utils.rsp import rsp_success


class HKSubmit(BaseSubmit):
    def __init__(self, req: IndividualReq):
        super().__init__(Broker.HK, req)

    def basic_info(self):
        basic_req = {
            "birth": fake.date(),
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "middle_name": fake.user_name(),
            "nation_info": fake.country(),
            "sex": fake.random_int(0, 1),
            "phone": fake.phone_number(),
            "email": fake.email(),
            "id_type": fake.random_int(0, 1),
            "id_number": fake.random_int(100000000000000000, 999999999999999999)
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
            "suburb": fake.street_suffix(),
            "zipcode": fake.postcode(),
            "address_type": fake.random_int(0, 1)
        }

        # 请求本地的mock接口，伪造返回成功
        with current_app.test_request_context():
            # 生成路由的 URL
            url = url_for("apis.mock_rsp", req="address_info")
            # 使用 requests 发送 POST 请求
            address_rsp = self.session.post(f"http://127.0.0.1:5000{url}", json=address_req)
        return address_rsp.json()

    def work_info(self):
        work_req = {
            "company_address": fake.street_address(),
            "company_country": fake.country(),
            "company_name": fake.company(),
            "company_phone": fake.phone_number(),
            "company_type": fake.random_int(0, 1),
            "job_title": fake.job(),
            "office_phone": fake.phone_number()
        }

        # 请求本地的mock接口，伪造返回成功
        with current_app.test_request_context():
            # 生成路由的 URL
            url = url_for("apis.mock_rsp", req="work_info")
            # 使用 requests 发送 POST 请求
            work_rsp = self.session.post(f"http://127.0.0.1:5000{url}", json=work_req)
        return work_rsp.json()

    def tax_info(self):
        tax_req = {
            "tax_code": fake.random_int(1000000, 9999999),
            "tax_country": fake.country(),
            "tax_information": fake.paragraph(),
            "w8_nation_info": fake.country()
        }

        # 请求本地的mock接口，伪造返回成功
        with current_app.test_request_context():
            # 生成路由的 URL
            url = url_for("apis.mock_rsp", req="tax_info")
            # 使用 requests 发送 POST 请求
            tax_rsp = self.session.post(f"http://127.0.0.1:5000{url}", json=tax_req)
        return tax_rsp.json()

    def disclosure_info(self):
        disclosure_req = {
            "setup_type": 1,
            "finish_info": fake.random_int(1, 99)
        }

        # 请求本地的mock接口，伪造返回成功
        with current_app.test_request_context():
            # 生成路由的 URL
            url = url_for("apis.mock_rsp", req="disclosure_info")
            # 使用 requests 发送 POST 请求
            disclosure_rsp = self.session.post(f"http://127.0.0.1:5000{url}", json=disclosure_req)
        return disclosure_rsp.json()

    def cert_info(self):
        cert_req = {
            "address_proof": fake.image_url(),
            "id_card": fake.image_url()
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
        work_rsp = self.work_info()
        disclosure_rsp = self.disclosure_info()
        cert_rsp = self.cert_info()

        submit_rsp = {
            "basic_rsp": basic_rsp.get("data"),
            "address_rsp": address_rsp.get("data"),
            "tax_rsp": tax_rsp.get("data"),
            "work_rsp": work_rsp.get("data"),
            "disclosure_rsp": disclosure_rsp.get("data"),
            "cert_rsp": cert_rsp.get("data")
        }

        return rsp_success(submit_rsp)
