<p align="center">
  <img src="images/icon-1024.png" width="128" alt="FileExplorer8">
</p>

<h1 align="center">FileExplorer8</h1>

<p align="center"><strong>macOS 네이티브 파일 관리자 · 파일 관리자 / 2분할 / 4분할을 한 창에서 전환</strong></p>

<p align="center">하나의 파일 작업 코어, 세 가지 조작 방식 · 쓰기 전 사전 점검 · 3단계 실행 취소 · 수만 항목 폴더도 끊김 없이</p>

<p align="center">
  <a href="https://rosesmall2010.github.io/FileExplorer8/"><img src="https://img.shields.io/badge/%EC%A7%80%EC%9B%90-blue" alt="Site"></a>
  <a href="https://rosesmall2010.github.io/FileExplorer8/privacy.ko.html"><img src="https://img.shields.io/badge/%EA%B0%9C%EC%9D%B8%EC%A0%95%EB%B3%B4-green" alt="Privacy"></a>
  <img src="https://img.shields.io/badge/version-1.1.6-lightgrey" alt="Version">
</p>

<p align="center"><a href="README.md" hreflang="zh-Hans" lang="zh-Hans">简体中文</a> · <a href="README.zh-Hant.md" hreflang="zh-Hant" lang="zh-Hant">繁體中文</a> · <a href="README.en.md" hreflang="en" lang="en">English</a> · <a href="README.ja.md" hreflang="ja" lang="ja">日本語</a> · <strong>한국어</strong> · <a href="README.de.md" hreflang="de" lang="de">Deutsch</a> · <a href="README.fr.md" hreflang="fr" lang="fr">Français</a> · <a href="README.es.md" hreflang="es" lang="es">Español</a> · <a href="README.pt-BR.md" hreflang="pt-BR" lang="pt-BR">Português (Brasil)</a> · <a href="README.ru.md" hreflang="ru" lang="ru">Русский</a> · <a href="README.vi.md" hreflang="vi" lang="vi">Tiếng Việt</a> · <a href="README.id.md" hreflang="id" lang="id">Bahasa Indonesia</a> · <a href="README.ms.md" hreflang="ms" lang="ms">Bahasa Melayu</a> · <a href="README.th.md" hreflang="th" lang="th">ไทย</a></p>

---

## 무엇인가

FileExplorer8은 macOS에서 네이티브로 동작하는 **파일 관리자**입니다. “파일 관리자”, “2분할 관리자”, “4분할 관리자” 세 가지 조작 방식을 한 창에 담고 `⇧⌘D`로 차례로 전환합니다. 각 형태는 경로, 탭, 정렬 방식, 열 너비, 선택 항목을 각자 기억하므로 오가도 잃지 않습니다.

Finder의 대체품도 아니고 Finder의 또 다른 겉모습도 아닙니다. Finder에 빠진 부분, 곧 **양손을 키보드에 둔 채로 하는 대량 이동**을 채웁니다.

기준으로 삼은 것은 고전적인 2분할 파일 관리자 방식입니다. 기본 앱으로 설정하지 않고, Finder 확장을 만들지 않으며, Finder 환경설정을 읽거나 쓰지 않습니다. 공유하는 것은 파일 시스템 자체뿐입니다. 그래서 Finder와 오래 공존해도 서로 부딪히지 않습니다.

---

## 화면

### 파일 관리자: 그리드 보기와 세부 정보 패널

![파일 관리자: 그리드 보기와 세부 정보 패널](images/readme/01-explorer.png)

### 2분할 관리자: 원본과 대상

![2분할 관리자: 원본과 대상](images/readme/02-dual-pane.png)

### 4분할 관리자: 2×2 배치

![4분할 관리자: 2×2 배치](images/readme/03-quad-pane.png)

---

## 기능

### 쓰기 전에 반드시 사전 점검

복사, 이동, 덮어쓰기 전에 먼저 시험 실행을 합니다. 대상에 쓸 수 있는지, 공간이 충분한지, 어떤 이름이 충돌하는지를 먼저 보여 줍니다. **이 단계에서는 단 1바이트도 쓰지 않습니다.**

