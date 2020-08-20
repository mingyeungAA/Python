#dictionary (순서 없음, 키는 없고 value는 있다 = map)


#생성자 사용
dict01 = dict()
dict01[1] = 'one'
dict01['two']=2
print(dict01)



#{} 사용
dict02 = {}
dict02['one'] = 1
dict02[2] = 'two'
dict02[3] = 3
print(dict02)



# key를 통해 value값 가져오기
print(dict01.get(1))
print(dict02['one'])

print(dict02.keys())   #key만 가져오는
print(dict02.values())   #value만 가져오는 


print(type(dict02.keys()))
print(list(dict02.keys()))   #해당 key 값들이 list에 담김
print(list(dict02.keys())[0])   #그 list에서 값 하나만 출력가능함


