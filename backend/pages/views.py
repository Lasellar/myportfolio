from django.shortcuts import render


def page_404(request, exception):
    template = 'pages/404.html'
    return render(request, template, status=404)


def page_500(request):
    template = 'pages/500.html'
    return render(request, template, status=500)


def page_502(request):
    template = 'pages/502.html'
    return render(request, template, status=502)


def page_503(request):
    template = 'pages/503.html'
    return render(request, template, status=503)