충돌 방식은 네 가지 중에서 고릅니다. 바꾸기(먼저 백업하고 실행 취소 지원), 둘 다 유지, 건너뛰기, 항목별 확인. 충돌이 5개 이하이면 하나씩 결정할 수 있습니다.

진행 상황에는 실시간 속도, 전송량 / 전체 / 남은 양이 나오고, 끝나면 성공·건너뜀·실패 건수를 정리한 결과를 보여 줍니다. 실패 항목은 파일 이름과 이유를 하나씩 적습니다.

### 3단계 실행 취소

같은 볼륨 내 이동, 이름 변경, 휴지통으로 삭제, ZIP 압축과 해제는 **100% 실행 취소됩니다**. 복사와 볼륨 간 이동은 최선을 다합니다. 실행 취소가 안 되는 작업은 실행 전에 다시 확인합니다.

### 여섯 가지 보기와 본격 미리보기

아주 큰 / 큰 / 중간 / 작은 아이콘, 목록, 세부 정보. 아이콘은 실제 픽셀 크기(256 / 128 / 64 / 32)로 골라 쓰므로 Retina에서도 가장자리가 흐려지지 않습니다.

`Space`로 미리 보고 `←` / `→`, `PgUp` / `PgDn`으로 이어서 넘길 수 있습니다:

- 텍스트와 소스 코드는 읽기 전용 고정폭 보기. 50개 이상 언어의 구문 강조와 줄 번호
- PDF는 PDFKit으로 표시
- 이미지는 비율을 유지한 채 패널 전체에 맞게 확대·축소
- 서식 있는 형식은 시스템 Quick Look에 맡김
- 표시할 수 없는 항목은 요약 정보를 보여 줌

### 압축과 해제

**ZIP으로 압축**: ZIP64, 압축 수준 조절, 이미 압축된 형식은 자동으로 건너뜀, 심볼릭 링크를 따라갈지 선택 가능. 결과는 실행 취소할 수 있습니다.

**더블클릭으로 해제**. 동작은 Finder와 같습니다. 최상위 폴더가 하나면 겹쳐 만들지 않고, 충돌하면 압축 파일 전체의 이름을 바꾸며, `__MACOSX`만 정리하고 Unix 권한 비트를 복원합니다.

### SSH 원격 폴더

SSH / SFTP 내장. 비밀번호나 임의 경로의 개인 키로 연결하고 원격 폴더도 로컬처럼 탐색, 복사, 삭제, 이름 변경, 실행 취소할 수 있습니다. 쓰기는 같은 경로를 지납니다.

탭에는 네트워크 드라이브 아이콘과 빨강·초록 상태로 연결 상황을 표시하고 끊기면 한 번의 클릭으로 다시 연결합니다. **비밀번호를 저장하지 않을 수도 있으며** 그때는 연결할 때마다 한 번씩 로그인을 묻습니다. 원격 파일도 10 MB까지는 빠르게 미리 볼 수 있습니다.

### 세부 사항

- Finder의 일곱 색 태그를 지원하고 겹쳐 붙일 수 있음. 모두 해제하면 사용자 텍스트 태그를 남김
- 명령 팔레트 `⌘K`. 일치도 → 최근 사용 → 사전순으로 정렬
- 경로 세 가지: 경로 복사, 상위 폴더 경로 복사, 파일 이름 복사. 그리고 “터미널에서 열기”
- 체크섬: SHA-256 / SHA-512 / SHA-1 / MD5 / BLAKE3 / CRC32 / CRC64
- 볼륨 자동 발견: USB 메모리, 외장 드라이브, 마운트된 디스크 이미지가 자동으로 나타나고 한 번의 클릭으로 추출
- 세션 복원: 창 위치, 탭, 열 너비, 정렬, 두 패널 비율을 기억. 충돌 후에도 대기 중인 쓰기를 다시 시작
- Finder와 양방향 복사·붙여넣기, 세 방향 끌어다 놓기 지원
- 언어 전환은 메뉴 막대 최상위 “언어” 메뉴에 있어 한 단계로 닿고 즉시 적용

### 14개 언어

중국어 간체, 중국어 번체, 영어, 일본어, 한국어, 독일어, 프랑스어, 스페인어, 브라질 포르투갈어, 러시아어, 베트남어, 인도네시아어, 말레이어, 태국어.

