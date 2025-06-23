# Create a class called Employee that has attribute name, dob, age, salary, skill_sets. Create class Developer inheriting Employee that has additional attributes github_profile, is_fullstack. Developer should have method display_profile thaf displays {name} has skills: s1, s2. Git profile: {profile} .Create class HR inheriting Employee that has attributes is_manager, onboard_rate. It should also have method display_profile that displays {name} has skills: s1, s2. Onboard rate: {rate}. 5 developers and 2 HR joined the company. Initialize the object for them. Also display the employee's name who have both Python and Git skill.


class Employee:
    def __init__(self, name, dob, age, salary, skill_sets):
        self.name = name
        self.dob = dob
        self.age = age
        self.salary = salary
        self.skill_sets = skill_sets

    def display_profile(self):
        raise NotImplementedError("Subclasses must implement display_profile")


class Developer(Employee):
    def __init__(
        self, name, dob, age, salary, skill_sets, github_profile, is_fullstack
    ):
        super().__init__(name, dob, age, salary, skill_sets)
        self.github_profile = github_profile
        self.is_fullstack = is_fullstack

    def display_profile(self):
        skills = ", ".join(self.skill_sets)
        fullstack_status = " (Fullstack)" if self.is_fullstack else ""
        print(
            f"{self.name}{fullstack_status} has skills: {skills}. Git profile: {self.github_profile}"
        )


class HR(Employee):
    def __init__(self, name, dob, age, salary, skill_sets, is_manager, onboard_rate):
        super().__init__(name, dob, age, salary, skill_sets)
        self.is_manager = is_manager
        self.onboard_rate = onboard_rate

    def display_profile(self):
        skills = ", ".join(self.skill_sets)
        manager_status = " (Manager)" if self.is_manager else ""
        print(
            f"{self.name}{manager_status} has skills: {skills}. Onboard rate: {self.onboard_rate}%"
        )


employees = [
    Developer(
        "John Doe",
        "1990-05-15",
        33,
        85000,
        ["Python", "Git", "Django"],
        "github.com/johndoe",
        True,
    ),
    Developer(
        "Jane Smith",
        "1988-11-22",
        35,
        92000,
        ["JavaScript", "React", "Node.js"],
        "github.com/janesmith",
        True,
    ),
    Developer(
        "Mike Johnson",
        "1995-03-10",
        28,
        78000,
        ["Python", "Git", "Flask", "AWS"],
        "github.com/mikej",
        False,
    ),
    Developer(
        "Sarah Williams",
        "1992-07-30",
        31,
        88000,
        ["Java", "Spring", "SQL"],
        "github.com/sarahw",
        False,
    ),
    Developer(
        "Alex Chen",
        "1985-09-18",
        38,
        95000,
        ["Python", "Git", "Docker", "Kubernetes"],
        "github.com/alexc",
        True,
    ),
    HR(
        "Emily Davis",
        "1980-12-05",
        43,
        75000,
        ["Recruitment", "Communication", "HR Software"],
        True,
        85,
    ),
    HR(
        "David Wilson",
        "1991-04-25",
        32,
        68000,
        ["Interviewing", "Employee Relations"],
        False,
        72,
    ),
]

print("=== Employee Profiles ===")
for emp in employees:
    emp.display_profile()

print("\n=== Employees with Python and Git skills ===")
python_git_employees = [
    emp.name
    for emp in employees
    if isinstance(emp, Developer)
    and "Python" in emp.skill_sets
    and "Git" in emp.skill_sets
]

for name in python_git_employees:
    print(name)
