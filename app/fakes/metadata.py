from dataclasses import dataclass

import requests

from app.fakes.fakes import fake
from app.utils.const.const import Broker


@dataclass
class SignUpRsp:
    """
    注册功能的返回参数，使用faker包构造数据
    """
    uid: int = None
    pwd: str = None
    attr: Broker = None

    def __post_init__(self):
        self.uid = self.uid or fake.random_int(100000000, 999999999)
        self.pwd = self.pwd or fake.password()
        self.attr = self.attr or fake.random_element(Broker)

    def __repr__(self):
        return f"uid: {self.uid}, pwd: {self.pwd}, attribution: {self.attr}"


@dataclass
class SignInRsp:
    """
    登录功能的返回参数
    """
    sig: requests.sessions.Session = None

    def __post_init__(self):
        self.sig = requests.session()

    def __repr__(self):
        return f"sig: {self.sig}"


if __name__ == '__main__':
    s = SignUpRsp()
    print(s)
    s1 = SignInRsp()
    print(s1)
