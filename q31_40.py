#q31 34

# q33
print("-" * 80)

# q34
t1 = 'python'
t2 = 'java'
print((t1+' '+t2+' ') * 4)

# q35
name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13
print("이름: %s 나이: %d" % (name1, age1))
print("이름: %s 나이: %d" % (name2, age2))

# q36
print("이름: {0} 나이: {1}".format(name1, age1))
print("이름: {0} 나이: {1}".format(name2, age2))

#q37
print(f"이름: {name1} 나이: {age1}")
print(f"이름: {name2} 나이: {age2}")

# q38
n = "5,969,782,550"
print(int(n.replace(",","")))

# q39
n = "2020/03(E) (IFRS연결)"
print(n.split("(")[0])

# q40
data = "   삼성전자    "
print(data.replace(" ", ""))
print(data.strip())     # strip 메서드를 쓰면 좌우 공백 제거 가능 . 원본 문자열은 유지되고 공백이 제거된 새로운 문자열 반환