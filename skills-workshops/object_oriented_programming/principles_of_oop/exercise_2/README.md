## Exercise 2 - Abstraction

If you search the internet for a definition of Abstraction, you'll find something about 'hiding implementation details' and revealing only what is necessary to perform a task. Which sounds a lot like encapsulation and the use of access modifiers (`public`, `protected`, `private` in Java). So what's the difference and from whom are you hiding things?

**Encapsulation is step 1 of Abstraction** because when you move code from being part of a `top-level` to a class, you are 'hiding' some of the implementation details behind the name of the class and its methods. This new arrangement means a reader could understand _what_ the program does, based on the class / methods names, without needing to understand _how_ it does it. Back when the code was a script, the only real option was to read the whole script line by line. Progressing beyond step 1, you can choose to use 'internal' or 'external' abstraction.

* **Internal abstraction** involves breaking up long methods into small methods, which might be more generic and easier to re-use. In this case, you are 'hiding' implementation details inside sensibly named methods.
  
* **External abstraction** involves breaking up large classes into smaller classes, which might be more generic and easier to re-use. In this case, you are 'hiding' implementation details inside sensibly named classes (and their methods).

Both approaches can ease the cognitive load of trying to understand a codebase and, also, they can both remove repetition. Here's a pseudocode example...

```python
# a class for generating traffic stats for London
class LondonTrafficStats:
  # this method "knows"
  # - where the data is stored
  # - how it's stored
  # - how to format it
  # AND how to find the worst road
  def worstRoad():
    # read from the file of traffic stats
    # format the data so I can then do something with it
    # find the road with the worst traffic in London

  # this method "knows"
  # - where the data is stored
  # - how it's stored
  # - how to format it
  # AND how to find the worst road
  def bestRoad():
    # read from the file of traffic stats
    # format the data so I can then do something with it
    # find the road with the least traffic in London
```

We can use internal abstraction to create a third method that takes care of reading and parsing the data

```python
# a class for generating traffic stats for London
class LondonTrafficStats:

  # this method "knows"
  # - where the data is stored
  # - how it's stored
  # - how to format it
  def loadData():
    # load the data
    # format it
    # return it

  # this method "knows"
  # how to find the worst road
  def worstRoad():
    data = loadData()
    # find the road with the worst traffic in London

  # this method "knows"
  # how to find the 'best' road
  def bestRoad():
    data = loadData()
    # find the road with the least traffic in London
```

Some of the implementation details are now 'hidden' inside the new method, away from `worstRoad` and `bestRoad`. As a reader, you now no longer _have_ to immediately confront the implementation details of loading and parsing files.

We could go one stage further and do some external abstraction...

```python
class FileLoader():
  def loadData(self)
    # load the file
    # parse the data
    # return it
```

You could use such a class as it is, or you might choose to use inheritance...

### Your Task

- Have a look at the code in `./exercise_2`
- Some encapsulation has already been done but the codebase could be improved
- Plan at least one internal and at least one external abstraction
- Implement the plan (don't implement any inheritance)
- Be ready to discuss your work when we regroup

> Careful not to go too far. Stop when you have completed the above.

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=object_oriented_programming/principles_of_oop/exercise_2/README.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=object_oriented_programming/principles_of_oop/exercise_2/README.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=object_oriented_programming/principles_of_oop/exercise_2/README.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=object_oriented_programming/principles_of_oop/exercise_2/README.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=object_oriented_programming/principles_of_oop/exercise_2/README.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
