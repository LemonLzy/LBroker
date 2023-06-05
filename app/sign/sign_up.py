from enum import Enum

from app.fakes.metadata import SignUpRsp
from app.logger.logger import l_log
from app.utils.const.const import Broker
from app.utils.info.info import gen_email, gen_11bit_phone


class SignUpUrl(str, Enum):
    """
    券商注册URL
    """
    BY = "https://lemonlzy.cn/sign_up/by"
    CG = "https://lemonlzy.cn/sign_up/cg"
    CR = "https://lemonlzy.cn/sign_up/cr"
    US = "https://lemonlzy.cn/sign_up/us"
    JP = "https://lemonlzy.cn/sign_up/jp"
    HK = "https://lemonlzy.cn/sign_up/hk"

    @classmethod
    def get_url(cls, broker: Broker) -> str:
        return cls[broker.name].value


class BaseSignUp:
    def __init__(self, broker: Broker):
        self.url = SignUpUrl.get_url(broker)

    def sign_up_by_email(self):
        """
        这里实现具体的邮箱注册逻辑，此处用faker数据返回
        """
        email = gen_email()
        l_log.debug(f"注册链接：{self.url}, 注册成功, email：{email}")
        return SignUpRsp()

    def sign_up_by_phone(self):
        """
        这里实现具体的手机注册逻辑，此处用faker数据返回
        """
        phone = gen_11bit_phone()
        l_log.debug(f"注册链接：{self.url}, 注册成功, phone：{phone}")
        return SignUpRsp()


if __name__ == '__main__':
    print(BaseSignUp(Broker.US).sign_up_by_email())
