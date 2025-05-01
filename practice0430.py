# 예외처리

# try:
#     print("나누기 전용 계산기")
#     num1 = int(input("첫 번째 숫자를 입력하세요 : "))
#     num2 = int(input("두 번째 숫자를 입력하세요 : "))
#     print(f"{num1} / {num2} = {int(num1/num2)}")
# except ValueError:
#     print("에러! 잘못된 값 입력")


# try:
#     print("나누기 전용 계산기")
#     nums = []
#     nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
#     nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
#     nums.append(int(nums[0] / nums[1]))
#     print(f"{nums[0]} / {nums[1]} = {nums[2]}")
# except Exception as err:
#     print(err)


# try:
#     print("한 자리 숫자 나누기 전용 계산기")
#     num1 = int(input("첫 번째 숫자를 입력하세요 : "))
#     num2 = int(input("두 번째 숫자를 입력하세요 : "))
#     if num1 >= 10 or num2 >= 10:
#         raise ValueError
#     print(f"{num1} / {num2} = {int(num1/num2)}")
# except ValueError:
#     print("잘못된 값 입력! 한 자리 숫자만 입력하세요.")


# ### 사용자 정의 에러
# class BigNumberError(Exception):
#     def __init__(self, msg):
#         self.msg = msg

#     def __str__(self):
#         return self.msg
    
# try:
#     print("한 자리 숫자 나누기 전용 계산기")
#     num1 = int(input("첫 번째 숫자를 입력하세요 : "))
#     num2 = int(input("두 번째 숫자를 입력하세요 : "))
#     if num1 >= 10 or num2 >= 10:
#         raise BigNumberError(f"입력값 : {num1}, {num2}")
#     print(f"{num1} / {num2} = {int(num1/num2)}")
# except ValueError:
#     print("잘못된 값 입력! 한 자리 숫자만 입력하세요.")
# except BigNumberError as err:
#     print("에러 발생! 한 자리 숫자만 입력하세요.")
#     print(err)
# finally:
#     print("이용해주셔서 감사합니다.")


### 퀴즈(치킨집 자동주문 시스템)
"""
조건1 : 1보다 작거나 숫자가 아닌 입력값이 들어올 때 ValueError 로 처리
        출력 메시지 : "잘못된 값을 입력하였습니다."
조건2 : 대기손님이 주문할 수 있는 총 치킨량은 10마리로 한정
        치킨 소진 시 사용자 정의에러[SoldOutError]를 발생시키고 프로그램 종료
        출력 메시지 : "재고가 소진되어 더 이상 주문을 받지 않습니다."
"""

# chicken = 10
# waiting = 1  # 홀 안은 만석. 대기번호 1부터 시작

# class SoldOutError(Exception):
#     pass

# while(True):
#     try:
#         print(f"[남은 치킨 : {chicken}]")
#         order = int(input("몇 마리 주문하시겠습니까? "))
        
#         if order > chicken:
#             print("재료가 부족해요. 남은 치킨이 아래에 표시됩니다.")

#         elif not int(order) or order <= 0:
#             raise ValueError("잘못된 값을 입력했어요.")

#         else:
#             print(f"[대기 번호 {waiting}] {order} 마리 주문이 완료되었습니다.")
#             waiting += 1
#             chicken -= order    

#         if chicken == 0:
#             raise SoldOutError("치킨이 다 떨어졌어요! 다음에 다시 와주세요.^^")        
        
#     except ValueError as err:
#         print("에러 발생!!", err)
#     except SoldOutError as err:
#         print(err)
#         break



## 세련되게 리팩토링한 버전

chicken = 10
waiting = 1   # 홀 안은 만석  대기번호 1부터 시작

class SoldOutError(Exception): 
    '''치킨이 모두 소진되었을 때 방생하는 사용자정의예외'''
    pass

while(True):
    try:
        print(f"[남은 치킨 : {chicken}]")
        order_input = input("몇 마리 주문하실래요? ")

        try:
            order = int(order_input)
        except ValueError:
            raise ValueError("숫자로만 입력해주세요!")   #문자열, 소수점 입력시 에러 

        if order <= 0:
            raise ValueError("1마리 이상 주문해주세요!")
        
        elif order > chicken:
            print("남은 치킨이 부족합니다.")
            continue   # 다시 주문 받기

        else:  # 주문 성공 처리
            print(f"[대기번호 {waiting}] : {order}마리 주문완료! 감사합니다.")
            waiting += 1
            chicken -= order

        if chicken == 0:
            raise SoldOutError("치킨이 다 떨어졌어요! 다음에 다시 와주세요.")
        
    except ValueError as err:
        print(" !! 입력 오류 !! : ", err)

    except SoldOutError as err:
        print("@.@", err)
        break