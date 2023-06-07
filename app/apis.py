from flask_cors import CORS

from app.params.params import BaseRsp
from app.transport.transport import Trans
from flask import Blueprint, jsonify, Response, request

apis = Blueprint('apis', __name__)
CORS(apis, resources={r"/*": {"origins": "*"}})


@apis.route("/individual", methods=["POST"])
def individual():
    # 获取请求参数
    req = request.json
    # 给转发函数处理后续流程
    rsp = Trans().transport(req)
    return jsonify(rsp)


@apis.route("/mock_rsp/<path:req>", methods=["POST"])
def mock_rsp(req: str) -> Response:
    rsp = BaseRsp(code=0, msg="Success", data=req)
    return jsonify(rsp)


@apis.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"
