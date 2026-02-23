# Answers

- Need to seed the db in `test_artist_repository.py::test_get_all_records`
    - if they run `pytest` (without -x) they should first see 5 failing tests and then 6 failing tests, because the deletion test affects the second run

- in `test_artist_repository.py::test_get_single_record`, need to use int for id, rather than string
    - I (Lotte) found this quite hard to spot and ended up printing `artist.__dict__` to see the difference, but the learners I ran it with spotted it pretty quick!

- in `artist_repository.py`, don't provide an id when inserting into db (and update corresponding `test_artist_repository.py::test_create_record`)
    - *This is an important one to talk through* because some learners will fix the test by inserting The Beatles with id 5, rather than realising that they shouldn't be providing an id at all!

- in `test_artist_repository.py::test_get_single_record`, look for ABBA not Abba
    - will probably need `pytest -vv` flag to see this
