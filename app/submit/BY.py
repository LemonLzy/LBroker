from app.fakes.fakes import fake
from app.params.params import IndividualReq
from app.submit.submit import BaseSubmit
from app.utils.const.const import Broker


class BYSubmit(BaseSubmit):
    def __init__(self, req: IndividualReq):
        super().__init__(Broker.BY, req)

    def basic_info(self):
        basic = {
            "birth": fake.date(),
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "middle_name": fake.user_name(),
            "nation_info": fake.country(),
            "sex": fake.random_int(0, 1)
        }
        self.session.post("http://www.baidu.com", json=basic)
        return basic
