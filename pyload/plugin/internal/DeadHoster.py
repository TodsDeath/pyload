# -*- coding: utf-8 -*-

from pyload.plugin.Hoster import Hoster as _Hoster


class DeadHoster(_Hoster):
    __name__    = "DeadHoster"
    __type__    = "hoster"
    __version__ = "0.14"

    __pattern__ = r'^unmatchable$'

    __description__ = """Hoster is no longer available"""
    __license__     = "GPLv3"
    __authors__     = [("zoidberg", "zoidberg@mujmail.cz")]


    @classmethod
    def apiInfo(cls, url="", get={}, post={}):
        api = super(DeadHoster, self).apiInfo(url, get, post)
        api['status'] = 1
        return api


    def setup(self):
        self.pyfile.error = "Hoster is no longer available"
        self.offline()  #@TODO: self.offline("Hoster is no longer available")