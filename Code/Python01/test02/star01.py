# -*- coding:utf-8 -*-
print('------1------') 
''' 1
*
**
***
****
*****
'''
for i in range(5):
    for j in range(i+1):
        print('*', end=' ')
    print()
    
for i in range(5):
    print('*' * (i+1))
  
print('------2------') 
''' 2
*****
****
***
**
*
'''
for i in range(5):
    print('*' * (5-i))


print('------3------') 
''' 3
      *
     **
   ***
  ****
*****
'''
for i in range(5):
    print(' ' * (4-i) + '*' * (i+1))


print('------4------') 
'''
*****
 ****
   ***
    **
      *
'''
for i in range(5):
    print(' ' * (i) + '*' * (5-i))

print('------5------') 
'''
        *
      ***
    *****
  *******
*********
'''



