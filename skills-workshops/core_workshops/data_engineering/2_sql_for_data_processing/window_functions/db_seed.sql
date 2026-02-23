DROP TABLE IF EXISTS sales;
DROP TABLE IF EXISTS transactions;
DROP TABLE IF EXISTS logins;
DROP TABLE IF EXISTS salespeople;

CREATE TABLE salespeople (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    region VARCHAR(50),
    amount INT
);

CREATE TABLE sales (
    id INT PRIMARY KEY,
    region VARCHAR(20),
    product VARCHAR(50),
    amount INT
);


CREATE TABLE transactions (
    id INT PRIMARY KEY,
    customer_id VARCHAR(20),
    amount INT,
    transaction_date DATE
);


CREATE TABLE logins (
    id INT PRIMARY KEY,
    user_id VARCHAR(20),
    login_date DATE
);

INSERT INTO salespeople (id, name, region, amount) VALUES
(1, 'Alice', 'East', 500),
(2, 'Bob', 'North', 400),
(3, 'Carla', 'West', 400),
(4, 'Dan', 'South', 300),
(5, 'Eve', 'East', 450),
(6, 'Frank', 'West', 350),
(7, 'Grace', 'North', 525),
(8, 'Henry', 'South', 275),
(9, 'Iris', 'West', 380),
(10, 'Jack', 'East', 420);

