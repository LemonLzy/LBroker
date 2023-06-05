import requests

from app.params.params import IndividualReq
from app.utils.const.const import Broker


class BaseSubmit:
    def __init__(self, broker: Broker, req: IndividualReq):
        self.uid = req.uid
        self.session = requests.session()
        self.broker = broker
        self.account_type = req.open_account

    def basic_info(self):
        raise Exception("You need to implement the basic_info method.")

    def address_info(self):
        raise Exception("You need to implement the address_info method.")

    def tax_info(self):
        raise Exception("You need to implement the tax_info method.")

    def question_info(self):
        raise Exception("You need to implement the question_info method.")

    def disclosure_info(self):
        raise Exception("You need to implement the disclosure_info method.")

    def cert_info(self):
        raise Exception("You need to implement the cert_info method.")

    def submit(self):
        raise Exception("You need to implement the submit method.")
