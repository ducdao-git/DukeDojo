import os

script_content = """\
from typing import Optional\n\n\n
# runtime O(?), space O(?)


# Question URL:
# Solution: ? -- runtime O(?), space O(?)
#
sol_test = Solution()
print(sol_test.FUNC_NAME())
"""


def create_py_file(problem_title):
    current_working_directory = os.getcwd()
    print(f"\nCWD: {current_working_directory}")

    name = problem_title
    name = name.lower().replace(" ", "_")
    print(f"File Name: {name}\n")

    file_name = os.path.join(current_working_directory, f"{name}.py")
    with open(file_name, "w") as file:
        file.write(script_content)


create_py_file("Rotting Fruit")
