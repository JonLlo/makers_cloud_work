# Databases - Modelling a database to satisfy user stories

In this workshop we'll explore how to model a database - what data needs to be stored, with what structure.

## Learning objectives

An exercise to learn three things:

1. Explain what a database model is.
2. Model a database to comply to user stories.
3. Explore different ways data can be stored and compare their merits.

## Instructions

Following are some user stories.

For each story, draw out the structure of the database that is needed to store the data used in the story.

* What tables are needed?
* What columns do these tables have?
* What SQL query will need to be run to satisfy the user story?

Here's an example model that complies with the first user story:

```
Table: students          
Columns: id, name        
                         
example:  |  id  |       name      |
          |------------------------|
          |  1   |  "Jenny Smith"  |
          |  2   |  "Bob Martin"   |                        


Query: "SELECT name FROM students;"

example result:    "Jenny Smith"
                   "Bob Martin" 
```

#### Notes
- Your model will need to change to adapt to each new user story. Eventually, you will need to use foreign keys and associations. There may be one or more 'join' tables involved too, in order to implement many-to-many relationships.

- Work on each story at a time, so you can see the model evolving, rather than all the stories in one go. Are there alternative ways you could store the necessary data?

**Tip:** It can be useful to use a spreadsheet to model tables easily. Create a new Google Spreadsheet by going to [sheet.new](http://sheet.new).

## Resources

- [SQL Reference](https://www.codecademy.com/learn/learn-sql/modules/learn-sql-queries/cheatsheet)
- [ELI5: Relational Databases](https://www.reddit.com/r/explainlikeimfive/comments/3qqm9h/eli5_relational_databases/)
- [ActiveRecord guide: Database Associations](http://guides.rubyonrails.org/association_basics.html#the-types-of-associations) (with diagrams!)

## User Stories

```
As a coach
So I can get to know all students
I want to see a list of students' names
```

```
As a coach
So I can link a name to a face
I want to see a URL with their picture next to each student
```

```
As a coach
So I don't get overwhelmed with a massive list of everyone
I want to filter the list of students by cohort
```

```
As a coach
So I can prepare for Day One and Demo Day
I want to see the start date and demo day date of a cohort
```

```
As a student
So I can plan my life
I want to see my demo day date 
```

```
As a student
So I can reflect on my days
I want to rate each day out of 10
```

```
As a coach
So I can get an overview of how students are feeling
I want to see an average of the day ratings for each student
```

```
As a coach
So I can tag certain students
I want to tag a student with many named tags (like "happy" or "ok")
```

```
As a coach
So I can see students with the same tag
I want to filter students in the list by tag name
```

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=how_databases_work/modelling_a_db_without_crc_cards/README.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=how_databases_work/modelling_a_db_without_crc_cards/README.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=how_databases_work/modelling_a_db_without_crc_cards/README.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=how_databases_work/modelling_a_db_without_crc_cards/README.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=how_databases_work/modelling_a_db_without_crc_cards/README.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
