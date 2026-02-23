# Tasks API

## Installation

1. Clone this repo.
2. Install dependencies with `bundle install`.
3. Ensure you have Postgres running.
4. Set up a database with `rake db:create` then `rake db:migrate`.
5. Seed the database with test data with `rake db:seed`.

## Getting Started

Start a Rails Server:

```sh
rails s
```

Your API is hosted at `http://localhost:3000`. There is one resource, `Task`, with associated routes:

```
   Prefix Verb   URI Pattern               Controller#Action
    tasks GET    /tasks(.:format)          tasks#index
          POST   /tasks(.:format)          tasks#create
 new_task GET    /tasks/new(.:format)      tasks#new
edit_task GET    /tasks/:id/edit(.:format) tasks#edit
     task GET    /tasks/:id(.:format)      tasks#show
          PATCH  /tasks/:id(.:format)      tasks#update
          PUT    /tasks/:id(.:format)      tasks#update
          DELETE /tasks/:id(.:format)      tasks#destroy
```

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=javascript_fundamentals/chasing_signals_around_your_code/api/README.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=javascript_fundamentals/chasing_signals_around_your_code/api/README.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=javascript_fundamentals/chasing_signals_around_your_code/api/README.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=javascript_fundamentals/chasing_signals_around_your_code/api/README.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=javascript_fundamentals/chasing_signals_around_your_code/api/README.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
