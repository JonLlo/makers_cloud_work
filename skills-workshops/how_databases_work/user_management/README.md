# User Management

In this workshop, you'll learn about user management by reading through an unfamiliar codebase, where user management has been implemented.

## Why user management?
Pretty much every important thing you work on will have users who will need to sign up and sign in. They also need their credentials to be safely stored in your database, so that someone can't hack their account!

## Why the unfamiliar codebase?
It's likely that, in your career, you'll change teams quite a few times. Every time, you'll probably have to get to grips with a new codebase.

> This is actually going to happen sooner than you think because, during the bootcamp, you'll be given at least one unfamiliar codebase to extend, as part of a team.

So getting some practice with the task reading unfamiliar codebases is going to help you a lot, in the short term _and_ in the long term.

## Learning outcomes

By the end of this workshop, all devs will be able to
1. Recognise the discomfort that sometimes comes from looking at new codebases
2. Follow the flow of execution within the context of a specific user story
3. Explain how sign up and sign in are implemented in the example codebase

## Set up

1. Clone [this repo](https://github.com/makersacademy/auth_workshop_codebase)
2. Follow the set up instructions in the `README` for that repo

## Exercise

First, work through these steps for sign up, then do them again for sign in...

1. Explore the user journey
2. The user journey starts with a form – find the corresponding view in the app's codebase
3. Identify the code in `app.rb` that is executed when the form is submitted
4. Dig into that code and try to get a high level understanding of what's going on
5. Diagram your understanding

### Questions
1. Why is the password encrypted before being stored in the database?
2. Why is the return value of `user.id` stored in the session after creating a new user?
3. It's possible to create bookmarks even if you're not signed in. How could you fix that?


<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=how_databases_work/user_management/README.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=how_databases_work/user_management/README.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=how_databases_work/user_management/README.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=how_databases_work/user_management/README.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=how_databases_work/user_management/README.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
