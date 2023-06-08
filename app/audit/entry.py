from app.params.params import IndividualReq
from app.utils.const.const import Broker


class AuditEntry:
    @staticmethod
    def audit(req: IndividualReq):
        """
        审批主方法
        """
        match req.broker:
            case Broker.JP:
                from app.audit.jp_audit import JPAudit
                return JPAudit(req).audit_flow()
            case Broker.HK:
                from app.audit.hk_audit import HKAudit
                return HKAudit(req).audit_flow()
            case Broker.US:
                from app.audit.us_audit import USAudit
                return USAudit(req).audit_flow()
            case Broker.BY:
                from app.audit.by_audit import BYAudit
                return BYAudit(req).audit_flow()
            case Broker.CG:
                from app.audit.cg_audit import CGAudit
                return CGAudit(req).audit_flow()
            case Broker.CR:
                from app.audit.cr_audit import CRAudit
                return CRAudit(req).audit_flow()
            case _:
                raise Exception("Broker not found.")
