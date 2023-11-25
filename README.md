# GisuksaSong
> [기숙사 기상송 추천]

## Description
> 아침 기상송으로 팔각모같은거 듣기 싫고, 기상송 추천제는 시행될 기미가 안보이니 답답해서 내가 직접 만들기로 했다.
## Environment
> 크롬 권장
## Files
> - db_functions.py
> - link_functions.py
> - main.py
## Usage
> 1. 기숙사 선택
> 2. 유튜브 링크 복사/붙여넣기
## Version
> GisuksaSong early_before_pre_alpha 1
## Xi story
> jona 어렵습니다
> 사실 쉽습니다

## Japdam
이건 내가보려고만든거

> 기본적인 구조는 무엇인가:
> - 웹에서 유튜브 영상 링크를 받아서 -> 그걸 DB에 저장하고 -> 일종의 재생목록처럼 만들어 다시 웹으로 보냄 / 모 영어 단어시험 사이트를 해킹하면서 얻어낸 경험을 바탕으로 대부분의 작업은 서버 내부적으로 이루어질 예정
> - 일반 사용자 권한: 영상 추천, 영상 재생
> - 사감실 권한: 영상 추천, 영상 재생, 영상 비활성화, 영상 삭제, 영상 차단
> 
> 개발 언어, 기타등등:
> - 프론트는 언제나처럼 HTML+CSS+JS
> - 서버는 python 기반, DB의 저장 형식은 pickle, 이유는 편해서 (사실 pickle로 저장하는데 데이터베이스라고 말하기도 애매하긴 함)
> - pickle로 했을때 용량이 약간 걱정되긴 하지만 다 쓰고난 파일은 txt로 바꿔서 저장하고 pickle파일은 폐기할 예정
> - FastAPI 사용