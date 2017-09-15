def get_data(data):
    """
    
    :param data: user data
    :return: user detail parameters needed to show
    """
    user_data = []
    for user in data:
        users = {}
        users['login'] = user.get('login')
        users['url'] = user.get('url')
        users['avatar_url'] = user.get('avatar_url')
        users['score'] = user.get('score')
        users['type'] = user.get('type')
        users['user_id'] = user.get('id')
        user_data.append(users)

    return user_data