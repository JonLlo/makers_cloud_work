# Classes Practical

Next week, when you start to learn about how to write your own RSpec tests, as part of the TDD process, you'll be using Ruby classes. These exercises will help prepare you for that.

Work through them in order, using this approach:
- Read the requirements
- Run the tests
- Focus on one test
- Make that test pass by building your program in small increments
- Re-run the tests frequently and pay close attention to the test output

## A short recap of classes

### What is a class?

A class is used to encapsulate state (such as a bank `balance`) and behaviour (such as the ability to `deposit` money and increase the value of `balance`).

### How do you define a class?

In ruby, classes are defined using the `class` keyword

```ruby
class Person
end
```

There's an empty `Person` class.  Let's give it some "state".

```ruby
class Person
  def initialize(name)
    @name
  end
end
```

So that we can set state (the person's `name`) when creating a new instance of `Person`, we've used the `initialize` method, which gets executed automatically and receives any arguments given to `new`.

Try this in IRB to see for yourself

```ruby
class Person
  def initialize(name)
    puts "creating an instance of Person class with name: #{name}"
    @name
  end
end

tom = Person.new("Tom")
rabhia = Person.new("Rabhia")
```

If we want to reveal the person's name to the outside world, we need a method that returns `@name`.

```ruby
class Person
  def initialize(name)
    @name
  end

  def name
    @name
  end
end

# now we can do this
migel = Person.new("Migel")
puts migel.name
```

You should play with the above examples, and create 5 of your own classes, in IRB before starting the exercises.

## How to get started

You'll need to first clone the whole Skills Workshops repo onto your machine. Once you've done that, `cd` into `skills-workshops/programming_fundamentals/classes_practical/exercise_1` to work on the first exercise then run `rspec`. If you see some failing tests like the ones below, you're ready to go.

```ruby
rspec ./spec/cohort_spec.rb:8 # Cohort#name returns the name of the cohort
rspec ./spec/cohort_spec.rb:14 # Cohort#add adds an apprentice to the cohort
rspec ./spec/cohort_spec.rb:22 # Cohort#remove remove an apprentice from the cohort
```

## Exercise 1

In this exercise, you will build a `Cohort` class that stores apprentices as strings.

### Requirements

- `Cohort#name` should return the name of the cohort
- `Cohort#apprentices` should return a list of all apprentices
- `Cohort#add` adds a new apprentice to the cohort
- `Cohort#remove` removes an apprentice from the cohort

## Exercise 2

In this exercise you'll build an `Apprentice` class

- `Apprentice#first_name` should return the apprentice's first name. For example: `Joan`
- `Apprentice#last_name` should return the apprentice's last name. For example: `Baez`
- `Apprentice#full_name` should return `first_name` and `last_name` concatenated, with a space in the middle. For example: 'Joan Baez'
- `Apprentice#program` should return either "Dev Ops" or "Software Development", depending on what apprenticeship program the apprentice is on
- `Apprentice#employer` should return the apprentice's employer
- `Apprentice#summary` should return `full_name`, `employer` and `program` concatenated. For example: `Joan Baez, Dev Ops Apprentice - AudioTech Ltd`

## Exercise 3

In this exercise you'll make `Cohort` work together with `Apprentice`

### Requirements

- `Cohort#add` should now take an instance of the `Apprentice` class and add it to the cohort
- `Cohort#remove` should now remove an instance of the `Apprentice` class from the cohort
- `Cohort#apprentices` should now return an array of `Apprentice` instances
- `Cohort#dev_ops_apprentices` (a new method) should return all the dev ops apprentices
- `Cohort#software_developer_apprentices` (a new method) should return all the software developer apprentices

## Exercise 4

In this exercise, you'll build a `Challenge` class.

### Requirements

- `Challenge#name` should return the name of the module
- `Challenge#state` should return whether or not the challenge has been completed
- `Challenge#complete!` should change `Challenge#state` to `complete`

## Exercise 5

In this exercise, you'll make `Cohort`, `Apprentice` and `Challenge` all work together

### Requirements

#### Apprentice
- `Apprentice#challenges` should return the list of challenges that have been assigned to the apprentice
- `Apprentice#assign` should take an instance of challenge as an argument and add it to `challenges`
– `Apprentice#complete_challenge` should take the name of a challenge as an argument then mark the corresponding challenge as `complete` using `Challenge#complete!`.

#### Cohort
- `Cohort#assign` takes a challenge name as an argument and assigns a new challenge to each apprentice in the cohort.

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=programming_fundamentals/classes_practical/README.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=programming_fundamentals/classes_practical/README.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=programming_fundamentals/classes_practical/README.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=programming_fundamentals/classes_practical/README.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=programming_fundamentals/classes_practical/README.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
