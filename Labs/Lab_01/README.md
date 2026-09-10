# Lab 01 — Python Basics

## Summary

This lab introduces the Python development workflow and core language basics. Follow the environment setup below before attempting the exercises in `tasks.py`.

## Objectives

By the end of this lab you will be able to:

- Set up a local Python development environment
- Run Python from the terminal and execute scripts
- Create and activate a virtual environment
- Use VS Code for Python development
- Use Git for the basic course workflow
- Work with variables and primitive data types
- Use `input()` and `print()`
- Convert values with `int()`, `float()`, and `str()`
- Apply arithmetic operators and simple expressions
- Follow basic PEP 8 conventions

---

## 0 — Environment setup (complete before starting)

1. Install Python (3.10+)

Download: https://www.python.org/downloads/

Verify installation:

Windows:

```
py --version
```

or

```
python --version
```

macOS / Linux:

```
python3 --version
```

Ubuntu / Debian (if needed):

```
sudo apt update
sudo apt install python3 python3-venv python3-pip
```

2. Install VS Code

Download: https://code.visualstudio.com/download

Install the official Python extension: https://marketplace.visualstudio.com/items?itemName=ms-python.python

Open the project in VS Code:

```
code .
```

3. Install and configure Git

Download: https://git-scm.com/downloads

Verify:

```
git --version
```

Configure (once):

```
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

4. Clone the course repository (if needed)

```
git clone https://github.com/RiyadhDerbale/NSU-Python-Course
cd NSU-Python-Course
```

Or update an existing clone:

```
git pull
```

5. Create a virtual environment

Create a `.venv` directory in the project root:

Windows:

```
py -m venv .venv
```

macOS / Linux:

```
python3 -m venv .venv
```

6. Activate the virtual environment

PowerShell:

```
.\.venv\Scripts\Activate.ps1
```

Command Prompt:

```
.venv\Scripts\activate.bat
```

macOS / Linux:

```
source .venv/bin/activate
```

You should see the environment name in your prompt, for example `(.venv)`.

Deactivate when finished:

```
deactivate
```

7. Run Python interactively

Start the REPL:

```
python   # or: py  (Windows)
python3  # (macOS / Linux)
```

Try:

```
print("Hello, Python!")
```

8. Run the example script

Open the examples folder and run `hello.py`:

```
cd Labs/Lab_01/examples
python hello.py
```

---

## Environment checkpoint

Before continuing, make sure:

- Python 3.10+ is installed
- VS Code and the Python extension are installed
- Git is installed and configured
- The course repository is cloned or up to date
- `.venv` was created and activated
- `hello.py` runs successfully

---

## Next

Work through `tasks.py` in this folder. Use `examples/` for reference implementation snippets.

## Submission & Updates

- Create your own GitHub repository for submitting work — do not push your solutions to the instructor repo.
- Keep it simple with two local folders:
  - `instructor` — a local copy of this repository (clone or download) used only to get tasks and updates.
  - `solutions` — your personal repository where you prepare, commit, and push your work.
- Copy the files you need from the `instructor` folder into your `solutions` folder, then commit and push the `solutions` repo.
- Add `RiyadhDerbale` as a collaborator on your `solutions` repo so the instructor can review your submissions.

Minimal example (update instructor copy, then push solutions):

```
# update the instructor folder (if you cloned it)
cd instructor
git pull origin main

# copy files into your solutions folder (use file explorer or OS copy command)
cd ../solutions
git add .
git commit -m "Submit Lab 01"
git push origin main
```
