import requests
import re
import os
from time import sleep

"""
# BazosParser
__Author__ = 'Matej Jurík'

- Program looks for searched items through Bazoš.sk and outputs their title and price
- How to use (input):

        => 'auto' (searched item)
        => 'púchov' (area to search in)
        => '25' (search radius - km)
        => '2000 4000' (price: from - to)
        => 'fromcheapest' || 'frommostexpensive' || 'maxviews' (sorting - type in one of three choices)
    
- Known bugs:   

        => Regex patterns sometimes fail to recognize titles of searched items. In this case, program prints out: 
           'An RE error occurred. Try again!' 
                
        => Running the program through commandline switches the '€' sign with '?' sign
                
        => Recommended:  set the price value higher when searching for items - advertisement may get mixed up with
                         the search results 

- Yet to come:  
            
        => options += saving user-specified items to a database

- Enjoy :]
"""



# Import clrscr() from pascal :P
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')



    #Request
def request(bazos_search, parameters):
    current_page = requests.get(bazos_search, params=parameters)

    #Webpage code
    page_layout = current_page.text

    print(current_page.url)

    return page_layout

def find_elements(parameters, bazos_search='https://www.bazos.sk/search.php'):
    #Get Webpage code
    new_layout = request(bazos_search, parameters)

    #print(new_layout)



    #Regex patterns for finding prices and titles
    #(a-zA-Z0-9./ \-=(),!"_><;§´ˇ{}%&^$#@~°`ŇÁÉÍÓÚČĽŠŤŽÝĹĎŔáéíóúô+ľščŕťžýäňďĺ€\\|*]+) < (.+)
    title_pattern = re.compile(r'<span class=nadpis><a href="[a-zA-Z0-9 \-=.:/&?]+">(.+)</a></span>', re.UNICODE)
    price_pattern = re.compile(r'<span class=cena><b>([0-9 ]+€)</b></span>', re.UNICODE)

    title_matches = title_pattern.findall(new_layout)
    price_matches = price_pattern.findall(new_layout)

    #print (len(title_matches))
    #print (len(price_matches))

    print(end='\n\n')
    print('Check: ')
    print('  ',len(title_matches),' matches')
    print('  ',len(price_matches),' prices')
    print()

    try:
        # regex check
        if (len(title_matches) % len(price_matches) == 0):
            for item in range(len(title_matches)):
                print(title_matches[item], '   : ', price_matches[item], end='\n \n')

        else:
            cls()
            print('An RE error occured. Try again!')
            start_cycle()

    except:
        print ('No items found!', end='\n\n')



# Algorithm
def search():

    # Used to set what items to show (see Bazos.sk web code: crz=20 when viewing 2nd page of searched items)
    # item_count = 0

    #Parameters to pass
    parameters = {
        'hledat' :  '',
        'rubriky' : 'www',
        'hlokalita' : '',
        'humkreis' : '25',
        'cenaod' : '' ,
        'cenado' : '' ,
        'order' : '1'
    }



    # Input: string to search for
    search_item = input('Bazos.sk: Search for >>> ')
    parameters['hledat'] = search_item

    # Input: localization (either a string=city or an int=postal code)
    search_loc = input('Bazos.sk: Search in (not needed) >>> ')
    parameters['hlokalita'] = search_loc

    # Input: search radius
    search_range = input('Bazos.sk: Max search distance >>> ')
    if search_range in ['']:
        print ('Default range selected.')
    parameters['humkreis'] = search_range

    # Input: item price from..to (format =   'x y'  )
    while True:
        try:
            search_price_from, search_price_to = input('Bazos.sk: Searched item price [from (space) to] >>> ').split(' ')
        except:
            print('Bad format!')
            continue
        else:
            break
    parameters['cenaod'] = search_price_from
    parameters['cenado'] = search_price_to

    # Input: how to organize items (options = fromcheapest | frommostexpensive | maxviews
    print('Bazos.sk: Organize searched items (default= fromcheapest)')
    layout = input(' Select Sorting: fromcheapest | frommostexpensive | maxviews >>> ')
    if layout in ['fromcheapest']:
        parameters['order'] = '1'
    elif layout in ['frommostexpensive']:
        parameters['order'] = '2'
    elif layout in ['maxviews']:
        parameters['order'] = '3'
    else:
        if layout not in ['']:
            print('Incorrect input: setting layout to default!')
        else:
            print('Default layout selected.')

    print('Please wait a moment...')
    print(end='\n\n')

    return parameters


# Getting various search pages
def console_input(parameters, page, item_count):

    # Next page, prev page, first page and search functions for our program
    print('Page: ', page)
    print('Press <Enter> to exit.')
    print('Type <"First"> to see the first page.')

    if page > 1:
        print('Type <"Prev"> to go back a page')
    print('Type <"Next"> to move up a page')

    options = input('Type <"Search"> to search for a different item >>> ')
    # functional programming: modifying and then passing the values of control variables to the main cycle
    if options in ['next','Next']:
        cls()
        # item_count changes the page number
        # when set equal to crz param. that controls the page number 2..n (see Bazos.sk url: 20=2, 40=3)
        item_count += 20
        parameters['crz'] = str(item_count)
        # some space
        print(end='\n\n\n')
        # page counter
        page += 1
        # cycle handling user input
        cycle(parameters, page, item_count)

    elif options in ['first','First']:
        if page == 1:
            print(end='\n\n')
            print('Page already is the first one!', end='\n\n')
            console_input(parameters, page, item_count)
        else:
            cls()
            # remove crz param. to see the 1st page of searched items (see Bazos.sk url)
            parameters.pop('crz')
            print(end='\n\n\n')
            cycle(parameters)

    elif options in ['prev','Prev']:
        if page > 1:
            cls()
            item_count -= 20
            parameters['crz'] = str(item_count)
            print(end='\n\n\n')
            page -= 1
            cycle(parameters,page, item_count)
        else:
            print('Cannot go back a page (page is already the first one).', end='\n\n')
            sleep(1)
            cycle(parameters)

    elif options in ['search','Search']:
        cls()
        start_cycle()
    else:
        quit()

# handles user input
def cycle(param_dict, page=1, item_count=0):
    find_elements(param_dict)
    console_input(param_dict, page, item_count)


# handles searching for a new item
def start_cycle():
    page = 1
    item_count = 0

    param_dict = search()

    find_elements(param_dict)
    console_input(param_dict, page, item_count)

# One line of code = ready to go
start_cycle()
