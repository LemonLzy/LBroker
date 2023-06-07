from app.params.params import IndividualReq
from app.sign.entry import SignEntry
from app.sign.sign_in import Source
from app.utils.const.const import Broker


class Audit:

    def __init__(self, broker: Broker, req: IndividualReq):
        self.broker = broker
        self.task_id = self.get_task_id(req.uid)
        self.session = SignEntry().sign_in(broker, Source.STAFF)

    def audit_flow(self):
        level1_rsp = self.level1_audit(self.task_id)
        level2_rsp = self.level2_audit(self.task_id)
        ro_rsp = self.ro_audit(self.task_id)
        acc_rsp = self.accelerate()
        get_audit_rsp = self.get_audit_result()

        audit_flow_rsp = {
            "level1_rsp": level1_rsp.get("data"),
            "level2_rsp": level2_rsp.get("data"),
            "ro_rsp": ro_rsp.get("data"),
            "acc_rsp": acc_rsp.get("data"),
            "get_audit_rsp": get_audit_rsp.get("data")
        }
        return audit_flow_rsp

    def get_audit_result(self):
        raise Exception("You need to implement the get_audit_result method.")

    def get_task_id(self, uid):
        raise Exception("You need to implement the get_task_id method.")

    def level1_audit(self, task_id):
        raise Exception("You need to implement the level1_audit method.")

    def level2_audit(self, task_id):
        raise Exception("You need to implement the level2_audit method.")

    def ro_audit(self, task_id):
        raise Exception("You need to implement the ro_audit method.")

    def accelerate(self):
        raise Exception("You need to implement the accelerate method.")
