# Spec-Driven Development in Java

The most popular IDE for programming in Java is IntelliJ. So, if you're an apprentice heading towards working in a Java team, you'll probably be using IntelliJ at work. If you're an Academy dev, who will soon be applying for Java jobs, knowing how to use IntelliJ will be a bonus for you too :)

Unfortunately, at the time of writing (20/11/2025), the Copilot plugin for IntelliJ doesn't fully implement all of GitHub Copilot's features, but we can build a workaround.

Your task is to work through steps 1, 2 and 3 below. This will involve...

- Creating a new project
- Adding a `copilot-instructions.md` and a `plan.md`
- Checking Copilot can find your `plan.md`
- Instructing Copilot to get started on the first feature

Read on for further details about each step.

## 1. Create a new project in IntelliJ

- If you already have IntelliJ open on another codebase, find it and go to `File` > `New` > `Project`.
- Give the project a name and choose whichever version of Java you are currently using.
- Then, click `Create` to continue

You will now have a basic application skeleton with some placeholder code in it. You don't need to change anything manually. Copilot will tidy things up :)

## 2. Add a `copilot-instructions.md`

One of the few features that works reliably in IntelliJ is `copilot-instructions.md`. Here, we'll use it to point at our specification.

Use this template, but adapt it as you see fit, based on your results.

```md
# copilot-instructions.md

## Style Guide
- All generated code should be clear, concise and correct (in that order)
- Use simple implementations over clever abstractions where possible
- Always use descriptive variable and class names
- Follow Java naming conventions (PascalCase for classes, camelCase for methods/variables)
- Include JavaDoc comments for public methods and classes

## Plans and specifications

The specifications for this project are in a file called "plan.md"
- Only work on features marked as "TODO" or "IN PROGRESS" 
- Do not modify features marked as "COMPLETED"
- Always read plan.md before starting any work

## Process

### Feature Development Flow
1. When prompted, identify the next feature in plan.md marked as "TODO"
2. Break the feature down into 3-5 small, testable steps
3. Update plan.md to show the breakdown and mark feature as "IN PROGRESS"
4. **STOP and wait for confirmation before proceeding**

### TDD Implementation
5. Write a failing test for the first step (RED)
  - Use the test cases in plan.md to guide you
6. Write minimal code to make the test pass (GREEN)
  - Update the relevant test case, if there is one, to show it's passed
7. **STOP after each step** - present only the test and implementation code
8. Wait for review/approval before moving to the next step
9. Update plan.md to mark completed steps with checkboxes

### Completion
10. Mark feature as "COMPLETED" in plan.md only after all tests pass
11. Quiz me with 2-3 questions about the implementation

## Code Review Guidelines
- Present changes in small, focused code blocks
- Always include the file path in code blocks
- Highlight what each code change accomplishes
- If modifying existing code, clearly show what's being changed

## Boundaries
- Only implement what's specified in plan.md
- Do not add "helpful" features not requested
- Do not refactor existing working code unless specifically asked
- If you're unsure about requirements, ask for clarification rather than making assumptions

## File Structure Expectations
- Tests should go in `src/test/java` following Maven conventions
- Source code should go in `src/main/java`
- Each class should have a corresponding test class (e.g., `Calculator.java` → `CalculatorTest.java`)
```

## 3. Add a `plan.md`

As mentioned above, `plan.md` will contain the specification for your app, in the form of some features. Today, we're going to build a command line app. You can decide exactly what you want your command line app to do and adapt our example (or you can just use our example).

> I used GitHub Copilot to help me write this, based on an initial (much shorter) first draft which described the core functionality I desired.

<br>
<details><summary>The original version</summary>
<hr>
<pre>
# plan.md

This document describes the specification for an app. Use it to guide your work in building the app. You can update this file as needed. If there are any conflicts between this file and `copilot-instructions.md`, as me for clarification before proceeding.
 
## Summary
This is a quiz app to be used by people who are learning Java. It should have a bank of 100 questions, evenly distributed between introductory, intermediate and advanced difficulty levels. When generating the application codebase, one of your tasks will also be to generate the questions based on your knowledge of Java.

Users will interact with the application on the command line. They will first be asked how many questions they would like. Then they will be asked the questions one by one. A record of which questions were asked and whether they got the right answer will be stored in a text file which can be read by the application and used to decide which questions should be asked in future. When the user gets an answer wrong, they should be asked that question again soon. When they get an answer right, they should not be asked that question again until a lot later. The first set of questions should all be "introductory" level. Based on performance, the app might increase the difficulty next time.
</pre>
<hr>
</details>
<br>

