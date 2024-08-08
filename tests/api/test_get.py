from tests.testbase import get_bearer_header,sync_playwright,get_random_user_id,global_id,SUT,urlUsers
def test_get(playwright: sync_playwright):
    global global_id
    context = playwright.request.new_context(base_url= SUT)
    response = context.get(url=urlUsers, headers=get_bearer_header())     
    print(response)
    global_id = get_random_user_id(response)
    assert response.status == 200 
    assert response.status_text == "OK" 
    assert response.ok
    assert response.headers["content-type"] == "application/json; charset=utf-8"