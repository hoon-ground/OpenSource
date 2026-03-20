from app import app, logs


def test_home_page():
    logs.clear()
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert "Dev.Log" in response.get_data(as_text=True)


def test_create_log():
    logs.clear()
    client = app.test_client()

    response = client.post("/write", data={
        "type": "TIL",
        "title": "Flask 공부",
        "content": "pytest로 테스트 작성"
    })

    assert response.status_code == 302
    assert len(logs) == 1
    assert logs[0]["title"] == "Flask 공부"
    assert logs[0]["content"] == "pytest로 테스트 작성"


def test_log_detail_page():
    logs.clear()
    logs.append({
        "id": 0,
        "type": "TIL",
        "title": "테스트 제목",
        "content": "테스트 내용"
    })

    client = app.test_client()
    response = client.get("/log/0")

    page = response.get_data(as_text=True)

    assert response.status_code == 200
    assert "테스트 제목" in page
    assert "테스트 내용" in page


def test_create_log_with_empty_title_should_not_save():
    logs.clear()
    client = app.test_client()

    response = client.post("/write", data={
        "type": "TIL",
        "title": "",
        "content": "내용은 있음"
    })

    assert response.status_code == 200
    assert len(logs) == 0


def test_create_log_with_empty_content_should_not_save():
    logs.clear()
    client = app.test_client()

    response = client.post("/write", data={
        "type": "TIL",
        "title": "제목은 있음",
        "content": ""
    })

    assert response.status_code == 200
    assert len(logs) == 0