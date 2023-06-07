from app.params.params import IndividualReq, deserialize, BaseRsp
from app.submit.entry import SubmitEntry


class Trans:
    @staticmethod
    def transport(req: dict):
        # 个人户
        match req["method"]:
            case "Individual":
                individual_req = deserialize(req, IndividualReq)
                return BaseRsp(code=0, msg="Success", data=SubmitEntry().submit(individual_req))
