## Exercise 3 - Inheritance and Polymorphism

### Inheritance

If you are doing **external abstraction** and creating new classes, you need a way to then use those classes. That's where **inheritance** comes in.

**Inheritance** allows you to create new classes based on existing classes that were created by **external abstraction**. The new (child) class receives (i.e. _inherits_) the attributes and methods of the abstract (parent) class, meaning it can reuse the functionality defined in the parent without having to rewrite it. In real life, children don't end up with _all_ the attributes of their parents, so perhaps that metaphor isn't great. Another way to think about it is to imagine the contents of one class (the abstract class) being _poured into_ the other class. Absolutely everything is shared. This reduces code duplication and allows you to build complex systems more efficiently. With inheritance, your abstract classes become powerful tools for reducing repetition across multiple classes.

> NOTE: Inheritance is not the only mechanism for sharing code, but it's the only one we'll cover here! If you want to look up some others, search for 'interfaces' and 'modules'.

### Polymorphism

Once you have classes that inherit from a common abstract class, you can take advantage of **polymorphism**. Polymorphism, which means "many forms," allows objects of different classes to be treated as objects of a common parent class. This is especially useful because it means that a single function can operate on objects of different classes without needing to know their specific types. Each subclass can implement methods defined in the parent class in its own way, but the calling code doesn't need to worry about the specifics. It just calls the method, and the right behaviour occurs based on the object's actual class. In statically typed languages like Java, this also means that the abstract class can be used as a type, enabling powerful design patterns and flexible code structures.

### Your Task

Reduce repetition and remove the need for type checking (in `icePlatform`) using inheritance and polymorphism.

To do this, **either**...

- Use your abstract class/es from exercise 2

OR

- Use the code in `exercise_3` as your starting point

> NOTE: Inheritance has already been implemented in the `exercise_3` codebase, so you should focus on Polymorphism if you're starting from there.

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=object_oriented_programming/principles_of_oop/exercise_3/README.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=object_oriented_programming/principles_of_oop/exercise_3/README.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=object_oriented_programming/principles_of_oop/exercise_3/README.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=object_oriented_programming/principles_of_oop/exercise_3/README.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=object_oriented_programming/principles_of_oop/exercise_3/README.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
