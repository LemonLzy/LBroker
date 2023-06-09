from typing import Any

from app.params.params import BaseRsp


def rsp_success(data: Any):
    return BaseRsp(code=0, msg="Success", data=data)


def rsp_error(msg: str):
    return BaseRsp(code=1001, msg=msg, data={})
