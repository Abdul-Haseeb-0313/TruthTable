# Truth Table Printer

A Python library to generate truth tables for logical expressions.

**Features:**

* Supports logical operators: NOT (`~`), AND (`.`), OR (`+`), IMPLICATION (`-`), BICONDITIONAL (`=`)
* Converts infix expressions to postfix internally for evaluation using the **Shunting Yard Algorithm**
* Easy to print complete truth tables for any expression

**Installation:**

* Clone the repo and use the library directly.

**Example:**

```python
from TruthTable import printTable

printTable("a-b")
```

**Output:**

```
___________
|a| b| a-b|
-----------
|T| T| T  |
|T| F| F  |
|F| T| T  |
|F| F| T  |
-----------
```

**Contributing:**
Contributions and feature extensions are encouraged! Submit issues or pull requests to improve the library.


---

