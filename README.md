# 학과 뉴스레터 생성기

호서대학교 게임소프트웨어학과 졸업생을 위한 HTML 뉴스레터 자동 생성 도구입니다.

Markdown으로 작성한 뉴스레터 내용을 세련된 HTML 이메일 형식으로 변환합니다.

## ✨ 주요 기능

- 📝 Markdown 기반 콘텐츠 작성
- 🎨 현대적이고 반응형 디자인
- 🖼️ 이미지 삽입 지원
- 📱 모바일 최적화
- 🎯 이메일 클라이언트 호환

## 🚀 빠른 시작

### 1. 의존성 설치

```bash
make init
# 또는
pip install jinja2 markdown2
```

### 2. 콘텐츠 작성

`content.md` 파일을 수정하여 뉴스레터 내용을 작성합니다.

```markdown
# 2025년 12월 뉴스레터

## 📢 학과 소식
- 새로운 소식 1
- 새로운 소식 2

## 🎓 졸업생 동정
...
```

### 3. HTML 생성

```bash
make
# 또는
python3 newsletter.py
```

### 4. 미리보기

```bash
make preview
```

생성된 파일은 `output/newsletter.html`에 저장됩니다.

## 📁 프로젝트 구조

```
newsletter/
├── README.md              # 프로젝트 설명서
├── Makefile              # 빌드 자동화
├── newsletter.py         # 메인 스크립트
├── template.html         # HTML 템플릿
├── content.md           # 뉴스레터 내용 (편집 필요)
└── output/              # 생성된 HTML 파일
    └── newsletter.html
```

## 🛠️ Makefile 명령어

| 명령어 | 설명 |
|--------|------|
| `make` | 뉴스레터 HTML 생성 |
| `make preview` | 생성 후 브라우저로 바로 열기 |
| `make clean` | 생성된 파일 삭제 |
| `make install` | Python 패키지 설치 |
| `make help` | 도움말 보기 |

## ✏️ 콘텐츠 작성 가이드

### 기본 Markdown 문법

```markdown
# 대제목 (섹션)
## 중제목 (서브섹션)
### 소제목

**굵은 글씨**로 강조할 수 있습니다.

- 리스트 항목 1
- 리스트 항목 2
- 리스트 항목 3

[링크 텍스트](https://example.com)

![이미지 설명](https://example.com/image.jpg)
```

### 이미지 삽입

이미지는 웹서버에 업로드 후 URL로 참조하는 것을 권장합니다:

```markdown
![행사 사진](https://game.hoseo.ac.kr/images/event2025.jpg)
```

## 🎨 템플릿 커스터마이징

`template.html` 파일을 수정하여 디자인을 변경할 수 있습니다.

### 색상 변경

템플릿의 `<style>` 섹션에서 다음 값들을 수정하세요:

```css
/* 메인 색상 */
background: linear-gradient(135deg, #2D3561 0%, #1F2544 50%, #0F0F23 100%);

/* 강조 색상 */
background: linear-gradient(135deg, #5E72EB 0%, #8B5CF6 100%);
```

### 연락처 정보 수정

`template.html` 파일의 푸터 섹션에서 수정:

```html
<div class="contact-value">game@hoseo.edu</div>
<div class="contact-value">041-XXX-XXXX</div>
```

## 📬 이메일 발송 방법

### Outlook 사용

1. `output/newsletter.html` 파일을 브라우저로 열기
2. 전체 선택 (Ctrl+A / Cmd+A)
3. 복사 (Ctrl+C / Cmd+C)
4. Outlook 새 메일에 붙여넣기 (Ctrl+V / Cmd+V)

### Gmail 사용

1. 브라우저로 `output/newsletter.html` 열기
2. 전체 선택 후 복사
3. Gmail 새 메일 작성에 붙여넣기

### Python으로 직접 발송 (고급)

```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# newsletter.html 내용 읽기
with open('output/newsletter.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# 이메일 구성
msg = MIMEMultipart('alternative')
msg['Subject'] = '게임소프트웨어학과 12월 뉴스레터'
msg['From'] = 'game@hoseo.edu'
msg['To'] = 'recipients@example.com'

# HTML 첨부
html_part = MIMEText(html_content, 'html', 'utf-8')
msg.attach(html_part)

# SMTP 서버로 발송
# (학교 메일 서버 설정 필요)
```

## 📝 작성 팁

1. **간결하게**: 각 섹션은 3-5개 항목 이내로 유지
2. **시각적 요소**: 이미지를 적절히 활용
3. **링크 포함**: 상세 정보는 링크로 연결
4. **정기성**: 월간/분기별 등 규칙적으로 발송
5. **테스트**: 여러 이메일 클라이언트에서 테스트

## 🔍 문제 해결

### Python 패키지 설치 오류

```bash
# pip 업그레이드
pip install --upgrade pip

# 재설치
pip install --force-reinstall jinja2 markdown2
```

### 한글 인코딩 오류

모든 파일이 UTF-8로 저장되어 있는지 확인하세요.

### 이미지가 표시되지 않음

- 이미지 URL이 공개적으로 접근 가능한지 확인
- HTTPS 프로토콜 사용 권장
- 이미지 파일 경로 확인

## 📚 참고 자료

- [Markdown 가이드](https://www.markdownguide.org/)
- [Jinja2 문서](https://jinja.palletsprojects.com/)
- [이메일 HTML 디자인 모범 사례](https://www.campaignmonitor.com/css/)

## 📄 라이선스

MIT License
