class Course:
    def __init__(self, name, trimester, credits):
        self.name = name
        self.trimester = trimester
        self.credits = credits

    def __repr__(self):
        return f"Course(name={self.name}, trimester={self.trimester}, credits={self.credits})"

