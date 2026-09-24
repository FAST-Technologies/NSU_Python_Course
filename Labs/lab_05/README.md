# NSU Python — Lab 05

## Functions in Practice: Arguments, Recursion, `math`, and List Methods

This lab corresponds to **Lecture 05 / Section 5**.

### Topics

- Positional arguments
- Keyword arguments
- Default arguments
- Early `return`
- `*args`
- `**kwargs`
- Local and global scope
- Recursive functions
- Base cases and recursive cases
- `math`
- List methods:
  - `append()`
  - `extend()`
  - `insert()`
  - `remove()`
  - `pop()`
  - `index()`
  - `count()`

## Files

```text
Lab_05/
├── tasks.py
├── README.md
├── examples/
│   ├── 01_arguments.py
│   ├── 02_flexible_arguments.py
│   ├── 03_scope.py
│   ├── 04_recursion.py
│   ├── 05_math_module.py
│   └── 06_list_methods.py
└── solutions/
    └── tasks_solution.py
```

## Tasks

Complete **Tasks 1–12** in `tasks.py`.

Tasks **13–14** are optional bonus tasks for students who finish early.

## Important rules

For this lab:

- Recursive tasks must actually use recursion.
- Do not replace recursive tasks with loops.
- Do not use `lambda`, `sorted()`, `filter()`, or `map()` yet.
- Use only concepts from Lecture 05 and earlier lectures.
- Write readable code and use clear variable and function names.

## Running the lab

From the lab directory:

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

1. Read the task carefully.
2. Write the required function.
3. Test it with the examples from the task.
4. Add one or two additional tests.
5. If the task uses recursion, identify the **base case** before writing the recursive case.
6. Compare your result with the expected behavior.

## Examples

The `examples/` directory contains short demonstrations of the main ideas from Lecture 05. Run them individually if you need a reminder.

Example:

```bash
python examples/04_recursion.py
```

## Submission

Submit your completed `tasks.py`.
