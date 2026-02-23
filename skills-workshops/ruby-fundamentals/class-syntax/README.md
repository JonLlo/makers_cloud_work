# Classes: state and behaviour

## Learning objectives

- Understand classes and objects
- Create a class with state and behaviour in Ruby

## Introduction

Imagine we had these user stories for a bank account:

- As a customer I would like to deposit money in my account
- As a customer I would like to withdraw money from my bank account
- As a customer I would like to view my balance

Here's a way we could represent a bank account. With an integer for the balance
and methods to deposit and withdraw money.

```ruby
$balance = 0

def deposit(money)
  $balance += money
end

def withdraw(money)
  $balance -= money
end
```

But what if we wanted to keep track of multiple bank accounts?

```ruby
$alices_balance = 0

def alice_deposit(money)
  $alices_balance += money
end

def alice_withdraw(money)
  $alices_balance -= money
end

$bobs_balance = 0

def bobs_deposit(money)
  $bobs_balance += money
end

def bobs_withdraw(money)
  $bobs_balance -= money
end
```

Repeating this for each customer will quickly become unmanageable. Let's look at
how classes could help us have multiple bank accounts without copying our code.

### What is a class?

A class defines a type of object. The simplest class we can have in Ruby just has
a name:

```ruby
class BankAccount
end
```

And now we can use this class:

```ruby
bank_account1 = BankAccount.new
bank_account2 = BankAccount.new
bank_account3 = BankAccount.new
```

Classes are like a cookie cutter. Each bank account comes from the same cutter.
These are called instances of the class, and they know their class:

```ruby
bank_account1.class  #=> BankAccount
```

But so far our bank accounts don't do very much. **Instances of a class are objects.**
What makes an object? State + behaviour.

Let's see how we can give instances of a class state and behaviour.

### State

We could give every bank account an opening balance:

```ruby
class BankAccount
  def initialize(opening_balance)
    @balance = opening_balance
  end
end
```

Now each bank account object can have a different opening balance:

```ruby
alices_account = BankAccount.new(101)
bobs_account = BankAccount.new(42)
```

### Behaviour

We can give our bank account behaviour by adding `deposit` and `withdraw` methods.

```ruby
class BankAccount
  def initialize(opening_balance)
    @balance = opening_balance
  end

  def deposit(money)
    @balance += money
  end

  def withdraw(money)
    @balance -= money
  end
end
```

Notice that the instance variable `@balance` is available in every method.

## Exercise One

For each of the exercises the aim is to write some code so that the tests pass.

You can run the tests by:

```shell
> bundle install
> cd exercise1
> rspec
```

The first exercise has tests that describe a thermostat:

- As an office worker I want to know what the thermostat is currently set to
- As an office worker who is too cold I want to increase the target temperature
- As an office worker who is too hot I want to reduce the target temperature

## Exercise Two

- As a garage owner I want to add a car to the garage
- As a garage owner I want to find a car by its registration plate
- As a garage owner I want to remove a car from the garage
- As a garage owner I want to see all the cars of a particular make

It should:

- Have one class:
  - `Garage`
    - Has one instance variable:
      `cars`. This is a list of cars. Each car has a `registration_plate` and `make`.
    - Has 5 methods:
      - `initialize` This is provided for you.
      - `add`. Takes a hash representing a car as a parameter and appends it to the list of cars.
      - `find`. Takes a number plate as a parameter and returns a car with a matching registration plate.
      - `remove`. Takes a number plate as a parameter and deletes the car from the list of cars.
      - `all_of_make`. Takes a make as a parameter and returns a list of all the cars of that make.

`cd` into the `exercise2` folder and run `irb`. Load your Garage class with:

```ruby
require 'garage'
```

You can now interact with your code directly:

- Create some instances of your garage class with `garage_1 = Garage.new` etc.
- Add some cars to the garages.
- Try out all of your methods!

## Bonus - Stretch Material

All objects have a built in method `.methods` , which can be used to see the available methods on that object.

- Use this in irb to inspect an instance of your `Garage` class. There should be a lot of methods listed that you didn't write!
- Pick one or two of these built-in methods and look up what they do. Try them out in irb. Don't worry if you don't understand all of them, some of them can get quite complex. `:nil?` and `:instance_of?` are good ones to start with.

In Ruby, _everything_ is an object, even numbers and strings!

- Use `.class` on a string or number. Does it make a difference if the number is a whole number?
- Use `.methods` on a string or number to see the methods available to it.
- Some of these methods are defined with punctuation, e.g. `:+`. How do you think these are used? Could you write a class that uses methods like this?

Write out definitions for the following terms, and check them with a coach:

- Object
- Class
- Instance
- State
- Method

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=ruby-fundamentals/class-syntax/README.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=ruby-fundamentals/class-syntax/README.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=ruby-fundamentals/class-syntax/README.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=ruby-fundamentals/class-syntax/README.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=ruby-fundamentals/class-syntax/README.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
