from app.fakes.metadata import SearchRsp
from app.logger.logger import l_log
from app.params.params import SearchReq, BaseRsp
from app.utils.rsp import rsp_success


class Search:
    def __init__(self, req: SearchReq):
        self.uid = req.uid

    def search(self) -> BaseRsp:
        l_log.debug(self.uid)
        search_rsp = [SearchRsp(), SearchRsp()]
        return rsp_success(search_rsp)
