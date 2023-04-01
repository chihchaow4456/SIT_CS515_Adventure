## Profile
Chih-Chao Wang cwang126@stevens.edu
## Github Repo
[My repo](https://github.com/chihchaow4456/SIT_CS515_Adventure)
## Estimate of hours
Around 16 hours were spent on this project.
## How I tested my code
I tested my code manually.
## Bugs and Issues
Test#14 cannot pass.
## An example of difficult issue how I resolved
The most challenging issue I faced was implementing the "help" verb to meet the professor's requirements. Initially, I implemented it with only static text using the "match" syntax in Python. However, after some contemplation, I utilized the property of dictionaries to implement it dynamically; that is, I implement the 'help()' methonds on each defined Class of verb. The implemetation like the interface on other Object-Oriented programming language. This way, each verb can customize its "help()" messages to display to users.
## Extensions
The following map would be presented as an interaction for three extensions.
####
    [
      {
        "name": "Taiwan",
        "desc": "You are in a beautiful island nation known for its bustling night markets, stunning mountains, and scenic beaches.",
        "items": ["bubble tea", "stinky tofu"],
        "exits": {"west": 1, "northeast": 2}
      },
      {
        "name": "China",
        "desc": "You are in the world's most populous country, famous for its rich history, diverse culture, and mouth-watering cuisine.",
        "items": ["dumplings", "hot pot"],
        "exits": {"south": 4, "west": 3}
      },
      {
        "name": "Japan",
        "desc": "You are in the Land of the Rising Sun, where ancient traditions blend seamlessly with modern technology.",
        "items": ["sushi", "ramen"],
        "exits": {"southwest": 0, "south": 3}
      },
      {
        "name": "Okinawa",
        "desc": "You are in a tropical paradise in southern Japan, famous for its pristine beaches, crystal-clear waters, and vibrant coral reefs.",
        "items": ["sata andagi", "shikuwasa juice"],
        "exits": {"west": 1,"north": 2}
      },
      {
        "name": "Thailand",
        "desc": "You are in the Land of Smiles, known for its warm hospitality, exotic temples, and spicy cuisine.",
        "items": ["pad thai","tom yum soup"],
        "exits": {"northeast": 2,"southeast": 5}
      },
      {
        "name": "Australia",
        "desc": "You are in the Land Down Under, home to stunning natural wonders, unique wildlife, and a laid-back lifestyle.",
        "items": ["vegemite","lamingtons"],
        "exits": {"north": 2,"northwest": 1}
      }
    ]
####
### Abbreviations for verbs, directions, and items
This extension allows users to input abbreviated commands that match any valid commands. For example, 'i' can be used instead of 'inventory,' or 'nor' instead of 'northeast.' In the event of multiple matches, the extension will display the possible choices for the user. Here are some examples of how this extension works:
####
    > Taiwan

    You are in a beautiful island nation known for its bustling night markets, stunning mountains, and scenic beaches.

    Items: bubble tea, stinky tofu

    Exits: west northeast 
    What would you like to do? go nor
    You go northeast.

    > Japan

    You are in the Land of the Rising Sun, where ancient traditions blend seamlessly with modern technology.

    Items: sushi, ramen

    Exits: southwest south 

    What would you like to do? go s
    Did you want to go southwest or south?
    What would you like to do? go sout
    Did you want to go southwest or south?
    What would you like to do? go south
    You go south.

    > Okinawa
    
    You are in a tropical paradise in southern Japan, famous for its pristine beaches, crystal-clear waters, and vibrant coral reefs.
    
    Items: sata andagi, shikuwasa juice
    
    Exits: west north 
    
    What would you like to do? get s
    Did you want to get the sata andagi or the shikuwasa juice?
    What would you like to do? get juice
    You pick up the shikuwasa juice.
    What would you like to do? get sa
    You pick up the sata andagi.
    What would you like to do? i
    Inventory:
      shikuwasa juice
      sata andagi
    What would you like to do?
####

### Help
The 'help' verb displays a list of valid commands for the user. Three distinct commands are available: 'go,' 'get,' and 'drop,' which respectively display available directions, items that can be obtained, and items that can be dropped. Here is an example interaction that demonstrates how "help" works:
####
    > Taiwan
    
    You are in a beautiful island nation known for its bustling night markets, stunning mountains, and scenic beaches.
    
    Items: bubble tea, stinky tofu
    
    Exits: west northeast 
    
    What would you like to do? help
    You can run the following commands:
      go west or northeast.
      get bubble tea or stinky tofu
      drop 
      look
      inventory
      quit
      help
    What would you like to do? get tea
    You pick up the bubble tea.
    What would you like to do? help
    You can run the following commands:
      go west or northeast.
      get stinky tofu
      drop bubble tea
      look
      inventory
      quit
      help
    What would you like to do?
####

### Drop
The "Drop" verb extension is similar to the "Get" verb in that they both require a room to store their items, but "Drop" is the opposite of "Get". To use the "Drop" verb, you first need to pick up an item using the "Get" verb so that you can drop it later. When you use the "Drop" verb, it removes the item from your inventory and places it in the current room. Here's the interaction of "drop".
####
    > Taiwan

    You are in a beautiful island nation known for its bustling night markets, stunning mountains, and scenic beaches.
    
    Items: bubble tea, stinky tofu
    
    Exits: west northeast 
    
    What would you like to do? drop tofu
    You don't have anything to drop.
    What would you like to do? get tea
    You pick up the bubble tea.
    What would you like to do? get tofu
    You pick up the stinky tofu.
    What would you like to do? look
    > Taiwan
    
    You are in a beautiful island nation known for its bustling night markets, stunning mountains, and scenic beaches.
    
    Exits: west northeast
    
    What would you like to do? go w
    You go west.
    
    > China
    
    You are in the world's most populous country, famous for its rich history, diverse culture, and mouth-watering cuisine.
    
    Items: dumplings, hot pot
    
    Exits: south west
    
    What would you like to do? h
    You can run the following commands:
      go south or west.
      get dumplings or hot pot
      drop bubble tea or stinky tofu
      look
      inventory
      quit
      help
    What would you like to do? dro tof
    You drop the stinky tofu.
    What would you like to do? dro tea
    You drop the bubble tea.
    What would you like to do? look
    > China
    
    You are in the world's most populous country, famous for its rich history, diverse culture, and mouth-watering cuisine.
    
    Items: dumplings, hot pot, stinky tofu, bubble tea
    
    Exits: south west 
    What would you like to do? 
####
