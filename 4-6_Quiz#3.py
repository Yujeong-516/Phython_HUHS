#나의 답
url = "http://naver.com"
print("생성된 비밀번호 :"+ url[7 : 10] + str(len(url[7 : 12])) + str(url. count("e")) + "!")

#강의 답
url = "http://naver.com"
my_str = url. replace("http://", "") #규칙1
my_str = my_str[:my_str.index(".")] #규칙2
password = my_str[ :3 ] + str(len(my_str)) + str(my_str. count("e")) + "!"
print("{0}의 비밀번호는 {1}입니다.".format(url ,password)) 

#보완
url = input("url을 입력하세요: \n")
my_str = url. replace("http://", "")
my_str = my_str[:my_str.index(".")]
password = my_str[ :3 ] + str(len(my_str)) + str(my_str. count("e")) + "!"
print("{0}의 비밀번호는 {1}입니다.".format(url ,password))