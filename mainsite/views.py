
from django.shortcuts import render
from .models import Post
from django.http import HttpResponse


#Create your views here.
def homepage(request):
	posts = Post.objects.all()
	post_lists = list()
	for count,post in enumerate(posts):
		post_lists.append("NO.{}:".format(str(count))+str(post.title)+"<br>")
		post_lists.append("<small>"+str(post.body)+"</small><br><br>")
	return HttpResponse(post_lists)


#
# from django.template.loader import get_template
# from gjango.http import  HttpResponse
# from datetime import datetime
# from .models import Post
#
# #create your views here.
# def homepage(request):
# 	template = get_template('index.html')
# 	posts = Post.objects.all()
# 	now = datetime\
# 	ht	.render(locals())