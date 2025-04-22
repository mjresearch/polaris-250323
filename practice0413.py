class Doll:
    def __init__(self, name: str, color: str, cute: str, baby: bool = False) -> None:
        self.name = name
        self.color = color
        self.cute = cute
        self.baby = baby
        self._location()

    def _location(self) -> None:
        print(f"{self.name}는 2층에 있어요.")
        self.show_info()

    def show_info(self) -> None:
        print(f"이름: {self.name}")
        print(f"색상: {self.color}")
        print(f"귀여움 지수: {self.cute}")
        if self.baby:
            print(f"{self.name}는 아기 인형이에요!")
        print("-" * 30 + "\n")

    
bear = Doll("곰돌이", "하얀색", "왕귀여움")
mini_aurora = Doll("작은 오로라", "하늘색", "귀여움 초월", baby=True)

bear.show_info()
mini_aurora.show_info()
