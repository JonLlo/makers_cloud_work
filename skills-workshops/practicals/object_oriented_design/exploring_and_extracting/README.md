# Refactoring with classes

## Programme

This programme helps users organise a league-style championship.
Right now the user can:
* create a league with a list of players names
* show the matches
* record who won a match (draws have not been implemented yet)
* once all matches have a winner, you can get the overall winner for the league. This method works in a general case, but is buggy if several players are tied for the maximum number of wins.

## Task 1

Clone skills-workshops on your machine. 

```
git clone https://github.com/makersacademy/skills-workshops.git
cd ./practicals/object_oriented_design/exploring_and_extracting/
```

Read the code and tests, run the tests (`rspec` or `rspec -fd` for more details), play with the programme in irb.
Here's an example irb usage:
```
require './lib/league_organiser.rb'
league = LeagueOrganiser.new(["Alice", "Bob", "Charlie", "Denise"])
league.show_matches
league.record_a_win(2, "Charlie")
```

* Are you able to use all the features? Read the spec file for examples of how to use the code.
* Can you understand the main structure of it? What parts are more challenging?
* Are there things you learnt from it?
* Can you spot ways of improving it?
* Can you spot some good candidates for classes that could be extracted?

## Task 2

Extract a `Match` class from the programme. The usage of the programme should not change.
* Start by modelling it - which properties and methods should that class have?
* Which methods from the `LeagueOrganiser` class will need to be rewritten?
* You'll use the existing test as a feature test (don't change it while you extract) and will create a unit test to test-drive the creation of your `Match` class.
* play with your solution in irb. Can you still use the programme in the same way?

Once you're happy with your extraction, feel free to take a look inside `possible_solution_dont_look_until_task_3` for a possible solution. Your solution does not have to be the same as there are many ways to organise code.
How do they compare? Feel free to amend your solution or base the further tasks on the solution if you'd like.

## Task 3 - *stretch*

Write a unit test for the `LeagueOrganiser` class that is isolated from the `Match` class. You'll have to use doubles.

## Task 4 - *stretch*

Create a new feature using TDD: Instead of recording a win, the user can now record a score for the match. You should change the way matches are displayed accordingly.
This is a good opportunity to introduce the possibility of draws.
* Which test files will you have to change?

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=practicals/object_oriented_design/exploring_and_extracting/README.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=practicals/object_oriented_design/exploring_and_extracting/README.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=practicals/object_oriented_design/exploring_and_extracting/README.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=practicals/object_oriented_design/exploring_and_extracting/README.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=practicals/object_oriented_design/exploring_and_extracting/README.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
