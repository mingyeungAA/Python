#문자 (single quotation) / double quotation 의 차이 없음)


#single * 1
a='Hello, Python!'
print(a)

b='python\'s \nHello, World!'
print(b)


#single * 3 (써준거 그대로 출력됨)
b='''python's
Hello, World!        !!!!
     Hello, Python'''
print(b)



#double * 1
c="python's \nHello, World!"
print(c)

d="python's \n\"Hello, World!\""
print(d)



#double * 3

d="""python's
"Hello, World!" """
print(d)


e="c:\\test"
print(e)


# raw string : \를 문자로 인식 
f=r"c:\test"
print(f)


str01 = "Hello, "
str02="World!"
print(str01+str02)
print(str01*3+str02)

