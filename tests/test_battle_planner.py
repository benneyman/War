from battalion_processor import BattalionProcessor
from battalion_types import BattalionType
from battle_planner import BattlePlanner
from army import Army
from copy import deepcopy


class Test_BattlePlanner(object):
    def test_apply_power_rule(self):
        bp = BattlePlanner(BattalionProcessor(), Army())
        assert bp.apply_power_rule(7) == 4
        assert bp.apply_power_rule(5) == 3

    def test_resolve_with_similar_battalion(self):
        horses, elephants, armoured_tanks, sling_guns = 100, 50, 10, 5
        army = Army(horses=horses, elephants=elephants,
                    armoured_tanks=armoured_tanks, sling_guns=sling_guns)
        horses, elephants, armoured_tanks, sling_guns = 1, 2, 3, 4
        bp = BattalionProcessor(horses=horses, elephants=elephants,
                                armoured_tanks=armoured_tanks,
                                sling_guns=sling_guns)
        planner = BattlePlanner(bp, army)
        assert planner.resolve_with_similar_battalion(BattalionType.HORSES, 50) == 0
        assert planner.resolve_with_similar_battalion(BattalionType.ELEPHANTS, 80) == 30
        assert planner.resolve_with_similar_battalion(BattalionType.ARMOUREDTANKS, 20) == 10
     
    def test_resolve_battalion_1(self):
        horses, elephants, armoured_tanks, sling_guns = 100, 50, 10, 5
        our_army = Army(horses=horses, elephants=elephants,
                    armoured_tanks=armoured_tanks, sling_guns=sling_guns)
        horses, elephants, armoured_tanks, sling_guns = 1, 2, 3, 4
        bp = BattalionProcessor(1, horses=horses, elephants=elephants,
                                armoured_tanks=armoured_tanks,
                                sling_guns=sling_guns)
        bp.add_battalion_substituation(BattalionType.ELEPHANTS, BattalionType.HORSES, 2)                                
        assert BattlePlanner(bp, deepcopy(our_army)).resolve_battalion(BattalionType.HORSES, 199) == True
        assert BattlePlanner(bp, deepcopy(our_army)).resolve_battalion(BattalionType.HORSES, 200) == True
        assert BattlePlanner(bp, deepcopy(our_army)).resolve_battalion(BattalionType.HORSES, 201) == False
        assert BattlePlanner(bp, deepcopy(our_army)).resolve_battalion(BattalionType.HORSES, 150) == True
        assert BattlePlanner(bp, deepcopy(our_army)).resolve_battalion(BattalionType.HORSES, 100) == True
        assert BattlePlanner(bp, deepcopy(our_army)).resolve_battalion(BattalionType.HORSES, 5) == True
        assert BattlePlanner(bp, deepcopy(our_army)).resolve_battalion(BattalionType.HORSES, 250) == False
    
    def test_resolve_battalion_2(self):
        horses, elephants, armoured_tanks, sling_guns = 100, 50, 10, 5
        our_army = Army(horses=horses, elephants=elephants,
                    armoured_tanks=armoured_tanks, sling_guns=sling_guns)
        horses, elephants, armoured_tanks, sling_guns = 1, 2, 3, 4
        bp = BattalionProcessor(2, horses=horses, elephants=elephants,
                                armoured_tanks=armoured_tanks,
                                sling_guns=sling_guns)
        bp.add_battalion_substituation(BattalionType.ELEPHANTS, BattalionType.HORSES, 2)                                
        bp.add_battalion_substituation(BattalionType.ARMOUREDTANKS, BattalionType.HORSES, 4)
        assert BattlePlanner(bp, deepcopy(our_army)).resolve_battalion(BattalionType.HORSES, 300) == True
        assert BattlePlanner(bp, deepcopy(our_army)).resolve_battalion(BattalionType.HORSES, 479) == True
        assert BattlePlanner(bp, deepcopy(our_army)).resolve_battalion(BattalionType.HORSES, 480) == True
        assert BattlePlanner(bp, deepcopy(our_army)).resolve_battalion(BattalionType.HORSES, 481) == False
        assert BattlePlanner(bp, deepcopy(our_army)).resolve_battalion(BattalionType.HORSES, 485) == False
    
    def test_resolve_battalion_3(self):
        horses, elephants, armoured_tanks, sling_guns = 100, 50, 10, 5
        our_army = Army(horses=horses, elephants=elephants,
                    armoured_tanks=armoured_tanks, sling_guns=sling_guns)
        horses, elephants, armoured_tanks, sling_guns = 1, 2, 3, 4
        bp = BattalionProcessor(3, horses=horses, elephants=elephants,
                                armoured_tanks=armoured_tanks,
                                sling_guns=sling_guns)
        bp.add_battalion_substituation(BattalionType.ELEPHANTS, BattalionType.HORSES, 2)                                
        bp.add_battalion_substituation(BattalionType.ARMOUREDTANKS, BattalionType.HORSES, 4)
        assert BattlePlanner(bp, deepcopy(our_army)).resolve_battalion(BattalionType.ARMOUREDTANKS, 30) == True
        assert BattlePlanner(bp, deepcopy(our_army)).resolve_battalion(BattalionType.ARMOUREDTANKS, 104) == True
        assert BattlePlanner(bp, deepcopy(our_army)).resolve_battalion(BattalionType.ARMOUREDTANKS, 105) == True
        assert BattlePlanner(bp, deepcopy(our_army)).resolve_battalion(BattalionType.ARMOUREDTANKS, 106) == False

    def test_resolve_battalion_4(self):
        horses, elephants, armoured_tanks, sling_guns = 100, 50, 10, 5
        our_army = Army(horses=horses, elephants=elephants,
                    armoured_tanks=armoured_tanks, sling_guns=sling_guns)
        horses, elephants, armoured_tanks, sling_guns = 1, 2, 3, 4
        bp = BattalionProcessor(3, horses=horses, elephants=elephants,
                                armoured_tanks=armoured_tanks,
                                sling_guns=sling_guns)
        assert BattlePlanner(bp, deepcopy(our_army)).resolve_battalion(BattalionType.ARMOUREDTANKS, 29) == True
        assert BattlePlanner(bp, deepcopy(our_army)).resolve_battalion(BattalionType.ARMOUREDTANKS, 30) == True
        assert BattlePlanner(bp, deepcopy(our_army)).resolve_battalion(BattalionType.ARMOUREDTANKS, 31) == False
        assert BattlePlanner(bp, deepcopy(our_army)).resolve_battalion(BattalionType.ARMOUREDTANKS, 104) == False
        assert BattlePlanner(bp, deepcopy(our_army)).resolve_battalion(BattalionType.ARMOUREDTANKS, 105) == False
        assert BattlePlanner(bp, deepcopy(our_army)).resolve_battalion(BattalionType.ARMOUREDTANKS, 106) == False        

    def test_get_winning_army_1(self):
        horses, elephants, armoured_tanks, sling_guns = 100, 50, 10, 5
        our_army = Army(horses=horses, elephants=elephants,
                    armoured_tanks=armoured_tanks, sling_guns=sling_guns)
        enemy_army = Army(horses=200, elephants=100,
                    armoured_tanks=20, sling_guns=10)
        horses_order, elephants_order, armoured_tanks_order, sling_guns_order = 1, 2, 3, 4
        bp = BattalionProcessor(2, horses=horses_order, elephants=elephants_order,
                                armoured_tanks=armoured_tanks_order,
                                sling_guns=sling_guns_order)
                                
        battle_result, winning_army = BattlePlanner(bp, deepcopy(our_army)).get_winning_army(deepcopy(enemy_army))
        assert battle_result == True
        assert winning_army == Army(horses=100, elephants=50,
                                    armoured_tanks=10,
                                    sling_guns=5)

    def test_get_winning_army_2(self):
        horses, elephants, armoured_tanks, sling_guns = 100, 50, 10, 5
        our_army = Army(horses=horses, elephants=elephants,
                    armoured_tanks=armoured_tanks, sling_guns=sling_guns)
        enemy_army = Army(horses=600, elephants=100)
        horses_order, elephants_order, armoured_tanks_order, sling_guns_order = 1, 2, 3, 4
        bp = BattalionProcessor(4, horses=horses_order, elephants=elephants_order,
                                armoured_tanks=armoured_tanks_order,
                                sling_guns=sling_guns_order)
        bp.add_battalion_substituation(BattalionType.ELEPHANTS, BattalionType.HORSES, 2)                        

        battle_result, winning_army = BattlePlanner(bp, deepcopy(our_army)).get_winning_army(deepcopy(enemy_army))
        assert battle_result == True
        assert winning_army == Army(horses=100, elephants=50)
    
    def test_get_winning_army_3(self):
        horses, elephants, armoured_tanks, sling_guns = 100, 50, 10, 5
        our_army = Army(horses=horses, elephants=elephants,
                    armoured_tanks=armoured_tanks, sling_guns=sling_guns)
        enemy_army = Army(horses=600, elephants=100)
        horses_order, elephants_order, armoured_tanks_order, sling_guns_order = 1, 2, 3, 4
        bp = BattalionProcessor(4, horses=horses_order, elephants=elephants_order,
                                armoured_tanks=armoured_tanks_order,
                                sling_guns=sling_guns_order)
        bp.add_battalion_substituation(BattalionType.ELEPHANTS, BattalionType.HORSES, 1)                        

        battle_result, winning_army = BattlePlanner(bp, deepcopy(our_army)).get_winning_army(deepcopy(enemy_army))
        assert battle_result == False
        assert winning_army == Army(horses=100, elephants=50)
    
    def test_get_winning_army_4(self):
        horses, elephants, armoured_tanks, sling_guns = 100, 50, 10, 5
        our_army = Army(horses=horses, elephants=elephants,
                    armoured_tanks=armoured_tanks, sling_guns=sling_guns)
        enemy_army = Army(horses=100, elephants=101,
                          armoured_tanks=20, sling_guns=5)
        horses_order, elephants_order, armoured_tanks_order, sling_guns_order = 1, 2, 3, 4
        bp = BattalionProcessor(2, horses=horses_order, elephants=elephants_order,
                                armoured_tanks=armoured_tanks_order,
                                sling_guns=sling_guns_order)
        bp.add_battalion_substituation(BattalionType.ELEPHANTS, BattalionType.HORSES, 2)
        bp.add_battalion_substituation(BattalionType.ARMOUREDTANKS, BattalionType.ELEPHANTS, 2)
        bp.add_battalion_substituation(BattalionType.SLINGGUNS, BattalionType.ARMOUREDTANKS, 2)

        battle_result, winning_army = BattlePlanner(bp, deepcopy(our_army)).get_winning_army(deepcopy(enemy_army))
        assert battle_result == True
        assert winning_army == Army(horses=52, elephants=50,
                                    armoured_tanks=10, sling_guns=3)

    def test_get_winning_army_5(self):
        horses, elephants, armoured_tanks, sling_guns = 100, 50, 10, 5
        our_army = Army(horses=horses, elephants=elephants,
                    armoured_tanks=armoured_tanks, sling_guns=sling_guns)
        enemy_army = Army(horses=150, elephants=96,
                          armoured_tanks=26, sling_guns=8)
        horses_order, elephants_order, armoured_tanks_order, sling_guns_order = 1, 2, 3, 4
        bp = BattalionProcessor(2, horses=horses_order, elephants=elephants_order,
                                armoured_tanks=armoured_tanks_order,
                                sling_guns=sling_guns_order)
        bp.add_battalion_substituation(BattalionType.ELEPHANTS, BattalionType.HORSES, 2)
        bp.add_battalion_substituation(BattalionType.ARMOUREDTANKS, BattalionType.ELEPHANTS, 2)
        bp.add_battalion_substituation(BattalionType.SLINGGUNS, BattalionType.ARMOUREDTANKS, 2)

        battle_result, winning_army = BattlePlanner(bp, deepcopy(our_army)).get_winning_army(deepcopy(enemy_army))
        assert battle_result == True
        assert winning_army == Army(horses=75, elephants=50,
                                    armoured_tanks=10, sling_guns=5)

    def test_get_winning_army_6(self):
        horses, elephants, armoured_tanks, sling_guns = 100, 50, 10, 5
        our_army = Army(horses=horses, elephants=elephants,
                    armoured_tanks=armoured_tanks, sling_guns=sling_guns)
        enemy_army = Army(horses=250, elephants=50,
                          armoured_tanks=20, sling_guns=15)
        horses_order, elephants_order, armoured_tanks_order, sling_guns_order = 1, 2, 3, 4
        bp = BattalionProcessor(2, horses=horses_order, elephants=elephants_order,
                                armoured_tanks=armoured_tanks_order,
                                sling_guns=sling_guns_order)
        bp.add_battalion_substituation(BattalionType.ELEPHANTS, BattalionType.HORSES, 2)
        bp.add_battalion_substituation(BattalionType.ARMOUREDTANKS, BattalionType.ELEPHANTS, 2)
        bp.add_battalion_substituation(BattalionType.SLINGGUNS, BattalionType.ARMOUREDTANKS, 2)

        battle_result, winning_army = BattlePlanner(bp, deepcopy(our_army)).get_winning_army(deepcopy(enemy_army))
        assert battle_result == False
        assert winning_army == Army(horses=100, elephants=38,
                                    armoured_tanks=10, sling_guns=5)
                                    