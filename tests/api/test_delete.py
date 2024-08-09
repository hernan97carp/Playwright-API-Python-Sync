from tests.testbase import get_bearer_header, createNewUser, sync_playwright, SUT, urlUsers,id_user
def test_post(playwright: sync_playwright):
    global id_user
    data = createNewUser()
    context = playwright.request.new_context(base_url=SUT)
    resp = context.post(url=urlUsers, headers=get_bearer_header(), data=data)
    resJson = resp.json()
    id_user = resJson["id"]
    assert resp.status == 201
    assert resp.status_text == "Created"
    assert resp.ok
    assert resJson["name"] == data["name"]
    assert resJson["email"] == data["email"]
    assert resJson["gender"] == data["gender"]
    assert resJson["status"] == data["status"]
    assert resp.headers["content-type"] == "application/json; charset=utf-8"


def test_delete(playwright: sync_playwright):
    global id_user
    context = playwright.request.new_context(base_url=SUT)
    resp = context.delete(url=f"{urlUsers}{id_user}", headers=get_bearer_header())
    assert resp.status == 204
def test_get(playwright: sync_playwright):
    global id_user
    context = playwright.request.new_context(base_url=SUT)
    response = context.get(url=f"{urlUsers}{id_user}", headers=get_bearer_header())
    assert response.status == 404
    assert response.json()["message"] == "Resource not found"

