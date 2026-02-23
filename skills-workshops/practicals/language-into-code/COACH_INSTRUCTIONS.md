# Language into code

## Learning Objectives

- Understand code as being a set of instructions
- Understand  pseudo code as a means of translating requirements into code
- Take a problem, develop pseudocode, and put into code

## Starter (5 minutes)

- Use a physical procedure to demonstrate the idea of code as a set of precise instructions which can be interpreted by the computer e.g. [make a sandwich](https://www.youtube.com/watch?v=euFj8D1A1Kw)

## Exercise 1 -> Group challenge

### 1.1 Idea to pseudocode (as the whole group)

Share the specification below on the board. As a group, discuss the process of turning this specification into pseudocode by considering each smaller problem which needs to be tackled.

Write a program that:
 * Says, “Give me a name”. The user enters a name.
 * Says, “Give me a name” again.  The user enters another name.
 * Continues asking for name until the user types “stop” instead
   of a number.
 * `puts`es the all the names on the terminal separated by a space.

### 1.2 -> Pseudocode to code (coach to demonstrate)

Demonstrate the process of translating the pseudocode created in the last step into a working application.

```ruby
names = []

while true do
 puts “Give me a name”
 name = gets.chomp.capitalize
 if name != “Stop”
   names.push(name)
 else
   p names.join(' ')
   break
 end
end
```

### 2.1 Idea to pseudocode (in groups of 3)

Provide the devs with the following specification:

- Write a program to control a lift which accepts commands to go up and down floors.
- If the user provides a positive number, the lift should go up by that number of floors.
- If the user provides a negative number, the lift should go down by that number of floors.
- The lift starts at floor 0.
- The building has a basement, so the lift *can* go to floors below 0.
- The program should continue to ask for input until the user enter 'stop'
- Once the user chooses to stop, the program should `puts` the number of the floor where the lift is currently located.

Get the devs to come up with a list of procedures to describe the program and arrange these into a piece of pseudocode. Feedback to the whole group each groups attempt and discuss similarities and differences.

### 2.2 Pseudocode to code (in pairs)

Get the devs to write the program from pseudocode to code.

```ruby
current_floor = 0
puts "How many floors would you like to go up/down by?"
while true do
 change = gets.chomp.capitalize
 if change != "stop"
   current_floor += change.to_i
   puts "How many floors would you like to go up/down by?"
 else
   p current_floor
   break
 end
end
```

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=practicals/language-into-code/COACH_INSTRUCTIONS.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=practicals/language-into-code/COACH_INSTRUCTIONS.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=practicals/language-into-code/COACH_INSTRUCTIONS.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=practicals/language-into-code/COACH_INSTRUCTIONS.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=practicals/language-into-code/COACH_INSTRUCTIONS.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
