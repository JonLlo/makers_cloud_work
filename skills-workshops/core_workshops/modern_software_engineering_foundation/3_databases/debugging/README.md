# Debugging Database Backed Apps

## Setup


### 1. Set up the virtual environment
```
; python -m venv databases-starter-venv
```

### 2. Activate the virtual environment
```
; source databases-starter-venv/bin/activate 
```


### 3. Install dependencies
```
(databases-starter-venv); pip install -r requirements.txt
```

> Read below if you see an error with `python_full_version`

### 4. Create the database
```
(databases-starter-venv); createdb db_debugging_workshop
```

### 5. Run the tests - see below if you have any issues
```
(databases-starter-venv); pytest
```
> If the tests fail, see below

### 6. Run the app
```
(databases-starter-venv); python app.py
```

<br>
<details>
  <summary>I get a <code>ModuleNotFoundError: No module named 'psycopg'</code></summary>
  <br>
If, after activating your <code>venv</code> and installing dependencies, you see this error when running <code>pytest</code>, please deactivate and reactivate your <code>venv</code>. This should solve the problem - if not, contact your coach.
</details>
