print("Zahra Memar")
final_index = 0
initial_index = 1


def AskForNumberCities():
    number_cities=input("Please type the number of cities that you want to see?")
    if number_cities == "Quit":
        return "Quit"
    try:
        n = int(number_cities)
    except ValueError:
        print("Error!", number_cities, " is not a valid integer")
        return "ERROR"
    else:
        print("You want to see", number_cities ," cities")
    return n

def AskForCityName(number_cities):
        city_namelist=[]
        i = 0
        n = number_cities
        while i<n: 
            names_for_city= str(input('''Please input the name of city/cities that you want to see'''))
            if names_for_city in city_namelist:
                print("Error! please make sure to input different city's name")
            else:
                city_namelist.append(names_for_city)
                i = i+1
        return city_namelist

def PrintFirstCitySentence(names_for_cities):
    n = len(names_for_cities)
    sentence = " You would like to visit "
    for i in range(0,n):
        sentence = sentence + ' ' + names_for_cities[i] + " as city " + str(i+1)
        if i<(n - 1) :
            sentence = sentence +" and "
    sentence = sentence +  " on your trip"
    print(sentence)
    return sentence

def PrintAddOneCityNameSentence(sentence):
    list1 = sentence.split()
    n = len(list1)
    for i in range (0,n):
        if list1[i].isdigit():
            list1[i]=int(list1[i])+1
    new_sentence = ' '.join(map(str,list1))
    print(new_sentence)

def Run():
    while True:
        number_cities=AskForNumberCities()
        if number_cities== 'Quit':
            break
        elif number_cities == 'ERROR':
            continue
        else:
            names_for_cities = AskForCityName(number_cities)
            sentence = PrintFirstCitySentence(names_for_cities)
            PrintAddOneCityNameSentence(sentence)

    return 
Run()
            
                    








