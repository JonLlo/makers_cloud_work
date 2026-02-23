# TDD Process Workshop

## Workshop learning objectives:

*There are no student facing documents for this workshop as the objectives should be drawn out of the students at the end of the workshop as reflections of what they have learnt. They should not be told these upfront so that their approach to the problem is authentic.*

*Prior to the workshop, it's a good idea to set the context of the workshop as a workshop that will be centred on how to break down a problem and approach solving it using TDD.*

- **Learn how to break a problem down into simple steps and translate those steps into tests.**
- **Use strict TDD and use tests to drive your code without making assumptions about implementation.**
- **Further student understanding of TDD.**

This workshop is structured like a process review but with many students rather than just one.

Set student expectations for the workshop and tell them they should imagine they are alone and shouldn’t be talking to one another during the workshop as the aim is to see how they would approach the problem independently.

## Instructions

Ask the students to build a roman numerals app that takes a normal number and converts it to the roman numeral equivalent for the numbers up to and including 10. Say nothing else.

#### First iteration

Tell the students they have 5 minutes to start approaching the problem in the way they see fit.

Walk round the room to observe different approaches the stop them after 5 minutes and ask what they did.

Comment on their approaches with the idea of showing them that rushing into code and setup shouldn’t be the first step to take.
Talk about anything interesting that people did.

#### Second iteration

Encourage them to step back and break the problem down into a series of simple steps as if they were explaining this to a child or someone that doesn’t know anything about code.
Think about clear and specific language.

Give them 5 - 10 minutes

Ask them to summarise the app in one line and draw out useful names for methods and behaviour. For example:
**“This is an app that converts numbers to numerals” => converts sounds like that should be our method name.**

Find out what people said and try and simplify it so it doesn’t involve pseudo code, logic or syntax.

The steps shouldn’t involve jumping ahead and thinking about implementation, for example:

Thinking out black box tests and specifically inputs/outputs

```
Converts 0 to “”
Converts 1 to “I”
Converts 2 to “II”
Converts 3 to “III”
```

#### Third iteration

Give people 15 minutes to take those simple steps and translate them into code.


## Plenary

Discuss what tests people wrote and what code they wrote - see if it’s the simplest implementation and tell them why the simplest implementation is useful:

- Simplest possible solution
- No over engineering
- Helps to identify duplication and see a pattern
- Helps to ultimately solve the real version of this kata which is actually to convert the numbers from 1 - 3000.

Write up the initial code for the first three tests people had. I believe the most basic solution to make the tests go green would be an if/else statement.

After the third test some duplication should be obvious (if number == *number* will be repeated multiple times) and the students should see a pattern and refactor at this point.

```
class RomanNumerals

  def convert(arabic)
    if arabic == 0
      return ""
    elsif arabic == 1
      return "I"
    elsif arabic == 2
      return "II"
    else
      return "III"
    end
  end

end
```

If students have done this then the obvious refactoring is:

```
def convert(arabic_number)
  if arabic_number == 0
    return ""
  else
    return "I" * arabic_number
  end
end
```

Ask students what the lessons are. Common learnings include:

- Don’t rush into coding.
- Break the problem down in very small steps.
- Focus on the simplest test and the simplest code to pass that test.
- Don't solve the problem upfront then try to fit the tests to that solution.


- Get people to reflect on what was learnt/main messages of the workshop and the process and TDD ideas (use the workshop objectives as a guide).

- Go through workshop objectives and do thumbs. Make sure the context of workshop is clear.

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=test_driven_development/tdd_process_workshop_with_roman_numerals_kata/COACH_INSTRUCTIONS.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=test_driven_development/tdd_process_workshop_with_roman_numerals_kata/COACH_INSTRUCTIONS.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=test_driven_development/tdd_process_workshop_with_roman_numerals_kata/COACH_INSTRUCTIONS.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=test_driven_development/tdd_process_workshop_with_roman_numerals_kata/COACH_INSTRUCTIONS.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=test_driven_development/tdd_process_workshop_with_roman_numerals_kata/COACH_INSTRUCTIONS.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
