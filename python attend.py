# ===================================
#   스터디 출석부 프로그램 (attend.py)
#   - 외부 라이브러리 없이 동작합니다
# ===================================

# 출석 데이터를 저장할 빈 리스트 (바구니)
attendance_data = []


def check_in():
    """출석 체크하기: 날짜와 이름을 입력받아 기록합니다."""
    date = input("날짜를 입력하세요 (예: 2023-10-27): ")
    name = input("이름을 입력하세요: ")

    # 입력한 정보를 하나로 묶어 리스트에 추가(append)
    record = f"날짜: {date} | 이름: {name}"
    attendance_data.append(record)
    print(f"✅ {name}님, 출석 체크 완료!")


def show_list():
    """출석 명단 보기: 지금까지 쌓인 기록을 보여줍니다."""
    print("\n--- 현재까지의 출석 명단 ---")
    if not attendance_data:
        print("아직 출석 기록이 없습니다.")
    else:
        # 번호를 붙여 하나씩 출력
        for i, item in enumerate(attendance_data, start=1):
            print(f"{i}. {item}")


def main():
    """프로그램의 시작점: 메뉴를 반복해서 보여줍니다."""
    while True:
        print("\n--- 스터디 출석 관리 프로그램 ---")
        print("1. 출석 체크하기")
        print("2. 출석 명단 보기")
        print("3. 종료하기")

        choice = input("원하는 메뉴 번호를 입력하세요: ")

        if choice == '1':
            check_in()
        elif choice == '2':
            show_list()
        elif choice == '3':
            print("프로그램을 종료합니다. 안녕히 가세요!")
            break  # while 반복문을 빠져나갑니다.
        else:
            print("❌ 잘못된 입력입니다. 1, 2, 3 중에서 골라주세요.")


# 이 파일을 직접 실행했을 때만 main()이 동작합니다.
if __name__ == "__main__":
    main()
