#!/usr/bin/python3

# EPL Teams List
EPL_TEAMS = ["manchester united", "manchester city", "chelsea", "arsenal", "tottenham"]
print("Initial Teams:", EPL_TEAMS)

# Append a new team
EPL_TEAMS.append("wolves")
print("After Appending:", EPL_TEAMS)


# Base Class
class Animals:
    def __init__(self):
        self.breathing_system = "All animals have a respiratory system that uses oxygen."
        self.digestion_system = "All animals digest food to get energy for survival."
        self.locomotive_system = "All animals have a way of moving from one place to another."

    def breathing(self):
        print(self.breathing_system)

    def digestion(self):
        print(self.digestion_system)

    def locomotion(self):
        print(self.locomotive_system)


# Subclass
class Mammals(Animals):
    def __init__(self):
        super().__init__()
        self.feature = "Mammals give birth to live young and feed them with milk."

    def describe(self):
        print(self.feature)


# Running Example
if __name__ == "__main__":
    print("\n--- Animal Class Demo ---")
    animal = Animals()
    animal.breathing()
    animal.digestion()
    animal.locomotion()

    print("\n--- Mammal Class Demo ---")
    mammal = Mammals()
    mammal.breathing()
    mammal.describe()
