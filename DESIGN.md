## 지침
- 참고1을 확인하라. designton_pdfs/ 디렉토리의 pdf 각각에 대한 서브도메인 후보를 만들어라.
- 만들어진 각각의 서브도메인 후보를 이름으로 out_spas/ 에 디렉토리를 생성한다.
- 생성한 각 디렉토리에 연결된 pdf에서 내용을 읽어 참고1의 `README.md` 파일을 작성하여 저장한다.
- 생성한 각 디렉토리에 연결된 pdf에서 html에 적용할 수 있는 디자인 컴포넌트, 색상, 컨셉을 정리하여 `DESIGN_RULE.md` 파일을 작성하여 저장한다.
- 각 디렉토리의 `README.md` 와 `DESIGN_RULE.md`에 따라 html 파일을 생성한다.
- 각 pdf 당 생성되는 페이지는 단일한 spa html 로 생성한다.
- html 안에 이미지를 삽입하지 말고 svg, png, jpeg, 등은 해당 디렉토리 내에 assets/ 디렉토리를 만들어 저장, 상대경로로 불러온다.

### 참고1 / 각 pdf에 대한 `README.md` 파일 양식
```
# 개요
제목:
부제목 # 없으면 공백
참여자: # 쉼표 후에 공백으로 구분
참여자 메일: # 없으면 공백
서브도메인 후보 1개: # $서브도메인.b-cube.kr 로 spa를 호스팅하기 위함, 3단어 이내, 각 단어는 하이픈으로 잇는다.

## 각 페이지 요약 # 모든 페이지를 순회하며 요약하고, 이미지, 차트에 대한 설명도 삽입한다.
### 0페이지 요약
페이지에 대한 요약
```

## 참고2
- 폰트 사용 시 cdn 사용
- 상단 nav 필요 시 페이지 전환이 아닌 fragment 로 url 뒤에 붙어 해당 영역까지 스크롤을 이동하는 기능 이상으로 구현 금지
- backend 가 필요한 기능 구현 금지. localstorage 등도 사용하지 않고, 각 pdf 프로젝트를 설명하는 html을 만드는데 집중
- 용량이 큰 pdf 는 과도한 토큰 사용을 방지하기 위해 jpeg으로 export 하여 내용을 확인하는 등 조치하라

## Netlify 호스팅 검토 및 운영 방안

