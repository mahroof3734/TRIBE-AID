from django.db import models


# Create your models here.

class Login(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    type = models.CharField(max_length=100)


class District_officer(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    photo = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    dob = models.DateField()
    place = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pin = models.CharField(max_length=100)
    workingdistrict = models.CharField(max_length=100)
    LOGIN = models.ForeignKey(Login, on_delete=models.CASCADE)


class Package(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)


class Allocate_package(models.Model):
    district = models.CharField(max_length=100)
    date = models.DateField()
    alloted_amount = models.CharField(max_length=100)
    PACKAGE = models.ForeignKey(Package, on_delete=models.CASCADE)


class Councilors(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    photo = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    dob = models.DateField()
    place = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    LOGIN = models.ForeignKey(Login, on_delete=models.CASCADE)


class Coordinater(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    photo = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    dob = models.DateField()
    place = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    LOGIN = models.ForeignKey(Login, on_delete=models.CASCADE)


class Tribes(models.Model):
    name = models.CharField(max_length=100)
    culture = models.CharField(max_length=100)
    population_size = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    traditional_occupation_on_jobs = models.CharField(max_length=100)
    caste_and_religion = models.CharField(max_length=100)


class Tribal_member(models.Model):
    member_name = models.CharField(max_length=100)
    dob = models.DateField()
    relation = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    TRIBE = models.ForeignKey(Tribes, on_delete=models.CASCADE)


class Tribal_related_problem(models.Model):
    title = models.CharField(max_length=100)
    problem = models.CharField(max_length=100)
    photo = models.CharField(max_length=100)
    date = models.DateField()
    status = models.CharField(max_length=100)
    TRIBE = models.ForeignKey(Tribes, on_delete=models.CASCADE)


class Food_and_medical_supply(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    unit = models.CharField(max_length=100)
    TRIBE = models.ForeignKey(Tribes, on_delete=models.CASCADE)
    COORDINATER = models.ForeignKey(Coordinater, on_delete=models.CASCADE)


class Action(models.Model):
    action = models.CharField(max_length=100)
    date = models.DateField()
    TRIBE_RELATED_PROBLEM = models.ForeignKey(Tribal_related_problem, on_delete=models.CASCADE)


class Request_entry_service(models.Model):
    service_name = models.CharField(max_length=100)
    date = models.DateField()
    status = models.CharField(max_length=100)
    TRIBE = models.ForeignKey(Tribes, on_delete=models.CASCADE)
    COORDINATER = models.ForeignKey(Coordinater, on_delete=models.CASCADE)


class Notification(models.Model):
    description = models.CharField(max_length=100)
    date = models.DateField()
    COORDINATER = models.ForeignKey(Coordinater, on_delete=models.CASCADE)
