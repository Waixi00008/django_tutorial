from django.views.generic import View
from .base_render import render_to_response


class Test(View):
    TEMPLATE = 'hi.html'

    def get(self, request):
        data = {
            'content': 'hello django mako'
        }
        return render_to_response(request, self.TEMPLATE, data=data)

