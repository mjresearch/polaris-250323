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

    
bear = Doll("곰돌이", "하얀색", "왕귀여움")
bear._location()

mini_aurora = Doll("작은 오로라", "하늘색", "귀여움 초월", baby=True)
mini_aurora._location()


#1차 상속, 오버라이딩
#Doll - AnimalDoll
class AnimalDoll(Doll):   #동물인형 클래스, Doll을 상속
    def __init__(self, name: str, color: str, cute: str, animal_type: str, baby: bool = False):
        super().__init__(name, color, cute, baby)
        self.animal_type = animal_type
        #self._location()

    def _location(self) -> None:   #_location 오버라이딩
        print(f"\n{self.name}는 침실에 있어요.")
        self.show_info()

    def show_info(self) -> None:   #show_info 오버라이딩:동물종류 추가
        super().show_info()
        print(f"어떤 동물?: {self.animal_type}")
        print(f"{self.name}는 동물 친구예요!")


aurora = AnimalDoll("오로라", "하늘색", "통통 귀여움", "돌고래")
aurora._location()

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



suksoo = CharacterDoll("석수", "파란색", "얼큰 귀여움", "노보리베츠 도깨비", baby=True)
suksoo._location()


#다단계상속
#Doll - AnimalDoll - ShirinAnimalDoll
class ShirinAnimalDoll(AnimalDoll):
    def __init__(self, name: str, color: str, cute: str, \
                 animal_type: str, shirin: bool = False, baby: bool = False):
        self.shirin = shirin
        super().__init__(name, color, cute, animal_type, baby)
        self._location()

    def _location(self):
        print(f"\n{self.name} 님은 1층 창틀에 모셨어요.")
        self.show_info()
    
    def show_info(self):
        super().show_info()
        if self.shirin:
            print(f"{self.name} 님은 신사에서 모시고 왔지요.\n")


rabbit = ShirinAnimalDoll("우지토끼", "흰색", "모찌같이 귀여움", "토끼", shirin=True)
#rabbit._location()
#rabbit.show_info()

dear = ShirinAnimalDoll("나라사슴", "흰색", "똑똑하게 귀여움", "사슴", shirin=True, baby=True)

cat = ShirinAnimalDoll("행복고양이", "흰바탕에 노랑얼룩", "토실토실 귀여움", "고양이")