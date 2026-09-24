"""Local and global names."""

COURSE = "Python"


def show_course():
    """Something."""
    level = "Master's"
    print(COURSE)
    print(level)


show_course()

# COURSE is global, so it is available here.
print(COURSE)

# level is local to show_course().
# Uncommenting the next line would cause NameError.
# print(level)
