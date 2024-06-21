import json
import os
import sys

from views.menu import display_menu
from views.quiz import display_quiz
from views.choosing_multiple_chapters import display_choosing_multiple_chapters
from views.options import display_options

def get_dataset():
    dataset = None
    try:
        if sys.argv[1].split(".")[-1] != "json":
            print(f"\n\njson 형식의 파일만 데이터셋으로 사용할 수 있습니다.\n\n")
            return None
        
        with open(sys.argv[1], "r") as f:
            dataset = json.load(f)
    except FileNotFoundError as _:
        print(f"\n\n{sys.argv[1]}이란 파일이 존재하지 않습니다.\n\n")
    except IndexError as _:
        print(f"\n\n데이터셋 파일의 경로와 함께 실행해주세요.")
        print("ex)python3 main.py ./dataset/cyber.json\n\n")
    return dataset

dataset = get_dataset()
CHAPTER_TITLES = list(dataset.keys()) if dataset is not None else []

RUNNING_FLAG = True
MENU_FLAG = True
CHAPTER_FLAGS = 0

CHOOSING_MULTIPLE_CHAPTER_FLAG = False
CHOOSING_OPTION_FLAG = False

# Options
MAXIMUM_QUESTION_COUNT = -1
HIDE_TITLE_FLAG = False

CHOOSE_MULTIPLE_CHAPTERS = len(CHAPTER_TITLES) + 1
ALL_RANDOM = len(CHAPTER_TITLES) + 2
OPTION = len(CHAPTER_TITLES) + 3
EXIT = len(CHAPTER_TITLES) + 4
ERROR = -1

def reset_flags():
    global MENU_FLAG, CHAPTER_FLAGS, CHOOSING_MULTIPLE_CHAPTER_FLAG, CHOOSING_OPTION_FLAG
    MENU_FLAG = True
    CHAPTER_FLAGS = 0

    CHOOSING_MULTIPLE_CHAPTER_FLAG = False
    CHOOSING_OPTION_FLAG = False

if __name__ == "__main__":
    if CHAPTER_TITLES == []:
        exit()

    chapters = []

    answer = -1
    error_message = ""
    
    while RUNNING_FLAG:
        chapters.clear()
        for chapter_title, chapter_data in dataset.items():
            if HIDE_TITLE_FLAG:
                chapter = [( "*"*5, q, a) for q, a in list(dataset[chapter_title].items())]
            else:
                chapter = [(chapter_title, q, a) for q, a in list(dataset[chapter_title].items())]
            
            chapters.append(chapter)
        
        os.system("clear") # For MacOS

        if MENU_FLAG:
            if error_message != "":
                print(error_message)
                error_message = ""
            answer, error_message = display_menu(CHAPTER_TITLES)

            if answer == ERROR:
                continue
            
            if answer == EXIT:
                break

            MENU_FLAG = False

            if answer == CHOOSE_MULTIPLE_CHAPTERS:
                CHOOSING_MULTIPLE_CHAPTER_FLAG = True
                continue

            if answer == ALL_RANDOM:
                CHAPTER_FLAGS = (1<<len(CHAPTER_TITLES)) - 1
                continue

            if answer == OPTION:
                CHOOSING_OPTION_FLAG = True
                continue

            CHAPTER_FLAGS = 1 << (answer - 1)
            continue

        if CHOOSING_MULTIPLE_CHAPTER_FLAG:
            CHAPTER_FLAGS = display_choosing_multiple_chapters(CHAPTER_TITLES)

        if CHOOSING_OPTION_FLAG:
            MAXIMUM_QUESTION_COUNT, HIDE_TITLE_FLAG = display_options(MAXIMUM_QUESTION_COUNT, HIDE_TITLE_FLAG)

        if CHAPTER_FLAGS > 0:
            chapter_flags = (str(bin(CHAPTER_FLAGS))[2:]).rjust(len(CHAPTER_TITLES), "0")[::-1]
            chapter_flags = [True if flag=="1" else False for flag in chapter_flags]

            datas = None
            for chapter_idx, flag in enumerate(chapter_flags):
                if flag:
                    if datas == None:
                        datas = chapters[chapter_idx]
                    else:
                        datas = datas + chapters[chapter_idx]
            
            display_quiz(datas, MAXIMUM_QUESTION_COUNT)
        
        reset_flags()