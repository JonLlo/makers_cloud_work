# Debugging in Python

In this workshop you will

- Welcome bugs as learning opportunities
- Observe and learn a debugging process
- Apply a debugging process
- Give feedback on your pair's process

## A familiar story...

You're doing some programming and your code doesn't quite do what it ought to but you think you know what the problem is, so you make some small changes in a few places. Now the program behaves even more strangely! A few hours pass and... you're not really sure what you've tried or whether any of it was helpful.

## The solution...

To avoid debugging hell, you need a solid debugging process. The great thing is that your debugging process will work with any language. The key is to delay making any changes until you understand the problem.

> “If I had an hour to solve a problem I'd spend 55 minutes thinking about the problem and five minutes thinking about solutions.” - Albert Einstein (allegedly)

## The process

Here's a process that will generalise to any language...

1. Tighten the loop
2. Get visibility
3. Change and verify

### 1. Tightening the loop

The first step is about trying to track down _where_ the bug is. I.e. In which line/s of code does the bug reside? To complete this step...

- Pay close attention to any error messages and test failures - some will direct your attention to specific lines in specific files
- Use `print` statements to identify which bits of code get executed and which do not

### 2. Getting visibility

In the first step you found _where_ the bug is - now you need to understand what is going on. To complete this step, use `print` statements to gain visibility over...

- Variables
- Function return values
- Function arguments
- State changes (e.g. the list of passwords in `PasswordManager` before and after a new item is added)

### 3. Change and verify

Having identified where the bug is and what is happening, you are ready to make a careful change but you need a way of knowing whether or not your change was good. If you have failing tests, your tests might now pass – but what if that change you made was just the first step in unpicking a complex problem? How will you know if you are going in the right direction? What was the desired impact of your change? Using `print` is useful here too!

## Main

You will be paired up with someone to work on exercises 1 and (if you have time) exercise 2. You will take turns as driver and observer. The driver does the debugging and the observer provides feedback.

1. Decide who is going to drive first and set a timer for 15 mins
2. The driver starts debugging whilst the observer... observes!
3. After the time is up, the observer provides feedback
4. Swap roles, restart the timer and repeat steps 2-3

### Observer rubric

When you are the observer, use this as a guide for your feedback

[ ] - The driver didn't jump into making changes
[ ] - The driver used error messages and tests failures where appropriate
[ ] - The driver used `print` statements to get visibility
[ ] - The driver verified their changes

> Note that the _process_ is more important than whether or not the bugs were all fixed

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=test_driven_development/debugging_fizzbuzz_and_more/python/README.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=test_driven_development/debugging_fizzbuzz_and_more/python/README.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=test_driven_development/debugging_fizzbuzz_and_more/python/README.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=test_driven_development/debugging_fizzbuzz_and_more/python/README.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=test_driven_development/debugging_fizzbuzz_and_more/python/README.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
