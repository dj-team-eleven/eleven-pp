def calculate_dday():
    
    from datetime import datetime
    
    target_date = datetime(2023, 12, 5)
    today_date = datetime.now()

    days_remaining = (target_date - today_date).days

    if days_remaining > 0:
        print(f"프로젝트 마감일까지 {days_remaining}일 남았습니다.")
    elif days_remaining == 0:
        print("D-day입니다!")
    else:
        print("프로젝트 마감 일자가 이미 지났습니다.")
        
