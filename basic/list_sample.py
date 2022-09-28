from var_dump import var_dump

bird = []
bird = ["오리", "새"]

# 3번째 항목에 추가
bird.insert(3,"참새")
print(bird)

# 맨뒤에 추가
bird.append("뻐구기")
print(bird)

# 다차원배열은 만들기
bird.append(["기러기", "소쩍새"])
print(bird)
var_dump(bird)

# 기러기 값 가져오기
print(bird[4][0])


# tuple로 치환
var_dump(tuple(bird))