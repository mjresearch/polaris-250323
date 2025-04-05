# import pickle

# profile = {"이름":"모규", "나이":44, "잘하는 것":["공부", "정돈", "글쓰기"]} 

# with open("profile.pkl", "wb") as profile_file:
#     pickle.dump(profile, profile_file)
#     print(profile)

# with open("profile.pkl", "rb") as profile_file:
#     profile = pickle.load(profile_file)
#     print(profile)
    

# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬 공부하고 있어요.^^")

# with open("study.txt", "r", encoding="utf8") as study_file:
#     print(study_file.read())


# # 퀴즈

# import os

# if not os.path.exists("work"):
#     os.mkdir("work")

# for week in range(1, 51):
#     report = f"work/{week}주차.txt"
#     with open(report, "w", encoding="utf8") as file:
#         file.write(f" - {week}주차 주간보고 - \n\n부서 : \n이름 : \n업무 요약 : \n")

# for week in range(1, 51):
#     report = f"work/{week}주차.txt"
#     with open(report, "r", encoding="utf8") as file:
#         print(file.read())

    


# class Unit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print(f"{self.name} 유닛이 생성되었습니다.")
#         print(f"체력 {self.hp}, 공격력 {self.damage}")

# marine1 = Unit("마린", 40, 5)

### class 
# class doll:
#     def __init__(self, name, color, cute):
#         self.name = name
#         self.color = color
#         self.cute = cute
#         print(f"\n{self.name}는 2층에 있습니다.")
#         print(f"색상 : {self.color} \n귀여움 지수 : {self.cute}\n")

# bear = doll("곰돌이", "하얀색", "왕귀여움")
# suksoo = doll("석수", "파란색", "초귀여움")

# orora = doll("오로라", "하늘색", "아주 귀여움")
# print(f"이름 : {orora.name} \n색상 : {orora.color} \
#       \n귀여운 정도 : {orora.cute}\n")

# orora_mini = doll("작은 오로라", "하늘색", "귀여움 초월")
# orora_mini.baby = True

# if orora_mini.baby == True:
#     print(f"{orora_mini.name}는 아기입니다.\n")


class Doll:
    def __init__(self, name, color, cute, baby=False):
        self.name = name
        self.color = color
        self.cute = cute
        self.baby = baby
        self.location()

    def location(self):
        print(f"\n{self.name}는 2층에 있습니다.")
        self.info()

    def info(self):
        print(f"색상 : {self.color}")
        print(f"귀여움 지수 : {self.cute}")
        if self.baby:
            print(f"{self.name}는 아기입니다.\n")

bear = Doll("곰돌이", "하얀색", "왕귀여움")
suksoo = Doll("석수", "파란색", "초귀여움")
orora = Doll("오로라", "하늘색", "아주 귀여움")

print(f"\n이름 : {bear.name} \n색상 : {bear.color} \
      \n귀여운 정도 : {bear.cute}\n")

orora_mini = Doll("작은 오로라", "하늘색", "귀여움 초월", baby=True)