from kivy.network.urlrequest import UrlRequest
from putils import AppMiscError
#req = UrlRequest(url, on_success, on_redirect, on_failure, on_error,
#                 on_progress, req_body, req_headers, chunk_size,
#                 timeout, method, decode, debug, file_path, ca_file,
#                 verify)


class SQLData(object):
    __tmpresult = {}
    __success = False
    __errormsg = ''
    __failuremsg = ''
    view = ""

    def __init__(self, url):
        self.__url = url

    def __geterror(self, req, results):
        self.__success = False
        self.__errormsg = results['detail']

    def __getfailure(self, req, results):
        self.__success = False
        self.__failuremsg = results['detail']

    def __getdatos(self, req, results):
        self.__success = True
        if 'count' in results:
            if results['count'] > 0:
                self.__tmpresult = results['results']
            else:
                self.__tmpresult = {}
        else:
            self.__tmpresult = results

    def __testsuccess(self, re1, results):
        self.__success = True

    def __testerror(self, req, results):
        self.__success = False

    def __testfailure(self, req, results):
        self.__success = False

    def testapi(self):
        test = UrlRequest('{0}/estudiante.json'.format(self.__url), on_success=self.__testsuccess,
                          on_failure=self.__testfailure, on_error=self.__testerror)
        return self.__success

    def getapidata(self):
        self.__success = False
        self.__errormsg = ''
        self.__failuremsg = ''
        data = UrlRequest('{0}/{1}.json'.format(self.__url, self.view), on_success=self.__getdatos,
                          on_failure=self.__getfailure, on_error=self.__geterror)
        data.wait()
        if not self.__success:
            if self.__errormsg != '':
                __title = 'Url Error Message'
                __message = self.__errormsg
            elif self.__failuremsg != '':
                __title = 'Url Failure Message'
                __message = self.__failuremsg
            raise AppMiscError(__title, __message)
        return self.__tmpresult

    def getapidatafiltered(self):
        self.__success = False
        self.__errormsg = ''
        self.__failuremsg = ''
        data = UrlRequest('{0}/{1}&format=json'.format(self.__url, self.view), on_success=self.__getdatos,
                          on_failure=self.__getfailure, on_error=self.__geterror)
        data.wait()
        if not self.__success:
            if self.__errormsg != '':
                __title = 'Url Error Message'
                __message = self.__errormsg
            elif self.__failuremsg != '':
                __title = 'Url Failure Message'
                __message = self.__failuremsg
            raise AppMiscError(__title, __message)
        return self.__tmpresult