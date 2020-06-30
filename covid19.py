import sys
import requests
import pyfiglet


def headerPart(devName,country):
    r = requests.get('https://api.covid19api.com/summary')
    data = r.json()
    fig = pyfiglet.figlet_format('Covid  19')
    print(fig)
    text = 'By '+ devName
    print(text.center(75))
    if country != 'Global':
        text = 'Country : ' + country
    else:
        text = ": Global"
    print(text.center(75), end='\n\n')
    return data


def corona():
    found = False
    data = headerPart('Bibek', country)
    for items in data['Countries']:
        if items['Country'] == country:
            found = True
            print('Total Cases: ' + str(items['TotalConfirmed']))
            print('New Cases: ' + str(items['NewConfirmed']))
            print('Total Deaths: ' + str(items['TotalDeaths']))
            print('New Deaths: ' + str(items['NewDeaths']))
            print('New Recovered: ' + str(items['NewRecovered']))
            print('Total Recovered: ' + str(items['TotalRecovered']))
    if(not found):
        print("Sorry "+country + " is not valid input.")

notCapital = ['of']

if len(sys.argv) == 1:
    data = headerPart('Bibek','Global')
    for k,v in data['Global'].items():
        print(f'{k}: {v}')
else:
    country = ''
    for i in range(1,len(sys.argv)):
        temp = sys.argv[i]
        if temp.lower() in notCapital:
            temp = temp.lower()
        else:
            temp = temp.lower().capitalize()
        
        if i == (len(sys.argv)-1):
    	    country += temp
        else:
    	    country += temp + ' '
    corona()
