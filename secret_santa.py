from random import shuffle

class person:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.gift = None


def choose_pairs(people):
    shuffle(people)
    pairs = []
    for i, person in enumerate(people[:-1]):
        person.gift = people[i+1]

    people[len(people) - 1].gift = people[0]


def main():
    people = ['sam', 'bone', 'alex', 'bingo']
    print choose_pairs(people)

if __name__ == "__main__":
    main()