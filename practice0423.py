# 상속

class Doll:
    def __init__(self, name: str, color: str, cute: str, baby: bool = False) -> None:
        self.name = name
        self.color = color
        self.cute = cute
        self.baby = baby
        
    def _location(self) -> None:     #기본 인형의 위치 출력
        print(f"\n{self.name}는 2층에 있어요.")
        self.show_info()

    def show_info(self) -> None:      #공통 정보 출력
        print(f"이름: {self.name}")
        print(f"색상: {self.color}")
        print(f"귀여움 지수: {self.cute}")
        if self.baby:
            print(f"{self.name}는 아기 인형이에요!")

    

#1차 상속, 오버라이딩
#Doll - AnimalDoll
class AnimalDoll(Doll):   #동물인형 클래스, Doll을 상속
    def __init__(self, name: str, color: str, cute: str, animal_type: str, baby: bool = False):
        super().__init__(name, color, cute, baby)
        self.animal_type = animal_type
        

    def _location(self) -> None:   #_location 오버라이딩
        print(f"\n{self.name}는 침실에 있어요.")
        self.show_info()

    def show_info(self) -> None:   #show_info 오버라이딩:동물종류 추가
        super().show_info()
        print(f"어떤 동물?: {self.animal_type}")
        print(f"{self.name}는 동물 친구예요!")


#Doll - CharaterDoll
class CharacterDoll(Doll):   #캐릭터인형 클래스. Doll을 상속
    def __init__(self, name: str, color: str, cute: str, character_origin: str, baby: bool = False):
        super().__init__(name, color, cute, baby)
        self.character_origin = character_origin

    def _location(self) -> None:    #_location 오버라이딩
        print(f"\n{self.name}는 침실에 있어요.")
        self.show_info()
    
    def show_info(self) -> None:    #show_info 오버라이딩 : 캐릭터 정보 추가
        super().show_info()
        print(f"누구?: {self.character_origin}")
        print(f"{self.name}는 유명한 캐릭터예요!")



#다단계상속
#Doll - AnimalDoll - ShirinAnimalDoll
class ShirinAnimalDoll(AnimalDoll):
    def __init__(self, name: str, color: str, cute: str, \
                 animal_type: str, shirin: bool = False, baby: bool = False):
        self.shirin = shirin
        super().__init__(name, color, cute, animal_type, baby)       

    def _location(self):
        print(f"\n{self.name} 님은 1층 창틀에 모셨어요.")
        self.show_info()
    
    def show_info(self):
        super().show_info()
        if self.shirin:
            print(f"{self.name} 님은 신사에서 모시고 왔지요.\n")



####인형들을 리스트로 묶고, 조건에 따라 분류하거나 출력하기###

# 인형 객체 생성
bear = Doll("곰돌이", "하얀색", "왕귀여움")
mini_aurora = Doll("작은 오로라", "하늘색", "귀여움 초월", baby=True)
aurora = AnimalDoll("오로라", "하늘색", "통통 귀여움", "돌고래")
suksoo = CharacterDoll("석수", "파란색", "얼큰 귀여움", "노보리베츠 도깨비", baby=True)
rabbit = ShirinAnimalDoll("우지토끼", "하얀색", "모찌같이 귀여움", "토끼", shirin=True)
dear = ShirinAnimalDoll("나라사슴", "하얀색", "똑똑하게 귀여움", "사슴", shirin=True, baby=True)
cat = ShirinAnimalDoll("행복고양이", "흰바탕에 노랑얼룩", "토실토실 귀여움", "고양이")


from typing import List

#인형리스트 생성
doll_collection: List[Doll] = \
    [bear, mini_aurora, aurora, suksoo, rabbit, dear, cat] 

print("\n<<전체 인형 위치와 정보 출력>> ")
for doll in doll_collection:
    doll._location()

#아기 인형만 출력하기
def print_baby_dolls(dolls: List[Doll]) -> None:
    print(f"\n<아기 인형을 소개할게요>")
    for doll in dolls:
        if doll.baby:
            doll._location()

print_baby_dolls(doll_collection)


#색깔별로 구분해서 출력하기
def print_doll_by_color(dolls: List[Doll], color: str) -> None:
    print(f"\n<{color} 인형을 소개할게요>")
    for doll in dolls:
        if doll.color == color:
            doll._location()

print_doll_by_color(doll_collection, "하늘색")
print_doll_by_color(doll_collection, "하얀색")

#동물인형만 출력하기
def print_animal_dolls(dolls: List[Doll]) -> None:
    print(f"\n<동물 인형을 소개할게요>")
    for doll in dolls:
        if isinstance(doll, AnimalDoll): ##잘보기
            doll._location()

print_animal_dolls(doll_collection)

#신사 인형들만 출력
def print_shirin_dolls(dolls: List[Doll]) -> None:
    print(f"\n\n\n\n\n<신사에서 모셔 왔어요>")
    for doll in dolls:
        if isinstance(doll, ShirinAnimalDoll) and doll.shirin:  ##잘보기
            doll._location()

print_shirin_dolls(doll_collection)