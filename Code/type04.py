# tuple : list와 거의 같다.


#생성자 사용
a=tuple()
print(a)
#a.append(1)  #tuple에는 append() 속성이  없음
#print(a)

#b=tuple(1,2,3,4)   #tuple에는 하나만 들어가야 한다.
b=tuple([1,2,3,4])
print(b)

list_b = list(b)
print(list_b)
list_b.append(5)
print(list_b)



#()사용
c=(1,2,'3')
print(c)


#tuple + tuple
d = b+c
print(d)


#unpacking
e=(1,2,3,4)
f,g,h,i = e
print(f)
print(g)
print(h)
print(i)





