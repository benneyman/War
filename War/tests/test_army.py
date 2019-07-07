from army import Army
from battalion_types import BattalionType
import pytest


class Test_Army(object):
    def test_army_init(self):
        horses, elephants, armoured_tanks, sling_guns = 100, 50, 10, 5
        army = Army(horses=horses, elephants=elephants,
                    armoured_tanks=armoured_tanks, sling_guns=sling_guns)
        assert army.get_battalion_strength(BattalionType.HORSES) == horses
        assert army.get_battalion_strength(BattalionType.ELEPHANTS) == elephants
        assert army.get_battalion_strength(BattalionType.ARMOUREDTANKS) == armoured_tanks
        assert army.get_battalion_strength(BattalionType.SLINGGUNS) == sling_guns
    
    def test_invalid_battalion_name(self):
        horses, elephants, armoured_tanks, sling_guns = 100, 50, 10, 5
        army = Army(horses=horses, elephants=elephants,
                    armoured_tanks=armoured_tanks, sling_guns=sling_guns)
        with pytest.raises(KeyError):
            army.get_battalion_strength(6)
    
    def test_change_battalion_strength(self):
        horses, elephants, armoured_tanks, sling_guns = 100, 50, 10, 5
        army = Army(horses=horses, elephants=elephants,
                    armoured_tanks=armoured_tanks, sling_guns=sling_guns)
        army.update_battalion_strength(BattalionType.HORSES, -50)
        army.update_battalion_strength(BattalionType.SLINGGUNS, 5)
        assert army.get_battalion_strength(BattalionType.HORSES) == 50
        assert army.get_battalion_strength(BattalionType.SLINGGUNS) == 10
    
    def test_change_battalion_strength_1(self):
        army = Army()
        army.update_battalion_strength(BattalionType.HORSES, 50)
        assert army.get_battalion_strength(BattalionType.HORSES) == 50

    def test_get_battalions(self):
        horses, elephants, armoured_tanks, sling_guns = 100, 50, 10, 5
        army = Army(horses=horses, elephants=elephants,
                    armoured_tanks=armoured_tanks, sling_guns=sling_guns)
        assert set(army.get_battalions()) == set([BattalionType.HORSES,
                                                  BattalionType.ELEPHANTS,
                                                  BattalionType.SLINGGUNS,
                                                  BattalionType.ARMOUREDTANKS])
    def test_has_battalion(self):
        horses, elephants, armoured_tanks, sling_guns = 100, 50, 10, 5
        army = Army(horses=horses, elephants=elephants,
                    armoured_tanks=armoured_tanks)
        assert army.has_battalion(BattalionType.HORSES) == True
        assert army.has_battalion(BattalionType.ELEPHANTS) == True
        assert army.has_battalion(BattalionType.ARMOUREDTANKS) == True
        assert army.has_battalion(BattalionType.SLINGGUNS) == False
        assert army.has_battalion("NonExistantBattalion") == False
