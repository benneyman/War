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
