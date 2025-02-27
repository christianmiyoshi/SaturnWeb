class Person:
    def __init__(self, first_name: str, middle_name:str, last_name:str):
        self.uuid = 1
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name

    def full_name(self):
        return " ".join(
            name for name in [
                self.first_name,
                self.middle_name,
                self.last_name
            ] if name
        )