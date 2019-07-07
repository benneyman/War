from battalion_types import BattalionType
from typing import Dict, List


class Army:

    def __init__(self, **battalions):
        self.battalion_strength: Dict[BattalionType, int] = {}
        for k, v in battalions.items():
            if BattalionType.is_valid_battalion(k) and isinstance(v, int):
                self.battalion_strength[BattalionType(k)] = v

    def get_battalion_strength(self, battalion_type: BattalionType):
        if battalion_type not in self.battalion_strength:
            raise KeyError("{0} not found".format(battalion_type))
        return self.battalion_strength.get(battalion_type)

    def update_battalion_strength(self, battalion_type: BattalionType,
                                  change: int):
        if battalion_type not in self.battalion_strength:
            self.battalion_strength[battalion_type] = change
        else:
            self.battalion_strength[battalion_type] += change

    def get_battalions(self) -> List[BattalionType]:
        return list(self.battalion_strength.keys())
    
    def has_battalion(self, battalion_type: BattalionType) -> bool:
        return battalion_type in self.battalion_strength
