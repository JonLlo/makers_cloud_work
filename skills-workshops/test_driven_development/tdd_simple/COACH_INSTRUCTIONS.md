# Test-driving a simple Ruby program

## Objectives
By the end of this workshop, learners should be able to:
 * Understand the TDD process and its value.
 * Apply the TDD process on a simple Ruby program, using RSpec.

## Intro (15min)

* Ask learners to describe the `PhoneChecker` class and what its doing. Write the list of the different outcomes of the method depending on the value passed to it.
* Ask learners how can we quickly test this class in IRB? If I want to test that `003` is not a valid number, for example. Make a table with two columns: one for the function call, one for the expected result, with about 3 test cases.
* Notice we do those tests manually, it takes time and we don't want to do this every time we update the code. So we need an automated way to run this. 
* Explain, at a high level, how RSpec does this, and demonstrate writing a first test case in `phone_checker_spec.rb`. Point them to RSpec's basic syntax (`it` and `expect(__).to(eq(__))` should be enough for them to get started — no other syntax bits should be needed).

## Exercise 1 (15min)

* Send the learners (15min) to pair and write the remaining test cases. Stress they *should not* modify the contents of `phone_checker.rb`.

## Plenary (15min)

* Ask how it went, what was hard, and if they have any questions.
* Suggest we try our class with an invalid number, such as `eytue656`, and show we forgot to handle for those edge cases.
* Say we'll now try a different approach, by writing the RSpec tests *before* writing the class itself.
* List the different test cases you'll need, in a table similar to the first exercise's one. This one will contain more test cases.
* Demonstrate setting up RSpec in the `exercise_2` directory and writing a first test case using a similar syntax as before. However this time the test is going to fail, since the code is not written yet.
* Demonstrate writing the minimal version for `PhoneChecker` that verifies only this first test.

## Exercise 2 (30min)

* Send the learners (30min) to write the remaining test cases and code, reminding them they should only work on one at a time.

## Plenary

* Ask to learners which approach they think was better? Which one did allow us to cover more edge cases? Also, is it easier to change requirements in English, or to change some code that is already written?
* Explain that the process they followed in the second exercise is TDD — explains the different steps are red, green, refactor (maybe show diagram).
* Explain the benefits of this process if this wasn't already clear to the learners.
* Answer any question.

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=test_driven_development/tdd_simple/COACH_INSTRUCTIONS.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=test_driven_development/tdd_simple/COACH_INSTRUCTIONS.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=test_driven_development/tdd_simple/COACH_INSTRUCTIONS.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=test_driven_development/tdd_simple/COACH_INSTRUCTIONS.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=test_driven_development/tdd_simple/COACH_INSTRUCTIONS.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
