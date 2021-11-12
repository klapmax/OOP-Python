import os
import timeit

file = open("some_file.txt", "w")
while (os.path.getsize('some_file.txt')/(1000*1000)) < 50:
    file.write('9874357643\n')

s = """
open1 = open("some_file.txt", "r")
res = 0
for line in open1.readlines():
    if line.strip().isdigit():
        res+=1
open1.close()
"""
print(timeit.timeit(s, number = 5))

s = """
open2 = open("some_file.txt", "r")
res = 0
for line in open2:
    if line.strip().isdigit():
        res+=1
open2.close()
"""
print(timeit.timeit(s, number = 5))

s = """
open3 = open("some_file.txt", "r")
res = sum(int(line.strip().isdigit()) for line in open3)
open3.close()
"""
print(timeit.timeit(s, number = 5))