-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS posts;
DROP SEQUENCE IF EXISTS posts_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS posts_id_seq;
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    content VARCHAR(255),
    tags VARCHAR(255)[]
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO posts (title, content, tags) VALUES ('Why I Always Lose My Keys', 'Every morning it''s the same ritual: frantically searching through coat pockets, under couch cushions, and in yesterday''s jeans. I''ve tried key hooks by the door, but somehow they still end up in the weirdest places.', ARRAY['lifestyle', 'personal']);
INSERT INTO posts (title, content, tags) VALUES ('The Art of Waiting for Toast', 'Standing by the toaster, watching the bread slowly turn golden brown, is one of life''s most underrated meditative experiences. Too light and it''s disappointing, too dark and breakfast is ruined.', ARRAY['food', 'mindfulness']);
INSERT INTO posts (title, content, tags) VALUES ('My Relationship with Laundry', 'Clean clothes pile up on the chair for weeks while I dig through the basket for that one shirt I actually want to wear. The folding part is where good intentions go to die.', ARRAY['lifestyle', 'humor']);
INSERT INTO posts (title, content, tags) VALUES ('Grocery Store Checkout Line Philosophy', 'Why do I always choose the slowest line? There''s an art to reading the signs: the person with a full cart but organized coupons versus the guy with three items who can''t find his wallet.', ARRAY['observations', 'humor']);
INSERT INTO posts (title, content, tags) VALUES ('The Perfect Room Temperature Debate', 'Living with roommates means endless thermostat wars. Someone''s always too hot or too cold, and somehow 72 degrees feels different depending on who set it.', ARRAY['lifestyle', 'relationships']);
