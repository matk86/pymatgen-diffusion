# coding: utf-8

from __future__ import division, unicode_literals
from pymatgen.core import Structure
from pymatgen_diffusion.neb.io import MVLCINEBEndPointSet, MVLCINEBSet

import unittest
import os

__author__ = 'hat003'

test_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)))


def get_path(path_str):
    cwd = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(cwd,path_str)
    return path

class MVLCINEBEndPointSetTest(unittest.TestCase):

    endpoint = Structure.from_file(get_path("POSCAR0"))

    def test_incar(self):
        m = MVLCINEBEndPointSet(self.endpoint)
        incar_string = m.incar.get_string(sort_keys=True, pretty=True)
        incar_expect = """ALGO    =  Fast
EDIFF   =  5e-05
EDIFFG  =  -0.02
ENCUT   =  520
IBRION  =  2
ICHARG  =  1
ISIF    =  2
ISMEAR  =  -5
ISPIN   =  2
ISYM    =  0
LORBIT  =  11
LREAL   =  Auto
LWAVE   =  False
MAGMOM  =  35*0.6
NELM    =  100
NELMIN  =  4
NSW     =  99
PREC    =  Accurate
SIGMA   =  0.05"""
        self.assertEqual(incar_string, incar_expect)
        pass

    def test_incar_user_setting(self):
        user_incar_settings = {"ALGO": "Normal",
                               "EDIFFG": -0.05,
                               "NELECT": 576,
                               "NPAR": 4,
                               "NSW": 100,}
        m = MVLCINEBEndPointSet(self.endpoint, user_incar_settings=user_incar_settings)
        incar_string = m.incar.get_string(sort_keys=True, pretty=True)
        incar_expect = """ALGO    =  Normal
EDIFF   =  5e-05
EDIFFG  =  -0.05
ENCUT   =  520
IBRION  =  2
ICHARG  =  1
ISIF    =  2
ISMEAR  =  -5
ISPIN   =  2
ISYM    =  0
LORBIT  =  11
LREAL   =  Auto
LWAVE   =  False
MAGMOM  =  35*0.6
NELECT  =  576
NELM    =  100
NELMIN  =  4
NPAR    =  4
NSW     =  100
PREC    =  Accurate
SIGMA   =  0.05"""

        self.assertEqual(incar_string, incar_expect)

        pass
    pass


class MVLCINEBSetTest(unittest.TestCase):

    structures = [Structure.from_file(get_path("POSCAR" + str(i))) for i in range(3)]

    def test_incar(self):
        m = MVLCINEBSet(self.structures)

        incar_string = m.incar.get_string(sort_keys=True, pretty=True)
        incar_expect ="""ALGO    =  Fast
EDIFF   =  5e-05
EDIFFG  =  -0.02
ENCUT   =  520
IBRION  =  3
ICHAIN  =  0
ICHARG  =  1
IMAGES  =  1
IOPT    =  1
ISIF    =  3
ISMEAR  =  0
ISPIN   =  2
ISYM    =  0
LCHARG  =  False
LCLIMB  =  True
LORBIT  =  0
LREAL   =  Auto
LWAVE   =  False
MAGMOM  =  35*0.6
NELM    =  100
NELMIN  =  6
NSW     =  200
POTIM   =  0
PREC    =  Accurate
SIGMA   =  0.05"""

        self.assertEqual(incar_string, incar_expect)

        pass

    def test_incar_user_setting(self):
        user_incar_settings = {"IOPT": 3,
                               "EDIFFG": -0.05,
                               "NPAR": 4}
        m = MVLCINEBSet(self.structures, user_incar_settings=user_incar_settings)
        incar_string = m.incar.get_string(sort_keys=True, pretty=True)
        incar_expect = """ALGO    =  Fast
EDIFF   =  5e-05
EDIFFG  =  -0.05
ENCUT   =  520
IBRION  =  3
ICHAIN  =  0
ICHARG  =  1
IMAGES  =  1
IOPT    =  3
ISIF    =  3
ISMEAR  =  0
ISPIN   =  2
ISYM    =  0
LCHARG  =  False
LCLIMB  =  True
LORBIT  =  0
LREAL   =  Auto
LWAVE   =  False
MAGMOM  =  35*0.6
NELM    =  100
NELMIN  =  6
NPAR    =  4
NSW     =  200
POTIM   =  0
PREC    =  Accurate
SIGMA   =  0.05"""

        self.assertEqual(incar_string, incar_expect)
        pass

    pass

if __name__ == '__main__':
    unittest.main()
