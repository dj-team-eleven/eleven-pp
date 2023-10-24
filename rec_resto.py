import random

def rec_resto() :
    resto_list = [
        {"name": "카츠디나인", "type": "돈가스","des":"돈가스 맛집"},
        {"name": "감탄계", "type": "치킨, 맥주","des":"새로오픈한 치킨집"},
        {"name": "쿠우쿠우", "type": "일식뷔페","des":"가성비일식뷔페"},
        {"name": "미분당", "type": "베트남음식","des":"쌀국수 맛집"},
        {"name": "킨로우라멘", "type": "라멘","des":"라멘 맛집"},
        {"name": "명륜진사갈비", "type": "육류","des":"다들아는 그 갈비"},
        {"name": "오다", "type": "일식","des":"게살 크림파스타 맛집"},
    ]

    rec = random.choice(resto_list)

    print("추천 식당명:", rec["name"])
    print("업 종:", rec["type"])
    print("한줄 평:", rec["des"])
