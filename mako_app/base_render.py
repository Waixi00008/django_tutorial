from django.template import RequestContext
from django.conf import settings
from django.template.context import Context
from django.http import HttpResponse
from mako.lookup import TemplateLookup
import os
def render_to_response(request,template,data=None):
    context_instance = RequestContext(request)
    # path = settings.TEMPLATES[0]['DIRS'][0] 只有主应用才能取到这个值 C:\Users\xiaobing\Desktop\Django_Projects\django_tutorial\templates
    # 不是C:\Users\xiaobing\Desktop\Django_Projects\django_tutorial\mako_app\templates
    path = os.path.join(os.path.dirname(__file__), 'templates/')
    lookup = TemplateLookup(
        directories=[path],
        output_encoding='utf-8',
        input_encoding='utf-8'
    )
    make_template = lookup.get_template(template)

    if not data:
        content = {}
    if context_instance:
        context_instance.update(data)
    else:
        context_instance=Context(data)

    data = {}
    for d in context_instance:
        data.update(d)

    data['csrf_token']='<input type="hidden" name="csrfmiddlewaretoken" value="{0}" />'.format(request.META['CSRF_COOKIE'])

    return HttpResponse(make_template.render(**data))