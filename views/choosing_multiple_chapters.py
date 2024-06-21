def display_choosing_multiple_chapters(chapter_titles):
    print("--"*20)
    print("아래 챕터중 같이 테스트하고싶은 챕터의 번호를 빈칸을 기준으로 작성해주세요.")
    print("ex)1 2 3")
    print("\n\n")
    print("[0] 메뉴로 돌아가기")
    for idx, chapter_title in enumerate(chapter_titles):
        print(f"[{idx+1}] {chapter_title}")
    print("\n")
    print("--"*20)

    answer = -1
    choosed_chapters = 0
    error_message = ""
    while True:
        if error_message != "":
            print(error_message)
            error_message = ""
        
        answer = input(">>> ")
        chapters = answer.split(" ")
        choosed_chapters = 0

        BACK_TO_MENU = 0
        
        for chapter in chapters:
            try:
                if int(chapter) == BACK_TO_MENU:
                    choosed_chapters = 0
                    break
                
                if (int(chapter) < 1) or (int(chapter) > len(chapter_titles)):
                    error_message = f"0~{len(chapter_titles)} 사이의 숫자만 입력해야합니다." 
                    break
                
                choosed_chapters += 1 << (int(chapter)-1)
            except ValueError as e:
                error_message = "숫자만 입력해주세요."
                break
        
        if error_message == "":
            break
    
    return choosed_chapters