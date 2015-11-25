from kivy.network.urlrequest import UrlRequest

#req = UrlRequest(url, on_success, on_redirect, on_failure, on_error,
#                 on_progress, req_body, req_headers, chunk_size,
#                 timeout, method, decode, debug, file_path, ca_file,
#                 verify)


class SQLData(object):
    __tmpresults = {}
    view = ""

    def __init__(self, url):
        self.__url = url

    def __geterror(self, req, results):
        print(results)

    def __getdatos(self, req, results):
        if results['count'] > 0:
            self.__tmpresult = results['results']
        else:
            self.__tmpresult = {}

    def getapidata(self):
        data = UrlRequest('{0}/{1}.json'.format(self.__url, self.view), on_success=self.__getdatos,
                                 on_failure=self.__geterror, on_error=self.__geterror)
        data.wait()

        return self.__tmpresult
