# attend.py - 스터디 출석부 프로그램

# 출석 기록을 담아 둘 빈 리스트(상자)
records = []


def add_attendance():
    """날짜와 이름을 입력받아 출석 기록을 추가하는 함수"""
    date = input("날짜를 입력하세요 (예: 2024-05-20): ")
    name = input("이름을 입력하세요: ")
    records.append({"date": date, "name": name})
    print(f"✅ 출석 완료! ({date} / {name})")


def show_attendance():
    """지금까지 쌓인 출석 목록을 보여주는 함수"""
    if not records:  # 기록이 하나도 없을 때
        print("\n아직 출석 기록이 없어요.")
        return

    print("\n===== 출석 목록 =====")
    # enumerate: 자동으로 1, 2, 3... 번호를 매겨 줌
    for i, record in enumerate(records, start=1):
        print(f"{i}. {record['date']} - {record['name']}")
    print("====================")


def main():
    """메뉴를 보여주고 선택을 처리하는 사령탑 함수"""
    while True:  # 종료 전까지 메뉴를 계속 반복
        print("\n1. 출석 추가")
        print("2. 출석 목록 보기")
        print("3. 종료")
        choice = input("메뉴를 선택하세요 (1/2/3): ")

        if choice == "1":
            add_attendance()
        elif choice == "2":
            show_attendance()
        elif choice == "3":
            print("👋 프로그램을 종료합니다.")
            break  # 무한 반복 탈출
        else:
            print("⚠️ 1, 2, 3 중에서 입력해 주세요.")


# 이 파일을 직접 실행했을 때만 main()이 돌아가도록 하는 부분
if __name__ == "__main__":
    main()
