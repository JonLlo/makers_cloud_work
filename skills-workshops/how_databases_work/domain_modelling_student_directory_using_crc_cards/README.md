# Databases - Domain Modelling using CRC Cards

Class Responsibility Collaborator cards are one approach to modelling a domain.  See this [example](crc_example.md).

## Learning objectives

An exercise to learn three things:

1. Explain how to use CRC cards to model a domain
2. Model a simple domain using CRC cards
3. Infer database structure from domain structure

## Instructions

Following are some user stories.

### Use CRC cards to model the domain (20 mins)

Using [CRC cards](http://agilemodeling.com/artifacts/crcModel.htm), model the domain in an Object-Oriented way.

### Create a database structure for the domain model (20 mins)

Draw out the structure of the database for the model you have built, in the following way (the example is a possible implementation of a `cohorts` table):

```
Table: cohorts

|  id  |     name     |
|---------------------|
|  1   |  "May 2016"  |
```

> You will probably need to use foreign keys and associations. There may be one or more 'join' tables involved too, in order to implement many-to-many relationships.

## Resources
- [ActiveRecord guide: Database Associations](http://guides.rubyonrails.org/association_basics.html#the-types-of-associations) (with diagrams!)
- [ELI5: Relational Databases](https://www.reddit.com/r/explainlikeimfive/comments/3qqm9h/eli5_relational_databases/)


## User Stories

```
As a coach
So I can get to know all students
I want to see a list of students' names
```

```
As a coach
So I don't get overwhelmed with a massive list of everyone
I want to filter the list of students by cohort name
```

```
As a coach
So I can prepare for Day One and Demo Day
I want to see the start date and demo day date of a cohort
```

```
As a coach
So I can learn students' names
I want each student to give a link to the URL of a picture of them
```

```
As a student
So I can reflect on my days
I want to rate each day out of 10
```

```
As a coach
So I can get an overview of feedback
I want to see an average of the day ratings for each student
```

```
As a coach
So I can mark certain students
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
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=how_databases_work/domain_modelling_student_directory_using_crc_cards/README.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=how_databases_work/domain_modelling_student_directory_using_crc_cards/README.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=how_databases_work/domain_modelling_student_directory_using_crc_cards/README.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=how_databases_work/domain_modelling_student_directory_using_crc_cards/README.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=how_databases_work/domain_modelling_student_directory_using_crc_cards/README.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
