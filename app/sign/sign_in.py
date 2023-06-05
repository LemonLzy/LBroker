from enum import Enum

import requests
from retrying import retry

from app.fakes.metadata import SignInRsp
from app.logger.logger import l_log
from app.utils.const.const import Broker


class Source(str, Enum):
    USER = "USER"
    STAFF = "STAFF"
    COMPANY = "COMPANY"


class SignInUrl(str, Enum):
    """
    券商登录URL
    """
    BY = "https://lemonlzy.cn/sign_in/by"
    CG = "https://lemonlzy.cn/sign_in/cg"
    CR = "https://lemonlzy.cn/sign_in/cr"
    US = "https://lemonlzy.cn/sign_in/us"
    JP = "https://lemonlzy.cn/sign_in/jp"
    HK = "https://lemonlzy.cn/sign_in/hk"

    @classmethod
    def get_url(cls, broker: Broker) -> str:
        return cls[broker.name].value


class BaseSignIn:
    def __init__(self, broker: Broker):
        self.url = SignInUrl.get_url(broker)
        # 创建HTTP连接池
        self.s = requests.Session()
        self.s.verify = False

    @retry(wait_random_min=2000, wait_random_max=4000, stop_max_attempt_number=10)
    def user_sign_in(self):
        """
        这里实现具体的用户登录逻辑，此处用faker数据返回登录成功后的session
        """
        l_log.debug(f"登录链接：{self.url}, 登录成功, session：{self.s}")
        return SignInRsp()

    @retry(wait_random_min=2000, wait_random_max=4000, stop_max_attempt_number=10)
    def company_sign_in(self):
        """
        这里实现具体的公司登录逻辑，此处用faker数据返回登录成功后的session
        """
        l_log.debug(f"登录链接：{self.url}, 登录成功, session：{self.s}")
        return SignInRsp()

    @retry(wait_random_min=2000, wait_random_max=4000, stop_max_attempt_number=10)
    def staff_sign_in(self):
        """
        这里实现具体的客服登录逻辑，此处用faker数据返回登录成功后的session
        """
        l_log.debug(f"登录链接：{self.url}, 登录成功, session：{self.s}")
        return SignInRsp()


if __name__ == '__main__':
    print(BaseSignIn(Broker.US).user_sign_in())
