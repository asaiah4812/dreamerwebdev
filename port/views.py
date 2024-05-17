from django.shortcuts import render, redirect

from django.contrib import messages
from .models import (
		UserProfile,
		Blog,
		Portfolio,
		Testimonial,
		Certificate,
		Media
	)

from django.views import generic


from . forms import ContactForm


class IndexView(generic.TemplateView):
	template_name = "port/index.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		
		testimonials = Testimonial.objects.filter(is_active=True)
		certificates = Certificate.objects.filter(is_active=True)
		blogs = Blog.objects.filter(is_active=True)
		portfolio = Portfolio.objects.filter(is_active=True)
		medias = Media.objects.all()
		
		context["testimonials"] = testimonials
		context["certificates"] = certificates
		context["blogs"] = blogs
		context["portfolio"] = portfolio
		context["medias"] = medias
		return context



# class ContactView(generic.FormView):
# 	template_name = "port/contact.html"
# 	form_class = ContactForm
# 	success_url = "/"
	
# 	def form_valid(self, form):
# 		form.save()
# 		messages.success(self.request, 'Thank you. We will be in touch soon.')
# 		return super().form_valid(form)
	
def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Thank you. We will be in touch soon.🙏')
			return redirect('port:contact')
		else:
			messages.warning(request, 'something went wrong')
			return redirect('port:contact')
	else:
		form = ContactForm()
		return render(request, 'port/contact.html', {'form':form})


class PortfolioView(generic.ListView):
	model = Portfolio
	template_name = "port/portfolio.html"
	paginate_by = 10

	def get_queryset(self):
		return super().get_queryset().filter(is_active=True)
	

class PortfolioDetailView(generic.DetailView):
	model = Portfolio
	template_name = "port/portfolio-detail.html"

class BlogView(generic.ListView):
	model = Blog
	template_name = "port/blog.html"
	paginate_by = 10
	
	def get_queryset(self):
		return super().get_queryset().filter(is_active=True)


class BlogDetailView(generic.DetailView):
	model = Blog
	template_name = "port/blog-detail.html"

