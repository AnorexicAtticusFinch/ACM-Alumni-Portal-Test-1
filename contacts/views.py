from django.shortcuts import render

from django.template.loader import render_to_string
from django.http import JsonResponse

from .models import AlumniContact, AlumniContactInterest

class MakeContactObj:

    def __init__(self, contactObj_raw, interestObjs_raw):
        self.name = contactObj_raw.name
        self.profile_picture = contactObj_raw.profile_picture
        self.gradyear = contactObj_raw.graduation_year
        self.branch = contactObj_raw.branch
        self.email = contactObj_raw.email
        self.phnum = contactObj_raw.phone_number
        self.curcount = contactObj_raw.current_country
        self.comp = contactObj_raw.company
        self.uni = contactObj_raw.university_for_higher_studies
        self.spec = contactObj_raw.specialisation_for_higher_studies
        self.moddate = contactObj_raw.last_updated
        self.interests = [obj.interest for obj in interestObjs_raw]

    def __lt__(self, operand):
        return False

def searchForQuery(query, contactObj):
    query = query.lower()
    count = 0

    count += contactObj.name.lower().count(query)
    count += str(contactObj.gradyear).lower().count(query)
    count += contactObj.branch.lower().count(query)
    count += contactObj.email.lower().count(query)
    count += contactObj.phnum.lower().count(query)
    count += contactObj.curcount.lower().count(query)
    count += contactObj.comp.lower().count(query)
    count += contactObj.uni.lower().count(query)
    count += contactObj.spec.lower().count(query)
    for interest in contactObj.interests:
        count += interest.lower().count(query)
        
    return count

# Create your views here.
def testpage_view(request):

    search_queries = request.GET.get("search", "")
    print(search_queries)

    contactObjs_raw = AlumniContact.objects.all()
    contactObjs = []
    for contactObj_raw in contactObjs_raw:
        interestObjs_raw = AlumniContactInterest.objects.filter(name=contactObj_raw.name)
        contactObjs.append(MakeContactObj(contactObj_raw, interestObjs_raw))

    if search_queries != "":
        search_queries = search_queries.split(" ")
        isRelevant = [0 for counter in range(len(contactObjs))]
        for query in search_queries:
            for counter in range(len(contactObjs)):
                isRelevant[counter] += searchForQuery(query, contactObjs[counter])
    else:
        isRelevant = [1 for count in range(len(contactObjs))]

    contactObjs_to_be_sorted = []
    for counter in range(len(contactObjs)):
        if isRelevant[counter] != 0:
            contactObjs_to_be_sorted.append((isRelevant[counter], contactObjs[counter]))
    contactObjs_to_be_sorted.sort(reverse=True)
    foundContactObjs = [obj[1] for obj in contactObjs_to_be_sorted]

    para = {
        "contacts": foundContactObjs,
    }

    if request.is_ajax():
        html = render_to_string(template_name="contacts/search_results.html", context=para)
        data_dict = {"html_from_view": html}
        return JsonResponse(data=data_dict, safe=False)

    return render(request, "contacts/testpage.html", para)