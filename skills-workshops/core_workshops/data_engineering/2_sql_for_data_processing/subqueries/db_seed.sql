
-- Table: departments
CREATE TABLE departments (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    location VARCHAR(50)
);

INSERT INTO departments (id, name, location) VALUES
(1, 'HR', 'London'),
(2, 'Engineering', 'New York'),
(3, 'Sales', 'London'),
(4, 'Marketing', 'San Francisco'),
(5, 'Finance', 'New York');

-- Table: employees
CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    salary INT,
    department_id INT REFERENCES departments(id)
);

INSERT INTO employees (id, name, salary, department_id) VALUES
(1, 'Alice', 60000, 1),
(2, 'Bob', 55000, 1),
(3, 'Charlie', 70000, 2),
(4, 'Diana', 80000, 2),
(5, 'Eve', 50000, 3),
(6, 'Frank', 45000, 3),
(7, 'Grace', 75000, NULL);

-- Table: customers
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    name VARCHAR(100)
);

INSERT INTO customers (customer_id, name) VALUES
(1, 'Acme Corp'),
(2, 'Beta Ltd'),
(3, 'Charlie Inc');

-- Table: orders
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT REFERENCES customers(customer_id),
    amount INT
);

INSERT INTO orders (order_id, customer_id, amount) VALUES
(1, 1, 300),
(2, 1, 150),
(3, 2, 500);
