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

        => regex patterns sometimes fail to recognize titles of searched items. In this case, program prints out: 
           'An RE error occurred. Try again!' 
                
        => running the program through commandline switches the '€' sign with '?'
                
        => recommended:  set the price value higher when searching for items - advertisement may mix up with
                                the search results 

- Yet to come:  
            
        => options += saving selected items to a database

- Enjoy :]
