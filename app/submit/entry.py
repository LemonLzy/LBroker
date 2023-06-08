from app.params.params import IndividualReq
from app.utils.const.const import Broker


class SubmitEntry:
    @staticmethod
    def submit(req: IndividualReq):
        """
        提交主方法
        """
        match req.broker:
            case Broker.JP:
                from app.submit.jp_submit import JPSubmit
                return JPSubmit(req).submit()
            case Broker.HK:
                from app.submit.hk_submit import HKSubmit
                return HKSubmit(req).submit()
            case Broker.US:
                from app.submit.us_submit import USSubmit
                return USSubmit(req).submit()
            case Broker.BY:
                from app.submit.by_submit import BYSubmit
                return BYSubmit(req).submit()
            case Broker.CG:
                from app.submit.cg_submit import CGSubmit
                return CGSubmit(req).submit()
            case Broker.CR:
                from app.submit.cr_submit import CRSubmit
                return CRSubmit(req).submit()
            case _:
                raise Exception("Broker not found.")