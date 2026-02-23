# Introduction to TypeScript
TypeScript is a language very similar to JavaScript, which allows us to define *types* which are checked during a *compilation step*. This helps us to verify that our code is correct. If that sounds like gibberish, you've come to the right place.

## Learning Objectives
By the end of this exercise, you should be able to:
1. Explain what a "type" is
2. Make an argument for why you might use TypeScript over JavaScript
3. Set up a basic TypeScript project
4. Be able to convert basic JavaScript code to typescript


## What is a Type?
In it's most basic form, a type is a description of some data. Some types you will have come across already include strings, numbers and booleans. These are known as *primitive types*. In JavaScript, you don't need to specify what type a piece of data is. For example, consider the function:
```javascript
const add = (a, b) => a + b; // A simple function for adding two numbers
const four = add(3, 1); // This variable has a value of 4.
```
This function is fine, but what happens if the data that is passed into it isn't a number, like it's expecting?
```javascript
const seven = add('3', 4); // WRONG! The actual outcome of this code is '34'!
```
This code doesn't give us the answer we want, but no error is thrown here. It might be many lines down the program where this finally breaks, or even worse, it might not break, and we might enter incorrect data into our database without ever knowing!

This is a basic version of the problem which TypeScript aims to solve, but variations of this pop up all over the place in coding. Functions returning strings instead of numbers, trying to iterate through an array when the value is actually undefined etc.

If we could have some confidence about the *type* of the data we are interacting with, we could solve a lot of bugs before they ever appear!

## Enter TypeScript
In Typescript, we can add *type annotations* to our code, to specify what data type is expected:
```typescript
const add = (a: number, b: number): number => a + b;
```
There are three `number` annotations here. The first two are specifying the expected *type* of this function's arguments. The third is specifying what *type* this function returns.

So this is a function that expects two arguments, both numbers, and it returns a number as well.

Now, if we try to _compile_ and run the code below, we get an error before it even runs!
```javascript
const seven = add('3', 4); 
// Error: Argument of type 'string' is not assignable to parameter of type 'number'
```

Great! But what do we actually mean by compiling code?

## Code Compilation
When we talk about TypeScript, compilation means converting from the TypeScript code that we have written, to JavaScript code that node.js or the browser can run. This is important, because **node and the browser cannot run typescript code directly**. You can see for yourself! Try to copy and paste the declaration for the add function above into the chrome console. What error do you get?

To fix this, we need to set up a TypeScript project.

## Setting Up a TypeScript Project
Create and set up a new npm project:
```shell
$ mkdir my-project && cd my-project
$ npm init -y
```

Add typescript to our project as a dev dependency:
```shell
$ npm install typescript --save-dev
```

Create a simple `tsconfig.json` config file at the root of our project:
```
{
  "compilerOptions": {
    "strict": true,
    "outDir": "build"
  },
  "include": ["src/**/*.ts"]
}
```
This tells typescript three things, that we want to be strict in our typechecking, that we want our output files to be in a `build` folder, and that we want to include all typescript files in the `src` directory and its subdirectories.


Create a typescript file:
```shell
$ mkdir src
$ touch src/main.ts
```

Write some typescript!
```typescript
// inside src/main.ts
//             takes a string ↓        ↓ returns a number
const numberOfLetters = (str: string): number => {
  const matches = str.match(/[a-zA-Z]/g);
  if (!matches) return 0;
  return matches.length;
};

console.log(numberOfLetters("Learning Typescript!!"));
```

Run the typescript compiler (`tsc`) to compile to JavaScript:
```shell
$ npx tsc
```

*Et voilà!* Our TypeScript code has been converted into usable JavaScript:

```javascript
// build/main.js (generated)
var numberOfLetters = function (str) {
    var matches = str.match(/[a-zA-Z]/g);
    if (!matches)
        return 0;
    return matches.length;
};
console.log(numberOfLetters("Learning Typescript!!"));
```

## Basic Types
TypeScript is a *superset* of JavaScript. This means that all JavaScript is valid TypeScript. Or at least, all of the *syntax* of JavaScript is valid *syntax* in TypeScript. The compiler might still complain if you're trying to do something that doesn't pass its checks, such as adding a number to a string.

So lets cover some of the basic TypeScript syntax. As you read each one, see if you can guess what it's indicating, and what code you could add that might break it.

You can use the [TypeScript Playground](https://www.typescriptlang.org/play) to test your assumptions.

1. Simple type annotation
```typescript
  let count: number;
  let input: string;
  let isComplete: boolean;
```

2. Function annotation
```typescript
  function isEven(n: number): boolean {
    return n % 2 === 0
  }

  const isOdd = (n: number): boolean => {
    return !isEven(n)
  } 
```

3. Array annotation
```typescript
  const films: string[] = [];
```

4. Object annotation
```typescript
  const person: {name: string, age: number} = {name: 'John', age: 30}
```

This is all good so far, but that last line is starting to look a bit long, and we don't want to have to be writing `{name: string, age: number}` everywhere, especially when the object grows to contain more than two fields. If only we could write this type once, and use it over and over... 🤔 More on that in Part 2! For now, let's practice what we've learned.


## Exercise - Using TypeScript to Debug

There's a bug in this JavaScript code. I'm sure you'd be able to find it given enough time, but instead we're going to leverage the power of TypeScript to help uncover the problem.

Copy this code into [a TypeScript project](#setting-up-a-typescript-project), and add in some type annotations. At the least, you'll need to add a type to the `tickets` variable, and to each parameter of each of the three functions.

Once you're done, run the compiler with `npx tsc` like we did above. TypeScript should highlight any problems! Once you've found the bug, fix it!

```javascript
const EVENT_CAPACITY = 20;
const MAX_TICKETS_PER_PERSON = 6;

const tickets = [];

export const bookTickets = (name, numberOfTickets) => {
  if (eventIsFull(numberOfTickets)) {
    throw new Error(
      "There are not enough tickets left to buy this many tickets"
    );
  }

  if (userAlreadyHasMaxTickets(name, numberOfTickets)) {
    throw new Error("This user has already purchased tickets");
  }

  for (let i = 0; i < numberOfTickets; i++) {
    tickets.push(name);
  }
};

const eventIsFull = (numberOfTickets) => {
  return numberOfTickets > EVENT_CAPACITY - tickets.length;
};

const userAlreadyHasMaxTickets = (ticketsToBuy, name) => {
  const ticketsAlreadyPurchased = tickets.filter(
    (nameOnTicket) => nameOnTicket === name
  ).length;

  return ticketsAlreadyPurchased + ticketsToBuy > MAX_TICKETS_PER_PERSON;
};

```

[Example Solution](https://youtu.be/wFIPgsW9pRU)

## Challenge - Quiz App

I've written a little quiz application, but something is wrong!

Find out more by visiting [this repo](https://github.com/makersacademy/intro-to-typescript-exercise), and following the instructions in the README.

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=fast-intros/typescript/intro-to-typescript.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=fast-intros/typescript/intro-to-typescript.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=fast-intros/typescript/intro-to-typescript.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=fast-intros/typescript/intro-to-typescript.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=fast-intros/typescript/intro-to-typescript.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
