import time

"""
기본출력

[출력값]
hello
"""
print("hello")


"""
문자열 연산

[출력값]
ABC DEF GHI
"""
print("ABC " + "DEF " + "GHI")


"""
한 줄 띄우기

[출력값]
첫번째줄
두번째줄
"""
print("첫번째줄\n두번째줄")


"""
줄 바꾸지 않고 이어서 출력

[출력값]
옆에 이어서 글이 출력된다.
"""
print("옆에 이어서 ", end="")
print("글이 출력된다.")


"""
변수처리

[출력값]
나의 이름은 = 춘향 / 나이 = 18 / 몸무개 = 30.130
"""
name = "춘향"
age = 18
height = 30.13
print("나의 이름은 = %s / 나이 = %s / 몸무개 = %0.3f" %(name, age, height))
print("나의 이름은 = " + name +"  / 나이 = " + str(age) + " / 몸무개 = " + str(height))

"""
긴글 출력

[출력값]

동해물과 백두산이
마르고 닳도록
하느님이 보우하사
"""
txt = """
동해물과 백두산이
마르고 닳도록
하느님이 보우하사
"""
print(txt)