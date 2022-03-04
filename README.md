![](https://github.com/KateKo04/Wander_game/blob/main/readme_img/wander_game.png)

# Wander game

Game created with Python.

* File **main.py** - playground
* File **game.py** - all required classes for game (Room, Character, Enemy, Friend, Item)
* File **log.txt** - example of game session

## Playground

Playground is created by creating rooms with name and description. 

Rooms are ordered by directions of world.

In rooms there are friends and enemies (so, characters) and items, which can be usefull while fighting an enemy.

## Information for player

After constructing the playground, player is given a backpach. He can put items in it.

Main loop of game goes until player dies or until two enemies of player die.

Player gets information about current room, its characters and items.

Player has such options:
  1. Go into another room
  2. Take item
  3. Start conversation
  4. Start fighting

## Basic rules

If player takes an item, it appeares in player's backpack.

If player opts direction, where another room is located, this room becomes "current".

If player starts talking, conversation is displayed on monitor.

Fight with enemy starts with entering name of item. If this item is in backpack and specifically with this item you can kill enemy, than the result - win.

Else - it's defeat.

🕸 Enjoy the game! 🧟‍♂️
