from django.shortcuts import render, redirect, get_object_or_404
from .models import Event, Category
from users.models import User
from .forms import EventForm
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, DeleteView
from django.core.urlresolvers import reverse, reverse_lazy
from braces.views import LoginRequiredMixin
from django.http import JsonResponse, HttpResponse



class index(TemplateView):
	template_name = 'index.html'
	def get_context_data(self, **kwargs):
		context = super(index, self).get_context_data(**kwargs)
		context['events'] = Event.objects.all().order_by('-created')[:6]
		context['categories'] = Category.objects.all()
		return context


def eventoajax(request):
	if request.is_ajax():
		evento = Event.objects.get(id = request.GET['id'])
		response = JsonResponse({'name':evento.name,'summary':evento.summary})
		return HttpResponse(response.content)


	else:
		return redirect('/')
	

class panel (LoginRequiredMixin,TemplateView):
	login_url = '/'
	template_name = 'panel.html'

	def get_context_data(self, **kwargs):
		context = super(panel,self).get_context_data(**kwargs)
		context['events'] = Event.objects.filter(orginazer = self.request.user).order_by('is_free','-created')

		return context


class crearevento(CreateView ):
	form_class = EventForm
	template_name = 'crearevento.html'
	success_url = reverse_lazy('events:panel')

	def form_valid(self, form):
		form.instance.orginazer = self.request.user
		return super(crearevento, self).form_valid(form)


class detalle(DetailView):
	template_name = 'detalle.html'
	model = Event


class editar(UpdateView):
	template_name = 'editar.html'
	model = Event
	form_class = EventForm
	success_url = reverse_lazy('events:panel')

	def form_valid(self, form):
		form.instance.orginazer = self.request.user
		return super(editar, self).form_valid(form)


class eliminar(DeleteView):
	template_name = 'eliminar.html'
	model = Event
	success_url = reverse_lazy('events:panel')
	context_objects_name = 'event'







	    
	


	























		
		