<details><summary>Refining the original</summary>
<hr>
<p>
<h3>Me</h3>
This is a spec to be used by an AI agent to generate code. I will add a list of ordered features later (let's not think about that yet). For now,  let's focus on the Summary. Please read it, ask me any clarifying questions you might have and then based on my answers, propose a new version.
</p>
<p>
<h3>AI</h3>

Looking at your Summary, I have several clarifying questions to help make the specification more precise.

Clarifying Questions:

1. Question Bank Generation: Should the 100 questions be hardcoded in the application, stored in a separate file, or generated dynamically? What format should they be in (multiple choice, true/false, short answer)?
2. Performance Tracking: What constitutes "soon" vs "a lot later" for re-asking questions? Should this be measured in number of sessions, questions asked, or time elapsed?
3. Difficulty Progression: How should the app determine when to increase difficulty? Is it based on a percentage of correct answers, consecutive correct answers, or some other metric?
4. File Storage Format: What should the structure of the text file be? Should it store question IDs, timestamps, correctness, difficulty levels, etc.?
5. Session Management: Should the app track individual sessions or cumulative performance across all sessions? Can users have different profiles?
6. Question Selection Algorithm: When selecting which questions to ask, how should the app balance between:
   - Questions the user got wrong recently
   - Questions from appropriate difficulty level
   - Questions not asked in a while
7. Answer Format: What types of answers should the app accept? Case-sensitive? Exact matches or fuzzy matching?

Please clarify these points so I can propose an improved Summary that will give clearer guidance to the AI agent.
</p>
<p>
<h3>Me</h3>

1. They can be hard coded and stored in a text file that is read by the app, or hard coded in a Java class – whatever feels right.
2. Time elapsed
3. Consecutive correct answers, I think, but I am open to challenge
4. Yes, it would need to store all of those things. Re: format – I think this depends on how the program is implemented.
5. Cumulative performance. One profile.
6. 25%, 50%, 25%
7. The questions should all be MCQs so the learner can answer unambiguously using a number

</p>
<hr>
</details>
<br>

```md
# plan.md
This document describes the specification for an app. Use it to guide your work in building the app. You can update this file as needed. If there are any conflicts between this file and copilot-instructions.md, as me for clarification before proceeding.

## Summary
This is a Java quiz app for people learning Java programming. The app maintains a bank of 100 multiple choice questions evenly distributed across three difficulty levels: introductory (33 questions), intermediate (33 questions), and advanced (34 questions). Questions can be hardcoded in the application (either in a text file or Java class).

### User Interaction
Users interact via command line and are prompted to specify how many questions they want to answer. Questions are presented as multiple choice with numbered options, and users respond by entering the corresponding number.

### Question Selection Algorithm
When selecting questions, the app should prioritize:
- 25% questions the user answered incorrectly (to be re-asked sooner based on time elapsed)
- 50% questions from the user's current difficulty level that haven't been asked recently
- 25% questions the user hasn't seen before or got right long ago

### Performance Tracking
The app tracks cumulative performance across all sessions in a persistent text file, storing:
- Question ID and difficulty level
- Whether the answer was correct
- Timestamp of when the question was asked
- User's selected answer

### Difficulty Progression
All users start at introductory level. The app increases difficulty level based on consecutive correct answers within the current difficulty level (you'll need to define the threshold during implementation).

### Data Persistence
Performance data persists between sessions, allowing the app to make informed decisions about which questions to ask based on:
- Time elapsed since last asking a question
- User's historical performance on specific questions
- Current difficulty level progression

## Features

### Feature 1: Basic Question Model
- **Status**: TODO
- **User Story**: As a developer, I need a way to represent quiz questions so that I can build the quiz functionality
- **Description**: Create a Question class that can store a multiple choice question with its options, correct answer, difficulty level, and unique ID
- **Test Cases**:
  - ❌ Can create a question with text, options, correct answer index, and difficulty
  - ❌ Can retrieve question text and options
  - ❌ Can validate if a given answer is correct
  - ❌ Question has a unique ID

### Feature 2: Question Bank Management
- **Status**: TODO
- **User Story**: As a quiz app, I need a collection of questions so that users can take quizzes
- **Description**: Create a QuestionBank class that loads and manages 100 hardcoded questions (33 intro, 33 intermediate, 34 advanced)
- **Test Cases**:
  - ❌ Can load questions from hardcoded data
  - ❌ Returns correct number of questions per difficulty level
  - ❌ Can retrieve questions by difficulty level
  - ❌ Can retrieve question by ID

### Feature 3: Basic Quiz Session
- **Status**: TODO
- **User Story**: As a user, I want to answer a specified number of random questions so that I can practice Java
- **Description**: Create a QuizSession class that can present a specified number of random questions and collect answers
- **Test Cases**:
  - ❌ Can start a quiz with specified number of questions
  - ❌ Can present a question with numbered options
  - ❌ Can accept numeric answers (1-4)
  - ❌ Can track correct/incorrect answers
  - ❌ Can display final score

### Feature 4: Command Line Interface
- **Status**: TODO
- **User Story**: As a user, I want to interact with the quiz through the command line so that I can take quizzes easily
- **Description**: Create a CLI that prompts for number of questions, displays questions with options, and shows results
- **Test Cases**:
  - ❌ Prompts user for number of questions
  - ❌ Displays questions with numbered options clearly
  - ❌ Accepts and validates numeric input
  - ❌ Handles invalid input gracefully
  - ❌ Shows final score and percentage

### Feature 5: Performance Data Storage
- **Status**: TODO
- **User Story**: As a user, I want my quiz performance to be remembered so that the app can improve over time
- **Description**: Create a PerformanceTracker that saves quiz results to a persistent text file
- **Test Cases**:
  - ❌ Can save question attempts with timestamp, question ID, correctness, and user answer
  - ❌ Can load existing performance data from file
  - ❌ Creates new file if none exists
  - ❌ Handles file I/O errors gracefully

### Feature 6: User Progress Tracking
- **Status**: TODO
- **User Story**: As a user, I want to progress through difficulty levels so that questions match my skill level
- **Description**: Implement difficulty progression based on consecutive correct answers within current level
- **Test Cases**:
  - ❌ New users start at introductory level
  - ❌ Tracks consecutive correct answers within difficulty level
  - ❌ Advances to next level after threshold (e.g., 5 consecutive correct)
  - ❌ Persists current difficulty level between sessions
  - ❌ Cannot advance beyond advanced level

### Feature 7: Smart Question Selection
- **Status**: TODO
- **User Story**: As a user, I want the app to ask me relevant questions so that I focus on areas that need improvement
- **Description**: Implement intelligent question selection algorithm (25% incorrect, 50% current level, 25% new/old correct)
- **Test Cases**:
  - ❌ Prioritizes recently incorrect answers (25% of questions)
  - ❌ Selects from current difficulty level for 50% of questions
  - ❌ Includes new or old questions for 25% of questions
  - ❌ Falls back gracefully when categories don't have enough questions
  - ❌ Uses time elapsed to determine "recent" vs "old"

### Feature 8: Session History and Analytics
- **Status**: TODO
- **User Story**: As a user, I want to see my progress over time so that I can track my learning
- **Description**: Add ability to view performance statistics and session history
- **Test Cases**:
  - ❌ Can display overall accuracy by difficulty level
  - ❌ Shows improvement trends over time
  - ❌ Displays most commonly missed question types
  - ❌ Shows current difficulty level and progress toward next level
  - ❌ Can view recent session results
```

## 4. Check Copilot can find your `plan.md`

Ask Copilot "what's the plan"? If it can find your `plan.md` it will describe the plan you have provided there. If it doesn't do that, you should move your `plan.md` to the top level of your project (out of `.github`).

## 5. Instruct Copilot to start work

Now you're ready to instruct Copilot, in Agent mode, to start working on your app. If we've set things up well, it will do exactly what you want, in small steps.

Tell copilot something like...

```
OK let's work on the next feature!
```

And it *should* jump into action.

You will need to pay close attention to what Copilot is doing, checking it's work and approving or rejecting it's changes as you go along.

## Further Reading

There are several tools which are designed to implement Spec-Driven Development. We chose not to use them here because we wanted to keep a tight scope, focusing on GitHub Copilot. You might, however, find it interesting to do your own research into...

- [Spec-Kit](https://github.com/github/spec-kit), a tool developed by GitHub for generating specs
- [Kiro](https://kiro.dev/), an IDE with Spec-Driven Development at it's heart
- [A summary of both tools](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html) on Martin Fowler's blog.

