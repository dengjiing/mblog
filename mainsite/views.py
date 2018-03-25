
# from django.shortcuts import render
# from .models import Post
# from django.http import HttpResponse
#
#
# #Create your views here.
# def homepage(request):
# 	posts = Post.objects.all()
# 	post_lists = list()
# 	for count,post in enumerate(posts):
# 		post_lists.append("NO.{}:".format(str(count))+str(post.title)+"<br>")
# 		post_lists.append("<small>"+str(post.body)+"</small><br><br>")
# 	return HttpResponse(post_lists)

from django.template.response   import TemplateResponse
from django.template import Template
from django.template.loader import get_template
from django.http import  HttpResponse
from django.shortcuts import redirect
from datetime import datetime
from .models import Post

#create your views here.
def homepage(request):
	template = get_template('index.html')

	posts =Post.objects.all()

	now = datetime.now()
	html = template.render(locals())
	return HttpResponse(html)

def showpost(request,slug):
	template = get_template('post.html')
	try:
		post = Post.objects.get(slug=slug)
		if post!=None:
			html = template.render(locals())
			return HttpResponse(html)
	except:
		return redirect('/') 