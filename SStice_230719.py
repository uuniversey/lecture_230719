

# def greeting(name, age):
#     print(f'안녕, {name}, {age}!!')


# greeting('Ailce', 25)

# greeting(25, 'Ailce')

# greeting(age=25, name='Alice')

# # greeting(age=25, 'Dave')



# print('hi', 'aaa', 'bbb')



# def calculate_sum(*args):
#     print(args) # (1, 2, 3, 4, 5)

# calculate_sum(1, 2, 3, 4, 5)



# def calculate_sum(**kwargs):
#     print(kwargs) 
#     # {'name': 'Alice', 'age': 30, 'address': 'korea'}

# calculate_sum(name = 'Alice', age =30, address='korea')


# def factorial(n):

#     if n == 0:
#         return 1
      
#     return n * factorial(n-1)
# result = factorial(5)
# print(result)


# numbers = [1, 2, 3]
# result = map(str, numbers) 

# print(result) # <map object at 0x000001E2C63703D0>
# print(list(result)) # ['1', '2', '3']


# result = []
# for number in numbers:
#     result.append(str(number))

# print(result)


# names = ['Alice', 'Bob', 'Charlie']
# ages = [30, 25, 35]
# cities = ['New York', 'London', 'Paris']

# for name, age, city in zip(names, ages, cities):
#     print(name, age, city)

# # Alice 30 New York
# # Bob 25 London
# # Charlie 35 Paris


# numbers = [1, 2, 3, 4, 5]
# result = map(lambda x: x * 2, numbers)
# print(result) # [2, 4, 6, 8, 10]



# my_list = [1, 2, 3, 4, 5]

# print(my_list) # [1, 2, 3, 4, 5]
# print(*my_list) # 1 2 3 4 5
# print(1, 2, 3, 4, 5)


# # packing : 함수가 정의될 때 사용
# def my_func(*args):
#     print(args)

# my_func('a', 'b', 'c')

# # unpacking : 함수를 호출할 때 사용

# my_func(my_list)   # ㅎ
# my_func(*my_list)  #




# def my_func_2(**kargs):
#         print(kargs)

# my_func_2(apple = '맛있어', banana = '노란색', coconut = '지코')


# my_dict = {
#         'apple' : '맛있어',
#         'banana' : '노란색',
#         'coconut' : '달콤해',
#     }

# # my_func_2(**my_dict)

# # 위치 인자로 키워드 인자를 받으려면 매개변수에 신경을 써야한다!!
# def my_func_3(apple, banana, coconut):
#         print(apple, banana, coconut)

# # dictionary를 언패킹 할 떄 dict의 key 이름과 매개변수명이 같은지를 확인하자!!


# my_func_3(**my_dict) # 맛있어 노란색 달콤해


# import math
 
# print(math.pi)

# help(math)



####### 사용자 정의 모듈 사용해보기

# # 미리 my_math.py 파일에 def add를 해놓음
# def add(input_1, input_2):
#     return input_1 + input_2

# # 1번 방법
# import my_math
# result = my_math.add(100, 25)
# print(result)

# # 2번 방법
# from my_math import add
# result = add(300, 75)
# print(result)



