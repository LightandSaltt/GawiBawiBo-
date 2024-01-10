import random

def gbb_game():
    game_result = 0
    
    user_choice = input("가위, 바위, 보 중 하나를 선택 후 입력해 주세요: ")

    ai_choice = random.choice(["가위", "바위", "보"])

    while game_result == 0:
        if user_choice == ai_choice:
            print("유저의 선택 : {} / ai의 선택 : {}".format(user_choice, ai_choice));
            print("비겼습니다. 다시 한 번 더!")
        elif (user_choice == "가위" and ai_choice == "보") or \
             (user_choice == "바위" and ai_choice == "가위") or \
             (user_choice == "보" and ai_choice == "바위"):
            print("유저의 선택 : {} / ai의 선택 : {}".format(user_choice, ai_choice));
            print("승리했습니다!")
            game_result = 1
        else:
            print("유저의 선택 : {} / ai의 선택 : {}".format(user_choice, ai_choice));
            print("패배했습니다...")
            break;

gbb_game()
