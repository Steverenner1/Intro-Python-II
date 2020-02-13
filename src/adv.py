from room import Room
from player import Player
from item import Item
# Declare all the rooms


item = [
    Item("Badass Sword of Unity", "the sword from age old kings that has been buried deep in the earth for centuries"),
    Item('Killer Mace of FU up', "your opponents don't want any of this"),
    Item("Strong Shield of Shieldiness", "this shield will protect you from even the sharpest arrows"),
    Item("Potion of Healing", "this will make you feel better")
]

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     None,
                     None,
                     None,
                     None,

                     [
                       item[0],
                       item[1] 
                     ]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",
                     None,
                     None,
                     None,
                     None,
                     [
                         item[0],
                         item[3]
                     ]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
                     None,
                     None,
                     None,
                     None,
                     [
                         item[1],
                         item[3]
                     ]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
                     None,
                     None,
                     None,
                     None,
                     [
                         item[2],
                         item[3]
                     ]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
                     None,
                     None,
                     None,
                     None,
                     [
                         item[0],
                         item[3]
                     ]),
}



# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


player = Player("Steve", room ['outside'], [item[0]])

def show_welcome_message():
    welcome_message = "Welcome to the game!"
    print(welcome_message)

def get_user_choice():
    choice = input("[n] north [s] south [e] east [w] west [q] quit\n")
    return choice_options[str(choice)]

choice_options = {
    "n": "north",
    "s": "south",
    "e": "east",
    "w": "west",
    "q": "quit",
    "get": "get item",
    "drop": "drop item",
    "i": "inventory",
    "inventory": "inventory"
}


show_welcome_message()

while True:
    current_room = player.current_room
    print(f"You are currently in {current_room.name}\n")
    print(f"{current_room.description}")
    move = input("Select N, S, E, or W >>> ")
    if move == "n":
        if current_room.n_to is not None:
            player.current_room = current_room.n_to
        else:
            print("You hit a dead end!  Try again.\n")
    elif move == "s":
        if current_room.s_to is not None:
            player.current_room = current_room.s_to
        else:
            print("You hit a dead end!  Try again.\n")
    elif move == "e":
        if current_room.e_to is not None:
            player.current_room = current_room.e_to
        else:
            print("You hit a dead end!  Try again.\n")
    elif move == "w":
        if current_room.w_to is not None:
            player.current_room = current_room.w_to
        else:
            print("You hit a dead end!  Try again.\n")

    elif "get" in move:
        item = move[4:]

        for x in range(len(current_room.items)):
            if item == current_room.items[x].item_name:
                player.inventory.append(current_room.items[x])
                print(f"you picked up {current_room.items[x]}")
                del current_room.items[x]
                break
            else:
                print("There are no items in the room")

    elif "drop" in move:
        item = move[5:]

        for x in range(len(player.inventory)):
            if item == player.inventory[x].item_name:
                current_room.items.append(player.inventory[x])
                print(f"you dropped {player.inventory[x]}")
                del player.inventory[x]
                break
            else:
                print("You don't have any items to drop")

    elif move == "i" or move == "inventory":
        for x in range(len(player.inventory)):
            print(player.inventory[x])

    # elif move == "search":
    #     current_room.item_name

    elif move == "q":
        print("Game has quit\n")
        exit()
   
