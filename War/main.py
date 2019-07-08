from army import Army
from battalion_processor import BattalionProcessor
from battalion_types import BattalionType
from battle_planner import BattlePlanner
from copy import deepcopy


def main():
    battalion_processor = BattalionProcessor(2,horses=1, elephants=2,
                                             armoured_tanks=3,
                                             sling_guns=4)
    battalion_processor.add_battalion_substituation(BattalionType.ELEPHANTS,
                                                    BattalionType.HORSES, 2)
    battalion_processor.add_battalion_substituation(BattalionType.ARMOUREDTANKS,
                                                    BattalionType.ELEPHANTS, 2)
    battalion_processor.add_battalion_substitu0ation(BattalionType.SLINGGUNS,
                                                    BattalionType.ARMOUREDTANKS, 2)                                          
    lengaburu_army = Army(horses=100, elephants=50,
                          armoured_tanks=10, sling_guns=5)

    

    with open("D:\\GeekTrust\\War\\War\\input.txt", "r") as testcases:
        for testcase in testcases:
            input = [x.strip() for x in testcase.split(",")]
            print(input)
            enemy_army = Army(horses=input[0], elephants=input[1],
                              armoured_tanks=input[2], sling_guns=input[3])
            print(enemy_army)
            planner = BattlePlanner(battalion_processor, deepcopy(lengaburu_army))
            result, army = planner.get_winning_army(enemy_army)
            print(result, army)
    

if __name__ == "__main__":
    main()
