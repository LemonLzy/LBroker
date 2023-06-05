from app.params.params import IndividualReq
from app.utils.const.const import Broker


class Approve:

    def __init__(self, broker: Broker, req: IndividualReq):
        self.broker = broker
        self.task_id = self.get_task_id(req.uid)

    def approve_flow(self):
        self.level1_audit(self.task_id)
        self.level2_audit(self.task_id)
        self.ro_audit(self.task_id)
        self.accelerate()
        self.get_audit_result()

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
        pass
