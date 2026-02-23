# Extracting Classes

## Learning Objectives:

- Know how to annotate code
- Spot indicators for similar behaviour
- Extract a class

## Starter (15 minutes)

- Set out objectives.
- Diagram an interaction of `Car#driver=(arg)` or `Car#driver_name`
- Discuss what annotation is and demonstrate fully annotating `Car#initialize` and a couple other methods.
- Q&A

## Main (40 minutes)

Instructions are in [the README](README.md).
Students in pairs
  - model the current domain
  - annotate the code in `/exercise/lib` (check the `annotations` branch for an example set of annotations in `/lib/car.rb`)
  - diagram a new domain based on their findings
  - extract classes one by one, test first. (usually encapsulate logic in `Person`, and extract an `Engine` object is a good indicator in 40 mins)

## Plenary (30 minutes)

Questions & Reflections

Common questions:

- Code Quality -> when to extract?
- Creating objects -> Why pass in data as a hash to a constructor?
- Modelling Reality, rather than looking at complexity -> Why encapsulate engine and motor, isn't speed part of the engine?
- Testing -> How to test in the Original class that the extracted component is working?
- Extraction -> What are the steps to take? Test first? Which component first? When to extract?
- Inheritance v Composition

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=object_oriented_programming/extracting_a_class/COACH_INSTRUCTIONS.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=object_oriented_programming/extracting_a_class/COACH_INSTRUCTIONS.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=object_oriented_programming/extracting_a_class/COACH_INSTRUCTIONS.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=object_oriented_programming/extracting_a_class/COACH_INSTRUCTIONS.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=object_oriented_programming/extracting_a_class/COACH_INSTRUCTIONS.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
