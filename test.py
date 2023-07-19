def create_user(a,b,c):
    user_info = {}
    user_info['name'] = a
    user_info['age'] = b
    user_info['city'] = c

    return user_info

info = create_user('홍길동', 30, '서울')
print (info)