# Lab 04 — `while` Loops, Typing, Identity, and Functions

**Course:** Programming in Python  
**Program:** Artificial Intelligence and Big Data Analytics, NSU  
**Week:** 2  
**Lecture:** 04 — Control Flow II  
**Syllabus section:** Section 4 — `for` and `while` loops, variables and typing, `id()`, `is`, basic functions

## Learning objectives

By the end of this lab, you should be able to:

- choose between `for` and `while` for simple problems;
- write `while` loops with clear stopping conditions;
- use `break`, `continue`, and loop `else`;
- use small nested loops;
- explain dynamic typing at a beginner level;
- understand that variable names refer to objects;
- distinguish value equality (`==`) from identity (`is`);
- use `id()` to inspect object identity;
- understand aliasing with mutable lists;
- define and call basic functions;
- pass arguments to function parameters;
- return values from functions;
- distinguish `print()` from `return`;
- work with local variables;
- return multiple values;
- combine validation, loops, conditions, and functions.

## Scope

This lab follows Lecture 04 only.

You **do not need**:

- default parameters;
- keyword arguments;
- `*args` or `**kwargs`;
- recursion;
- lambda functions;
- the `math` library;
- list methods beyond the basic methods already seen;
- classes;
- file handling;
- exception handling.

Those topics are covered later.

## Structure

```text
NSU_Python_Lab_04_Loops_Typing_Functions/
├── README.md
├── tasks.py
├── examples/
│   ├── 01_while_basics.py
│   ├── 02_break_continue_loop_else.py
│   ├── 03_nested_loops.py
│   ├── 04_dynamic_typing.py
│   ├── 05_identity_and_references.py
│   ├── 06_basic_functions.py
│   ├── 07_return_and_none.py
│   └── 08_multiple_values_and_local_scope.py
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
    ├── task_13.py
    ├── task_14_bonus.py
    └── task_15_bonus.py
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

Run an example separately:

```bash
python examples/05_identity_and_references.py
```

## Recommended workflow

1. Read one task.
2. Decide whether repetition is controlled by a known sequence or by a condition.
3. For every `while` loop, identify what changes so the loop can stop.
4. For identity tasks, predict the result before running the program.
5. For function tasks, identify the inputs, processing, and returned result.
6. Test normal values and boundary cases.
7. Check the provided solution only after attempting the task.

## Difficulty

- Tasks 1–4: `while`, `break`, `continue`, loop `else`
- Tasks 5–7: nested loops, typing, references, identity
- Tasks 8–13: functions and integration
- Tasks 14–15: optional bonus tasks

## Important reminders

### `==` and `is`

Use `==` to compare values:

```python
a = [1, 2]
b = [1, 2]

print(a == b)  # True
```

Use `is` to check whether two names refer to the same object:

```python
print(a is b)  # False
```

A common and correct use is:

```python
if result is None:
    print("No result")
```

### `print()` is not `return`

```python
def square(number):
    return number ** 2

result = square(5)
print(result)
```

`return` sends a value back to the caller so later code can reuse it.
