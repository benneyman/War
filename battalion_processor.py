from battalion_types import BattalionType
from typing import Dict, List, Tuple


class BattalionProcessor:
    """[summary]
    Class to hold the battalion seniority and substituion battalions
    """

    def __init__(self, multiplier: int = 2, **battalions):
        self.multiplier = multiplier
        self.battalion_seniority: Dict[BattalionType, int] = {}
        self.substitution_graph: Dict[BattalionType, List[Tuple[BattalionType, float]]] = {}
        for k, v in battalions.items():
            if BattalionType.is_valid_battalion(k) and isinstance(v, int):
                self.battalion_seniority[BattalionType(k)] = v    

    def get_battalion_seniority(self, battalion_type: BattalionType) -> int:
        return self.battalion_seniority.get(battalion_type, 100)

    def add_battalion_substituation(self, from_battalion_type: BattalionType,
                                    to_battalion_type: BattalionType,
                                    multiplier: int,
                                    bidirectional: bool = True) -> None:
        """[summary]
        
        Arguments:
            from_battalion_type {BattalionType} -- [from battalion_type]
            to_battalion_type {BattalionType} -- [to battalion_type]
            multiplier {int} -- [amount of from_battalion_type required to 
            make 1 to_battalion_type]
            bidirectional {bool} -- [indicates weather the relationship 
            is bidirectional] (default: {True})
        """
        from_sub_btn = self.substitution_graph.get(from_battalion_type, [])
        from_sub_btn.append((to_battalion_type, multiplier))
        self.substitution_graph[from_battalion_type] = from_sub_btn
        if(bidirectional):
            to_sub_btn = self.substitution_graph.get(to_battalion_type, [])
            to_sub_btn.append((from_battalion_type, 1/multiplier))
            self.substitution_graph[to_battalion_type] = to_sub_btn

    def get_substitution_battalion(self, battalion_type: BattalionType) -> List[Tuple[BattalionType, float]]:
        """[summary]
        Returns the list of Tuple of BattalionType and multipler indicating
        how much of that battalion is need to make 1 of the input battalion_type
        Arguments:
            battalion_type {BattalionType} -- [Input battalion whose 
            substitution order needs to be found]
        
        Returns:
            List[Tuple[BattalionType, float]] -- [substitution order of the 
            input battalion]
        """
        unordered_sub_btn = self.substitution_graph.get(battalion_type, [])
        return sorted(unordered_sub_btn,
                      key=lambda btn: self.get_battalion_seniority(btn))
