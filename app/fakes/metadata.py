import time
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


@dataclass
class SearchRsp:
    """
    搜索功能的返回参数
    """
    broker: Broker = None
    account_id: int = None
    market_id: int = None
    enable_market: list = None
    model: str = None
    kind: str = None
    opened_time: float = None
    closed_time: float = None

    def __post_init__(self):
        self.broker = fake.random_element(Broker)
        self.account_id = fake.random_int(10000000000, 99999999999)
        self.market_id = fake.random_int(1, 9)
        self.enable_market = fake.random_elements(
            elements=("US_STOCK", "HK_STOCK", "A_STOCK", "JP_STOCK", "SG_STOCK", "UK_STOCK", "DE_STOCK",
                      "FUND", "BOND", "FUTURES", "OPTION", "FOREX", "CRYPTO",),
            length=self.market_id, unique=True)
        self.model = fake.random_element(("fund_acc", "single_acc", "uni_acc"))
        self.kind = fake.random_element(("individual", "institution"))
        self.opened_time = time.mktime(fake.date_time_this_year().timetuple())
        self.closed_time = time.mktime(fake.date_time_this_year().timetuple())

    def __repr__(self):
        return f"broker: {self.broker}, account_id: {self.account_id}, market_id: {self.market_id}, " \
               f"enable_market: {self.enable_market}, model: {self.model}, kind: {self.kind}, " \
               f"opened_time: {self.opened_time}, closed_time: {self.closed_time}"


if __name__ == '__main__':
    s = SignUpRsp()
    print(s)
    s1 = SearchRsp()
    print(s1)
