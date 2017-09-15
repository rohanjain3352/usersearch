from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers
from . import models
from . import utils
import requests


class Search(APIView):
    """
    To search Users from github. If searching for first time store them in database else pick the data
    """
    def get(self, request):
        """
        :param request: username to be searched
        :return: json data
        """
        data = {}
        length = len(request.GET['user_name'])
        str = ""
        flag = False
        for i in range(1,length-1):
            str = str + request.GET['user_name'][i]
            try:
                data = models.SearchKeys.objects.get(search_key=str)
                flag = True
            except:
                pass
        if not flag:
            search_key_data={}
            search_key_data['search_key'] = str
            serializer = serializers.SearchKeySerializer(data=search_key_data)
            if serializer.is_valid():
                serializer.save()
            datas = {}
            datas['q'] = request.GET['user_name']
            res = requests.get('https://api.github.com/search/users?', datas)
            res = res.json()
            user_data = res.get('items')
            for user in user_data:
                users = {}
                users['login'] = user.get('login')
                users['url'] = user.get('url')
                users['avatar_url'] = user.get('avatar_url')
                users['score'] = user.get('score')
                users['type'] = user.get('type')
                users['user_id'] = user.get('id')
                serializer = serializers.UserSerializer(data=users)
                if serializer.is_valid():
                    serializer.save()
            res = utils.get_data(res.get('items'))
        else:
            user_result = models.User.objects.filter(login__icontains=str)
            res = serializers.UserSerializer(user_result, many=True)
            if res.is_valid:
                res = res.data

        return Response(res,status=status.HTTP_200_OK)
