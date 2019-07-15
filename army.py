from battalion_types import BattalionType
from typing import List
from collections import defaultdict


class Army:
    """Army holds all the battalions along with their strength.
    Army can update, add new battalions and their strength
    """
    def __init__(self, **battalions):
        self.battalion_strength = defaultdict(int)
        for k, v in battalions.items():
            if BattalionType.is_valid_battalion(k) and isinstance(v, int):
                self.battalion_strength[BattalionType(k)] = v

    def get_battalion_strength(self, battalion_type: BattalionType) -> int:
        """Returns the strength of the battalion in this army
        Arguments:
            battalion_type {BattalionType} -- [type of battalion whose 
            strength needs to be found]
        
        Raises:
            KeyError: [Raises when battalion_type is not present in the army]
        
        Returns:
            [int] -- [strength of battalion_type]
        """
        if battalion_type not in self.battalion_strength:
            raise KeyError("{0} not found".format(battalion_type))
        return self.battalion_strength.get(battalion_type)

    def update_battalion_strength(self, battalion_type: BattalionType,
                                  change: int):
        """adds a new battalion_type battalion if not present else 
        updates the strength of the battalion
        
        Arguments:
            battalion_type {BattalionType} -- [Type of battalion to be added or updated]
            change {int} -- [represents change in the strength of the battalion]
        """
        self.battalion_strength[battalion_type] += change

    def get_battalions(self) -> List[BattalionType]:
        return list(self.battalion_strength.keys())
    
    def has_battalion(self, battalion_type: BattalionType) -> bool:
        return battalion_type in self.battalion_strength
    
    def get_all_battalion_with_strength(self):
        return self.battalion_strength

    def __eq__(self, other): 
        if not isinstance(other, Army):
            return False
        return self.battalion_strength == other.battalion_strength
