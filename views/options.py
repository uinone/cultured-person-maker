import os

def set_maximum_question_count():
    answer = -1
    error_message = ""

    NO_LIMIT = -1

    while True:
        os.system("clear")
        if error_message != "":
            print(error_message)
            print("-"*20)
            error_message = ""
        
        try:
            print("최대 문제 개수를 설정해주세요")
            answer = int(input(">>> "))

            if (answer != NO_LIMIT) and (answer <= 0):
                error_message = "0과 같거나 작을 수 없습니다."
                continue

            break
        except ValueError as e:
            error_message = "숫자만 입력해주세요"
    
    return answer
    
def set_hide_title_flag():
    answer = -1
    error_message = ""
    while True:
        os.system("clear")
        if error_message != "":
            print(error_message)
            print("-"*20)
            error_message = ""
        
        print("챕터 제목을 가릴까요?")
        print("[1] 가린다.")
        print("[2] 가리지 않는다.")

        try:
            answer = int(input(">>> "))

            if (answer < 1) or (answer > 2):
                error_message = f"1~2 사이의 숫자를 입력해주세요."
                continue
                
            break
        except ValueError as e:
            error_message = "숫자만 입력해주세요."
    
    return answer == 1

def display_options(current_maximum_question_count, current_hide_title_flag):
    error_message = ""
    while True:
        os.system("clear")
        if error_message != "":
            print(error_message)
            error_message = ""
        
        print("--"*20)
        print("옵션 목록")
        print("\n\n")
        print("[1] 최대 문제 개수")
        v = "제한없음" if current_maximum_question_count == -1 else current_maximum_question_count
        print('\033[32m' + f"현재값 : {v}\n" + '\033[0m')
        print("최대 문제 개수를 설정하면, 딱 설정한 만큼만 문제가 나옵니다.")
        print("최대 문제 개수 제한을 없애고 싶은 경우 '-1'을 입력해주세요.")
        print("*** 올 랜덤 포함 여러 챕터를 같이 보는 경우, 모든 챕터에서 문제가 골고루 나오지 않습니다. ***")
        print("*** 최대 문제 개수가 모든 문제의 개수보다 많다면, 그냥 모든 문제가 나옵니다. ***")
        print("\n")
        print("[2] 챕터 제목 가리기")
        v = "챕터 제목이 보이지 않습니다." if current_hide_title_flag else "챕터 제목이 보입니다."
        print('\033[32m' + f"현재값 : {v}\n" + '\033[0m')
        print("챕터 제목이 정답 추론에 영향을 끼친다고 생각한다면, 가리세요!")
        print("\n")
        print("[3] 메뉴로 돌아가기")
        print("\n\n")
        print("--"*20)

        answer = -1
        error_message = ""
        try:
            answer = int(input(">>> "))

            if (answer < 1) or (answer > 3):
                error_message = f"1~3 사이의 숫자를 입력해주세요."
                continue
            
            if answer == 1:
                current_maximum_question_count = set_maximum_question_count()
            
            if answer == 2:
                current_hide_title_flag = set_hide_title_flag()
            
            break

        except ValueError as e:
            error_message = "숫자만 입력해주세요"
    
    return (current_maximum_question_count, current_hide_title_flag)