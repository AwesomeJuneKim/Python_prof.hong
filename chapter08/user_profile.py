def build_profile(first, last, **user_info):
    """사용자에 대해 아는 정보를 전부 딕셔너리에 저장합니다."""
    user_info['first_name']=first.title()
    user_info['last_name']=last.title()
    return user_info

# user_profile= build_profile('hong', 'gildong', location='busan', field='computer')

# print(user_profile)
#->다른 파일에서 홍길동을 출력하지 않기 위해 주석처리 함