from django.shortcuts import redirect


class mimidel(object):

	def process_request(self, request):
		if request.user.is_auntheticated():
			if not request.user.is__superuser:
				paths = ['/']
				if request.paths in paths:
					return None
				else:
					return redirect('/')
			else :
				return None