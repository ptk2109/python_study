from var_dump import var_dump
from pprint import pprint

# 일반적으로 1차원 딕셔너리 시작 =======================================
KEY_VALUE_NAME_AGE_ = """
var_dump(test)

# for 사용 
for key in test.keys():
    print(key, " : ", test[key])
# 출력
#    name: 홍길동
#    age: 15


print("=========================")
print("key() 사용안해도 같구만...")
for key in test:
    print(key, " : ", test[key])
# 출력
#   name
#   age

print("=========================")
print("items() 사용  // 이게 좋네!")
for key, value in test.items():
    print(key, " : ", value)
# 출력
#   name  :  홍길동
#   age  :  15
"""
test = {"name": "홍길동", "age": 15}
# 일반적으로 1차원 딕셔너리 끝 =======================================



# 2차원 딕셔너리 시작 ===============================================
test2 = {
    0: {"name": "홍길동", "age": 15},
    1: {"name": "임꺽정", "age": 18},
}
"""
print(test2)
# 출력 : {'0': {'age': 15, 'name': '홍길동'}, '1': {'age': 18, 'name': '임꺽정'}}

# 항목 값 치환
test2["0"]["name"] = "임순이"
print(test2)
# 출력 : {'0': {'name': '임순이', 'age': 15}, '1': {'name': '임꺽정', 'age': 18}}
"""
for key, row in test2.items():
    print("name = %s // age = %s" % (row['name'], row['age']))

# 2차원 딕셔너리 끝 =================================================



