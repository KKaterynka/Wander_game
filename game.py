class Room:
    """Defines class Room"""

    def __init__(self, room_name):
        """Takes name, description
        of room, its nearest rooms."""

        self.room_name = room_name
        self.room_description = None
        self.nearest_rooms = {}
        self.character = None
        self.item = None

    def set_description(self, room_description):
        """Sets room description"""
        self.room_description = room_description

    def link_room(self, nearest_room, direction):
        """Defines linked rooms"""
        self.nearest_rooms[direction] = nearest_room

    def set_character(self, character):
        """Sets character for room"""
        self.character = character

    def set_item(self, item):
        """Sets item for room"""
        self.item = item

    def get_details(self):
        """Details about room"""

        print(self.room_name)
        print("--------------------")
        print(self.room_description)
        for nearest_room in self.nearest_rooms:
            room = self.nearest_rooms[nearest_room]
            print("The " + room.get_name() + " is " + nearest_room)

    def get_character(self):
        """Gets room character"""
        return self.character

    def get_item(self):
        """Gets room item"""
        return self.item

    def describe(self):
        """Gets room description"""
        print(self.description)

    def move(self, command):
        """Coordinates user"""
        if command in self.nearest_rooms:
            return self.nearest_rooms[command]
        while command not in self.nearest_rooms:
            print("Wrong command!")
            return self

    def get_defeated(self):
        print(self.room_name + "\n--------------------\n" + self.room_description)
        for command in self.nearest_rooms:
            room = self.nearest_rooms[command]
            print(f"The {room.get_name()} is {command}")

    def get_name(self):
        """Gets name of room"""
        return self.room_name

class Character:
    """Defines class Character"""

    enemies_defeated = 0

    def __init__(self, person_name, person_description):
        """Takes name and description of person."""

        self.person_name = person_name
        self.person_description = person_description
        self.phrase = None

    def set_conversation(self, phrase):
        """Sets phrase of person"""
        self.phrase = phrase

    def talk(self):
        """Communicates with user"""
        if self.phrase:
            print(f"[{self.person_name} says]: {self.phrase}")
        else:
            print(f"No time for talking!")

    def fight(self, enemy):
        """Defines following fight"""
        print(f"{self.person_name} doesn't want to fight with you.")
        return False

    def describe(self):
        """Describes person"""
        print(self.person_name + " is here!")
        print(self.person_description)


class Friend(Character):
    """Defines class Friend"""

    def __init__(self, person_name, person_description):
        """Inherits from class Character"""
        super().__init__( person_name, person_description)

class Enemy(Character):
    """Defines class Enemy"""


    def __init__(self, person_name, person_description, weakness=None):
        """Inherits from class Character"""
        super().__init__(person_name, person_description)
        self.weakness = weakness

    def set_weakness(self, enemy_weakness):
        """Sets weakness of enemy"""
        self.enemy_weakness = enemy_weakness

    def fight(self, item_to_fight):
        """Defines user fight with enemy"""
        if item_to_fight == self.weakness:
            print(f"You fend {self.person_name} off with the {combat_item}")
            return True
        else:
            print(f"{self.person_name} crushes you, puny adventurer!")
            return False

    def get_defeated(self):
        return Enemy.enemies_defeated


class Item:
    """Defines class Item"""

    def __init__(self, item_name, item_description=None):
        """Takes name and description of item"""
        self.item_name = item_name
        self.item_description = item_description

    def set_description(self, item_description):
        """Sets description of item"""
        self.item_description = item_description

    def get_name(self):
        """Returns name of item"""
        return self.item_name

    def set_item(self, item_name):
        """Sets name of item"""
        self.item_name = item_name

    def describe(self):
        """Description of item"""
        print(f"The [{self.item_name}] is here - {self.item_description}")
