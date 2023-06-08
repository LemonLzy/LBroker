from flask import current_app, url_for

from app.audit.audit import Audit
from app.fakes.fakes import fake
from app.params.params import IndividualReq
from app.utils.const.const import Broker
from app.utils.rsp import rsp_success


class HKAudit(Audit):
    def __init__(self, req: IndividualReq):
        super().__init__(Broker.HK, req)

    def audit_flow(self):
        level2_rsp = self.level2_audit(self.task_id)
        account_rsp = self.accelerate()
        get_audit_rsp = self.get_audit_result()

        audit_flow_rsp = {
            "level2_rsp": level2_rsp.get("data"),
            "account_rsp": account_rsp.get("data"),
            "get_audit_rsp": get_audit_rsp.get("data"),
            "broker": self.broker.value
        }
        return rsp_success(audit_flow_rsp)

    def get_audit_result(self):
        get_audit_req = {
            "task_id": self.task_id,
            "broker": self.broker
        }

        # 请求本地的mock接口，伪造返回成功
        with current_app.test_request_context():
            # 生成路由的 URL
            url = url_for("apis.mock_rsp", req="get_audit_result")
            # 使用 requests 发送 POST 请求
            get_audit_rsp = self.session.post(f"http://127.0.0.1:5000{url}", json=get_audit_req)
        return get_audit_rsp.json()

    def get_task_id(self, uid):
        return fake.random_int(10000, 999999)

    def level1_audit(self, task_id):
        """
        HK券商没有level1审核
        """
        pass

    def level2_audit(self, task_id):
        level2_req = {
            "task_id": self.task_id,
            "action": "Approve",
        }

        # 请求本地的mock接口，伪造返回成功
        with current_app.test_request_context():
            # 生成路由的 URL
            url = url_for("apis.mock_rsp", req="level1_audit")
            # 使用 requests 发送 POST 请求
            level2_rsp = self.session.post(f"http://127.0.0.1:5000{url}", json=level2_req)
        return level2_rsp.json()

    def ro_audit(self, task_id):
        """
        CR券商没有RO审核
        """
        pass

    def accelerate(self):
        accelerate_req = {
            "task_id": self.task_id,
            "action": "Accelerate",
        }

        # 请求本地的mock接口，伪造返回成功
        with current_app.test_request_context():
            # 生成路由的 URL
            url = url_for("apis.mock_rsp", req="level1_audit")
            # 使用 requests 发送 POST 请求
            accelerate_rsp = self.session.post(f"http://127.0.0.1:5000{url}", json=accelerate_req)
        return accelerate_rsp.json()
