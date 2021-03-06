import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.performance_tables import TableMultiVariableLookup

log = logging.getLogger(__name__)

class TestTableMultiVariableLookup(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_tablemultivariablelookup(self):

        pyidf.validation_level = ValidationLevel.error

        obj = TableMultiVariableLookup()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_interpolation_method = "LinearInterpolationOfTable"
        obj.interpolation_method = var_interpolation_method
        # integer
        var_number_of_interpolation_points = 3
        obj.number_of_interpolation_points = var_number_of_interpolation_points
        # alpha
        var_curve_type = "Linear"
        obj.curve_type = var_curve_type
        # alpha
        var_table_data_format = "SingleLineIndependentVariableWithMatrix"
        obj.table_data_format = var_table_data_format
        # alpha
        var_external_file_name = "External File Name"
        obj.external_file_name = var_external_file_name
        # alpha
        var_x1_sort_order = "Ascending"
        obj.x1_sort_order = var_x1_sort_order
        # alpha
        var_x2_sort_order = "Ascending"
        obj.x2_sort_order = var_x2_sort_order
        # real
        var_normalization_reference = 9.9
        obj.normalization_reference = var_normalization_reference
        # real
        var_minimum_value_of_x1 = 10.1
        obj.minimum_value_of_x1 = var_minimum_value_of_x1
        # real
        var_maximum_value_of_x1 = 11.11
        obj.maximum_value_of_x1 = var_maximum_value_of_x1
        # real
        var_minimum_value_of_x2 = 12.12
        obj.minimum_value_of_x2 = var_minimum_value_of_x2
        # real
        var_maximum_value_of_x2 = 13.13
        obj.maximum_value_of_x2 = var_maximum_value_of_x2
        # real
        var_minimum_value_of_x3 = 14.14
        obj.minimum_value_of_x3 = var_minimum_value_of_x3
        # real
        var_maximum_value_of_x3 = 15.15
        obj.maximum_value_of_x3 = var_maximum_value_of_x3
        # real
        var_minimum_value_of_x4 = 16.16
        obj.minimum_value_of_x4 = var_minimum_value_of_x4
        # real
        var_maximum_value_of_x4 = 17.17
        obj.maximum_value_of_x4 = var_maximum_value_of_x4
        # real
        var_minimum_value_of_x5 = 18.18
        obj.minimum_value_of_x5 = var_minimum_value_of_x5
        # real
        var_maximum_value_of_x5 = 19.19
        obj.maximum_value_of_x5 = var_maximum_value_of_x5
        # real
        var_minimum_table_output = 20.2
        obj.minimum_table_output = var_minimum_table_output
        # real
        var_maximum_table_output = 21.21
        obj.maximum_table_output = var_maximum_table_output
        # alpha
        var_input_unit_type_for_x1 = "Dimensionless"
        obj.input_unit_type_for_x1 = var_input_unit_type_for_x1
        # alpha
        var_input_unit_type_for_x2 = "Dimensionless"
        obj.input_unit_type_for_x2 = var_input_unit_type_for_x2
        # alpha
        var_input_unit_type_for_x3 = "Dimensionless"
        obj.input_unit_type_for_x3 = var_input_unit_type_for_x3
        # alpha
        var_input_unit_type_for_x4 = "Dimensionless"
        obj.input_unit_type_for_x4 = var_input_unit_type_for_x4
        # alpha
        var_input_unit_type_for_x5 = "Dimensionless"
        obj.input_unit_type_for_x5 = var_input_unit_type_for_x5
        # alpha
        var_output_unit_type = "Dimensionless"
        obj.output_unit_type = var_output_unit_type
        # integer
        var_number_of_independent_variables = 3
        obj.number_of_independent_variables = var_number_of_independent_variables
        # integer
        var_number_of_values_for_independent_variable_x1 = 29
        obj.number_of_values_for_independent_variable_x1 = var_number_of_values_for_independent_variable_x1
        # real
        var_field_1_determined_by_the_number_of_independent_variables = 30.3
        obj.field_1_determined_by_the_number_of_independent_variables = var_field_1_determined_by_the_number_of_independent_variables
        # real
        var_field_2_determined_by_the_number_of_independent_variables = 31.31
        obj.field_2_determined_by_the_number_of_independent_variables = var_field_2_determined_by_the_number_of_independent_variables
        paras = []
        var_field_3_determined_by_the_number_of_independent_variables = 32.32
        paras.append(var_field_3_determined_by_the_number_of_independent_variables)
        var_v1 = 33.33
        paras.append(var_v1)
        var_v2 = 34.34
        paras.append(var_v2)
        var_v3 = 35.35
        paras.append(var_v3)
        var_v4 = 36.36
        paras.append(var_v4)
        var_v5 = 37.37
        paras.append(var_v5)
        var_v6 = 38.38
        paras.append(var_v6)
        var_v7 = 39.39
        paras.append(var_v7)
        var_v8 = 40.4
        paras.append(var_v8)
        var_v9 = 41.41
        paras.append(var_v9)
        var_v10 = 42.42
        paras.append(var_v10)
        var_v11 = 43.43
        paras.append(var_v11)
        var_v12 = 44.44
        paras.append(var_v12)
        var_v13 = 45.45
        paras.append(var_v13)
        var_v14 = 46.46
        paras.append(var_v14)
        var_v15 = 47.47
        paras.append(var_v15)
        var_v16 = 48.48
        paras.append(var_v16)
        var_v17 = 49.49
        paras.append(var_v17)
        var_v18 = 50.5
        paras.append(var_v18)
        var_v19 = 51.51
        paras.append(var_v19)
        obj.add_extensible(*paras)
        

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.tablemultivariablelookups[0].name, var_name)
        self.assertEqual(idf2.tablemultivariablelookups[0].interpolation_method, var_interpolation_method)
        self.assertEqual(idf2.tablemultivariablelookups[0].number_of_interpolation_points, var_number_of_interpolation_points)
        self.assertEqual(idf2.tablemultivariablelookups[0].curve_type, var_curve_type)
        self.assertEqual(idf2.tablemultivariablelookups[0].table_data_format, var_table_data_format)
        self.assertEqual(idf2.tablemultivariablelookups[0].external_file_name, var_external_file_name)
        self.assertEqual(idf2.tablemultivariablelookups[0].x1_sort_order, var_x1_sort_order)
        self.assertEqual(idf2.tablemultivariablelookups[0].x2_sort_order, var_x2_sort_order)
        self.assertAlmostEqual(idf2.tablemultivariablelookups[0].normalization_reference, var_normalization_reference)
        self.assertAlmostEqual(idf2.tablemultivariablelookups[0].minimum_value_of_x1, var_minimum_value_of_x1)
        self.assertAlmostEqual(idf2.tablemultivariablelookups[0].maximum_value_of_x1, var_maximum_value_of_x1)
        self.assertAlmostEqual(idf2.tablemultivariablelookups[0].minimum_value_of_x2, var_minimum_value_of_x2)
        self.assertAlmostEqual(idf2.tablemultivariablelookups[0].maximum_value_of_x2, var_maximum_value_of_x2)
        self.assertAlmostEqual(idf2.tablemultivariablelookups[0].minimum_value_of_x3, var_minimum_value_of_x3)
        self.assertAlmostEqual(idf2.tablemultivariablelookups[0].maximum_value_of_x3, var_maximum_value_of_x3)
        self.assertAlmostEqual(idf2.tablemultivariablelookups[0].minimum_value_of_x4, var_minimum_value_of_x4)
        self.assertAlmostEqual(idf2.tablemultivariablelookups[0].maximum_value_of_x4, var_maximum_value_of_x4)
        self.assertAlmostEqual(idf2.tablemultivariablelookups[0].minimum_value_of_x5, var_minimum_value_of_x5)
        self.assertAlmostEqual(idf2.tablemultivariablelookups[0].maximum_value_of_x5, var_maximum_value_of_x5)
        self.assertAlmostEqual(idf2.tablemultivariablelookups[0].minimum_table_output, var_minimum_table_output)
        self.assertAlmostEqual(idf2.tablemultivariablelookups[0].maximum_table_output, var_maximum_table_output)
        self.assertEqual(idf2.tablemultivariablelookups[0].input_unit_type_for_x1, var_input_unit_type_for_x1)
        self.assertEqual(idf2.tablemultivariablelookups[0].input_unit_type_for_x2, var_input_unit_type_for_x2)
        self.assertEqual(idf2.tablemultivariablelookups[0].input_unit_type_for_x3, var_input_unit_type_for_x3)
        self.assertEqual(idf2.tablemultivariablelookups[0].input_unit_type_for_x4, var_input_unit_type_for_x4)
        self.assertEqual(idf2.tablemultivariablelookups[0].input_unit_type_for_x5, var_input_unit_type_for_x5)
        self.assertEqual(idf2.tablemultivariablelookups[0].output_unit_type, var_output_unit_type)
        self.assertEqual(idf2.tablemultivariablelookups[0].number_of_independent_variables, var_number_of_independent_variables)
        self.assertEqual(idf2.tablemultivariablelookups[0].number_of_values_for_independent_variable_x1, var_number_of_values_for_independent_variable_x1)
        self.assertAlmostEqual(idf2.tablemultivariablelookups[0].field_1_determined_by_the_number_of_independent_variables, var_field_1_determined_by_the_number_of_independent_variables)
        self.assertAlmostEqual(idf2.tablemultivariablelookups[0].field_2_determined_by_the_number_of_independent_variables, var_field_2_determined_by_the_number_of_independent_variables)
        index = obj.extensible_field_index("Field 3 Determined by the Number of Independent Variables")
        self.assertAlmostEqual(idf2.tablemultivariablelookups[0].extensibles[0][index], var_field_3_determined_by_the_number_of_independent_variables)
        index = obj.extensible_field_index("V1")
        self.assertAlmostEqual(idf2.tablemultivariablelookups[0].extensibles[0][index], var_v1)
        index = obj.extensible_field_index("V2")
        self.assertAlmostEqual(idf2.tablemultivariablelookups[0].extensibles[0][index], var_v2)
        index = obj.extensible_field_index("V3")
        self.assertAlmostEqual(idf2.tablemultivariablelookups[0].extensibles[0][index], var_v3)
        index = obj.extensible_field_index("V4")
        self.assertAlmostEqual(idf2.tablemultivariablelookups[0].extensibles[0][index], var_v4)
        index = obj.extensible_field_index("V5")
        self.assertAlmostEqual(idf2.tablemultivariablelookups[0].extensibles[0][index], var_v5)
        index = obj.extensible_field_index("V6")
        self.assertAlmostEqual(idf2.tablemultivariablelookups[0].extensibles[0][index], var_v6)
        index = obj.extensible_field_index("V7")
        self.assertAlmostEqual(idf2.tablemultivariablelookups[0].extensibles[0][index], var_v7)
        index = obj.extensible_field_index("V8")
        self.assertAlmostEqual(idf2.tablemultivariablelookups[0].extensibles[0][index], var_v8)
        index = obj.extensible_field_index("V9")
        self.assertAlmostEqual(idf2.tablemultivariablelookups[0].extensibles[0][index], var_v9)
        index = obj.extensible_field_index("V10")
        self.assertAlmostEqual(idf2.tablemultivariablelookups[0].extensibles[0][index], var_v10)
        index = obj.extensible_field_index("V11")
        self.assertAlmostEqual(idf2.tablemultivariablelookups[0].extensibles[0][index], var_v11)
        index = obj.extensible_field_index("V12")
        self.assertAlmostEqual(idf2.tablemultivariablelookups[0].extensibles[0][index], var_v12)
        index = obj.extensible_field_index("V13")
        self.assertAlmostEqual(idf2.tablemultivariablelookups[0].extensibles[0][index], var_v13)
        index = obj.extensible_field_index("V14")
        self.assertAlmostEqual(idf2.tablemultivariablelookups[0].extensibles[0][index], var_v14)
        index = obj.extensible_field_index("V15")
        self.assertAlmostEqual(idf2.tablemultivariablelookups[0].extensibles[0][index], var_v15)
        index = obj.extensible_field_index("V16")
        self.assertAlmostEqual(idf2.tablemultivariablelookups[0].extensibles[0][index], var_v16)
        index = obj.extensible_field_index("V17")
        self.assertAlmostEqual(idf2.tablemultivariablelookups[0].extensibles[0][index], var_v17)
        index = obj.extensible_field_index("V18")
        self.assertAlmostEqual(idf2.tablemultivariablelookups[0].extensibles[0][index], var_v18)
        index = obj.extensible_field_index("V19")
        self.assertAlmostEqual(idf2.tablemultivariablelookups[0].extensibles[0][index], var_v19)