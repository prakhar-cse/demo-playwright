

def test_login(page):
    page.goto("https://www.saucedemo.com/")
    page.fill(selector="#user-name", value="standard_user")
    page.fill(selector="#password", value="secret_sauce")
    page.click(selector="#login-button")
    assert "inventory" in page.url