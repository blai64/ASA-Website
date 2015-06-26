from django.shortcuts import render, render_to_response
from django.template import Context
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader



# for the blog
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse



from website.forms import JoinForm
from website.models import Boardmember, BlogPost

# Create your views here.

def home(request):
    if request.method == "GET":
        return render(request, "website/index.html")

def about(request):
    if request.method == "GET":
        return render(request, "website/second.html")

def events(request):
    if request.method == "GET":
        return render(request, "website/events.html")

def gallery(request):
    if request.method == "GET":
        return render(request, "website/gallery.html")

# def board(request):
#   member_list = Boardmember.objects
#   cont = Context({'member_list' : member_list})
#   if request.method == "GET":
#       return render(request, template_name = "website/board.html", context=cont)

def board(request):
    member_list = Boardmember.objects.all()
    template = loader.get_template('website/board.html')
    context = RequestContext(request, {
        'member_list': member_list,
        })
    return HttpResponse(template.render(context))

def join(request):
    if request.method == 'POST':
        form = JoinForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = JoinForm()

    return render (request, 'website/join.html' , {'form' : form})

def thanks(request):
    if request.method == "GET":
        return render(request, "website/thanks.html")

def blog(request):
    posts = BlogPost.objects.all().order_by("-created")
    template = loader.get_template('website/list.html')
    context = RequestContext(request, {
        'posts' : posts
        })
    return HttpResponse(template.render(context))




    # paginator = Paginator(posts,2)

    # page = request.GET.get('page')
    # try:
    #     posts = paginator.page(page)
    # except PageNotAnInteger: 
    #     posts - paginator.page(1)
    # except EmptyPage:
    #     posts = paginator.page(paginator.num_pages)

    # return render_to_response("website/gallery.html", {"posts" : posts})  