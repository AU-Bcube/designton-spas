# B-CUBE 디자인톤 프로젝트 소개 페이지

B-CUBE 디자인톤에서 기획한 프로젝트를 발표 자료와 프로젝트 설명을 바탕으로 정리한 정적 웹사이트 모음입니다. 각 프로젝트는 독립적인 단일 HTML 페이지로, 기획 배경과 핵심 아이디어, 발표 화면을 소개합니다.

## 프로젝트 살펴보기

| 연도 | 프로젝트 | 소개 |
| --- | --- | --- |
| 2023 | [Glo:meet](out_spas/glomeet/) | 재학생과 교환학생의 관심사 기반 교류 |
| 2023 | [아주대 캠퍼스맵](out_spas/ajou-campus-map/) | 지도 기반 캠퍼스 시설과 행사 정보 |
| 2023 | [치토의 기록집](out_spas/chito-record/) | 게임처럼 즐기는 대학생활 활동 기록 |
| 2023 | [AJOUWAY](out_spas/ajouway/) | 캠퍼스 정보와 학생 커뮤니티 |
| 2024 | [치토스](out_spas/cheetos-mentoring/) | 아주대학교 재학생을 위한 동문 멘토링 |
| 2024 | [아주찌릿](out_spas/ajou-jjirit/) | 아주대 학생을 위한 당일 번개 모임 |
| 2024 | [AjouLab](out_spas/ajoulab/) | 대학원과 연구실 정보 탐색 |
| 2024 | [DEMATE](out_spas/demate/) | 관심사와 적성에 맞는 봉사활동 매칭 |
| 2024 | [A-chedular](out_spas/a-chedular/) | 교내 강연 추천과 일정 관리 |
| 2025 | [Toolib](out_spas/toolib/) | 대학생을 위한 AI 도구 추천 |
| 2025 | [HeyPick!](out_spas/heypick/) | 대학생 할인과 혜택 정보 |
| 2025 | [AJOU SHUTTLE](out_spas/ajou-shuttle/) | 아주대학교 셔틀버스 정보 |
| 2025 | [SPORTIZE](out_spas/sportize/) | 스포츠 시설, 클래스와 커뮤니티 |
| 2025 | [HELP ME!](out_spas/help-me/) | 대학생을 위한 물품 대여 |
| 2026 | [마실:온](out_spas/masil-on/) | 시니어를 위한 동네 모임과 소통 |
| 2026 | [DOTT](out_spas/dott/) | 작은 행동부터 시작하는 실행 관리 |
| 2026 | [Haru:ON](out_spas/haru-on/) | 발달장애 아동의 일상 적응 지원 |
| 2026 | [효돈](out_spas/hyodon/) | 시니어와 가족을 위한 금융 보호 |

## 저장소 구성

```text
.
├── DESIGN.md                 # 결과물 작성 지침
├── netlify.toml              # Netlify 빌드 및 공개 디렉토리 설정
├── scripts/build_netlify.py  # 배포 파일과 도메인별 라우팅 생성
├── tests/                    # 도메인 등록 동작 테스트
├── designton_pdfs/           # 원본 PDF와 프로젝트 목록 CSV
└── out_spas/
    └── <서브도메인 후보>/
        ├── index.html        # 프로젝트 소개 페이지
        ├── README.md         # 프로젝트 개요와 PDF 페이지별 요약
        ├── DESIGN_RULE.md    # 디자인 컨셉과 구성 규칙
        └── assets/           # 페이지에서 참조하는 이미지
```

`designton_pdfs/bcube.designtons.csv`에는 프로젝트 설명과 원본 PDF 주소가 담겨 있습니다. 일부 PDF는 CSV에 연결된 외부 원본이며 `designton_pdfs/`에 저장되어 있지 않습니다. 이미지 기반 PDF의 세부 내용은 각 프로젝트 README와 원본 자료를 함께 참고하세요.

## 로컬에서 보기

별도의 빌드나 의존성 설치 없이 각 프로젝트의 `index.html`을 브라우저에서 열 수 있습니다. 또는 저장소 루트에서 정적 서버를 실행합니다.

```sh
python3 -m http.server 8000
```

브라우저에서 `http://localhost:8000/out_spas/`에 접속해 프로젝트를 선택하거나, 예를 들어 `http://localhost:8000/out_spas/masil-on/`으로 바로 열 수 있습니다. 폰트는 CDN을 사용하므로 인터넷 연결이 없으면 대체 글꼴로 표시됩니다.

각 페이지는 프로젝트를 설명하는 정적 결과물입니다. 소개된 앱의 회원가입, 매칭, 예약 등은 실제로 동작하는 서비스 기능이 아닙니다. 작성 및 구현 기준은 [DESIGN.md](DESIGN.md)를 참고하세요.

## 개발 및 빌드

필요한 도구는 Python 3이며, 추가 패키지를 설치할 필요는 없습니다. 프로젝트 페이지는 위의 정적 서버로 바로 확인할 수 있습니다. Netlify 배포 파일을 로컬에서 만들려면 저장소 루트에서 다음 명령을 실행합니다.

```sh
python3 scripts/build_netlify.py
```

