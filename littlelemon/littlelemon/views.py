from django.http import HttpResponse

def handler404(request,exception) :
    msg = '''
    <h1 style="color:red;">Error 404 !</h1>
    <h3 style="color:red;"> this page was not found ! check your urls again.</h3>
    '''
    return HttpResponse(msg)
