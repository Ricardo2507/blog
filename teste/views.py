from django.shortcuts import render

def post_list(request):
    return render(request, 'teste/post_list.html', {})
