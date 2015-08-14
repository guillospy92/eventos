
def get_avatar(backend, strategy, details, response, user=None , *args, **kwargs):
	url = None
	if backend.name == 'facebook':
		url = "https://graph.facebook.com/%s/picture?type=large" % response['id']

	if url:
		user.avatar = url
		user.save()

	





def user_details(strategy, details, response, is_new=False,  user=None, *args, **kwargs):
	"""Update user details using data from provider."""
	if user and is_new:
		changed = False
		protected = strategy.setting('PROTECTED_USER_FIELDS', [])
		keep = ('username', 'id', 'pk') + tuple(protected)
		for name, value in details.items():
			if name not in keep and hasattr(user, name):
				if value and value != getattr(user, name, None):
					try:
						setattr(user, name, value)
						changed = True

					except AttributeError:
						pass

		if changed:
			strategy.storage.user.changed(user)
					
		
			
				
					
				
					
	
	

	

	
		

	
	