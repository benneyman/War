from battalion_types import BattalionType
from typing import Dict, List


class BattalionProcessor:

    def __init__(self, multiplier: int = 2, horses: int = 1,
                 elephants: int = 2, armoured_tanks: int = 3,
                 sling_guns: int = 4):
        self.multiplier = multiplier
        self.battalion_seniority: Dict[BattalionType, int] = {
            BattalionType.HORSES: horses,
            BattalionType.ELEPHANTS: elephants,
            BattalionType.ARMOUREDTANKS: armoured_tanks,
            BattalionType.SLINGGUNS: sling_guns
        }
        self.substitution_graph: Dict[BattalionType, List[BattalionType]] = {}

    def get_battalion_seniority(self, battalion_type: BattalionType) -> int:
        return self.battalion_seniority.get(battalion_type)

    def add_battalion_substituation(self, from_battalion_type: BattalionType,
                                    to_battalion_type: BattalionType,
                                    bidirectional: bool = True):
        from_sub_btn = self.substitution_graph.get(from_battalion_type, [])
        from_sub_btn.append(to_battalion_type)
        self.substitution_graph[from_battalion_type] = from_sub_btn
        if(bidirectional):
            to_sub_btn = self.substitution_graph.get(to_battalion_type, [])
            to_sub_btn.append(from_battalion_type)
            self.substitution_graph[to_battalion_type] = to_sub_btn

    def get_substitution_battalion(self, battalion_type: BattalionType) -> List[BattalionType]:
        unordered_sub_btn = self.substitution_graph.get(battalion_type, [])
        return sorted(unordered_sub_btn,
                      key=lambda btn: self.get_battalion_seniority(btn))
