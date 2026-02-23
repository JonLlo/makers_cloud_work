### Example CRC

This is an example of using Class-Responsibility-Collaborator cards to model a domain.

#### The User Stories

```
As a customer
So I can get a bicycle
I want to withdraw a bicycle from a docking station
```

```
As a customer
So I can complete my trip
I want to dock a bicycle back at a docking station
```

```
As a customer
So I can have the best cycling experience
I want to only get working bikes from the docking station
```

```
As an administrator
So I can tell how many bikes are at each docking station
I want to get a count of the number of bikes at the docking station
```

#### Suggested CRC

```
|-----------------------------------|
|                Bike               |
|-----------------------------------|
| Responsibilities |  Collaborators |
|-----------------------------------|
| Knows if working |                |
|-----------------------------------|

|----------------------------------|
|         Docking Station          |
|----------------------------------|
| Responsibilities | Collaborators |
|----------------------------------|
| Release a bike   | Bike          |
| Dock a bike      |               |
| Count bikes      |               |
|----------------------------------|

```

#### Suggested Database Structure

```
Table: bikes
|-------------------|-----------------------|
|  id  |   working  |   docking_station_id  |
|-------------------|-----------------------|
|   1  |    true    |           1           |
|-------------------|-----------------------|

Table: docking_stations
|-----|
| id  |
|-----|
|  1  |
|-----|
```

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=how_databases_work/domain_modelling_student_directory_using_crc_cards/crc_example.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=how_databases_work/domain_modelling_student_directory_using_crc_cards/crc_example.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=how_databases_work/domain_modelling_student_directory_using_crc_cards/crc_example.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=how_databases_work/domain_modelling_student_directory_using_crc_cards/crc_example.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=how_databases_work/domain_modelling_student_directory_using_crc_cards/crc_example.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
