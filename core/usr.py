import random as rd


class Usr:
    def __init__(self, params: list[list] | None=None):
        self.params: list[list] = params or []
        if self.params == []:
            self.params = [
                [
                    "Peter", "Blake", "Jimmy",
                    "Nolan", "Karl", "Ella",
                    "Sophie", "Karen", "Stephany",
                    "Grace"
                ],
                [
                    "Bot", "Whatever", "Powerful",
                    "Stoopid", "Interesting", "Hot",
                    "PK", "Coder", "Gamer",
                    "Xtreme"
                ]
            ]

    def generate(self) -> str:
        result: str = ""
        for options in self.params:
            result = "".join([result, rd.choice(options)])

        return result