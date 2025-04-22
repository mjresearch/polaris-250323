# 상속

class Doll:
    def __init__(self, name: str, color: str, cute: str, baby: bool = False) -> None:
        self.name = name
        self.color = color
        self.cute = cute
        self.baby = baby
        

    def _location(self) -> None:
        print(f"\n{self.name}는 2층에 있어요.")
        self.show_info()

    def show_info(self) -> None:
        print(f"이름: {self.name}")
        print(f"색상: {self.color}")
        print(f"귀여움 지수: {self.cute}")
        if self.baby:
            print(f"{self.name}는 아기 인형이에요!")

    
bear = Doll("곰돌이", "하얀색", "왕귀여움")
bear._location()
mini_aurora = Doll("작은 오로라", "하늘색", "귀여움 초월", baby=True)
mini_aurora._location()


class AnimalDoll(Doll):
    def __init__(self, name: str, color: str, cute: str, animal_type: str, baby: bool = False):
        super().__init__(name, color, cute, baby)
        self.animal_type = animal_type
        self._location()

    def show_info(self) -> None:
        super().show_info()
        print(f"어떤 동물?: {self.animal_type}")
        print(f"{self.name}는 동물 친구예요! \n")

aurora = AnimalDoll("오로라", "하늘색", "통통 귀여움", "돌고래")

class CharacterDoll(Doll):
    def __init__(self, name: str, color: str, cute: str, character_origin: str, baby: bool = False):
        super().__init__(name, color, cute, baby)
        self.character_origin = character_origin
        self._location()

    def show_info(self) -> None:
        super().show_info()
        print(f"누구?: {self.character_origin}")
        print(f"{self.name}는 유명한 캐릭터예요! \n")

suksoo = CharacterDoll("석수", "파란색", "얼큰 귀여움", "노보리베츠 도깨비", baby=True)