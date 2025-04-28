# 다중상속
class Doll:
    def __init__(self, name: str, color: str, cute: str, baby: bool = False) -> None:
        self.name = name
        self.color = color
        self.cute = cute
        self.baby = baby
        
    def location(self) -> None:     #기본 인형의 위치 출력
        print(f"\n{self.name}는 2층에 있어요.")
        self.show_info()

    def show_info(self) -> None:      #공통 정보 출력
        print(f"이름: {self.name}")
        print(f"색상: {self.color}")
        print(f"귀여움 지수: {self.cute}")
        if self.baby:
            print(f"{self.name}는 아기 인형이에요!")

#super() + *args, **kwargs 체인으로 각 부모가 한 번씩만 초기화되게 만들기
#다중 상속 시 super().__init__(*args, **kwargs) 패턴으로 충돌 없이 전달

# #1차 상속, 오버라이딩
# #Doll - AnimalDoll
class AnimalDoll(Doll):
    def __init__(self, animal_type: str, *args, **kwargs):
        self.animal_type = animal_type
        super().__init__(*args, **kwargs)        

    def location(self) -> None:   #_location 오버라이딩
        print(f"\n{self.name}는 침실에 있어요.")
        self.show_info()

    def show_info(self) -> None:   #show_info 오버라이딩:동물종류 추가
        super().show_info()
        print(f"어떤 동물?: {self.animal_type}")
        print(f"{self.name}는 동물 친구예요!")


# #Doll - CharaterDoll
# class CharacterDoll(Doll):   #캐릭터인형 클래스. Doll을 상속
class CharacterDoll(Doll):
    def __init__(self, character_origin: str, *args, **kwargs):
        self.character_origin = character_origin
        super().__init__(*args, **kwargs)

    def location(self) -> None:    #_location 오버라이딩
        print(f"\n{self.name}는 침실에 있어요.")
        self.show_info()
    
    def show_info(self) -> None:    #show_info 오버라이딩 : 캐릭터 정보 추가
        super().show_info()
        print(f"누구?: {self.character_origin}")
        print(f"{self.name}는 유명한 캐릭터예요!")


#다중상속 #다중 상속 시 super().__init__(*args, **kwargs) 패턴으로 충돌 없이 전달

class MeanigDoll(AnimalDoll, CharacterDoll):
    def __init__(self, meaning: str, *args, **kwargs):
        self.meaning = meaning
        super().__init__(*args, **kwargs)

    def location(self):
        self.show_info()

    def show_info(self):
        super().show_info()
        print(f"의미: {self.meaning}")
        print(f"{self.name}는 행복과 돈을 불러와요!")


cat = MeanigDoll(name="행복고양이",
                  color="흰색바탕노란얼룩이",
                  cute="통통하게 귀여움",
                  animal_type="고양이",
                  character_origin="시아와세네코",
                  meaning="행복과 돈",
                  baby=False)
cat.location()

# MRO(Method Resolution Order)확인해보기
for cls in MeanigDoll.mro():
    print(cls.__name__)
