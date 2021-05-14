from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    number = models.IntegerField()
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name + " " + self.email

    @staticmethod
    def get_Customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False

    def register(self):
        self.save()

    def isExists(self):
        if Customer.objects.filter(email=self.email):
            return True

        return False
