
# Window Functions

---

## Part 1: Anatomy of a Window Function

A **window function** performs a calculation across a set of rows that are **related to the current row**.
This set of related rows is called **the window**.

### General Form

```sql
function_name(expression) 
OVER (
    PARTITION BY some_column
    ORDER BY another_column
    ROWS BETWEEN ... AND ...
)
```

### Key Parts

* **`function_name(expression)`**: e.g. `SUM(amount)`, `ROW_NUMBER()`, `LAG(salary)`.
* **`PARTITION BY`**: Divides the data into groups (like `GROUP BY`, but rows are *not collapsed*).
* **`ORDER BY`**: Sets the order of rows *inside each partition* — important for ranking, running totals, comparisons.
* **`ROWS BETWEEN …`)**: Optional. Defines how many rows before/after are included in the calculation.


### Example 1: Compare each sale with the total regional sales

```sql
SELECT *, SUM(amount) OVER (PARTITION BY region) FROM sales
```


### Example 2: Calculate the balance after each transaction

```sql
SELECT *, SUM(amount) OVER (ORDER BY transaction_date) as balance FROM transactions
```

* **Window**: all rows from the first sale up to the current row, ordered by `sale_date`.

### Example 3: Rank transactions

```sql
SELECT *, RANK() OVER (ORDER BY amount DESC) FROM transactions;
```

---

### Visual: Window Concept

Imagine this data:

| Row | Date  | Amount |
| --- | ----- | ------ |
| 1   | Jan 1 | 100    |
| 2   | Jan 2 | 200    |
| 3   | Jan 3 | 150    |

For row 3 (`Jan 3`), the **window** with
`SUM(amount) OVER (ORDER BY date)`
includes rows 1, 2, and 3.
So the running total at `Jan 3` = `100 + 200 + 150 = 450`.

```
[ Row 1 ] ─┐
[ Row 2 ] ─┼──► Window for Row 3
[ Row 3 ] ─┘
```

---

## Part 2: Case Studies

---

### Case Study 1: Aggregates — Running balances per customer

**Scenario:**
The analytics team asks:

> "Finance wants running account balances for each customer, so they can reconcile statements."

**Underlying Need:**
They need a **running total per customer**, not just a running total.

**Exercise:**
Write a query that:

1. Partitions by `customer_id`.
2. Orders by `transaction_date`.
3. Calculates a running total of `amount` using `SUM() OVER(...)`.

---

### Case Study 2: Ranking — Salesperson Leaderboard

**Scenario:**
The analytics team asks:

> "We’d like to publish a leaderboard of salespeople by total revenue, so that managers can celebrate top performers."

**Underlying Need:**
Sorting alone will only show the order of salespeople. The business needs an actual rank number next to each salesperson, and it must handle ties correctly (two people with the same sales should have the same rank).

**Exercise:**
Write a query that:

1. Uses RANK() with a window function.
2. Orders by amount in descending order.
3. Assigns a rank to each salesperson based on their total sales.

