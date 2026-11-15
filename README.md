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

## 라이선스

저장소의 라이선스는 [LICENSE](LICENSE)를 확인하세요.
