from django.shortcuts import render,redirect
from .forms import coin_form
from django.contrib import messages
from .models import  *

# Create your views here.
def home(request):
    if request.method=='POST':
        form = coin_form(request.POST)
        if form.is_valid():

            penny = form.cleaned_data.get("penny_1")
            nickel = form.cleaned_data.get("nickel_5")
            dime = form.cleaned_data.get("dime_10")
            quarter=form.cleaned_data.get("quarter_25")
            coke=form.cleaned_data.get("Coke")
            pepsi=form.cleaned_data.get("Pepsi")
            soda=form.cleaned_data.get("Soda")
            cancel=form.cleaned_data.get("Cancel")


            total= (penny*1)+(nickel*5)+(dime*10)+(quarter*25)
            if cancel == True:
                s="Items cancelled"
                change="Collect your refund: {}". format(total)
                context = {'s': s, 'change': change}
                return render(request, 'collect.html', context)

            item_price=(coke*25)+(pepsi*32)+(soda*47)
            if total>=item_price:
                change=total-item_price
                form.save()
                s=[]
                if coke>0:
                    s.append(' {} coke'.format(coke))
                if soda>0:
                    s.append(' {} soda'.format(soda))
                if pepsi>0:
                    s.append(' {} pepsi'.format(pepsi))
                s='and'.join(s)
                s="Here's your"+s
                if change>0:
                    change='Collect your change:{} bucks'.format(change)
                else:
                    change=''
                if soda==0 and coke==0 and pepsi==0:
                    s='Please select an item'
                context={'s':s,'change':change}
                return render (request,'collect.html',context)
            else:
                messages.info(request, 'Insufficient fund!')

    else:
        form = coin_form()
    context_data = {'form': form}

    return render(request ,'home.html',context_data)
