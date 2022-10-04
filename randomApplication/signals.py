from django.db.models.signals import pre_save
from django.dispatch import receiver
from randomApplication.models import User
from CRUD .models import Post
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail 
# from django.dispatch import receiver

@receiver(pre_save, sender = Post)
def at_beginning_save(sender, instance, raw,using,**kwargs):
    # email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)
    email_plaintext_message = "Your Post Has Been Created Successfully"
    print("++++++++++++=")
    send_mail(
        # title:
        "Post Created By {name}".format(name=instance.post.username),
        # message:
        email_plaintext_message,
        # from:
        "abdullahakhlaq14@gmail.com",
        # to:
        [instance.post.email]
    )