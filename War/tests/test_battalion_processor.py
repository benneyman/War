from battalion_processor import BattalionProcessor
from battalion_types import BattalionType
from typing import List


class Test_BattalionProcessor(object):
    def test_get_default_battalion_seniority(self):
        horses, elephants, armoured_tanks, sling_guns = 1, 2, 3, 4
        bp = BattalionProcessor(horses=horses, elephants=elephants,
                                armoured_tanks=armoured_tanks, sling_guns=sling_guns)
        assert bp.get_battalion_seniority(BattalionType.HORSES) == 1
        assert bp.get_battalion_seniority(BattalionType.ELEPHANTS) == 2
        assert bp.get_battalion_seniority(BattalionType.ARMOUREDTANKS) == 3
        assert bp.get_battalion_seniority(BattalionType.SLINGGUNS) == 4

    def test_get_custom_battalion_seniority(self):
        armoured_tanks, sling_guns, elephants, horses = 4, 3, 2, 1
        bp = BattalionProcessor(horses=horses, elephants=elephants,
                                armoured_tanks=armoured_tanks, sling_guns=sling_guns)
        assert bp.get_battalion_seniority(BattalionType.HORSES) == horses
        assert bp.get_battalion_seniority(BattalionType.ELEPHANTS) == elephants
        assert bp.get_battalion_seniority(BattalionType.ARMOUREDTANKS) == armoured_tanks
        assert bp.get_battalion_seniority(BattalionType.SLINGGUNS) == sling_guns

    def test_add_substitution_battalion(self):
        horses, elephants, armoured_tanks, sling_guns = 1, 2, 3, 4
        bp = BattalionProcessor(horses=horses, elephants=elephants,
                                armoured_tanks=armoured_tanks,
                                sling_guns=sling_guns)
        bp.add_battalion_substituation(BattalionType.HORSES,
                                       BattalionType.ELEPHANTS, 4)
        assert bp.get_substitution_battalion(BattalionType.HORSES) == [(BattalionType.ELEPHANTS, 4)]
        assert bp.get_substitution_battalion(BattalionType.ELEPHANTS) == [(BattalionType.HORSES, 0.25)]

    def test_default_substitution_battalion(self):
        horses, elephants, armoured_tanks, sling_guns = 1, 2, 3, 4
        bp = BattalionProcessor(horses=horses, elephants=elephants,
                                armoured_tanks=armoured_tanks,
                                sling_guns=sling_guns)
        actual = bp.get_substitution_battalion(BattalionType.HORSES)
        expected: List[BattalionType] = []
        assert actual == expected

    def test_custom_substitution_battalion(self):
        bp = BattalionProcessor()
        bp.add_battalion_substituation(BattalionType.HORSES,
                                       BattalionType.ARMOUREDTANKS, 2)
        bp.add_battalion_substituation(BattalionType.HORSES,
                                       BattalionType.ELEPHANTS, 4)
        assert set(bp.get_substitution_battalion(BattalionType.HORSES)) == set([(BattalionType.ELEPHANTS, 4), (BattalionType.ARMOUREDTANKS, 2)])
        assert set(bp.get_substitution_battalion(BattalionType.ARMOUREDTANKS)) == set([(BattalionType.HORSES, 0.5)])
        assert set(bp.get_substitution_battalion(BattalionType.ELEPHANTS)) == set([(BattalionType.HORSES, 0.25)])

        
