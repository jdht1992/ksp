from django.utils.translation import gettext_lazy as _

from django.db import models


class Person(models.Model):
    identifier = models.CharField(max_length=50)
    full_name = models.CharField(max_length=50)

    class Meta:
        abstract = True


class Employee(Person):
    class Status(models.TextChoices):
        ENABLE = 'enable', _('Enable')
        DISABLED = 'disabled', _('Disabled')

    image = models.ImageField(upload_to='employee')
    job = models.CharField(max_length=50)
    salary = models.FloatField()
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.ENABLE,
    )
    date_hire = models.DateField()

    def __str__(self):
        return self.identifier


class Beneficiary(Person):

    class Relationship(models.TextChoices):
        FATHER = 'father', _('Father')
        BROTHER = 'brother', _('Brother')
        GRANDSON = 'grandson', _('Grandson')
        GRANDFATHER = 'grandfather', _('Grandfather')

    relationship = models.CharField(
        max_length=12,
        choices=Relationship.choices,
        default=Relationship.FATHER,
    )
    birthday = models.DateField()

    class Gender(models.TextChoices):
        MAN = 'man', _('Man')
        WOMEN = 'women', _('Women')

    gender = models.CharField(
        max_length=10,
        choices=Gender.choices,
        default=Gender.MAN,
    )
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name
