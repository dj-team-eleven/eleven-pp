# eleven-pp
- Team-eleven's `pip Development Storage`
- The team-eleven's first pypi project. We make several functions for our work
<br>

- View at : https://pypi.org/project/eleven-pp/

### Install

`$ pip install eleven-pp`

- if you already intalled but, old version,<br>
`$ pip install --upgrade eleven-pp`

### USE

```bash
$ 11-blog

블로그 탐방가기~
재호 : https://shims94.github.io/
수빈 : https://velog.io/@ppippi
하현 : https://hxhkim.github.io/
민정 : https://velog.io/@minjung00
주선 : https://assomdevgit.github.io/
인균 : https://aaingyunii.github.io/

```

```bash
$ 11-dday

프로젝트 마감일까지 41일 남았습니다.

```

```bash
$ 11-lunch

추천 식당명: 카츠디나인
업 종: 돈가스
한줄 평: 돈가스 맛집

# 무작위로 맛집 추천
```

```bash
$ 11-lotto

[24, 41, 9, 36, 18, 30]

# 무작위로 1~45사이의 6개의 숫자 출력
```

### DEV

```bash
$ git clone ...
$ cd eleven-pp
$ pdm venv create
$ source .venv/bin/activate
(eleven-pp-3.8) $ pdm install
```

### TEST

```bash
$ pdm add -dG test pytest pytest-cov
$ pytest
$ pytest -s
$ pytest --cov
```

### DEPLOY

```bash
$ pdm publish
```

### how2pr
- https://oss.cashmallow.com/team/how2pr/

### REF

- [네이버 신대방삼거리 음식점 지도](https://map.naver.com/p/search/%EC%8B%A0%EB%8C%80%EB%B0%A9%EC%82%BC%EA%B1%B0%EB%A6%AC%20%EC%9D%8C%EC%8B%9D%EC%A0%90?c=15.00,0,0,0,dh)