태국어는 별도의 정렬 규칙을 구현했습니다. 앞선 모음, 성조 기호, 문자 순서 모두 코드 포인트 순서가 아니므로 코드 포인트로 정렬하면 흐트러집니다.

---

## 개인정보

**어떤 데이터도 수집하지 않습니다.** 계정도, 통계도, 광고 SDK도, 충돌 보고도 없습니다.

직접 시작한 SSH 연결을 제외하면 앱은 어떤 서버로도 단 1바이트도 보내지 않습니다. 파일, 방문 기록, 서버 자격 증명은 모두 사용자의 Mac에 남습니다. 비밀번호와 암호는 시스템 키체인에, 개인 키 파일은 사용자가 둔 곳에 있습니다.

앱은 App Sandbox를 켜고 허용한 폴더 범위에서만 읽고 씁니다. 연락처, 카메라, 마이크, 화면 기록, 전체 디스크 접근은 요청하지 않습니다.

[개인정보 처리방침 전문 보기](https://rosesmall2010.github.io/FileExplorer8/privacy.ko.html)

---

## 지원

문제가 생겼거나 제안이 있거나 버그를 발견하셨나요?

- [지원 페이지](https://rosesmall2010.github.io/FileExplorer8/)에서 자주 묻는 질문을 확인하세요
- 또는 [Issues](https://github.com/rosesmall2010/FileExplorer8/issues)에 macOS 버전, FileExplorer8 버전, 재현 단계를 적어 올려 주세요

버전은 “FileExplorer8 › FileExplorer8 정보”에서 확인할 수 있습니다.

### 자주 묻는 질문

**폴더를 열 때 권한을 묻는 이유는 무엇인가요?**
App Sandbox를 켜 두었기 때문입니다. 데스크탑, 다운로드, 문서, 외장 디스크 등은 샌드박스 밖에 있어 해당 폴더에 처음 들어갈 때 macOS가 반드시 확인을 요청합니다. 이는 시스템의 안전 설계이며 결함이 아닙니다. “이 폴더에 대한 접근 허용”을 선택하면 기억되며, 같은 경로는 한 번 실행에 한 번만 묻습니다.

**연락처나 카메라, 화면을 읽나요?**
아니요. FileExplorer8이 요청하는 것은 사용자가 선택한 파일 접근, 표준 폴더(다운로드 / 문서 / 음악 / 사진 / 동영상), 그리고 외부 네트워크 접근뿐입니다. 연락처, 카메라, 마이크, 화면 기록, 전체 디스크 접근 권한은 없습니다.

**SSH 비밀번호는 어디에 저장되나요?**
macOS 키체인에 저장됩니다. 서버 엔드포인트 정보는 로컬 샌드박스 컨테이너 안에 AES-256-GCM으로 암호화되어 있습니다. 비밀번호를 저장하지 않고 연결할 때마다 한 번씩 로그인하도록 할 수도 있습니다. 자세한 내용은 <a href="https://rosesmall2010.github.io/FileExplorer8/privacy.ko.html">개인정보 처리방침</a>을 보세요.

**Apple Silicon과 Intel을 모두 지원하나요?**
둘 다 지원합니다. 설치 파일은 유니버설 바이너리입니다. macOS 15.0 이상이 필요합니다.

**앱을 삭제한 뒤 남은 데이터는 어떻게 정리하나요?**
앱을 삭제한 다음 <code>~/Library/Containers/com.donghuazhu.FileExplorer8/</code>을 삭제하면 환경설정, 세션 상태, 서버 엔드포인트 정보가 지워집니다(샌드박스 앱의 데이터는 이 컨테이너 안에 있으며 시스템 공용 위치에 있지 않습니다). SSH 비밀번호는 키체인에 있고, 해당 연결을 삭제하면 함께 삭제됩니다.

---

## 시스템 요구 사항

- macOS 15.0 이상
- Apple Silicon 또는 Intel(유니버설 바이너리)

---

<p align="center"><sub>macOS는 Apple Inc.의 상표입니다. 이 앱은 Apple Inc.와 무관합니다.</sub></p>
