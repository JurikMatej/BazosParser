# BazosParser
__Author__ = 'Matej Jurík'

- Program looks for and outputs searched items through Bazoš.sk
- How to use (input):
    auto (searched item)
    púchov (area to search in)
    25 (search radius - km)
    2000 4000 (price: from - to)
    fromcheapest || frommostexpensive || maxviews (sorting - type in one of three choices)
    
- Known bugs:   = regex patterns sometimes fail to recognize titles of searched items and prints 'An RE error occurred. 
                  Try again!' 
                
                = running the program through commandline switches the '€' sign with '?'
                
                = recommended:  set the price value higher when searching for items - advertisement may mix up with
                                the search results 

- Yet to come:  = +options >>> saving selected items to a database

- Enjoy :]
