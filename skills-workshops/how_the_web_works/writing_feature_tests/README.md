# Feature testing a web application

## Learning objectives
- understand the difference between a feature test, manual test and unit
test
- write a feature test for code that exists
- write a feature test for code that doesn't yet exist

## Introduction
Feature tests can be a very useful way to make sure our web application
fulfils the user requirements, and can help guard against breaking
changes that can be introduced when making modifications to the code.

Let's consider the following user stories:

```
As a busy person, so that I can keep track of my business
I want to be able see a list of my existing to do items
```

```
As a busy person, so that I can keep track of my business
I want to be able to add an item including a name and a category to my to do list
```

```
As a busy person, so that I can keep track of my business
I want to be able to see my to do list by category
```

```
As a busy person, so that I can keep track of my business
I want to be able to be able to select a category from a drop down list
```

For each user story we can take a step by step approach to writing a feature test

- Manually test the web app
- Write down each step you took
- Translate each step into Capybara syntax
- Run the test to check we got the syntax correct

## Useful Resources
- [Capybara Cheatsheet](https://devhints.io/capybara)
- [HTML forms](https://www.w3schools.com/html/html_forms.asp)


## Exercise 1

For the above user stories, have a go at each of the steps.

To run the to do list app on your machine by:

- Fork the repo onto your Github repo
- Clone the repo onto your machine
- `cd todo-list-web`
- `ruby app.rb`

To run the tests:
- `rspec`

## Exercise 2

Looking at the following user stories:

```
As a busy person, so that I can keep track of my business
I want to add an optional deadline to my to do item
```

```
As a busy person, so that I can keep track of my business
I want to mark an item as complete
```

For each of these stories, have a go at:

- Imagining a manual test. What would it mean for this to be working?
- Write down each step your manual test would take
- Translate these steps into Capybara syntax
- Run your test and check that it is failing in the right way

## Exercise 3

For the user stories above have a go at:
- Drawing a sequence diagram of the interaction between browser,
model, view and controller
- What new methods would your Todo List object need? Can you unit test them?
- Try writing the code to make your feature tests go green.

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=how_the_web_works/writing_feature_tests/README.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=how_the_web_works/writing_feature_tests/README.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=how_the_web_works/writing_feature_tests/README.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=how_the_web_works/writing_feature_tests/README.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=how_the_web_works/writing_feature_tests/README.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
