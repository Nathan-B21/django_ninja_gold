from django.shortcuts import render, redirect
import random
def index(request):
    if 'activities' not in request.session:
        request.session['activities'] = []
    if 'totalmoney' not in request.session:
        request.session['totalmoney'] = 0
    
    return render(request,'index.html')

# def populateRandom(max, length):
#     for x in range(0,length,1):
#         temp = Math.floor(Math.random() * max) +1
#         x = temp
#     return x

def process_money(request):
    if request.POST['location_form'] == 'farm':
        amountChosen = random.randint(10,20)
        request.session['totalmoney'] += amountChosen
        request.session['activities'].append(f"You went to the farm and gained {amountChosen} gold")
        return redirect("/")
    
    if request.POST['location_form'] == 'cave':
        possibleGold = [5,6,7,8,9,10]
        amountChosen = random.randrange(0,5)
        request.session['totalmoney'] += possibleGold[amountChosen]
        request.session['activities'].append(f"You explored the caves and came back with {amountChosen} gold")
        return redirect("/")
    
    if request.POST['location_form'] == 'house':
        possibleGold = [2,3,4,5]
        amountChosen = random.randrange(0,3)
        request.session['totalmoney'] += possibleGold[amountChosen]
        request.session['activities'].append(f"you ransacked a stranger's house and pockted {amountChosen} gold")
        return redirect("/")
    
    if request.POST['location_form'] == 'casino':
        # for x in range(-50, 50, 1):
        #     possibleGold = Math.floor(Math.random() * 50)
        amountChosen = random.randint(-50,50)
        
        request.session['totalmoney'] += amountChosen
        if amountChosen == 0:
            request.session['activities'].append(f"you made {amountChosen}, better than losing money I guess...")
            return redirect("/")
        elif amountChosen < 0:
            request.session['activities'].append(f"You tried your luck at the casino and lost {amountChosen} gold. Too bad!")
            return redirect("/")
        elif amountChosen == 50:
            request.session['activities'].append(f"you hit JACKPOT, gained {amountChosen}!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            return redirect("/")
        elif amountChosen > 0:
            request.session['activities'].append(f"you tried your luck at the casino and came out with {amountChosen} gold. Nice!")
            return redirect("/")
        return redirect("/")
        
def destory(request):
    del request.session['totalmoney']
    del request.session['activities']
    return redirect("/")