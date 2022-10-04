from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.dispatch import receiver
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail  
# Create your models here.


class User(AbstractUser):
    friends = models.ManyToManyField("User",blank=True)
    blockList =models.ManyToManyField("User", related_name='blockUsers',blank=True)
    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
    def __str__(self):
        return self.username


class FriendRequest(models.Model):
    from_user = models.ForeignKey(User, related_name='from_user', on_delete=models.CASCADE,)
    to_user = models.ForeignKey(User, related_name='to_user', on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.to_user


class blockList(models.Model):
    from_user = models.ForeignKey(User, related_name='fromBlock', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='toBlock', on_delete=models.CASCADE)




@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)

    send_mail(
        # title:
        "Password Reset for {title}".format(title="Some website title"),
        # message:
        email_plaintext_message,
        # from:
        "abdullahakhlaq14@gmail.com",
        # to:
        [reset_password_token.user.email]
    )


