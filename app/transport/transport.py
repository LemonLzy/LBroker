from app.audit.entry import AuditEntry
from app.logger.logger import l_log
from app.params.params import IndividualReq, deserialize
from app.submit.entry import SubmitEntry
from app.utils.rsp import rsp_error


class Trans:
    @staticmethod
    def transport(req: dict):
        # 个人户
        match req["method"]:
            case "Individual":
                individual_req = deserialize(req, IndividualReq)
                submit_rsp = SubmitEntry().submit(individual_req)
                if submit_rsp.code != 0:
                    l_log.error(f"submit error: {submit_rsp.msg}")
                    return rsp_error(submit_rsp)

                audit_rsp = AuditEntry().audit(individual_req)
                if audit_rsp.code != 0:
                    l_log.error(f"audit error: {audit_rsp.msg}")
                    return rsp_error(audit_rsp)
                return audit_rsp
