import requests
from django.views.generic import View
from django.http import JsonResponse


class Music(View):
    DOUBAN_MUSIC_API = 'https://api.douban.com/v2/music/search?q={0}'

    def get(self, request):
        music_name = request.GET.get('musicname', '')

        if not music_name:
            return JsonResponse({'errcode': -1, 'errmsg': '音乐名称不能为空'})
        url = self.DOUBAN_MUSIC_API.format(music_name)

        try:
            response = requests.get(url)
        except Exception as e:
            return JsonResponse({
                'errcode': -1,
                'errmsg': str(e)
            })
        if response.status_code != 200:
            return JsonResponse({
                'errcode': -1,
                'errmsg': '请求豆瓣异常'
            })
        data = response.json()
        return JsonResponse({
            'errcode': 0,
            'errmsg': '成功',
            'data': data
        })
