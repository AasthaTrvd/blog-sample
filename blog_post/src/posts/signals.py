from django.db.models.signals import post_save # signal triggerred when new user gets created
from django.contrib.auth.models import User #sender
from django.dispatch import receiver  # receiver performs some task after recieving signal
from .models import Profile

# Create profile for user
@receiver(post_save, User) #(signal, sender)
def create_profile(sender, instance, created, **kwargs):
	if created:						# user created?
		Profile.objects.create(user=instance)		# user=instance of user created

# save profile
@receiver(post_save, User)
def save_profile(sender, instance, **kwargs):
	instance.profile.save()


