class TestApiData():
    def __init__(self, url, method, payload, response):
        self.url = url
        self.method = method
        self.payload = payload
        self.response = response


testin = TestApiData(url='www.auth_api.info/admin/company/208/branches', method='Post',
                     payload='company_name, company_number, company_internal_id', response={'info': 'information',
                                                                                            'id': 77,
                                                                                            'date': '20.02.2012',
                                                                                            'time': '11:27'})
