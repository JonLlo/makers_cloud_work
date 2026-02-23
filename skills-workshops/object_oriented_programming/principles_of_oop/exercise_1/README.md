## Exercise 1: Encapsulation

**Encapsulation is our starting point**. It's about bundling together related data (state) and the methods (behaviour) that operate on that data into a single unit (a class). Encapsulation also involves controlling access to these data and methods, ensuring that only the necessary parts are exposed to the outside world while protecting the rest. In some languages, this control is typically achieved through access modifiers (like `private`, `protected`, and `public`), which determine which parts of the class are accessible from outside.

In Python...
- **private** methods start with `__` (double underscore)
- **protected** methods start with `_` (single underscore)
- **public** methods do not have a prefix

### Ice

You've just been hired by Ice who build a platform that is also called Ice - it's like Steam but... cooler? Anyway, Ice is in its infancy and the Ice platform only exists on paper. Right now, there are just two games that can be played and the codebase is a bit of a mess. If there were not plans to extend the codebase and make a proper platform then we could just leave it all as it is, but Ice have big ambitions.

### Your Task

Have a look at the code in [exercise_1](./games.py). In there, you'll find a script that allows a user to play two games one after the other - the first is a number guessing game and the second is a quiz. Nothing is wrapped in a class, it's all just there, out in the open for all the world to see. Playing the game is simple, you just need to do `python3 ./games.py` (if you're in the `exercise_1` directory).

Your job is to do some encapsulation...
- Decide how many classes to create, what their names should be and what state/behaviour goes into each
- Create the classes
- Think about access modifiers - what state/behaviour should be private or protected?

> Careful not to go too far. Stop once you have completed the above.

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=object_oriented_programming/principles_of_oop/exercise_1/README.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=object_oriented_programming/principles_of_oop/exercise_1/README.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=object_oriented_programming/principles_of_oop/exercise_1/README.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=object_oriented_programming/principles_of_oop/exercise_1/README.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=object_oriented_programming/principles_of_oop/exercise_1/README.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
