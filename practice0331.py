# gun = 10

# def checkpoint(soldiers):
#     global gun
#     gun = gun - soldiers
#     print(f"[def 내] 남은 총 : {gun}")



# print(f"전체 총 : {gun}")
# checkpoint(2)
# print(f"남은 총 : {gun}")



# 표준체중을 구하는 프로그램
# by me

def std_weight(height, gender):
    if gender == "남자":
        result = ((height * 0.01) ** 2) * 22
    if gender == "여자":
        result = ((height * 0.01) ** 2) * 21
    print(f"키 {height}cm {gender}의 표준체중은 {result:.2f}kg 입니다.")

std_weight(154, "여자")
std_weight(172, "남자")

# 쌤 해설
def std_weight(height, gender):
    if gender == "남자":
        return height * height * 22
    else:
        return height * height * 21
    
height = 154
gender = "여자"
weight = round(std_weight(height / 100, gender), 2)
print(f"키 {height}cm {gender}의 표준체중은 {weight}kg 입니다.")

