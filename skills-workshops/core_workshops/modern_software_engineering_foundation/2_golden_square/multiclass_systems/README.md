# Designing Multiclass Systems

In this workshop, you will...

- Create a [design recipe](https://journey.makers.tech/pages/class-design-recipe-template) to plan a multiclass system
- Compare plans

## Learning Objectives

- Create a design recipe for a multiclass system
- Compare and contrast two design recipes
- Improve your own design recipe

## Agenda

There are 4 parts to this workshop...

- The **intro**, where your coach provides context and an explanation of the tasks
- The **main**, where you work with a pair to do the tasks
- An **intermezzo**, where you compare your design with someone else's in a group of four
- The **plenary**, where you regroup to discuss designs as a cohort and reflect on the learning objectives


As per the [design recipe](https://journey.makers.tech/pages/class-design-recipe-template)

## Tasks

During the **main** part of the workshop, you and a pair will work through these tasks.

### 1. Read the User Stories

```
As a game player
I want to create a character with a cool name
So that other players recognise my character
```

```
As a game player
I want to see my characters health
So that I know when I might need to drink a health potion
```

```
As a game player
I want my character to be able to pick up items (potions/weapons) that they find in the game
So that they can use them when they need
```

```
As a game player
I want to be able to use my health potion item
So that my character's health goes back to 100
```

```
As a game player
I want to attack another character
So that they lose the health points associated with an attack by that weapon
```

### 2. Design the Class Interfaces

A class interface is the set of things that someone can use to interact with the class or instances of the class. It includes...

- Methods
- Properties

> In your design recipe, design the methods and properties that each of your classes will encapsulate

### 3. Create Examples as Tests

No need to write actual tests here. The task is to create a set of examples which describe how your classes can be used and what the outcomes should be.

For example...

```
"""Every character should have a name"""
player1 = Character("Cookie Monster")
player1.name => should return "Cookie Monster"
```

> In your design recipe, craft some examples for 1 or 2 methods. Remember to include some "edge cases".

## Intermezzo

Now, you and your pair will compare your design with someone else's.

- Exchange designs by sharing the markdown file/s you created.
- Take 5 mins to quietly read and compare designs
- Take another 5 mins to discuss the similarities and differences
- Consider what you might now change about your own design. It's OK to steal good ideas :)

> Nominate someone in your group of 4 to share a summary of your discussion

## Plenary

Your coach will facilitate a short discussion and reflection on the learning objectives.

