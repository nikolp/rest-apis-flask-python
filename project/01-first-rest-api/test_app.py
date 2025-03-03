import pytest
# import unittest
import app

@pytest.fixture
def myapp():
    return app.app

@pytest.fixture
def myclient(myapp):
    return myapp.test_client()

def test_root(myclient):
    resp = myclient.get("/")
    assert resp.status_code == 404

def test_get_store(myclient):
    resp = myclient.get("/store")
    assert resp.status_code == 200
    data = resp.get_json()
    assert isinstance(data, dict)
    assert 'stores' in data
    assert isinstance(data['stores'], list) 
    st = data['stores'][0]
    assert st["name"] == "My Store" 

def test_post_store(myclient):
    resp = myclient.post("/store", json={'name': 'newstore'})
    assert resp.status_code == 201
    resp = myclient.get("/store")
    resp_dict = resp.json
    assert len(resp_dict['stores']) == 2
    # data = resp.get_json()
    # assert isinstance(data, dict)
    # print(data)
    # assert 'stores' in data
    # assert isinstance(data['stores'], list) 
    # st = data['stores'][0]
    # assert st["name"] == "My Store" 

# class MyTest(unittest.TestCase):
#     def setUp(self):
#         self.myapp = app.app
#         self.myclient = self.myapp.test_client()

#     def test_foo(self):
#         resp = self.myclient.get("/")
#         self.assertEqual(404, resp.status_code)

# if __name__ == '__main__':
#     unittest.main()