이 명령은 `out_spas/`를 `.netlify-publish/`로 복사하고, 각 서브도메인을 해당 프로젝트로 연결하는 `_redirects` 파일을 생성합니다. `.netlify-publish/`는 생성 결과물이므로 Git에 포함하지 않습니다. 로컬에서 일반적으로 실행할 때는 Netlify API를 호출하거나 도메인을 등록하지 않습니다. 기존 `.netlify-publish/`는 실행할 때마다 다시 생성됩니다.

도메인 등록 로직의 테스트는 다음과 같이 실행합니다. 테스트는 모의 API 응답을 사용하며 실제 도메인 설정을 변경하지 않습니다.

```sh
python3 -m unittest discover -s tests -v
```

## Netlify 배포 설정

이 저장소는 Netlify 프로젝트 하나에서 `out_spas/<프로젝트명>/`을 `https://<프로젝트명>.b-cube.kr/`로 제공하도록 구성되어 있습니다.

1. Netlify에서 Git 저장소를 연결하고 프로젝트를 생성합니다. Base directory는 비워 저장소 루트를 사용합니다. [netlify.toml](netlify.toml)이 빌드 명령 `python3 scripts/build_netlify.py`와 공개 디렉토리 `.netlify-publish`를 설정합니다.
2. Netlify 계정의 **User settings > Applications > Personal access tokens**에서 토큰을 생성합니다. 토큰을 발급한 계정은 해당 Netlify 팀과 프로젝트의 도메인을 조회·변경할 권한이 있어야 합니다. 토큰을 생성할 때 해당 팀에 대한 접근 권한을 부여합니다. [Netlify 토큰 안내](https://docs.netlify.com/accounts-and-billing/user-settings/)
3. Netlify 프로젝트의 **Project configuration > Environment variables**에 다음 값을 추가합니다. 선택할 수 있다면 비밀 값으로 표시하고 범위에 **Builds**를 포함합니다. 토큰 값은 저장소, `netlify.toml`, PR, 빌드 로그에 기록하지 않습니다. [환경 변수 설정 안내](https://docs.netlify.com/build/environment-variables/get-started/)

   | 변수 | 설정 방법 | 용도 |
   | --- | --- | --- |
   | `NETLIFY_DOMAIN_TOKEN` | 개발자가 Netlify 환경 변수에 비밀 값으로 등록 | 프로젝트의 도메인 별칭 조회 및 등록 |
   | `SITE_ID` | Netlify가 빌드 시 자동 제공 | 도메인을 등록할 프로젝트 식별 |
   | `NETLIFY` | Netlify가 빌드 시 자동 제공 | Netlify 빌드에서 도메인 등록 실행 여부 판단 |

   별도의 앱 비밀키나 DNS API 키는 이 빌드에 필요하지 않습니다. 토큰을 설정하거나 변경한 뒤 새 빌드를 실행합니다. 토큰이 없거나 권한이 부족하면 Netlify 빌드는 실패합니다.
4. 빌드 시 `out_spas/`의 모든 프로젝트 도메인을 확인하고 빠진 도메인만 Netlify 별칭에 추가합니다. 기존 기본 도메인과 별칭은 유지하며 디렉토리를 삭제해도 등록된 별칭은 자동 삭제하지 않습니다. 새 프로젝트에는 소문자·숫자·하이픈으로 된 DNS 레이블 이름과 `index.html`이 필요합니다.
5. DNS 레코드 및 네임서버는 별도로 관리합니다. 외부 DNS를 사용한다면 각 서브도메인을 해당 Netlify 프로젝트의 `.netlify.app` 주소로 연결하고 HTTPS 인증서 발급을 확인합니다. 빌드 스크립트는 DNS API를 호출하지 않습니다. Netlify DNS를 사용하면 Netlify가 도메인 연결에 따라 DNS 레코드를 자동 생성할 수 있습니다. [외부 DNS 설정](https://docs.netlify.com/manage/domains/configure-domains/configure-external-dns/)

**프리뷰와 브랜치 빌드를 포함한 모든 Netlify 빌드가 실제 프로젝트의 도메인 설정을 변경합니다.** 각 빌드 컨텍스트에 토큰이 없으면 해당 빌드는 실패합니다. 신뢰할 수 없는 PR에서 비밀 값이 노출되거나 도메인이 변경되지 않도록 Netlify의 untrusted deploy 정책을 설정하고, 비밀을 제공하는 코드를 검토하세요. 동시에 여러 빌드나 관리자가 별칭 목록을 변경하면 덮어쓰기가 발생할 수 있으므로 변경을 직렬화하고 결과를 확인해야 합니다. 빌드 중 등록된 도메인은 이후 배포에 실패해도 자동으로 취소되지 않습니다.

배포 후에는 각 도메인의 페이지와 이미지, HTTPS, 존재하지 않는 파일의 404 응답을 확인합니다. `.netlify-publish/`에는 각 프로젝트의 `README.md`와 `DESIGN_RULE.md`도 복사되어 공개될 수 있습니다. 상세 운영 방안은 [DESIGN.md](DESIGN.md)의 Netlify 호스팅 섹션을 참고하세요.

## 라이선스

저장소의 라이선스는 [LICENSE](LICENSE)를 확인하세요.