하나의 Git 저장소와 하나의 Netlify 프로젝트에서 접속 도메인별로 다른 프로젝트를 제공할 수 있다. Apache의 `ServerName`과 비슷하게 Netlify의 도메인별 rewrite를 이용한다. 예를 들어 `https://a-chedular.b-cube.kr/`은 `out_spas/a-chedular/index.html`을, `https://a-chedular.b-cube.kr/assets/example.png`는 해당 프로젝트의 `assets/example.png`를 제공한다. 200 rewrite는 브라우저의 주소를 바꾸지 않는다. [Netlify 도메인별 규칙](https://docs.netlify.com/manage/routing/redirects/redirect-options/), [rewrite 동작](https://docs.netlify.com/manage/routing/redirects/rewrites-proxies/)

### 권장 설정: 단일 프로젝트와 도메인별 rewrite

1. 저장소를 Netlify 프로젝트 하나에 연결하고 Base directory는 비워 둔다. 저장소의 `netlify.toml`이 빌드 명령 `python3 scripts/build_netlify.py`와 Publish directory `.netlify-publish`를 지정한다. 빌드는 `out_spas`를 해당 디렉토리로 복사하므로 배포된 `/a-chedular/index.html`은 저장소의 `out_spas/a-chedular/index.html`에 해당한다.
2. 프로젝트의 Domain management에 `a-chedular.b-cube.kr` 등 각 서브도메인을 같은 프로젝트의 사용자 지정 도메인 또는 도메인 별칭으로 등록한다. Netlify는 [사이트 하나에 여러 도메인 별칭](https://docs.netlify.com/manage/domains/configure-domains/add-a-domain-alias/)을 지원하며 50개 이하를 권장한다. 현재 디렉토리는 18개다.
3. 외부 DNS를 사용하는 경우 각 서브도메인을 같은 프로젝트의 `<프로젝트명>.netlify.app`에 CNAME으로 연결한다. 도메인을 Netlify에 등록한 후 DNS를 설정하고, Netlify DNS 사용 시에는 해당 관리 방식에 따른다. [외부 DNS 설정](https://docs.netlify.com/manage/domains/configure-domains/configure-external-dns/)
4. 빌드 스크립트는 `out_spas`의 프로젝트 디렉토리를 읽어 `.netlify-publish/_redirects`에 도메인별 규칙을 생성한다. 예를 들어 `a-chedular`에 대해 아래 규칙이 생성된다.

```text
https://a-chedular.b-cube.kr/ /a-chedular/index.html 200!
https://a-chedular.b-cube.kr/* /a-chedular/:splat 200!
```

루트 규칙을 먼저 두고 나머지 경로를 `:splat`으로 전달한다. `200!`은 공개 디렉토리에 같은 요청 경로의 파일이 있어도 rewrite를 적용한다. Netlify는 첫 번째로 일치하는 규칙을 사용하므로 더 구체적인 규칙을 앞에 둔다. Netlify의 HTTPS 강제를 활성화해야 한다. fragment는 브라우저에서 처리되며 서버로 전송되지 않는다. 배포 후 루트와 파일 경로, 누락 파일에 대해 실제 동작을 확인한다.

5. 새 프로젝트를 추가할 때는 유효한 소문자 DNS 레이블 이름의 디렉토리와 `index.html`을 추가한다. 다음 배포 시 규칙이 자동 생성되며, 같은 Netlify 프로젝트의 도메인 등록과 DNS 및 HTTPS 설정은 별도로 필요하다. 잘못된 이름이나 누락된 `index.html`이 있으면 빌드가 실패한다.

로컬에서 `python3 scripts/build_netlify.py`를 실행하면 배포 파일과 규칙을 확인할 수 있다. 생성된 `.netlify-publish/`는 Git에서 제외된다. Netlify 빌드마다 규칙을 생성하므로 GitHub Actions의 자동 커밋은 필요하지 않다.

와일드카드 DNS 또는 인증서만으로 모든 서브도메인이 이 Netlify 프로젝트에 자동 연결된다고 가정하지 않는다. 자동 연결을 원하면 해당 계정의 지원 여부와 조건을 별도 확인해야 한다. [Netlify HTTPS 문서](https://docs.netlify.com/manage/domains/secure-domains-with-https/https-ssl/)

### 공개 범위와 대안

`out_spas` 전체를 공개 디렉토리로 복사하므로 Netlify 기본 도메인이나 다른 경로를 통해 프로젝트 간 파일 및 `README.md`, `DESIGN_RULE.md`에 접근할 수 있다. rewrite는 접근 제어 기능이 아니다. 모든 파일을 공개해도 되는지 확인하고, 제외해야 할 파일은 빌드 단계에서 공개용 출력 디렉토리로 복사하지 않는다. 프로젝트 간 접근 제한이 필요하면 별도 접근 제어 설계가 필요하다.

프로젝트 수가 늘어나 정적 규칙을 관리하기 어렵다면 [Netlify Edge Functions](https://docs.netlify.com/build/edge-functions/api/)에서 요청 호스트를 검사하고 같은 사이트의 경로로 rewrite하는 대안도 있다. 이 경우 허용된 서브도메인 목록, 예상하지 못한 호스트의 404 처리, 경로 검증과 함수 사용량을 고려한다. Edge Function도 DNS, 도메인 연결, HTTPS 설정을 대체하지 않는다.

### 배포 후 확인

- 각 도메인의 `/`에서 해당 프로젝트가 열리고 주소가 유지되는지, 다른 프로젝트 내용이 표시되지 않는지 확인한다.
- 이미지 등 상대 경로 리소스, fragment 링크, 모바일 화면을 확인한다. 존재하지 않는 파일은 404로 처리되는지 확인한다.
- HTTPS 인증서와 HTTP에서 HTTPS로의 이동을 확인한다.
- Netlify Deploy File Explorer 및 기본 도메인에서 공개 파일과 의도하지 않은 직접 접근 가능 여부를 점검한다.

이 내용은 구현 가능성 및 설정 안내이며, 실제 Netlify 프로젝트 생성, DNS 변경, 배포 및 도메인 접속 검증은 아직 수행하지 않았다.
