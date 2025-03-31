# # import random

# # user_list = list(range(1, 51))
# # count = 0

# # for user in user_list:      #for i in range(1, 51):
# #     time = random.randint(5, 50)
# #     if 5 <= time <= 15:
# #         print(f"[0] {user}번째 손님 (소요시간 : {time}분)")
# #         count += 1
# #     else:
# #         print(f"[ ] {user}번째 손님 (소요시간 : {time}분)")

# # print()
# # print(f"총 탐승 승객 : {count}명")





# def open_account():
#     print("새로운 계좌가 생성되었습니다.")

# def deposit(balance, money):
#     print(f"입금이 완료되었습니다. 잔액은 {balance + money}원 입니다.")
#     return balance + money

# def withdraw(balance, money):
#     if balance >= money:
#         print(f"출금이 완료되었습니다. 잔액은 {balance - money}입니다.")
#         return balance - money
#     else:
#         print(f"출금이 되지 않았습니다. 잔액은 {balance}입니다.")
#         return balance

# def withdraw_night(balance, money):
#     commision = 100
#     return commision, balance - money - commision
    

# balance = 0
# balance = deposit(balance, 1000)
# balance = withdraw(balance, 500)
# commision, balance = withdraw_night(balance, 500)
# print(f"수수료는 {commision}이며, 잔액은 {balance}입니다.")





# def profile(name, age, main_lang):
#     print(f"이름 : {name}\t 나이 : {age}\t 주 언어 : {main_lang}")

# profile("김명희", 44, "python")
# profile("서정우", 52, "JAVA")

# def profile(name, age=44, main_lang="python"):
#     print(f"이름 : {name}\t 나이 : {age}\t 주 언어 : {main_lang}")

# profile("김명희")
# profile("모규")

# def profile(name, age, main_lang):
#     print(name, age, main_lang)

# profile(age=44, main_lang="python", name="김명희")


def profile(name, age, *language):
    print(f"이름 : {name}\t 나이 : {age}\t", end=" ")
    for lang in language:
        print(lang, end=" ")
    print()

profile("김명희", 44, "python", "C++", "JAVA")