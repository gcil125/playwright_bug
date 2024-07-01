def test_playwright_request():
    from playwright import _repo_version
    from playwright.sync_api import sync_playwright
    with sync_playwright() as sp:
        request = sp.request.new_context()
        response = request.put(
            "http://127.0.0.1:5000/headers", headers={"Content-Type": "application/json"},
            data=[])
        print(f"playwright version: {_repo_version.version}")
        print(f"playwright: {response.text()}")


def test_httpx():
    import httpx

    response = httpx.put("http://127.0.0.1:5000/headers", json=[])
    print(f"httpx: {response.text}")


if __name__ == '__main__':
    test_httpx()
    test_playwright_request()
