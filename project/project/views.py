from django.http import HttpResponse

def demo(request):
    return HttpResponse('i love india')
def hello(request):
    data="""<html>
    <head><title>hello</title></head>
    <body>
    <h1>welcome to my area</h1>
    <marquee>thank you so mucn </marquee>
    </html>"""
    return HttpResponse(data)

def hellodemo(request):
    return HttpResponse("""<html>
    <head><title>hello</title></head>
    </body>
    </html>""")