from django.db import models

class AlumniContact(models.Model):

    name = models.CharField(max_length=200, blank=False, null=False, primary_key=True)
    graduation_year = models.PositiveSmallIntegerField(default=2020)

    CHEMICAL = "Chemical Engineering"
    CIVIL = "Civil Engineering"
    COMP = "Computer Science and Engineering"
    EEE = "Electrical and Electronics Engineering"
    ECE = "Electronics and Communication Engineering"
    INFO_TECH = "Information Technology"
    MECH = "Mechanical Engineering"
    META = "Metallurgical and Materials Engineering"
    MINING = "Mining Engineering"
    UNKNOWN = "Unknown"
    BRANCH_CHOICES = [
        (CHEMICAL, CHEMICAL),
        (CIVIL, CIVIL),
        (COMP, COMP),
        (EEE, EEE),
        (ECE, ECE),
        (INFO_TECH, INFO_TECH),
        (MECH, MECH),
        (META, META),
        (MINING, MINING),
        (UNKNOWN, UNKNOWN),
    ]
    branch = models.CharField(max_length=50, choices=BRANCH_CHOICES)

    email = models.EmailField(default="", blank=True)
    phone_number = models.CharField(max_length=20, default="", blank=True)
    current_country = models.CharField(max_length=50, default="", blank=True)

    company = models.CharField(max_length=50, default="", blank=True)

    university_for_higher_studies = models.CharField(max_length=100, default="", blank=True)
    specialisation_for_higher_studies = models.CharField(max_length=100, default="", blank=True)

    last_updated = models.DateField(auto_now=True)

class AlumniContactInterest(models.Model):

    name = models.ForeignKey("AlumniContact", on_delete=models.CASCADE)
    interest = models.CharField(max_length=100, blank=False, null=False)