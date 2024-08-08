
from tests.testbase import sync_playwright,get_bearer_header,verify_name_in_response, json,SUT,urlUsers
def test_list(playwright: sync_playwright):
    query_params = {
        "page": "1"
    }
    context = playwright.request.new_context(base_url= SUT)
    res = context.get(url=urlUsers, params=query_params, headers=get_bearer_header())
    resJson = res.json()
    name= resJson[0].get("name")
    verify_name_in_response(resJson, name)
    assert res.status == 200
    assert res.status_text == "OK"
  
   
        