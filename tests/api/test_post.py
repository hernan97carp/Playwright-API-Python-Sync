
from tests.testbase import get_bearer_header,createNewUser, sync_playwright,SUT,urlUsers

def test_post(playwright: sync_playwright):
    data = createNewUser()
    context = playwright.request.new_context(base_url= SUT)
    res = context.post(url=urlUsers, headers= get_bearer_header(), data = data)
    resJson= res.json()
    assert res.status == 201 
    assert res.status_text == "Created" 
    assert res.ok
    assert resJson["name"] == data["name"]
    assert resJson["email"] == data["email"]
    assert resJson["gender"] == data["gender"]
    assert resJson["status"] == data["status"]
    assert res.headers["content-type"] == "application/json; charset=utf-8"
    
    