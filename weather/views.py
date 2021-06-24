from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404

# Create your views here.
def home(request):
    import json
    import requests

    if request.method == "POST":
        zipcode = request.POST['zipcode']
        #return render(request, 'home.html', {'zipcode': zipcode})
 

        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode + "&distance=5&API_KEY=B2910B43-3265-49E4-BE07-40DB21B3DDDE")
        #https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20001&distance=5&API_KEY=B2910B43-3265-49E4-BE07-40DB21B3DDDE

        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error...."


  

        if api[0]['Category']['Name'] == "Good":
            category_description = "(0-50) Air quality is considered satisfactory"
            category_color = "good"
        elif api[0]['Category']['Name'] == "Moderate":
            category_description= "(51-100) Air is acceptable"
            category_color = "moderate"
        elif api[0]['Category']['Name'] == "Unhealty for Sensitive Groups":
            category_description= "(101-150) Risk for weak lung people"
            category_color = "USG"
        elif api[0]['Category']['Name'] == "Unhealthy":
            category_description= "(151-200) Everyone will have suffer in health issue"
            category_color = "unhealthy"
        elif api[0]['Category']['Name'] == "Very Unhealthy":
            category_description= "(201-250) it will effect seriously"
            category_color = "veryunhealthy"
        elif api[0]['Category']['Name'] == "Hazardous":
            category_description= "(251-300) Health warning emergency condition"
            category_color = "hazardous"

        
        diction= {
            'api': api, 
            'category_description':category_description, 
            'category_color':category_color,}
        return render(request, 'home.html', context= diction)

    else:
        return render(request, 'home.html', )
                   


            


 




def about(request):
    diction= {}
    return render(request, 'about.html', context= diction) 



            



