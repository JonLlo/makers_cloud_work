# Questions

## Question 1

```javascript
console.log(1) // program starts

// click callback is set up to run when clicks happen
document.addEventListener('click', (clickEvent) => {
  console.log(3) // sometime later, a click has happened

  console.log("The click event:", clickEvent);

  console.log(4) // callback finishes running
});

console.log(2) // after callback set up, program stops work (for now)
```

## Question 2

```javascript
console.log(1) // program starts

// AJAX request sent to async-workshops-api.herokuapp.com and callback
// set up to run when response comes back
fetch("https://async-workshops-api.herokuapp.com/people")
  .then(response => response.json())
  .then(peopleResponse => {
    console.log(3) // sometime later, the response has come in

    console.log("People response:", peopleResponse);

    console.log(4) // callback finishes running
  });

console.log(2) // after callback set up, program stops work (for now)
```

## Question 3

```javascript
console.log(1) // program starts

// AJAX request sent to async-workshops-api.herokuapp.com and callback
// set up to run when response comes back
const getReturnValue = fetch("https://async-workshops-api.herokuapp.com/people")
  .then(response => response.json())
  .then(peopleResponse => {
    console.log(4) // sometime later, the response has come in

    // peopleResponse contains the people data
    console.log("peopleResponse:", peopleResponse)

    console.log(5) // about to finish running the callback

    // A variable returned from a callback won't be returned from the function
    // that the callback was passed to ($.get).  So this return line is redundant.
    // (Research this!)
    return peopleResponse;
  });

console.log(2) // after callback is set up, program continues

// getReturnValue contains the return value of the $.get() call (the JS
// object that represents the details of the AJAX request), **not** the
// people data returned by the request.
console.log("getReturnValue:", getReturnValue)

console.log(3) // after callback set up, program stops work (for now)
```

## Question 4

```javascript
console.log(1) // program starts

// AJAX request sent to async-workshops-api.herokuapp.com and callback
// set up to run when response comes back
fetch("https://async-workshops-api.herokuapp.com/people")
  .then(response => response.json())
  .then(peopleResponse => {
    console.log(3) // sometime later, response has come in

    // iterate through each person in peopleResponse
    peopleResponse.forEach(person => {
      // **Immediately**, a person is printed. There's no "sometime
      // later". The program doesn't pause between starting the
      // iteration and calling the callback for the first person.

      console.log("4 and 5 and 6 and 7") // prints once for each person

      console.log(person.name); // print person's name

      console.log(8) // about to finish running the callback
    });

    console.log(9)
  });

console.log(2) // after callback set up, program stops work (for now)
```

## Question 5

```javascript
console.log(1) // program starts

// hiThere is set up to run 0 milliseconds after we finish executing console.log(2)
setTimeout(() => {
  // callback starts executing
  console.log(3)

  console.log("Hi there!");

  console.log(4) // callback finishes running
}, 0)

console.log(2) // after setTimeout is set up
```

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=javascript_fundamentals/callbacks_following_the_flow_of_control/exemplar_dont_read_until_workshop_over/questions.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=javascript_fundamentals/callbacks_following_the_flow_of_control/exemplar_dont_read_until_workshop_over/questions.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=javascript_fundamentals/callbacks_following_the_flow_of_control/exemplar_dont_read_until_workshop_over/questions.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=javascript_fundamentals/callbacks_following_the_flow_of_control/exemplar_dont_read_until_workshop_over/questions.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=javascript_fundamentals/callbacks_following_the_flow_of_control/exemplar_dont_read_until_workshop_over/questions.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
