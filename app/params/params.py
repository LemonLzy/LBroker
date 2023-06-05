from dataclasses import dataclass, field
from typing import Optional, Type, TypeVar

import requests

from app.utils.const.const import Broker

T = TypeVar("T")


@dataclass
class BaseRsp:
    code: int
    msg: str
    data: dataclass


@dataclass
class Sig:
    session: requests.sessions.Session


@dataclass
class IndividualReq:
    method: str
    attribution: Broker
    account_status: int
    broker: Broker
    open_account: Optional[list] = field(default_factory=list)
    activate_account: Optional[list] = field(default_factory=list)
    sig: Optional[Sig] = dataclass
    nation_info: Optional[str] = "CN"
    uid: Optional[int] = 0
    pwd: Optional[str] = ""


@dataclass
class SearchReq:
    method: str
    uid: int


def deserialize(req: dict, req_class: Type[T]) -> T:
    if issubclass(req_class, IndividualReq):
        attribution = req.get("attribution")
        broker = req.get("broker")

        # 将券商字符串转为Broker枚举值
        if attribution is not None:
            req["attribution"] = Broker[attribution]
        if broker is not None:
            req["broker"] = Broker[broker]

    # 此处警告为引入泛型之后（为了IDE能正确提示属性），反序列化时产生的警告。不可根据警告提示，移除此传参
    return req_class(**req)