INSERT INTO sales (id, region, product, amount) VALUES (1, 'East', 'Widget', 330);
INSERT INTO sales (id, region, product, amount) VALUES (2, 'North', 'Gizmo', 351);
INSERT INTO sales (id, region, product, amount) VALUES (3, 'North', 'Thingamajig', 478);
INSERT INTO sales (id, region, product, amount) VALUES (4, 'South', 'Widget', 199);
INSERT INTO sales (id, region, product, amount) VALUES (5, 'South', 'Gadget', 264);
INSERT INTO sales (id, region, product, amount) VALUES (6, 'North', 'Gizmo', 316);
INSERT INTO sales (id, region, product, amount) VALUES (7, 'East', 'Doodad', 459);
INSERT INTO sales (id, region, product, amount) VALUES (8, 'South', 'Widget', 51);
INSERT INTO sales (id, region, product, amount) VALUES (9, 'West', 'Widget', 223);
INSERT INTO sales (id, region, product, amount) VALUES (10, 'South', 'Thingamajig', 336);
INSERT INTO sales (id, region, product, amount) VALUES (11, 'East', 'Gadget', 218);
INSERT INTO sales (id, region, product, amount) VALUES (12, 'South', 'Doodad', 105);
INSERT INTO sales (id, region, product, amount) VALUES (13, 'South', 'Gizmo', 314);
INSERT INTO sales (id, region, product, amount) VALUES (14, 'East', 'Thingamajig', 457);
INSERT INTO sales (id, region, product, amount) VALUES (15, 'East', 'Gadget', 144);
INSERT INTO sales (id, region, product, amount) VALUES (16, 'North', 'Gadget', 453);
INSERT INTO sales (id, region, product, amount) VALUES (17, 'East', 'Thingamajig', 202);
INSERT INTO sales (id, region, product, amount) VALUES (18, 'East', 'Thingamajig', 341);
INSERT INTO sales (id, region, product, amount) VALUES (19, 'West', 'Widget', 434);
INSERT INTO sales (id, region, product, amount) VALUES (20, 'West', 'Doodad', 131);
INSERT INTO sales (id, region, product, amount) VALUES (21, 'North', 'Thingamajig', 93);
INSERT INTO sales (id, region, product, amount) VALUES (22, 'East', 'Gizmo', 272);
INSERT INTO sales (id, region, product, amount) VALUES (23, 'South', 'Gadget', 90);
INSERT INTO sales (id, region, product, amount) VALUES (24, 'East', 'Gizmo', 69);
INSERT INTO sales (id, region, product, amount) VALUES (25, 'East', 'Doodad', 455);
INSERT INTO sales (id, region, product, amount) VALUES (26, 'West', 'Gadget', 341);
INSERT INTO sales (id, region, product, amount) VALUES (27, 'West', 'Doodad', 473);
INSERT INTO sales (id, region, product, amount) VALUES (28, 'West', 'Thingamajig', 158);
INSERT INTO sales (id, region, product, amount) VALUES (29, 'East', 'Widget', 168);
INSERT INTO sales (id, region, product, amount) VALUES (30, 'West', 'Doodad', 184);
INSERT INTO sales (id, region, product, amount) VALUES (31, 'West', 'Thingamajig', 378);
INSERT INTO sales (id, region, product, amount) VALUES (32, 'South', 'Thingamajig', 354);
INSERT INTO sales (id, region, product, amount) VALUES (33, 'East', 'Doodad', 379);
INSERT INTO sales (id, region, product, amount) VALUES (34, 'East', 'Thingamajig', 134);
INSERT INTO sales (id, region, product, amount) VALUES (35, 'East', 'Thingamajig', 498);
INSERT INTO sales (id, region, product, amount) VALUES (36, 'East', 'Gadget', 362);
INSERT INTO sales (id, region, product, amount) VALUES (37, 'North', 'Gizmo', 264);
INSERT INTO sales (id, region, product, amount) VALUES (38, 'West', 'Gadget', 197);
INSERT INTO sales (id, region, product, amount) VALUES (39, 'North', 'Gizmo', 495);
INSERT INTO sales (id, region, product, amount) VALUES (40, 'North', 'Gadget', 60);
INSERT INTO sales (id, region, product, amount) VALUES (41, 'South', 'Gadget', 195);
INSERT INTO sales (id, region, product, amount) VALUES (42, 'East', 'Widget', 415);
INSERT INTO sales (id, region, product, amount) VALUES (43, 'East', 'Thingamajig', 53);
INSERT INTO sales (id, region, product, amount) VALUES (44, 'North', 'Thingamajig', 308);
INSERT INTO sales (id, region, product, amount) VALUES (45, 'North', 'Widget', 376);
INSERT INTO sales (id, region, product, amount) VALUES (46, 'South', 'Doodad', 476);
INSERT INTO sales (id, region, product, amount) VALUES (47, 'West', 'Gizmo', 65);
INSERT INTO sales (id, region, product, amount) VALUES (48, 'East', 'Widget', 295);
INSERT INTO sales (id, region, product, amount) VALUES (49, 'South', 'Thingamajig', 235);
INSERT INTO sales (id, region, product, amount) VALUES (50, 'West', 'Gizmo', 385);
INSERT INTO transactions (id, customer_id, amount, transaction_date) VALUES (1, 'CUST5', -106, '2025-02-03');
INSERT INTO transactions (id, customer_id, amount, transaction_date) VALUES (2, 'CUST4', -55, '2025-01-07');
INSERT INTO transactions (id, customer_id, amount, transaction_date) VALUES (3, 'CUST3', 49, '2025-01-02');
INSERT INTO transactions (id, customer_id, amount, transaction_date) VALUES (4, 'CUST4', 424, '2025-02-13');
INSERT INTO transactions (id, customer_id, amount, transaction_date) VALUES (5, 'CUST4', 263, '2025-02-18');
INSERT INTO transactions (id, customer_id, amount, transaction_date) VALUES (6, 'CUST3', 423, '2025-02-26');
INSERT INTO transactions (id, customer_id, amount, transaction_date) VALUES (7, 'CUST1', -131, '2025-01-15');
INSERT INTO transactions (id, customer_id, amount, transaction_date) VALUES (8, 'CUST3', 262, '2025-02-13');
INSERT INTO transactions (id, customer_id, amount, transaction_date) VALUES (9, 'CUST2', 346, '2025-02-23');
INSERT INTO transactions (id, customer_id, amount, transaction_date) VALUES (10, 'CUST1', 358, '2025-02-11');
INSERT INTO transactions (id, customer_id, amount, transaction_date) VALUES (11, 'CUST3', -142, '2025-01-12');
INSERT INTO transactions (id, customer_id, amount, transaction_date) VALUES (12, 'CUST4', -59, '2025-01-11');
INSERT INTO transactions (id, customer_id, amount, transaction_date) VALUES (13, 'CUST2', 63, '2025-02-02');
INSERT INTO transactions (id, customer_id, amount, transaction_date) VALUES (14, 'CUST1', 345, '2025-01-02');
INSERT INTO transactions (id, customer_id, amount, transaction_date) VALUES (15, 'CUST4', 187, '2025-01-27');
INSERT INTO transactions (id, customer_id, amount, transaction_date) VALUES (16, 'CUST5', 116, '2025-02-16');
INSERT INTO transactions (id, customer_id, amount, transaction_date) VALUES (17, 'CUST5', 42, '2025-02-12');
INSERT INTO transactions (id, customer_id, amount, transaction_date) VALUES (18, 'CUST5', -1, '2025-02-02');
INSERT INTO transactions (id, customer_id, amount, transaction_date) VALUES (19, 'CUST3', 310, '2025-02-27');
INSERT INTO transactions (id, customer_id, amount, transaction_date) VALUES (20, 'CUST5', -189, '2025-01-21');
INSERT INTO transactions (id, customer_id, amount, transaction_date) VALUES (21, 'CUST1', 416, '2025-02-22');
INSERT INTO transactions (id, customer_id, amount, transaction_date) VALUES (22, 'CUST5', -130, '2025-02-07');
INSERT INTO transactions (id, customer_id, amount, transaction_date) VALUES (23, 'CUST2', 493, '2025-02-01');
INSERT INTO transactions (id, customer_id, amount, transaction_date) VALUES (24, 'CUST1', 68, '2025-01-09');
INSERT INTO transactions (id, customer_id, amount, transaction_date) VALUES (25, 'CUST1', 444, '2025-02-06');
INSERT INTO transactions (id, customer_id, amount, transaction_date) VALUES (26, 'CUST1', -55, '2025-01-20');
INSERT INTO transactions (id, customer_id, amount, transaction_date) VALUES (27, 'CUST1', 453, '2025-01-26');
INSERT INTO transactions (id, customer_id, amount, transaction_date) VALUES (28, 'CUST2', -105, '2025-01-14');
INSERT INTO transactions (id, customer_id, amount, transaction_date) VALUES (29, 'CUST1', 48, '2025-02-27');
INSERT INTO transactions (id, customer_id, amount, transaction_date) VALUES (30, 'CUST1', 225, '2025-01-31');
INSERT INTO transactions (id, customer_id, amount, transaction_date) VALUES (31, 'CUST2', 411, '2025-01-16');
INSERT INTO transactions (id, customer_id, amount, transaction_date) VALUES (32, 'CUST3', 65, '2025-01-30');
INSERT INTO transactions (id, customer_id, amount, transaction_date) VALUES (33, 'CUST4', 236, '2025-01-14');
INSERT INTO transactions (id, customer_id, amount, transaction_date) VALUES (34, 'CUST2', 368, '2025-02-17');
INSERT INTO transactions (id, customer_id, amount, transaction_date) VALUES (35, 'CUST2', 485, '2025-02-19');
INSERT INTO transactions (id, customer_id, amount, transaction_date) VALUES (36, 'CUST4', -11, '2025-02-26');
INSERT INTO transactions (id, customer_id, amount, transaction_date) VALUES (37, 'CUST4', 261, '2025-02-09');
INSERT INTO transactions (id, customer_id, amount, transaction_date) VALUES (38, 'CUST4', -24, '2025-02-05');
INSERT INTO transactions (id, customer_id, amount, transaction_date) VALUES (39, 'CUST1', 403, '2025-03-02');
INSERT INTO transactions (id, customer_id, amount, transaction_date) VALUES (40, 'CUST3', 310, '2025-01-22');
INSERT INTO transactions (id, customer_id, amount, transaction_date) VALUES (41, 'CUST2', -112, '2025-02-23');
INSERT INTO transactions (id, customer_id, amount, transaction_date) VALUES (42, 'CUST4', -25, '2025-02-23');
INSERT INTO transactions (id, customer_id, amount, transaction_date) VALUES (43, 'CUST5', 29, '2025-01-23');
INSERT INTO transactions (id, customer_id, amount, transaction_date) VALUES (44, 'CUST2', 93, '2025-02-01');
INSERT INTO transactions (id, customer_id, amount, transaction_date) VALUES (45, 'CUST4', 46, '2025-01-18');
INSERT INTO transactions (id, customer_id, amount, transaction_date) VALUES (46, 'CUST3', 367, '2025-02-11');
INSERT INTO transactions (id, customer_id, amount, transaction_date) VALUES (47, 'CUST1', -88, '2025-03-02');
INSERT INTO transactions (id, customer_id, amount, transaction_date) VALUES (48, 'CUST1', 483, '2025-02-27');
INSERT INTO transactions (id, customer_id, amount, transaction_date) VALUES (49, 'CUST3', -179, '2025-01-03');
INSERT INTO transactions (id, customer_id, amount, transaction_date) VALUES (50, 'CUST5', -180, '2025-03-02');
INSERT INTO logins (id, user_id, login_date) VALUES (1, 'USER4', '2025-02-16');
INSERT INTO logins (id, user_id, login_date) VALUES (2, 'USER4', '2025-03-07');
INSERT INTO logins (id, user_id, login_date) VALUES (3, 'USER4', '2025-01-29');
INSERT INTO logins (id, user_id, login_date) VALUES (4, 'USER3', '2025-03-08');
INSERT INTO logins (id, user_id, login_date) VALUES (5, 'USER4', '2025-03-12');
INSERT INTO logins (id, user_id, login_date) VALUES (6, 'USER4', '2025-03-11');
INSERT INTO logins (id, user_id, login_date) VALUES (7, 'USER3', '2025-01-02');
INSERT INTO logins (id, user_id, login_date) VALUES (8, 'USER5', '2025-02-13');
INSERT INTO logins (id, user_id, login_date) VALUES (9, 'USER5', '2025-01-15');
INSERT INTO logins (id, user_id, login_date) VALUES (10, 'USER5', '2025-02-23');
INSERT INTO logins (id, user_id, login_date) VALUES (11, 'USER4', '2025-01-24');
INSERT INTO logins (id, user_id, login_date) VALUES (12, 'USER1', '2025-03-15');
INSERT INTO logins (id, user_id, login_date) VALUES (13, 'USER4', '2025-02-15');
INSERT INTO logins (id, user_id, login_date) VALUES (14, 'USER5', '2025-01-22');
INSERT INTO logins (id, user_id, login_date) VALUES (15, 'USER2', '2025-04-01');
INSERT INTO logins (id, user_id, login_date) VALUES (16, 'USER1', '2025-03-08');
INSERT INTO logins (id, user_id, login_date) VALUES (17, 'USER3', '2025-03-12');
INSERT INTO logins (id, user_id, login_date) VALUES (18, 'USER1', '2025-01-16');
INSERT INTO logins (id, user_id, login_date) VALUES (19, 'USER5', '2025-01-07');
INSERT INTO logins (id, user_id, login_date) VALUES (20, 'USER2', '2025-02-03');
INSERT INTO logins (id, user_id, login_date) VALUES (21, 'USER1', '2025-01-25');
INSERT INTO logins (id, user_id, login_date) VALUES (22, 'USER5', '2025-03-04');
INSERT INTO logins (id, user_id, login_date) VALUES (23, 'USER2', '2025-02-03');
INSERT INTO logins (id, user_id, login_date) VALUES (24, 'USER1', '2025-03-07');
INSERT INTO logins (id, user_id, login_date) VALUES (25, 'USER3', '2025-03-23');
INSERT INTO logins (id, user_id, login_date) VALUES (26, 'USER3', '2025-03-22');
INSERT INTO logins (id, user_id, login_date) VALUES (27, 'USER5', '2025-01-01');
INSERT INTO logins (id, user_id, login_date) VALUES (28, 'USER1', '2025-01-21');
INSERT INTO logins (id, user_id, login_date) VALUES (29, 'USER3', '2025-03-20');
INSERT INTO logins (id, user_id, login_date) VALUES (30, 'USER3', '2025-02-28');
INSERT INTO logins (id, user_id, login_date) VALUES (31, 'USER4', '2025-03-17');
INSERT INTO logins (id, user_id, login_date) VALUES (32, 'USER1', '2025-01-04');
INSERT INTO logins (id, user_id, login_date) VALUES (33, 'USER4', '2025-02-28');
INSERT INTO logins (id, user_id, login_date) VALUES (34, 'USER2', '2025-03-10');
INSERT INTO logins (id, user_id, login_date) VALUES (35, 'USER5', '2025-02-16');
INSERT INTO logins (id, user_id, login_date) VALUES (36, 'USER2', '2025-02-05');
INSERT INTO logins (id, user_id, login_date) VALUES (37, 'USER2', '2025-03-29');
INSERT INTO logins (id, user_id, login_date) VALUES (38, 'USER3', '2025-02-04');
INSERT INTO logins (id, user_id, login_date) VALUES (39, 'USER4', '2025-01-14');
INSERT INTO logins (id, user_id, login_date) VALUES (40, 'USER3', '2025-03-02');
INSERT INTO logins (id, user_id, login_date) VALUES (41, 'USER2', '2025-01-24');
INSERT INTO logins (id, user_id, login_date) VALUES (42, 'USER4', '2025-01-07');
INSERT INTO logins (id, user_id, login_date) VALUES (43, 'USER3', '2025-01-29');
INSERT INTO logins (id, user_id, login_date) VALUES (44, 'USER2', '2025-02-20');
INSERT INTO logins (id, user_id, login_date) VALUES (45, 'USER4', '2025-03-11');
INSERT INTO logins (id, user_id, login_date) VALUES (46, 'USER2', '2025-02-10');
INSERT INTO logins (id, user_id, login_date) VALUES (47, 'USER3', '2025-01-23');
INSERT INTO logins (id, user_id, login_date) VALUES (48, 'USER1', '2025-01-13');
INSERT INTO logins (id, user_id, login_date) VALUES (49, 'USER2', '2025-02-28');
INSERT INTO logins (id, user_id, login_date) VALUES (50, 'USER4', '2025-01-07');
INSERT INTO logins (id, user_id, login_date) VALUES (51, 'USER2', '2025-03-22');
INSERT INTO logins (id, user_id, login_date) VALUES (52, 'USER1', '2025-02-11');
INSERT INTO logins (id, user_id, login_date) VALUES (53, 'USER2', '2025-03-30');
INSERT INTO logins (id, user_id, login_date) VALUES (54, 'USER4', '2025-03-23');
INSERT INTO logins (id, user_id, login_date) VALUES (55, 'USER3', '2025-03-30');
INSERT INTO logins (id, user_id, login_date) VALUES (56, 'USER1', '2025-02-04');
INSERT INTO logins (id, user_id, login_date) VALUES (57, 'USER2', '2025-01-21');
INSERT INTO logins (id, user_id, login_date) VALUES (58, 'USER1', '2025-03-25');
INSERT INTO logins (id, user_id, login_date) VALUES (59, 'USER5', '2025-02-12');
INSERT INTO logins (id, user_id, login_date) VALUES (60, 'USER4', '2025-03-07');