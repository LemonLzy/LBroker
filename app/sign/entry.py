from app.sign.sign_in import BaseSignIn, Source
from app.sign.sign_up import BaseSignUp
from app.utils.const.const import Broker


class SignEntry:
    @staticmethod
    def sign_in(broker: Broker, source: Source):
        """
        注册主方法
        """
        match source:
            case Source.USER:
                return BaseSignIn(broker).user_sign_in()
            case Source.STAFF:
                return BaseSignIn(broker).staff_sign_in()
            case Source.COMPANY:
                return BaseSignIn(broker).company_sign_in()

    @staticmethod
    def sign_up(broker: Broker):
        """
        注册主方法
        """
        if broker in [Broker.BY, Broker.CG, Broker.CR]:
            return BaseSignUp(broker).sign_up_by_email()
        else:
            return BaseSignUp(broker).sign_up_by_phone()
