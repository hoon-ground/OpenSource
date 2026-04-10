# Dev.Log 📝

> Flask와 Flasgger로 만든 현대적이고 상호작용적인 개발 로깅 애플리케이션. 아름다운 웹 인터페이스와 완전한 REST API로 게발 여정을 쉽게 기록, 관리, 문서화할 수 있다.

[![Python](https://img.shields.io/badge/Python-3.8+-3776ab.svg?style=flat-square&logo=python)](https://www.python.org)
[![Flask](https://img.shields.io/badge/Flask-3.0+-000000.svg?style=flat-square&logo=flask)](https://flask.palletsprojects.com)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=flat-square)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg?style=flat-square)](https://github.com/hoon-ground/OpenSource)

## 🌟 주요 기능

- **Web Interface** - 로그 작성 및 관리를 위한 사용자 친화적 인터페이스
- **RESTful API** - 프로그래밍 방식의 접근을 위한 완전한 REST API
- **Swagger UI 문서** - Flasgger를 이용한 상호작용적 API 문서
- **Multi-type Logs** - 다양한 로그 카테고리 지원 (TIL, 버그 수정, 기능 추가 등)
- **Content Management** - 로그 엔트리의 생성, 읽기, 수정, 삭제 기능
- **포괄적 테스트** - pytest를 이용한 완전한 테스트 커버리지
- **Sphinx 문서** - 문서화된 docstring으로부터 자동 생성되는 API 문서

## 🛠️ 기술 스택

| 분류              | 기술                           |
| ----------------- | ------------------------------ |
| **BE**            | Flask 3.0+                     |
| **API 문서**      | Flasgger (OpenAPI/Swagger)     |
| **DB**            | 메모리 내 리스트 (데이터 구조) |
| **FE**            | HTML, CSS, Jinja2 템플릿       |
| **TEST**          | pytest                         |
| **Documentation** | Sphinx, Python docstring       |

## 📋 빠른 시작

### 필수 요건

- Python 3.8 이상
- pip (Python 패키지 관리자)

### 설치 방법

1. **저장소 클론**

   ```bash
   git clone https://github.com/hoon-ground/OpenSource.git
   cd OpenSource
   ```

2. **가상 환경 생성** (권장)

   ```bash
   python -m venv venv
   # Windows의 경우
   venv\Scripts\activate
   # macOS/Linux의 경우
   source venv/bin/activate
   ```

3. **의존성 설치**

   ```bash
   pip install -r requirements.txt
   ```

4. **애플리케이션 실행**

   ```bash
   py -m flask --app app/app.py run
   ```

5. **애플리케이션 접속**
   - 웹 인터페이스: http://localhost:5000
   - Swagger API 문서: http://localhost:5000/apidocs

## 📚 사용 가이드

### 웹 인터페이스

#### 홈 페이지

- 모든 개발 로그 보기
- 엔트리 빠르게 접근 및 탐색
- 로그 타입 및 생성 순서로 정렬

#### 새 로그 작성

- `/write` 페이지로 이동
- 로그 타입 선택 (TIL, 버그 수정, 기능 추가 등)
- 제목 및 내용 입력
- 자동으로 컬렉션에 저장

#### 로그 상세 보기

- 로그 엔트리 클릭하여 전체 내용 보기
- 타입, 제목, 전체 내용 확인

### REST API 엔드포인트

모든 엔드포인트는 JSON 응답을 반환-. [Swagger UI](http://localhost:5000/apidocs)에서 직접 테스트할 수 있다.

#### 모든 로그 조회

```bash
GET /api/logs

# 응답
[
  {
    "id": 0,
    "type": "TIL",
    "title": "Flask 공부",
    "content": "pytest로 테스트 작성"
  }
]
```

#### 새 로그 생성

```bash
POST /api/logs
Content-Type: application/json

{
  "type": "TIL",
  "title": "Flask 학습",
  "content": "오늘 Flask 기초를 배웠다"
}

# 응답 (201 Created)
{
  "id": 0,
  "type": "TIL",
  "title": "Flask 학습",
  "content": "오늘 Flask 기초를 배웠다"
}
```

#### 특정 로그 조회

```bash
GET /api/logs/0

# 응답
{
  "id": 0,
  "type": "TIL",
  "title": "Flask 학습",
  "content": "오늘 Flask 기초를 배웠다"
}
```

#### 로그 수정

```bash
PUT /api/logs/0
Content-Type: application/json

{
  "title": "Flask 심화 학습",
  "content": "Flask 고급 개념 학습"
}

# 응답 (200 OK)
{
  "id": 0,
  "type": "TIL",
  "title": "Flask 심화 학습",
  "content": "Flask 고급 개념 학습"
}
```

#### 로그 삭제

```bash
DELETE /api/logs/0

# 응답 (200 OK)
{
  "message": "로그가 성공적으로 삭제되었습니다"
}
```

## 📁 프로젝트 구조

```
OpenSource/
├── app/
│   ├── app.py                 # Flasgger API를 포함한 Flask 메인 애플리케이션
│   ├── static/                # 정적 파일 (CSS, 이미지)
│   │   └── style.css
│   └── templates/             # HTML 템플릿
│       ├── home.html
│       ├── write.html
│       └── log.html
├── tests/
│   └── test_app.py            # pytest 테스트 스위트
├── docs/
│   ├── Makefile               # Sphinx 문서 생성
│   ├── source/
│   │   ├── conf.py
│   │   └── index.rst
│   └── build/                 # 생성된 문서
├── static/
│   └── style.css              # 메인 스타일시트
├── templates/                 # 템플릿 파일
│   ├── home.html
│   ├── log.html
│   └── write.html
├── README.md                  # 이 파일
└── requirements.txt           # Python 의존성
```

## 🧪 테스트

테스트 스위트를 실행하여 모든 것이 올바르게 작동하는지 확인:

```bash
pytest tests/

# 상세 출력
pytest tests/ -v

# 커버리지 리포트 포함
pytest --cov=app tests/
```

### 테스트 커버리지

- ✅ 홈 페이지 렌더링
- ✅ 로그 생성 및 유효성 검사
- ✅ 로그 상세 페이지 표시
- ✅ 빈 필드 유효성 검사
- ✅ API 엔드포인트

## 📖 API 문서

### 상호작용적 Swagger UI

애플리케이션에는 상호작용적 API 문서를 위한 **Flasgger**가 포함되어 있다. 서버를 시작하고 다음으로 이동:

- **Swagger UI**: http://localhost:5000/apidocs
- **ReDoc**: http://localhost:5000/redoc

여기서 다음을 할 수 있다:

- 모든 사용 가능한 엔드포인트 보기
- 요청/응답 스키마 확인
- **브라우저에서 직접 API 호출 테스트**
- 여러 언어로 코드 샘플 생성

### Python Docstring

코드베이스는 Google 스타일 docstring을 따른다. Sphinx를 사용하여 전체 API 문서를 생성할 수 있다:

```bash
cd docs
make html
# build/html/index.html을 브라우저에서 열기
```

## 🚀 애플리케이션 실행

### 개발 서버

```bash
# 자동 재로드 및 디버그 모드로 실행
py -m flask --app app/app.py run
```

### 프로덕션 서버

```bash
# Gunicorn 사용 (설치: pip install gunicorn)
gunicorn -w 4 -b 0.0.0.0:5000 app.app:app
```

## 📝 로그 엔트리 타입

더 나은 분류를 위해 타입별로 로그를 정렬:

| 타입          | 설명                                 |
| ------------- | ------------------------------------ |
| **TIL**       | Today I Learned - 새로운 개념과 지식 |
| **버그 수정** | 해결된 문제 및 솔루션                |
| **기능**      | 구현된 새로운 기능                   |
| **리팩토링**  | 코드 개선 및 최적화                  |
| **일반**      | 기타 메모                            |

### 개발 환경 설정

```bash
# 개발 의존성 설치
pip install -r requirements-dev.txt

# PR 제출 전 테스트 실행
pytest tests/

# 코드 포매팅
black app/ tests/
```

## 🎯 개발 로드맵

- [ ] 데이터베이스 통합 (PostgreSQL/MongoDB)
- [ ] 사용자 인증 및 권한 부여
- [ ] 검색 및 필터링 기능
- [ ] 태그 시스템으로 더 나은 정렬
- [ ] 로그를 PDF/Markdown으로 내보내기
- [ ] 다크 모드 UI
- [ ] 모바일 반응형 디자인 개선

## References

- [Flask 문서](https://flask.palletsprojects.com/)
- [Flasgger](https://flasgger.readthedocs.io/)
- [Sphinx 문서](https://www.sphinx-doc.org/)

---

<div align="center">

**[⬆ 맨 위로](#devlog-)**

❤️ [hoon-ground](https://github.com/hoon-ground)

</div>
