from django.shortcuts import render

from .models import AlumniContact, AlumniContactInterest

class MakeFinContactObj:

    def __init__(self, contactObj, interestObjs):
        self.name = contactObj.name
        self.gradyear = contactObj.graduation_year
        self.branch = contactObj.branch
        self.email = contactObj.email
        self.phnum = contactObj.phone_number
        self.curcount = contactObj.current_country
        self.comp = contactObj.company
        self.uni = contactObj.university_for_higher_studies
        self.spec = contactObj.specialisation_for_higher_studies
        self.moddate = contactObj.last_updated
        self.interests = [obj.interest for obj in interestObjs]

# Create your views here.
def testpage_view(request):

    contactObjs = AlumniContact.objects.all()
    finContactObjs = []
    for contactObj in contactObjs:
        interestObjs = AlumniContactInterest.objects.filter(name=contactObj.name)
        finContactObjs.append(MakeFinContactObj(contactObj, interestObjs))

    para = {
        "contacts": finContactObjs,
    }

    return render(request, "testpage.html", para)