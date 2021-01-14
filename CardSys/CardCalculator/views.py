from django.shortcuts import render
from datetime import datetime
from django.contrib import messages
# Create your views here.


# Create your views here.

def home(request):
	return render(request, "age/Dob.html", )
	#else:
			#return redirect("/")

def age(request):
		if request.method=='POST' :
			mtn_5 = int(request.POST['Mtn_500']) * 550
			mtn_2 = int(request.POST['Mtn_200']) * 220
			mtn_1 = int(request.POST['Mtn_100']) * 110
			#c_y = 2020
			age = mtn_1 + mtn_2 + mtn_5
			#if age > 20:
			#	messages.info(request, f"You are an adult")
		if request.method=='POST' :
			gl_5 = int(request.POST['Glo_500']) * 500
			gl_2 = int(request.POST['Glo_200']) * 210
			gl_1 = int(request.POST['Glo_100']) * 110
			#c_y = 2020
			GLO = gl_1 + gl_2 + gl_5

		if request.method=='POST' :
			AirT_5 = int(request.POST['Glo_500']) * 500
			AirT_2 = int(request.POST['Glo_200']) * 210
			AirT_1 = int(request.POST['Glo_100']) * 110
			#c_y = 2020
			AirT = AirT_1 + AirT_2 + AirT_5
		else:
			return redirect("/")
			
				#messages.info(request, f"You are an adult")
		return render(request, 'age/result.html', {'result' : age} , {'res': GLO}, {'Airtel':AirT})
	

	    
#import datetime
#DOb = input('Enter Year:- ')
#Currentyear #=datetime.datetime.now#().year
#Age = Currentyear - int(DOb)
#print('Your Age is #{}'.format(Age))


