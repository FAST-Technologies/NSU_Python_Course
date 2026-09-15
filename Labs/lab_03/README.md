# Lab 03 — Conditions and `for` Loops

**Course:** Programming in Python  
**Program:** Artificial Intelligence and Big Data Analytics, NSU  
**Week:** 2  
**Lecture:** 03 — Control Flow I  
**Syllabus section:** Section 3 — PEP 8, conditional statements, `for` loop

## Learning objectives

By the end of this lab, you should be able to:

- build Boolean expressions with comparison and logical operators;
- write `if`, `if-else`, and `if-elif-else` statements;
- use correct Python indentation;
- use `for` loops with `range()`, strings, lists, tuples, sets, and dictionaries;
- use counters and accumulators inside loops;
- use `break` to stop a loop;
- use `continue` to skip an iteration;
- apply basic input validation with conditions;
- write readable code following basic PEP 8 conventions.

## Scope

Use the material from Lecture 03 only.

You **do not need** `while` loops, user-defined functions, recursion, classes,
file handling, or exception handling. Those topics are covered later.

## Structure

```text
NSU_Python_Lab_03_Conditions_For_Loops/
├── README.md
├── tasks.py
├── examples/
│   ├── 01_boolean_conditions.py
│   ├── 02_if_elif_validation.py
│   ├── 03_for_and_range.py
│   ├── 04_iterables_and_accumulators.py
│   ├── 05_break_continue.py
│   └── 06_truthiness_conditional_expression.py
└── solutions/
    ├── task_01.py
    ├── task_02.py
    ├── task_03.py
    ├── task_04.py
    ├── task_05.py
    ├── task_06.py
    ├── task_07.py
    ├── task_08.py
    ├── task_09.py
    ├── task_10.py
    ├── task_11.py
    ├── task_12.py
    ├── task_13_bonus.py
    └── task_14_bonus.py
```

## Running the lab

Windows:

```bash
python tasks.py
```

or:

```bash
py tasks.py
```

macOS / Linux:

```bash
python3 tasks.py
```

You can run examples separately, for example:

```bash
python examples/03_for_and_range.py
```

## Recommended workflow

1. Read the task.
2. Decide what condition or loop you need.
3. Write the code.
4. Test normal values.
5. Test boundary values.
6. Check indentation and variable names.
7. Compare with the solution only after attempting the task.

## Difficulty

- Tasks 1–4: conditions
- Tasks 5–8: `for` loops and accumulators
- Tasks 9–12: combined control flow
- Tasks 13–14: optional bonus tasks for students who finish early

## PEP 8 reminder

Prefer:

```python
if age >= 18 and score >= 60:
    print("Accepted")
```

Avoid:

```python
if age>=18 and score>=60:
    print("Accepted")
```

Use four spaces for indentation and meaningful variable names.
