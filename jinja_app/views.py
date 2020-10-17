from django.shortcuts import render


# Create your views here.
def test(request):
    data = {
        'content': 'hello django jinja2'
    }
    return render(request, 'test.html', data)
