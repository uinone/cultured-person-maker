import random
import os

def display_quiz(datas, maximum_question_count):
    random.shuffle(datas)

    if (maximum_question_count != -1) and (maximum_question_count < len(datas)):
        datas = datas[:maximum_question_count]

    error_message = ""

    for idx, (c, q, a) in enumerate(datas):
        os.system("clear")
        print("--"*20)
        print(f"[{c}] {idx+1}/{len(datas)}")
        print(f"\n\n{q}\n\n")
        print("--"*20)
        input(">>> ")
        print("--"*20)
        print("\n\n")
        print(f"[정답] ", end="")
        for _a in a:
            print(_a, end="  ")
        print()
        print("\n\n")
        print("--"*20)
        print("[ENTER] 다음문제로, [1] 메뉴로")

        answer = -1
        while True:
            if error_message != "":
                print(error_message)
                error_message = ""
            
            try:
                inp = input(">>> ")
                answer = int(inp)

                if answer != 1:
                    error_message = "메뉴로 가고싶다면 1을 입력해주세요."
                    continue
                break
            except ValueError as e:
                if inp == "":
                    answer = -1
                    break
                else:
                    error_message = "ENTER 혹은 1을 입력해주세요."
        
        if answer == -1:
            continue
        else:
            break
