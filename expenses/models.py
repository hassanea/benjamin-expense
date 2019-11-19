from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Expense(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=256)
    color = models.CharField(
        max_length = 6,
        default="none",
        choices=[
            ("none", "None"),
            ("red", "Red"),
            ("blue", "Blue"),
            ("green", "Green"),
            ("yellow", "Yellow")
        ]
    )
    comment = models.TextField()
    value = models.DecimalField(max_digits=16, decimal_places=2)
    start_date = models.DateField()
    recurrences = models.IntegerField(default=0)
    end_date = models.DateField()

    def __str__(self):
        return self.title

# See https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone
class AccountPreferences(models.Model):
    # Every user must have an AccountPreferences object
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True
    )

    # The optional limit a user can set on their monthly expenses
    monthly_expense_limit = models.DecimalField(
        max_digits=16, 
        decimal_places=2, 
        blank=True, 
        null=True
    )

# create an account preferences object when a user signs up
@receiver(post_save, sender=User)
def create_user_account_preferences(sender, instance, created, **kwargs):
    if created:
        AccountPreferences.objects.create(user=instance)