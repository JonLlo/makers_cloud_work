# SQL Subqueries

There are a few ways to use SQL subqueries but in many cases, subqueries are not the only option. So how do you decide when to use one?

## Learning Objectives

- Compare and contrast queries for readability
- Recognise one case where a subquery is needed
- Recognise one case where a subquery _could_ be problematic

## Exercise

1. Compare pairs of queries
2. Figure out if they generate the same output
3. Decide which one you prefer

---

## Setup

1. Create a database `createdb subqueries_vs_joins`
2. Seed the database `psql -d subqueries_vs_joins -f db_seed.sql`
3. Use `psql` to check everything worked

> You should have 4 non-empty tables
> - `employees`
> - `departments`
> - `customers`
> - `orders`

---

### 1. Employees with above-average salary

**Subquery**
```sql
SELECT name, salary
FROM employees
WHERE salary > (
  SELECT AVG(salary) FROM employees
);
```

**JOIN alternative**

> ‼️ Not possible without a subquery or window function

---

### 2. Employees who work in London

**Subquery**
```sql
SELECT name
FROM employees
WHERE department_id IN (
  SELECT id FROM departments WHERE location = 'London'
);
```

**JOIN alternative**
```sql
SELECT e.name
FROM employees e
JOIN departments d
  ON e.department_id = d.id
WHERE d.location = 'London';
```

---

### 3. Customers who have ordered something

**Subquery**
```sql
SELECT c.customer_id, c.name
FROM customers c
WHERE EXISTS (
  SELECT 1
  FROM orders o
  WHERE o.customer_id = c.customer_id
);
```

**JOIN alternative**
```sql
SELECT DISTINCT c.customer_id, c.name
FROM customers c
JOIN orders o
  ON c.customer_id = o.customer_id;
```

> BONUS QUESTION: What happens if you omit `DISTINCT`?

---

### 4. Top earning employee for each department

**Subquery**
```sql
SELECT e.name, e.salary
FROM employees e
WHERE e.salary = (
  SELECT MAX(salary)
  FROM employees
  WHERE department_id = e.department_id
);
```

**JOIN alternative**

> ❓ Is it possible to do this one without a subquery or window function?

---

### 5. Departments with no employees

**Subquery**
```sql
SELECT name
FROM departments
WHERE id NOT IN (
  SELECT department_id FROM employees
);
```

> ‼️ This version, with the subquery, won't work. How can you fix it and what does it teach you about subqueries?

**JOIN alternative**
```sql
SELECT d.name
FROM departments d
LEFT JOIN employees e
  ON d.id = e.department_id
WHERE e.department_id IS NULL;
```

