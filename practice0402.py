# #
# # scores = {"수학":100, "영어":100, "코딩":50}
# # for subject, score in scores.items():
# #     #print(subject, score)
# #     print(subject.ljust(4), str(score).rjust(5), sep=":")


# #
# # for num in range(1, 21):
# #     print(f"대기번호 : {num:03}")

# #
# # hello = input("오늘 날씨 어때요? ")
# # print("그래요, 날마다 좋은 날인 거 아시죠? ^^")
   

# print(f"{500: >10}")

# print(f"{500: >+10}")
# print(f"{-500: >+10}")

# print(f"{500:_<+10}")

# print(f"{10000000000:,}")
# print(f"{10000000000:+,}")
# print(f"{10000000000:^<+30,}")

# print(f"{5/3:f}")
# print(f"{5/3:.2f}")


##
# score_file = open("score.txt", "w", encoding="utf8")
# print("수학 : 100", file=score_file)
# print("영어 : 100", file=score_file)
# score_file.close() 

# score_file = open("score.txt", "a", encoding="utf8")
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 60")
# score_file.close()


# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read())
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline())
# print(score_file.readline())
# print(score_file.readline())
# print(score_file.readline())
# score_file.close()

with open("score.txt", "r", encoding="utf8") as score_file:
    for line in score_file:
        print(line.strip())