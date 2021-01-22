# -*- coding: utf-8 -*-
import requests
class TestDemo():
    def setup_class(self):
        url1 = " https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        param = {
            "corpid":"ww25c8f6bf8deb47a1",
            "corpsecret":"UIzjlQgq5eQbLjWiGhKaTh7u3ZuJ1P57sYU-qYEY4nU"
        }
        r1 = requests.request(method="GET",url = url1,params = param)
        self.token = r1.json()['access_token']
        print(r1.json()['access_token'])
        assert r1.json()['errcode'] == 0
    def test_create_department(self):

        url1 = "https://qyapi.weixin.qq.com/cgi-bin/department/create"
        data = {
            "name": "广州研发中心2",
            "name_en": "RDGZ2",
            "parentid": 1,
            "order": 1,
            "id": 3}
        params = {
            "access_token":self.token
        }
        r1 = requests.request(method="POST", url=url1, params = params,json=data)
        print(r1.json())
        assert r1.json()["errcode"] == 0
    def test_updata_department(self):
        url2 = "https://qyapi.weixin.qq.com/cgi-bin/department/update"
        data1 ={
            "name": "广州研发中心",
            "name_en": "RDGZ2",
            "parentid": 1,
            "order": 1,
            "id": 1}
        params1 = {
            "access_token":self.token
        }
        r2 = requests.request(method="POST",url=url2,json = data1,params = params1)
        print(r2.json())
        assert r2.json()['errmsg'] == 'updated'
    def test_delete_department(self):
        url3 = "https://qyapi.weixin.qq.com/cgi-bin/department/delete"
        params2 = {
            "access_token": self.token,
            "id":3,

        }
        r3 = requests.request(method="GET",url = url3,params = params2)
        print(r3.json())

    def test_get_list(self):
        url4 = "https://qyapi.weixin.qq.com/cgi-bin/department/list"
        params3 = {
            "access_token":self.token
        }
        r4 = requests.request(method="GET",url =url4,params = params3)
        print(r4.json())