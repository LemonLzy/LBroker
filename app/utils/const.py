from enum import Enum


class Broker(str, Enum):
    BY = "BY"
    CG = "CG"
    CR = "CR"
    US = "US"
    JP = "JP"
    HK = "HK"


class BrokerID(int, Enum):
    BY = 112
    CG = 178
    CR = 188
    US = 840
    JP = 392
    HK = 344

    @classmethod
    def get_broker_id(cls, broker: Broker) -> int:
        return BrokerID[f"{broker}"].value
