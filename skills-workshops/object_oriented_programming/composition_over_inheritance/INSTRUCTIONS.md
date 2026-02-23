# Composition over Inheritance

> "Prefer Composition to Inheritance"
> – Russ Olsen

A workshop that introduces composition, inheritance, and the benefits of one over the other.

A video of this workshop is available [here](https://www.youtube.com/watch?v=AR1Tdt68Jm4&index=6&list=PLc4BYny7PXeR5ZLHCY_oPU2I97aPtS8jm).

### Outcomes

- Define Inheritance, and define Composition
- Explain why Composition is generally preferable to Inheritance
- Use Composition to abstract shared behaviour

### Terminology

- Inheritance
- Composition
- Mixin
- Behaviour
- Shared Behaviour

### Starter (20 minutes)

- Demonstrate Inheritance using a `Parent` and `Child` class that implement the same method `speak`.
- Demonstrate the shortcomings of Inheritance by violating Liskov and introducing a `misbehave` method to `Child`
- Demonstrate the shortcomings of Inheritance by subclassing `Animal` from `Child` "because we want an `Animal` to speak"
- Demonstrate moving the `speak` method to a module `CanSpeak` and mixing it in to the class by composition.
- Check terminology: Inheritance, Composition, Mixin, Behaviour, Shared Behaviour.

### Main (40 minutes)

- Ask students to come to the board and write down:

| Superhero | Title |
|-----------|------|
| Superman  | Flight |

- Pick a couple. Build a basic `Superhero` class that implements the following (up to the current state of `/lib/superhero.rb` on the main branch:

```ruby
superman = Superhero.new("Superman", "flying")
superman.use_power # => "Superman is now flying!"
```

- **Ask students to implement a `Villain` class that responds to `use_power` with (e.g. `"Galactus is now eating planets, villainously!"`)**
- _Extension_: students should implement some way of having superheroes fight villains. There may be more shared behaviour to extract.

### Plenary (30 minutes)

- Share a few students' code, critique it, and then share the example code from this repository's `plenary` branch (encouraging critique).
- Common issues: 'over-modularising', mixing in state rather than behaviour, using metaprogramming, not using `super`
- Discussion topics: clean design, modules vs. classes for refactoring, `super` and the inheritance chain.

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=object_oriented_programming/composition_over_inheritance/INSTRUCTIONS.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=object_oriented_programming/composition_over_inheritance/INSTRUCTIONS.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=object_oriented_programming/composition_over_inheritance/INSTRUCTIONS.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=object_oriented_programming/composition_over_inheritance/INSTRUCTIONS.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=object_oriented_programming/composition_over_inheritance/INSTRUCTIONS.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
