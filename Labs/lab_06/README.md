# NSU Python — Lab 06

## Functions as Values: `lambda`, Sorting, Filtering, and `map`

This lab corresponds to **Lecture 06 / Section 6**.

### Topics

- Functions as objects
- Assigning functions to variables
- Passing functions as arguments
- Higher-order functions
- `lambda`
- `sorted()`
- `list.sort()`
- `key`
- `reverse`
- Sorting strings, tuples, and dictionaries
- `filter()`
- `map()`
- Converting iterators with `list()`
- Combining filtering, sorting, and transformation

## Files

```text
Lab_06/
├── tasks.py
├── README.md
├── examples/
│   ├── 01_functions_as_values.py
│   ├── 02_lambda.py
│   ├── 03_sorting.py
│   ├── 04_sorting_with_key.py
│   ├── 05_filter.py
│   ├── 06_map.py
│   └── 07_pipeline.py
└── solutions/
    └── tasks_solution.py
```

## Tasks

Complete **Tasks 1–12** in `tasks.py`.

Tasks **13–14** are optional bonus tasks for students who finish early.

## Important ideas

### Function object vs function call

```python
operation = square
```

stores the function itself.

```python
value = square(5)
```

calls the function and stores its returned value.

### `sorted()` vs `list.sort()`

```python
ordered = sorted(numbers)
```

creates a **new list**.

```python
numbers.sort()
```

changes the **existing list** and returns `None`.

### `filter()`

`filter()` selects values.

```python
passed = filter(lambda score: score >= 60, scores)
```

### `map()`

`map()` transforms values.

```python
doubled = map(lambda number: number * 2, numbers)
```

Both `filter()` and `map()` return iterators, so use `list()` when you need a stored list.

## Running the lab

From the Lab 06 directory:

### Windows

```bash
python tasks.py
```

or:

```bash
py tasks.py
```

### macOS / Linux

```bash
python3 tasks.py
```

## Suggested workflow

1. Complete the tasks in order.
2. Run the file after every task.
3. Test with additional values.
4. Pay attention to whether an operation changes the original list.
5. Keep lambda expressions short and readable.
6. Use `def` when the logic becomes too complicated for a lambda.

## Submission

Submit your completed `tasks.py`.
