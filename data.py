from dataclasses import dataclass


@dataclass
class SetUpData:
    string_arg: str
    sweet: bool = False
    spicy: bool = False
    bitter: bool = False
    cheese: bool = False
    cuisineItalian: bool = False

    def __post_init__(self):
        true_args = [arg for arg in (self.sweet, self.spicy, self.bitter, self.cheese) if arg]
        if len(true_args) == 0:
            raise ValueError("At least one bool argument must be True.")
"""example of usage:
example = SetUpData('some string', sweet=True, spicy=True)
print(example)
output:
SetUpData(string_arg='some string', sweet=True, spicy=True, bitter=False, cheese=False)
"""