# Pairing styles

### 1. Unstructured

- Two programmers try to help each other
- They're winging it (the pairing) a bit
- But they're definitely both fully engaged with the task

### 2. Driver - navigator

The most commonly used style.  Be mindful that you don't lapse into unstructured pairing.

#### The 'traditional' model...

- The driver handles the basic mechanics of programming: typing, moving between files and basic implementation.
- The navigator is responsible for broader concerns and checks for mistakes.
- The navigator might ask or suggest
  - Are we duplicating code from elsewhere in the codebase?
  - Is now the right moment to create a new class?
  - What _should_ that new class be?
  - Should we refactor now or later?
  - Perhaps there's a known solution to this problem.

#### But...

**The research of Sal Freudenberg, observing how people actually do pair programming, finds that**

1. Not only are a very small number of utterances spoken by a programming pair about syntax and spelling (just 2%), these are distributed pretty evenly between the driver and navigator. Thus implying that, contrary to suggestions (e.g. Williams & Kessler (2003) “ The navigator…observes the work of the driver, looking for tactical…defects. Tactical defects are syntax errors, typos..”), pointing out spelling mistakes is not a significant part of the navigator’s role.

2. The navigators did not talk at a higher level of abstraction than the driver. Rather they both spoke at roughly the same levels of abstraction. Thus implying that, contrary to suggestions (e.g. Kent Beck (2000) “While (the driver) is busy typing, the other partner is thinking at a more strategic level”) the navigator’s role is not defined by them doing more strategic thinking.

**And she concludes**

I suggest some alternative possibilities: i) The fact that both navigator and driver speak most at an intermediate level of abstraction may provide some “cognitive glue” to help gel together the real world and programming domain. ii) Speaking may provide clarification by transforming our sometimes sloppy and incomplete mental models into verbalisations. iii) Speaking at an intermediate level primes the navigator to take over. Solving programming problems, typing and talking all at once is an incredible cognitive load to bear.

**A very brief summary of her findings is available [here](https://salfreudenberg.wordpress.com/2013/11/16/10-years-of-thinking-about-pair-programming/).**

### 3. Strong style

A twist on driver - navigator (similar to backseat navigator).  This can be great with expert-novice pairings.  When the novice drives, they get to experience implementing the plans of the expert and will likely find that they learn the new language / tech stack / domain very quickly.

- All code comes from the mind of the navigator, through the hands of the driver.
- The driver should be willing to implement the navigators ideas, without necessarily understanding what is going on, trusting that it will make sense eventually.
- If the driver wants to have an input on the direction, they yield control of the keyboard (push) and become the navigator.

> Contrast this to the 'normal' situation where being the driver (having the keyboard) constitutes being in control.

### 4. Ping pong

With this model, you may choose to collaborate at each step but the person with the keyboard should be given plenty of time and space to experiment.

Works best when the task is one that both developers would be capable of dealing with independently.

- Person A writes a failing test.
- Person B writes some code (as little as possible) to make the test pass.
- Person B writes a failing test.
- Person A writes some code (as little as possible) to make the test pass.
- Repeat from the start.

### 5. Tour guide

Try this for expert-novice pairings.  A 'novice' being _anyone_, regardless of their overall experience, who is not familiar with the codebase in question.

- The expert (tour guide) takes on both strategic and tactical responsibilities (they both drive and navigate).  As they do so, the explain to the novice (tourist) the what and why of the things they're doing.
- The expert must ensure that the novice does not become disengaged.

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=pair_programming/pairing_styles.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=pair_programming/pairing_styles.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=pair_programming/pairing_styles.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=pair_programming/pairing_styles.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=pair_programming/pairing_styles.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
