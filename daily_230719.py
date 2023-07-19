
# hw_3_2


# def add_numbers(num1, num2):
#     return num1 + num2

# print('3과 5를 인자로 \033[4m넘긴\033[0m 경우') 
# print(add_numbers(3, 5))


# hw_3_4

# # 1. 절댓값을 반환하는 함수 abs를 사용하여 아래 변수에 담긴 값의 절댓값을 출력하시오.
# negative = -3


# # 2. 아래 변수에 담긴 값의 boolean 값을 출력하시오.
# empty_list = []


# # 3. 주어진 리스트가 가진 모든 값을 더한 결과를 출력하시오.
# my_list = [1, 2, 3, 4, 5]
# sum = my_list[0] + my_list[1] + my_list[2] + my_list[3] + my_list[4]


# # 4. 주어진 정렬을 오름차순으로 정렬한 결과를 출력하시오.
# unsorted_list = ['하', '교', '캅', '의', '지', '가']

# clean_list = sorted(unsorted_list)

# print(abs(negative))
# print(bool(empty_list))
# print(sum)
# print(clean_list)



# 1680 ws_3_1

# number_of_people = 0


# def increase_user():
#     global number_of_people
#     number_of_people += 1
#     return bool(1>0)


# increase_user()

# print('현재 가입 된 유저 수 : ', number_of_people)


# 1681 ws_3_2


number_of_people = 0

def increase_user():
    global number_of_people
    number_of_people += 1
    return bool(1>0)

print('현재 가입 된 유저 수 :', number_of_people)

def create_user(*args):
    user_info = {}
    user_info['name'] = args[0]
    user_info['age'] = args[1]
    user_info['city'] = args[2]
    increase_user()

    return user_info

info = create_user('홍길동', 30, '서울')
name = info.get('name')


print(name +'님 환영합니다!')
print(info)
print('현재 가입 된 유저 수 :', number_of_people)



# 1682 ws_3_3

# 폴더 ws_3_3에...


 
#1683 ws_3_4

# number_of_people = 0


# def increase_user():
#     pass

# def create_user():
#     pass
    

# name = ['김시습', '허균', '남영로', '임제', '박지원']
# age = [20, 16, 52, 36, 60]
# address = ['서울', '강릉', '조선', '나주', '한성부']


# # map(create_user, name,age,address)

# for name_greeting in name:
#     print(name_greeting + '님 환영합니다!')
