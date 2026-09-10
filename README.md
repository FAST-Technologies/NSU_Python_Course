# NSU Python Course

Course materials for "Programming in Python" at Novosibirsk State University (NSU). This repository contains lectures, labs, examples, and supporting resources for first-year Master's students in Artificial Intelligence and Big Data Analytics.

## Table of Contents

- [NSU Python Course](#nsu-python-course)
  - [Table of Contents](#table-of-contents)
  - [Course Topics](#course-topics)
  - [Repository Structure](#repository-structure)
  - [Requirements](#requirements)
  - [Course Repository](#course-repository)
  - [Typical Workflow](#typical-workflow)

## Course Topics

- Python basics and PEP 8
- Variables and basic data types
- Arithmetic and logical operations
- Input and output
- Conditions and loops
- Functions and recursion
- Lists, sorting, filtering, and `map()`
- Strings and regular expressions
- File handling
- Exceptions
- Object-oriented programming
- Decorators
- Iterators and generators
- NumPy
- Pandas

## Repository Structure

Top-level layout:

```
NSU-Python-Course/
├── Lectures/
├── Labs/
│   ├── Lab_01_Python_Basics/
│   ├── Lab_02_...
│   └── ...
├── requirements.txt
├── .gitignore
└── README.md
```

## Requirements

- Python 3.10 or newer
- A code editor (VS Code or PyCharm recommended)
- Git and a GitHub account

Verify Python in a terminal:

```
python --version
```

## Course Repository

Clone or visit the repository on GitHub:

https://github.com/RiyadhDerbale/NSU-Python-Course

## Typical Workflow

Keep materials up to date and submit your work using Git:

```
# Get the latest changes
git pull

# After completing work
git status
git add .
git commit -m "Complete Lab 01"
git push
```

## Submission & Updates

- Create your own GitHub repository for submitting work — do not push solutions to the instructor repo.
- Keep two local folders (simple option):
  - `instructor` — a local copy of this repository (clone or download) you use to get tasks and updates.
  - `solutions` — your personal repository where you prepare and push your finished work.
- Copy needed files from the `instructor` folder into your `solutions` folder, then commit and push your `solutions` repo.
- Add `RiyadhDerbale` as a collaborator on your `solutions` repo so the instructor can review your submissions.

Example commands (minimal):

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
