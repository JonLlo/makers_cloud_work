# How to coach multi class systems workshop

*Recommended timing: early/mid Week 2 Golden Square.*

This has only as yet been tried out on one cohort a lot of whom had previous experience so your experience may differ from mine, if you try it please do update here with any
learnings/tweaks, let's iterate!

This workshop is all about getting the learners to slow down and make the most of the design process for more complicated systems.
There's no coding involved, although if they're keen beans you could let them continue pairing on the exercise after the workshop to start on implementation.

(If you've already run the [Age Averager workshop](https://github.com/PaulNGilson/workshops_at_makers/tree/main/golden_square/age_averager_design_recipe) in Week 1 this is also very Design Recipe
focused so you may want to demo some implementation instead but I have not tried this with this particular exercise)

## Key points to draw out

- There is no one true/obvious implementation for this exercise. Everyone will come at it with their own assumptions, so the design process is a great place for digging out those assumptions
and coming to a shared understanding of what needs to be built.
- You could have separate classes for Potion and Weapon, or a single Item class. Devs with some previous experience might even suggest inheritance for these.
- The "attack another character" API needs some consideration as to what feels intuitive as well as allowing access to info about the attacker's weapon damage capability. A few ways to skin this particular cat!
- What are the behaviours they need to define around inventory, and can they resist the temptation to bake assumptions about underlying data structures into their test examples?
- At least some of the learners will likely find that their API design needs adjusting during their example writing phase. This is a good demonstration of the value of doing this bit of design up front
- At some point a decision must be made about which weapon from the inventory is used for a given attack. How do they solve this, can they state their assumptions clearly and agree on an approach?

@lotte

