# -*- coding:utf-8 -*-

import pickle

file = open('test02.txt', 'rb')   #binary를 읽어올겨
score = pickle.load(file)
file.close()

print(score)

