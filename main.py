import pathlib
import sys
from dataclasses import dataclass, field
import random


@dataclass
class Group:
    """Candidates that need to be paired"""
    g1: list[str]
    g2: list[str]
    unpaired: list = field(default_factory=list)

    def pair(self) -> dict:
        """Randomly pair those from g1 to g2. Place any unpaired people in self.unpaired"""
        if not (self.g1 or self.g2):
            raise ValueError(f"""groups not initialised""")

        random.shuffle(self.g1)  # g1 arbitrary

        n_pairings = min(len(self.g1), len(self.g2))
        self.unpaired = self.g1[n_pairings:] + self.g2[n_pairings:]

        return {k: v for k, v in zip(self.g1, self.g2)}

    def __str__(self):
        out = ""
        for p1, p2 in zip(self.g1, self.g2):
            out += f"* {p1}{'<->':^9}{p2}\n"

        out += f"**Unpaired**: {', '.join(self.unpaired)}\n" if self.unpaired else '\n'

        return out


def parse_file(filepath: str | pathlib.Path) -> list[Group]:
    """Builds Groups - doesn't pair


    File format (.md):

    person1
    person2

    person3
    person4
    ---
    p5

    p6

    person1 eligible to be paired with person3 or person4
    p5 eligible to be paired with p6
    """

    with open(filepath, 'r') as f:
        file = f.read()

    # split into groupings
    file = file.split('---')
    # split groupings into g1 and g2 - currently strings w terms seperated by \n
    groupings = [[g.split() for g in f.split('\n\n')] for f in file]

    return [Group(*g) for g in groupings]


def main():
    RESULTS_FILE = "./results.md"

    filepath = pathlib.Path(sys.argv[1])
    if not filepath.is_file():
        raise FileNotFoundError(f"Can't find file {filepath}")

    print('# Pub Crawl Pairings\n\n\n')

    with open(RESULTS_FILE, 'w') as f:
        f.write('# Pub Crawl Pairings\n---\n\n')

    groups = parse_file(filepath)
    for i, group in enumerate(groups):
        group.pair()

        with open("%s" % RESULTS_FILE, 'a') as f:
            f.write(f"## Group {i + 1}\n\n")
            f.write(str(group))

        print(group)


if __name__ == '__main__':
    main()
