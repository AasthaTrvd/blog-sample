from django.apps import AppConfig
from . import signals

class PostsConfig(AppConfig):
    name = 'posts'

    # import signals
    def ready(self):
	    import posts.signals
