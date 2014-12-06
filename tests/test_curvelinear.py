import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.performance_curves import CurveLinear

log = logging.getLogger(__name__)

class TestCurveLinear(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_curvelinear(self):

        pyidf.validation_level = ValidationLevel.error

        obj = CurveLinear()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # real
        var_coefficient1_constant = 2.2
        obj.coefficient1_constant = var_coefficient1_constant
        # real
        var_coefficient2_x = 3.3
        obj.coefficient2_x = var_coefficient2_x
        # real
        var_minimum_value_of_x = 4.4
        obj.minimum_value_of_x = var_minimum_value_of_x
        # real
        var_maximum_value_of_x = 5.5
        obj.maximum_value_of_x = var_maximum_value_of_x
        # real
        var_minimum_curve_output = 6.6
        obj.minimum_curve_output = var_minimum_curve_output
        # real
        var_maximum_curve_output = 7.7
        obj.maximum_curve_output = var_maximum_curve_output
        # alpha
        var_input_unit_type_for_x = "Dimensionless"
        obj.input_unit_type_for_x = var_input_unit_type_for_x
        # alpha
        var_output_unit_type = "Dimensionless"
        obj.output_unit_type = var_output_unit_type

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.curvelinears[0].name, var_name)
        self.assertAlmostEqual(idf2.curvelinears[0].coefficient1_constant, var_coefficient1_constant)
        self.assertAlmostEqual(idf2.curvelinears[0].coefficient2_x, var_coefficient2_x)
        self.assertAlmostEqual(idf2.curvelinears[0].minimum_value_of_x, var_minimum_value_of_x)
        self.assertAlmostEqual(idf2.curvelinears[0].maximum_value_of_x, var_maximum_value_of_x)
        self.assertAlmostEqual(idf2.curvelinears[0].minimum_curve_output, var_minimum_curve_output)
        self.assertAlmostEqual(idf2.curvelinears[0].maximum_curve_output, var_maximum_curve_output)
        self.assertEqual(idf2.curvelinears[0].input_unit_type_for_x, var_input_unit_type_for_x)
        self.assertEqual(idf2.curvelinears[0].output_unit_type, var_output_unit_type)