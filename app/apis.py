from flask_cors import CORS

from app.audit.by_audit import BYAudit
from app.params.params import BaseRsp, IndividualReq
from app.submit.by_submit import BYSubmit
from app.utils.const.const import Broker
from flask import Blueprint, jsonify, Response

apis = Blueprint('apis', __name__)
CORS(apis, resources={r"/*": {"origins": "*"}})


@apis.route("/individual", methods=["POST"])
def individual():
    req = IndividualReq(
        method="individual",
        attribution=Broker.BY,
        account_status=1,
        broker=Broker.BY,
        sig=None,
    )
    # 提交开户申请
    rsp = BaseRsp(code=0, msg="Success", data=BYSubmit(req).submit())
    # 审批开户申请
    rsp = BaseRsp(code=0, msg="Success", data=BYAudit(req).audit_flow())
    return jsonify(rsp)


@apis.route("/mock_rsp/<path:req>", methods=["POST"])
def mock_rsp(req: str) -> Response:
    rsp = BaseRsp(code=0, msg="Success", data=req)
    return jsonify(rsp)


@apis.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"
