### append 와 isinstance 에 대해여

# class Doll:
#     def __init__(self, name: str, color: str, cute: str, baby: bool = False) -> None:
#         self.name = name
#         self.color = color
#         self.cute = cute
#         self.baby = baby

#     def show_detail(self):
#         baby_status = "아기인형" if self.baby else " "  #if-else 로 bool형도 출력
#         print(self.name, self.color, self.cute, baby_status)

# Dolls = []
# doll1 = Doll("곰돌이", "하얀색", "왕귀여움")
# doll2 = Doll("작은오로라", "하늘색", "초귀여움", True)

# Dolls.append(doll1)
# Dolls.append(doll2)

# for i in Dolls:     #관례적으로 클래스는 대분자, 인스턴스는 소문자를 쓴다
#     i.show_detail()



class Doll:
    def __init__(self, name: str, color: str, cute: str, baby: bool = False) -> None:
        self.name = name
        self.color = color
        self.cute = cute
        self.baby = baby

    def show_detail(self):
        baby_status = "아기인형" if self.baby else " "  #if-else 로 bool형도 출력
        print(self.name, self.color, self.cute, baby_status)

class DollCollection:
    def __init__(self):
        self.dolls = []  #인형을 담을 리스트 준비

    def add_doll(self, doll):
        if isinstance(doll, Doll):
            self.dolls.append(doll)
            print(f"{doll.name}는 우리집 인형이에요!")
        else:
            print(f"{doll}은 인형이 아니에요.")

    def show_all_dolls(self):
        print("\n--우리집 인형들--")
        for doll in self.dolls:
            doll.show_detail()


# 인형 만들기
doll1 = Doll("곰돌이", "하얀색", "왕귀여움")
doll2 = Doll("작은오로라", "하늘색", "초귀여움", True)

# 인형 모음집 만들기
my_collection = DollCollection()

# 인형을 모음집에 추가
my_collection.add_doll(doll1)
my_collection.add_doll(doll2)
my_collection.add_doll("나는 인형이 아니야!")  # 실수로 추가하면 경고!
my_collection.add_doll("피구들")             # 문자열
my_collection.add_doll(123)                    # 숫자
my_collection.add_doll(["인형 리스트?"])         # 리스트
my_collection.add_doll({'name': '인형'})         # 딕셔너리

# 모든 인형 출력
my_collection.show_all_dolls()