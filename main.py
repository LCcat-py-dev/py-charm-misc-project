import random

def LCcat_num():
    num = random.randint(0,9)
    return num
def num_size(count):
    nums = 0
    n = len(count)
    for i in range(n):
        for j in range(i + 1 , n):
            if count[i] > count[j]:
                nums += 1
    return nums

length = random.randint(3,9)
count = []
while len(count) < length:
    num = LCcat_num()
    if num in count:
        continue
    count.append(num)
print("随机生成的数字为：")
print(count)

if num_size(count) % 2 == 0:
    print("偶")
else:
    print("奇")

num1,num2 = random.sample(range(length),2)
count[num1],count[num2] = count[num2],count[num1]
print(count)

if num_size(count) % 2 == 0:
    print("偶")
else:
    print("奇")