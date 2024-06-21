def display_menu(chapter_titles):
    CHOOSE_MULTIPLE_CHAPTERS = len(chapter_titles) + 1
    ALL_RANDOM = len(chapter_titles) + 2
    OPTION = len(chapter_titles) + 3
    EXIT = len(chapter_titles) + 4
    ERROR = -1
    
    print("--"*20)
    print("보기중에 하나를 골라주세요")

    for idx, chapter_title in enumerate(chapter_titles):
        print(f"[{idx+1}] {chapter_title}만 랜덤")
    
    print(f"[{CHOOSE_MULTIPLE_CHAPTERS}] 몇개 골라서 랜덤")
    print(f"[{ALL_RANDOM}] 모조리 랜덤")
    print(f"[{OPTION}] 옵션")
    print(f"[{EXIT}] 종료")
    print("--"*20)
    
    error_message = ""
    try:
        answer = int(input(">>> "))

        if (answer < 1) or (answer > EXIT):
            error_message = f"1~{EXIT} 사이의 숫자를 입력해주세요."
            answer = ERROR
    except ValueError as e:
        error_message = "숫자만 입력해주세요"
        answer = ERROR
    
    return (answer, error_message)