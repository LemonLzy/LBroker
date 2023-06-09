from app.audit.entry import AuditEntry
from app.logger.logger import l_log
from app.params.params import IndividualReq, deserialize, SearchReq
from app.search.search import Search
from app.submit.entry import SubmitEntry
from app.utils.rsp import rsp_error


class Trans:
    @staticmethod
    def transport(req: dict):
        match req["method"]:
            # 个人户
            case "Individual":
                individual_req = deserialize(req, IndividualReq)
                submit_rsp = SubmitEntry().submit(individual_req)
                if submit_rsp.code != 0:
                    l_log.error(f"submit error: {submit_rsp.msg}")
                    return rsp_error(f"submit error: {submit_rsp.msg}")

                audit_rsp = AuditEntry().audit(individual_req)
                if audit_rsp.code != 0:
                    l_log.error(f"audit error: {audit_rsp.msg}")
                    return rsp_error(f"audit error: {audit_rsp.msg}")
                return audit_rsp
            # 搜索
            case "Search":
                search_req = deserialize(req, SearchReq)
                search_rsp = Search(search_req).search()
                if search_rsp.code != 0:
                    l_log.error(f"search error: {search_rsp.msg}")
                    return rsp_error(f"search error: {search_rsp.msg}")
                return search_rsp
