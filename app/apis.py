from app.params.params import BaseRsp, IndividualReq
from app.submit.by import BYSubmit
from app.utils.const.const import Broker
from flask import Blueprint, jsonify, Response

apis = Blueprint('apis', __name__)


@apis.route("/individual", methods=["POST"])
def individual():
    req = IndividualReq(
        method="individual",
        attribution=Broker.BY,
        account_status=1,
        broker=Broker.BY,
        sig=None,
    )
    rsp = BaseRsp(code=0, msg="Success", data=BYSubmit(req).submit())
    return jsonify(rsp)


@apis.route("/mock_rsp/<path:req>", methods=["POST"])
def mock_rsp(req: str) -> Response:
    rsp = BaseRsp(code=0, msg="Success", data=req)
    return jsonify(rsp)


@apis.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"
