from django.shortcuts import render

# Create your views here.
def posts_list(request):
    names = ['oleg','oly']
    return render(request, 'blog/index.html', context={'names':names})