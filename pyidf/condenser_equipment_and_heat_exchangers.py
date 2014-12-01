from collections import OrderedDict

class CoolingTowerSingleSpeed(object):
    """ Corresponds to IDD object `CoolingTower:SingleSpeed`
        This tower model is based on Merkel's theory, which is also the basis
        for the tower model in ASHRAE's HVAC1 Toolkit. The closed-circuit cooling tower
        is modeled as a counter flow heat exchanger with a single-speed fan drawing air
        through the tower (induced-draft configuration).
        Added fluid bypass as an additional capacity control. 8/2008.
        For a multi-cell tower, the capacity and air/water flow rate inputs are for the entire tower.
    
    """
    internal_name = "CoolingTower:SingleSpeed"
    field_count = 33
    required_fields = ["Name", "Water Inlet Node Name", "Water Outlet Node Name", "Design Air Flow Rate", "Design Fan Power", "Free Convection Air Flow Rate Sizing Factor", "Free Convection U-Factor Times Area Value Sizing Factor", "Heat Rejection Capacity and Nominal Capacity Sizing Ratio", "Free Convection Nominal Capacity Sizing Factor"]

    def __init__(self):
        """ Init data dictionary object for IDD  `CoolingTower:SingleSpeed`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Water Inlet Node Name"] = None
        self._data["Water Outlet Node Name"] = None
        self._data["Design Water Flow Rate"] = None
        self._data["Design Air Flow Rate"] = None
        self._data["Design Fan Power"] = None
        self._data["Design U-Factor Times Area Value"] = None
        self._data["Free Convection Air Flow Rate"] = None
        self._data["Free Convection Air Flow Rate Sizing Factor"] = None
        self._data["Free Convection U-Factor Times Area Value"] = None
        self._data["Free Convection U-Factor Times Area Value Sizing Factor"] = None
        self._data["Performance Input Method"] = None
        self._data["Heat Rejection Capacity and Nominal Capacity Sizing Ratio"] = None
        self._data["Nominal Capacity"] = None
        self._data["Free Convection Capacity"] = None
        self._data["Free Convection Nominal Capacity Sizing Factor"] = None
        self._data["Basin Heater Capacity"] = None
        self._data["Basin Heater Setpoint Temperature"] = None
        self._data["Basin Heater Operating Schedule Name"] = None
        self._data["Evaporation Loss Mode"] = None
        self._data["Evaporation Loss Factor"] = None
        self._data["Drift Loss Percent"] = None
        self._data["Blowdown Calculation Mode"] = None
        self._data["Blowdown Concentration Ratio"] = None
        self._data["Blowdown Makeup Water Usage Schedule Name"] = None
        self._data["Supply Water Storage Tank Name"] = None
        self._data["Outdoor Air Inlet Node Name"] = None
        self._data["Capacity Control"] = None
        self._data["Number of Cells"] = None
        self._data["Cell Control"] = None
        self._data["Cell Minimum  Water Flow Rate Fraction"] = None
        self._data["Cell Maximum Water Flow Rate Fraction"] = None
        self._data["Sizing Factor"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.water_inlet_node_name = None
        else:
            self.water_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.water_outlet_node_name = None
        else:
            self.water_outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_water_flow_rate = None
        else:
            self.design_water_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_air_flow_rate = None
        else:
            self.design_air_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_fan_power = None
        else:
            self.design_fan_power = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_ufactor_times_area_value = None
        else:
            self.design_ufactor_times_area_value = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.free_convection_air_flow_rate = None
        else:
            self.free_convection_air_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.free_convection_air_flow_rate_sizing_factor = None
        else:
            self.free_convection_air_flow_rate_sizing_factor = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.free_convection_ufactor_times_area_value = None
        else:
            self.free_convection_ufactor_times_area_value = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.free_convection_ufactor_times_area_value_sizing_factor = None
        else:
            self.free_convection_ufactor_times_area_value_sizing_factor = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.performance_input_method = None
        else:
            self.performance_input_method = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heat_rejection_capacity_and_nominal_capacity_sizing_ratio = None
        else:
            self.heat_rejection_capacity_and_nominal_capacity_sizing_ratio = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.nominal_capacity = None
        else:
            self.nominal_capacity = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.free_convection_capacity = None
        else:
            self.free_convection_capacity = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.free_convection_nominal_capacity_sizing_factor = None
        else:
            self.free_convection_nominal_capacity_sizing_factor = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.basin_heater_capacity = None
        else:
            self.basin_heater_capacity = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.basin_heater_setpoint_temperature = None
        else:
            self.basin_heater_setpoint_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.basin_heater_operating_schedule_name = None
        else:
            self.basin_heater_operating_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.evaporation_loss_mode = None
        else:
            self.evaporation_loss_mode = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.evaporation_loss_factor = None
        else:
            self.evaporation_loss_factor = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.drift_loss_percent = None
        else:
            self.drift_loss_percent = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.blowdown_calculation_mode = None
        else:
            self.blowdown_calculation_mode = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.blowdown_concentration_ratio = None
        else:
            self.blowdown_concentration_ratio = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.blowdown_makeup_water_usage_schedule_name = None
        else:
            self.blowdown_makeup_water_usage_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.supply_water_storage_tank_name = None
        else:
            self.supply_water_storage_tank_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outdoor_air_inlet_node_name = None
        else:
            self.outdoor_air_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.capacity_control = None
        else:
            self.capacity_control = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.number_of_cells = None
        else:
            self.number_of_cells = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cell_control = None
        else:
            self.cell_control = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cell_minimum_water_flow_rate_fraction = None
        else:
            self.cell_minimum_water_flow_rate_fraction = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cell_maximum_water_flow_rate_fraction = None
        else:
            self.cell_maximum_water_flow_rate_fraction = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.sizing_factor = None
        else:
            self.sizing_factor = vals[i]
        i += 1
        if i >= len(vals):
            return

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `Name`
        Tower Name

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')
        self._data["Name"] = value

    @property
    def water_inlet_node_name(self):
        """Get water_inlet_node_name

        Returns:
            str: the value of `water_inlet_node_name` or None if not set
        """
        return self._data["Water Inlet Node Name"]

    @water_inlet_node_name.setter
    def water_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Water Inlet Node Name`
        Name of tower water inlet node

        Args:
            value (str): value for IDD Field `Water Inlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `water_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `water_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `water_inlet_node_name`')
        self._data["Water Inlet Node Name"] = value

    @property
    def water_outlet_node_name(self):
        """Get water_outlet_node_name

        Returns:
            str: the value of `water_outlet_node_name` or None if not set
        """
        return self._data["Water Outlet Node Name"]

    @water_outlet_node_name.setter
    def water_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Water Outlet Node Name`
        Name of tower water outlet node

        Args:
            value (str): value for IDD Field `Water Outlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `water_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `water_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `water_outlet_node_name`')
        self._data["Water Outlet Node Name"] = value

    @property
    def design_water_flow_rate(self):
        """Get design_water_flow_rate

        Returns:
            float: the value of `design_water_flow_rate` or None if not set
        """
        return self._data["Design Water Flow Rate"]

    @design_water_flow_rate.setter
    def design_water_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Design Water Flow Rate`
        Leave field blank if tower performance input method is NominalCapacity

        Args:
            value (float or "Autosize"): value for IDD Field `Design Water Flow Rate`
                Units: m3/s
                IP-Units: gal/min
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Design Water Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `design_water_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `design_water_flow_rate`')
        self._data["Design Water Flow Rate"] = value

    @property
    def design_air_flow_rate(self):
        """Get design_air_flow_rate

        Returns:
            float: the value of `design_air_flow_rate` or None if not set
        """
        return self._data["Design Air Flow Rate"]

    @design_air_flow_rate.setter
    def design_air_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Design Air Flow Rate`

        Args:
            value (float or "Autosize"): value for IDD Field `Design Air Flow Rate`
                Units: m3/s
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Design Air Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `design_air_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `design_air_flow_rate`')
        self._data["Design Air Flow Rate"] = value

    @property
    def design_fan_power(self):
        """Get design_fan_power

        Returns:
            float: the value of `design_fan_power` or None if not set
        """
        return self._data["Design Fan Power"]

    @design_fan_power.setter
    def design_fan_power(self, value=None):
        """  Corresponds to IDD Field `Design Fan Power`
        This is the fan motor electric input power

        Args:
            value (float or "Autosize"): value for IDD Field `Design Fan Power`
                Units: W
                IP-Units: W
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Design Fan Power"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `design_fan_power`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `design_fan_power`')
        self._data["Design Fan Power"] = value

    @property
    def design_ufactor_times_area_value(self):
        """Get design_ufactor_times_area_value

        Returns:
            float: the value of `design_ufactor_times_area_value` or None if not set
        """
        return self._data["Design U-Factor Times Area Value"]

    @design_ufactor_times_area_value.setter
    def design_ufactor_times_area_value(self, value=None):
        """  Corresponds to IDD Field `Design U-Factor Times Area Value`
        Leave field blank if tower performance input method is NominalCapacity

        Args:
            value (float or "Autosize"): value for IDD Field `Design U-Factor Times Area Value`
                Units: W/K
                value > 0.0
                value <= 2100000.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Design U-Factor Times Area Value"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `design_ufactor_times_area_value`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `design_ufactor_times_area_value`')
            if value > 2100000.0:
                raise ValueError('value need to be smaller 2100000.0 '
                                 'for field `design_ufactor_times_area_value`')
        self._data["Design U-Factor Times Area Value"] = value

    @property
    def free_convection_air_flow_rate(self):
        """Get free_convection_air_flow_rate

        Returns:
            float: the value of `free_convection_air_flow_rate` or None if not set
        """
        return self._data["Free Convection Air Flow Rate"]

    @free_convection_air_flow_rate.setter
    def free_convection_air_flow_rate(self, value=0.0):
        """  Corresponds to IDD Field `Free Convection Air Flow Rate`

        Args:
            value (float or "Autocalculate"): value for IDD Field `Free Convection Air Flow Rate`
                Units: m3/s
                Default value: 0.0
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autocalculate":
                    self._data["Free Convection Air Flow Rate"] = "Autocalculate"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `free_convection_air_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `free_convection_air_flow_rate`')
        self._data["Free Convection Air Flow Rate"] = value

    @property
    def free_convection_air_flow_rate_sizing_factor(self):
        """Get free_convection_air_flow_rate_sizing_factor

        Returns:
            float: the value of `free_convection_air_flow_rate_sizing_factor` or None if not set
        """
        return self._data["Free Convection Air Flow Rate Sizing Factor"]

    @free_convection_air_flow_rate_sizing_factor.setter
    def free_convection_air_flow_rate_sizing_factor(self, value=0.1):
        """  Corresponds to IDD Field `Free Convection Air Flow Rate Sizing Factor`
        This field is only used if the previous field is set to autocalculate.

        Args:
            value (float): value for IDD Field `Free Convection Air Flow Rate Sizing Factor`
                Default value: 0.1
                value > 0.0
                value < 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `free_convection_air_flow_rate_sizing_factor`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `free_convection_air_flow_rate_sizing_factor`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `free_convection_air_flow_rate_sizing_factor`')
        self._data["Free Convection Air Flow Rate Sizing Factor"] = value

    @property
    def free_convection_ufactor_times_area_value(self):
        """Get free_convection_ufactor_times_area_value

        Returns:
            float: the value of `free_convection_ufactor_times_area_value` or None if not set
        """
        return self._data["Free Convection U-Factor Times Area Value"]

    @free_convection_ufactor_times_area_value.setter
    def free_convection_ufactor_times_area_value(self, value=0.0):
        """  Corresponds to IDD Field `Free Convection U-Factor Times Area Value`

        Args:
            value (float or "Autocalculate"): value for IDD Field `Free Convection U-Factor Times Area Value`
                Units: W/K
                Default value: 0.0
                value >= 0.0
                value <= 300000.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autocalculate":
                    self._data["Free Convection U-Factor Times Area Value"] = "Autocalculate"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `free_convection_ufactor_times_area_value`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `free_convection_ufactor_times_area_value`')
            if value > 300000.0:
                raise ValueError('value need to be smaller 300000.0 '
                                 'for field `free_convection_ufactor_times_area_value`')
        self._data["Free Convection U-Factor Times Area Value"] = value

    @property
    def free_convection_ufactor_times_area_value_sizing_factor(self):
        """Get free_convection_ufactor_times_area_value_sizing_factor

        Returns:
            float: the value of `free_convection_ufactor_times_area_value_sizing_factor` or None if not set
        """
        return self._data["Free Convection U-Factor Times Area Value Sizing Factor"]

    @free_convection_ufactor_times_area_value_sizing_factor.setter
    def free_convection_ufactor_times_area_value_sizing_factor(self, value=0.1):
        """  Corresponds to IDD Field `Free Convection U-Factor Times Area Value Sizing Factor`
        This field is only used if the previous field is set to autocalculate and
        the Performance Input Method is UFactorTimesAreaAndDesignWaterFlowRate

        Args:
            value (float): value for IDD Field `Free Convection U-Factor Times Area Value Sizing Factor`
                Default value: 0.1
                value > 0.0
                value < 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `free_convection_ufactor_times_area_value_sizing_factor`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `free_convection_ufactor_times_area_value_sizing_factor`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `free_convection_ufactor_times_area_value_sizing_factor`')
        self._data["Free Convection U-Factor Times Area Value Sizing Factor"] = value

    @property
    def performance_input_method(self):
        """Get performance_input_method

        Returns:
            str: the value of `performance_input_method` or None if not set
        """
        return self._data["Performance Input Method"]

    @performance_input_method.setter
    def performance_input_method(self, value="UFactorTimesAreaAndDesignWaterFlowRate"):
        """  Corresponds to IDD Field `Performance Input Method`
        User can define tower thermal performance by specifying the tower UA,
        the Design Air Flow Rate and the Design Water Flow Rate,
        or by specifying the tower nominal capacity

        Args:
            value (str): value for IDD Field `Performance Input Method`
                Default value: UFactorTimesAreaAndDesignWaterFlowRate
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `performance_input_method`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `performance_input_method`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `performance_input_method`')
        self._data["Performance Input Method"] = value

    @property
    def heat_rejection_capacity_and_nominal_capacity_sizing_ratio(self):
        """Get heat_rejection_capacity_and_nominal_capacity_sizing_ratio

        Returns:
            float: the value of `heat_rejection_capacity_and_nominal_capacity_sizing_ratio` or None if not set
        """
        return self._data["Heat Rejection Capacity and Nominal Capacity Sizing Ratio"]

    @heat_rejection_capacity_and_nominal_capacity_sizing_ratio.setter
    def heat_rejection_capacity_and_nominal_capacity_sizing_ratio(self, value=1.25):
        """  Corresponds to IDD Field `Heat Rejection Capacity and Nominal Capacity Sizing Ratio`

        Args:
            value (float): value for IDD Field `Heat Rejection Capacity and Nominal Capacity Sizing Ratio`
                Default value: 1.25
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `heat_rejection_capacity_and_nominal_capacity_sizing_ratio`'.format(value))
        self._data["Heat Rejection Capacity and Nominal Capacity Sizing Ratio"] = value

    @property
    def nominal_capacity(self):
        """Get nominal_capacity

        Returns:
            float: the value of `nominal_capacity` or None if not set
        """
        return self._data["Nominal Capacity"]

    @nominal_capacity.setter
    def nominal_capacity(self, value=None):
        """  Corresponds to IDD Field `Nominal Capacity`
        Nominal tower capacity with entering water at 35C (95F), leaving water at
        29.44C (85F), entering air at 25.56C (78F) wet-bulb temperature and 35C (95F)
        dry-bulb temperature. Design water flow rate assumed to be 5.382E-8 m3/s per watt
        (3 gpm/ton). Nominal tower capacity times (1.25) gives the actual tower
        heat rejection at these operating conditions.

        Args:
            value (float): value for IDD Field `Nominal Capacity`
                Units: W
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `nominal_capacity`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `nominal_capacity`')
        self._data["Nominal Capacity"] = value

    @property
    def free_convection_capacity(self):
        """Get free_convection_capacity

        Returns:
            float: the value of `free_convection_capacity` or None if not set
        """
        return self._data["Free Convection Capacity"]

    @free_convection_capacity.setter
    def free_convection_capacity(self, value=None):
        """  Corresponds to IDD Field `Free Convection Capacity`
        Tower capacity in free convection regime with entering water at 35C (95F),
        leaving water at 29.44C (85F), entering air at 25.56C (78F) wet-bulb temperature
        and 35C (95F) dry-bulb temperature. Design water flow rate assumed to be
        5.382E-8 m3/s per watt of nominal tower capacity (3 gpm/ton). Tower free
        convection capacity times (1.25) gives the actual tower heat rejection at these
        operating conditions.

        Args:
            value (float or "Autocalculate"): value for IDD Field `Free Convection Capacity`
                Units: W
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autocalculate":
                    self._data["Free Convection Capacity"] = "Autocalculate"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `free_convection_capacity`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `free_convection_capacity`')
        self._data["Free Convection Capacity"] = value

    @property
    def free_convection_nominal_capacity_sizing_factor(self):
        """Get free_convection_nominal_capacity_sizing_factor

        Returns:
            float: the value of `free_convection_nominal_capacity_sizing_factor` or None if not set
        """
        return self._data["Free Convection Nominal Capacity Sizing Factor"]

    @free_convection_nominal_capacity_sizing_factor.setter
    def free_convection_nominal_capacity_sizing_factor(self, value=0.1):
        """  Corresponds to IDD Field `Free Convection Nominal Capacity Sizing Factor`
        This field is only used if the previous field is set to autocalculate

        Args:
            value (float): value for IDD Field `Free Convection Nominal Capacity Sizing Factor`
                Default value: 0.1
                value > 0.0
                value < 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `free_convection_nominal_capacity_sizing_factor`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `free_convection_nominal_capacity_sizing_factor`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `free_convection_nominal_capacity_sizing_factor`')
        self._data["Free Convection Nominal Capacity Sizing Factor"] = value

    @property
    def basin_heater_capacity(self):
        """Get basin_heater_capacity

        Returns:
            float: the value of `basin_heater_capacity` or None if not set
        """
        return self._data["Basin Heater Capacity"]

    @basin_heater_capacity.setter
    def basin_heater_capacity(self, value=0.0):
        """  Corresponds to IDD Field `Basin Heater Capacity`
        This heater maintains the basin water temperature at the basin heater setpoint
        temperature when the outdoor air temperature falls below the setpoint temperature.
        The basin heater only operates when water is not flowing through the tower.

        Args:
            value (float): value for IDD Field `Basin Heater Capacity`
                Units: W/K
                Default value: 0.0
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `basin_heater_capacity`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `basin_heater_capacity`')
        self._data["Basin Heater Capacity"] = value

    @property
    def basin_heater_setpoint_temperature(self):
        """Get basin_heater_setpoint_temperature

        Returns:
            float: the value of `basin_heater_setpoint_temperature` or None if not set
        """
        return self._data["Basin Heater Setpoint Temperature"]

    @basin_heater_setpoint_temperature.setter
    def basin_heater_setpoint_temperature(self, value=2.0):
        """  Corresponds to IDD Field `Basin Heater Setpoint Temperature`
        Enter the outdoor dry-bulb temperature when the basin heater turns on

        Args:
            value (float): value for IDD Field `Basin Heater Setpoint Temperature`
                Units: C
                Default value: 2.0
                value >= 2.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `basin_heater_setpoint_temperature`'.format(value))
            if value < 2.0:
                raise ValueError('value need to be greater or equal 2.0 '
                                 'for field `basin_heater_setpoint_temperature`')
        self._data["Basin Heater Setpoint Temperature"] = value

    @property
    def basin_heater_operating_schedule_name(self):
        """Get basin_heater_operating_schedule_name

        Returns:
            str: the value of `basin_heater_operating_schedule_name` or None if not set
        """
        return self._data["Basin Heater Operating Schedule Name"]

    @basin_heater_operating_schedule_name.setter
    def basin_heater_operating_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Basin Heater Operating Schedule Name`
        Schedule values greater than 0 allow the basin heater to operate whenever the outdoor
        air dry-bulb temperature is below the basin heater setpoint temperature.
        If a schedule name is not entered, the basin heater is allowed to operate
        throughout the entire simulation.

        Args:
            value (str): value for IDD Field `Basin Heater Operating Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `basin_heater_operating_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `basin_heater_operating_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `basin_heater_operating_schedule_name`')
        self._data["Basin Heater Operating Schedule Name"] = value

    @property
    def evaporation_loss_mode(self):
        """Get evaporation_loss_mode

        Returns:
            str: the value of `evaporation_loss_mode` or None if not set
        """
        return self._data["Evaporation Loss Mode"]

    @evaporation_loss_mode.setter
    def evaporation_loss_mode(self, value=None):
        """  Corresponds to IDD Field `Evaporation Loss Mode`

        Args:
            value (str): value for IDD Field `Evaporation Loss Mode`
                Accepted values are:
                      - LossFactor
                      - SaturatedExit
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `evaporation_loss_mode`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `evaporation_loss_mode`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `evaporation_loss_mode`')
            vals = {}
            vals["lossfactor"] = "LossFactor"
            vals["saturatedexit"] = "SaturatedExit"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `evaporation_loss_mode`'.format(value))
            value = vals[value_lower]
        self._data["Evaporation Loss Mode"] = value

    @property
    def evaporation_loss_factor(self):
        """Get evaporation_loss_factor

        Returns:
            float: the value of `evaporation_loss_factor` or None if not set
        """
        return self._data["Evaporation Loss Factor"]

    @evaporation_loss_factor.setter
    def evaporation_loss_factor(self, value=0.2):
        """  Corresponds to IDD Field `Evaporation Loss Factor`
        Rate of water evaporation from the cooling tower and lost to the outdoor air [%/K]
        Evaporation loss is calculated as percentage of the circulating condenser water rate
        Value entered here is percent-per-degree K of temperature drop in the condenser water
        Typical values are from 0.15 to 0.27 [%/K].

        Args:
            value (float): value for IDD Field `Evaporation Loss Factor`
                Units: percent/K
                Default value: 0.2
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `evaporation_loss_factor`'.format(value))
        self._data["Evaporation Loss Factor"] = value

    @property
    def drift_loss_percent(self):
        """Get drift_loss_percent

        Returns:
            float: the value of `drift_loss_percent` or None if not set
        """
        return self._data["Drift Loss Percent"]

    @drift_loss_percent.setter
    def drift_loss_percent(self, value=0.008):
        """  Corresponds to IDD Field `Drift Loss Percent`
        Rate of drift loss as a percentage of circulating condenser water flow rate
        Typical values are between 0.002 and 0.2% The default value is 0.008%

        Args:
            value (float): value for IDD Field `Drift Loss Percent`
                Units: percent
                Default value: 0.008
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `drift_loss_percent`'.format(value))
        self._data["Drift Loss Percent"] = value

    @property
    def blowdown_calculation_mode(self):
        """Get blowdown_calculation_mode

        Returns:
            str: the value of `blowdown_calculation_mode` or None if not set
        """
        return self._data["Blowdown Calculation Mode"]

    @blowdown_calculation_mode.setter
    def blowdown_calculation_mode(self, value=None):
        """  Corresponds to IDD Field `Blowdown Calculation Mode`

        Args:
            value (str): value for IDD Field `Blowdown Calculation Mode`
                Accepted values are:
                      - ConcentrationRatio
                      - ScheduledRate
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `blowdown_calculation_mode`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `blowdown_calculation_mode`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `blowdown_calculation_mode`')
            vals = {}
            vals["concentrationratio"] = "ConcentrationRatio"
            vals["scheduledrate"] = "ScheduledRate"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `blowdown_calculation_mode`'.format(value))
            value = vals[value_lower]
        self._data["Blowdown Calculation Mode"] = value

    @property
    def blowdown_concentration_ratio(self):
        """Get blowdown_concentration_ratio

        Returns:
            float: the value of `blowdown_concentration_ratio` or None if not set
        """
        return self._data["Blowdown Concentration Ratio"]

    @blowdown_concentration_ratio.setter
    def blowdown_concentration_ratio(self, value=3.0):
        """  Corresponds to IDD Field `Blowdown Concentration Ratio`
        Characterizes the rate of blowdown in the cooling tower.
        Blowdown is water intentionally drained from the tower in order to offset the build up
        of solids in the water that would otherwise occur because of evaporation.
        Ratio of solids in the blowdown water to solids in the make up water.
        Typical values for tower operation are 3 to 5.  The default value is 3.

        Args:
            value (float): value for IDD Field `Blowdown Concentration Ratio`
                Default value: 3.0
                value >= 2.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `blowdown_concentration_ratio`'.format(value))
            if value < 2.0:
                raise ValueError('value need to be greater or equal 2.0 '
                                 'for field `blowdown_concentration_ratio`')
        self._data["Blowdown Concentration Ratio"] = value

    @property
    def blowdown_makeup_water_usage_schedule_name(self):
        """Get blowdown_makeup_water_usage_schedule_name

        Returns:
            str: the value of `blowdown_makeup_water_usage_schedule_name` or None if not set
        """
        return self._data["Blowdown Makeup Water Usage Schedule Name"]

    @blowdown_makeup_water_usage_schedule_name.setter
    def blowdown_makeup_water_usage_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Blowdown Makeup Water Usage Schedule Name`
        Makeup water usage due to blowdown results from occasionally draining a small amount
        of water in the tower basin to purge scale or other contaminants to reduce their
        concentration in order to maintain an acceptable level of water quality.
        Schedule values should reflect water usage in m3/s.

        Args:
            value (str): value for IDD Field `Blowdown Makeup Water Usage Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `blowdown_makeup_water_usage_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `blowdown_makeup_water_usage_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `blowdown_makeup_water_usage_schedule_name`')
        self._data["Blowdown Makeup Water Usage Schedule Name"] = value

    @property
    def supply_water_storage_tank_name(self):
        """Get supply_water_storage_tank_name

        Returns:
            str: the value of `supply_water_storage_tank_name` or None if not set
        """
        return self._data["Supply Water Storage Tank Name"]

    @supply_water_storage_tank_name.setter
    def supply_water_storage_tank_name(self, value=None):
        """  Corresponds to IDD Field `Supply Water Storage Tank Name`

        Args:
            value (str): value for IDD Field `Supply Water Storage Tank Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_water_storage_tank_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_water_storage_tank_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `supply_water_storage_tank_name`')
        self._data["Supply Water Storage Tank Name"] = value

    @property
    def outdoor_air_inlet_node_name(self):
        """Get outdoor_air_inlet_node_name

        Returns:
            str: the value of `outdoor_air_inlet_node_name` or None if not set
        """
        return self._data["Outdoor Air Inlet Node Name"]

    @outdoor_air_inlet_node_name.setter
    def outdoor_air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Outdoor Air Inlet Node Name`
        Enter the name of an outdoor air node

        Args:
            value (str): value for IDD Field `Outdoor Air Inlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `outdoor_air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outdoor_air_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `outdoor_air_inlet_node_name`')
        self._data["Outdoor Air Inlet Node Name"] = value

    @property
    def capacity_control(self):
        """Get capacity_control

        Returns:
            str: the value of `capacity_control` or None if not set
        """
        return self._data["Capacity Control"]

    @capacity_control.setter
    def capacity_control(self, value="FanCycling"):
        """  Corresponds to IDD Field `Capacity Control`

        Args:
            value (str): value for IDD Field `Capacity Control`
                Accepted values are:
                      - FanCycling
                      - FluidBypass
                Default value: FanCycling
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `capacity_control`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `capacity_control`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `capacity_control`')
            vals = {}
            vals["fancycling"] = "FanCycling"
            vals["fluidbypass"] = "FluidBypass"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `capacity_control`'.format(value))
            value = vals[value_lower]
        self._data["Capacity Control"] = value

    @property
    def number_of_cells(self):
        """Get number_of_cells

        Returns:
            int: the value of `number_of_cells` or None if not set
        """
        return self._data["Number of Cells"]

    @number_of_cells.setter
    def number_of_cells(self, value=1):
        """  Corresponds to IDD Field `Number of Cells`

        Args:
            value (int): value for IDD Field `Number of Cells`
                Default value: 1
                value >= 1
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = int(value)
            except ValueError:
                raise ValueError('value {} need to be of type int '
                                 'for field `number_of_cells`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `number_of_cells`')
        self._data["Number of Cells"] = value

    @property
    def cell_control(self):
        """Get cell_control

        Returns:
            str: the value of `cell_control` or None if not set
        """
        return self._data["Cell Control"]

    @cell_control.setter
    def cell_control(self, value="MinimalCell"):
        """  Corresponds to IDD Field `Cell Control`

        Args:
            value (str): value for IDD Field `Cell Control`
                Default value: MinimalCell
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `cell_control`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `cell_control`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `cell_control`')
        self._data["Cell Control"] = value

    @property
    def cell_minimum_water_flow_rate_fraction(self):
        """Get cell_minimum_water_flow_rate_fraction

        Returns:
            float: the value of `cell_minimum_water_flow_rate_fraction` or None if not set
        """
        return self._data["Cell Minimum  Water Flow Rate Fraction"]

    @cell_minimum_water_flow_rate_fraction.setter
    def cell_minimum_water_flow_rate_fraction(self, value=0.33):
        """  Corresponds to IDD Field `Cell Minimum  Water Flow Rate Fraction`
        The allowable minimal fraction of the nominal flow rate per cell

        Args:
            value (float): value for IDD Field `Cell Minimum  Water Flow Rate Fraction`
                Default value: 0.33
                value > 0.0
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `cell_minimum_water_flow_rate_fraction`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `cell_minimum_water_flow_rate_fraction`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `cell_minimum_water_flow_rate_fraction`')
        self._data["Cell Minimum  Water Flow Rate Fraction"] = value

    @property
    def cell_maximum_water_flow_rate_fraction(self):
        """Get cell_maximum_water_flow_rate_fraction

        Returns:
            float: the value of `cell_maximum_water_flow_rate_fraction` or None if not set
        """
        return self._data["Cell Maximum Water Flow Rate Fraction"]

    @cell_maximum_water_flow_rate_fraction.setter
    def cell_maximum_water_flow_rate_fraction(self, value=2.5):
        """  Corresponds to IDD Field `Cell Maximum Water Flow Rate Fraction`
        The allowable maximal fraction of the nominal flow rate per cell

        Args:
            value (float): value for IDD Field `Cell Maximum Water Flow Rate Fraction`
                Default value: 2.5
                value >= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `cell_maximum_water_flow_rate_fraction`'.format(value))
            if value < 1.0:
                raise ValueError('value need to be greater or equal 1.0 '
                                 'for field `cell_maximum_water_flow_rate_fraction`')
        self._data["Cell Maximum Water Flow Rate Fraction"] = value

    @property
    def sizing_factor(self):
        """Get sizing_factor

        Returns:
            float: the value of `sizing_factor` or None if not set
        """
        return self._data["Sizing Factor"]

    @sizing_factor.setter
    def sizing_factor(self, value=1.0):
        """  Corresponds to IDD Field `Sizing Factor`
        Multiplies the autosized capacity and flow rates

        Args:
            value (float): value for IDD Field `Sizing Factor`
                Default value: 1.0
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `sizing_factor`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `sizing_factor`')
        self._data["Sizing Factor"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
        return good

    @classmethod
    def _to_str(cls, value):
        """ Represents values either as string or None values as empty string

        Args:
            value: a value
        """
        if value is None:
            return ''
        else:
            return str(value)

    def export(self):
        """ Export values of data object as list of strings"""
        out = []
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class CoolingTowerTwoSpeed(object):
    """ Corresponds to IDD object `CoolingTower:TwoSpeed`
        This tower model is based on Merkel's theory, which is also the basis
        for the tower model in ASHRAE's HVAC1 Toolkit. The closed-circuit cooling tower
        is modeled as a counter flow heat exchanger with a two-speed fan drawing air
        through the tower (induced-draft configuration).
        For a multi-cell tower, the capacity and air/water flow rate inputs are for the entire tower.
    
    """
    internal_name = "CoolingTower:TwoSpeed"
    field_count = 40
    required_fields = ["Name", "Water Inlet Node Name", "Water Outlet Node Name", "High Fan Speed Air Flow Rate", "High Fan Speed Fan Power", "Low Fan Speed Air Flow Rate", "Low Fan Speed Air Flow Rate Sizing Factor", "Low Fan Speed Fan Power", "Low Fan Speed Fan Power Sizing Factor", "Low Fan Speed U-Factor Times Area Sizing Factor", "Free Convection Regime Air Flow Rate Sizing Factor", "Free Convection U-Factor Times Area Value Sizing Factor", "Heat Rejection Capacity and Nominal Capacity Sizing Ratio", "Low Speed Nominal Capacity Sizing Factor", "Free Convection Nominal Capacity Sizing Factor"]

    def __init__(self):
        """ Init data dictionary object for IDD  `CoolingTower:TwoSpeed`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Water Inlet Node Name"] = None
        self._data["Water Outlet Node Name"] = None
        self._data["Design Water Flow Rate"] = None
        self._data["High Fan Speed Air Flow Rate"] = None
        self._data["High Fan Speed Fan Power"] = None
        self._data["High Fan Speed U-Factor Times Area Value"] = None
        self._data["Low Fan Speed Air Flow Rate"] = None
        self._data["Low Fan Speed Air Flow Rate Sizing Factor"] = None
        self._data["Low Fan Speed Fan Power"] = None
        self._data["Low Fan Speed Fan Power Sizing Factor"] = None
        self._data["Low Fan Speed U-Factor Times Area Value"] = None
        self._data["Low Fan Speed U-Factor Times Area Sizing Factor"] = None
        self._data["Free Convection Regime Air Flow Rate"] = None
        self._data["Free Convection Regime Air Flow Rate Sizing Factor"] = None
        self._data["Free Convection Regime U-Factor Times Area Value"] = None
        self._data["Free Convection U-Factor Times Area Value Sizing Factor"] = None
        self._data["Performance Input Method"] = None
        self._data["Heat Rejection Capacity and Nominal Capacity Sizing Ratio"] = None
        self._data["High Speed Nominal Capacity"] = None
        self._data["Low Speed Nominal Capacity"] = None
        self._data["Low Speed Nominal Capacity Sizing Factor"] = None
        self._data["Free Convection Nominal Capacity"] = None
        self._data["Free Convection Nominal Capacity Sizing Factor"] = None
        self._data["Basin Heater Capacity"] = None
        self._data["Basin Heater Setpoint Temperature"] = None
        self._data["Basin Heater Operating Schedule Name"] = None
        self._data["Evaporation Loss Mode"] = None
        self._data["Evaporation Loss Factor"] = None
        self._data["Drift Loss Percent"] = None
        self._data["Blowdown Calculation Mode"] = None
        self._data["Blowdown Concentration Ratio"] = None
        self._data["Blowdown Makeup Water Usage Schedule Name"] = None
        self._data["Supply Water Storage Tank Name"] = None
        self._data["Outdoor Air Inlet Node Name"] = None
        self._data["Number of Cells"] = None
        self._data["Cell Control"] = None
        self._data["Cell Minimum  Water Flow Rate Fraction"] = None
        self._data["Cell Maximum Water Flow Rate Fraction"] = None
        self._data["Sizing Factor"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.water_inlet_node_name = None
        else:
            self.water_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.water_outlet_node_name = None
        else:
            self.water_outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_water_flow_rate = None
        else:
            self.design_water_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.high_fan_speed_air_flow_rate = None
        else:
            self.high_fan_speed_air_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.high_fan_speed_fan_power = None
        else:
            self.high_fan_speed_fan_power = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.high_fan_speed_ufactor_times_area_value = None
        else:
            self.high_fan_speed_ufactor_times_area_value = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.low_fan_speed_air_flow_rate = None
        else:
            self.low_fan_speed_air_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.low_fan_speed_air_flow_rate_sizing_factor = None
        else:
            self.low_fan_speed_air_flow_rate_sizing_factor = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.low_fan_speed_fan_power = None
        else:
            self.low_fan_speed_fan_power = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.low_fan_speed_fan_power_sizing_factor = None
        else:
            self.low_fan_speed_fan_power_sizing_factor = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.low_fan_speed_ufactor_times_area_value = None
        else:
            self.low_fan_speed_ufactor_times_area_value = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.low_fan_speed_ufactor_times_area_sizing_factor = None
        else:
            self.low_fan_speed_ufactor_times_area_sizing_factor = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.free_convection_regime_air_flow_rate = None
        else:
            self.free_convection_regime_air_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.free_convection_regime_air_flow_rate_sizing_factor = None
        else:
            self.free_convection_regime_air_flow_rate_sizing_factor = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.free_convection_regime_ufactor_times_area_value = None
        else:
            self.free_convection_regime_ufactor_times_area_value = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.free_convection_ufactor_times_area_value_sizing_factor = None
        else:
            self.free_convection_ufactor_times_area_value_sizing_factor = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.performance_input_method = None
        else:
            self.performance_input_method = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heat_rejection_capacity_and_nominal_capacity_sizing_ratio = None
        else:
            self.heat_rejection_capacity_and_nominal_capacity_sizing_ratio = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.high_speed_nominal_capacity = None
        else:
            self.high_speed_nominal_capacity = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.low_speed_nominal_capacity = None
        else:
            self.low_speed_nominal_capacity = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.low_speed_nominal_capacity_sizing_factor = None
        else:
            self.low_speed_nominal_capacity_sizing_factor = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.free_convection_nominal_capacity = None
        else:
            self.free_convection_nominal_capacity = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.free_convection_nominal_capacity_sizing_factor = None
        else:
            self.free_convection_nominal_capacity_sizing_factor = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.basin_heater_capacity = None
        else:
            self.basin_heater_capacity = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.basin_heater_setpoint_temperature = None
        else:
            self.basin_heater_setpoint_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.basin_heater_operating_schedule_name = None
        else:
            self.basin_heater_operating_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.evaporation_loss_mode = None
        else:
            self.evaporation_loss_mode = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.evaporation_loss_factor = None
        else:
            self.evaporation_loss_factor = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.drift_loss_percent = None
        else:
            self.drift_loss_percent = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.blowdown_calculation_mode = None
        else:
            self.blowdown_calculation_mode = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.blowdown_concentration_ratio = None
        else:
            self.blowdown_concentration_ratio = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.blowdown_makeup_water_usage_schedule_name = None
        else:
            self.blowdown_makeup_water_usage_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.supply_water_storage_tank_name = None
        else:
            self.supply_water_storage_tank_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outdoor_air_inlet_node_name = None
        else:
            self.outdoor_air_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.number_of_cells = None
        else:
            self.number_of_cells = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cell_control = None
        else:
            self.cell_control = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cell_minimum_water_flow_rate_fraction = None
        else:
            self.cell_minimum_water_flow_rate_fraction = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cell_maximum_water_flow_rate_fraction = None
        else:
            self.cell_maximum_water_flow_rate_fraction = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.sizing_factor = None
        else:
            self.sizing_factor = vals[i]
        i += 1
        if i >= len(vals):
            return

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `Name`
        Tower Name

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')
        self._data["Name"] = value

    @property
    def water_inlet_node_name(self):
        """Get water_inlet_node_name

        Returns:
            str: the value of `water_inlet_node_name` or None if not set
        """
        return self._data["Water Inlet Node Name"]

    @water_inlet_node_name.setter
    def water_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Water Inlet Node Name`
        Name of tower Water Inlet Node

        Args:
            value (str): value for IDD Field `Water Inlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `water_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `water_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `water_inlet_node_name`')
        self._data["Water Inlet Node Name"] = value

    @property
    def water_outlet_node_name(self):
        """Get water_outlet_node_name

        Returns:
            str: the value of `water_outlet_node_name` or None if not set
        """
        return self._data["Water Outlet Node Name"]

    @water_outlet_node_name.setter
    def water_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Water Outlet Node Name`
        Name of tower Water Outlet Node

        Args:
            value (str): value for IDD Field `Water Outlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `water_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `water_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `water_outlet_node_name`')
        self._data["Water Outlet Node Name"] = value

    @property
    def design_water_flow_rate(self):
        """Get design_water_flow_rate

        Returns:
            float: the value of `design_water_flow_rate` or None if not set
        """
        return self._data["Design Water Flow Rate"]

    @design_water_flow_rate.setter
    def design_water_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Design Water Flow Rate`
        Leave field blank if Tower Performance Input Method is NominalCapacity

        Args:
            value (float or "Autosize"): value for IDD Field `Design Water Flow Rate`
                Units: m3/s
                IP-Units: gal/min
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Design Water Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `design_water_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `design_water_flow_rate`')
        self._data["Design Water Flow Rate"] = value

    @property
    def high_fan_speed_air_flow_rate(self):
        """Get high_fan_speed_air_flow_rate

        Returns:
            float: the value of `high_fan_speed_air_flow_rate` or None if not set
        """
        return self._data["High Fan Speed Air Flow Rate"]

    @high_fan_speed_air_flow_rate.setter
    def high_fan_speed_air_flow_rate(self, value=None):
        """  Corresponds to IDD Field `High Fan Speed Air Flow Rate`

        Args:
            value (float or "Autosize"): value for IDD Field `High Fan Speed Air Flow Rate`
                Units: m3/s
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["High Fan Speed Air Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `high_fan_speed_air_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `high_fan_speed_air_flow_rate`')
        self._data["High Fan Speed Air Flow Rate"] = value

    @property
    def high_fan_speed_fan_power(self):
        """Get high_fan_speed_fan_power

        Returns:
            float: the value of `high_fan_speed_fan_power` or None if not set
        """
        return self._data["High Fan Speed Fan Power"]

    @high_fan_speed_fan_power.setter
    def high_fan_speed_fan_power(self, value=None):
        """  Corresponds to IDD Field `High Fan Speed Fan Power`
        This is the fan motor electric input power at high speed

        Args:
            value (float or "Autosize"): value for IDD Field `High Fan Speed Fan Power`
                Units: W
                IP-Units: W
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["High Fan Speed Fan Power"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `high_fan_speed_fan_power`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `high_fan_speed_fan_power`')
        self._data["High Fan Speed Fan Power"] = value

    @property
    def high_fan_speed_ufactor_times_area_value(self):
        """Get high_fan_speed_ufactor_times_area_value

        Returns:
            float: the value of `high_fan_speed_ufactor_times_area_value` or None if not set
        """
        return self._data["High Fan Speed U-Factor Times Area Value"]

    @high_fan_speed_ufactor_times_area_value.setter
    def high_fan_speed_ufactor_times_area_value(self, value=None):
        """  Corresponds to IDD Field `High Fan Speed U-Factor Times Area Value`
        Leave field blank if Tower Performance Input Method is NominalCapacity

        Args:
            value (float or "Autosize"): value for IDD Field `High Fan Speed U-Factor Times Area Value`
                Units: W/K
                value > 0.0
                value <= 2100000.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["High Fan Speed U-Factor Times Area Value"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `high_fan_speed_ufactor_times_area_value`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `high_fan_speed_ufactor_times_area_value`')
            if value > 2100000.0:
                raise ValueError('value need to be smaller 2100000.0 '
                                 'for field `high_fan_speed_ufactor_times_area_value`')
        self._data["High Fan Speed U-Factor Times Area Value"] = value

    @property
    def low_fan_speed_air_flow_rate(self):
        """Get low_fan_speed_air_flow_rate

        Returns:
            float: the value of `low_fan_speed_air_flow_rate` or None if not set
        """
        return self._data["Low Fan Speed Air Flow Rate"]

    @low_fan_speed_air_flow_rate.setter
    def low_fan_speed_air_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Low Fan Speed Air Flow Rate`
        Low speed air flow rate must be less than high speed air flow rate
        Low speed air flow rate must be greater than free convection air flow rate

        Args:
            value (float or "Autocalculate"): value for IDD Field `Low Fan Speed Air Flow Rate`
                Units: m3/s
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autocalculate":
                    self._data["Low Fan Speed Air Flow Rate"] = "Autocalculate"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `low_fan_speed_air_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `low_fan_speed_air_flow_rate`')
        self._data["Low Fan Speed Air Flow Rate"] = value

    @property
    def low_fan_speed_air_flow_rate_sizing_factor(self):
        """Get low_fan_speed_air_flow_rate_sizing_factor

        Returns:
            float: the value of `low_fan_speed_air_flow_rate_sizing_factor` or None if not set
        """
        return self._data["Low Fan Speed Air Flow Rate Sizing Factor"]

    @low_fan_speed_air_flow_rate_sizing_factor.setter
    def low_fan_speed_air_flow_rate_sizing_factor(self, value=0.5):
        """  Corresponds to IDD Field `Low Fan Speed Air Flow Rate Sizing Factor`
        This field is only used if the previous field is set to autocalculate.

        Args:
            value (float): value for IDD Field `Low Fan Speed Air Flow Rate Sizing Factor`
                Default value: 0.5
                value > 0.0
                value < 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `low_fan_speed_air_flow_rate_sizing_factor`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `low_fan_speed_air_flow_rate_sizing_factor`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `low_fan_speed_air_flow_rate_sizing_factor`')
        self._data["Low Fan Speed Air Flow Rate Sizing Factor"] = value

    @property
    def low_fan_speed_fan_power(self):
        """Get low_fan_speed_fan_power

        Returns:
            float: the value of `low_fan_speed_fan_power` or None if not set
        """
        return self._data["Low Fan Speed Fan Power"]

    @low_fan_speed_fan_power.setter
    def low_fan_speed_fan_power(self, value=None):
        """  Corresponds to IDD Field `Low Fan Speed Fan Power`
        This is the fan motor electric input power at low speed

        Args:
            value (float or "Autocalculate"): value for IDD Field `Low Fan Speed Fan Power`
                Units: W
                IP-Units: W
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autocalculate":
                    self._data["Low Fan Speed Fan Power"] = "Autocalculate"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `low_fan_speed_fan_power`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `low_fan_speed_fan_power`')
        self._data["Low Fan Speed Fan Power"] = value

    @property
    def low_fan_speed_fan_power_sizing_factor(self):
        """Get low_fan_speed_fan_power_sizing_factor

        Returns:
            float: the value of `low_fan_speed_fan_power_sizing_factor` or None if not set
        """
        return self._data["Low Fan Speed Fan Power Sizing Factor"]

    @low_fan_speed_fan_power_sizing_factor.setter
    def low_fan_speed_fan_power_sizing_factor(self, value=0.16):
        """  Corresponds to IDD Field `Low Fan Speed Fan Power Sizing Factor`
        This field is only used if the previous field is set to autocalculate.

        Args:
            value (float): value for IDD Field `Low Fan Speed Fan Power Sizing Factor`
                Default value: 0.16
                value > 0.0
                value < 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `low_fan_speed_fan_power_sizing_factor`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `low_fan_speed_fan_power_sizing_factor`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `low_fan_speed_fan_power_sizing_factor`')
        self._data["Low Fan Speed Fan Power Sizing Factor"] = value

    @property
    def low_fan_speed_ufactor_times_area_value(self):
        """Get low_fan_speed_ufactor_times_area_value

        Returns:
            float: the value of `low_fan_speed_ufactor_times_area_value` or None if not set
        """
        return self._data["Low Fan Speed U-Factor Times Area Value"]

    @low_fan_speed_ufactor_times_area_value.setter
    def low_fan_speed_ufactor_times_area_value(self, value=None):
        """  Corresponds to IDD Field `Low Fan Speed U-Factor Times Area Value`
        Leave field blank if tower Performance Input Method is NominalCapacity
        Low speed tower UA must be less than high speed tower UA
        Low speed tower UA must be greater than free convection tower UA

        Args:
            value (float or "Autocalculate"): value for IDD Field `Low Fan Speed U-Factor Times Area Value`
                Units: W/K
                value > 0.0
                value <= 300000.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autocalculate":
                    self._data["Low Fan Speed U-Factor Times Area Value"] = "Autocalculate"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `low_fan_speed_ufactor_times_area_value`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `low_fan_speed_ufactor_times_area_value`')
            if value > 300000.0:
                raise ValueError('value need to be smaller 300000.0 '
                                 'for field `low_fan_speed_ufactor_times_area_value`')
        self._data["Low Fan Speed U-Factor Times Area Value"] = value

    @property
    def low_fan_speed_ufactor_times_area_sizing_factor(self):
        """Get low_fan_speed_ufactor_times_area_sizing_factor

        Returns:
            float: the value of `low_fan_speed_ufactor_times_area_sizing_factor` or None if not set
        """
        return self._data["Low Fan Speed U-Factor Times Area Sizing Factor"]

    @low_fan_speed_ufactor_times_area_sizing_factor.setter
    def low_fan_speed_ufactor_times_area_sizing_factor(self, value=0.6):
        """  Corresponds to IDD Field `Low Fan Speed U-Factor Times Area Sizing Factor`
        This field is only used if the previous field is set to autocalculate and
        the Performance Input Method is UFactorTimesAreaAndDesignWaterFlowRate

        Args:
            value (float): value for IDD Field `Low Fan Speed U-Factor Times Area Sizing Factor`
                Default value: 0.6
                value > 0.0
                value < 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `low_fan_speed_ufactor_times_area_sizing_factor`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `low_fan_speed_ufactor_times_area_sizing_factor`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `low_fan_speed_ufactor_times_area_sizing_factor`')
        self._data["Low Fan Speed U-Factor Times Area Sizing Factor"] = value

    @property
    def free_convection_regime_air_flow_rate(self):
        """Get free_convection_regime_air_flow_rate

        Returns:
            float: the value of `free_convection_regime_air_flow_rate` or None if not set
        """
        return self._data["Free Convection Regime Air Flow Rate"]

    @free_convection_regime_air_flow_rate.setter
    def free_convection_regime_air_flow_rate(self, value=0.0):
        """  Corresponds to IDD Field `Free Convection Regime Air Flow Rate`

        Args:
            value (float or "Autocalculate"): value for IDD Field `Free Convection Regime Air Flow Rate`
                Units: m3/s
                Default value: 0.0
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autocalculate":
                    self._data["Free Convection Regime Air Flow Rate"] = "Autocalculate"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `free_convection_regime_air_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `free_convection_regime_air_flow_rate`')
        self._data["Free Convection Regime Air Flow Rate"] = value

    @property
    def free_convection_regime_air_flow_rate_sizing_factor(self):
        """Get free_convection_regime_air_flow_rate_sizing_factor

        Returns:
            float: the value of `free_convection_regime_air_flow_rate_sizing_factor` or None if not set
        """
        return self._data["Free Convection Regime Air Flow Rate Sizing Factor"]

    @free_convection_regime_air_flow_rate_sizing_factor.setter
    def free_convection_regime_air_flow_rate_sizing_factor(self, value=0.1):
        """  Corresponds to IDD Field `Free Convection Regime Air Flow Rate Sizing Factor`
        This field is only used if the previous field is set to autocalculate.

        Args:
            value (float): value for IDD Field `Free Convection Regime Air Flow Rate Sizing Factor`
                Default value: 0.1
                value > 0.0
                value < 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `free_convection_regime_air_flow_rate_sizing_factor`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `free_convection_regime_air_flow_rate_sizing_factor`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `free_convection_regime_air_flow_rate_sizing_factor`')
        self._data["Free Convection Regime Air Flow Rate Sizing Factor"] = value

    @property
    def free_convection_regime_ufactor_times_area_value(self):
        """Get free_convection_regime_ufactor_times_area_value

        Returns:
            float: the value of `free_convection_regime_ufactor_times_area_value` or None if not set
        """
        return self._data["Free Convection Regime U-Factor Times Area Value"]

    @free_convection_regime_ufactor_times_area_value.setter
    def free_convection_regime_ufactor_times_area_value(self, value=0.0):
        """  Corresponds to IDD Field `Free Convection Regime U-Factor Times Area Value`
        Leave field blank if Tower Performance Input Method is NominalCapacity

        Args:
            value (float or "Autocalculate"): value for IDD Field `Free Convection Regime U-Factor Times Area Value`
                Units: W/K
                Default value: 0.0
                value >= 0.0
                value <= 300000.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autocalculate":
                    self._data["Free Convection Regime U-Factor Times Area Value"] = "Autocalculate"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `free_convection_regime_ufactor_times_area_value`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `free_convection_regime_ufactor_times_area_value`')
            if value > 300000.0:
                raise ValueError('value need to be smaller 300000.0 '
                                 'for field `free_convection_regime_ufactor_times_area_value`')
        self._data["Free Convection Regime U-Factor Times Area Value"] = value

    @property
    def free_convection_ufactor_times_area_value_sizing_factor(self):
        """Get free_convection_ufactor_times_area_value_sizing_factor

        Returns:
            float: the value of `free_convection_ufactor_times_area_value_sizing_factor` or None if not set
        """
        return self._data["Free Convection U-Factor Times Area Value Sizing Factor"]

    @free_convection_ufactor_times_area_value_sizing_factor.setter
    def free_convection_ufactor_times_area_value_sizing_factor(self, value=0.1):
        """  Corresponds to IDD Field `Free Convection U-Factor Times Area Value Sizing Factor`
        This field is only used if the previous field is set to autocalculate and
        the Performance Input Method is UFactorTimesAreaAndDesignWaterFlowRate

        Args:
            value (float): value for IDD Field `Free Convection U-Factor Times Area Value Sizing Factor`
                Default value: 0.1
                value > 0.0
                value < 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `free_convection_ufactor_times_area_value_sizing_factor`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `free_convection_ufactor_times_area_value_sizing_factor`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `free_convection_ufactor_times_area_value_sizing_factor`')
        self._data["Free Convection U-Factor Times Area Value Sizing Factor"] = value

    @property
    def performance_input_method(self):
        """Get performance_input_method

        Returns:
            str: the value of `performance_input_method` or None if not set
        """
        return self._data["Performance Input Method"]

    @performance_input_method.setter
    def performance_input_method(self, value="UFactorTimesAreaAndDesignWaterFlowRate"):
        """  Corresponds to IDD Field `Performance Input Method`
        User can define tower thermal performance by specifying the tower UA,
        the Design Air Flow Rate and the Design Water Flow Rate,
        or by specifying the tower nominal capacity

        Args:
            value (str): value for IDD Field `Performance Input Method`
                Default value: UFactorTimesAreaAndDesignWaterFlowRate
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `performance_input_method`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `performance_input_method`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `performance_input_method`')
        self._data["Performance Input Method"] = value

    @property
    def heat_rejection_capacity_and_nominal_capacity_sizing_ratio(self):
        """Get heat_rejection_capacity_and_nominal_capacity_sizing_ratio

        Returns:
            float: the value of `heat_rejection_capacity_and_nominal_capacity_sizing_ratio` or None if not set
        """
        return self._data["Heat Rejection Capacity and Nominal Capacity Sizing Ratio"]

    @heat_rejection_capacity_and_nominal_capacity_sizing_ratio.setter
    def heat_rejection_capacity_and_nominal_capacity_sizing_ratio(self, value=1.25):
        """  Corresponds to IDD Field `Heat Rejection Capacity and Nominal Capacity Sizing Ratio`

        Args:
            value (float): value for IDD Field `Heat Rejection Capacity and Nominal Capacity Sizing Ratio`
                Default value: 1.25
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `heat_rejection_capacity_and_nominal_capacity_sizing_ratio`'.format(value))
        self._data["Heat Rejection Capacity and Nominal Capacity Sizing Ratio"] = value

    @property
    def high_speed_nominal_capacity(self):
        """Get high_speed_nominal_capacity

        Returns:
            float: the value of `high_speed_nominal_capacity` or None if not set
        """
        return self._data["High Speed Nominal Capacity"]

    @high_speed_nominal_capacity.setter
    def high_speed_nominal_capacity(self, value=None):
        """  Corresponds to IDD Field `High Speed Nominal Capacity`
        Nominal tower capacity with entering water at 35C (95F), leaving water at
        29.44C (85F), entering air at 25.56C (78F) wet-bulb temperature and 35C (95F)
        dry-bulb temperature, with the tower fan operating at high speed. Design water
        flow rate assumed to be 5.382E-8 m3/s per watt(3 gpm/ton). Nominal tower capacity
        times the Heat Rejection Capacity and Nominal Capacity Sizing Ratio (e.g. 1.25)
        gives the actual tower heat rejection at these operating conditions.

        Args:
            value (float): value for IDD Field `High Speed Nominal Capacity`
                Units: W
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `high_speed_nominal_capacity`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `high_speed_nominal_capacity`')
        self._data["High Speed Nominal Capacity"] = value

    @property
    def low_speed_nominal_capacity(self):
        """Get low_speed_nominal_capacity

        Returns:
            float: the value of `low_speed_nominal_capacity` or None if not set
        """
        return self._data["Low Speed Nominal Capacity"]

    @low_speed_nominal_capacity.setter
    def low_speed_nominal_capacity(self, value=None):
        """  Corresponds to IDD Field `Low Speed Nominal Capacity`
        Nominal tower capacity with entering water at 35C (95F), leaving water at
        29.44C (85F), entering air at 25.56C (78F) wet-bulb temperature and 35C (95F)
        dry-bulb temperature, with the tower fan operating at low speed. Design water flow
        rate assumed to be 5.382E-8 m3/s per watt of tower high-speed nominal capacity
        (3 gpm/ton). Nominal tower capacity times the Heat Rejection Capacity and Nominal
        Capacity Sizing Ratio (e.g. 1.25) gives the actual tower heat
        rejection at these operating conditions.

        Args:
            value (float or "Autocalculate"): value for IDD Field `Low Speed Nominal Capacity`
                Units: W
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autocalculate":
                    self._data["Low Speed Nominal Capacity"] = "Autocalculate"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `low_speed_nominal_capacity`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `low_speed_nominal_capacity`')
        self._data["Low Speed Nominal Capacity"] = value

    @property
    def low_speed_nominal_capacity_sizing_factor(self):
        """Get low_speed_nominal_capacity_sizing_factor

        Returns:
            float: the value of `low_speed_nominal_capacity_sizing_factor` or None if not set
        """
        return self._data["Low Speed Nominal Capacity Sizing Factor"]

    @low_speed_nominal_capacity_sizing_factor.setter
    def low_speed_nominal_capacity_sizing_factor(self, value=0.5):
        """  Corresponds to IDD Field `Low Speed Nominal Capacity Sizing Factor`
        This field is only used if the previous field is set to autocalculate

        Args:
            value (float): value for IDD Field `Low Speed Nominal Capacity Sizing Factor`
                Default value: 0.5
                value > 0.0
                value < 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `low_speed_nominal_capacity_sizing_factor`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `low_speed_nominal_capacity_sizing_factor`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `low_speed_nominal_capacity_sizing_factor`')
        self._data["Low Speed Nominal Capacity Sizing Factor"] = value

    @property
    def free_convection_nominal_capacity(self):
        """Get free_convection_nominal_capacity

        Returns:
            float: the value of `free_convection_nominal_capacity` or None if not set
        """
        return self._data["Free Convection Nominal Capacity"]

    @free_convection_nominal_capacity.setter
    def free_convection_nominal_capacity(self, value=None):
        """  Corresponds to IDD Field `Free Convection Nominal Capacity`
        Tower capacity in free convection regime with entering water at 35C (95F),
        leaving water at 29.44C (85F), entering air at 25.56C (78F) wet-bulb temperature
        and 35C (95F) dry-bulb temperature. Design water flow rate assumed to be
        5.382E-8 m3/s per watt of tower high-speed nominal capacity (3 gpm/ton). Tower
        free convection capacity times the Heat Rejection Capacity and Nominal Capacity Sizing Ratio
        (e.g. 1.25)  gives the actual tower heat rejection at these operating conditions

        Args:
            value (float or "Autocalculate"): value for IDD Field `Free Convection Nominal Capacity`
                Units: W
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autocalculate":
                    self._data["Free Convection Nominal Capacity"] = "Autocalculate"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `free_convection_nominal_capacity`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `free_convection_nominal_capacity`')
        self._data["Free Convection Nominal Capacity"] = value

    @property
    def free_convection_nominal_capacity_sizing_factor(self):
        """Get free_convection_nominal_capacity_sizing_factor

        Returns:
            float: the value of `free_convection_nominal_capacity_sizing_factor` or None if not set
        """
        return self._data["Free Convection Nominal Capacity Sizing Factor"]

    @free_convection_nominal_capacity_sizing_factor.setter
    def free_convection_nominal_capacity_sizing_factor(self, value=0.1):
        """  Corresponds to IDD Field `Free Convection Nominal Capacity Sizing Factor`
        This field is only used if the previous field is set to autocalculate

        Args:
            value (float): value for IDD Field `Free Convection Nominal Capacity Sizing Factor`
                Default value: 0.1
                value > 0.0
                value < 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `free_convection_nominal_capacity_sizing_factor`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `free_convection_nominal_capacity_sizing_factor`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `free_convection_nominal_capacity_sizing_factor`')
        self._data["Free Convection Nominal Capacity Sizing Factor"] = value

    @property
    def basin_heater_capacity(self):
        """Get basin_heater_capacity

        Returns:
            float: the value of `basin_heater_capacity` or None if not set
        """
        return self._data["Basin Heater Capacity"]

    @basin_heater_capacity.setter
    def basin_heater_capacity(self, value=0.0):
        """  Corresponds to IDD Field `Basin Heater Capacity`
        This heater maintains the basin water temperature at the basin heater setpoint
        temperature when the outdoor air temperature falls below the setpoint temperature.
        The basin heater only operates when water is not flowing through the tower.

        Args:
            value (float): value for IDD Field `Basin Heater Capacity`
                Units: W/K
                Default value: 0.0
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `basin_heater_capacity`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `basin_heater_capacity`')
        self._data["Basin Heater Capacity"] = value

    @property
    def basin_heater_setpoint_temperature(self):
        """Get basin_heater_setpoint_temperature

        Returns:
            float: the value of `basin_heater_setpoint_temperature` or None if not set
        """
        return self._data["Basin Heater Setpoint Temperature"]

    @basin_heater_setpoint_temperature.setter
    def basin_heater_setpoint_temperature(self, value=2.0):
        """  Corresponds to IDD Field `Basin Heater Setpoint Temperature`
        Enter the outdoor dry-bulb temperature when the basin heater turns on

        Args:
            value (float): value for IDD Field `Basin Heater Setpoint Temperature`
                Units: C
                Default value: 2.0
                value >= 2.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `basin_heater_setpoint_temperature`'.format(value))
            if value < 2.0:
                raise ValueError('value need to be greater or equal 2.0 '
                                 'for field `basin_heater_setpoint_temperature`')
        self._data["Basin Heater Setpoint Temperature"] = value

    @property
    def basin_heater_operating_schedule_name(self):
        """Get basin_heater_operating_schedule_name

        Returns:
            str: the value of `basin_heater_operating_schedule_name` or None if not set
        """
        return self._data["Basin Heater Operating Schedule Name"]

    @basin_heater_operating_schedule_name.setter
    def basin_heater_operating_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Basin Heater Operating Schedule Name`
        Schedule values greater than 0 allow the basin heater to operate whenever the outdoor
        air dry-bulb temperature is below the basin heater setpoint temperature.
        If a schedule name is not entered, the basin heater is allowed to operate
        throughout the entire simulation.

        Args:
            value (str): value for IDD Field `Basin Heater Operating Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `basin_heater_operating_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `basin_heater_operating_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `basin_heater_operating_schedule_name`')
        self._data["Basin Heater Operating Schedule Name"] = value

    @property
    def evaporation_loss_mode(self):
        """Get evaporation_loss_mode

        Returns:
            str: the value of `evaporation_loss_mode` or None if not set
        """
        return self._data["Evaporation Loss Mode"]

    @evaporation_loss_mode.setter
    def evaporation_loss_mode(self, value=None):
        """  Corresponds to IDD Field `Evaporation Loss Mode`

        Args:
            value (str): value for IDD Field `Evaporation Loss Mode`
                Accepted values are:
                      - LossFactor
                      - SaturatedExit
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `evaporation_loss_mode`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `evaporation_loss_mode`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `evaporation_loss_mode`')
            vals = {}
            vals["lossfactor"] = "LossFactor"
            vals["saturatedexit"] = "SaturatedExit"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `evaporation_loss_mode`'.format(value))
            value = vals[value_lower]
        self._data["Evaporation Loss Mode"] = value

    @property
    def evaporation_loss_factor(self):
        """Get evaporation_loss_factor

        Returns:
            float: the value of `evaporation_loss_factor` or None if not set
        """
        return self._data["Evaporation Loss Factor"]

    @evaporation_loss_factor.setter
    def evaporation_loss_factor(self, value=0.2):
        """  Corresponds to IDD Field `Evaporation Loss Factor`
        Rate of water evaporated from the cooling tower and lost to the outdoor air [%/K]
        Evaporation loss is calculated as percentage of the circulating condenser water rate
        Value entered here is percent-per-degree K of temperature drop in the condenser water
        Typical values are from 0.15 to 0.27 [%/K].

        Args:
            value (float): value for IDD Field `Evaporation Loss Factor`
                Units: percent/K
                Default value: 0.2
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `evaporation_loss_factor`'.format(value))
        self._data["Evaporation Loss Factor"] = value

    @property
    def drift_loss_percent(self):
        """Get drift_loss_percent

        Returns:
            float: the value of `drift_loss_percent` or None if not set
        """
        return self._data["Drift Loss Percent"]

    @drift_loss_percent.setter
    def drift_loss_percent(self, value=0.008):
        """  Corresponds to IDD Field `Drift Loss Percent`
        Rate of drift loss as a percentage of circulating condenser water flow rate
        Typical values are between 0.002 and 0.2% The default value is 0.008%

        Args:
            value (float): value for IDD Field `Drift Loss Percent`
                Units: percent
                Default value: 0.008
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `drift_loss_percent`'.format(value))
        self._data["Drift Loss Percent"] = value

    @property
    def blowdown_calculation_mode(self):
        """Get blowdown_calculation_mode

        Returns:
            str: the value of `blowdown_calculation_mode` or None if not set
        """
        return self._data["Blowdown Calculation Mode"]

    @blowdown_calculation_mode.setter
    def blowdown_calculation_mode(self, value=None):
        """  Corresponds to IDD Field `Blowdown Calculation Mode`

        Args:
            value (str): value for IDD Field `Blowdown Calculation Mode`
                Accepted values are:
                      - ConcentrationRatio
                      - ScheduledRate
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `blowdown_calculation_mode`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `blowdown_calculation_mode`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `blowdown_calculation_mode`')
            vals = {}
            vals["concentrationratio"] = "ConcentrationRatio"
            vals["scheduledrate"] = "ScheduledRate"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `blowdown_calculation_mode`'.format(value))
            value = vals[value_lower]
        self._data["Blowdown Calculation Mode"] = value

    @property
    def blowdown_concentration_ratio(self):
        """Get blowdown_concentration_ratio

        Returns:
            float: the value of `blowdown_concentration_ratio` or None if not set
        """
        return self._data["Blowdown Concentration Ratio"]

    @blowdown_concentration_ratio.setter
    def blowdown_concentration_ratio(self, value=3.0):
        """  Corresponds to IDD Field `Blowdown Concentration Ratio`
        Characterizes the rate of blowdown in the cooling tower.
        Blowdown is water intentionally drained from the tower in order to offset the build up
        of solids in the water that would otherwise occur because of evaporation.
        Ratio of solids in the blowdown water to solids in the make up water.
        Typical values for tower operation are 3 to 5.  The default value is 3.

        Args:
            value (float): value for IDD Field `Blowdown Concentration Ratio`
                Default value: 3.0
                value >= 2.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `blowdown_concentration_ratio`'.format(value))
            if value < 2.0:
                raise ValueError('value need to be greater or equal 2.0 '
                                 'for field `blowdown_concentration_ratio`')
        self._data["Blowdown Concentration Ratio"] = value

    @property
    def blowdown_makeup_water_usage_schedule_name(self):
        """Get blowdown_makeup_water_usage_schedule_name

        Returns:
            str: the value of `blowdown_makeup_water_usage_schedule_name` or None if not set
        """
        return self._data["Blowdown Makeup Water Usage Schedule Name"]

    @blowdown_makeup_water_usage_schedule_name.setter
    def blowdown_makeup_water_usage_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Blowdown Makeup Water Usage Schedule Name`
        Makeup water usage due to blowdown results from occasionally draining some amount
        of water in the tower basin to purge scale or other contaminants to reduce their
        concentration in order to maintain an acceptable level of water quality.
        Schedule values should reflect water usage in m3/s.

        Args:
            value (str): value for IDD Field `Blowdown Makeup Water Usage Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `blowdown_makeup_water_usage_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `blowdown_makeup_water_usage_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `blowdown_makeup_water_usage_schedule_name`')
        self._data["Blowdown Makeup Water Usage Schedule Name"] = value

    @property
    def supply_water_storage_tank_name(self):
        """Get supply_water_storage_tank_name

        Returns:
            str: the value of `supply_water_storage_tank_name` or None if not set
        """
        return self._data["Supply Water Storage Tank Name"]

    @supply_water_storage_tank_name.setter
    def supply_water_storage_tank_name(self, value=None):
        """  Corresponds to IDD Field `Supply Water Storage Tank Name`

        Args:
            value (str): value for IDD Field `Supply Water Storage Tank Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_water_storage_tank_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_water_storage_tank_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `supply_water_storage_tank_name`')
        self._data["Supply Water Storage Tank Name"] = value

    @property
    def outdoor_air_inlet_node_name(self):
        """Get outdoor_air_inlet_node_name

        Returns:
            str: the value of `outdoor_air_inlet_node_name` or None if not set
        """
        return self._data["Outdoor Air Inlet Node Name"]

    @outdoor_air_inlet_node_name.setter
    def outdoor_air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Outdoor Air Inlet Node Name`
        Enter the name of an outdoor air node

        Args:
            value (str): value for IDD Field `Outdoor Air Inlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `outdoor_air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outdoor_air_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `outdoor_air_inlet_node_name`')
        self._data["Outdoor Air Inlet Node Name"] = value

    @property
    def number_of_cells(self):
        """Get number_of_cells

        Returns:
            int: the value of `number_of_cells` or None if not set
        """
        return self._data["Number of Cells"]

    @number_of_cells.setter
    def number_of_cells(self, value=1):
        """  Corresponds to IDD Field `Number of Cells`

        Args:
            value (int): value for IDD Field `Number of Cells`
                Default value: 1
                value >= 1
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = int(value)
            except ValueError:
                raise ValueError('value {} need to be of type int '
                                 'for field `number_of_cells`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `number_of_cells`')
        self._data["Number of Cells"] = value

    @property
    def cell_control(self):
        """Get cell_control

        Returns:
            str: the value of `cell_control` or None if not set
        """
        return self._data["Cell Control"]

    @cell_control.setter
    def cell_control(self, value="MinimalCell"):
        """  Corresponds to IDD Field `Cell Control`

        Args:
            value (str): value for IDD Field `Cell Control`
                Default value: MinimalCell
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `cell_control`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `cell_control`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `cell_control`')
        self._data["Cell Control"] = value

    @property
    def cell_minimum_water_flow_rate_fraction(self):
        """Get cell_minimum_water_flow_rate_fraction

        Returns:
            float: the value of `cell_minimum_water_flow_rate_fraction` or None if not set
        """
        return self._data["Cell Minimum  Water Flow Rate Fraction"]

    @cell_minimum_water_flow_rate_fraction.setter
    def cell_minimum_water_flow_rate_fraction(self, value=0.33):
        """  Corresponds to IDD Field `Cell Minimum  Water Flow Rate Fraction`
        The allowable mininal fraction of the nominal flow rate per cell

        Args:
            value (float): value for IDD Field `Cell Minimum  Water Flow Rate Fraction`
                Default value: 0.33
                value > 0.0
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `cell_minimum_water_flow_rate_fraction`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `cell_minimum_water_flow_rate_fraction`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `cell_minimum_water_flow_rate_fraction`')
        self._data["Cell Minimum  Water Flow Rate Fraction"] = value

    @property
    def cell_maximum_water_flow_rate_fraction(self):
        """Get cell_maximum_water_flow_rate_fraction

        Returns:
            float: the value of `cell_maximum_water_flow_rate_fraction` or None if not set
        """
        return self._data["Cell Maximum Water Flow Rate Fraction"]

    @cell_maximum_water_flow_rate_fraction.setter
    def cell_maximum_water_flow_rate_fraction(self, value=2.5):
        """  Corresponds to IDD Field `Cell Maximum Water Flow Rate Fraction`
        The allowable maximal fraction of the nominal flow rate per cell

        Args:
            value (float): value for IDD Field `Cell Maximum Water Flow Rate Fraction`
                Default value: 2.5
                value >= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `cell_maximum_water_flow_rate_fraction`'.format(value))
            if value < 1.0:
                raise ValueError('value need to be greater or equal 1.0 '
                                 'for field `cell_maximum_water_flow_rate_fraction`')
        self._data["Cell Maximum Water Flow Rate Fraction"] = value

    @property
    def sizing_factor(self):
        """Get sizing_factor

        Returns:
            float: the value of `sizing_factor` or None if not set
        """
        return self._data["Sizing Factor"]

    @sizing_factor.setter
    def sizing_factor(self, value=1.0):
        """  Corresponds to IDD Field `Sizing Factor`
        Multiplies the autosized capacity and flow rates

        Args:
            value (float): value for IDD Field `Sizing Factor`
                Default value: 1.0
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `sizing_factor`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `sizing_factor`')
        self._data["Sizing Factor"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
        return good

    @classmethod
    def _to_str(cls, value):
        """ Represents values either as string or None values as empty string

        Args:
            value: a value
        """
        if value is None:
            return ''
        else:
            return str(value)

    def export(self):
        """ Export values of data object as list of strings"""
        out = []
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class CoolingTowerVariableSpeedMerkel(object):
    """ Corresponds to IDD object `CoolingTower:VariableSpeed:Merkel`
        This tower model is based on Merkel's theory, which is also the basis
        for the tower model in ASHRAE's HVAC1 Toolkit. The closed-circuit cooling tower
        is modeled as a counter flow heat exchanger with a variable-speed fan drawing air
        through the tower (induced-draft configuration).
        For a multi-cell tower, the capacity and air/water flow rate inputs are for the entire tower.
    
    """
    internal_name = "CoolingTower:VariableSpeed:Merkel"
    field_count = 40
    required_fields = ["Name", "Water Inlet Node Name", "Water Outlet Node Name", "Performance Input Method", "Heat Rejection Capacity and Nominal Capacity Sizing Ratio", "Free Convection Nominal Capacity Sizing Factor", "Design Water Flow Rate", "Design Air Flow Rate", "Design Fan Power", "Fan Power Modifier Function of Air Flow Rate Ratio Curve Name", "Free Convection Regime Air Flow Rate Sizing Factor", "U-Factor Times Area Modifier Function of Air Flow Ratio Curve Name", "U-Factor Times Area Modifier Function of Wetbulb Temperature Difference Curve Name", "U-Factor Times Area Modifier Function of Water Flow Ratio Curve Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `CoolingTower:VariableSpeed:Merkel`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Water Inlet Node Name"] = None
        self._data["Water Outlet Node Name"] = None
        self._data["Performance Input Method"] = None
        self._data["Heat Rejection Capacity and Nominal Capacity Sizing Ratio"] = None
        self._data["Nominal Capacity"] = None
        self._data["Free Convection Nominal Capacity"] = None
        self._data["Free Convection Nominal Capacity Sizing Factor"] = None
        self._data["Design Water Flow Rate"] = None
        self._data["Design Water Flow Rate per Unit of Nominal Capacity"] = None
        self._data["Design Air Flow Rate"] = None
        self._data["Design Air Flow Rate Per Unit of Nominal Capacity"] = None
        self._data["Minimum Air Flow Rate Ratio"] = None
        self._data["Design Fan Power"] = None
        self._data["Design Fan Power Per Unit of Nominal Capacity"] = None
        self._data["Fan Power Modifier Function of Air Flow Rate Ratio Curve Name"] = None
        self._data["Free Convection Regime Air Flow Rate"] = None
        self._data["Free Convection Regime Air Flow Rate Sizing Factor"] = None
        self._data["Design Air Flow Rate U-Factor Times Area Value"] = None
        self._data["Free Convection Regime U-Factor Times Area Value"] = None
        self._data["Free Convection U-Factor Times Area Value Sizing Factor"] = None
        self._data["U-Factor Times Area Modifier Function of Air Flow Ratio Curve Name"] = None
        self._data["U-Factor Times Area Modifier Function of Wetbulb Temperature Difference Curve Name"] = None
        self._data["U-Factor Times Area Modifier Function of Water Flow Ratio Curve Name"] = None
        self._data["Basin Heater Capacity"] = None
        self._data["Basin Heater Setpoint Temperature"] = None
        self._data["Basin Heater Operating Schedule Name"] = None
        self._data["Evaporation Loss Mode"] = None
        self._data["Evaporation Loss Factor"] = None
        self._data["Drift Loss Percent"] = None
        self._data["Blowdown Calculation Mode"] = None
        self._data["Blowdown Concentration Ratio"] = None
        self._data["Blowdown Makeup Water Usage Schedule Name"] = None
        self._data["Supply Water Storage Tank Name"] = None
        self._data["Outdoor Air Inlet Node Name"] = None
        self._data["Number of Cells"] = None
        self._data["Cell Control"] = None
        self._data["Cell Minimum  Water Flow Rate Fraction"] = None
        self._data["Cell Maximum Water Flow Rate Fraction"] = None
        self._data["Sizing Factor"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.water_inlet_node_name = None
        else:
            self.water_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.water_outlet_node_name = None
        else:
            self.water_outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.performance_input_method = None
        else:
            self.performance_input_method = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heat_rejection_capacity_and_nominal_capacity_sizing_ratio = None
        else:
            self.heat_rejection_capacity_and_nominal_capacity_sizing_ratio = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.nominal_capacity = None
        else:
            self.nominal_capacity = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.free_convection_nominal_capacity = None
        else:
            self.free_convection_nominal_capacity = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.free_convection_nominal_capacity_sizing_factor = None
        else:
            self.free_convection_nominal_capacity_sizing_factor = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_water_flow_rate = None
        else:
            self.design_water_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_water_flow_rate_per_unit_of_nominal_capacity = None
        else:
            self.design_water_flow_rate_per_unit_of_nominal_capacity = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_air_flow_rate = None
        else:
            self.design_air_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_air_flow_rate_per_unit_of_nominal_capacity = None
        else:
            self.design_air_flow_rate_per_unit_of_nominal_capacity = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_air_flow_rate_ratio = None
        else:
            self.minimum_air_flow_rate_ratio = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_fan_power = None
        else:
            self.design_fan_power = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_fan_power_per_unit_of_nominal_capacity = None
        else:
            self.design_fan_power_per_unit_of_nominal_capacity = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fan_power_modifier_function_of_air_flow_rate_ratio_curve_name = None
        else:
            self.fan_power_modifier_function_of_air_flow_rate_ratio_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.free_convection_regime_air_flow_rate = None
        else:
            self.free_convection_regime_air_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.free_convection_regime_air_flow_rate_sizing_factor = None
        else:
            self.free_convection_regime_air_flow_rate_sizing_factor = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_air_flow_rate_ufactor_times_area_value = None
        else:
            self.design_air_flow_rate_ufactor_times_area_value = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.free_convection_regime_ufactor_times_area_value = None
        else:
            self.free_convection_regime_ufactor_times_area_value = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.free_convection_ufactor_times_area_value_sizing_factor = None
        else:
            self.free_convection_ufactor_times_area_value_sizing_factor = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.ufactor_times_area_modifier_function_of_air_flow_ratio_curve_name = None
        else:
            self.ufactor_times_area_modifier_function_of_air_flow_ratio_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.ufactor_times_area_modifier_function_of_wetbulb_temperature_difference_curve_name = None
        else:
            self.ufactor_times_area_modifier_function_of_wetbulb_temperature_difference_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.ufactor_times_area_modifier_function_of_water_flow_ratio_curve_name = None
        else:
            self.ufactor_times_area_modifier_function_of_water_flow_ratio_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.basin_heater_capacity = None
        else:
            self.basin_heater_capacity = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.basin_heater_setpoint_temperature = None
        else:
            self.basin_heater_setpoint_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.basin_heater_operating_schedule_name = None
        else:
            self.basin_heater_operating_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.evaporation_loss_mode = None
        else:
            self.evaporation_loss_mode = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.evaporation_loss_factor = None
        else:
            self.evaporation_loss_factor = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.drift_loss_percent = None
        else:
            self.drift_loss_percent = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.blowdown_calculation_mode = None
        else:
            self.blowdown_calculation_mode = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.blowdown_concentration_ratio = None
        else:
            self.blowdown_concentration_ratio = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.blowdown_makeup_water_usage_schedule_name = None
        else:
            self.blowdown_makeup_water_usage_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.supply_water_storage_tank_name = None
        else:
            self.supply_water_storage_tank_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outdoor_air_inlet_node_name = None
        else:
            self.outdoor_air_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.number_of_cells = None
        else:
            self.number_of_cells = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cell_control = None
        else:
            self.cell_control = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cell_minimum_water_flow_rate_fraction = None
        else:
            self.cell_minimum_water_flow_rate_fraction = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cell_maximum_water_flow_rate_fraction = None
        else:
            self.cell_maximum_water_flow_rate_fraction = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.sizing_factor = None
        else:
            self.sizing_factor = vals[i]
        i += 1
        if i >= len(vals):
            return

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `Name`
        Tower Name

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')
        self._data["Name"] = value

    @property
    def water_inlet_node_name(self):
        """Get water_inlet_node_name

        Returns:
            str: the value of `water_inlet_node_name` or None if not set
        """
        return self._data["Water Inlet Node Name"]

    @water_inlet_node_name.setter
    def water_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Water Inlet Node Name`
        Name of tower water inlet node

        Args:
            value (str): value for IDD Field `Water Inlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `water_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `water_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `water_inlet_node_name`')
        self._data["Water Inlet Node Name"] = value

    @property
    def water_outlet_node_name(self):
        """Get water_outlet_node_name

        Returns:
            str: the value of `water_outlet_node_name` or None if not set
        """
        return self._data["Water Outlet Node Name"]

    @water_outlet_node_name.setter
    def water_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Water Outlet Node Name`
        Name of tower water outlet node

        Args:
            value (str): value for IDD Field `Water Outlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `water_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `water_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `water_outlet_node_name`')
        self._data["Water Outlet Node Name"] = value

    @property
    def performance_input_method(self):
        """Get performance_input_method

        Returns:
            str: the value of `performance_input_method` or None if not set
        """
        return self._data["Performance Input Method"]

    @performance_input_method.setter
    def performance_input_method(self, value="NominalCapacity"):
        """  Corresponds to IDD Field `Performance Input Method`
        User can define tower thermal performance by specifying the tower UA,
        the Design Air Flow Rate and the Design Water Flow Rate,
        or by specifying the tower nominal capacity

        Args:
            value (str): value for IDD Field `Performance Input Method`
                Default value: NominalCapacity
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `performance_input_method`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `performance_input_method`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `performance_input_method`')
        self._data["Performance Input Method"] = value

    @property
    def heat_rejection_capacity_and_nominal_capacity_sizing_ratio(self):
        """Get heat_rejection_capacity_and_nominal_capacity_sizing_ratio

        Returns:
            float: the value of `heat_rejection_capacity_and_nominal_capacity_sizing_ratio` or None if not set
        """
        return self._data["Heat Rejection Capacity and Nominal Capacity Sizing Ratio"]

    @heat_rejection_capacity_and_nominal_capacity_sizing_ratio.setter
    def heat_rejection_capacity_and_nominal_capacity_sizing_ratio(self, value=1.25):
        """  Corresponds to IDD Field `Heat Rejection Capacity and Nominal Capacity Sizing Ratio`

        Args:
            value (float): value for IDD Field `Heat Rejection Capacity and Nominal Capacity Sizing Ratio`
                Default value: 1.25
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `heat_rejection_capacity_and_nominal_capacity_sizing_ratio`'.format(value))
        self._data["Heat Rejection Capacity and Nominal Capacity Sizing Ratio"] = value

    @property
    def nominal_capacity(self):
        """Get nominal_capacity

        Returns:
            float: the value of `nominal_capacity` or None if not set
        """
        return self._data["Nominal Capacity"]

    @nominal_capacity.setter
    def nominal_capacity(self, value=None):
        """  Corresponds to IDD Field `Nominal Capacity`
        Nominal tower capacity with entering water at 35C (95F), leaving water at
        29.44C (85F), entering air at 25.56C (78F) wet-bulb temperature and 35C (95F)
        dry-bulb temperature, with the tower fan operating at Design Air Flow Rate (full speed). Design water
        flow rate is as set in Design Water Flow Rate per Unit of Nominal Capacity. Nominal tower capacity
        times the Heat Rejection Capacity and Nominal Capacity Sizing Ratio (e.g. 1.25)
        gives the actual tower heat rejection at these operating conditions.

        Args:
            value (float or "Autosize"): value for IDD Field `Nominal Capacity`
                Units: W
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Nominal Capacity"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `nominal_capacity`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `nominal_capacity`')
        self._data["Nominal Capacity"] = value

    @property
    def free_convection_nominal_capacity(self):
        """Get free_convection_nominal_capacity

        Returns:
            float: the value of `free_convection_nominal_capacity` or None if not set
        """
        return self._data["Free Convection Nominal Capacity"]

    @free_convection_nominal_capacity.setter
    def free_convection_nominal_capacity(self, value=None):
        """  Corresponds to IDD Field `Free Convection Nominal Capacity`
        required field when performance method is NominalCapacity
        Tower capacity in free convection regime with entering water at 35C (95F),
        leaving water at 29.44C (85F), entering air at 25.56C (78F) wet-bulb temperature
        and 35C (95F) dry-bulb temperature. Design water flow rate is as set
        in Design Water Flow Rate per Unit of Nominal Capacity. Tower
        free convection capacity times the Heat Rejection Capacity and Nominal Capacity Sizing Ratio
        (e.g. 1.25)  gives the actual tower heat rejection at these operating conditions

        Args:
            value (float or "Autocalculate"): value for IDD Field `Free Convection Nominal Capacity`
                Units: W
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autocalculate":
                    self._data["Free Convection Nominal Capacity"] = "Autocalculate"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `free_convection_nominal_capacity`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `free_convection_nominal_capacity`')
        self._data["Free Convection Nominal Capacity"] = value

    @property
    def free_convection_nominal_capacity_sizing_factor(self):
        """Get free_convection_nominal_capacity_sizing_factor

        Returns:
            float: the value of `free_convection_nominal_capacity_sizing_factor` or None if not set
        """
        return self._data["Free Convection Nominal Capacity Sizing Factor"]

    @free_convection_nominal_capacity_sizing_factor.setter
    def free_convection_nominal_capacity_sizing_factor(self, value=0.1):
        """  Corresponds to IDD Field `Free Convection Nominal Capacity Sizing Factor`
        This field is only used if the previous field is set to autocalculate

        Args:
            value (float): value for IDD Field `Free Convection Nominal Capacity Sizing Factor`
                Default value: 0.1
                value > 0.0
                value < 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `free_convection_nominal_capacity_sizing_factor`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `free_convection_nominal_capacity_sizing_factor`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `free_convection_nominal_capacity_sizing_factor`')
        self._data["Free Convection Nominal Capacity Sizing Factor"] = value

    @property
    def design_water_flow_rate(self):
        """Get design_water_flow_rate

        Returns:
            float: the value of `design_water_flow_rate` or None if not set
        """
        return self._data["Design Water Flow Rate"]

    @design_water_flow_rate.setter
    def design_water_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Design Water Flow Rate`

        Args:
            value (float or "Autosize"): value for IDD Field `Design Water Flow Rate`
                Units: m3/s
                IP-Units: gal/min
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Design Water Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `design_water_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `design_water_flow_rate`')
        self._data["Design Water Flow Rate"] = value

    @property
    def design_water_flow_rate_per_unit_of_nominal_capacity(self):
        """Get design_water_flow_rate_per_unit_of_nominal_capacity

        Returns:
            float: the value of `design_water_flow_rate_per_unit_of_nominal_capacity` or None if not set
        """
        return self._data["Design Water Flow Rate per Unit of Nominal Capacity"]

    @design_water_flow_rate_per_unit_of_nominal_capacity.setter
    def design_water_flow_rate_per_unit_of_nominal_capacity(self, value=5.382e-08):
        """  Corresponds to IDD Field `Design Water Flow Rate per Unit of Nominal Capacity`
        This field is only used if the previous is set to autocalculate and performance input method is NominalCapacity

        Args:
            value (float): value for IDD Field `Design Water Flow Rate per Unit of Nominal Capacity`
                Units: m3/s-W
                Default value: 5.382e-08
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `design_water_flow_rate_per_unit_of_nominal_capacity`'.format(value))
        self._data["Design Water Flow Rate per Unit of Nominal Capacity"] = value

    @property
    def design_air_flow_rate(self):
        """Get design_air_flow_rate

        Returns:
            float: the value of `design_air_flow_rate` or None if not set
        """
        return self._data["Design Air Flow Rate"]

    @design_air_flow_rate.setter
    def design_air_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Design Air Flow Rate`
        This is the air flow rate at full fan speed

        Args:
            value (float or "Autocalculate"): value for IDD Field `Design Air Flow Rate`
                Units: m3/s
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autocalculate":
                    self._data["Design Air Flow Rate"] = "Autocalculate"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `design_air_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `design_air_flow_rate`')
        self._data["Design Air Flow Rate"] = value

    @property
    def design_air_flow_rate_per_unit_of_nominal_capacity(self):
        """Get design_air_flow_rate_per_unit_of_nominal_capacity

        Returns:
            float: the value of `design_air_flow_rate_per_unit_of_nominal_capacity` or None if not set
        """
        return self._data["Design Air Flow Rate Per Unit of Nominal Capacity"]

    @design_air_flow_rate_per_unit_of_nominal_capacity.setter
    def design_air_flow_rate_per_unit_of_nominal_capacity(self, value=2.76316e-05):
        """  Corresponds to IDD Field `Design Air Flow Rate Per Unit of Nominal Capacity`
        This field is only used if the previous is set to autocalculate
        When field is left blank the default scaling factor is adjusted for elevation to increase volume flow at altitude
        When field has a value the scaling factor is used without adjusting for elevation

        Args:
            value (float): value for IDD Field `Design Air Flow Rate Per Unit of Nominal Capacity`
                Units: m3/s-W
                Default value: 2.76316e-05
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `design_air_flow_rate_per_unit_of_nominal_capacity`'.format(value))
        self._data["Design Air Flow Rate Per Unit of Nominal Capacity"] = value

    @property
    def minimum_air_flow_rate_ratio(self):
        """Get minimum_air_flow_rate_ratio

        Returns:
            float: the value of `minimum_air_flow_rate_ratio` or None if not set
        """
        return self._data["Minimum Air Flow Rate Ratio"]

    @minimum_air_flow_rate_ratio.setter
    def minimum_air_flow_rate_ratio(self, value=0.2):
        """  Corresponds to IDD Field `Minimum Air Flow Rate Ratio`
        Enter the minimum air flow rate ratio. This is typically determined by the variable
        speed drive that controls the fan motor speed. Valid entries are from 0.1 to 0.5.

        Args:
            value (float): value for IDD Field `Minimum Air Flow Rate Ratio`
                Default value: 0.2
                value >= 0.1
                value <= 0.5
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `minimum_air_flow_rate_ratio`'.format(value))
            if value < 0.1:
                raise ValueError('value need to be greater or equal 0.1 '
                                 'for field `minimum_air_flow_rate_ratio`')
            if value > 0.5:
                raise ValueError('value need to be smaller 0.5 '
                                 'for field `minimum_air_flow_rate_ratio`')
        self._data["Minimum Air Flow Rate Ratio"] = value

    @property
    def design_fan_power(self):
        """Get design_fan_power

        Returns:
            float: the value of `design_fan_power` or None if not set
        """
        return self._data["Design Fan Power"]

    @design_fan_power.setter
    def design_fan_power(self, value=None):
        """  Corresponds to IDD Field `Design Fan Power`
        This is the fan motor electric input power at high speed

        Args:
            value (float or "Autocalculate"): value for IDD Field `Design Fan Power`
                Units: W
                IP-Units: W
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autocalculate":
                    self._data["Design Fan Power"] = "Autocalculate"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `design_fan_power`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `design_fan_power`')
        self._data["Design Fan Power"] = value

    @property
    def design_fan_power_per_unit_of_nominal_capacity(self):
        """Get design_fan_power_per_unit_of_nominal_capacity

        Returns:
            float: the value of `design_fan_power_per_unit_of_nominal_capacity` or None if not set
        """
        return self._data["Design Fan Power Per Unit of Nominal Capacity"]

    @design_fan_power_per_unit_of_nominal_capacity.setter
    def design_fan_power_per_unit_of_nominal_capacity(self, value=0.0105):
        """  Corresponds to IDD Field `Design Fan Power Per Unit of Nominal Capacity`
        This field is only used if the previous is set to autocalculate
        [W/W] Watts of fan power per Watt of tower nominal capacity

        Args:
            value (float): value for IDD Field `Design Fan Power Per Unit of Nominal Capacity`
                Units: dimensionless
                Default value: 0.0105
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `design_fan_power_per_unit_of_nominal_capacity`'.format(value))
        self._data["Design Fan Power Per Unit of Nominal Capacity"] = value

    @property
    def fan_power_modifier_function_of_air_flow_rate_ratio_curve_name(self):
        """Get fan_power_modifier_function_of_air_flow_rate_ratio_curve_name

        Returns:
            str: the value of `fan_power_modifier_function_of_air_flow_rate_ratio_curve_name` or None if not set
        """
        return self._data["Fan Power Modifier Function of Air Flow Rate Ratio Curve Name"]

    @fan_power_modifier_function_of_air_flow_rate_ratio_curve_name.setter
    def fan_power_modifier_function_of_air_flow_rate_ratio_curve_name(self, value=None):
        """  Corresponds to IDD Field `Fan Power Modifier Function of Air Flow Rate Ratio Curve Name`
        Any curve or table with one independent variable can be used:
        Curve:Linear, Curve:Quadratic, Curve:Cubic, Curve:Quartic, Curve:Exponent,
        Curve:ExponentialSkewNormal, Curve:Sigmoid, Curve:RectuangularHyperbola1,
        Curve:RectangularHyperbola2, Curve:ExponentialDecay, Curve:DoubleExponentialDecay,
        Table:OneIndependentVariable
        cubic curve = a + b*AFR + c*AFR**2 + d*AFR**3
        quartic curve = a + b*AFR + c*AFR**2 + d*AFR**3 + e*AFR**4
        x = AFR = Ratio of current operating air flow rate to Design Air Flow Rate

        Args:
            value (str): value for IDD Field `Fan Power Modifier Function of Air Flow Rate Ratio Curve Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `fan_power_modifier_function_of_air_flow_rate_ratio_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `fan_power_modifier_function_of_air_flow_rate_ratio_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `fan_power_modifier_function_of_air_flow_rate_ratio_curve_name`')
        self._data["Fan Power Modifier Function of Air Flow Rate Ratio Curve Name"] = value

    @property
    def free_convection_regime_air_flow_rate(self):
        """Get free_convection_regime_air_flow_rate

        Returns:
            float: the value of `free_convection_regime_air_flow_rate` or None if not set
        """
        return self._data["Free Convection Regime Air Flow Rate"]

    @free_convection_regime_air_flow_rate.setter
    def free_convection_regime_air_flow_rate(self, value=0.0):
        """  Corresponds to IDD Field `Free Convection Regime Air Flow Rate`

        Args:
            value (float or "Autocalculate"): value for IDD Field `Free Convection Regime Air Flow Rate`
                Units: m3/s
                Default value: 0.0
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autocalculate":
                    self._data["Free Convection Regime Air Flow Rate"] = "Autocalculate"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `free_convection_regime_air_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `free_convection_regime_air_flow_rate`')
        self._data["Free Convection Regime Air Flow Rate"] = value

    @property
    def free_convection_regime_air_flow_rate_sizing_factor(self):
        """Get free_convection_regime_air_flow_rate_sizing_factor

        Returns:
            float: the value of `free_convection_regime_air_flow_rate_sizing_factor` or None if not set
        """
        return self._data["Free Convection Regime Air Flow Rate Sizing Factor"]

    @free_convection_regime_air_flow_rate_sizing_factor.setter
    def free_convection_regime_air_flow_rate_sizing_factor(self, value=0.1):
        """  Corresponds to IDD Field `Free Convection Regime Air Flow Rate Sizing Factor`
        This field is only used if the previous field is set to autocalculate.

        Args:
            value (float): value for IDD Field `Free Convection Regime Air Flow Rate Sizing Factor`
                Default value: 0.1
                value > 0.0
                value < 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `free_convection_regime_air_flow_rate_sizing_factor`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `free_convection_regime_air_flow_rate_sizing_factor`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `free_convection_regime_air_flow_rate_sizing_factor`')
        self._data["Free Convection Regime Air Flow Rate Sizing Factor"] = value

    @property
    def design_air_flow_rate_ufactor_times_area_value(self):
        """Get design_air_flow_rate_ufactor_times_area_value

        Returns:
            float: the value of `design_air_flow_rate_ufactor_times_area_value` or None if not set
        """
        return self._data["Design Air Flow Rate U-Factor Times Area Value"]

    @design_air_flow_rate_ufactor_times_area_value.setter
    def design_air_flow_rate_ufactor_times_area_value(self, value=None):
        """  Corresponds to IDD Field `Design Air Flow Rate U-Factor Times Area Value`
        required field when performance method is UFactorTimesAreaAndDesignWaterFlowRate
        when performance method is NominalCapacity the program will solve for this UA

        Args:
            value (float or "Autosize"): value for IDD Field `Design Air Flow Rate U-Factor Times Area Value`
                Units: W/K
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Design Air Flow Rate U-Factor Times Area Value"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `design_air_flow_rate_ufactor_times_area_value`'.format(value))
        self._data["Design Air Flow Rate U-Factor Times Area Value"] = value

    @property
    def free_convection_regime_ufactor_times_area_value(self):
        """Get free_convection_regime_ufactor_times_area_value

        Returns:
            float: the value of `free_convection_regime_ufactor_times_area_value` or None if not set
        """
        return self._data["Free Convection Regime U-Factor Times Area Value"]

    @free_convection_regime_ufactor_times_area_value.setter
    def free_convection_regime_ufactor_times_area_value(self, value=0.0):
        """  Corresponds to IDD Field `Free Convection Regime U-Factor Times Area Value`
        required field when performance input method is UFactorTimesAreaAndDesignWaterFlowRate
        Leave field blank if performance input method is NominalCapacity

        Args:
            value (float or "Autocalculate"): value for IDD Field `Free Convection Regime U-Factor Times Area Value`
                Units: W/K
                Default value: 0.0
                value >= 0.0
                value <= 300000.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autocalculate":
                    self._data["Free Convection Regime U-Factor Times Area Value"] = "Autocalculate"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `free_convection_regime_ufactor_times_area_value`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `free_convection_regime_ufactor_times_area_value`')
            if value > 300000.0:
                raise ValueError('value need to be smaller 300000.0 '
                                 'for field `free_convection_regime_ufactor_times_area_value`')
        self._data["Free Convection Regime U-Factor Times Area Value"] = value

    @property
    def free_convection_ufactor_times_area_value_sizing_factor(self):
        """Get free_convection_ufactor_times_area_value_sizing_factor

        Returns:
            float: the value of `free_convection_ufactor_times_area_value_sizing_factor` or None if not set
        """
        return self._data["Free Convection U-Factor Times Area Value Sizing Factor"]

    @free_convection_ufactor_times_area_value_sizing_factor.setter
    def free_convection_ufactor_times_area_value_sizing_factor(self, value=0.1):
        """  Corresponds to IDD Field `Free Convection U-Factor Times Area Value Sizing Factor`
        required field when performance input method is UFactorTimesAreaAndDesignWaterFlowRate
        This field is only used if the previous field is set to autocalculate and
        the performance input method is UFactorTimesAreaAndDesignWaterFlowRate

        Args:
            value (float): value for IDD Field `Free Convection U-Factor Times Area Value Sizing Factor`
                Default value: 0.1
                value > 0.0
                value < 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `free_convection_ufactor_times_area_value_sizing_factor`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `free_convection_ufactor_times_area_value_sizing_factor`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `free_convection_ufactor_times_area_value_sizing_factor`')
        self._data["Free Convection U-Factor Times Area Value Sizing Factor"] = value

    @property
    def ufactor_times_area_modifier_function_of_air_flow_ratio_curve_name(self):
        """Get ufactor_times_area_modifier_function_of_air_flow_ratio_curve_name

        Returns:
            str: the value of `ufactor_times_area_modifier_function_of_air_flow_ratio_curve_name` or None if not set
        """
        return self._data["U-Factor Times Area Modifier Function of Air Flow Ratio Curve Name"]

    @ufactor_times_area_modifier_function_of_air_flow_ratio_curve_name.setter
    def ufactor_times_area_modifier_function_of_air_flow_ratio_curve_name(self, value=None):
        """  Corresponds to IDD Field `U-Factor Times Area Modifier Function of Air Flow Ratio Curve Name`
        This curve describes how tower's design UA changes with variable air flow rate
        Any curve or table with one independent variable can be used:
        Curve:Linear, Curve:Quadratic, Curve:Cubic, Curve:Quartic, Curve:Exponent,
        Curve:ExponentialSkewNormal, Curve:Sigmoid, Curve:RectuangularHyperbola1,
        Curve:RectangularHyperbola2, Curve:ExponentialDecay, Curve:DoubleExponentialDecay,
        Table:OneIndependentVariable
        cubic curve = a + b*AFR + c*AFR**2 + d*AFR**3
        quartic curve = a + b*AFR + c*AFR**2 + d*AFR**3 + e*AFR**4
        x = AFR = Ratio of current operating air flow rate to Design Air Flow Rate

        Args:
            value (str): value for IDD Field `U-Factor Times Area Modifier Function of Air Flow Ratio Curve Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `ufactor_times_area_modifier_function_of_air_flow_ratio_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ufactor_times_area_modifier_function_of_air_flow_ratio_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ufactor_times_area_modifier_function_of_air_flow_ratio_curve_name`')
        self._data["U-Factor Times Area Modifier Function of Air Flow Ratio Curve Name"] = value

    @property
    def ufactor_times_area_modifier_function_of_wetbulb_temperature_difference_curve_name(self):
        """Get ufactor_times_area_modifier_function_of_wetbulb_temperature_difference_curve_name

        Returns:
            str: the value of `ufactor_times_area_modifier_function_of_wetbulb_temperature_difference_curve_name` or None if not set
        """
        return self._data["U-Factor Times Area Modifier Function of Wetbulb Temperature Difference Curve Name"]

    @ufactor_times_area_modifier_function_of_wetbulb_temperature_difference_curve_name.setter
    def ufactor_times_area_modifier_function_of_wetbulb_temperature_difference_curve_name(self, value=None):
        """  Corresponds to IDD Field `U-Factor Times Area Modifier Function of Wetbulb Temperature Difference Curve Name`
        curve describes how tower UA changes with outdoor air wetbulb temperature difference from design wetbulb
        Any curve or table with one independent variable can be used:
        Curve:Linear, Curve:Quadratic, Curve:Cubic, Curve:Quartic, Curve:Exponent,
        Curve:ExponentialSkewNormal, Curve:Sigmoid, Curve:RectuangularHyperbola1,
        Curve:RectangularHyperbola2, Curve:ExponentialDecay, Curve:DoubleExponentialDecay,
        Table:OneIndependentVariable
        cubic curve = a + b*DeltaWB + c*DeltaWB**2 + d*DeltaWB**3
        quartic curve = a + b*DeltaWB + c*DeltaWB**2 + d*DeltaWB**3 + e*DeltaWB**4
        x = DeltaWB = (design wetbulb temperature in C - current wetbulb temperature in C)
        where design wetbulb temperature of entering air is 25.56C (78F)

        Args:
            value (str): value for IDD Field `U-Factor Times Area Modifier Function of Wetbulb Temperature Difference Curve Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `ufactor_times_area_modifier_function_of_wetbulb_temperature_difference_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ufactor_times_area_modifier_function_of_wetbulb_temperature_difference_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ufactor_times_area_modifier_function_of_wetbulb_temperature_difference_curve_name`')
        self._data["U-Factor Times Area Modifier Function of Wetbulb Temperature Difference Curve Name"] = value

    @property
    def ufactor_times_area_modifier_function_of_water_flow_ratio_curve_name(self):
        """Get ufactor_times_area_modifier_function_of_water_flow_ratio_curve_name

        Returns:
            str: the value of `ufactor_times_area_modifier_function_of_water_flow_ratio_curve_name` or None if not set
        """
        return self._data["U-Factor Times Area Modifier Function of Water Flow Ratio Curve Name"]

    @ufactor_times_area_modifier_function_of_water_flow_ratio_curve_name.setter
    def ufactor_times_area_modifier_function_of_water_flow_ratio_curve_name(self, value=None):
        """  Corresponds to IDD Field `U-Factor Times Area Modifier Function of Water Flow Ratio Curve Name`
        curve describes how tower UA changes with the flow rate of condenser water through the tower
        Any curve or table with one independent variable can be used:
        Curve:Linear, Curve:Quadratic, Curve:Cubic, Curve:Quartic, Curve:Exponent,
        Curve:ExponentialSkewNormal, Curve:Sigmoid, Curve:RectuangularHyperbola1,
        Curve:RectangularHyperbola2, Curve:ExponentialDecay, Curve:DoubleExponentialDecay,
        Table:OneIndependentVariable
        cubic curve = a + b*WFR + c*WFR**2 + d*WFR**3
        quartic curve = a + b*WFR + c*WFR**2 + d*WFR**3 + e*WFR**4
        x = WFR = Ratio of current operationg water flow rate to Design Water Flow Rate

        Args:
            value (str): value for IDD Field `U-Factor Times Area Modifier Function of Water Flow Ratio Curve Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `ufactor_times_area_modifier_function_of_water_flow_ratio_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ufactor_times_area_modifier_function_of_water_flow_ratio_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ufactor_times_area_modifier_function_of_water_flow_ratio_curve_name`')
        self._data["U-Factor Times Area Modifier Function of Water Flow Ratio Curve Name"] = value

    @property
    def basin_heater_capacity(self):
        """Get basin_heater_capacity

        Returns:
            float: the value of `basin_heater_capacity` or None if not set
        """
        return self._data["Basin Heater Capacity"]

    @basin_heater_capacity.setter
    def basin_heater_capacity(self, value=0.0):
        """  Corresponds to IDD Field `Basin Heater Capacity`
        This heater maintains the basin water temperature at the basin heater setpoint
        temperature when the outdoor air temperature falls below the setpoint temperature.
        The basin heater only operates when water is not flowing through the tower.

        Args:
            value (float): value for IDD Field `Basin Heater Capacity`
                Units: W/K
                Default value: 0.0
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `basin_heater_capacity`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `basin_heater_capacity`')
        self._data["Basin Heater Capacity"] = value

    @property
    def basin_heater_setpoint_temperature(self):
        """Get basin_heater_setpoint_temperature

        Returns:
            float: the value of `basin_heater_setpoint_temperature` or None if not set
        """
        return self._data["Basin Heater Setpoint Temperature"]

    @basin_heater_setpoint_temperature.setter
    def basin_heater_setpoint_temperature(self, value=2.0):
        """  Corresponds to IDD Field `Basin Heater Setpoint Temperature`
        Enter the outdoor dry-bulb temperature when the basin heater turns on

        Args:
            value (float): value for IDD Field `Basin Heater Setpoint Temperature`
                Units: C
                Default value: 2.0
                value >= 2.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `basin_heater_setpoint_temperature`'.format(value))
            if value < 2.0:
                raise ValueError('value need to be greater or equal 2.0 '
                                 'for field `basin_heater_setpoint_temperature`')
        self._data["Basin Heater Setpoint Temperature"] = value

    @property
    def basin_heater_operating_schedule_name(self):
        """Get basin_heater_operating_schedule_name

        Returns:
            str: the value of `basin_heater_operating_schedule_name` or None if not set
        """
        return self._data["Basin Heater Operating Schedule Name"]

    @basin_heater_operating_schedule_name.setter
    def basin_heater_operating_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Basin Heater Operating Schedule Name`
        Schedule values greater than 0 allow the basin heater to operate whenever the outdoor
        air dry-bulb temperature is below the basin heater setpoint temperature.
        If a schedule name is not entered, the basin heater is allowed to operate
        throughout the entire simulation.

        Args:
            value (str): value for IDD Field `Basin Heater Operating Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `basin_heater_operating_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `basin_heater_operating_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `basin_heater_operating_schedule_name`')
        self._data["Basin Heater Operating Schedule Name"] = value

    @property
    def evaporation_loss_mode(self):
        """Get evaporation_loss_mode

        Returns:
            str: the value of `evaporation_loss_mode` or None if not set
        """
        return self._data["Evaporation Loss Mode"]

    @evaporation_loss_mode.setter
    def evaporation_loss_mode(self, value=None):
        """  Corresponds to IDD Field `Evaporation Loss Mode`

        Args:
            value (str): value for IDD Field `Evaporation Loss Mode`
                Accepted values are:
                      - LossFactor
                      - SaturatedExit
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `evaporation_loss_mode`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `evaporation_loss_mode`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `evaporation_loss_mode`')
            vals = {}
            vals["lossfactor"] = "LossFactor"
            vals["saturatedexit"] = "SaturatedExit"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `evaporation_loss_mode`'.format(value))
            value = vals[value_lower]
        self._data["Evaporation Loss Mode"] = value

    @property
    def evaporation_loss_factor(self):
        """Get evaporation_loss_factor

        Returns:
            float: the value of `evaporation_loss_factor` or None if not set
        """
        return self._data["Evaporation Loss Factor"]

    @evaporation_loss_factor.setter
    def evaporation_loss_factor(self, value=0.2):
        """  Corresponds to IDD Field `Evaporation Loss Factor`
        Rate of water evaporated from the cooling tower and lost to the outdoor air [%/K]
        Evaporation loss is calculated as percentage of the circulating condenser water rate
        Value entered here is percent-per-degree K of temperature drop in the condenser water
        Typical values are from 0.15 to 0.27 [%/K].

        Args:
            value (float): value for IDD Field `Evaporation Loss Factor`
                Units: percent/K
                Default value: 0.2
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `evaporation_loss_factor`'.format(value))
        self._data["Evaporation Loss Factor"] = value

    @property
    def drift_loss_percent(self):
        """Get drift_loss_percent

        Returns:
            float: the value of `drift_loss_percent` or None if not set
        """
        return self._data["Drift Loss Percent"]

    @drift_loss_percent.setter
    def drift_loss_percent(self, value=0.008):
        """  Corresponds to IDD Field `Drift Loss Percent`
        Rate of drift loss as a percentage of circulating condenser water flow rate
        Typical values are between 0.002 and 0.2% The default value is 0.008%

        Args:
            value (float): value for IDD Field `Drift Loss Percent`
                Units: percent
                Default value: 0.008
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `drift_loss_percent`'.format(value))
        self._data["Drift Loss Percent"] = value

    @property
    def blowdown_calculation_mode(self):
        """Get blowdown_calculation_mode

        Returns:
            str: the value of `blowdown_calculation_mode` or None if not set
        """
        return self._data["Blowdown Calculation Mode"]

    @blowdown_calculation_mode.setter
    def blowdown_calculation_mode(self, value=None):
        """  Corresponds to IDD Field `Blowdown Calculation Mode`

        Args:
            value (str): value for IDD Field `Blowdown Calculation Mode`
                Accepted values are:
                      - ConcentrationRatio
                      - ScheduledRate
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `blowdown_calculation_mode`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `blowdown_calculation_mode`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `blowdown_calculation_mode`')
            vals = {}
            vals["concentrationratio"] = "ConcentrationRatio"
            vals["scheduledrate"] = "ScheduledRate"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `blowdown_calculation_mode`'.format(value))
            value = vals[value_lower]
        self._data["Blowdown Calculation Mode"] = value

    @property
    def blowdown_concentration_ratio(self):
        """Get blowdown_concentration_ratio

        Returns:
            float: the value of `blowdown_concentration_ratio` or None if not set
        """
        return self._data["Blowdown Concentration Ratio"]

    @blowdown_concentration_ratio.setter
    def blowdown_concentration_ratio(self, value=3.0):
        """  Corresponds to IDD Field `Blowdown Concentration Ratio`
        Characterizes the rate of blowdown in the cooling tower.
        Blowdown is water intentionally drained from the tower in order to offset the build up
        of solids in the water that would otherwise occur because of evaporation.
        Ratio of solids in the blowdown water to solids in the make up water.
        Typical values for tower operation are 3 to 5.  The default value is 3.

        Args:
            value (float): value for IDD Field `Blowdown Concentration Ratio`
                Default value: 3.0
                value >= 2.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `blowdown_concentration_ratio`'.format(value))
            if value < 2.0:
                raise ValueError('value need to be greater or equal 2.0 '
                                 'for field `blowdown_concentration_ratio`')
        self._data["Blowdown Concentration Ratio"] = value

    @property
    def blowdown_makeup_water_usage_schedule_name(self):
        """Get blowdown_makeup_water_usage_schedule_name

        Returns:
            str: the value of `blowdown_makeup_water_usage_schedule_name` or None if not set
        """
        return self._data["Blowdown Makeup Water Usage Schedule Name"]

    @blowdown_makeup_water_usage_schedule_name.setter
    def blowdown_makeup_water_usage_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Blowdown Makeup Water Usage Schedule Name`
        Makeup water usage due to blowdown results from occasionally draining some amount
        of water in the tower basin to purge scale or other contaminants to reduce their
        concentration in order to maintain an acceptable level of water quality.
        Schedule values should reflect water usage in m3/s.

        Args:
            value (str): value for IDD Field `Blowdown Makeup Water Usage Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `blowdown_makeup_water_usage_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `blowdown_makeup_water_usage_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `blowdown_makeup_water_usage_schedule_name`')
        self._data["Blowdown Makeup Water Usage Schedule Name"] = value

    @property
    def supply_water_storage_tank_name(self):
        """Get supply_water_storage_tank_name

        Returns:
            str: the value of `supply_water_storage_tank_name` or None if not set
        """
        return self._data["Supply Water Storage Tank Name"]

    @supply_water_storage_tank_name.setter
    def supply_water_storage_tank_name(self, value=None):
        """  Corresponds to IDD Field `Supply Water Storage Tank Name`

        Args:
            value (str): value for IDD Field `Supply Water Storage Tank Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_water_storage_tank_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_water_storage_tank_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `supply_water_storage_tank_name`')
        self._data["Supply Water Storage Tank Name"] = value

    @property
    def outdoor_air_inlet_node_name(self):
        """Get outdoor_air_inlet_node_name

        Returns:
            str: the value of `outdoor_air_inlet_node_name` or None if not set
        """
        return self._data["Outdoor Air Inlet Node Name"]

    @outdoor_air_inlet_node_name.setter
    def outdoor_air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Outdoor Air Inlet Node Name`
        Enter the name of an outdoor air node

        Args:
            value (str): value for IDD Field `Outdoor Air Inlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `outdoor_air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outdoor_air_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `outdoor_air_inlet_node_name`')
        self._data["Outdoor Air Inlet Node Name"] = value

    @property
    def number_of_cells(self):
        """Get number_of_cells

        Returns:
            int: the value of `number_of_cells` or None if not set
        """
        return self._data["Number of Cells"]

    @number_of_cells.setter
    def number_of_cells(self, value=1):
        """  Corresponds to IDD Field `Number of Cells`

        Args:
            value (int): value for IDD Field `Number of Cells`
                Default value: 1
                value >= 1
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = int(value)
            except ValueError:
                raise ValueError('value {} need to be of type int '
                                 'for field `number_of_cells`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `number_of_cells`')
        self._data["Number of Cells"] = value

    @property
    def cell_control(self):
        """Get cell_control

        Returns:
            str: the value of `cell_control` or None if not set
        """
        return self._data["Cell Control"]

    @cell_control.setter
    def cell_control(self, value="MinimalCell"):
        """  Corresponds to IDD Field `Cell Control`

        Args:
            value (str): value for IDD Field `Cell Control`
                Default value: MinimalCell
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `cell_control`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `cell_control`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `cell_control`')
        self._data["Cell Control"] = value

    @property
    def cell_minimum_water_flow_rate_fraction(self):
        """Get cell_minimum_water_flow_rate_fraction

        Returns:
            float: the value of `cell_minimum_water_flow_rate_fraction` or None if not set
        """
        return self._data["Cell Minimum  Water Flow Rate Fraction"]

    @cell_minimum_water_flow_rate_fraction.setter
    def cell_minimum_water_flow_rate_fraction(self, value=0.33):
        """  Corresponds to IDD Field `Cell Minimum  Water Flow Rate Fraction`
        The allowable mininal fraction of the nominal flow rate per cell

        Args:
            value (float): value for IDD Field `Cell Minimum  Water Flow Rate Fraction`
                Default value: 0.33
                value > 0.0
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `cell_minimum_water_flow_rate_fraction`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `cell_minimum_water_flow_rate_fraction`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `cell_minimum_water_flow_rate_fraction`')
        self._data["Cell Minimum  Water Flow Rate Fraction"] = value

    @property
    def cell_maximum_water_flow_rate_fraction(self):
        """Get cell_maximum_water_flow_rate_fraction

        Returns:
            float: the value of `cell_maximum_water_flow_rate_fraction` or None if not set
        """
        return self._data["Cell Maximum Water Flow Rate Fraction"]

    @cell_maximum_water_flow_rate_fraction.setter
    def cell_maximum_water_flow_rate_fraction(self, value=2.5):
        """  Corresponds to IDD Field `Cell Maximum Water Flow Rate Fraction`
        The allowable maximal fraction of the nominal flow rate per cell

        Args:
            value (float): value for IDD Field `Cell Maximum Water Flow Rate Fraction`
                Default value: 2.5
                value >= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `cell_maximum_water_flow_rate_fraction`'.format(value))
            if value < 1.0:
                raise ValueError('value need to be greater or equal 1.0 '
                                 'for field `cell_maximum_water_flow_rate_fraction`')
        self._data["Cell Maximum Water Flow Rate Fraction"] = value

    @property
    def sizing_factor(self):
        """Get sizing_factor

        Returns:
            float: the value of `sizing_factor` or None if not set
        """
        return self._data["Sizing Factor"]

    @sizing_factor.setter
    def sizing_factor(self, value=1.0):
        """  Corresponds to IDD Field `Sizing Factor`
        Multiplies the autosized capacity and flow rates

        Args:
            value (float): value for IDD Field `Sizing Factor`
                Default value: 1.0
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `sizing_factor`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `sizing_factor`')
        self._data["Sizing Factor"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
        return good

    @classmethod
    def _to_str(cls, value):
        """ Represents values either as string or None values as empty string

        Args:
            value: a value
        """
        if value is None:
            return ''
        else:
            return str(value)

    def export(self):
        """ Export values of data object as list of strings"""
        out = []
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class CoolingTowerVariableSpeed(object):
    """ Corresponds to IDD object `CoolingTower:VariableSpeed`
        This tower model is based on purely empirical algorithms derived from manufacturer's
        performance data or field measurements. The user can select from two existing
        algorithms (CoolTools or YorkCalc), or they can enter their own correlation for
        approach temperature by using a variable speed tower model coefficient object.
        For a multi-cell tower, the capacity and air/water flow rate inputs are for the entire tower.
    
    """
    internal_name = "CoolingTower:VariableSpeed"
    field_count = 30
    required_fields = ["Name", "Water Inlet Node Name", "Water Outlet Node Name", "Design Water Flow Rate", "Design Air Flow Rate", "Design Fan Power"]

    def __init__(self):
        """ Init data dictionary object for IDD  `CoolingTower:VariableSpeed`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Water Inlet Node Name"] = None
        self._data["Water Outlet Node Name"] = None
        self._data["Model Type"] = None
        self._data["Model Coefficient Name"] = None
        self._data["Design Inlet Air Wet-Bulb Temperature"] = None
        self._data["Design Approach Temperature"] = None
        self._data["Design Range Temperature"] = None
        self._data["Design Water Flow Rate"] = None
        self._data["Design Air Flow Rate"] = None
        self._data["Design Fan Power"] = None
        self._data["Fan Power Ratio Function of Air Flow Rate Ratio Curve Name"] = None
        self._data["Minimum Air Flow Rate Ratio"] = None
        self._data["Fraction of Tower Capacity in Free Convection Regime"] = None
        self._data["Basin Heater Capacity"] = None
        self._data["Basin Heater Setpoint Temperature"] = None
        self._data["Basin Heater Operating Schedule Name"] = None
        self._data["Evaporation Loss Mode"] = None
        self._data["Evaporation Loss Factor"] = None
        self._data["Drift Loss Percent"] = None
        self._data["Blowdown Calculation Mode"] = None
        self._data["Blowdown Concentration Ratio"] = None
        self._data["Blowdown Makeup Water Usage Schedule Name"] = None
        self._data["Supply Water Storage Tank Name"] = None
        self._data["Outdoor Air Inlet Node Name"] = None
        self._data["Number of Cells"] = None
        self._data["Cell Control"] = None
        self._data["Cell Minimum  Water Flow Rate Fraction"] = None
        self._data["Cell Maximum Water Flow Rate Fraction"] = None
        self._data["Sizing Factor"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.water_inlet_node_name = None
        else:
            self.water_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.water_outlet_node_name = None
        else:
            self.water_outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.model_type = None
        else:
            self.model_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.model_coefficient_name = None
        else:
            self.model_coefficient_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_inlet_air_wetbulb_temperature = None
        else:
            self.design_inlet_air_wetbulb_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_approach_temperature = None
        else:
            self.design_approach_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_range_temperature = None
        else:
            self.design_range_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_water_flow_rate = None
        else:
            self.design_water_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_air_flow_rate = None
        else:
            self.design_air_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_fan_power = None
        else:
            self.design_fan_power = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fan_power_ratio_function_of_air_flow_rate_ratio_curve_name = None
        else:
            self.fan_power_ratio_function_of_air_flow_rate_ratio_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_air_flow_rate_ratio = None
        else:
            self.minimum_air_flow_rate_ratio = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fraction_of_tower_capacity_in_free_convection_regime = None
        else:
            self.fraction_of_tower_capacity_in_free_convection_regime = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.basin_heater_capacity = None
        else:
            self.basin_heater_capacity = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.basin_heater_setpoint_temperature = None
        else:
            self.basin_heater_setpoint_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.basin_heater_operating_schedule_name = None
        else:
            self.basin_heater_operating_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.evaporation_loss_mode = None
        else:
            self.evaporation_loss_mode = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.evaporation_loss_factor = None
        else:
            self.evaporation_loss_factor = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.drift_loss_percent = None
        else:
            self.drift_loss_percent = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.blowdown_calculation_mode = None
        else:
            self.blowdown_calculation_mode = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.blowdown_concentration_ratio = None
        else:
            self.blowdown_concentration_ratio = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.blowdown_makeup_water_usage_schedule_name = None
        else:
            self.blowdown_makeup_water_usage_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.supply_water_storage_tank_name = None
        else:
            self.supply_water_storage_tank_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outdoor_air_inlet_node_name = None
        else:
            self.outdoor_air_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.number_of_cells = None
        else:
            self.number_of_cells = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cell_control = None
        else:
            self.cell_control = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cell_minimum_water_flow_rate_fraction = None
        else:
            self.cell_minimum_water_flow_rate_fraction = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cell_maximum_water_flow_rate_fraction = None
        else:
            self.cell_maximum_water_flow_rate_fraction = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.sizing_factor = None
        else:
            self.sizing_factor = vals[i]
        i += 1
        if i >= len(vals):
            return

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `Name`
        Tower Name

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')
        self._data["Name"] = value

    @property
    def water_inlet_node_name(self):
        """Get water_inlet_node_name

        Returns:
            str: the value of `water_inlet_node_name` or None if not set
        """
        return self._data["Water Inlet Node Name"]

    @water_inlet_node_name.setter
    def water_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Water Inlet Node Name`
        Name of tower water inlet node

        Args:
            value (str): value for IDD Field `Water Inlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `water_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `water_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `water_inlet_node_name`')
        self._data["Water Inlet Node Name"] = value

    @property
    def water_outlet_node_name(self):
        """Get water_outlet_node_name

        Returns:
            str: the value of `water_outlet_node_name` or None if not set
        """
        return self._data["Water Outlet Node Name"]

    @water_outlet_node_name.setter
    def water_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Water Outlet Node Name`
        Name of tower water outlet node

        Args:
            value (str): value for IDD Field `Water Outlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `water_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `water_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `water_outlet_node_name`')
        self._data["Water Outlet Node Name"] = value

    @property
    def model_type(self):
        """Get model_type

        Returns:
            str: the value of `model_type` or None if not set
        """
        return self._data["Model Type"]

    @model_type.setter
    def model_type(self, value="YorkCalc"):
        """  Corresponds to IDD Field `Model Type`
        Determines the coefficients and form of the equation for calculating
        approach temperature

        Args:
            value (str): value for IDD Field `Model Type`
                Accepted values are:
                      - CoolToolsCrossFlow
                      - CoolToolsUserDefined
                      - YorkCalc
                      - YorkCalcUserDefined
                Default value: YorkCalc
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `model_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `model_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `model_type`')
            vals = {}
            vals["cooltoolscrossflow"] = "CoolToolsCrossFlow"
            vals["cooltoolsuserdefined"] = "CoolToolsUserDefined"
            vals["yorkcalc"] = "YorkCalc"
            vals["yorkcalcuserdefined"] = "YorkCalcUserDefined"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `model_type`'.format(value))
            value = vals[value_lower]
        self._data["Model Type"] = value

    @property
    def model_coefficient_name(self):
        """Get model_coefficient_name

        Returns:
            str: the value of `model_coefficient_name` or None if not set
        """
        return self._data["Model Coefficient Name"]

    @model_coefficient_name.setter
    def model_coefficient_name(self, value=None):
        """  Corresponds to IDD Field `Model Coefficient Name`
        Name of the tower model coefficient object.
        Used only when tower Model Type is either CoolToolsUserDefined or YorkCalcUserDefined.

        Args:
            value (str): value for IDD Field `Model Coefficient Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `model_coefficient_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `model_coefficient_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `model_coefficient_name`')
        self._data["Model Coefficient Name"] = value

    @property
    def design_inlet_air_wetbulb_temperature(self):
        """Get design_inlet_air_wetbulb_temperature

        Returns:
            float: the value of `design_inlet_air_wetbulb_temperature` or None if not set
        """
        return self._data["Design Inlet Air Wet-Bulb Temperature"]

    @design_inlet_air_wetbulb_temperature.setter
    def design_inlet_air_wetbulb_temperature(self, value=25.6):
        """  Corresponds to IDD Field `Design Inlet Air Wet-Bulb Temperature`
        Enter the tower's design inlet air wet-bulb temperature

        Args:
            value (float): value for IDD Field `Design Inlet Air Wet-Bulb Temperature`
                Units: C
                Default value: 25.6
                value >= 20.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `design_inlet_air_wetbulb_temperature`'.format(value))
            if value < 20.0:
                raise ValueError('value need to be greater or equal 20.0 '
                                 'for field `design_inlet_air_wetbulb_temperature`')
        self._data["Design Inlet Air Wet-Bulb Temperature"] = value

    @property
    def design_approach_temperature(self):
        """Get design_approach_temperature

        Returns:
            float: the value of `design_approach_temperature` or None if not set
        """
        return self._data["Design Approach Temperature"]

    @design_approach_temperature.setter
    def design_approach_temperature(self, value=3.9):
        """  Corresponds to IDD Field `Design Approach Temperature`
        Enter the approach temperature corresponding to the design inlet air
        wet-bulb temperature and design range temperature.
        Design approach temp = outlet water temperature minus inlet air wet-bulb temperature
        at design conditions.

        Args:
            value (float): value for IDD Field `Design Approach Temperature`
                Units: deltaC
                Default value: 3.9
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `design_approach_temperature`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `design_approach_temperature`')
        self._data["Design Approach Temperature"] = value

    @property
    def design_range_temperature(self):
        """Get design_range_temperature

        Returns:
            float: the value of `design_range_temperature` or None if not set
        """
        return self._data["Design Range Temperature"]

    @design_range_temperature.setter
    def design_range_temperature(self, value=5.6):
        """  Corresponds to IDD Field `Design Range Temperature`
        Enter the range temperature corresponding to the design inlet air
        wet-bulb temperature and design approach temperature.
        Design range = inlet water temperature minus outlet water temperature
        at design conditions.

        Args:
            value (float): value for IDD Field `Design Range Temperature`
                Units: deltaC
                Default value: 5.6
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `design_range_temperature`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `design_range_temperature`')
        self._data["Design Range Temperature"] = value

    @property
    def design_water_flow_rate(self):
        """Get design_water_flow_rate

        Returns:
            float: the value of `design_water_flow_rate` or None if not set
        """
        return self._data["Design Water Flow Rate"]

    @design_water_flow_rate.setter
    def design_water_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Design Water Flow Rate`
        Water flow rate through the tower at design conditions

        Args:
            value (float or "Autosize"): value for IDD Field `Design Water Flow Rate`
                Units: m3/s
                IP-Units: gal/min
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Design Water Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `design_water_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `design_water_flow_rate`')
        self._data["Design Water Flow Rate"] = value

    @property
    def design_air_flow_rate(self):
        """Get design_air_flow_rate

        Returns:
            float: the value of `design_air_flow_rate` or None if not set
        """
        return self._data["Design Air Flow Rate"]

    @design_air_flow_rate.setter
    def design_air_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Design Air Flow Rate`
        Design (maximum) air flow rate through the tower

        Args:
            value (float or "Autosize"): value for IDD Field `Design Air Flow Rate`
                Units: m3/s
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Design Air Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `design_air_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `design_air_flow_rate`')
        self._data["Design Air Flow Rate"] = value

    @property
    def design_fan_power(self):
        """Get design_fan_power

        Returns:
            float: the value of `design_fan_power` or None if not set
        """
        return self._data["Design Fan Power"]

    @design_fan_power.setter
    def design_fan_power(self, value=None):
        """  Corresponds to IDD Field `Design Fan Power`
        Enter the fan motor electric input power at design (max) air flow through the tower
        Standard conversion for horsepower is 1 HP = 745.7 W

        Args:
            value (float or "Autosize"): value for IDD Field `Design Fan Power`
                Units: W
                IP-Units: W
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Design Fan Power"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `design_fan_power`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `design_fan_power`')
        self._data["Design Fan Power"] = value

    @property
    def fan_power_ratio_function_of_air_flow_rate_ratio_curve_name(self):
        """Get fan_power_ratio_function_of_air_flow_rate_ratio_curve_name

        Returns:
            str: the value of `fan_power_ratio_function_of_air_flow_rate_ratio_curve_name` or None if not set
        """
        return self._data["Fan Power Ratio Function of Air Flow Rate Ratio Curve Name"]

    @fan_power_ratio_function_of_air_flow_rate_ratio_curve_name.setter
    def fan_power_ratio_function_of_air_flow_rate_ratio_curve_name(self, value=None):
        """  Corresponds to IDD Field `Fan Power Ratio Function of Air Flow Rate Ratio Curve Name`
        Table:OneIndependentVariable object can also be used
        FPR = a + b*AFR + c*AFR**2 + d*AFR**3
        FPR = fraction of the design fan power
        AFR = fraction of the design air flow rate
        If left blank, then fan power is assumed to be proportional to
        (air flow rate ratio)^3

        Args:
            value (str): value for IDD Field `Fan Power Ratio Function of Air Flow Rate Ratio Curve Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `fan_power_ratio_function_of_air_flow_rate_ratio_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `fan_power_ratio_function_of_air_flow_rate_ratio_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `fan_power_ratio_function_of_air_flow_rate_ratio_curve_name`')
        self._data["Fan Power Ratio Function of Air Flow Rate Ratio Curve Name"] = value

    @property
    def minimum_air_flow_rate_ratio(self):
        """Get minimum_air_flow_rate_ratio

        Returns:
            float: the value of `minimum_air_flow_rate_ratio` or None if not set
        """
        return self._data["Minimum Air Flow Rate Ratio"]

    @minimum_air_flow_rate_ratio.setter
    def minimum_air_flow_rate_ratio(self, value=0.2):
        """  Corresponds to IDD Field `Minimum Air Flow Rate Ratio`
        Enter the minimum air flow rate ratio. This is typically determined by the variable
        speed drive that controls the fan motor speed. Valid entries are from 0.2 to 0.5.

        Args:
            value (float): value for IDD Field `Minimum Air Flow Rate Ratio`
                Default value: 0.2
                value >= 0.2
                value <= 0.5
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `minimum_air_flow_rate_ratio`'.format(value))
            if value < 0.2:
                raise ValueError('value need to be greater or equal 0.2 '
                                 'for field `minimum_air_flow_rate_ratio`')
            if value > 0.5:
                raise ValueError('value need to be smaller 0.5 '
                                 'for field `minimum_air_flow_rate_ratio`')
        self._data["Minimum Air Flow Rate Ratio"] = value

    @property
    def fraction_of_tower_capacity_in_free_convection_regime(self):
        """Get fraction_of_tower_capacity_in_free_convection_regime

        Returns:
            float: the value of `fraction_of_tower_capacity_in_free_convection_regime` or None if not set
        """
        return self._data["Fraction of Tower Capacity in Free Convection Regime"]

    @fraction_of_tower_capacity_in_free_convection_regime.setter
    def fraction_of_tower_capacity_in_free_convection_regime(self, value=0.125):
        """  Corresponds to IDD Field `Fraction of Tower Capacity in Free Convection Regime`
        Enter the fraction of tower capacity in the free convection regime. This is the
        fraction of the tower capacity, at the current inlet air wet-bulb temperature,
        that is available when the tower fan is off. Manufacturers typically estimate the
        free convection capacity at approximately 10-15%. Values are entered as a fraction
        and can range from 0 to 0.2.

        Args:
            value (float): value for IDD Field `Fraction of Tower Capacity in Free Convection Regime`
                Default value: 0.125
                value >= 0.0
                value <= 0.2
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `fraction_of_tower_capacity_in_free_convection_regime`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `fraction_of_tower_capacity_in_free_convection_regime`')
            if value > 0.2:
                raise ValueError('value need to be smaller 0.2 '
                                 'for field `fraction_of_tower_capacity_in_free_convection_regime`')
        self._data["Fraction of Tower Capacity in Free Convection Regime"] = value

    @property
    def basin_heater_capacity(self):
        """Get basin_heater_capacity

        Returns:
            float: the value of `basin_heater_capacity` or None if not set
        """
        return self._data["Basin Heater Capacity"]

    @basin_heater_capacity.setter
    def basin_heater_capacity(self, value=0.0):
        """  Corresponds to IDD Field `Basin Heater Capacity`
        This heater maintains the basin water temperature at the basin heater setpoint
        temperature when the outdoor air temperature falls below the setpoint temperature.
        The basin heater only operates when water is not flowing through the tower.

        Args:
            value (float): value for IDD Field `Basin Heater Capacity`
                Units: W/K
                Default value: 0.0
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `basin_heater_capacity`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `basin_heater_capacity`')
        self._data["Basin Heater Capacity"] = value

    @property
    def basin_heater_setpoint_temperature(self):
        """Get basin_heater_setpoint_temperature

        Returns:
            float: the value of `basin_heater_setpoint_temperature` or None if not set
        """
        return self._data["Basin Heater Setpoint Temperature"]

    @basin_heater_setpoint_temperature.setter
    def basin_heater_setpoint_temperature(self, value=2.0):
        """  Corresponds to IDD Field `Basin Heater Setpoint Temperature`
        Enter the outdoor dry-bulb temperature when the basin heater turns on

        Args:
            value (float): value for IDD Field `Basin Heater Setpoint Temperature`
                Units: C
                Default value: 2.0
                value >= 2.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `basin_heater_setpoint_temperature`'.format(value))
            if value < 2.0:
                raise ValueError('value need to be greater or equal 2.0 '
                                 'for field `basin_heater_setpoint_temperature`')
        self._data["Basin Heater Setpoint Temperature"] = value

    @property
    def basin_heater_operating_schedule_name(self):
        """Get basin_heater_operating_schedule_name

        Returns:
            str: the value of `basin_heater_operating_schedule_name` or None if not set
        """
        return self._data["Basin Heater Operating Schedule Name"]

    @basin_heater_operating_schedule_name.setter
    def basin_heater_operating_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Basin Heater Operating Schedule Name`
        Schedule values greater than 0 allow the basin heater to operate whenever the outdoor
        air dry-bulb temperature is below the basin heater setpoint temperature.
        If a schedule name is not entered, the basin heater is allowed to operate
        throughout the entire simulation.

        Args:
            value (str): value for IDD Field `Basin Heater Operating Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `basin_heater_operating_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `basin_heater_operating_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `basin_heater_operating_schedule_name`')
        self._data["Basin Heater Operating Schedule Name"] = value

    @property
    def evaporation_loss_mode(self):
        """Get evaporation_loss_mode

        Returns:
            str: the value of `evaporation_loss_mode` or None if not set
        """
        return self._data["Evaporation Loss Mode"]

    @evaporation_loss_mode.setter
    def evaporation_loss_mode(self, value=None):
        """  Corresponds to IDD Field `Evaporation Loss Mode`

        Args:
            value (str): value for IDD Field `Evaporation Loss Mode`
                Accepted values are:
                      - LossFactor
                      - SaturatedExit
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `evaporation_loss_mode`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `evaporation_loss_mode`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `evaporation_loss_mode`')
            vals = {}
            vals["lossfactor"] = "LossFactor"
            vals["saturatedexit"] = "SaturatedExit"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `evaporation_loss_mode`'.format(value))
            value = vals[value_lower]
        self._data["Evaporation Loss Mode"] = value

    @property
    def evaporation_loss_factor(self):
        """Get evaporation_loss_factor

        Returns:
            float: the value of `evaporation_loss_factor` or None if not set
        """
        return self._data["Evaporation Loss Factor"]

    @evaporation_loss_factor.setter
    def evaporation_loss_factor(self, value=0.2):
        """  Corresponds to IDD Field `Evaporation Loss Factor`
        Rate of water evaporated from the cooling tower and lost to the outdoor air [%/K]
        Evaporation loss is calculated as percentage of the circulating condenser water rate
        Value entered here is percent-per-degree K of temperature drop in the condenser water
        Typical values are from 0.15 to 0.27 [percent/K].

        Args:
            value (float): value for IDD Field `Evaporation Loss Factor`
                Units: percent/K
                Default value: 0.2
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `evaporation_loss_factor`'.format(value))
        self._data["Evaporation Loss Factor"] = value

    @property
    def drift_loss_percent(self):
        """Get drift_loss_percent

        Returns:
            float: the value of `drift_loss_percent` or None if not set
        """
        return self._data["Drift Loss Percent"]

    @drift_loss_percent.setter
    def drift_loss_percent(self, value=None):
        """  Corresponds to IDD Field `Drift Loss Percent`
        Rate of drift loss as a percentage of circulating condenser water flow rate
        Typical values are between 0.002 and 0.2% The default value is 0.008%

        Args:
            value (float): value for IDD Field `Drift Loss Percent`
                Units: percent
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `drift_loss_percent`'.format(value))
        self._data["Drift Loss Percent"] = value

    @property
    def blowdown_calculation_mode(self):
        """Get blowdown_calculation_mode

        Returns:
            str: the value of `blowdown_calculation_mode` or None if not set
        """
        return self._data["Blowdown Calculation Mode"]

    @blowdown_calculation_mode.setter
    def blowdown_calculation_mode(self, value=None):
        """  Corresponds to IDD Field `Blowdown Calculation Mode`

        Args:
            value (str): value for IDD Field `Blowdown Calculation Mode`
                Accepted values are:
                      - ConcentrationRatio
                      - ScheduledRate
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `blowdown_calculation_mode`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `blowdown_calculation_mode`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `blowdown_calculation_mode`')
            vals = {}
            vals["concentrationratio"] = "ConcentrationRatio"
            vals["scheduledrate"] = "ScheduledRate"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `blowdown_calculation_mode`'.format(value))
            value = vals[value_lower]
        self._data["Blowdown Calculation Mode"] = value

    @property
    def blowdown_concentration_ratio(self):
        """Get blowdown_concentration_ratio

        Returns:
            float: the value of `blowdown_concentration_ratio` or None if not set
        """
        return self._data["Blowdown Concentration Ratio"]

    @blowdown_concentration_ratio.setter
    def blowdown_concentration_ratio(self, value=3.0):
        """  Corresponds to IDD Field `Blowdown Concentration Ratio`
        Characterizes the rate of blowdown in the cooling tower.
        Blowdown is water intentionally drained from the tower in order to offset the build up
        of solids in the water that would otherwise occur because of evaporation.
        Ratio of solids in the blowdown water to solids in the make up water.
        Typical values for tower operation are 3 to 5.  The default value is 3.

        Args:
            value (float): value for IDD Field `Blowdown Concentration Ratio`
                Default value: 3.0
                value >= 2.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `blowdown_concentration_ratio`'.format(value))
            if value < 2.0:
                raise ValueError('value need to be greater or equal 2.0 '
                                 'for field `blowdown_concentration_ratio`')
        self._data["Blowdown Concentration Ratio"] = value

    @property
    def blowdown_makeup_water_usage_schedule_name(self):
        """Get blowdown_makeup_water_usage_schedule_name

        Returns:
            str: the value of `blowdown_makeup_water_usage_schedule_name` or None if not set
        """
        return self._data["Blowdown Makeup Water Usage Schedule Name"]

    @blowdown_makeup_water_usage_schedule_name.setter
    def blowdown_makeup_water_usage_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Blowdown Makeup Water Usage Schedule Name`
        Makeup water usage due to blowdown results from occasionally draining a small amount
        of water in the tower basin to purge scale or other contaminants to reduce their
        concentration in order to maintain an acceptable level of water quality.
        Schedule values should reflect water usage in m3/s.

        Args:
            value (str): value for IDD Field `Blowdown Makeup Water Usage Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `blowdown_makeup_water_usage_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `blowdown_makeup_water_usage_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `blowdown_makeup_water_usage_schedule_name`')
        self._data["Blowdown Makeup Water Usage Schedule Name"] = value

    @property
    def supply_water_storage_tank_name(self):
        """Get supply_water_storage_tank_name

        Returns:
            str: the value of `supply_water_storage_tank_name` or None if not set
        """
        return self._data["Supply Water Storage Tank Name"]

    @supply_water_storage_tank_name.setter
    def supply_water_storage_tank_name(self, value=None):
        """  Corresponds to IDD Field `Supply Water Storage Tank Name`

        Args:
            value (str): value for IDD Field `Supply Water Storage Tank Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_water_storage_tank_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_water_storage_tank_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `supply_water_storage_tank_name`')
        self._data["Supply Water Storage Tank Name"] = value

    @property
    def outdoor_air_inlet_node_name(self):
        """Get outdoor_air_inlet_node_name

        Returns:
            str: the value of `outdoor_air_inlet_node_name` or None if not set
        """
        return self._data["Outdoor Air Inlet Node Name"]

    @outdoor_air_inlet_node_name.setter
    def outdoor_air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Outdoor Air Inlet Node Name`
        Enter the name of an outdoor air node

        Args:
            value (str): value for IDD Field `Outdoor Air Inlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `outdoor_air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outdoor_air_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `outdoor_air_inlet_node_name`')
        self._data["Outdoor Air Inlet Node Name"] = value

    @property
    def number_of_cells(self):
        """Get number_of_cells

        Returns:
            int: the value of `number_of_cells` or None if not set
        """
        return self._data["Number of Cells"]

    @number_of_cells.setter
    def number_of_cells(self, value=1):
        """  Corresponds to IDD Field `Number of Cells`

        Args:
            value (int): value for IDD Field `Number of Cells`
                Default value: 1
                value >= 1
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = int(value)
            except ValueError:
                raise ValueError('value {} need to be of type int '
                                 'for field `number_of_cells`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `number_of_cells`')
        self._data["Number of Cells"] = value

    @property
    def cell_control(self):
        """Get cell_control

        Returns:
            str: the value of `cell_control` or None if not set
        """
        return self._data["Cell Control"]

    @cell_control.setter
    def cell_control(self, value="MinimalCell"):
        """  Corresponds to IDD Field `Cell Control`

        Args:
            value (str): value for IDD Field `Cell Control`
                Default value: MinimalCell
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `cell_control`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `cell_control`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `cell_control`')
        self._data["Cell Control"] = value

    @property
    def cell_minimum_water_flow_rate_fraction(self):
        """Get cell_minimum_water_flow_rate_fraction

        Returns:
            float: the value of `cell_minimum_water_flow_rate_fraction` or None if not set
        """
        return self._data["Cell Minimum  Water Flow Rate Fraction"]

    @cell_minimum_water_flow_rate_fraction.setter
    def cell_minimum_water_flow_rate_fraction(self, value=0.33):
        """  Corresponds to IDD Field `Cell Minimum  Water Flow Rate Fraction`
        The allowable mininal fraction of the nominal flow rate per cell

        Args:
            value (float): value for IDD Field `Cell Minimum  Water Flow Rate Fraction`
                Default value: 0.33
                value > 0.0
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `cell_minimum_water_flow_rate_fraction`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `cell_minimum_water_flow_rate_fraction`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `cell_minimum_water_flow_rate_fraction`')
        self._data["Cell Minimum  Water Flow Rate Fraction"] = value

    @property
    def cell_maximum_water_flow_rate_fraction(self):
        """Get cell_maximum_water_flow_rate_fraction

        Returns:
            float: the value of `cell_maximum_water_flow_rate_fraction` or None if not set
        """
        return self._data["Cell Maximum Water Flow Rate Fraction"]

    @cell_maximum_water_flow_rate_fraction.setter
    def cell_maximum_water_flow_rate_fraction(self, value=2.5):
        """  Corresponds to IDD Field `Cell Maximum Water Flow Rate Fraction`
        The allowable maximal fraction of the nominal flow rate per cell

        Args:
            value (float): value for IDD Field `Cell Maximum Water Flow Rate Fraction`
                Default value: 2.5
                value >= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `cell_maximum_water_flow_rate_fraction`'.format(value))
            if value < 1.0:
                raise ValueError('value need to be greater or equal 1.0 '
                                 'for field `cell_maximum_water_flow_rate_fraction`')
        self._data["Cell Maximum Water Flow Rate Fraction"] = value

    @property
    def sizing_factor(self):
        """Get sizing_factor

        Returns:
            float: the value of `sizing_factor` or None if not set
        """
        return self._data["Sizing Factor"]

    @sizing_factor.setter
    def sizing_factor(self, value=1.0):
        """  Corresponds to IDD Field `Sizing Factor`
        Multiplies the autosized capacity and flow rates

        Args:
            value (float): value for IDD Field `Sizing Factor`
                Default value: 1.0
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `sizing_factor`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `sizing_factor`')
        self._data["Sizing Factor"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
        return good

    @classmethod
    def _to_str(cls, value):
        """ Represents values either as string or None values as empty string

        Args:
            value: a value
        """
        if value is None:
            return ''
        else:
            return str(value)

    def export(self):
        """ Export values of data object as list of strings"""
        out = []
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class CoolingTowerPerformanceCoolTools(object):
    """ Corresponds to IDD object `CoolingTowerPerformance:CoolTools`
        This object is used to define coefficients for the approach temperature
        correlation for a variable speed cooling tower when tower Model Type is
        specified as CoolToolsUserDefined in the object CoolingTower:VariableSpeed.
    
    """
    internal_name = "CoolingTowerPerformance:CoolTools"
    field_count = 44
    required_fields = ["Name", "Minimum Inlet Air Wet-Bulb Temperature", "Maximum Inlet Air Wet-Bulb Temperature", "Minimum Range Temperature", "Maximum Range Temperature", "Minimum Approach Temperature", "Maximum Approach Temperature", "Minimum Water Flow Rate Ratio", "Maximum Water Flow Rate Ratio", "Coefficient 1", "Coefficient 2", "Coefficient 3", "Coefficient 4", "Coefficient 5", "Coefficient 6", "Coefficient 7", "Coefficient 8", "Coefficient 9", "Coefficient 10", "Coefficient 11", "Coefficient 12", "Coefficient 13", "Coefficient 14", "Coefficient 15", "Coefficient 16", "Coefficient 17", "Coefficient 18", "Coefficient 19", "Coefficient 20", "Coefficient 21", "Coefficient 22", "Coefficient 23", "Coefficient 24", "Coefficient 25", "Coefficient 26", "Coefficient 27", "Coefficient 28", "Coefficient 29", "Coefficient 30", "Coefficient 31", "Coefficient 32", "Coefficient 33", "Coefficient 34", "Coefficient 35"]

    def __init__(self):
        """ Init data dictionary object for IDD  `CoolingTowerPerformance:CoolTools`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Minimum Inlet Air Wet-Bulb Temperature"] = None
        self._data["Maximum Inlet Air Wet-Bulb Temperature"] = None
        self._data["Minimum Range Temperature"] = None
        self._data["Maximum Range Temperature"] = None
        self._data["Minimum Approach Temperature"] = None
        self._data["Maximum Approach Temperature"] = None
        self._data["Minimum Water Flow Rate Ratio"] = None
        self._data["Maximum Water Flow Rate Ratio"] = None
        self._data["Coefficient 1"] = None
        self._data["Coefficient 2"] = None
        self._data["Coefficient 3"] = None
        self._data["Coefficient 4"] = None
        self._data["Coefficient 5"] = None
        self._data["Coefficient 6"] = None
        self._data["Coefficient 7"] = None
        self._data["Coefficient 8"] = None
        self._data["Coefficient 9"] = None
        self._data["Coefficient 10"] = None
        self._data["Coefficient 11"] = None
        self._data["Coefficient 12"] = None
        self._data["Coefficient 13"] = None
        self._data["Coefficient 14"] = None
        self._data["Coefficient 15"] = None
        self._data["Coefficient 16"] = None
        self._data["Coefficient 17"] = None
        self._data["Coefficient 18"] = None
        self._data["Coefficient 19"] = None
        self._data["Coefficient 20"] = None
        self._data["Coefficient 21"] = None
        self._data["Coefficient 22"] = None
        self._data["Coefficient 23"] = None
        self._data["Coefficient 24"] = None
        self._data["Coefficient 25"] = None
        self._data["Coefficient 26"] = None
        self._data["Coefficient 27"] = None
        self._data["Coefficient 28"] = None
        self._data["Coefficient 29"] = None
        self._data["Coefficient 30"] = None
        self._data["Coefficient 31"] = None
        self._data["Coefficient 32"] = None
        self._data["Coefficient 33"] = None
        self._data["Coefficient 34"] = None
        self._data["Coefficient 35"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_inlet_air_wetbulb_temperature = None
        else:
            self.minimum_inlet_air_wetbulb_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_inlet_air_wetbulb_temperature = None
        else:
            self.maximum_inlet_air_wetbulb_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_range_temperature = None
        else:
            self.minimum_range_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_range_temperature = None
        else:
            self.maximum_range_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_approach_temperature = None
        else:
            self.minimum_approach_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_approach_temperature = None
        else:
            self.maximum_approach_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_water_flow_rate_ratio = None
        else:
            self.minimum_water_flow_rate_ratio = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_water_flow_rate_ratio = None
        else:
            self.maximum_water_flow_rate_ratio = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient_1 = None
        else:
            self.coefficient_1 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient_2 = None
        else:
            self.coefficient_2 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient_3 = None
        else:
            self.coefficient_3 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient_4 = None
        else:
            self.coefficient_4 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient_5 = None
        else:
            self.coefficient_5 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient_6 = None
        else:
            self.coefficient_6 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient_7 = None
        else:
            self.coefficient_7 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient_8 = None
        else:
            self.coefficient_8 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient_9 = None
        else:
            self.coefficient_9 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient_10 = None
        else:
            self.coefficient_10 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient_11 = None
        else:
            self.coefficient_11 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient_12 = None
        else:
            self.coefficient_12 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient_13 = None
        else:
            self.coefficient_13 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient_14 = None
        else:
            self.coefficient_14 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient_15 = None
        else:
            self.coefficient_15 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient_16 = None
        else:
            self.coefficient_16 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient_17 = None
        else:
            self.coefficient_17 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient_18 = None
        else:
            self.coefficient_18 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient_19 = None
        else:
            self.coefficient_19 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient_20 = None
        else:
            self.coefficient_20 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient_21 = None
        else:
            self.coefficient_21 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient_22 = None
        else:
            self.coefficient_22 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient_23 = None
        else:
            self.coefficient_23 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient_24 = None
        else:
            self.coefficient_24 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient_25 = None
        else:
            self.coefficient_25 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient_26 = None
        else:
            self.coefficient_26 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient_27 = None
        else:
            self.coefficient_27 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient_28 = None
        else:
            self.coefficient_28 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient_29 = None
        else:
            self.coefficient_29 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient_30 = None
        else:
            self.coefficient_30 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient_31 = None
        else:
            self.coefficient_31 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient_32 = None
        else:
            self.coefficient_32 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient_33 = None
        else:
            self.coefficient_33 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient_34 = None
        else:
            self.coefficient_34 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient_35 = None
        else:
            self.coefficient_35 = vals[i]
        i += 1
        if i >= len(vals):
            return

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `Name`

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')
        self._data["Name"] = value

    @property
    def minimum_inlet_air_wetbulb_temperature(self):
        """Get minimum_inlet_air_wetbulb_temperature

        Returns:
            float: the value of `minimum_inlet_air_wetbulb_temperature` or None if not set
        """
        return self._data["Minimum Inlet Air Wet-Bulb Temperature"]

    @minimum_inlet_air_wetbulb_temperature.setter
    def minimum_inlet_air_wetbulb_temperature(self, value=None):
        """  Corresponds to IDD Field `Minimum Inlet Air Wet-Bulb Temperature`
        Minimum valid inlet air wet-bulb temperature for this approach
        temperature correlation.

        Args:
            value (float): value for IDD Field `Minimum Inlet Air Wet-Bulb Temperature`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `minimum_inlet_air_wetbulb_temperature`'.format(value))
        self._data["Minimum Inlet Air Wet-Bulb Temperature"] = value

    @property
    def maximum_inlet_air_wetbulb_temperature(self):
        """Get maximum_inlet_air_wetbulb_temperature

        Returns:
            float: the value of `maximum_inlet_air_wetbulb_temperature` or None if not set
        """
        return self._data["Maximum Inlet Air Wet-Bulb Temperature"]

    @maximum_inlet_air_wetbulb_temperature.setter
    def maximum_inlet_air_wetbulb_temperature(self, value=None):
        """  Corresponds to IDD Field `Maximum Inlet Air Wet-Bulb Temperature`
        Maximum valid inlet air wet-bulb temperature for this approach
        temperature correlation.

        Args:
            value (float): value for IDD Field `Maximum Inlet Air Wet-Bulb Temperature`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_inlet_air_wetbulb_temperature`'.format(value))
        self._data["Maximum Inlet Air Wet-Bulb Temperature"] = value

    @property
    def minimum_range_temperature(self):
        """Get minimum_range_temperature

        Returns:
            float: the value of `minimum_range_temperature` or None if not set
        """
        return self._data["Minimum Range Temperature"]

    @minimum_range_temperature.setter
    def minimum_range_temperature(self, value=None):
        """  Corresponds to IDD Field `Minimum Range Temperature`
        Minimum valid range temperature for this approach temperature
        correlation.

        Args:
            value (float): value for IDD Field `Minimum Range Temperature`
                Units: deltaC
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `minimum_range_temperature`'.format(value))
        self._data["Minimum Range Temperature"] = value

    @property
    def maximum_range_temperature(self):
        """Get maximum_range_temperature

        Returns:
            float: the value of `maximum_range_temperature` or None if not set
        """
        return self._data["Maximum Range Temperature"]

    @maximum_range_temperature.setter
    def maximum_range_temperature(self, value=None):
        """  Corresponds to IDD Field `Maximum Range Temperature`
        Maximum valid range temperature for this approach temperature
        correlation.

        Args:
            value (float): value for IDD Field `Maximum Range Temperature`
                Units: deltaC
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_range_temperature`'.format(value))
        self._data["Maximum Range Temperature"] = value

    @property
    def minimum_approach_temperature(self):
        """Get minimum_approach_temperature

        Returns:
            float: the value of `minimum_approach_temperature` or None if not set
        """
        return self._data["Minimum Approach Temperature"]

    @minimum_approach_temperature.setter
    def minimum_approach_temperature(self, value=None):
        """  Corresponds to IDD Field `Minimum Approach Temperature`
        Minimum valid approach temperature for this correlation.

        Args:
            value (float): value for IDD Field `Minimum Approach Temperature`
                Units: deltaC
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `minimum_approach_temperature`'.format(value))
        self._data["Minimum Approach Temperature"] = value

    @property
    def maximum_approach_temperature(self):
        """Get maximum_approach_temperature

        Returns:
            float: the value of `maximum_approach_temperature` or None if not set
        """
        return self._data["Maximum Approach Temperature"]

    @maximum_approach_temperature.setter
    def maximum_approach_temperature(self, value=None):
        """  Corresponds to IDD Field `Maximum Approach Temperature`
        Maximum valid approach temperature for this correlation.

        Args:
            value (float): value for IDD Field `Maximum Approach Temperature`
                Units: deltaC
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_approach_temperature`'.format(value))
        self._data["Maximum Approach Temperature"] = value

    @property
    def minimum_water_flow_rate_ratio(self):
        """Get minimum_water_flow_rate_ratio

        Returns:
            float: the value of `minimum_water_flow_rate_ratio` or None if not set
        """
        return self._data["Minimum Water Flow Rate Ratio"]

    @minimum_water_flow_rate_ratio.setter
    def minimum_water_flow_rate_ratio(self, value=None):
        """  Corresponds to IDD Field `Minimum Water Flow Rate Ratio`
        Minimum valid water flow rate ratio for this approach
        temperature correlation.

        Args:
            value (float): value for IDD Field `Minimum Water Flow Rate Ratio`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `minimum_water_flow_rate_ratio`'.format(value))
        self._data["Minimum Water Flow Rate Ratio"] = value

    @property
    def maximum_water_flow_rate_ratio(self):
        """Get maximum_water_flow_rate_ratio

        Returns:
            float: the value of `maximum_water_flow_rate_ratio` or None if not set
        """
        return self._data["Maximum Water Flow Rate Ratio"]

    @maximum_water_flow_rate_ratio.setter
    def maximum_water_flow_rate_ratio(self, value=None):
        """  Corresponds to IDD Field `Maximum Water Flow Rate Ratio`
        Maximum valid water flow rate ratio for this approach
        temperature correlation.

        Args:
            value (float): value for IDD Field `Maximum Water Flow Rate Ratio`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_water_flow_rate_ratio`'.format(value))
        self._data["Maximum Water Flow Rate Ratio"] = value

    @property
    def coefficient_1(self):
        """Get coefficient_1

        Returns:
            float: the value of `coefficient_1` or None if not set
        """
        return self._data["Coefficient 1"]

    @coefficient_1.setter
    def coefficient_1(self, value=None):
        """  Corresponds to IDD Field `Coefficient 1`

        Args:
            value (float): value for IDD Field `Coefficient 1`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient_1`'.format(value))
        self._data["Coefficient 1"] = value

    @property
    def coefficient_2(self):
        """Get coefficient_2

        Returns:
            float: the value of `coefficient_2` or None if not set
        """
        return self._data["Coefficient 2"]

    @coefficient_2.setter
    def coefficient_2(self, value=None):
        """  Corresponds to IDD Field `Coefficient 2`

        Args:
            value (float): value for IDD Field `Coefficient 2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient_2`'.format(value))
        self._data["Coefficient 2"] = value

    @property
    def coefficient_3(self):
        """Get coefficient_3

        Returns:
            float: the value of `coefficient_3` or None if not set
        """
        return self._data["Coefficient 3"]

    @coefficient_3.setter
    def coefficient_3(self, value=None):
        """  Corresponds to IDD Field `Coefficient 3`

        Args:
            value (float): value for IDD Field `Coefficient 3`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient_3`'.format(value))
        self._data["Coefficient 3"] = value

    @property
    def coefficient_4(self):
        """Get coefficient_4

        Returns:
            float: the value of `coefficient_4` or None if not set
        """
        return self._data["Coefficient 4"]

    @coefficient_4.setter
    def coefficient_4(self, value=None):
        """  Corresponds to IDD Field `Coefficient 4`

        Args:
            value (float): value for IDD Field `Coefficient 4`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient_4`'.format(value))
        self._data["Coefficient 4"] = value

    @property
    def coefficient_5(self):
        """Get coefficient_5

        Returns:
            float: the value of `coefficient_5` or None if not set
        """
        return self._data["Coefficient 5"]

    @coefficient_5.setter
    def coefficient_5(self, value=None):
        """  Corresponds to IDD Field `Coefficient 5`

        Args:
            value (float): value for IDD Field `Coefficient 5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient_5`'.format(value))
        self._data["Coefficient 5"] = value

    @property
    def coefficient_6(self):
        """Get coefficient_6

        Returns:
            float: the value of `coefficient_6` or None if not set
        """
        return self._data["Coefficient 6"]

    @coefficient_6.setter
    def coefficient_6(self, value=None):
        """  Corresponds to IDD Field `Coefficient 6`

        Args:
            value (float): value for IDD Field `Coefficient 6`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient_6`'.format(value))
        self._data["Coefficient 6"] = value

    @property
    def coefficient_7(self):
        """Get coefficient_7

        Returns:
            float: the value of `coefficient_7` or None if not set
        """
        return self._data["Coefficient 7"]

    @coefficient_7.setter
    def coefficient_7(self, value=None):
        """  Corresponds to IDD Field `Coefficient 7`

        Args:
            value (float): value for IDD Field `Coefficient 7`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient_7`'.format(value))
        self._data["Coefficient 7"] = value

    @property
    def coefficient_8(self):
        """Get coefficient_8

        Returns:
            float: the value of `coefficient_8` or None if not set
        """
        return self._data["Coefficient 8"]

    @coefficient_8.setter
    def coefficient_8(self, value=None):
        """  Corresponds to IDD Field `Coefficient 8`

        Args:
            value (float): value for IDD Field `Coefficient 8`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient_8`'.format(value))
        self._data["Coefficient 8"] = value

    @property
    def coefficient_9(self):
        """Get coefficient_9

        Returns:
            float: the value of `coefficient_9` or None if not set
        """
        return self._data["Coefficient 9"]

    @coefficient_9.setter
    def coefficient_9(self, value=None):
        """  Corresponds to IDD Field `Coefficient 9`

        Args:
            value (float): value for IDD Field `Coefficient 9`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient_9`'.format(value))
        self._data["Coefficient 9"] = value

    @property
    def coefficient_10(self):
        """Get coefficient_10

        Returns:
            float: the value of `coefficient_10` or None if not set
        """
        return self._data["Coefficient 10"]

    @coefficient_10.setter
    def coefficient_10(self, value=None):
        """  Corresponds to IDD Field `Coefficient 10`

        Args:
            value (float): value for IDD Field `Coefficient 10`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient_10`'.format(value))
        self._data["Coefficient 10"] = value

    @property
    def coefficient_11(self):
        """Get coefficient_11

        Returns:
            float: the value of `coefficient_11` or None if not set
        """
        return self._data["Coefficient 11"]

    @coefficient_11.setter
    def coefficient_11(self, value=None):
        """  Corresponds to IDD Field `Coefficient 11`

        Args:
            value (float): value for IDD Field `Coefficient 11`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient_11`'.format(value))
        self._data["Coefficient 11"] = value

    @property
    def coefficient_12(self):
        """Get coefficient_12

        Returns:
            float: the value of `coefficient_12` or None if not set
        """
        return self._data["Coefficient 12"]

    @coefficient_12.setter
    def coefficient_12(self, value=None):
        """  Corresponds to IDD Field `Coefficient 12`

        Args:
            value (float): value for IDD Field `Coefficient 12`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient_12`'.format(value))
        self._data["Coefficient 12"] = value

    @property
    def coefficient_13(self):
        """Get coefficient_13

        Returns:
            float: the value of `coefficient_13` or None if not set
        """
        return self._data["Coefficient 13"]

    @coefficient_13.setter
    def coefficient_13(self, value=None):
        """  Corresponds to IDD Field `Coefficient 13`

        Args:
            value (float): value for IDD Field `Coefficient 13`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient_13`'.format(value))
        self._data["Coefficient 13"] = value

    @property
    def coefficient_14(self):
        """Get coefficient_14

        Returns:
            float: the value of `coefficient_14` or None if not set
        """
        return self._data["Coefficient 14"]

    @coefficient_14.setter
    def coefficient_14(self, value=None):
        """  Corresponds to IDD Field `Coefficient 14`

        Args:
            value (float): value for IDD Field `Coefficient 14`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient_14`'.format(value))
        self._data["Coefficient 14"] = value

    @property
    def coefficient_15(self):
        """Get coefficient_15

        Returns:
            float: the value of `coefficient_15` or None if not set
        """
        return self._data["Coefficient 15"]

    @coefficient_15.setter
    def coefficient_15(self, value=None):
        """  Corresponds to IDD Field `Coefficient 15`

        Args:
            value (float): value for IDD Field `Coefficient 15`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient_15`'.format(value))
        self._data["Coefficient 15"] = value

    @property
    def coefficient_16(self):
        """Get coefficient_16

        Returns:
            float: the value of `coefficient_16` or None if not set
        """
        return self._data["Coefficient 16"]

    @coefficient_16.setter
    def coefficient_16(self, value=None):
        """  Corresponds to IDD Field `Coefficient 16`

        Args:
            value (float): value for IDD Field `Coefficient 16`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient_16`'.format(value))
        self._data["Coefficient 16"] = value

    @property
    def coefficient_17(self):
        """Get coefficient_17

        Returns:
            float: the value of `coefficient_17` or None if not set
        """
        return self._data["Coefficient 17"]

    @coefficient_17.setter
    def coefficient_17(self, value=None):
        """  Corresponds to IDD Field `Coefficient 17`

        Args:
            value (float): value for IDD Field `Coefficient 17`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient_17`'.format(value))
        self._data["Coefficient 17"] = value

    @property
    def coefficient_18(self):
        """Get coefficient_18

        Returns:
            float: the value of `coefficient_18` or None if not set
        """
        return self._data["Coefficient 18"]

    @coefficient_18.setter
    def coefficient_18(self, value=None):
        """  Corresponds to IDD Field `Coefficient 18`

        Args:
            value (float): value for IDD Field `Coefficient 18`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient_18`'.format(value))
        self._data["Coefficient 18"] = value

    @property
    def coefficient_19(self):
        """Get coefficient_19

        Returns:
            float: the value of `coefficient_19` or None if not set
        """
        return self._data["Coefficient 19"]

    @coefficient_19.setter
    def coefficient_19(self, value=None):
        """  Corresponds to IDD Field `Coefficient 19`

        Args:
            value (float): value for IDD Field `Coefficient 19`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient_19`'.format(value))
        self._data["Coefficient 19"] = value

    @property
    def coefficient_20(self):
        """Get coefficient_20

        Returns:
            float: the value of `coefficient_20` or None if not set
        """
        return self._data["Coefficient 20"]

    @coefficient_20.setter
    def coefficient_20(self, value=None):
        """  Corresponds to IDD Field `Coefficient 20`

        Args:
            value (float): value for IDD Field `Coefficient 20`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient_20`'.format(value))
        self._data["Coefficient 20"] = value

    @property
    def coefficient_21(self):
        """Get coefficient_21

        Returns:
            float: the value of `coefficient_21` or None if not set
        """
        return self._data["Coefficient 21"]

    @coefficient_21.setter
    def coefficient_21(self, value=None):
        """  Corresponds to IDD Field `Coefficient 21`

        Args:
            value (float): value for IDD Field `Coefficient 21`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient_21`'.format(value))
        self._data["Coefficient 21"] = value

    @property
    def coefficient_22(self):
        """Get coefficient_22

        Returns:
            float: the value of `coefficient_22` or None if not set
        """
        return self._data["Coefficient 22"]

    @coefficient_22.setter
    def coefficient_22(self, value=None):
        """  Corresponds to IDD Field `Coefficient 22`

        Args:
            value (float): value for IDD Field `Coefficient 22`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient_22`'.format(value))
        self._data["Coefficient 22"] = value

    @property
    def coefficient_23(self):
        """Get coefficient_23

        Returns:
            float: the value of `coefficient_23` or None if not set
        """
        return self._data["Coefficient 23"]

    @coefficient_23.setter
    def coefficient_23(self, value=None):
        """  Corresponds to IDD Field `Coefficient 23`

        Args:
            value (float): value for IDD Field `Coefficient 23`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient_23`'.format(value))
        self._data["Coefficient 23"] = value

    @property
    def coefficient_24(self):
        """Get coefficient_24

        Returns:
            float: the value of `coefficient_24` or None if not set
        """
        return self._data["Coefficient 24"]

    @coefficient_24.setter
    def coefficient_24(self, value=None):
        """  Corresponds to IDD Field `Coefficient 24`

        Args:
            value (float): value for IDD Field `Coefficient 24`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient_24`'.format(value))
        self._data["Coefficient 24"] = value

    @property
    def coefficient_25(self):
        """Get coefficient_25

        Returns:
            float: the value of `coefficient_25` or None if not set
        """
        return self._data["Coefficient 25"]

    @coefficient_25.setter
    def coefficient_25(self, value=None):
        """  Corresponds to IDD Field `Coefficient 25`

        Args:
            value (float): value for IDD Field `Coefficient 25`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient_25`'.format(value))
        self._data["Coefficient 25"] = value

    @property
    def coefficient_26(self):
        """Get coefficient_26

        Returns:
            float: the value of `coefficient_26` or None if not set
        """
        return self._data["Coefficient 26"]

    @coefficient_26.setter
    def coefficient_26(self, value=None):
        """  Corresponds to IDD Field `Coefficient 26`

        Args:
            value (float): value for IDD Field `Coefficient 26`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient_26`'.format(value))
        self._data["Coefficient 26"] = value

    @property
    def coefficient_27(self):
        """Get coefficient_27

        Returns:
            float: the value of `coefficient_27` or None if not set
        """
        return self._data["Coefficient 27"]

    @coefficient_27.setter
    def coefficient_27(self, value=None):
        """  Corresponds to IDD Field `Coefficient 27`

        Args:
            value (float): value for IDD Field `Coefficient 27`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient_27`'.format(value))
        self._data["Coefficient 27"] = value

    @property
    def coefficient_28(self):
        """Get coefficient_28

        Returns:
            float: the value of `coefficient_28` or None if not set
        """
        return self._data["Coefficient 28"]

    @coefficient_28.setter
    def coefficient_28(self, value=None):
        """  Corresponds to IDD Field `Coefficient 28`

        Args:
            value (float): value for IDD Field `Coefficient 28`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient_28`'.format(value))
        self._data["Coefficient 28"] = value

    @property
    def coefficient_29(self):
        """Get coefficient_29

        Returns:
            float: the value of `coefficient_29` or None if not set
        """
        return self._data["Coefficient 29"]

    @coefficient_29.setter
    def coefficient_29(self, value=None):
        """  Corresponds to IDD Field `Coefficient 29`

        Args:
            value (float): value for IDD Field `Coefficient 29`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient_29`'.format(value))
        self._data["Coefficient 29"] = value

    @property
    def coefficient_30(self):
        """Get coefficient_30

        Returns:
            float: the value of `coefficient_30` or None if not set
        """
        return self._data["Coefficient 30"]

    @coefficient_30.setter
    def coefficient_30(self, value=None):
        """  Corresponds to IDD Field `Coefficient 30`

        Args:
            value (float): value for IDD Field `Coefficient 30`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient_30`'.format(value))
        self._data["Coefficient 30"] = value

    @property
    def coefficient_31(self):
        """Get coefficient_31

        Returns:
            float: the value of `coefficient_31` or None if not set
        """
        return self._data["Coefficient 31"]

    @coefficient_31.setter
    def coefficient_31(self, value=None):
        """  Corresponds to IDD Field `Coefficient 31`

        Args:
            value (float): value for IDD Field `Coefficient 31`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient_31`'.format(value))
        self._data["Coefficient 31"] = value

    @property
    def coefficient_32(self):
        """Get coefficient_32

        Returns:
            float: the value of `coefficient_32` or None if not set
        """
        return self._data["Coefficient 32"]

    @coefficient_32.setter
    def coefficient_32(self, value=None):
        """  Corresponds to IDD Field `Coefficient 32`

        Args:
            value (float): value for IDD Field `Coefficient 32`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient_32`'.format(value))
        self._data["Coefficient 32"] = value

    @property
    def coefficient_33(self):
        """Get coefficient_33

        Returns:
            float: the value of `coefficient_33` or None if not set
        """
        return self._data["Coefficient 33"]

    @coefficient_33.setter
    def coefficient_33(self, value=None):
        """  Corresponds to IDD Field `Coefficient 33`

        Args:
            value (float): value for IDD Field `Coefficient 33`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient_33`'.format(value))
        self._data["Coefficient 33"] = value

    @property
    def coefficient_34(self):
        """Get coefficient_34

        Returns:
            float: the value of `coefficient_34` or None if not set
        """
        return self._data["Coefficient 34"]

    @coefficient_34.setter
    def coefficient_34(self, value=None):
        """  Corresponds to IDD Field `Coefficient 34`

        Args:
            value (float): value for IDD Field `Coefficient 34`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient_34`'.format(value))
        self._data["Coefficient 34"] = value

    @property
    def coefficient_35(self):
        """Get coefficient_35

        Returns:
            float: the value of `coefficient_35` or None if not set
        """
        return self._data["Coefficient 35"]

    @coefficient_35.setter
    def coefficient_35(self, value=None):
        """  Corresponds to IDD Field `Coefficient 35`

        Args:
            value (float): value for IDD Field `Coefficient 35`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient_35`'.format(value))
        self._data["Coefficient 35"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
        return good

    @classmethod
    def _to_str(cls, value):
        """ Represents values either as string or None values as empty string

        Args:
            value: a value
        """
        if value is None:
            return ''
        else:
            return str(value)

    def export(self):
        """ Export values of data object as list of strings"""
        out = []
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class CoolingTowerPerformanceYorkCalc(object):
    """ Corresponds to IDD object `CoolingTowerPerformance:YorkCalc`
        This object is used to define coefficients for the approach temperature
        correlation for a variable speed cooling tower when tower Model Type is
        specified as YorkCalcUserDefined in the object CoolingTower:VariableSpeed.
    
    """
    internal_name = "CoolingTowerPerformance:YorkCalc"
    field_count = 37
    required_fields = ["Name", "Minimum Inlet Air Wet-Bulb Temperature", "Maximum Inlet Air Wet-Bulb Temperature", "Minimum Range Temperature", "Maximum Range Temperature", "Minimum Approach Temperature", "Maximum Approach Temperature", "Minimum Water Flow Rate Ratio", "Maximum Water Flow Rate Ratio", "Maximum Liquid to Gas Ratio", "Coefficient 1", "Coefficient 2", "Coefficient 3", "Coefficient 4", "Coefficient 5", "Coefficient 6", "Coefficient 7", "Coefficient 8", "Coefficient 9", "Coefficient 10", "Coefficient 11", "Coefficient 12", "Coefficient 13", "Coefficient 14", "Coefficient 15", "Coefficient 16", "Coefficient 17", "Coefficient 18", "Coefficient 19", "Coefficient 20", "Coefficient 21", "Coefficient 22", "Coefficient 23", "Coefficient 24", "Coefficient 25", "Coefficient 26", "Coefficient 27"]

    def __init__(self):
        """ Init data dictionary object for IDD  `CoolingTowerPerformance:YorkCalc`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Minimum Inlet Air Wet-Bulb Temperature"] = None
        self._data["Maximum Inlet Air Wet-Bulb Temperature"] = None
        self._data["Minimum Range Temperature"] = None
        self._data["Maximum Range Temperature"] = None
        self._data["Minimum Approach Temperature"] = None
        self._data["Maximum Approach Temperature"] = None
        self._data["Minimum Water Flow Rate Ratio"] = None
        self._data["Maximum Water Flow Rate Ratio"] = None
        self._data["Maximum Liquid to Gas Ratio"] = None
        self._data["Coefficient 1"] = None
        self._data["Coefficient 2"] = None
        self._data["Coefficient 3"] = None
        self._data["Coefficient 4"] = None
        self._data["Coefficient 5"] = None
        self._data["Coefficient 6"] = None
        self._data["Coefficient 7"] = None
        self._data["Coefficient 8"] = None
        self._data["Coefficient 9"] = None
        self._data["Coefficient 10"] = None
        self._data["Coefficient 11"] = None
        self._data["Coefficient 12"] = None
        self._data["Coefficient 13"] = None
        self._data["Coefficient 14"] = None
        self._data["Coefficient 15"] = None
        self._data["Coefficient 16"] = None
        self._data["Coefficient 17"] = None
        self._data["Coefficient 18"] = None
        self._data["Coefficient 19"] = None
        self._data["Coefficient 20"] = None
        self._data["Coefficient 21"] = None
        self._data["Coefficient 22"] = None
        self._data["Coefficient 23"] = None
        self._data["Coefficient 24"] = None
        self._data["Coefficient 25"] = None
        self._data["Coefficient 26"] = None
        self._data["Coefficient 27"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_inlet_air_wetbulb_temperature = None
        else:
            self.minimum_inlet_air_wetbulb_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_inlet_air_wetbulb_temperature = None
        else:
            self.maximum_inlet_air_wetbulb_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_range_temperature = None
        else:
            self.minimum_range_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_range_temperature = None
        else:
            self.maximum_range_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_approach_temperature = None
        else:
            self.minimum_approach_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_approach_temperature = None
        else:
            self.maximum_approach_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_water_flow_rate_ratio = None
        else:
            self.minimum_water_flow_rate_ratio = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_water_flow_rate_ratio = None
        else:
            self.maximum_water_flow_rate_ratio = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_liquid_to_gas_ratio = None
        else:
            self.maximum_liquid_to_gas_ratio = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient_1 = None
        else:
            self.coefficient_1 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient_2 = None
        else:
            self.coefficient_2 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient_3 = None
        else:
            self.coefficient_3 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient_4 = None
        else:
            self.coefficient_4 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient_5 = None
        else:
            self.coefficient_5 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient_6 = None
        else:
            self.coefficient_6 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient_7 = None
        else:
            self.coefficient_7 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient_8 = None
        else:
            self.coefficient_8 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient_9 = None
        else:
            self.coefficient_9 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient_10 = None
        else:
            self.coefficient_10 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient_11 = None
        else:
            self.coefficient_11 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient_12 = None
        else:
            self.coefficient_12 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient_13 = None
        else:
            self.coefficient_13 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient_14 = None
        else:
            self.coefficient_14 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient_15 = None
        else:
            self.coefficient_15 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient_16 = None
        else:
            self.coefficient_16 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient_17 = None
        else:
            self.coefficient_17 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient_18 = None
        else:
            self.coefficient_18 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient_19 = None
        else:
            self.coefficient_19 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient_20 = None
        else:
            self.coefficient_20 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient_21 = None
        else:
            self.coefficient_21 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient_22 = None
        else:
            self.coefficient_22 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient_23 = None
        else:
            self.coefficient_23 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient_24 = None
        else:
            self.coefficient_24 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient_25 = None
        else:
            self.coefficient_25 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient_26 = None
        else:
            self.coefficient_26 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient_27 = None
        else:
            self.coefficient_27 = vals[i]
        i += 1
        if i >= len(vals):
            return

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `Name`

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')
        self._data["Name"] = value

    @property
    def minimum_inlet_air_wetbulb_temperature(self):
        """Get minimum_inlet_air_wetbulb_temperature

        Returns:
            float: the value of `minimum_inlet_air_wetbulb_temperature` or None if not set
        """
        return self._data["Minimum Inlet Air Wet-Bulb Temperature"]

    @minimum_inlet_air_wetbulb_temperature.setter
    def minimum_inlet_air_wetbulb_temperature(self, value=None):
        """  Corresponds to IDD Field `Minimum Inlet Air Wet-Bulb Temperature`
        Minimum valid inlet air wet-bulb temperature for this approach
        temperature correlation.

        Args:
            value (float): value for IDD Field `Minimum Inlet Air Wet-Bulb Temperature`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `minimum_inlet_air_wetbulb_temperature`'.format(value))
        self._data["Minimum Inlet Air Wet-Bulb Temperature"] = value

    @property
    def maximum_inlet_air_wetbulb_temperature(self):
        """Get maximum_inlet_air_wetbulb_temperature

        Returns:
            float: the value of `maximum_inlet_air_wetbulb_temperature` or None if not set
        """
        return self._data["Maximum Inlet Air Wet-Bulb Temperature"]

    @maximum_inlet_air_wetbulb_temperature.setter
    def maximum_inlet_air_wetbulb_temperature(self, value=None):
        """  Corresponds to IDD Field `Maximum Inlet Air Wet-Bulb Temperature`
        Maximum valid inlet air wet-bulb temperature for this approach
        temperature correlation.

        Args:
            value (float): value for IDD Field `Maximum Inlet Air Wet-Bulb Temperature`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_inlet_air_wetbulb_temperature`'.format(value))
        self._data["Maximum Inlet Air Wet-Bulb Temperature"] = value

    @property
    def minimum_range_temperature(self):
        """Get minimum_range_temperature

        Returns:
            float: the value of `minimum_range_temperature` or None if not set
        """
        return self._data["Minimum Range Temperature"]

    @minimum_range_temperature.setter
    def minimum_range_temperature(self, value=None):
        """  Corresponds to IDD Field `Minimum Range Temperature`
        Minimum valid range temperature for this approach temperature
        correlation.

        Args:
            value (float): value for IDD Field `Minimum Range Temperature`
                Units: deltaC
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `minimum_range_temperature`'.format(value))
        self._data["Minimum Range Temperature"] = value

    @property
    def maximum_range_temperature(self):
        """Get maximum_range_temperature

        Returns:
            float: the value of `maximum_range_temperature` or None if not set
        """
        return self._data["Maximum Range Temperature"]

    @maximum_range_temperature.setter
    def maximum_range_temperature(self, value=None):
        """  Corresponds to IDD Field `Maximum Range Temperature`
        Maximum valid range temperature for this approach temperature
        correlation.

        Args:
            value (float): value for IDD Field `Maximum Range Temperature`
                Units: deltaC
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_range_temperature`'.format(value))
        self._data["Maximum Range Temperature"] = value

    @property
    def minimum_approach_temperature(self):
        """Get minimum_approach_temperature

        Returns:
            float: the value of `minimum_approach_temperature` or None if not set
        """
        return self._data["Minimum Approach Temperature"]

    @minimum_approach_temperature.setter
    def minimum_approach_temperature(self, value=None):
        """  Corresponds to IDD Field `Minimum Approach Temperature`
        Minimum valid approach temperature for this correlation.

        Args:
            value (float): value for IDD Field `Minimum Approach Temperature`
                Units: deltaC
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `minimum_approach_temperature`'.format(value))
        self._data["Minimum Approach Temperature"] = value

    @property
    def maximum_approach_temperature(self):
        """Get maximum_approach_temperature

        Returns:
            float: the value of `maximum_approach_temperature` or None if not set
        """
        return self._data["Maximum Approach Temperature"]

    @maximum_approach_temperature.setter
    def maximum_approach_temperature(self, value=None):
        """  Corresponds to IDD Field `Maximum Approach Temperature`
        Maximum valid approach temperature for this correlation.

        Args:
            value (float): value for IDD Field `Maximum Approach Temperature`
                Units: deltaC
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_approach_temperature`'.format(value))
        self._data["Maximum Approach Temperature"] = value

    @property
    def minimum_water_flow_rate_ratio(self):
        """Get minimum_water_flow_rate_ratio

        Returns:
            float: the value of `minimum_water_flow_rate_ratio` or None if not set
        """
        return self._data["Minimum Water Flow Rate Ratio"]

    @minimum_water_flow_rate_ratio.setter
    def minimum_water_flow_rate_ratio(self, value=None):
        """  Corresponds to IDD Field `Minimum Water Flow Rate Ratio`
        Minimum valid water flow rate ratio for this approach
        temperature correlation.

        Args:
            value (float): value for IDD Field `Minimum Water Flow Rate Ratio`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `minimum_water_flow_rate_ratio`'.format(value))
        self._data["Minimum Water Flow Rate Ratio"] = value

    @property
    def maximum_water_flow_rate_ratio(self):
        """Get maximum_water_flow_rate_ratio

        Returns:
            float: the value of `maximum_water_flow_rate_ratio` or None if not set
        """
        return self._data["Maximum Water Flow Rate Ratio"]

    @maximum_water_flow_rate_ratio.setter
    def maximum_water_flow_rate_ratio(self, value=None):
        """  Corresponds to IDD Field `Maximum Water Flow Rate Ratio`
        Maximum valid water flow rate ratio for this approach
        temperature correlation.

        Args:
            value (float): value for IDD Field `Maximum Water Flow Rate Ratio`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_water_flow_rate_ratio`'.format(value))
        self._data["Maximum Water Flow Rate Ratio"] = value

    @property
    def maximum_liquid_to_gas_ratio(self):
        """Get maximum_liquid_to_gas_ratio

        Returns:
            float: the value of `maximum_liquid_to_gas_ratio` or None if not set
        """
        return self._data["Maximum Liquid to Gas Ratio"]

    @maximum_liquid_to_gas_ratio.setter
    def maximum_liquid_to_gas_ratio(self, value=None):
        """  Corresponds to IDD Field `Maximum Liquid to Gas Ratio`
        Maximum liquid (water) to gas (air) ratio for this approach
        temperature correlation.

        Args:
            value (float): value for IDD Field `Maximum Liquid to Gas Ratio`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_liquid_to_gas_ratio`'.format(value))
        self._data["Maximum Liquid to Gas Ratio"] = value

    @property
    def coefficient_1(self):
        """Get coefficient_1

        Returns:
            float: the value of `coefficient_1` or None if not set
        """
        return self._data["Coefficient 1"]

    @coefficient_1.setter
    def coefficient_1(self, value=None):
        """  Corresponds to IDD Field `Coefficient 1`

        Args:
            value (float): value for IDD Field `Coefficient 1`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient_1`'.format(value))
        self._data["Coefficient 1"] = value

    @property
    def coefficient_2(self):
        """Get coefficient_2

        Returns:
            float: the value of `coefficient_2` or None if not set
        """
        return self._data["Coefficient 2"]

    @coefficient_2.setter
    def coefficient_2(self, value=None):
        """  Corresponds to IDD Field `Coefficient 2`

        Args:
            value (float): value for IDD Field `Coefficient 2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient_2`'.format(value))
        self._data["Coefficient 2"] = value

    @property
    def coefficient_3(self):
        """Get coefficient_3

        Returns:
            float: the value of `coefficient_3` or None if not set
        """
        return self._data["Coefficient 3"]

    @coefficient_3.setter
    def coefficient_3(self, value=None):
        """  Corresponds to IDD Field `Coefficient 3`

        Args:
            value (float): value for IDD Field `Coefficient 3`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient_3`'.format(value))
        self._data["Coefficient 3"] = value

    @property
    def coefficient_4(self):
        """Get coefficient_4

        Returns:
            float: the value of `coefficient_4` or None if not set
        """
        return self._data["Coefficient 4"]

    @coefficient_4.setter
    def coefficient_4(self, value=None):
        """  Corresponds to IDD Field `Coefficient 4`

        Args:
            value (float): value for IDD Field `Coefficient 4`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient_4`'.format(value))
        self._data["Coefficient 4"] = value

    @property
    def coefficient_5(self):
        """Get coefficient_5

        Returns:
            float: the value of `coefficient_5` or None if not set
        """
        return self._data["Coefficient 5"]

    @coefficient_5.setter
    def coefficient_5(self, value=None):
        """  Corresponds to IDD Field `Coefficient 5`

        Args:
            value (float): value for IDD Field `Coefficient 5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient_5`'.format(value))
        self._data["Coefficient 5"] = value

    @property
    def coefficient_6(self):
        """Get coefficient_6

        Returns:
            float: the value of `coefficient_6` or None if not set
        """
        return self._data["Coefficient 6"]

    @coefficient_6.setter
    def coefficient_6(self, value=None):
        """  Corresponds to IDD Field `Coefficient 6`

        Args:
            value (float): value for IDD Field `Coefficient 6`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient_6`'.format(value))
        self._data["Coefficient 6"] = value

    @property
    def coefficient_7(self):
        """Get coefficient_7

        Returns:
            float: the value of `coefficient_7` or None if not set
        """
        return self._data["Coefficient 7"]

    @coefficient_7.setter
    def coefficient_7(self, value=None):
        """  Corresponds to IDD Field `Coefficient 7`

        Args:
            value (float): value for IDD Field `Coefficient 7`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient_7`'.format(value))
        self._data["Coefficient 7"] = value

    @property
    def coefficient_8(self):
        """Get coefficient_8

        Returns:
            float: the value of `coefficient_8` or None if not set
        """
        return self._data["Coefficient 8"]

    @coefficient_8.setter
    def coefficient_8(self, value=None):
        """  Corresponds to IDD Field `Coefficient 8`

        Args:
            value (float): value for IDD Field `Coefficient 8`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient_8`'.format(value))
        self._data["Coefficient 8"] = value

    @property
    def coefficient_9(self):
        """Get coefficient_9

        Returns:
            float: the value of `coefficient_9` or None if not set
        """
        return self._data["Coefficient 9"]

    @coefficient_9.setter
    def coefficient_9(self, value=None):
        """  Corresponds to IDD Field `Coefficient 9`

        Args:
            value (float): value for IDD Field `Coefficient 9`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient_9`'.format(value))
        self._data["Coefficient 9"] = value

    @property
    def coefficient_10(self):
        """Get coefficient_10

        Returns:
            float: the value of `coefficient_10` or None if not set
        """
        return self._data["Coefficient 10"]

    @coefficient_10.setter
    def coefficient_10(self, value=None):
        """  Corresponds to IDD Field `Coefficient 10`

        Args:
            value (float): value for IDD Field `Coefficient 10`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient_10`'.format(value))
        self._data["Coefficient 10"] = value

    @property
    def coefficient_11(self):
        """Get coefficient_11

        Returns:
            float: the value of `coefficient_11` or None if not set
        """
        return self._data["Coefficient 11"]

    @coefficient_11.setter
    def coefficient_11(self, value=None):
        """  Corresponds to IDD Field `Coefficient 11`

        Args:
            value (float): value for IDD Field `Coefficient 11`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient_11`'.format(value))
        self._data["Coefficient 11"] = value

    @property
    def coefficient_12(self):
        """Get coefficient_12

        Returns:
            float: the value of `coefficient_12` or None if not set
        """
        return self._data["Coefficient 12"]

    @coefficient_12.setter
    def coefficient_12(self, value=None):
        """  Corresponds to IDD Field `Coefficient 12`

        Args:
            value (float): value for IDD Field `Coefficient 12`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient_12`'.format(value))
        self._data["Coefficient 12"] = value

    @property
    def coefficient_13(self):
        """Get coefficient_13

        Returns:
            float: the value of `coefficient_13` or None if not set
        """
        return self._data["Coefficient 13"]

    @coefficient_13.setter
    def coefficient_13(self, value=None):
        """  Corresponds to IDD Field `Coefficient 13`

        Args:
            value (float): value for IDD Field `Coefficient 13`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient_13`'.format(value))
        self._data["Coefficient 13"] = value

    @property
    def coefficient_14(self):
        """Get coefficient_14

        Returns:
            float: the value of `coefficient_14` or None if not set
        """
        return self._data["Coefficient 14"]

    @coefficient_14.setter
    def coefficient_14(self, value=None):
        """  Corresponds to IDD Field `Coefficient 14`

        Args:
            value (float): value for IDD Field `Coefficient 14`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient_14`'.format(value))
        self._data["Coefficient 14"] = value

    @property
    def coefficient_15(self):
        """Get coefficient_15

        Returns:
            float: the value of `coefficient_15` or None if not set
        """
        return self._data["Coefficient 15"]

    @coefficient_15.setter
    def coefficient_15(self, value=None):
        """  Corresponds to IDD Field `Coefficient 15`

        Args:
            value (float): value for IDD Field `Coefficient 15`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient_15`'.format(value))
        self._data["Coefficient 15"] = value

    @property
    def coefficient_16(self):
        """Get coefficient_16

        Returns:
            float: the value of `coefficient_16` or None if not set
        """
        return self._data["Coefficient 16"]

    @coefficient_16.setter
    def coefficient_16(self, value=None):
        """  Corresponds to IDD Field `Coefficient 16`

        Args:
            value (float): value for IDD Field `Coefficient 16`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient_16`'.format(value))
        self._data["Coefficient 16"] = value

    @property
    def coefficient_17(self):
        """Get coefficient_17

        Returns:
            float: the value of `coefficient_17` or None if not set
        """
        return self._data["Coefficient 17"]

    @coefficient_17.setter
    def coefficient_17(self, value=None):
        """  Corresponds to IDD Field `Coefficient 17`

        Args:
            value (float): value for IDD Field `Coefficient 17`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient_17`'.format(value))
        self._data["Coefficient 17"] = value

    @property
    def coefficient_18(self):
        """Get coefficient_18

        Returns:
            float: the value of `coefficient_18` or None if not set
        """
        return self._data["Coefficient 18"]

    @coefficient_18.setter
    def coefficient_18(self, value=None):
        """  Corresponds to IDD Field `Coefficient 18`

        Args:
            value (float): value for IDD Field `Coefficient 18`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient_18`'.format(value))
        self._data["Coefficient 18"] = value

    @property
    def coefficient_19(self):
        """Get coefficient_19

        Returns:
            float: the value of `coefficient_19` or None if not set
        """
        return self._data["Coefficient 19"]

    @coefficient_19.setter
    def coefficient_19(self, value=None):
        """  Corresponds to IDD Field `Coefficient 19`

        Args:
            value (float): value for IDD Field `Coefficient 19`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient_19`'.format(value))
        self._data["Coefficient 19"] = value

    @property
    def coefficient_20(self):
        """Get coefficient_20

        Returns:
            float: the value of `coefficient_20` or None if not set
        """
        return self._data["Coefficient 20"]

    @coefficient_20.setter
    def coefficient_20(self, value=None):
        """  Corresponds to IDD Field `Coefficient 20`

        Args:
            value (float): value for IDD Field `Coefficient 20`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient_20`'.format(value))
        self._data["Coefficient 20"] = value

    @property
    def coefficient_21(self):
        """Get coefficient_21

        Returns:
            float: the value of `coefficient_21` or None if not set
        """
        return self._data["Coefficient 21"]

    @coefficient_21.setter
    def coefficient_21(self, value=None):
        """  Corresponds to IDD Field `Coefficient 21`

        Args:
            value (float): value for IDD Field `Coefficient 21`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient_21`'.format(value))
        self._data["Coefficient 21"] = value

    @property
    def coefficient_22(self):
        """Get coefficient_22

        Returns:
            float: the value of `coefficient_22` or None if not set
        """
        return self._data["Coefficient 22"]

    @coefficient_22.setter
    def coefficient_22(self, value=None):
        """  Corresponds to IDD Field `Coefficient 22`

        Args:
            value (float): value for IDD Field `Coefficient 22`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient_22`'.format(value))
        self._data["Coefficient 22"] = value

    @property
    def coefficient_23(self):
        """Get coefficient_23

        Returns:
            float: the value of `coefficient_23` or None if not set
        """
        return self._data["Coefficient 23"]

    @coefficient_23.setter
    def coefficient_23(self, value=None):
        """  Corresponds to IDD Field `Coefficient 23`

        Args:
            value (float): value for IDD Field `Coefficient 23`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient_23`'.format(value))
        self._data["Coefficient 23"] = value

    @property
    def coefficient_24(self):
        """Get coefficient_24

        Returns:
            float: the value of `coefficient_24` or None if not set
        """
        return self._data["Coefficient 24"]

    @coefficient_24.setter
    def coefficient_24(self, value=None):
        """  Corresponds to IDD Field `Coefficient 24`

        Args:
            value (float): value for IDD Field `Coefficient 24`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient_24`'.format(value))
        self._data["Coefficient 24"] = value

    @property
    def coefficient_25(self):
        """Get coefficient_25

        Returns:
            float: the value of `coefficient_25` or None if not set
        """
        return self._data["Coefficient 25"]

    @coefficient_25.setter
    def coefficient_25(self, value=None):
        """  Corresponds to IDD Field `Coefficient 25`

        Args:
            value (float): value for IDD Field `Coefficient 25`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient_25`'.format(value))
        self._data["Coefficient 25"] = value

    @property
    def coefficient_26(self):
        """Get coefficient_26

        Returns:
            float: the value of `coefficient_26` or None if not set
        """
        return self._data["Coefficient 26"]

    @coefficient_26.setter
    def coefficient_26(self, value=None):
        """  Corresponds to IDD Field `Coefficient 26`

        Args:
            value (float): value for IDD Field `Coefficient 26`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient_26`'.format(value))
        self._data["Coefficient 26"] = value

    @property
    def coefficient_27(self):
        """Get coefficient_27

        Returns:
            float: the value of `coefficient_27` or None if not set
        """
        return self._data["Coefficient 27"]

    @coefficient_27.setter
    def coefficient_27(self, value=None):
        """  Corresponds to IDD Field `Coefficient 27`

        Args:
            value (float): value for IDD Field `Coefficient 27`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient_27`'.format(value))
        self._data["Coefficient 27"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
        return good

    @classmethod
    def _to_str(cls, value):
        """ Represents values either as string or None values as empty string

        Args:
            value: a value
        """
        if value is None:
            return ''
        else:
            return str(value)

    def export(self):
        """ Export values of data object as list of strings"""
        out = []
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class EvaporativeFluidCoolerSingleSpeed(object):
    """ Corresponds to IDD object `EvaporativeFluidCooler:SingleSpeed`
        This model is based on Merkel's theory, which is also the basis
        for the cooling tower model in EnergyPlus. The Evaporative fluid cooler
        is modeled as a counter flow heat exchanger.
    
    """
    internal_name = "EvaporativeFluidCooler:SingleSpeed"
    field_count = 25
    required_fields = ["Name", "Water Inlet Node Name", "Water Outlet Node Name", "Design Air Flow Rate", "Design Air Flow Rate Fan Power", "Design Spray Water Flow Rate", "Heat Rejection Capacity and Nominal Capacity Sizing Ratio"]

    def __init__(self):
        """ Init data dictionary object for IDD  `EvaporativeFluidCooler:SingleSpeed`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Water Inlet Node Name"] = None
        self._data["Water Outlet Node Name"] = None
        self._data["Design Air Flow Rate"] = None
        self._data["Design Air Flow Rate Fan Power"] = None
        self._data["Design Spray Water Flow Rate"] = None
        self._data["Performance Input Method"] = None
        self._data["Outdoor Air Inlet Node Name"] = None
        self._data["Heat Rejection Capacity and Nominal Capacity Sizing Ratio"] = None
        self._data["Standard Design Capacity"] = None
        self._data["Design Air Flow Rate U-factor Times Area Value"] = None
        self._data["Design Water Flow Rate"] = None
        self._data["User Specified Design Capacity"] = None
        self._data["Design Entering Water Temperature"] = None
        self._data["Design Entering Air Temperature"] = None
        self._data["Design Entering Air Wet-bulb Temperature"] = None
        self._data["Capacity Control"] = None
        self._data["Sizing Factor"] = None
        self._data["Evaporation Loss Mode"] = None
        self._data["Evaporation Loss Factor"] = None
        self._data["Drift Loss Percent"] = None
        self._data["Blowdown Calculation Mode"] = None
        self._data["Blowdown Concentration Ratio"] = None
        self._data["Blowdown Makeup Water Usage Schedule Name"] = None
        self._data["Supply Water Storage Tank Name"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.water_inlet_node_name = None
        else:
            self.water_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.water_outlet_node_name = None
        else:
            self.water_outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_air_flow_rate = None
        else:
            self.design_air_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_air_flow_rate_fan_power = None
        else:
            self.design_air_flow_rate_fan_power = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_spray_water_flow_rate = None
        else:
            self.design_spray_water_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.performance_input_method = None
        else:
            self.performance_input_method = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outdoor_air_inlet_node_name = None
        else:
            self.outdoor_air_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heat_rejection_capacity_and_nominal_capacity_sizing_ratio = None
        else:
            self.heat_rejection_capacity_and_nominal_capacity_sizing_ratio = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.standard_design_capacity = None
        else:
            self.standard_design_capacity = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_air_flow_rate_ufactor_times_area_value = None
        else:
            self.design_air_flow_rate_ufactor_times_area_value = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_water_flow_rate = None
        else:
            self.design_water_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.user_specified_design_capacity = None
        else:
            self.user_specified_design_capacity = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_entering_water_temperature = None
        else:
            self.design_entering_water_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_entering_air_temperature = None
        else:
            self.design_entering_air_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_entering_air_wetbulb_temperature = None
        else:
            self.design_entering_air_wetbulb_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.capacity_control = None
        else:
            self.capacity_control = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.sizing_factor = None
        else:
            self.sizing_factor = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.evaporation_loss_mode = None
        else:
            self.evaporation_loss_mode = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.evaporation_loss_factor = None
        else:
            self.evaporation_loss_factor = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.drift_loss_percent = None
        else:
            self.drift_loss_percent = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.blowdown_calculation_mode = None
        else:
            self.blowdown_calculation_mode = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.blowdown_concentration_ratio = None
        else:
            self.blowdown_concentration_ratio = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.blowdown_makeup_water_usage_schedule_name = None
        else:
            self.blowdown_makeup_water_usage_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.supply_water_storage_tank_name = None
        else:
            self.supply_water_storage_tank_name = vals[i]
        i += 1
        if i >= len(vals):
            return

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `Name`
        Fluid Cooler Name

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')
        self._data["Name"] = value

    @property
    def water_inlet_node_name(self):
        """Get water_inlet_node_name

        Returns:
            str: the value of `water_inlet_node_name` or None if not set
        """
        return self._data["Water Inlet Node Name"]

    @water_inlet_node_name.setter
    def water_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Water Inlet Node Name`
        Name of Fluid Cooler water inlet node

        Args:
            value (str): value for IDD Field `Water Inlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `water_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `water_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `water_inlet_node_name`')
        self._data["Water Inlet Node Name"] = value

    @property
    def water_outlet_node_name(self):
        """Get water_outlet_node_name

        Returns:
            str: the value of `water_outlet_node_name` or None if not set
        """
        return self._data["Water Outlet Node Name"]

    @water_outlet_node_name.setter
    def water_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Water Outlet Node Name`
        Name of Fluid Cooler water outlet node

        Args:
            value (str): value for IDD Field `Water Outlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `water_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `water_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `water_outlet_node_name`')
        self._data["Water Outlet Node Name"] = value

    @property
    def design_air_flow_rate(self):
        """Get design_air_flow_rate

        Returns:
            float: the value of `design_air_flow_rate` or None if not set
        """
        return self._data["Design Air Flow Rate"]

    @design_air_flow_rate.setter
    def design_air_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Design Air Flow Rate`

        Args:
            value (float or "Autosize"): value for IDD Field `Design Air Flow Rate`
                Units: m3/s
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Design Air Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `design_air_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `design_air_flow_rate`')
        self._data["Design Air Flow Rate"] = value

    @property
    def design_air_flow_rate_fan_power(self):
        """Get design_air_flow_rate_fan_power

        Returns:
            float: the value of `design_air_flow_rate_fan_power` or None if not set
        """
        return self._data["Design Air Flow Rate Fan Power"]

    @design_air_flow_rate_fan_power.setter
    def design_air_flow_rate_fan_power(self, value=None):
        """  Corresponds to IDD Field `Design Air Flow Rate Fan Power`
        This is the fan motor electric input power

        Args:
            value (float or "Autosize"): value for IDD Field `Design Air Flow Rate Fan Power`
                Units: W
                IP-Units: W
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Design Air Flow Rate Fan Power"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `design_air_flow_rate_fan_power`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `design_air_flow_rate_fan_power`')
        self._data["Design Air Flow Rate Fan Power"] = value

    @property
    def design_spray_water_flow_rate(self):
        """Get design_spray_water_flow_rate

        Returns:
            float: the value of `design_spray_water_flow_rate` or None if not set
        """
        return self._data["Design Spray Water Flow Rate"]

    @design_spray_water_flow_rate.setter
    def design_spray_water_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Design Spray Water Flow Rate`

        Args:
            value (float): value for IDD Field `Design Spray Water Flow Rate`
                Units: m3/s
                IP-Units: gal/min
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `design_spray_water_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `design_spray_water_flow_rate`')
        self._data["Design Spray Water Flow Rate"] = value

    @property
    def performance_input_method(self):
        """Get performance_input_method

        Returns:
            str: the value of `performance_input_method` or None if not set
        """
        return self._data["Performance Input Method"]

    @performance_input_method.setter
    def performance_input_method(self, value=None):
        """  Corresponds to IDD Field `Performance Input Method`
        User can define fluid cooler thermal performance by specifying the fluid cooler UA
        and the Design Water Flow Rate, or by specifying the fluid cooler Standard Design
        Capacity or by specifying Design Capacity for Non standard conditions.

        Args:
            value (str): value for IDD Field `Performance Input Method`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `performance_input_method`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `performance_input_method`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `performance_input_method`')
        self._data["Performance Input Method"] = value

    @property
    def outdoor_air_inlet_node_name(self):
        """Get outdoor_air_inlet_node_name

        Returns:
            str: the value of `outdoor_air_inlet_node_name` or None if not set
        """
        return self._data["Outdoor Air Inlet Node Name"]

    @outdoor_air_inlet_node_name.setter
    def outdoor_air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Outdoor Air Inlet Node Name`
        Enter the name of an outdoor air node

        Args:
            value (str): value for IDD Field `Outdoor Air Inlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `outdoor_air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outdoor_air_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `outdoor_air_inlet_node_name`')
        self._data["Outdoor Air Inlet Node Name"] = value

    @property
    def heat_rejection_capacity_and_nominal_capacity_sizing_ratio(self):
        """Get heat_rejection_capacity_and_nominal_capacity_sizing_ratio

        Returns:
            float: the value of `heat_rejection_capacity_and_nominal_capacity_sizing_ratio` or None if not set
        """
        return self._data["Heat Rejection Capacity and Nominal Capacity Sizing Ratio"]

    @heat_rejection_capacity_and_nominal_capacity_sizing_ratio.setter
    def heat_rejection_capacity_and_nominal_capacity_sizing_ratio(self, value=1.25):
        """  Corresponds to IDD Field `Heat Rejection Capacity and Nominal Capacity Sizing Ratio`

        Args:
            value (float): value for IDD Field `Heat Rejection Capacity and Nominal Capacity Sizing Ratio`
                Default value: 1.25
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `heat_rejection_capacity_and_nominal_capacity_sizing_ratio`'.format(value))
        self._data["Heat Rejection Capacity and Nominal Capacity Sizing Ratio"] = value

    @property
    def standard_design_capacity(self):
        """Get standard_design_capacity

        Returns:
            float: the value of `standard_design_capacity` or None if not set
        """
        return self._data["Standard Design Capacity"]

    @standard_design_capacity.setter
    def standard_design_capacity(self, value=None):
        """  Corresponds to IDD Field `Standard Design Capacity`
        Standard design capacity with entering water at 35C (95F), leaving water at
        29.44C (85F), entering air at 25.56C (78F) wet-bulb temperature and 35C (95F)
        dry-bulb temperature. Design water flow rate assumed to be 5.382E-8 m3/s per watt
        (3 gpm/ton). Standard design capacity times the Heat Rejection Capacity and
        Nominal Capacity Sizing Ratio (e.g. 1.25) gives the actual fluid cooler
        heat rejection at these operating conditions.
        Only used for Performance Input Method = StandardDesignCapacity;
        for other input methods, this field is ignored.
        The standard conditions mentioned above for Standard design capacity are already
        specified in the EnergyPlus. So the input fields such as design entering water
        temp., design entering air wet-bulb and dry-bulb temp. and design water flow rate, if
        provided in the input, will be ignored for the StandardDesignCapacity performance input
        method. Also, the standard conditions are for water as a fluid type so this performance input
        method can only be used with water as a fluid type (as specified in CondenserLoop object).

        Args:
            value (float): value for IDD Field `Standard Design Capacity`
                Units: W
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `standard_design_capacity`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `standard_design_capacity`')
        self._data["Standard Design Capacity"] = value

    @property
    def design_air_flow_rate_ufactor_times_area_value(self):
        """Get design_air_flow_rate_ufactor_times_area_value

        Returns:
            float: the value of `design_air_flow_rate_ufactor_times_area_value` or None if not set
        """
        return self._data["Design Air Flow Rate U-factor Times Area Value"]

    @design_air_flow_rate_ufactor_times_area_value.setter
    def design_air_flow_rate_ufactor_times_area_value(self, value=None):
        """  Corresponds to IDD Field `Design Air Flow Rate U-factor Times Area Value`
        Only used for Performance Input Method = UFactorTimesAreaAndDesignWaterFlowRate;
        for other Performance Input Methods, this field is ignored.

        Args:
            value (float or "Autosize"): value for IDD Field `Design Air Flow Rate U-factor Times Area Value`
                Units: W/K
                value > 0.0
                value <= 2100000.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Design Air Flow Rate U-factor Times Area Value"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `design_air_flow_rate_ufactor_times_area_value`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `design_air_flow_rate_ufactor_times_area_value`')
            if value > 2100000.0:
                raise ValueError('value need to be smaller 2100000.0 '
                                 'for field `design_air_flow_rate_ufactor_times_area_value`')
        self._data["Design Air Flow Rate U-factor Times Area Value"] = value

    @property
    def design_water_flow_rate(self):
        """Get design_water_flow_rate

        Returns:
            float: the value of `design_water_flow_rate` or None if not set
        """
        return self._data["Design Water Flow Rate"]

    @design_water_flow_rate.setter
    def design_water_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Design Water Flow Rate`
        Input value is ignored if fluid cooler Performance Input Method= StandardDesignCapacity.

        Args:
            value (float or "Autosize"): value for IDD Field `Design Water Flow Rate`
                Units: m3/s
                IP-Units: gal/min
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Design Water Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `design_water_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `design_water_flow_rate`')
        self._data["Design Water Flow Rate"] = value

    @property
    def user_specified_design_capacity(self):
        """Get user_specified_design_capacity

        Returns:
            float: the value of `user_specified_design_capacity` or None if not set
        """
        return self._data["User Specified Design Capacity"]

    @user_specified_design_capacity.setter
    def user_specified_design_capacity(self, value=None):
        """  Corresponds to IDD Field `User Specified Design Capacity`
        Only used for Performance Input Method = UserSpecifiedDesignCapacity;
        for other Performance Input Methods, this field is ignored.

        Args:
            value (float): value for IDD Field `User Specified Design Capacity`
                Units: W
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `user_specified_design_capacity`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `user_specified_design_capacity`')
        self._data["User Specified Design Capacity"] = value

    @property
    def design_entering_water_temperature(self):
        """Get design_entering_water_temperature

        Returns:
            float: the value of `design_entering_water_temperature` or None if not set
        """
        return self._data["Design Entering Water Temperature"]

    @design_entering_water_temperature.setter
    def design_entering_water_temperature(self, value=None):
        """  Corresponds to IDD Field `Design Entering Water Temperature`
        Only used for Performance Input Method = UserSpecifiedDesignCapacity;
        for other Performance Input Methods, this field is ignored.
        Design Entering Water Temperature must be greater than Design Entering Air Temperature.

        Args:
            value (float): value for IDD Field `Design Entering Water Temperature`
                Units: C
                IP-Units: F
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `design_entering_water_temperature`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `design_entering_water_temperature`')
        self._data["Design Entering Water Temperature"] = value

    @property
    def design_entering_air_temperature(self):
        """Get design_entering_air_temperature

        Returns:
            float: the value of `design_entering_air_temperature` or None if not set
        """
        return self._data["Design Entering Air Temperature"]

    @design_entering_air_temperature.setter
    def design_entering_air_temperature(self, value=None):
        """  Corresponds to IDD Field `Design Entering Air Temperature`
        Only used for Performance Input Method = UserSpecifiedDesignCapacity;
        for other Performance Input Methods, this field is ignored.
        Design Entering Air Temperature must be greater than Design Entering Air Wet-bulb
        Temperature.

        Args:
            value (float): value for IDD Field `Design Entering Air Temperature`
                Units: C
                IP-Units: F
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `design_entering_air_temperature`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `design_entering_air_temperature`')
        self._data["Design Entering Air Temperature"] = value

    @property
    def design_entering_air_wetbulb_temperature(self):
        """Get design_entering_air_wetbulb_temperature

        Returns:
            float: the value of `design_entering_air_wetbulb_temperature` or None if not set
        """
        return self._data["Design Entering Air Wet-bulb Temperature"]

    @design_entering_air_wetbulb_temperature.setter
    def design_entering_air_wetbulb_temperature(self, value=None):
        """  Corresponds to IDD Field `Design Entering Air Wet-bulb Temperature`
        Only used for Performance Input Method = UserSpecifiedDesignCapacity;
        for other Performance Input Methods, this field is ignored.
        Design Entering Air Wet-bulb Temperature must be less than Design Entering Air
        Temperature.

        Args:
            value (float): value for IDD Field `Design Entering Air Wet-bulb Temperature`
                Units: C
                IP-Units: F
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `design_entering_air_wetbulb_temperature`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `design_entering_air_wetbulb_temperature`')
        self._data["Design Entering Air Wet-bulb Temperature"] = value

    @property
    def capacity_control(self):
        """Get capacity_control

        Returns:
            str: the value of `capacity_control` or None if not set
        """
        return self._data["Capacity Control"]

    @capacity_control.setter
    def capacity_control(self, value="FanCycling"):
        """  Corresponds to IDD Field `Capacity Control`

        Args:
            value (str): value for IDD Field `Capacity Control`
                Accepted values are:
                      - FanCycling
                      - FluidBypass
                Default value: FanCycling
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `capacity_control`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `capacity_control`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `capacity_control`')
            vals = {}
            vals["fancycling"] = "FanCycling"
            vals["fluidbypass"] = "FluidBypass"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `capacity_control`'.format(value))
            value = vals[value_lower]
        self._data["Capacity Control"] = value

    @property
    def sizing_factor(self):
        """Get sizing_factor

        Returns:
            float: the value of `sizing_factor` or None if not set
        """
        return self._data["Sizing Factor"]

    @sizing_factor.setter
    def sizing_factor(self, value=1.0):
        """  Corresponds to IDD Field `Sizing Factor`
        Multiplies the autosized capacity and flow rates

        Args:
            value (float): value for IDD Field `Sizing Factor`
                Default value: 1.0
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `sizing_factor`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `sizing_factor`')
        self._data["Sizing Factor"] = value

    @property
    def evaporation_loss_mode(self):
        """Get evaporation_loss_mode

        Returns:
            str: the value of `evaporation_loss_mode` or None if not set
        """
        return self._data["Evaporation Loss Mode"]

    @evaporation_loss_mode.setter
    def evaporation_loss_mode(self, value="SaturatedExit"):
        """  Corresponds to IDD Field `Evaporation Loss Mode`

        Args:
            value (str): value for IDD Field `Evaporation Loss Mode`
                Accepted values are:
                      - LossFactor
                      - SaturatedExit
                Default value: SaturatedExit
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `evaporation_loss_mode`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `evaporation_loss_mode`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `evaporation_loss_mode`')
            vals = {}
            vals["lossfactor"] = "LossFactor"
            vals["saturatedexit"] = "SaturatedExit"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `evaporation_loss_mode`'.format(value))
            value = vals[value_lower]
        self._data["Evaporation Loss Mode"] = value

    @property
    def evaporation_loss_factor(self):
        """Get evaporation_loss_factor

        Returns:
            float: the value of `evaporation_loss_factor` or None if not set
        """
        return self._data["Evaporation Loss Factor"]

    @evaporation_loss_factor.setter
    def evaporation_loss_factor(self, value=None):
        """  Corresponds to IDD Field `Evaporation Loss Factor`
        Rate of water evaporation from the Fluid Cooler and lost to the outdoor air [%/K]
        Empirical correlation is used to calculate default loss factor if it not explicitly provided.

        Args:
            value (float): value for IDD Field `Evaporation Loss Factor`
                Units: percent/K
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `evaporation_loss_factor`'.format(value))
        self._data["Evaporation Loss Factor"] = value

    @property
    def drift_loss_percent(self):
        """Get drift_loss_percent

        Returns:
            float: the value of `drift_loss_percent` or None if not set
        """
        return self._data["Drift Loss Percent"]

    @drift_loss_percent.setter
    def drift_loss_percent(self, value=0.008):
        """  Corresponds to IDD Field `Drift Loss Percent`
        Rate of drift loss as a percentage of circulating spray water flow rate
        Default value for this field in under investigation. For now Cooling towers drift loss
        percent default value is taken here.

        Args:
            value (float): value for IDD Field `Drift Loss Percent`
                Units: percent
                Default value: 0.008
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `drift_loss_percent`'.format(value))
        self._data["Drift Loss Percent"] = value

    @property
    def blowdown_calculation_mode(self):
        """Get blowdown_calculation_mode

        Returns:
            str: the value of `blowdown_calculation_mode` or None if not set
        """
        return self._data["Blowdown Calculation Mode"]

    @blowdown_calculation_mode.setter
    def blowdown_calculation_mode(self, value="ConcentrationRatio"):
        """  Corresponds to IDD Field `Blowdown Calculation Mode`

        Args:
            value (str): value for IDD Field `Blowdown Calculation Mode`
                Accepted values are:
                      - ConcentrationRatio
                      - ScheduledRate
                Default value: ConcentrationRatio
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `blowdown_calculation_mode`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `blowdown_calculation_mode`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `blowdown_calculation_mode`')
            vals = {}
            vals["concentrationratio"] = "ConcentrationRatio"
            vals["scheduledrate"] = "ScheduledRate"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `blowdown_calculation_mode`'.format(value))
            value = vals[value_lower]
        self._data["Blowdown Calculation Mode"] = value

    @property
    def blowdown_concentration_ratio(self):
        """Get blowdown_concentration_ratio

        Returns:
            float: the value of `blowdown_concentration_ratio` or None if not set
        """
        return self._data["Blowdown Concentration Ratio"]

    @blowdown_concentration_ratio.setter
    def blowdown_concentration_ratio(self, value=3.0):
        """  Corresponds to IDD Field `Blowdown Concentration Ratio`
        Characterizes the rate of blowdown in the Evaporative Fluid Cooler.
        Blowdown is water intentionally drained from the basin in order to offset the build
        up of solids in the water that would otherwise occur because of evaporation.
        Ratio of solids in the blowdown water to solids in the make up water.
        Default value for this field in under investigation. For now Cooling towers
        Blowdown Concentration Ratio percent default value is taken here.

        Args:
            value (float): value for IDD Field `Blowdown Concentration Ratio`
                Default value: 3.0
                value >= 2.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `blowdown_concentration_ratio`'.format(value))
            if value < 2.0:
                raise ValueError('value need to be greater or equal 2.0 '
                                 'for field `blowdown_concentration_ratio`')
        self._data["Blowdown Concentration Ratio"] = value

    @property
    def blowdown_makeup_water_usage_schedule_name(self):
        """Get blowdown_makeup_water_usage_schedule_name

        Returns:
            str: the value of `blowdown_makeup_water_usage_schedule_name` or None if not set
        """
        return self._data["Blowdown Makeup Water Usage Schedule Name"]

    @blowdown_makeup_water_usage_schedule_name.setter
    def blowdown_makeup_water_usage_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Blowdown Makeup Water Usage Schedule Name`
        Makeup water usage due to blowdown results from occasionally draining a small
        amount of water in the Fluid Cooler basin to purge scale or other contaminants to
        reduce their concentration in order to maintain an acceptable level of water quality.
        Schedule values should reflect water usage in m3/s.

        Args:
            value (str): value for IDD Field `Blowdown Makeup Water Usage Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `blowdown_makeup_water_usage_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `blowdown_makeup_water_usage_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `blowdown_makeup_water_usage_schedule_name`')
        self._data["Blowdown Makeup Water Usage Schedule Name"] = value

    @property
    def supply_water_storage_tank_name(self):
        """Get supply_water_storage_tank_name

        Returns:
            str: the value of `supply_water_storage_tank_name` or None if not set
        """
        return self._data["Supply Water Storage Tank Name"]

    @supply_water_storage_tank_name.setter
    def supply_water_storage_tank_name(self, value=None):
        """  Corresponds to IDD Field `Supply Water Storage Tank Name`

        Args:
            value (str): value for IDD Field `Supply Water Storage Tank Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_water_storage_tank_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_water_storage_tank_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `supply_water_storage_tank_name`')
        self._data["Supply Water Storage Tank Name"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
        return good

    @classmethod
    def _to_str(cls, value):
        """ Represents values either as string or None values as empty string

        Args:
            value: a value
        """
        if value is None:
            return ''
        else:
            return str(value)

    def export(self):
        """ Export values of data object as list of strings"""
        out = []
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class EvaporativeFluidCoolerTwoSpeed(object):
    """ Corresponds to IDD object `EvaporativeFluidCooler:TwoSpeed`
        This model is based on Merkel's theory, which is also the basis
        for the cooling tower model in EnergyPlus. The Evaporative fluid cooler
        is modeled as a counter flow heat exchanger.
    
    """
    internal_name = "EvaporativeFluidCooler:TwoSpeed"
    field_count = 34
    required_fields = ["Name", "Water Inlet Node Name", "Water Outlet Node Name", "High Fan Speed Air Flow Rate", "High Fan Speed Fan Power", "Low Fan Speed Air Flow Rate", "Low Fan Speed Air Flow Rate Sizing Factor", "Low Fan Speed Fan Power", "Low Fan Speed Fan Power Sizing Factor", "Design Spray Water Flow Rate", "Performance Input Method", "Heat Rejection Capacity and Nominal Capacity Sizing Ratio", "Low Speed Standard Capacity Sizing Factor", "Low Fan Speed U-Factor Times Area Sizing Factor", "Low Speed User Specified Design Capacity Sizing Factor"]

    def __init__(self):
        """ Init data dictionary object for IDD  `EvaporativeFluidCooler:TwoSpeed`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Water Inlet Node Name"] = None
        self._data["Water Outlet Node Name"] = None
        self._data["High Fan Speed Air Flow Rate"] = None
        self._data["High Fan Speed Fan Power"] = None
        self._data["Low Fan Speed Air Flow Rate"] = None
        self._data["Low Fan Speed Air Flow Rate Sizing Factor"] = None
        self._data["Low Fan Speed Fan Power"] = None
        self._data["Low Fan Speed Fan Power Sizing Factor"] = None
        self._data["Design Spray Water Flow Rate"] = None
        self._data["Performance Input Method"] = None
        self._data["Outdoor Air Inlet Node Name"] = None
        self._data["Heat Rejection Capacity and Nominal Capacity Sizing Ratio"] = None
        self._data["High Speed Standard Design Capacity"] = None
        self._data["Low Speed Standard Design Capacity"] = None
        self._data["Low Speed Standard Capacity Sizing Factor"] = None
        self._data["High Fan Speed U-factor Times Area Value"] = None
        self._data["Low Fan Speed U-factor Times Area Value"] = None
        self._data["Low Fan Speed U-Factor Times Area Sizing Factor"] = None
        self._data["Design Water Flow Rate"] = None
        self._data["High Speed User Specified Design Capacity"] = None
        self._data["Low Speed User Specified Design Capacity"] = None
        self._data["Low Speed User Specified Design Capacity Sizing Factor"] = None
        self._data["Design Entering Water Temperature"] = None
        self._data["Design Entering Air Temperature"] = None
        self._data["Design Entering Air Wet-bulb Temperature"] = None
        self._data["High Speed Sizing Factor"] = None
        self._data["Evaporation Loss Mode"] = None
        self._data["Evaporation Loss Factor"] = None
        self._data["Drift Loss Percent"] = None
        self._data["Blowdown Calculation Mode"] = None
        self._data["Blowdown Concentration Ratio"] = None
        self._data["Blowdown Makeup Water Usage Schedule Name"] = None
        self._data["Supply Water Storage Tank Name"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.water_inlet_node_name = None
        else:
            self.water_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.water_outlet_node_name = None
        else:
            self.water_outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.high_fan_speed_air_flow_rate = None
        else:
            self.high_fan_speed_air_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.high_fan_speed_fan_power = None
        else:
            self.high_fan_speed_fan_power = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.low_fan_speed_air_flow_rate = None
        else:
            self.low_fan_speed_air_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.low_fan_speed_air_flow_rate_sizing_factor = None
        else:
            self.low_fan_speed_air_flow_rate_sizing_factor = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.low_fan_speed_fan_power = None
        else:
            self.low_fan_speed_fan_power = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.low_fan_speed_fan_power_sizing_factor = None
        else:
            self.low_fan_speed_fan_power_sizing_factor = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_spray_water_flow_rate = None
        else:
            self.design_spray_water_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.performance_input_method = None
        else:
            self.performance_input_method = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outdoor_air_inlet_node_name = None
        else:
            self.outdoor_air_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heat_rejection_capacity_and_nominal_capacity_sizing_ratio = None
        else:
            self.heat_rejection_capacity_and_nominal_capacity_sizing_ratio = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.high_speed_standard_design_capacity = None
        else:
            self.high_speed_standard_design_capacity = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.low_speed_standard_design_capacity = None
        else:
            self.low_speed_standard_design_capacity = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.low_speed_standard_capacity_sizing_factor = None
        else:
            self.low_speed_standard_capacity_sizing_factor = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.high_fan_speed_ufactor_times_area_value = None
        else:
            self.high_fan_speed_ufactor_times_area_value = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.low_fan_speed_ufactor_times_area_value = None
        else:
            self.low_fan_speed_ufactor_times_area_value = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.low_fan_speed_ufactor_times_area_sizing_factor = None
        else:
            self.low_fan_speed_ufactor_times_area_sizing_factor = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_water_flow_rate = None
        else:
            self.design_water_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.high_speed_user_specified_design_capacity = None
        else:
            self.high_speed_user_specified_design_capacity = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.low_speed_user_specified_design_capacity = None
        else:
            self.low_speed_user_specified_design_capacity = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.low_speed_user_specified_design_capacity_sizing_factor = None
        else:
            self.low_speed_user_specified_design_capacity_sizing_factor = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_entering_water_temperature = None
        else:
            self.design_entering_water_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_entering_air_temperature = None
        else:
            self.design_entering_air_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_entering_air_wetbulb_temperature = None
        else:
            self.design_entering_air_wetbulb_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.high_speed_sizing_factor = None
        else:
            self.high_speed_sizing_factor = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.evaporation_loss_mode = None
        else:
            self.evaporation_loss_mode = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.evaporation_loss_factor = None
        else:
            self.evaporation_loss_factor = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.drift_loss_percent = None
        else:
            self.drift_loss_percent = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.blowdown_calculation_mode = None
        else:
            self.blowdown_calculation_mode = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.blowdown_concentration_ratio = None
        else:
            self.blowdown_concentration_ratio = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.blowdown_makeup_water_usage_schedule_name = None
        else:
            self.blowdown_makeup_water_usage_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.supply_water_storage_tank_name = None
        else:
            self.supply_water_storage_tank_name = vals[i]
        i += 1
        if i >= len(vals):
            return

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `Name`
        fluid cooler name

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')
        self._data["Name"] = value

    @property
    def water_inlet_node_name(self):
        """Get water_inlet_node_name

        Returns:
            str: the value of `water_inlet_node_name` or None if not set
        """
        return self._data["Water Inlet Node Name"]

    @water_inlet_node_name.setter
    def water_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Water Inlet Node Name`
        Name of fluid cooler water inlet node

        Args:
            value (str): value for IDD Field `Water Inlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `water_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `water_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `water_inlet_node_name`')
        self._data["Water Inlet Node Name"] = value

    @property
    def water_outlet_node_name(self):
        """Get water_outlet_node_name

        Returns:
            str: the value of `water_outlet_node_name` or None if not set
        """
        return self._data["Water Outlet Node Name"]

    @water_outlet_node_name.setter
    def water_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Water Outlet Node Name`
        Name of fluid cooler water outlet node

        Args:
            value (str): value for IDD Field `Water Outlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `water_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `water_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `water_outlet_node_name`')
        self._data["Water Outlet Node Name"] = value

    @property
    def high_fan_speed_air_flow_rate(self):
        """Get high_fan_speed_air_flow_rate

        Returns:
            float: the value of `high_fan_speed_air_flow_rate` or None if not set
        """
        return self._data["High Fan Speed Air Flow Rate"]

    @high_fan_speed_air_flow_rate.setter
    def high_fan_speed_air_flow_rate(self, value=None):
        """  Corresponds to IDD Field `High Fan Speed Air Flow Rate`

        Args:
            value (float or "Autosize"): value for IDD Field `High Fan Speed Air Flow Rate`
                Units: m3/s
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["High Fan Speed Air Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `high_fan_speed_air_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `high_fan_speed_air_flow_rate`')
        self._data["High Fan Speed Air Flow Rate"] = value

    @property
    def high_fan_speed_fan_power(self):
        """Get high_fan_speed_fan_power

        Returns:
            float: the value of `high_fan_speed_fan_power` or None if not set
        """
        return self._data["High Fan Speed Fan Power"]

    @high_fan_speed_fan_power.setter
    def high_fan_speed_fan_power(self, value=None):
        """  Corresponds to IDD Field `High Fan Speed Fan Power`
        This is the fan motor electric input power at high speed

        Args:
            value (float or "Autosize"): value for IDD Field `High Fan Speed Fan Power`
                Units: W
                IP-Units: W
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["High Fan Speed Fan Power"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `high_fan_speed_fan_power`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `high_fan_speed_fan_power`')
        self._data["High Fan Speed Fan Power"] = value

    @property
    def low_fan_speed_air_flow_rate(self):
        """Get low_fan_speed_air_flow_rate

        Returns:
            float: the value of `low_fan_speed_air_flow_rate` or None if not set
        """
        return self._data["Low Fan Speed Air Flow Rate"]

    @low_fan_speed_air_flow_rate.setter
    def low_fan_speed_air_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Low Fan Speed Air Flow Rate`
        Low speed air flow rate must be less than high speed air flow rate

        Args:
            value (float or "Autocalculate"): value for IDD Field `Low Fan Speed Air Flow Rate`
                Units: m3/s
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autocalculate":
                    self._data["Low Fan Speed Air Flow Rate"] = "Autocalculate"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `low_fan_speed_air_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `low_fan_speed_air_flow_rate`')
        self._data["Low Fan Speed Air Flow Rate"] = value

    @property
    def low_fan_speed_air_flow_rate_sizing_factor(self):
        """Get low_fan_speed_air_flow_rate_sizing_factor

        Returns:
            float: the value of `low_fan_speed_air_flow_rate_sizing_factor` or None if not set
        """
        return self._data["Low Fan Speed Air Flow Rate Sizing Factor"]

    @low_fan_speed_air_flow_rate_sizing_factor.setter
    def low_fan_speed_air_flow_rate_sizing_factor(self, value=0.5):
        """  Corresponds to IDD Field `Low Fan Speed Air Flow Rate Sizing Factor`
        This field is only used if the previous field is set to autocalculate

        Args:
            value (float): value for IDD Field `Low Fan Speed Air Flow Rate Sizing Factor`
                Default value: 0.5
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `low_fan_speed_air_flow_rate_sizing_factor`'.format(value))
        self._data["Low Fan Speed Air Flow Rate Sizing Factor"] = value

    @property
    def low_fan_speed_fan_power(self):
        """Get low_fan_speed_fan_power

        Returns:
            float: the value of `low_fan_speed_fan_power` or None if not set
        """
        return self._data["Low Fan Speed Fan Power"]

    @low_fan_speed_fan_power.setter
    def low_fan_speed_fan_power(self, value=None):
        """  Corresponds to IDD Field `Low Fan Speed Fan Power`
        This is the fan motor electric input power at low speed

        Args:
            value (float or "Autocalculate"): value for IDD Field `Low Fan Speed Fan Power`
                Units: W
                IP-Units: W
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autocalculate":
                    self._data["Low Fan Speed Fan Power"] = "Autocalculate"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `low_fan_speed_fan_power`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `low_fan_speed_fan_power`')
        self._data["Low Fan Speed Fan Power"] = value

    @property
    def low_fan_speed_fan_power_sizing_factor(self):
        """Get low_fan_speed_fan_power_sizing_factor

        Returns:
            float: the value of `low_fan_speed_fan_power_sizing_factor` or None if not set
        """
        return self._data["Low Fan Speed Fan Power Sizing Factor"]

    @low_fan_speed_fan_power_sizing_factor.setter
    def low_fan_speed_fan_power_sizing_factor(self, value=0.16):
        """  Corresponds to IDD Field `Low Fan Speed Fan Power Sizing Factor`
        This field is only used if the previous field is set to autocalculate.

        Args:
            value (float): value for IDD Field `Low Fan Speed Fan Power Sizing Factor`
                Default value: 0.16
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `low_fan_speed_fan_power_sizing_factor`'.format(value))
        self._data["Low Fan Speed Fan Power Sizing Factor"] = value

    @property
    def design_spray_water_flow_rate(self):
        """Get design_spray_water_flow_rate

        Returns:
            float: the value of `design_spray_water_flow_rate` or None if not set
        """
        return self._data["Design Spray Water Flow Rate"]

    @design_spray_water_flow_rate.setter
    def design_spray_water_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Design Spray Water Flow Rate`

        Args:
            value (float): value for IDD Field `Design Spray Water Flow Rate`
                Units: m3/s
                IP-Units: gal/min
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `design_spray_water_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `design_spray_water_flow_rate`')
        self._data["Design Spray Water Flow Rate"] = value

    @property
    def performance_input_method(self):
        """Get performance_input_method

        Returns:
            str: the value of `performance_input_method` or None if not set
        """
        return self._data["Performance Input Method"]

    @performance_input_method.setter
    def performance_input_method(self, value=None):
        """  Corresponds to IDD Field `Performance Input Method`
        User can define fluid cooler thermal performance by specifying the fluid cooler UA
        and the Design Water Flow Rate, or by specifying the fluid cooler Standard Design
        Capacity or by specifying Design Capacity for Non standard conditions.

        Args:
            value (str): value for IDD Field `Performance Input Method`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `performance_input_method`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `performance_input_method`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `performance_input_method`')
        self._data["Performance Input Method"] = value

    @property
    def outdoor_air_inlet_node_name(self):
        """Get outdoor_air_inlet_node_name

        Returns:
            str: the value of `outdoor_air_inlet_node_name` or None if not set
        """
        return self._data["Outdoor Air Inlet Node Name"]

    @outdoor_air_inlet_node_name.setter
    def outdoor_air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Outdoor Air Inlet Node Name`
        Enter the name of an outdoor air node

        Args:
            value (str): value for IDD Field `Outdoor Air Inlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `outdoor_air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outdoor_air_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `outdoor_air_inlet_node_name`')
        self._data["Outdoor Air Inlet Node Name"] = value

    @property
    def heat_rejection_capacity_and_nominal_capacity_sizing_ratio(self):
        """Get heat_rejection_capacity_and_nominal_capacity_sizing_ratio

        Returns:
            float: the value of `heat_rejection_capacity_and_nominal_capacity_sizing_ratio` or None if not set
        """
        return self._data["Heat Rejection Capacity and Nominal Capacity Sizing Ratio"]

    @heat_rejection_capacity_and_nominal_capacity_sizing_ratio.setter
    def heat_rejection_capacity_and_nominal_capacity_sizing_ratio(self, value=1.25):
        """  Corresponds to IDD Field `Heat Rejection Capacity and Nominal Capacity Sizing Ratio`

        Args:
            value (float): value for IDD Field `Heat Rejection Capacity and Nominal Capacity Sizing Ratio`
                Default value: 1.25
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `heat_rejection_capacity_and_nominal_capacity_sizing_ratio`'.format(value))
        self._data["Heat Rejection Capacity and Nominal Capacity Sizing Ratio"] = value

    @property
    def high_speed_standard_design_capacity(self):
        """Get high_speed_standard_design_capacity

        Returns:
            float: the value of `high_speed_standard_design_capacity` or None if not set
        """
        return self._data["High Speed Standard Design Capacity"]

    @high_speed_standard_design_capacity.setter
    def high_speed_standard_design_capacity(self, value=None):
        """  Corresponds to IDD Field `High Speed Standard Design Capacity`
        Standard design capacity with entering water at 35C (95F), leaving water at
        29.44C (85F), entering air at 25.56C (78F) wet-bulb temperature and 35C (95F)
        dry-bulb temperature. Design water flow rate assumed to be 5.382E-8 m3/s per watt
        (3 gpm/ton). Standard design capacity times the Heat Rejection Capacity and
        Nominal Capacity Sizing Ratio (e.g. 1.25) gives the actual fluid cooler
        heat rejection at these operating conditions.
        Only used for Performance Input Method = StandardDesignCapacity;
        for other input methods, this field is ignored.
        The standard conditions mentioned above for Standard design capacity are already
        specified in the EnergyPlus. So the input fields such as design entering water
        temp., design entering air wet-bulb and dry-bulb temp. and design water flow rate, if
        provided in the input, will be ignored for the StandardDesignCapacity performance input
        method. Also, the standard conditions are for water as a fluid type so this performance input
        method can only be used with water as a fluid type (as specified in CondenserLoop object).

        Args:
            value (float): value for IDD Field `High Speed Standard Design Capacity`
                Units: W
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `high_speed_standard_design_capacity`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `high_speed_standard_design_capacity`')
        self._data["High Speed Standard Design Capacity"] = value

    @property
    def low_speed_standard_design_capacity(self):
        """Get low_speed_standard_design_capacity

        Returns:
            float: the value of `low_speed_standard_design_capacity` or None if not set
        """
        return self._data["Low Speed Standard Design Capacity"]

    @low_speed_standard_design_capacity.setter
    def low_speed_standard_design_capacity(self, value=None):
        """  Corresponds to IDD Field `Low Speed Standard Design Capacity`
        Standard design capacity with entering water at 35C (95F), leaving water at
        29.44C (85F), entering air at 25.56C (78F) wet-bulb temperature and 35C (95F)
        dry-bulb temperature. Design water flow rate assumed to be 5.382E-8 m3/s per watt
        (3 gpm/ton). Standard design capacity times the Heat Rejection Capacity and
        Nominal Capacity Sizing Ratio (e.g. 1.25) gives the actual fluid cooler
        heat rejection at these operating conditions.
        Only used for Performance Input Method = StandardDesignCapacity;
        for other input methods, this field is ignored.
        The standard conditions mentioned above for Standard design capacity are already
        specified in the EnergyPlus. So the input fields such as design entering water
        temp., design entering air wet-bulb and dry-bulb temp. and design water flow rate, if
        provided in the input, will be ignored for the StandardDesignCapacity performance input
        method. Also, the standard conditions are for water as a fluid type so this performance input
        method can only be used with water as a fluid type (as specified in CondenserLoop object).

        Args:
            value (float or "Autocalculate"): value for IDD Field `Low Speed Standard Design Capacity`
                Units: W
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autocalculate":
                    self._data["Low Speed Standard Design Capacity"] = "Autocalculate"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `low_speed_standard_design_capacity`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `low_speed_standard_design_capacity`')
        self._data["Low Speed Standard Design Capacity"] = value

    @property
    def low_speed_standard_capacity_sizing_factor(self):
        """Get low_speed_standard_capacity_sizing_factor

        Returns:
            float: the value of `low_speed_standard_capacity_sizing_factor` or None if not set
        """
        return self._data["Low Speed Standard Capacity Sizing Factor"]

    @low_speed_standard_capacity_sizing_factor.setter
    def low_speed_standard_capacity_sizing_factor(self, value=0.5):
        """  Corresponds to IDD Field `Low Speed Standard Capacity Sizing Factor`
        This field is only used if the previous field is set to autocalculate

        Args:
            value (float): value for IDD Field `Low Speed Standard Capacity Sizing Factor`
                Default value: 0.5
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `low_speed_standard_capacity_sizing_factor`'.format(value))
        self._data["Low Speed Standard Capacity Sizing Factor"] = value

    @property
    def high_fan_speed_ufactor_times_area_value(self):
        """Get high_fan_speed_ufactor_times_area_value

        Returns:
            float: the value of `high_fan_speed_ufactor_times_area_value` or None if not set
        """
        return self._data["High Fan Speed U-factor Times Area Value"]

    @high_fan_speed_ufactor_times_area_value.setter
    def high_fan_speed_ufactor_times_area_value(self, value=None):
        """  Corresponds to IDD Field `High Fan Speed U-factor Times Area Value`
        Only used for Performance Input Method = UFactorTimesAreaAndDesignWaterFlowRate;
        for other Performance Input Methods, this field is ignored.

        Args:
            value (float or "Autosize"): value for IDD Field `High Fan Speed U-factor Times Area Value`
                Units: W/K
                value > 0.0
                value <= 2100000.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["High Fan Speed U-factor Times Area Value"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `high_fan_speed_ufactor_times_area_value`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `high_fan_speed_ufactor_times_area_value`')
            if value > 2100000.0:
                raise ValueError('value need to be smaller 2100000.0 '
                                 'for field `high_fan_speed_ufactor_times_area_value`')
        self._data["High Fan Speed U-factor Times Area Value"] = value

    @property
    def low_fan_speed_ufactor_times_area_value(self):
        """Get low_fan_speed_ufactor_times_area_value

        Returns:
            float: the value of `low_fan_speed_ufactor_times_area_value` or None if not set
        """
        return self._data["Low Fan Speed U-factor Times Area Value"]

    @low_fan_speed_ufactor_times_area_value.setter
    def low_fan_speed_ufactor_times_area_value(self, value=None):
        """  Corresponds to IDD Field `Low Fan Speed U-factor Times Area Value`
        Only used for Performance Input Method = UFactorTimesAreaAndDesignWaterFlowRate;
        for other input methods, this field is ignored.
        Low speed fluid cooler UA must be less than high speed fluid cooler UA

        Args:
            value (float or "Autocalculate"): value for IDD Field `Low Fan Speed U-factor Times Area Value`
                Units: W/K
                value > 0.0
                value <= 300000.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autocalculate":
                    self._data["Low Fan Speed U-factor Times Area Value"] = "Autocalculate"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `low_fan_speed_ufactor_times_area_value`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `low_fan_speed_ufactor_times_area_value`')
            if value > 300000.0:
                raise ValueError('value need to be smaller 300000.0 '
                                 'for field `low_fan_speed_ufactor_times_area_value`')
        self._data["Low Fan Speed U-factor Times Area Value"] = value

    @property
    def low_fan_speed_ufactor_times_area_sizing_factor(self):
        """Get low_fan_speed_ufactor_times_area_sizing_factor

        Returns:
            float: the value of `low_fan_speed_ufactor_times_area_sizing_factor` or None if not set
        """
        return self._data["Low Fan Speed U-Factor Times Area Sizing Factor"]

    @low_fan_speed_ufactor_times_area_sizing_factor.setter
    def low_fan_speed_ufactor_times_area_sizing_factor(self, value=0.6):
        """  Corresponds to IDD Field `Low Fan Speed U-Factor Times Area Sizing Factor`
        This field is only used if the previous field is set to autocalculate and
        the Performance Input Method is UFactorTimesAreaAndDesignWaterFlowRate

        Args:
            value (float): value for IDD Field `Low Fan Speed U-Factor Times Area Sizing Factor`
                Default value: 0.6
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `low_fan_speed_ufactor_times_area_sizing_factor`'.format(value))
        self._data["Low Fan Speed U-Factor Times Area Sizing Factor"] = value

    @property
    def design_water_flow_rate(self):
        """Get design_water_flow_rate

        Returns:
            float: the value of `design_water_flow_rate` or None if not set
        """
        return self._data["Design Water Flow Rate"]

    @design_water_flow_rate.setter
    def design_water_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Design Water Flow Rate`
        Input value is ignored if fluid cooler Performance Input Method= StandardDesignCapacity

        Args:
            value (float or "Autosize"): value for IDD Field `Design Water Flow Rate`
                Units: m3/s
                IP-Units: gal/min
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Design Water Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `design_water_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `design_water_flow_rate`')
        self._data["Design Water Flow Rate"] = value

    @property
    def high_speed_user_specified_design_capacity(self):
        """Get high_speed_user_specified_design_capacity

        Returns:
            float: the value of `high_speed_user_specified_design_capacity` or None if not set
        """
        return self._data["High Speed User Specified Design Capacity"]

    @high_speed_user_specified_design_capacity.setter
    def high_speed_user_specified_design_capacity(self, value=None):
        """  Corresponds to IDD Field `High Speed User Specified Design Capacity`
        Only used for Performance Input Method = UserSpecifiedDesignCapacity;
        for other Performance Input Methods, this field is ignored.

        Args:
            value (float): value for IDD Field `High Speed User Specified Design Capacity`
                Units: W
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `high_speed_user_specified_design_capacity`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `high_speed_user_specified_design_capacity`')
        self._data["High Speed User Specified Design Capacity"] = value

    @property
    def low_speed_user_specified_design_capacity(self):
        """Get low_speed_user_specified_design_capacity

        Returns:
            float: the value of `low_speed_user_specified_design_capacity` or None if not set
        """
        return self._data["Low Speed User Specified Design Capacity"]

    @low_speed_user_specified_design_capacity.setter
    def low_speed_user_specified_design_capacity(self, value=None):
        """  Corresponds to IDD Field `Low Speed User Specified Design Capacity`
        Only used for Performance Input Method = UserSpecifiedDesignCapacity;
        for other Performance Input Methods, this field is ignored.

        Args:
            value (float or "Autocalculate"): value for IDD Field `Low Speed User Specified Design Capacity`
                Units: W
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autocalculate":
                    self._data["Low Speed User Specified Design Capacity"] = "Autocalculate"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `low_speed_user_specified_design_capacity`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `low_speed_user_specified_design_capacity`')
        self._data["Low Speed User Specified Design Capacity"] = value

    @property
    def low_speed_user_specified_design_capacity_sizing_factor(self):
        """Get low_speed_user_specified_design_capacity_sizing_factor

        Returns:
            float: the value of `low_speed_user_specified_design_capacity_sizing_factor` or None if not set
        """
        return self._data["Low Speed User Specified Design Capacity Sizing Factor"]

    @low_speed_user_specified_design_capacity_sizing_factor.setter
    def low_speed_user_specified_design_capacity_sizing_factor(self, value=0.5):
        """  Corresponds to IDD Field `Low Speed User Specified Design Capacity Sizing Factor`
        This field is only used if the previous field is set to autocalculate

        Args:
            value (float): value for IDD Field `Low Speed User Specified Design Capacity Sizing Factor`
                Default value: 0.5
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `low_speed_user_specified_design_capacity_sizing_factor`'.format(value))
        self._data["Low Speed User Specified Design Capacity Sizing Factor"] = value

    @property
    def design_entering_water_temperature(self):
        """Get design_entering_water_temperature

        Returns:
            float: the value of `design_entering_water_temperature` or None if not set
        """
        return self._data["Design Entering Water Temperature"]

    @design_entering_water_temperature.setter
    def design_entering_water_temperature(self, value=None):
        """  Corresponds to IDD Field `Design Entering Water Temperature`
        Only used for Performance Input Method = UserSpecifiedDesignCapacity;
        for other Performance Input Methods, this field is ignored.
        Design Entering Water Temperature must be greater than Design Entering Air Temperature.

        Args:
            value (float): value for IDD Field `Design Entering Water Temperature`
                Units: C
                IP-Units: F
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `design_entering_water_temperature`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `design_entering_water_temperature`')
        self._data["Design Entering Water Temperature"] = value

    @property
    def design_entering_air_temperature(self):
        """Get design_entering_air_temperature

        Returns:
            float: the value of `design_entering_air_temperature` or None if not set
        """
        return self._data["Design Entering Air Temperature"]

    @design_entering_air_temperature.setter
    def design_entering_air_temperature(self, value=None):
        """  Corresponds to IDD Field `Design Entering Air Temperature`
        Only used for Performance Input Method = UserSpecifiedDesignCapacity;
        for other Performance Input Methods, this field is ignored.
        Design Entering Air Temperature must be greater than Design Entering Air Wet-bulb
        Temperature.

        Args:
            value (float): value for IDD Field `Design Entering Air Temperature`
                Units: C
                IP-Units: F
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `design_entering_air_temperature`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `design_entering_air_temperature`')
        self._data["Design Entering Air Temperature"] = value

    @property
    def design_entering_air_wetbulb_temperature(self):
        """Get design_entering_air_wetbulb_temperature

        Returns:
            float: the value of `design_entering_air_wetbulb_temperature` or None if not set
        """
        return self._data["Design Entering Air Wet-bulb Temperature"]

    @design_entering_air_wetbulb_temperature.setter
    def design_entering_air_wetbulb_temperature(self, value=None):
        """  Corresponds to IDD Field `Design Entering Air Wet-bulb Temperature`
        Only used for Performance Input Method = UserSpecifiedDesignCapacity;
        for other Performance Input Methods, this field is ignored.
        Design Entering Air Wet-bulb Temperature must be less than Design Entering Air
        Temperature.

        Args:
            value (float): value for IDD Field `Design Entering Air Wet-bulb Temperature`
                Units: C
                IP-Units: F
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `design_entering_air_wetbulb_temperature`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `design_entering_air_wetbulb_temperature`')
        self._data["Design Entering Air Wet-bulb Temperature"] = value

    @property
    def high_speed_sizing_factor(self):
        """Get high_speed_sizing_factor

        Returns:
            float: the value of `high_speed_sizing_factor` or None if not set
        """
        return self._data["High Speed Sizing Factor"]

    @high_speed_sizing_factor.setter
    def high_speed_sizing_factor(self, value=1.0):
        """  Corresponds to IDD Field `High Speed Sizing Factor`
        Multiplies the autosized capacity and flow rates

        Args:
            value (float): value for IDD Field `High Speed Sizing Factor`
                Default value: 1.0
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `high_speed_sizing_factor`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `high_speed_sizing_factor`')
        self._data["High Speed Sizing Factor"] = value

    @property
    def evaporation_loss_mode(self):
        """Get evaporation_loss_mode

        Returns:
            str: the value of `evaporation_loss_mode` or None if not set
        """
        return self._data["Evaporation Loss Mode"]

    @evaporation_loss_mode.setter
    def evaporation_loss_mode(self, value="SaturatedExit"):
        """  Corresponds to IDD Field `Evaporation Loss Mode`

        Args:
            value (str): value for IDD Field `Evaporation Loss Mode`
                Accepted values are:
                      - LossFactor
                      - SaturatedExit
                Default value: SaturatedExit
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `evaporation_loss_mode`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `evaporation_loss_mode`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `evaporation_loss_mode`')
            vals = {}
            vals["lossfactor"] = "LossFactor"
            vals["saturatedexit"] = "SaturatedExit"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `evaporation_loss_mode`'.format(value))
            value = vals[value_lower]
        self._data["Evaporation Loss Mode"] = value

    @property
    def evaporation_loss_factor(self):
        """Get evaporation_loss_factor

        Returns:
            float: the value of `evaporation_loss_factor` or None if not set
        """
        return self._data["Evaporation Loss Factor"]

    @evaporation_loss_factor.setter
    def evaporation_loss_factor(self, value=None):
        """  Corresponds to IDD Field `Evaporation Loss Factor`
        Rate of water evaporation from the Fluid Cooler and lost to the outdoor air [%/K]
        Empirical correlation is used to calculate default loss factor if it not explicitly provided.

        Args:
            value (float): value for IDD Field `Evaporation Loss Factor`
                Units: percent/K
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `evaporation_loss_factor`'.format(value))
        self._data["Evaporation Loss Factor"] = value

    @property
    def drift_loss_percent(self):
        """Get drift_loss_percent

        Returns:
            float: the value of `drift_loss_percent` or None if not set
        """
        return self._data["Drift Loss Percent"]

    @drift_loss_percent.setter
    def drift_loss_percent(self, value=0.008):
        """  Corresponds to IDD Field `Drift Loss Percent`
        Default value is under investigation. For now cooling towers default value is taken.

        Args:
            value (float): value for IDD Field `Drift Loss Percent`
                Units: percent
                Default value: 0.008
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `drift_loss_percent`'.format(value))
        self._data["Drift Loss Percent"] = value

    @property
    def blowdown_calculation_mode(self):
        """Get blowdown_calculation_mode

        Returns:
            str: the value of `blowdown_calculation_mode` or None if not set
        """
        return self._data["Blowdown Calculation Mode"]

    @blowdown_calculation_mode.setter
    def blowdown_calculation_mode(self, value="ConcentrationRatio"):
        """  Corresponds to IDD Field `Blowdown Calculation Mode`

        Args:
            value (str): value for IDD Field `Blowdown Calculation Mode`
                Accepted values are:
                      - ConcentrationRatio
                      - ScheduledRate
                Default value: ConcentrationRatio
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `blowdown_calculation_mode`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `blowdown_calculation_mode`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `blowdown_calculation_mode`')
            vals = {}
            vals["concentrationratio"] = "ConcentrationRatio"
            vals["scheduledrate"] = "ScheduledRate"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `blowdown_calculation_mode`'.format(value))
            value = vals[value_lower]
        self._data["Blowdown Calculation Mode"] = value

    @property
    def blowdown_concentration_ratio(self):
        """Get blowdown_concentration_ratio

        Returns:
            float: the value of `blowdown_concentration_ratio` or None if not set
        """
        return self._data["Blowdown Concentration Ratio"]

    @blowdown_concentration_ratio.setter
    def blowdown_concentration_ratio(self, value=3.0):
        """  Corresponds to IDD Field `Blowdown Concentration Ratio`
        Characterizes the rate of blowdown in the Evaporative Fluid Cooler.
        Blowdown is water intentionally drained from the Evaporative Fluid Cooler in order to offset the
        build up of solids in the water that would otherwise occur because of evaporation.
        Ratio of solids in the blowdown water to solids in the make up water.
        Default value is under investigation. For now cooling towers default value is taken.

        Args:
            value (float): value for IDD Field `Blowdown Concentration Ratio`
                Default value: 3.0
                value >= 2.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `blowdown_concentration_ratio`'.format(value))
            if value < 2.0:
                raise ValueError('value need to be greater or equal 2.0 '
                                 'for field `blowdown_concentration_ratio`')
        self._data["Blowdown Concentration Ratio"] = value

    @property
    def blowdown_makeup_water_usage_schedule_name(self):
        """Get blowdown_makeup_water_usage_schedule_name

        Returns:
            str: the value of `blowdown_makeup_water_usage_schedule_name` or None if not set
        """
        return self._data["Blowdown Makeup Water Usage Schedule Name"]

    @blowdown_makeup_water_usage_schedule_name.setter
    def blowdown_makeup_water_usage_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Blowdown Makeup Water Usage Schedule Name`
        Makeup water usage due to blowdown results from occasionally draining some amount
        of water in the Evaporative Fluid Cooler basin to purge scale or other contaminants to reduce
        their concentration in order to maintain an acceptable level of water quality.
        Schedule values should reflect water usage in m3/s.

        Args:
            value (str): value for IDD Field `Blowdown Makeup Water Usage Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `blowdown_makeup_water_usage_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `blowdown_makeup_water_usage_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `blowdown_makeup_water_usage_schedule_name`')
        self._data["Blowdown Makeup Water Usage Schedule Name"] = value

    @property
    def supply_water_storage_tank_name(self):
        """Get supply_water_storage_tank_name

        Returns:
            str: the value of `supply_water_storage_tank_name` or None if not set
        """
        return self._data["Supply Water Storage Tank Name"]

    @supply_water_storage_tank_name.setter
    def supply_water_storage_tank_name(self, value=None):
        """  Corresponds to IDD Field `Supply Water Storage Tank Name`

        Args:
            value (str): value for IDD Field `Supply Water Storage Tank Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_water_storage_tank_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_water_storage_tank_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `supply_water_storage_tank_name`')
        self._data["Supply Water Storage Tank Name"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
        return good

    @classmethod
    def _to_str(cls, value):
        """ Represents values either as string or None values as empty string

        Args:
            value: a value
        """
        if value is None:
            return ''
        else:
            return str(value)

    def export(self):
        """ Export values of data object as list of strings"""
        out = []
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class FluidCoolerSingleSpeed(object):
    """ Corresponds to IDD object `FluidCooler:SingleSpeed`
        The fluid cooler is modeled as a cross flow heat exchanger (both streams unmixed) with
        single-speed fans (induced draft configuration).
    
    """
    internal_name = "FluidCooler:SingleSpeed"
    field_count = 13
    required_fields = ["Name", "Water Inlet Node Name", "Water Outlet Node Name", "Design Entering Water Temperature", "Design Entering Air Temperature", "Design Entering Air Wetbulb Temperature", "Design Water Flow Rate", "Design Air Flow Rate", "Design Air Flow Rate Fan Power"]

    def __init__(self):
        """ Init data dictionary object for IDD  `FluidCooler:SingleSpeed`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Water Inlet Node Name"] = None
        self._data["Water Outlet Node Name"] = None
        self._data["Performance Input Method"] = None
        self._data["Design Air Flow Rate U-factor Times Area Value"] = None
        self._data["Nominal Capacity"] = None
        self._data["Design Entering Water Temperature"] = None
        self._data["Design Entering Air Temperature"] = None
        self._data["Design Entering Air Wetbulb Temperature"] = None
        self._data["Design Water Flow Rate"] = None
        self._data["Design Air Flow Rate"] = None
        self._data["Design Air Flow Rate Fan Power"] = None
        self._data["Outdoor Air Inlet Node Name"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.water_inlet_node_name = None
        else:
            self.water_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.water_outlet_node_name = None
        else:
            self.water_outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.performance_input_method = None
        else:
            self.performance_input_method = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_air_flow_rate_ufactor_times_area_value = None
        else:
            self.design_air_flow_rate_ufactor_times_area_value = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.nominal_capacity = None
        else:
            self.nominal_capacity = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_entering_water_temperature = None
        else:
            self.design_entering_water_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_entering_air_temperature = None
        else:
            self.design_entering_air_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_entering_air_wetbulb_temperature = None
        else:
            self.design_entering_air_wetbulb_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_water_flow_rate = None
        else:
            self.design_water_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_air_flow_rate = None
        else:
            self.design_air_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_air_flow_rate_fan_power = None
        else:
            self.design_air_flow_rate_fan_power = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outdoor_air_inlet_node_name = None
        else:
            self.outdoor_air_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `Name`
        fluid cooler name

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')
        self._data["Name"] = value

    @property
    def water_inlet_node_name(self):
        """Get water_inlet_node_name

        Returns:
            str: the value of `water_inlet_node_name` or None if not set
        """
        return self._data["Water Inlet Node Name"]

    @water_inlet_node_name.setter
    def water_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Water Inlet Node Name`
        Name of fluid cooler water inlet node

        Args:
            value (str): value for IDD Field `Water Inlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `water_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `water_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `water_inlet_node_name`')
        self._data["Water Inlet Node Name"] = value

    @property
    def water_outlet_node_name(self):
        """Get water_outlet_node_name

        Returns:
            str: the value of `water_outlet_node_name` or None if not set
        """
        return self._data["Water Outlet Node Name"]

    @water_outlet_node_name.setter
    def water_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Water Outlet Node Name`
        Name of fluid cooler water outlet node

        Args:
            value (str): value for IDD Field `Water Outlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `water_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `water_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `water_outlet_node_name`')
        self._data["Water Outlet Node Name"] = value

    @property
    def performance_input_method(self):
        """Get performance_input_method

        Returns:
            str: the value of `performance_input_method` or None if not set
        """
        return self._data["Performance Input Method"]

    @performance_input_method.setter
    def performance_input_method(self, value="NominalCapacity"):
        """  Corresponds to IDD Field `Performance Input Method`
        User can define fluid cooler thermal performance by specifying the fluid cooler UA
        and the Design Water Flow Rate, or by specifying the fluid cooler nominal capacity

        Args:
            value (str): value for IDD Field `Performance Input Method`
                Default value: NominalCapacity
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `performance_input_method`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `performance_input_method`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `performance_input_method`')
        self._data["Performance Input Method"] = value

    @property
    def design_air_flow_rate_ufactor_times_area_value(self):
        """Get design_air_flow_rate_ufactor_times_area_value

        Returns:
            float: the value of `design_air_flow_rate_ufactor_times_area_value` or None if not set
        """
        return self._data["Design Air Flow Rate U-factor Times Area Value"]

    @design_air_flow_rate_ufactor_times_area_value.setter
    def design_air_flow_rate_ufactor_times_area_value(self, value=None):
        """  Corresponds to IDD Field `Design Air Flow Rate U-factor Times Area Value`
        Leave field blank if fluid cooler Performance Input Method is NominalCapacity

        Args:
            value (float or "Autosize"): value for IDD Field `Design Air Flow Rate U-factor Times Area Value`
                Units: W/K
                value > 0.0
                value <= 2100000.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Design Air Flow Rate U-factor Times Area Value"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `design_air_flow_rate_ufactor_times_area_value`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `design_air_flow_rate_ufactor_times_area_value`')
            if value > 2100000.0:
                raise ValueError('value need to be smaller 2100000.0 '
                                 'for field `design_air_flow_rate_ufactor_times_area_value`')
        self._data["Design Air Flow Rate U-factor Times Area Value"] = value

    @property
    def nominal_capacity(self):
        """Get nominal_capacity

        Returns:
            float: the value of `nominal_capacity` or None if not set
        """
        return self._data["Nominal Capacity"]

    @nominal_capacity.setter
    def nominal_capacity(self, value=None):
        """  Corresponds to IDD Field `Nominal Capacity`
        Nominal fluid cooler capacity

        Args:
            value (float): value for IDD Field `Nominal Capacity`
                Units: W
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `nominal_capacity`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `nominal_capacity`')
        self._data["Nominal Capacity"] = value

    @property
    def design_entering_water_temperature(self):
        """Get design_entering_water_temperature

        Returns:
            float: the value of `design_entering_water_temperature` or None if not set
        """
        return self._data["Design Entering Water Temperature"]

    @design_entering_water_temperature.setter
    def design_entering_water_temperature(self, value=None):
        """  Corresponds to IDD Field `Design Entering Water Temperature`
        Design Entering Water Temperature must be specified for both the performance input methods and
        its value must be greater than Design Entering Air Temperature.

        Args:
            value (float): value for IDD Field `Design Entering Water Temperature`
                Units: C
                IP-Units: F
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `design_entering_water_temperature`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `design_entering_water_temperature`')
        self._data["Design Entering Water Temperature"] = value

    @property
    def design_entering_air_temperature(self):
        """Get design_entering_air_temperature

        Returns:
            float: the value of `design_entering_air_temperature` or None if not set
        """
        return self._data["Design Entering Air Temperature"]

    @design_entering_air_temperature.setter
    def design_entering_air_temperature(self, value=None):
        """  Corresponds to IDD Field `Design Entering Air Temperature`
        Design Entering Air Temperature must be specified for both the performance input methods and
        its value must be greater than Design Entering Air Wet-bulb Temperature.

        Args:
            value (float): value for IDD Field `Design Entering Air Temperature`
                Units: C
                IP-Units: F
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `design_entering_air_temperature`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `design_entering_air_temperature`')
        self._data["Design Entering Air Temperature"] = value

    @property
    def design_entering_air_wetbulb_temperature(self):
        """Get design_entering_air_wetbulb_temperature

        Returns:
            float: the value of `design_entering_air_wetbulb_temperature` or None if not set
        """
        return self._data["Design Entering Air Wetbulb Temperature"]

    @design_entering_air_wetbulb_temperature.setter
    def design_entering_air_wetbulb_temperature(self, value=None):
        """  Corresponds to IDD Field `Design Entering Air Wetbulb Temperature`
        Design Entering Air Wet-bulb Temperature must be specified for both the performance input methods and
        its value must be less than Design Entering Air Temperature.

        Args:
            value (float): value for IDD Field `Design Entering Air Wetbulb Temperature`
                Units: C
                IP-Units: F
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `design_entering_air_wetbulb_temperature`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `design_entering_air_wetbulb_temperature`')
        self._data["Design Entering Air Wetbulb Temperature"] = value

    @property
    def design_water_flow_rate(self):
        """Get design_water_flow_rate

        Returns:
            float: the value of `design_water_flow_rate` or None if not set
        """
        return self._data["Design Water Flow Rate"]

    @design_water_flow_rate.setter
    def design_water_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Design Water Flow Rate`

        Args:
            value (float or "Autosize"): value for IDD Field `Design Water Flow Rate`
                Units: m3/s
                IP-Units: gal/min
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Design Water Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `design_water_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `design_water_flow_rate`')
        self._data["Design Water Flow Rate"] = value

    @property
    def design_air_flow_rate(self):
        """Get design_air_flow_rate

        Returns:
            float: the value of `design_air_flow_rate` or None if not set
        """
        return self._data["Design Air Flow Rate"]

    @design_air_flow_rate.setter
    def design_air_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Design Air Flow Rate`

        Args:
            value (float or "Autosize"): value for IDD Field `Design Air Flow Rate`
                Units: m3/s
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Design Air Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `design_air_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `design_air_flow_rate`')
        self._data["Design Air Flow Rate"] = value

    @property
    def design_air_flow_rate_fan_power(self):
        """Get design_air_flow_rate_fan_power

        Returns:
            float: the value of `design_air_flow_rate_fan_power` or None if not set
        """
        return self._data["Design Air Flow Rate Fan Power"]

    @design_air_flow_rate_fan_power.setter
    def design_air_flow_rate_fan_power(self, value=None):
        """  Corresponds to IDD Field `Design Air Flow Rate Fan Power`
        This is the fan motor electric input power

        Args:
            value (float or "Autosize"): value for IDD Field `Design Air Flow Rate Fan Power`
                Units: W
                IP-Units: W
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Design Air Flow Rate Fan Power"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `design_air_flow_rate_fan_power`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `design_air_flow_rate_fan_power`')
        self._data["Design Air Flow Rate Fan Power"] = value

    @property
    def outdoor_air_inlet_node_name(self):
        """Get outdoor_air_inlet_node_name

        Returns:
            str: the value of `outdoor_air_inlet_node_name` or None if not set
        """
        return self._data["Outdoor Air Inlet Node Name"]

    @outdoor_air_inlet_node_name.setter
    def outdoor_air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Outdoor Air Inlet Node Name`
        Enter the name of an outdoor air node

        Args:
            value (str): value for IDD Field `Outdoor Air Inlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `outdoor_air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outdoor_air_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `outdoor_air_inlet_node_name`')
        self._data["Outdoor Air Inlet Node Name"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
        return good

    @classmethod
    def _to_str(cls, value):
        """ Represents values either as string or None values as empty string

        Args:
            value: a value
        """
        if value is None:
            return ''
        else:
            return str(value)

    def export(self):
        """ Export values of data object as list of strings"""
        out = []
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class FluidCoolerTwoSpeed(object):
    """ Corresponds to IDD object `FluidCooler:TwoSpeed`
        The fluid cooler is modeled as a cross flow heat exchanger (both streams unmixed) with
        two-speed fans (induced draft configuration).
    
    """
    internal_name = "FluidCooler:TwoSpeed"
    field_count = 21
    required_fields = ["Name", "Water Inlet Node Name", "Water Outlet Node Name", "Low Fan Speed U-Factor Times Area Sizing Factor", "Low Speed Nominal Capacity Sizing Factor", "Design Entering Water Temperature", "Design Entering Air Temperature", "Design Entering Air Wet-bulb Temperature", "Design Water Flow Rate", "High Fan Speed Air Flow Rate", "High Fan Speed Fan Power", "Low Fan Speed Air Flow Rate", "Low Fan Speed Air Flow Rate Sizing Factor", "Low Fan Speed Fan Power", "Low Fan Speed Fan Power Sizing Factor"]

    def __init__(self):
        """ Init data dictionary object for IDD  `FluidCooler:TwoSpeed`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Water Inlet Node Name"] = None
        self._data["Water Outlet Node Name"] = None
        self._data["Performance Input Method"] = None
        self._data["High Fan Speed U-factor Times Area Value"] = None
        self._data["Low Fan Speed U-factor Times Area Value"] = None
        self._data["Low Fan Speed U-Factor Times Area Sizing Factor"] = None
        self._data["High Speed Nominal Capacity"] = None
        self._data["Low Speed Nominal Capacity"] = None
        self._data["Low Speed Nominal Capacity Sizing Factor"] = None
        self._data["Design Entering Water Temperature"] = None
        self._data["Design Entering Air Temperature"] = None
        self._data["Design Entering Air Wet-bulb Temperature"] = None
        self._data["Design Water Flow Rate"] = None
        self._data["High Fan Speed Air Flow Rate"] = None
        self._data["High Fan Speed Fan Power"] = None
        self._data["Low Fan Speed Air Flow Rate"] = None
        self._data["Low Fan Speed Air Flow Rate Sizing Factor"] = None
        self._data["Low Fan Speed Fan Power"] = None
        self._data["Low Fan Speed Fan Power Sizing Factor"] = None
        self._data["Outdoor Air Inlet Node Name"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.water_inlet_node_name = None
        else:
            self.water_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.water_outlet_node_name = None
        else:
            self.water_outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.performance_input_method = None
        else:
            self.performance_input_method = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.high_fan_speed_ufactor_times_area_value = None
        else:
            self.high_fan_speed_ufactor_times_area_value = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.low_fan_speed_ufactor_times_area_value = None
        else:
            self.low_fan_speed_ufactor_times_area_value = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.low_fan_speed_ufactor_times_area_sizing_factor = None
        else:
            self.low_fan_speed_ufactor_times_area_sizing_factor = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.high_speed_nominal_capacity = None
        else:
            self.high_speed_nominal_capacity = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.low_speed_nominal_capacity = None
        else:
            self.low_speed_nominal_capacity = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.low_speed_nominal_capacity_sizing_factor = None
        else:
            self.low_speed_nominal_capacity_sizing_factor = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_entering_water_temperature = None
        else:
            self.design_entering_water_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_entering_air_temperature = None
        else:
            self.design_entering_air_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_entering_air_wetbulb_temperature = None
        else:
            self.design_entering_air_wetbulb_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_water_flow_rate = None
        else:
            self.design_water_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.high_fan_speed_air_flow_rate = None
        else:
            self.high_fan_speed_air_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.high_fan_speed_fan_power = None
        else:
            self.high_fan_speed_fan_power = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.low_fan_speed_air_flow_rate = None
        else:
            self.low_fan_speed_air_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.low_fan_speed_air_flow_rate_sizing_factor = None
        else:
            self.low_fan_speed_air_flow_rate_sizing_factor = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.low_fan_speed_fan_power = None
        else:
            self.low_fan_speed_fan_power = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.low_fan_speed_fan_power_sizing_factor = None
        else:
            self.low_fan_speed_fan_power_sizing_factor = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outdoor_air_inlet_node_name = None
        else:
            self.outdoor_air_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `Name`
        fluid cooler name

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')
        self._data["Name"] = value

    @property
    def water_inlet_node_name(self):
        """Get water_inlet_node_name

        Returns:
            str: the value of `water_inlet_node_name` or None if not set
        """
        return self._data["Water Inlet Node Name"]

    @water_inlet_node_name.setter
    def water_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Water Inlet Node Name`
        Name of fluid cooler water inlet node

        Args:
            value (str): value for IDD Field `Water Inlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `water_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `water_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `water_inlet_node_name`')
        self._data["Water Inlet Node Name"] = value

    @property
    def water_outlet_node_name(self):
        """Get water_outlet_node_name

        Returns:
            str: the value of `water_outlet_node_name` or None if not set
        """
        return self._data["Water Outlet Node Name"]

    @water_outlet_node_name.setter
    def water_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Water Outlet Node Name`
        Name of fluid cooler water outlet node

        Args:
            value (str): value for IDD Field `Water Outlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `water_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `water_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `water_outlet_node_name`')
        self._data["Water Outlet Node Name"] = value

    @property
    def performance_input_method(self):
        """Get performance_input_method

        Returns:
            str: the value of `performance_input_method` or None if not set
        """
        return self._data["Performance Input Method"]

    @performance_input_method.setter
    def performance_input_method(self, value="NominalCapacity"):
        """  Corresponds to IDD Field `Performance Input Method`
        User can define fluid cooler thermal performance by specifying the fluid cooler UA
        and the Design Water Flow Rate, or by specifying the fluid cooler nominal capacity

        Args:
            value (str): value for IDD Field `Performance Input Method`
                Default value: NominalCapacity
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `performance_input_method`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `performance_input_method`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `performance_input_method`')
        self._data["Performance Input Method"] = value

    @property
    def high_fan_speed_ufactor_times_area_value(self):
        """Get high_fan_speed_ufactor_times_area_value

        Returns:
            float: the value of `high_fan_speed_ufactor_times_area_value` or None if not set
        """
        return self._data["High Fan Speed U-factor Times Area Value"]

    @high_fan_speed_ufactor_times_area_value.setter
    def high_fan_speed_ufactor_times_area_value(self, value=None):
        """  Corresponds to IDD Field `High Fan Speed U-factor Times Area Value`
        Leave field blank if fluid cooler Performance Input Method is NominalCapacity

        Args:
            value (float or "Autosize"): value for IDD Field `High Fan Speed U-factor Times Area Value`
                Units: W/K
                value > 0.0
                value <= 2100000.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["High Fan Speed U-factor Times Area Value"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `high_fan_speed_ufactor_times_area_value`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `high_fan_speed_ufactor_times_area_value`')
            if value > 2100000.0:
                raise ValueError('value need to be smaller 2100000.0 '
                                 'for field `high_fan_speed_ufactor_times_area_value`')
        self._data["High Fan Speed U-factor Times Area Value"] = value

    @property
    def low_fan_speed_ufactor_times_area_value(self):
        """Get low_fan_speed_ufactor_times_area_value

        Returns:
            float: the value of `low_fan_speed_ufactor_times_area_value` or None if not set
        """
        return self._data["Low Fan Speed U-factor Times Area Value"]

    @low_fan_speed_ufactor_times_area_value.setter
    def low_fan_speed_ufactor_times_area_value(self, value=None):
        """  Corresponds to IDD Field `Low Fan Speed U-factor Times Area Value`
        Leave field blank if fluid cooler Performance Input Method is NominalCapacity
        Low speed fluid cooler UA must be less than high speed fluid cooler UA
        Low speed fluid cooler UA must be greater than free convection fluid cooler UA

        Args:
            value (float or "Autocalculate"): value for IDD Field `Low Fan Speed U-factor Times Area Value`
                Units: W/K
                value > 0.0
                value <= 300000.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autocalculate":
                    self._data["Low Fan Speed U-factor Times Area Value"] = "Autocalculate"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `low_fan_speed_ufactor_times_area_value`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `low_fan_speed_ufactor_times_area_value`')
            if value > 300000.0:
                raise ValueError('value need to be smaller 300000.0 '
                                 'for field `low_fan_speed_ufactor_times_area_value`')
        self._data["Low Fan Speed U-factor Times Area Value"] = value

    @property
    def low_fan_speed_ufactor_times_area_sizing_factor(self):
        """Get low_fan_speed_ufactor_times_area_sizing_factor

        Returns:
            float: the value of `low_fan_speed_ufactor_times_area_sizing_factor` or None if not set
        """
        return self._data["Low Fan Speed U-Factor Times Area Sizing Factor"]

    @low_fan_speed_ufactor_times_area_sizing_factor.setter
    def low_fan_speed_ufactor_times_area_sizing_factor(self, value=0.6):
        """  Corresponds to IDD Field `Low Fan Speed U-Factor Times Area Sizing Factor`
        This field is only used if the previous field is set to autocalculate and
        the Performance Input Method is UFactorTimesAreaAndDesignWaterFlowRate

        Args:
            value (float): value for IDD Field `Low Fan Speed U-Factor Times Area Sizing Factor`
                Default value: 0.6
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `low_fan_speed_ufactor_times_area_sizing_factor`'.format(value))
        self._data["Low Fan Speed U-Factor Times Area Sizing Factor"] = value

    @property
    def high_speed_nominal_capacity(self):
        """Get high_speed_nominal_capacity

        Returns:
            float: the value of `high_speed_nominal_capacity` or None if not set
        """
        return self._data["High Speed Nominal Capacity"]

    @high_speed_nominal_capacity.setter
    def high_speed_nominal_capacity(self, value=None):
        """  Corresponds to IDD Field `High Speed Nominal Capacity`
        Nominal fluid cooler capacity at high fan speed

        Args:
            value (float): value for IDD Field `High Speed Nominal Capacity`
                Units: W
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `high_speed_nominal_capacity`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `high_speed_nominal_capacity`')
        self._data["High Speed Nominal Capacity"] = value

    @property
    def low_speed_nominal_capacity(self):
        """Get low_speed_nominal_capacity

        Returns:
            float: the value of `low_speed_nominal_capacity` or None if not set
        """
        return self._data["Low Speed Nominal Capacity"]

    @low_speed_nominal_capacity.setter
    def low_speed_nominal_capacity(self, value=None):
        """  Corresponds to IDD Field `Low Speed Nominal Capacity`
        Nominal fluid cooler capacity at low fan speed

        Args:
            value (float or "Autocalculate"): value for IDD Field `Low Speed Nominal Capacity`
                Units: W
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autocalculate":
                    self._data["Low Speed Nominal Capacity"] = "Autocalculate"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `low_speed_nominal_capacity`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `low_speed_nominal_capacity`')
        self._data["Low Speed Nominal Capacity"] = value

    @property
    def low_speed_nominal_capacity_sizing_factor(self):
        """Get low_speed_nominal_capacity_sizing_factor

        Returns:
            float: the value of `low_speed_nominal_capacity_sizing_factor` or None if not set
        """
        return self._data["Low Speed Nominal Capacity Sizing Factor"]

    @low_speed_nominal_capacity_sizing_factor.setter
    def low_speed_nominal_capacity_sizing_factor(self, value=0.5):
        """  Corresponds to IDD Field `Low Speed Nominal Capacity Sizing Factor`
        This field is only used if the previous field is set to autocalculate and
        the Performance Input Method is NominalCapacity

        Args:
            value (float): value for IDD Field `Low Speed Nominal Capacity Sizing Factor`
                Default value: 0.5
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `low_speed_nominal_capacity_sizing_factor`'.format(value))
        self._data["Low Speed Nominal Capacity Sizing Factor"] = value

    @property
    def design_entering_water_temperature(self):
        """Get design_entering_water_temperature

        Returns:
            float: the value of `design_entering_water_temperature` or None if not set
        """
        return self._data["Design Entering Water Temperature"]

    @design_entering_water_temperature.setter
    def design_entering_water_temperature(self, value=None):
        """  Corresponds to IDD Field `Design Entering Water Temperature`
        Design Entering Water Temperature must be specified for both the performance input methods and
        its value must be greater than Design Entering Air Temperature.

        Args:
            value (float): value for IDD Field `Design Entering Water Temperature`
                Units: C
                IP-Units: F
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `design_entering_water_temperature`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `design_entering_water_temperature`')
        self._data["Design Entering Water Temperature"] = value

    @property
    def design_entering_air_temperature(self):
        """Get design_entering_air_temperature

        Returns:
            float: the value of `design_entering_air_temperature` or None if not set
        """
        return self._data["Design Entering Air Temperature"]

    @design_entering_air_temperature.setter
    def design_entering_air_temperature(self, value=None):
        """  Corresponds to IDD Field `Design Entering Air Temperature`
        Design Entering Air Temperature must be specified for both the performance input methods and
        its value must be greater than Design Entering Air Wet-bulb Temperature.

        Args:
            value (float): value for IDD Field `Design Entering Air Temperature`
                Units: C
                IP-Units: F
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `design_entering_air_temperature`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `design_entering_air_temperature`')
        self._data["Design Entering Air Temperature"] = value

    @property
    def design_entering_air_wetbulb_temperature(self):
        """Get design_entering_air_wetbulb_temperature

        Returns:
            float: the value of `design_entering_air_wetbulb_temperature` or None if not set
        """
        return self._data["Design Entering Air Wet-bulb Temperature"]

    @design_entering_air_wetbulb_temperature.setter
    def design_entering_air_wetbulb_temperature(self, value=None):
        """  Corresponds to IDD Field `Design Entering Air Wet-bulb Temperature`
        Design Entering Air Wet-bulb Temperature must be specified for both the performance input methods and
        its value must be less than Design Entering Air Temperature.

        Args:
            value (float): value for IDD Field `Design Entering Air Wet-bulb Temperature`
                Units: C
                IP-Units: F
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `design_entering_air_wetbulb_temperature`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `design_entering_air_wetbulb_temperature`')
        self._data["Design Entering Air Wet-bulb Temperature"] = value

    @property
    def design_water_flow_rate(self):
        """Get design_water_flow_rate

        Returns:
            float: the value of `design_water_flow_rate` or None if not set
        """
        return self._data["Design Water Flow Rate"]

    @design_water_flow_rate.setter
    def design_water_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Design Water Flow Rate`

        Args:
            value (float or "Autosize"): value for IDD Field `Design Water Flow Rate`
                Units: m3/s
                IP-Units: gal/min
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Design Water Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `design_water_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `design_water_flow_rate`')
        self._data["Design Water Flow Rate"] = value

    @property
    def high_fan_speed_air_flow_rate(self):
        """Get high_fan_speed_air_flow_rate

        Returns:
            float: the value of `high_fan_speed_air_flow_rate` or None if not set
        """
        return self._data["High Fan Speed Air Flow Rate"]

    @high_fan_speed_air_flow_rate.setter
    def high_fan_speed_air_flow_rate(self, value=None):
        """  Corresponds to IDD Field `High Fan Speed Air Flow Rate`
        Air Flow Rate at High Fan Speed must be greater than Air Flow Rate at Low Fan Speed

        Args:
            value (float or "Autosize"): value for IDD Field `High Fan Speed Air Flow Rate`
                Units: m3/s
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["High Fan Speed Air Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `high_fan_speed_air_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `high_fan_speed_air_flow_rate`')
        self._data["High Fan Speed Air Flow Rate"] = value

    @property
    def high_fan_speed_fan_power(self):
        """Get high_fan_speed_fan_power

        Returns:
            float: the value of `high_fan_speed_fan_power` or None if not set
        """
        return self._data["High Fan Speed Fan Power"]

    @high_fan_speed_fan_power.setter
    def high_fan_speed_fan_power(self, value=None):
        """  Corresponds to IDD Field `High Fan Speed Fan Power`
        This is the fan motor electric input power at high speed

        Args:
            value (float or "Autosize"): value for IDD Field `High Fan Speed Fan Power`
                Units: W
                IP-Units: W
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["High Fan Speed Fan Power"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `high_fan_speed_fan_power`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `high_fan_speed_fan_power`')
        self._data["High Fan Speed Fan Power"] = value

    @property
    def low_fan_speed_air_flow_rate(self):
        """Get low_fan_speed_air_flow_rate

        Returns:
            float: the value of `low_fan_speed_air_flow_rate` or None if not set
        """
        return self._data["Low Fan Speed Air Flow Rate"]

    @low_fan_speed_air_flow_rate.setter
    def low_fan_speed_air_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Low Fan Speed Air Flow Rate`
        Air Flow Rate at Low Fan Speed must be less than Air Flow Rate at High Fan Speed

        Args:
            value (float or "Autocalculate"): value for IDD Field `Low Fan Speed Air Flow Rate`
                Units: m3/s
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autocalculate":
                    self._data["Low Fan Speed Air Flow Rate"] = "Autocalculate"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `low_fan_speed_air_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `low_fan_speed_air_flow_rate`')
        self._data["Low Fan Speed Air Flow Rate"] = value

    @property
    def low_fan_speed_air_flow_rate_sizing_factor(self):
        """Get low_fan_speed_air_flow_rate_sizing_factor

        Returns:
            float: the value of `low_fan_speed_air_flow_rate_sizing_factor` or None if not set
        """
        return self._data["Low Fan Speed Air Flow Rate Sizing Factor"]

    @low_fan_speed_air_flow_rate_sizing_factor.setter
    def low_fan_speed_air_flow_rate_sizing_factor(self, value=0.5):
        """  Corresponds to IDD Field `Low Fan Speed Air Flow Rate Sizing Factor`
        This field is only used if the previous field is set to autocalculate.

        Args:
            value (float): value for IDD Field `Low Fan Speed Air Flow Rate Sizing Factor`
                Default value: 0.5
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `low_fan_speed_air_flow_rate_sizing_factor`'.format(value))
        self._data["Low Fan Speed Air Flow Rate Sizing Factor"] = value

    @property
    def low_fan_speed_fan_power(self):
        """Get low_fan_speed_fan_power

        Returns:
            float: the value of `low_fan_speed_fan_power` or None if not set
        """
        return self._data["Low Fan Speed Fan Power"]

    @low_fan_speed_fan_power.setter
    def low_fan_speed_fan_power(self, value=None):
        """  Corresponds to IDD Field `Low Fan Speed Fan Power`
        This is the fan motor electric input power at low speed

        Args:
            value (float or "Autocalculate"): value for IDD Field `Low Fan Speed Fan Power`
                Units: W
                IP-Units: W
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autocalculate":
                    self._data["Low Fan Speed Fan Power"] = "Autocalculate"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `low_fan_speed_fan_power`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `low_fan_speed_fan_power`')
        self._data["Low Fan Speed Fan Power"] = value

    @property
    def low_fan_speed_fan_power_sizing_factor(self):
        """Get low_fan_speed_fan_power_sizing_factor

        Returns:
            float: the value of `low_fan_speed_fan_power_sizing_factor` or None if not set
        """
        return self._data["Low Fan Speed Fan Power Sizing Factor"]

    @low_fan_speed_fan_power_sizing_factor.setter
    def low_fan_speed_fan_power_sizing_factor(self, value=0.16):
        """  Corresponds to IDD Field `Low Fan Speed Fan Power Sizing Factor`
        This field is only used if the previous field is set to autocalculate.

        Args:
            value (float): value for IDD Field `Low Fan Speed Fan Power Sizing Factor`
                Default value: 0.16
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `low_fan_speed_fan_power_sizing_factor`'.format(value))
        self._data["Low Fan Speed Fan Power Sizing Factor"] = value

    @property
    def outdoor_air_inlet_node_name(self):
        """Get outdoor_air_inlet_node_name

        Returns:
            str: the value of `outdoor_air_inlet_node_name` or None if not set
        """
        return self._data["Outdoor Air Inlet Node Name"]

    @outdoor_air_inlet_node_name.setter
    def outdoor_air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Outdoor Air Inlet Node Name`

        Args:
            value (str): value for IDD Field `Outdoor Air Inlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `outdoor_air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outdoor_air_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `outdoor_air_inlet_node_name`')
        self._data["Outdoor Air Inlet Node Name"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
        return good

    @classmethod
    def _to_str(cls, value):
        """ Represents values either as string or None values as empty string

        Args:
            value: a value
        """
        if value is None:
            return ''
        else:
            return str(value)

    def export(self):
        """ Export values of data object as list of strings"""
        out = []
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class GroundHeatExchangerVertical(object):
    """ Corresponds to IDD object `GroundHeatExchanger:Vertical`
        Variable short time step vertical ground heat exchanger model based on
        Yavuztruk, C., J.D.Spitler. 1999. A Short Time Step response Factor Model for
        Vertical Ground Loop Heat Exchangers
        The Fluid Type in the associated condenser loop must be same for which the
        g-functions below are calculated.
    
    """
    internal_name = "GroundHeatExchanger:Vertical"
    field_count = 219
    required_fields = ["Name", "Inlet Node Name", "Outlet Node Name", "Number of Data Pairs of the G Function", "G-Function Ln(T/Ts) Value 1", "G-Function G Value 1"]

    def __init__(self):
        """ Init data dictionary object for IDD  `GroundHeatExchanger:Vertical`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Inlet Node Name"] = None
        self._data["Outlet Node Name"] = None
        self._data["Maximum Flow Rate"] = None
        self._data["Number of Bore Holes"] = None
        self._data["Bore Hole Length"] = None
        self._data["Bore Hole Radius"] = None
        self._data["Ground Thermal Conductivity"] = None
        self._data["Ground Thermal Heat Capacity"] = None
        self._data["Ground Temperature"] = None
        self._data["Design Flow Rate"] = None
        self._data["Grout Thermal Conductivity"] = None
        self._data["Pipe Thermal Conductivity"] = None
        self._data["Pipe Out Diameter"] = None
        self._data["U-Tube Distance"] = None
        self._data["Pipe Thickness"] = None
        self._data["Maximum Length of Simulation"] = None
        self._data["G-Function Reference Ratio"] = None
        self._data["Number of Data Pairs of the G Function"] = None
        self._data["G-Function Ln(T/Ts) Value 1"] = None
        self._data["G-Function G Value 1"] = None
        self._data["G-Function Ln(T/Ts) Value 2"] = None
        self._data["G-Function G Value 2"] = None
        self._data["G-Function Ln(T/Ts) Value 3"] = None
        self._data["G-Function G Value 3"] = None
        self._data["G-Function Ln(T/Ts) Value 4"] = None
        self._data["G-Function G Value 4"] = None
        self._data["G-Function Ln(T/Ts) Value 5"] = None
        self._data["G-Function G Value 5"] = None
        self._data["G-Function Ln(T/Ts) Value 6"] = None
        self._data["G-Function G Value 6"] = None
        self._data["G-Function Ln(T/Ts) Value 7"] = None
        self._data["G-Function G Value 7"] = None
        self._data["G-Function Ln(T/Ts) Value 8"] = None
        self._data["G-Function G Value 8"] = None
        self._data["G-Function Ln(T/Ts) Value 9"] = None
        self._data["G-Function G Value 9"] = None
        self._data["G-Function Ln(T/Ts) Value 10"] = None
        self._data["G-Function G Value 10"] = None
        self._data["G-Function Ln(T/Ts) Value 11"] = None
        self._data["G-Function G Value 11"] = None
        self._data["G-Function Ln(T/Ts) Value 12"] = None
        self._data["G-Function G Value 12"] = None
        self._data["G-Function Ln(T/Ts) Value 13"] = None
        self._data["G-Function G Value 13"] = None
        self._data["G-Function Ln(T/Ts) Value 14"] = None
        self._data["G-Function G Value 14"] = None
        self._data["G-Function Ln(T/Ts) Value 15"] = None
        self._data["G-Function G Value 15"] = None
        self._data["G-Function Ln(T/Ts) Value 16"] = None
        self._data["G-Function G Value 16"] = None
        self._data["G-Function Ln(T/Ts) Value 17"] = None
        self._data["G-Function G Value 17"] = None
        self._data["G-Function Ln(T/Ts) Value 18"] = None
        self._data["G-Function G Value 18"] = None
        self._data["G-Function Ln(T/Ts) Value 19"] = None
        self._data["G-Function G Value 19"] = None
        self._data["G-Function Ln(T/Ts) Value 20"] = None
        self._data["G-Function G Value 20"] = None
        self._data["G-Function Ln(T/Ts) Value 21"] = None
        self._data["G-Function G Value 21"] = None
        self._data["G-Function Ln(T/Ts) Value 22"] = None
        self._data["G-Function G Value 22"] = None
        self._data["G-Function Ln(T/Ts) Value 23"] = None
        self._data["G-Function G Value 23"] = None
        self._data["G-Function Ln(T/Ts) Value 24"] = None
        self._data["G-Function G Value 24"] = None
        self._data["G-Function Ln(T/Ts) Value 25"] = None
        self._data["G-Function G Value 25"] = None
        self._data["G-Function Ln(T/Ts) Value 26"] = None
        self._data["G-Function G Value 26"] = None
        self._data["G-Function Ln(T/Ts) Value 27"] = None
        self._data["G-Function G Value 27"] = None
        self._data["G-Function Ln(T/Ts) Value 28"] = None
        self._data["G-Function G Value 28"] = None
        self._data["G-Function Ln(T/Ts) Value 29"] = None
        self._data["G-Function G Value 29"] = None
        self._data["G-Function Ln(T/Ts) Value 30"] = None
        self._data["G-Function G Value 30"] = None
        self._data["G-Function Ln(T/Ts) Value 31"] = None
        self._data["G-Function G Value 31"] = None
        self._data["G-Function Ln(T/Ts) Value 32"] = None
        self._data["G-Function G Value 32"] = None
        self._data["G-Function Ln(T/Ts) Value 33"] = None
        self._data["G-Function G Value 33"] = None
        self._data["G-Function Ln(T/Ts) Value 34"] = None
        self._data["G-Function G Value 34"] = None
        self._data["G-Function Ln(T/Ts) Value 35"] = None
        self._data["G-Function G Value 35"] = None
        self._data["G-Function Ln(T/Ts) Value 36"] = None
        self._data["G-Function G Value 36"] = None
        self._data["G-Function Ln(T/Ts) Value 37"] = None
        self._data["G-Function G Value 37"] = None
        self._data["G-Function Ln(T/Ts) Value 38"] = None
        self._data["G-Function G Value 38"] = None
        self._data["G-Function Ln(T/Ts) Value 39"] = None
        self._data["G-Function G Value 39"] = None
        self._data["G-Function Ln(T/Ts) Value 40"] = None
        self._data["G-Function G Value 40"] = None
        self._data["G-Function Ln(T/Ts) Value 41"] = None
        self._data["G-Function G Value 41"] = None
        self._data["G-Function Ln(T/Ts) Value 42"] = None
        self._data["G-Function G Value 42"] = None
        self._data["G-Function Ln(T/Ts) Value 43"] = None
        self._data["G-Function G Value 43"] = None
        self._data["G-Function Ln(T/Ts) Value 44"] = None
        self._data["G-Function G Value 44"] = None
        self._data["G-Function Ln(T/Ts) Value 45"] = None
        self._data["G-Function G Value 45"] = None
        self._data["G-Function Ln(T/Ts) Value 46"] = None
        self._data["G-Function G Value 46"] = None
        self._data["G-Function Ln(T/Ts) Value 47"] = None
        self._data["G-Function G Value 47"] = None
        self._data["G-Function Ln(T/Ts) Value 48"] = None
        self._data["G-Function G Value 48"] = None
        self._data["G-Function Ln(T/Ts) Value 49"] = None
        self._data["G-Function G Value 49"] = None
        self._data["G-Function Ln(T/Ts) Value 50"] = None
        self._data["G-Function G Value 50"] = None
        self._data["G-Function Ln(T/Ts) Value 51"] = None
        self._data["G-Function G Value 51"] = None
        self._data["G-Function Ln(T/Ts) Value 52"] = None
        self._data["G-Function G Value 52"] = None
        self._data["G-Function Ln(T/Ts) Value 53"] = None
        self._data["G-Function G Value 53"] = None
        self._data["G-Function Ln(T/Ts) Value 54"] = None
        self._data["G-Function G Value 54"] = None
        self._data["G-Function Ln(T/Ts) Value 55"] = None
        self._data["G-Function G Value 55"] = None
        self._data["G-Function Ln(T/Ts) Value 56"] = None
        self._data["G-Function G Value 56"] = None
        self._data["G-Function Ln(T/Ts) Value 57"] = None
        self._data["G-Function G Value 57"] = None
        self._data["G-Function Ln(T/Ts) Value 58"] = None
        self._data["G-Function G Value 58"] = None
        self._data["G-Function Ln(T/Ts) Value 59"] = None
        self._data["G-Function G Value 59"] = None
        self._data["G-Function Ln(T/Ts) Value 60"] = None
        self._data["G-Function G Value 60"] = None
        self._data["G-Function Ln(T/Ts) Value 61"] = None
        self._data["G-Function G Value 61"] = None
        self._data["G-Function Ln(T/Ts) Value 62"] = None
        self._data["G-Function G Value 62"] = None
        self._data["G-Function Ln(T/Ts) Value 63"] = None
        self._data["G-Function G Value 63"] = None
        self._data["G-Function Ln(T/Ts) Value 64"] = None
        self._data["G-Function G Value 64"] = None
        self._data["G-Function Ln(T/Ts) Value 65"] = None
        self._data["G-Function G Value 65"] = None
        self._data["G-Function Ln(T/Ts) Value 66"] = None
        self._data["G-Function G Value 66"] = None
        self._data["G-Function Ln(T/Ts) Value 67"] = None
        self._data["G-Function G Value 67"] = None
        self._data["G-Function Ln(T/Ts) Value 68"] = None
        self._data["G-Function G Value 68"] = None
        self._data["G-Function Ln(T/Ts) Value 69"] = None
        self._data["G-Function G Value 69"] = None
        self._data["G-Function Ln(T/Ts) Value 70"] = None
        self._data["G-Function G Value 70"] = None
        self._data["G-Function Ln(T/Ts) Value 71"] = None
        self._data["G-Function G Value 71"] = None
        self._data["G-Function Ln(T/Ts) Value 72"] = None
        self._data["G-Function G Value 72"] = None
        self._data["G-Function Ln(T/Ts) Value 73"] = None
        self._data["G-Function G Value 73"] = None
        self._data["G-Function Ln(T/Ts) Value 74"] = None
        self._data["G-Function G Value 74"] = None
        self._data["G-Function Ln(T/Ts) Value 75"] = None
        self._data["G-Function G Value 75"] = None
        self._data["G-Function Ln(T/Ts) Value 76"] = None
        self._data["G-Function G Value 76"] = None
        self._data["G-Function Ln(T/Ts) Value 77"] = None
        self._data["G-Function G Value 77"] = None
        self._data["G-Function Ln(T/Ts) Value 78"] = None
        self._data["G-Function G Value 78"] = None
        self._data["G-Function Ln(T/Ts) Value 79"] = None
        self._data["G-Function G Value 79"] = None
        self._data["G-Function Ln(T/Ts) Value 80"] = None
        self._data["G-Function G Value 80"] = None
        self._data["G-Function Ln(T/Ts) Value 81"] = None
        self._data["G-Function G Value 81"] = None
        self._data["G-Function Ln(T/Ts) Value 82"] = None
        self._data["G-Function G Value 82"] = None
        self._data["G-Function Ln(T/Ts) Value 83"] = None
        self._data["G-Function G Value 83"] = None
        self._data["G-Function Ln(T/Ts) Value 84"] = None
        self._data["G-Function G Value 84"] = None
        self._data["G-Function Ln(T/Ts) Value 85"] = None
        self._data["G-Function G Value 85"] = None
        self._data["G-Function Ln(T/Ts) Value 86"] = None
        self._data["G-Function G Value 86"] = None
        self._data["G-Function Ln(T/Ts) Value 87"] = None
        self._data["G-Function G Value 87"] = None
        self._data["G-Function Ln(T/Ts) Value 88"] = None
        self._data["G-Function G Value 88"] = None
        self._data["G-Function Ln(T/Ts) Value 89"] = None
        self._data["G-Function G Value 89"] = None
        self._data["G-Function Ln(T/Ts) Value 90"] = None
        self._data["G-Function G Value 90"] = None
        self._data["G-Function Ln(T/Ts) Value 91"] = None
        self._data["G-Function G Value 91"] = None
        self._data["G-Function Ln(T/Ts) Value 92"] = None
        self._data["G-Function G Value 92"] = None
        self._data["G-Function Ln(T/Ts) Value 93"] = None
        self._data["G-Function G Value 93"] = None
        self._data["G-Function Ln(T/Ts) Value 94"] = None
        self._data["G-Function G Value 94"] = None
        self._data["G-Function Ln(T/Ts) Value 95"] = None
        self._data["G-Function G Value 95"] = None
        self._data["G-Function Ln(T/Ts) Value 96"] = None
        self._data["G-Function G Value 96"] = None
        self._data["G-Function Ln(T/Ts) Value 97"] = None
        self._data["G-Function G Value 97"] = None
        self._data["G-Function Ln(T/Ts) Value 98"] = None
        self._data["G-Function G Value 98"] = None
        self._data["G-Function Ln(T/Ts) Value 99"] = None
        self._data["G-Function G Value 99"] = None
        self._data["G-Function Ln(T/Ts) Value 100"] = None
        self._data["G-Function G Value 100"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.inlet_node_name = None
        else:
            self.inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outlet_node_name = None
        else:
            self.outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_flow_rate = None
        else:
            self.maximum_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.number_of_bore_holes = None
        else:
            self.number_of_bore_holes = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.bore_hole_length = None
        else:
            self.bore_hole_length = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.bore_hole_radius = None
        else:
            self.bore_hole_radius = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.ground_thermal_conductivity = None
        else:
            self.ground_thermal_conductivity = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.ground_thermal_heat_capacity = None
        else:
            self.ground_thermal_heat_capacity = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.ground_temperature = None
        else:
            self.ground_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_flow_rate = None
        else:
            self.design_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.grout_thermal_conductivity = None
        else:
            self.grout_thermal_conductivity = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pipe_thermal_conductivity = None
        else:
            self.pipe_thermal_conductivity = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pipe_out_diameter = None
        else:
            self.pipe_out_diameter = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.utube_distance = None
        else:
            self.utube_distance = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pipe_thickness = None
        else:
            self.pipe_thickness = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_length_of_simulation = None
        else:
            self.maximum_length_of_simulation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_reference_ratio = None
        else:
            self.gfunction_reference_ratio = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.number_of_data_pairs_of_the_g_function = None
        else:
            self.number_of_data_pairs_of_the_g_function = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_1 = None
        else:
            self.gfunction_lnt_or_ts_value_1 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_1 = None
        else:
            self.gfunction_g_value_1 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_2 = None
        else:
            self.gfunction_lnt_or_ts_value_2 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_2 = None
        else:
            self.gfunction_g_value_2 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_3 = None
        else:
            self.gfunction_lnt_or_ts_value_3 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_3 = None
        else:
            self.gfunction_g_value_3 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_4 = None
        else:
            self.gfunction_lnt_or_ts_value_4 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_4 = None
        else:
            self.gfunction_g_value_4 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_5 = None
        else:
            self.gfunction_lnt_or_ts_value_5 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_5 = None
        else:
            self.gfunction_g_value_5 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_6 = None
        else:
            self.gfunction_lnt_or_ts_value_6 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_6 = None
        else:
            self.gfunction_g_value_6 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_7 = None
        else:
            self.gfunction_lnt_or_ts_value_7 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_7 = None
        else:
            self.gfunction_g_value_7 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_8 = None
        else:
            self.gfunction_lnt_or_ts_value_8 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_8 = None
        else:
            self.gfunction_g_value_8 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_9 = None
        else:
            self.gfunction_lnt_or_ts_value_9 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_9 = None
        else:
            self.gfunction_g_value_9 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_10 = None
        else:
            self.gfunction_lnt_or_ts_value_10 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_10 = None
        else:
            self.gfunction_g_value_10 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_11 = None
        else:
            self.gfunction_lnt_or_ts_value_11 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_11 = None
        else:
            self.gfunction_g_value_11 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_12 = None
        else:
            self.gfunction_lnt_or_ts_value_12 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_12 = None
        else:
            self.gfunction_g_value_12 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_13 = None
        else:
            self.gfunction_lnt_or_ts_value_13 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_13 = None
        else:
            self.gfunction_g_value_13 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_14 = None
        else:
            self.gfunction_lnt_or_ts_value_14 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_14 = None
        else:
            self.gfunction_g_value_14 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_15 = None
        else:
            self.gfunction_lnt_or_ts_value_15 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_15 = None
        else:
            self.gfunction_g_value_15 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_16 = None
        else:
            self.gfunction_lnt_or_ts_value_16 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_16 = None
        else:
            self.gfunction_g_value_16 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_17 = None
        else:
            self.gfunction_lnt_or_ts_value_17 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_17 = None
        else:
            self.gfunction_g_value_17 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_18 = None
        else:
            self.gfunction_lnt_or_ts_value_18 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_18 = None
        else:
            self.gfunction_g_value_18 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_19 = None
        else:
            self.gfunction_lnt_or_ts_value_19 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_19 = None
        else:
            self.gfunction_g_value_19 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_20 = None
        else:
            self.gfunction_lnt_or_ts_value_20 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_20 = None
        else:
            self.gfunction_g_value_20 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_21 = None
        else:
            self.gfunction_lnt_or_ts_value_21 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_21 = None
        else:
            self.gfunction_g_value_21 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_22 = None
        else:
            self.gfunction_lnt_or_ts_value_22 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_22 = None
        else:
            self.gfunction_g_value_22 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_23 = None
        else:
            self.gfunction_lnt_or_ts_value_23 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_23 = None
        else:
            self.gfunction_g_value_23 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_24 = None
        else:
            self.gfunction_lnt_or_ts_value_24 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_24 = None
        else:
            self.gfunction_g_value_24 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_25 = None
        else:
            self.gfunction_lnt_or_ts_value_25 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_25 = None
        else:
            self.gfunction_g_value_25 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_26 = None
        else:
            self.gfunction_lnt_or_ts_value_26 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_26 = None
        else:
            self.gfunction_g_value_26 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_27 = None
        else:
            self.gfunction_lnt_or_ts_value_27 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_27 = None
        else:
            self.gfunction_g_value_27 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_28 = None
        else:
            self.gfunction_lnt_or_ts_value_28 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_28 = None
        else:
            self.gfunction_g_value_28 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_29 = None
        else:
            self.gfunction_lnt_or_ts_value_29 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_29 = None
        else:
            self.gfunction_g_value_29 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_30 = None
        else:
            self.gfunction_lnt_or_ts_value_30 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_30 = None
        else:
            self.gfunction_g_value_30 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_31 = None
        else:
            self.gfunction_lnt_or_ts_value_31 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_31 = None
        else:
            self.gfunction_g_value_31 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_32 = None
        else:
            self.gfunction_lnt_or_ts_value_32 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_32 = None
        else:
            self.gfunction_g_value_32 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_33 = None
        else:
            self.gfunction_lnt_or_ts_value_33 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_33 = None
        else:
            self.gfunction_g_value_33 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_34 = None
        else:
            self.gfunction_lnt_or_ts_value_34 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_34 = None
        else:
            self.gfunction_g_value_34 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_35 = None
        else:
            self.gfunction_lnt_or_ts_value_35 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_35 = None
        else:
            self.gfunction_g_value_35 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_36 = None
        else:
            self.gfunction_lnt_or_ts_value_36 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_36 = None
        else:
            self.gfunction_g_value_36 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_37 = None
        else:
            self.gfunction_lnt_or_ts_value_37 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_37 = None
        else:
            self.gfunction_g_value_37 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_38 = None
        else:
            self.gfunction_lnt_or_ts_value_38 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_38 = None
        else:
            self.gfunction_g_value_38 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_39 = None
        else:
            self.gfunction_lnt_or_ts_value_39 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_39 = None
        else:
            self.gfunction_g_value_39 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_40 = None
        else:
            self.gfunction_lnt_or_ts_value_40 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_40 = None
        else:
            self.gfunction_g_value_40 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_41 = None
        else:
            self.gfunction_lnt_or_ts_value_41 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_41 = None
        else:
            self.gfunction_g_value_41 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_42 = None
        else:
            self.gfunction_lnt_or_ts_value_42 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_42 = None
        else:
            self.gfunction_g_value_42 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_43 = None
        else:
            self.gfunction_lnt_or_ts_value_43 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_43 = None
        else:
            self.gfunction_g_value_43 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_44 = None
        else:
            self.gfunction_lnt_or_ts_value_44 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_44 = None
        else:
            self.gfunction_g_value_44 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_45 = None
        else:
            self.gfunction_lnt_or_ts_value_45 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_45 = None
        else:
            self.gfunction_g_value_45 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_46 = None
        else:
            self.gfunction_lnt_or_ts_value_46 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_46 = None
        else:
            self.gfunction_g_value_46 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_47 = None
        else:
            self.gfunction_lnt_or_ts_value_47 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_47 = None
        else:
            self.gfunction_g_value_47 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_48 = None
        else:
            self.gfunction_lnt_or_ts_value_48 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_48 = None
        else:
            self.gfunction_g_value_48 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_49 = None
        else:
            self.gfunction_lnt_or_ts_value_49 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_49 = None
        else:
            self.gfunction_g_value_49 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_50 = None
        else:
            self.gfunction_lnt_or_ts_value_50 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_50 = None
        else:
            self.gfunction_g_value_50 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_51 = None
        else:
            self.gfunction_lnt_or_ts_value_51 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_51 = None
        else:
            self.gfunction_g_value_51 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_52 = None
        else:
            self.gfunction_lnt_or_ts_value_52 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_52 = None
        else:
            self.gfunction_g_value_52 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_53 = None
        else:
            self.gfunction_lnt_or_ts_value_53 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_53 = None
        else:
            self.gfunction_g_value_53 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_54 = None
        else:
            self.gfunction_lnt_or_ts_value_54 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_54 = None
        else:
            self.gfunction_g_value_54 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_55 = None
        else:
            self.gfunction_lnt_or_ts_value_55 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_55 = None
        else:
            self.gfunction_g_value_55 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_56 = None
        else:
            self.gfunction_lnt_or_ts_value_56 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_56 = None
        else:
            self.gfunction_g_value_56 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_57 = None
        else:
            self.gfunction_lnt_or_ts_value_57 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_57 = None
        else:
            self.gfunction_g_value_57 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_58 = None
        else:
            self.gfunction_lnt_or_ts_value_58 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_58 = None
        else:
            self.gfunction_g_value_58 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_59 = None
        else:
            self.gfunction_lnt_or_ts_value_59 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_59 = None
        else:
            self.gfunction_g_value_59 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_60 = None
        else:
            self.gfunction_lnt_or_ts_value_60 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_60 = None
        else:
            self.gfunction_g_value_60 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_61 = None
        else:
            self.gfunction_lnt_or_ts_value_61 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_61 = None
        else:
            self.gfunction_g_value_61 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_62 = None
        else:
            self.gfunction_lnt_or_ts_value_62 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_62 = None
        else:
            self.gfunction_g_value_62 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_63 = None
        else:
            self.gfunction_lnt_or_ts_value_63 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_63 = None
        else:
            self.gfunction_g_value_63 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_64 = None
        else:
            self.gfunction_lnt_or_ts_value_64 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_64 = None
        else:
            self.gfunction_g_value_64 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_65 = None
        else:
            self.gfunction_lnt_or_ts_value_65 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_65 = None
        else:
            self.gfunction_g_value_65 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_66 = None
        else:
            self.gfunction_lnt_or_ts_value_66 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_66 = None
        else:
            self.gfunction_g_value_66 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_67 = None
        else:
            self.gfunction_lnt_or_ts_value_67 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_67 = None
        else:
            self.gfunction_g_value_67 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_68 = None
        else:
            self.gfunction_lnt_or_ts_value_68 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_68 = None
        else:
            self.gfunction_g_value_68 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_69 = None
        else:
            self.gfunction_lnt_or_ts_value_69 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_69 = None
        else:
            self.gfunction_g_value_69 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_70 = None
        else:
            self.gfunction_lnt_or_ts_value_70 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_70 = None
        else:
            self.gfunction_g_value_70 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_71 = None
        else:
            self.gfunction_lnt_or_ts_value_71 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_71 = None
        else:
            self.gfunction_g_value_71 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_72 = None
        else:
            self.gfunction_lnt_or_ts_value_72 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_72 = None
        else:
            self.gfunction_g_value_72 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_73 = None
        else:
            self.gfunction_lnt_or_ts_value_73 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_73 = None
        else:
            self.gfunction_g_value_73 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_74 = None
        else:
            self.gfunction_lnt_or_ts_value_74 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_74 = None
        else:
            self.gfunction_g_value_74 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_75 = None
        else:
            self.gfunction_lnt_or_ts_value_75 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_75 = None
        else:
            self.gfunction_g_value_75 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_76 = None
        else:
            self.gfunction_lnt_or_ts_value_76 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_76 = None
        else:
            self.gfunction_g_value_76 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_77 = None
        else:
            self.gfunction_lnt_or_ts_value_77 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_77 = None
        else:
            self.gfunction_g_value_77 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_78 = None
        else:
            self.gfunction_lnt_or_ts_value_78 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_78 = None
        else:
            self.gfunction_g_value_78 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_79 = None
        else:
            self.gfunction_lnt_or_ts_value_79 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_79 = None
        else:
            self.gfunction_g_value_79 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_80 = None
        else:
            self.gfunction_lnt_or_ts_value_80 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_80 = None
        else:
            self.gfunction_g_value_80 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_81 = None
        else:
            self.gfunction_lnt_or_ts_value_81 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_81 = None
        else:
            self.gfunction_g_value_81 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_82 = None
        else:
            self.gfunction_lnt_or_ts_value_82 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_82 = None
        else:
            self.gfunction_g_value_82 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_83 = None
        else:
            self.gfunction_lnt_or_ts_value_83 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_83 = None
        else:
            self.gfunction_g_value_83 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_84 = None
        else:
            self.gfunction_lnt_or_ts_value_84 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_84 = None
        else:
            self.gfunction_g_value_84 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_85 = None
        else:
            self.gfunction_lnt_or_ts_value_85 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_85 = None
        else:
            self.gfunction_g_value_85 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_86 = None
        else:
            self.gfunction_lnt_or_ts_value_86 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_86 = None
        else:
            self.gfunction_g_value_86 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_87 = None
        else:
            self.gfunction_lnt_or_ts_value_87 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_87 = None
        else:
            self.gfunction_g_value_87 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_88 = None
        else:
            self.gfunction_lnt_or_ts_value_88 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_88 = None
        else:
            self.gfunction_g_value_88 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_89 = None
        else:
            self.gfunction_lnt_or_ts_value_89 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_89 = None
        else:
            self.gfunction_g_value_89 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_90 = None
        else:
            self.gfunction_lnt_or_ts_value_90 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_90 = None
        else:
            self.gfunction_g_value_90 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_91 = None
        else:
            self.gfunction_lnt_or_ts_value_91 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_91 = None
        else:
            self.gfunction_g_value_91 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_92 = None
        else:
            self.gfunction_lnt_or_ts_value_92 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_92 = None
        else:
            self.gfunction_g_value_92 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_93 = None
        else:
            self.gfunction_lnt_or_ts_value_93 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_93 = None
        else:
            self.gfunction_g_value_93 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_94 = None
        else:
            self.gfunction_lnt_or_ts_value_94 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_94 = None
        else:
            self.gfunction_g_value_94 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_95 = None
        else:
            self.gfunction_lnt_or_ts_value_95 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_95 = None
        else:
            self.gfunction_g_value_95 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_96 = None
        else:
            self.gfunction_lnt_or_ts_value_96 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_96 = None
        else:
            self.gfunction_g_value_96 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_97 = None
        else:
            self.gfunction_lnt_or_ts_value_97 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_97 = None
        else:
            self.gfunction_g_value_97 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_98 = None
        else:
            self.gfunction_lnt_or_ts_value_98 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_98 = None
        else:
            self.gfunction_g_value_98 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_99 = None
        else:
            self.gfunction_lnt_or_ts_value_99 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_99 = None
        else:
            self.gfunction_g_value_99 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_100 = None
        else:
            self.gfunction_lnt_or_ts_value_100 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gfunction_g_value_100 = None
        else:
            self.gfunction_g_value_100 = vals[i]
        i += 1
        if i >= len(vals):
            return

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `Name`

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')
        self._data["Name"] = value

    @property
    def inlet_node_name(self):
        """Get inlet_node_name

        Returns:
            str: the value of `inlet_node_name` or None if not set
        """
        return self._data["Inlet Node Name"]

    @inlet_node_name.setter
    def inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Inlet Node Name`

        Args:
            value (str): value for IDD Field `Inlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `inlet_node_name`')
        self._data["Inlet Node Name"] = value

    @property
    def outlet_node_name(self):
        """Get outlet_node_name

        Returns:
            str: the value of `outlet_node_name` or None if not set
        """
        return self._data["Outlet Node Name"]

    @outlet_node_name.setter
    def outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Outlet Node Name`

        Args:
            value (str): value for IDD Field `Outlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `outlet_node_name`')
        self._data["Outlet Node Name"] = value

    @property
    def maximum_flow_rate(self):
        """Get maximum_flow_rate

        Returns:
            float: the value of `maximum_flow_rate` or None if not set
        """
        return self._data["Maximum Flow Rate"]

    @maximum_flow_rate.setter
    def maximum_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Maximum Flow Rate`

        Args:
            value (float): value for IDD Field `Maximum Flow Rate`
                Units: m3/s
                IP-Units: gal/min
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `maximum_flow_rate`')
        self._data["Maximum Flow Rate"] = value

    @property
    def number_of_bore_holes(self):
        """Get number_of_bore_holes

        Returns:
            float: the value of `number_of_bore_holes` or None if not set
        """
        return self._data["Number of Bore Holes"]

    @number_of_bore_holes.setter
    def number_of_bore_holes(self, value=None):
        """  Corresponds to IDD Field `Number of Bore Holes`

        Args:
            value (float): value for IDD Field `Number of Bore Holes`
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `number_of_bore_holes`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `number_of_bore_holes`')
        self._data["Number of Bore Holes"] = value

    @property
    def bore_hole_length(self):
        """Get bore_hole_length

        Returns:
            float: the value of `bore_hole_length` or None if not set
        """
        return self._data["Bore Hole Length"]

    @bore_hole_length.setter
    def bore_hole_length(self, value=None):
        """  Corresponds to IDD Field `Bore Hole Length`

        Args:
            value (float): value for IDD Field `Bore Hole Length`
                Units: m
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `bore_hole_length`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `bore_hole_length`')
        self._data["Bore Hole Length"] = value

    @property
    def bore_hole_radius(self):
        """Get bore_hole_radius

        Returns:
            float: the value of `bore_hole_radius` or None if not set
        """
        return self._data["Bore Hole Radius"]

    @bore_hole_radius.setter
    def bore_hole_radius(self, value=None):
        """  Corresponds to IDD Field `Bore Hole Radius`

        Args:
            value (float): value for IDD Field `Bore Hole Radius`
                Units: m
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `bore_hole_radius`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `bore_hole_radius`')
        self._data["Bore Hole Radius"] = value

    @property
    def ground_thermal_conductivity(self):
        """Get ground_thermal_conductivity

        Returns:
            float: the value of `ground_thermal_conductivity` or None if not set
        """
        return self._data["Ground Thermal Conductivity"]

    @ground_thermal_conductivity.setter
    def ground_thermal_conductivity(self, value=None):
        """  Corresponds to IDD Field `Ground Thermal Conductivity`

        Args:
            value (float): value for IDD Field `Ground Thermal Conductivity`
                Units: W/m-K
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `ground_thermal_conductivity`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `ground_thermal_conductivity`')
        self._data["Ground Thermal Conductivity"] = value

    @property
    def ground_thermal_heat_capacity(self):
        """Get ground_thermal_heat_capacity

        Returns:
            float: the value of `ground_thermal_heat_capacity` or None if not set
        """
        return self._data["Ground Thermal Heat Capacity"]

    @ground_thermal_heat_capacity.setter
    def ground_thermal_heat_capacity(self, value=None):
        """  Corresponds to IDD Field `Ground Thermal Heat Capacity`

        Args:
            value (float): value for IDD Field `Ground Thermal Heat Capacity`
                Units: J/m3-K
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `ground_thermal_heat_capacity`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `ground_thermal_heat_capacity`')
        self._data["Ground Thermal Heat Capacity"] = value

    @property
    def ground_temperature(self):
        """Get ground_temperature

        Returns:
            float: the value of `ground_temperature` or None if not set
        """
        return self._data["Ground Temperature"]

    @ground_temperature.setter
    def ground_temperature(self, value=None):
        """  Corresponds to IDD Field `Ground Temperature`

        Args:
            value (float): value for IDD Field `Ground Temperature`
                Units: C
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `ground_temperature`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `ground_temperature`')
        self._data["Ground Temperature"] = value

    @property
    def design_flow_rate(self):
        """Get design_flow_rate

        Returns:
            float: the value of `design_flow_rate` or None if not set
        """
        return self._data["Design Flow Rate"]

    @design_flow_rate.setter
    def design_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Design Flow Rate`

        Args:
            value (float): value for IDD Field `Design Flow Rate`
                Units: m3/s
                IP-Units: gal/min
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `design_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `design_flow_rate`')
        self._data["Design Flow Rate"] = value

    @property
    def grout_thermal_conductivity(self):
        """Get grout_thermal_conductivity

        Returns:
            float: the value of `grout_thermal_conductivity` or None if not set
        """
        return self._data["Grout Thermal Conductivity"]

    @grout_thermal_conductivity.setter
    def grout_thermal_conductivity(self, value=None):
        """  Corresponds to IDD Field `Grout Thermal Conductivity`

        Args:
            value (float): value for IDD Field `Grout Thermal Conductivity`
                Units: W/m-K
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `grout_thermal_conductivity`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `grout_thermal_conductivity`')
        self._data["Grout Thermal Conductivity"] = value

    @property
    def pipe_thermal_conductivity(self):
        """Get pipe_thermal_conductivity

        Returns:
            float: the value of `pipe_thermal_conductivity` or None if not set
        """
        return self._data["Pipe Thermal Conductivity"]

    @pipe_thermal_conductivity.setter
    def pipe_thermal_conductivity(self, value=None):
        """  Corresponds to IDD Field `Pipe Thermal Conductivity`

        Args:
            value (float): value for IDD Field `Pipe Thermal Conductivity`
                Units: W/m-K
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `pipe_thermal_conductivity`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `pipe_thermal_conductivity`')
        self._data["Pipe Thermal Conductivity"] = value

    @property
    def pipe_out_diameter(self):
        """Get pipe_out_diameter

        Returns:
            float: the value of `pipe_out_diameter` or None if not set
        """
        return self._data["Pipe Out Diameter"]

    @pipe_out_diameter.setter
    def pipe_out_diameter(self, value=None):
        """  Corresponds to IDD Field `Pipe Out Diameter`

        Args:
            value (float): value for IDD Field `Pipe Out Diameter`
                Units: m
                IP-Units: in
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `pipe_out_diameter`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `pipe_out_diameter`')
        self._data["Pipe Out Diameter"] = value

    @property
    def utube_distance(self):
        """Get utube_distance

        Returns:
            float: the value of `utube_distance` or None if not set
        """
        return self._data["U-Tube Distance"]

    @utube_distance.setter
    def utube_distance(self, value=None):
        """  Corresponds to IDD Field `U-Tube Distance`

        Args:
            value (float): value for IDD Field `U-Tube Distance`
                Units: m
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `utube_distance`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `utube_distance`')
        self._data["U-Tube Distance"] = value

    @property
    def pipe_thickness(self):
        """Get pipe_thickness

        Returns:
            float: the value of `pipe_thickness` or None if not set
        """
        return self._data["Pipe Thickness"]

    @pipe_thickness.setter
    def pipe_thickness(self, value=None):
        """  Corresponds to IDD Field `Pipe Thickness`

        Args:
            value (float): value for IDD Field `Pipe Thickness`
                Units: m
                IP-Units: in
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `pipe_thickness`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `pipe_thickness`')
        self._data["Pipe Thickness"] = value

    @property
    def maximum_length_of_simulation(self):
        """Get maximum_length_of_simulation

        Returns:
            float: the value of `maximum_length_of_simulation` or None if not set
        """
        return self._data["Maximum Length of Simulation"]

    @maximum_length_of_simulation.setter
    def maximum_length_of_simulation(self, value=None):
        """  Corresponds to IDD Field `Maximum Length of Simulation`

        Args:
            value (float): value for IDD Field `Maximum Length of Simulation`
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_length_of_simulation`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `maximum_length_of_simulation`')
        self._data["Maximum Length of Simulation"] = value

    @property
    def gfunction_reference_ratio(self):
        """Get gfunction_reference_ratio

        Returns:
            float: the value of `gfunction_reference_ratio` or None if not set
        """
        return self._data["G-Function Reference Ratio"]

    @gfunction_reference_ratio.setter
    def gfunction_reference_ratio(self, value=0.0005):
        """  Corresponds to IDD Field `G-Function Reference Ratio`

        Args:
            value (float): value for IDD Field `G-Function Reference Ratio`
                Units: dimensionless
                Default value: 0.0005
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_reference_ratio`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `gfunction_reference_ratio`')
        self._data["G-Function Reference Ratio"] = value

    @property
    def number_of_data_pairs_of_the_g_function(self):
        """Get number_of_data_pairs_of_the_g_function

        Returns:
            float: the value of `number_of_data_pairs_of_the_g_function` or None if not set
        """
        return self._data["Number of Data Pairs of the G Function"]

    @number_of_data_pairs_of_the_g_function.setter
    def number_of_data_pairs_of_the_g_function(self, value=None):
        """  Corresponds to IDD Field `Number of Data Pairs of the G Function`

        Args:
            value (float): value for IDD Field `Number of Data Pairs of the G Function`
                value > 0.0
                value <= 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `number_of_data_pairs_of_the_g_function`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `number_of_data_pairs_of_the_g_function`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `number_of_data_pairs_of_the_g_function`')
        self._data["Number of Data Pairs of the G Function"] = value

    @property
    def gfunction_lnt_or_ts_value_1(self):
        """Get gfunction_lnt_or_ts_value_1

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_1` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 1"]

    @gfunction_lnt_or_ts_value_1.setter
    def gfunction_lnt_or_ts_value_1(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 1`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 1`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_1`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 1"] = value

    @property
    def gfunction_g_value_1(self):
        """Get gfunction_g_value_1

        Returns:
            float: the value of `gfunction_g_value_1` or None if not set
        """
        return self._data["G-Function G Value 1"]

    @gfunction_g_value_1.setter
    def gfunction_g_value_1(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 1`

        Args:
            value (float): value for IDD Field `G-Function G Value 1`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_1`'.format(value))
        self._data["G-Function G Value 1"] = value

    @property
    def gfunction_lnt_or_ts_value_2(self):
        """Get gfunction_lnt_or_ts_value_2

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_2` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 2"]

    @gfunction_lnt_or_ts_value_2.setter
    def gfunction_lnt_or_ts_value_2(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 2`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_2`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 2"] = value

    @property
    def gfunction_g_value_2(self):
        """Get gfunction_g_value_2

        Returns:
            float: the value of `gfunction_g_value_2` or None if not set
        """
        return self._data["G-Function G Value 2"]

    @gfunction_g_value_2.setter
    def gfunction_g_value_2(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 2`

        Args:
            value (float): value for IDD Field `G-Function G Value 2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_2`'.format(value))
        self._data["G-Function G Value 2"] = value

    @property
    def gfunction_lnt_or_ts_value_3(self):
        """Get gfunction_lnt_or_ts_value_3

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_3` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 3"]

    @gfunction_lnt_or_ts_value_3.setter
    def gfunction_lnt_or_ts_value_3(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 3`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 3`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_3`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 3"] = value

    @property
    def gfunction_g_value_3(self):
        """Get gfunction_g_value_3

        Returns:
            float: the value of `gfunction_g_value_3` or None if not set
        """
        return self._data["G-Function G Value 3"]

    @gfunction_g_value_3.setter
    def gfunction_g_value_3(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 3`

        Args:
            value (float): value for IDD Field `G-Function G Value 3`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_3`'.format(value))
        self._data["G-Function G Value 3"] = value

    @property
    def gfunction_lnt_or_ts_value_4(self):
        """Get gfunction_lnt_or_ts_value_4

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_4` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 4"]

    @gfunction_lnt_or_ts_value_4.setter
    def gfunction_lnt_or_ts_value_4(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 4`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 4`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_4`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 4"] = value

    @property
    def gfunction_g_value_4(self):
        """Get gfunction_g_value_4

        Returns:
            float: the value of `gfunction_g_value_4` or None if not set
        """
        return self._data["G-Function G Value 4"]

    @gfunction_g_value_4.setter
    def gfunction_g_value_4(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 4`

        Args:
            value (float): value for IDD Field `G-Function G Value 4`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_4`'.format(value))
        self._data["G-Function G Value 4"] = value

    @property
    def gfunction_lnt_or_ts_value_5(self):
        """Get gfunction_lnt_or_ts_value_5

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_5` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 5"]

    @gfunction_lnt_or_ts_value_5.setter
    def gfunction_lnt_or_ts_value_5(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 5`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_5`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 5"] = value

    @property
    def gfunction_g_value_5(self):
        """Get gfunction_g_value_5

        Returns:
            float: the value of `gfunction_g_value_5` or None if not set
        """
        return self._data["G-Function G Value 5"]

    @gfunction_g_value_5.setter
    def gfunction_g_value_5(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 5`

        Args:
            value (float): value for IDD Field `G-Function G Value 5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_5`'.format(value))
        self._data["G-Function G Value 5"] = value

    @property
    def gfunction_lnt_or_ts_value_6(self):
        """Get gfunction_lnt_or_ts_value_6

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_6` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 6"]

    @gfunction_lnt_or_ts_value_6.setter
    def gfunction_lnt_or_ts_value_6(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 6`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 6`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_6`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 6"] = value

    @property
    def gfunction_g_value_6(self):
        """Get gfunction_g_value_6

        Returns:
            float: the value of `gfunction_g_value_6` or None if not set
        """
        return self._data["G-Function G Value 6"]

    @gfunction_g_value_6.setter
    def gfunction_g_value_6(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 6`

        Args:
            value (float): value for IDD Field `G-Function G Value 6`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_6`'.format(value))
        self._data["G-Function G Value 6"] = value

    @property
    def gfunction_lnt_or_ts_value_7(self):
        """Get gfunction_lnt_or_ts_value_7

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_7` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 7"]

    @gfunction_lnt_or_ts_value_7.setter
    def gfunction_lnt_or_ts_value_7(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 7`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 7`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_7`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 7"] = value

    @property
    def gfunction_g_value_7(self):
        """Get gfunction_g_value_7

        Returns:
            float: the value of `gfunction_g_value_7` or None if not set
        """
        return self._data["G-Function G Value 7"]

    @gfunction_g_value_7.setter
    def gfunction_g_value_7(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 7`

        Args:
            value (float): value for IDD Field `G-Function G Value 7`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_7`'.format(value))
        self._data["G-Function G Value 7"] = value

    @property
    def gfunction_lnt_or_ts_value_8(self):
        """Get gfunction_lnt_or_ts_value_8

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_8` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 8"]

    @gfunction_lnt_or_ts_value_8.setter
    def gfunction_lnt_or_ts_value_8(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 8`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 8`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_8`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 8"] = value

    @property
    def gfunction_g_value_8(self):
        """Get gfunction_g_value_8

        Returns:
            float: the value of `gfunction_g_value_8` or None if not set
        """
        return self._data["G-Function G Value 8"]

    @gfunction_g_value_8.setter
    def gfunction_g_value_8(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 8`

        Args:
            value (float): value for IDD Field `G-Function G Value 8`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_8`'.format(value))
        self._data["G-Function G Value 8"] = value

    @property
    def gfunction_lnt_or_ts_value_9(self):
        """Get gfunction_lnt_or_ts_value_9

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_9` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 9"]

    @gfunction_lnt_or_ts_value_9.setter
    def gfunction_lnt_or_ts_value_9(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 9`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 9`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_9`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 9"] = value

    @property
    def gfunction_g_value_9(self):
        """Get gfunction_g_value_9

        Returns:
            float: the value of `gfunction_g_value_9` or None if not set
        """
        return self._data["G-Function G Value 9"]

    @gfunction_g_value_9.setter
    def gfunction_g_value_9(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 9`

        Args:
            value (float): value for IDD Field `G-Function G Value 9`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_9`'.format(value))
        self._data["G-Function G Value 9"] = value

    @property
    def gfunction_lnt_or_ts_value_10(self):
        """Get gfunction_lnt_or_ts_value_10

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_10` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 10"]

    @gfunction_lnt_or_ts_value_10.setter
    def gfunction_lnt_or_ts_value_10(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 10`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 10`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_10`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 10"] = value

    @property
    def gfunction_g_value_10(self):
        """Get gfunction_g_value_10

        Returns:
            float: the value of `gfunction_g_value_10` or None if not set
        """
        return self._data["G-Function G Value 10"]

    @gfunction_g_value_10.setter
    def gfunction_g_value_10(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 10`

        Args:
            value (float): value for IDD Field `G-Function G Value 10`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_10`'.format(value))
        self._data["G-Function G Value 10"] = value

    @property
    def gfunction_lnt_or_ts_value_11(self):
        """Get gfunction_lnt_or_ts_value_11

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_11` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 11"]

    @gfunction_lnt_or_ts_value_11.setter
    def gfunction_lnt_or_ts_value_11(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 11`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 11`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_11`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 11"] = value

    @property
    def gfunction_g_value_11(self):
        """Get gfunction_g_value_11

        Returns:
            float: the value of `gfunction_g_value_11` or None if not set
        """
        return self._data["G-Function G Value 11"]

    @gfunction_g_value_11.setter
    def gfunction_g_value_11(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 11`

        Args:
            value (float): value for IDD Field `G-Function G Value 11`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_11`'.format(value))
        self._data["G-Function G Value 11"] = value

    @property
    def gfunction_lnt_or_ts_value_12(self):
        """Get gfunction_lnt_or_ts_value_12

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_12` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 12"]

    @gfunction_lnt_or_ts_value_12.setter
    def gfunction_lnt_or_ts_value_12(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 12`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 12`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_12`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 12"] = value

    @property
    def gfunction_g_value_12(self):
        """Get gfunction_g_value_12

        Returns:
            float: the value of `gfunction_g_value_12` or None if not set
        """
        return self._data["G-Function G Value 12"]

    @gfunction_g_value_12.setter
    def gfunction_g_value_12(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 12`

        Args:
            value (float): value for IDD Field `G-Function G Value 12`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_12`'.format(value))
        self._data["G-Function G Value 12"] = value

    @property
    def gfunction_lnt_or_ts_value_13(self):
        """Get gfunction_lnt_or_ts_value_13

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_13` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 13"]

    @gfunction_lnt_or_ts_value_13.setter
    def gfunction_lnt_or_ts_value_13(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 13`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 13`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_13`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 13"] = value

    @property
    def gfunction_g_value_13(self):
        """Get gfunction_g_value_13

        Returns:
            float: the value of `gfunction_g_value_13` or None if not set
        """
        return self._data["G-Function G Value 13"]

    @gfunction_g_value_13.setter
    def gfunction_g_value_13(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 13`

        Args:
            value (float): value for IDD Field `G-Function G Value 13`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_13`'.format(value))
        self._data["G-Function G Value 13"] = value

    @property
    def gfunction_lnt_or_ts_value_14(self):
        """Get gfunction_lnt_or_ts_value_14

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_14` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 14"]

    @gfunction_lnt_or_ts_value_14.setter
    def gfunction_lnt_or_ts_value_14(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 14`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 14`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_14`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 14"] = value

    @property
    def gfunction_g_value_14(self):
        """Get gfunction_g_value_14

        Returns:
            float: the value of `gfunction_g_value_14` or None if not set
        """
        return self._data["G-Function G Value 14"]

    @gfunction_g_value_14.setter
    def gfunction_g_value_14(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 14`

        Args:
            value (float): value for IDD Field `G-Function G Value 14`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_14`'.format(value))
        self._data["G-Function G Value 14"] = value

    @property
    def gfunction_lnt_or_ts_value_15(self):
        """Get gfunction_lnt_or_ts_value_15

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_15` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 15"]

    @gfunction_lnt_or_ts_value_15.setter
    def gfunction_lnt_or_ts_value_15(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 15`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 15`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_15`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 15"] = value

    @property
    def gfunction_g_value_15(self):
        """Get gfunction_g_value_15

        Returns:
            float: the value of `gfunction_g_value_15` or None if not set
        """
        return self._data["G-Function G Value 15"]

    @gfunction_g_value_15.setter
    def gfunction_g_value_15(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 15`

        Args:
            value (float): value for IDD Field `G-Function G Value 15`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_15`'.format(value))
        self._data["G-Function G Value 15"] = value

    @property
    def gfunction_lnt_or_ts_value_16(self):
        """Get gfunction_lnt_or_ts_value_16

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_16` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 16"]

    @gfunction_lnt_or_ts_value_16.setter
    def gfunction_lnt_or_ts_value_16(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 16`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 16`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_16`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 16"] = value

    @property
    def gfunction_g_value_16(self):
        """Get gfunction_g_value_16

        Returns:
            float: the value of `gfunction_g_value_16` or None if not set
        """
        return self._data["G-Function G Value 16"]

    @gfunction_g_value_16.setter
    def gfunction_g_value_16(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 16`

        Args:
            value (float): value for IDD Field `G-Function G Value 16`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_16`'.format(value))
        self._data["G-Function G Value 16"] = value

    @property
    def gfunction_lnt_or_ts_value_17(self):
        """Get gfunction_lnt_or_ts_value_17

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_17` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 17"]

    @gfunction_lnt_or_ts_value_17.setter
    def gfunction_lnt_or_ts_value_17(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 17`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 17`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_17`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 17"] = value

    @property
    def gfunction_g_value_17(self):
        """Get gfunction_g_value_17

        Returns:
            float: the value of `gfunction_g_value_17` or None if not set
        """
        return self._data["G-Function G Value 17"]

    @gfunction_g_value_17.setter
    def gfunction_g_value_17(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 17`

        Args:
            value (float): value for IDD Field `G-Function G Value 17`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_17`'.format(value))
        self._data["G-Function G Value 17"] = value

    @property
    def gfunction_lnt_or_ts_value_18(self):
        """Get gfunction_lnt_or_ts_value_18

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_18` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 18"]

    @gfunction_lnt_or_ts_value_18.setter
    def gfunction_lnt_or_ts_value_18(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 18`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 18`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_18`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 18"] = value

    @property
    def gfunction_g_value_18(self):
        """Get gfunction_g_value_18

        Returns:
            float: the value of `gfunction_g_value_18` or None if not set
        """
        return self._data["G-Function G Value 18"]

    @gfunction_g_value_18.setter
    def gfunction_g_value_18(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 18`

        Args:
            value (float): value for IDD Field `G-Function G Value 18`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_18`'.format(value))
        self._data["G-Function G Value 18"] = value

    @property
    def gfunction_lnt_or_ts_value_19(self):
        """Get gfunction_lnt_or_ts_value_19

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_19` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 19"]

    @gfunction_lnt_or_ts_value_19.setter
    def gfunction_lnt_or_ts_value_19(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 19`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 19`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_19`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 19"] = value

    @property
    def gfunction_g_value_19(self):
        """Get gfunction_g_value_19

        Returns:
            float: the value of `gfunction_g_value_19` or None if not set
        """
        return self._data["G-Function G Value 19"]

    @gfunction_g_value_19.setter
    def gfunction_g_value_19(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 19`

        Args:
            value (float): value for IDD Field `G-Function G Value 19`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_19`'.format(value))
        self._data["G-Function G Value 19"] = value

    @property
    def gfunction_lnt_or_ts_value_20(self):
        """Get gfunction_lnt_or_ts_value_20

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_20` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 20"]

    @gfunction_lnt_or_ts_value_20.setter
    def gfunction_lnt_or_ts_value_20(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 20`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 20`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_20`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 20"] = value

    @property
    def gfunction_g_value_20(self):
        """Get gfunction_g_value_20

        Returns:
            float: the value of `gfunction_g_value_20` or None if not set
        """
        return self._data["G-Function G Value 20"]

    @gfunction_g_value_20.setter
    def gfunction_g_value_20(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 20`

        Args:
            value (float): value for IDD Field `G-Function G Value 20`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_20`'.format(value))
        self._data["G-Function G Value 20"] = value

    @property
    def gfunction_lnt_or_ts_value_21(self):
        """Get gfunction_lnt_or_ts_value_21

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_21` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 21"]

    @gfunction_lnt_or_ts_value_21.setter
    def gfunction_lnt_or_ts_value_21(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 21`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 21`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_21`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 21"] = value

    @property
    def gfunction_g_value_21(self):
        """Get gfunction_g_value_21

        Returns:
            float: the value of `gfunction_g_value_21` or None if not set
        """
        return self._data["G-Function G Value 21"]

    @gfunction_g_value_21.setter
    def gfunction_g_value_21(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 21`

        Args:
            value (float): value for IDD Field `G-Function G Value 21`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_21`'.format(value))
        self._data["G-Function G Value 21"] = value

    @property
    def gfunction_lnt_or_ts_value_22(self):
        """Get gfunction_lnt_or_ts_value_22

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_22` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 22"]

    @gfunction_lnt_or_ts_value_22.setter
    def gfunction_lnt_or_ts_value_22(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 22`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 22`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_22`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 22"] = value

    @property
    def gfunction_g_value_22(self):
        """Get gfunction_g_value_22

        Returns:
            float: the value of `gfunction_g_value_22` or None if not set
        """
        return self._data["G-Function G Value 22"]

    @gfunction_g_value_22.setter
    def gfunction_g_value_22(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 22`

        Args:
            value (float): value for IDD Field `G-Function G Value 22`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_22`'.format(value))
        self._data["G-Function G Value 22"] = value

    @property
    def gfunction_lnt_or_ts_value_23(self):
        """Get gfunction_lnt_or_ts_value_23

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_23` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 23"]

    @gfunction_lnt_or_ts_value_23.setter
    def gfunction_lnt_or_ts_value_23(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 23`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 23`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_23`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 23"] = value

    @property
    def gfunction_g_value_23(self):
        """Get gfunction_g_value_23

        Returns:
            float: the value of `gfunction_g_value_23` or None if not set
        """
        return self._data["G-Function G Value 23"]

    @gfunction_g_value_23.setter
    def gfunction_g_value_23(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 23`

        Args:
            value (float): value for IDD Field `G-Function G Value 23`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_23`'.format(value))
        self._data["G-Function G Value 23"] = value

    @property
    def gfunction_lnt_or_ts_value_24(self):
        """Get gfunction_lnt_or_ts_value_24

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_24` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 24"]

    @gfunction_lnt_or_ts_value_24.setter
    def gfunction_lnt_or_ts_value_24(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 24`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 24`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_24`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 24"] = value

    @property
    def gfunction_g_value_24(self):
        """Get gfunction_g_value_24

        Returns:
            float: the value of `gfunction_g_value_24` or None if not set
        """
        return self._data["G-Function G Value 24"]

    @gfunction_g_value_24.setter
    def gfunction_g_value_24(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 24`

        Args:
            value (float): value for IDD Field `G-Function G Value 24`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_24`'.format(value))
        self._data["G-Function G Value 24"] = value

    @property
    def gfunction_lnt_or_ts_value_25(self):
        """Get gfunction_lnt_or_ts_value_25

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_25` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 25"]

    @gfunction_lnt_or_ts_value_25.setter
    def gfunction_lnt_or_ts_value_25(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 25`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 25`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_25`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 25"] = value

    @property
    def gfunction_g_value_25(self):
        """Get gfunction_g_value_25

        Returns:
            float: the value of `gfunction_g_value_25` or None if not set
        """
        return self._data["G-Function G Value 25"]

    @gfunction_g_value_25.setter
    def gfunction_g_value_25(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 25`

        Args:
            value (float): value for IDD Field `G-Function G Value 25`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_25`'.format(value))
        self._data["G-Function G Value 25"] = value

    @property
    def gfunction_lnt_or_ts_value_26(self):
        """Get gfunction_lnt_or_ts_value_26

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_26` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 26"]

    @gfunction_lnt_or_ts_value_26.setter
    def gfunction_lnt_or_ts_value_26(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 26`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 26`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_26`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 26"] = value

    @property
    def gfunction_g_value_26(self):
        """Get gfunction_g_value_26

        Returns:
            float: the value of `gfunction_g_value_26` or None if not set
        """
        return self._data["G-Function G Value 26"]

    @gfunction_g_value_26.setter
    def gfunction_g_value_26(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 26`

        Args:
            value (float): value for IDD Field `G-Function G Value 26`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_26`'.format(value))
        self._data["G-Function G Value 26"] = value

    @property
    def gfunction_lnt_or_ts_value_27(self):
        """Get gfunction_lnt_or_ts_value_27

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_27` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 27"]

    @gfunction_lnt_or_ts_value_27.setter
    def gfunction_lnt_or_ts_value_27(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 27`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 27`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_27`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 27"] = value

    @property
    def gfunction_g_value_27(self):
        """Get gfunction_g_value_27

        Returns:
            float: the value of `gfunction_g_value_27` or None if not set
        """
        return self._data["G-Function G Value 27"]

    @gfunction_g_value_27.setter
    def gfunction_g_value_27(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 27`

        Args:
            value (float): value for IDD Field `G-Function G Value 27`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_27`'.format(value))
        self._data["G-Function G Value 27"] = value

    @property
    def gfunction_lnt_or_ts_value_28(self):
        """Get gfunction_lnt_or_ts_value_28

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_28` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 28"]

    @gfunction_lnt_or_ts_value_28.setter
    def gfunction_lnt_or_ts_value_28(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 28`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 28`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_28`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 28"] = value

    @property
    def gfunction_g_value_28(self):
        """Get gfunction_g_value_28

        Returns:
            float: the value of `gfunction_g_value_28` or None if not set
        """
        return self._data["G-Function G Value 28"]

    @gfunction_g_value_28.setter
    def gfunction_g_value_28(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 28`

        Args:
            value (float): value for IDD Field `G-Function G Value 28`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_28`'.format(value))
        self._data["G-Function G Value 28"] = value

    @property
    def gfunction_lnt_or_ts_value_29(self):
        """Get gfunction_lnt_or_ts_value_29

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_29` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 29"]

    @gfunction_lnt_or_ts_value_29.setter
    def gfunction_lnt_or_ts_value_29(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 29`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 29`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_29`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 29"] = value

    @property
    def gfunction_g_value_29(self):
        """Get gfunction_g_value_29

        Returns:
            float: the value of `gfunction_g_value_29` or None if not set
        """
        return self._data["G-Function G Value 29"]

    @gfunction_g_value_29.setter
    def gfunction_g_value_29(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 29`

        Args:
            value (float): value for IDD Field `G-Function G Value 29`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_29`'.format(value))
        self._data["G-Function G Value 29"] = value

    @property
    def gfunction_lnt_or_ts_value_30(self):
        """Get gfunction_lnt_or_ts_value_30

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_30` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 30"]

    @gfunction_lnt_or_ts_value_30.setter
    def gfunction_lnt_or_ts_value_30(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 30`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 30`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_30`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 30"] = value

    @property
    def gfunction_g_value_30(self):
        """Get gfunction_g_value_30

        Returns:
            float: the value of `gfunction_g_value_30` or None if not set
        """
        return self._data["G-Function G Value 30"]

    @gfunction_g_value_30.setter
    def gfunction_g_value_30(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 30`

        Args:
            value (float): value for IDD Field `G-Function G Value 30`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_30`'.format(value))
        self._data["G-Function G Value 30"] = value

    @property
    def gfunction_lnt_or_ts_value_31(self):
        """Get gfunction_lnt_or_ts_value_31

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_31` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 31"]

    @gfunction_lnt_or_ts_value_31.setter
    def gfunction_lnt_or_ts_value_31(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 31`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 31`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_31`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 31"] = value

    @property
    def gfunction_g_value_31(self):
        """Get gfunction_g_value_31

        Returns:
            float: the value of `gfunction_g_value_31` or None if not set
        """
        return self._data["G-Function G Value 31"]

    @gfunction_g_value_31.setter
    def gfunction_g_value_31(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 31`

        Args:
            value (float): value for IDD Field `G-Function G Value 31`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_31`'.format(value))
        self._data["G-Function G Value 31"] = value

    @property
    def gfunction_lnt_or_ts_value_32(self):
        """Get gfunction_lnt_or_ts_value_32

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_32` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 32"]

    @gfunction_lnt_or_ts_value_32.setter
    def gfunction_lnt_or_ts_value_32(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 32`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 32`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_32`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 32"] = value

    @property
    def gfunction_g_value_32(self):
        """Get gfunction_g_value_32

        Returns:
            float: the value of `gfunction_g_value_32` or None if not set
        """
        return self._data["G-Function G Value 32"]

    @gfunction_g_value_32.setter
    def gfunction_g_value_32(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 32`

        Args:
            value (float): value for IDD Field `G-Function G Value 32`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_32`'.format(value))
        self._data["G-Function G Value 32"] = value

    @property
    def gfunction_lnt_or_ts_value_33(self):
        """Get gfunction_lnt_or_ts_value_33

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_33` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 33"]

    @gfunction_lnt_or_ts_value_33.setter
    def gfunction_lnt_or_ts_value_33(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 33`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 33`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_33`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 33"] = value

    @property
    def gfunction_g_value_33(self):
        """Get gfunction_g_value_33

        Returns:
            float: the value of `gfunction_g_value_33` or None if not set
        """
        return self._data["G-Function G Value 33"]

    @gfunction_g_value_33.setter
    def gfunction_g_value_33(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 33`

        Args:
            value (float): value for IDD Field `G-Function G Value 33`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_33`'.format(value))
        self._data["G-Function G Value 33"] = value

    @property
    def gfunction_lnt_or_ts_value_34(self):
        """Get gfunction_lnt_or_ts_value_34

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_34` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 34"]

    @gfunction_lnt_or_ts_value_34.setter
    def gfunction_lnt_or_ts_value_34(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 34`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 34`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_34`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 34"] = value

    @property
    def gfunction_g_value_34(self):
        """Get gfunction_g_value_34

        Returns:
            float: the value of `gfunction_g_value_34` or None if not set
        """
        return self._data["G-Function G Value 34"]

    @gfunction_g_value_34.setter
    def gfunction_g_value_34(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 34`

        Args:
            value (float): value for IDD Field `G-Function G Value 34`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_34`'.format(value))
        self._data["G-Function G Value 34"] = value

    @property
    def gfunction_lnt_or_ts_value_35(self):
        """Get gfunction_lnt_or_ts_value_35

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_35` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 35"]

    @gfunction_lnt_or_ts_value_35.setter
    def gfunction_lnt_or_ts_value_35(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 35`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 35`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_35`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 35"] = value

    @property
    def gfunction_g_value_35(self):
        """Get gfunction_g_value_35

        Returns:
            float: the value of `gfunction_g_value_35` or None if not set
        """
        return self._data["G-Function G Value 35"]

    @gfunction_g_value_35.setter
    def gfunction_g_value_35(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 35`

        Args:
            value (float): value for IDD Field `G-Function G Value 35`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_35`'.format(value))
        self._data["G-Function G Value 35"] = value

    @property
    def gfunction_lnt_or_ts_value_36(self):
        """Get gfunction_lnt_or_ts_value_36

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_36` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 36"]

    @gfunction_lnt_or_ts_value_36.setter
    def gfunction_lnt_or_ts_value_36(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 36`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 36`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_36`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 36"] = value

    @property
    def gfunction_g_value_36(self):
        """Get gfunction_g_value_36

        Returns:
            float: the value of `gfunction_g_value_36` or None if not set
        """
        return self._data["G-Function G Value 36"]

    @gfunction_g_value_36.setter
    def gfunction_g_value_36(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 36`

        Args:
            value (float): value for IDD Field `G-Function G Value 36`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_36`'.format(value))
        self._data["G-Function G Value 36"] = value

    @property
    def gfunction_lnt_or_ts_value_37(self):
        """Get gfunction_lnt_or_ts_value_37

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_37` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 37"]

    @gfunction_lnt_or_ts_value_37.setter
    def gfunction_lnt_or_ts_value_37(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 37`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 37`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_37`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 37"] = value

    @property
    def gfunction_g_value_37(self):
        """Get gfunction_g_value_37

        Returns:
            float: the value of `gfunction_g_value_37` or None if not set
        """
        return self._data["G-Function G Value 37"]

    @gfunction_g_value_37.setter
    def gfunction_g_value_37(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 37`

        Args:
            value (float): value for IDD Field `G-Function G Value 37`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_37`'.format(value))
        self._data["G-Function G Value 37"] = value

    @property
    def gfunction_lnt_or_ts_value_38(self):
        """Get gfunction_lnt_or_ts_value_38

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_38` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 38"]

    @gfunction_lnt_or_ts_value_38.setter
    def gfunction_lnt_or_ts_value_38(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 38`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 38`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_38`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 38"] = value

    @property
    def gfunction_g_value_38(self):
        """Get gfunction_g_value_38

        Returns:
            float: the value of `gfunction_g_value_38` or None if not set
        """
        return self._data["G-Function G Value 38"]

    @gfunction_g_value_38.setter
    def gfunction_g_value_38(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 38`

        Args:
            value (float): value for IDD Field `G-Function G Value 38`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_38`'.format(value))
        self._data["G-Function G Value 38"] = value

    @property
    def gfunction_lnt_or_ts_value_39(self):
        """Get gfunction_lnt_or_ts_value_39

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_39` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 39"]

    @gfunction_lnt_or_ts_value_39.setter
    def gfunction_lnt_or_ts_value_39(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 39`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 39`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_39`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 39"] = value

    @property
    def gfunction_g_value_39(self):
        """Get gfunction_g_value_39

        Returns:
            float: the value of `gfunction_g_value_39` or None if not set
        """
        return self._data["G-Function G Value 39"]

    @gfunction_g_value_39.setter
    def gfunction_g_value_39(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 39`

        Args:
            value (float): value for IDD Field `G-Function G Value 39`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_39`'.format(value))
        self._data["G-Function G Value 39"] = value

    @property
    def gfunction_lnt_or_ts_value_40(self):
        """Get gfunction_lnt_or_ts_value_40

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_40` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 40"]

    @gfunction_lnt_or_ts_value_40.setter
    def gfunction_lnt_or_ts_value_40(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 40`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 40`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_40`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 40"] = value

    @property
    def gfunction_g_value_40(self):
        """Get gfunction_g_value_40

        Returns:
            float: the value of `gfunction_g_value_40` or None if not set
        """
        return self._data["G-Function G Value 40"]

    @gfunction_g_value_40.setter
    def gfunction_g_value_40(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 40`

        Args:
            value (float): value for IDD Field `G-Function G Value 40`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_40`'.format(value))
        self._data["G-Function G Value 40"] = value

    @property
    def gfunction_lnt_or_ts_value_41(self):
        """Get gfunction_lnt_or_ts_value_41

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_41` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 41"]

    @gfunction_lnt_or_ts_value_41.setter
    def gfunction_lnt_or_ts_value_41(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 41`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 41`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_41`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 41"] = value

    @property
    def gfunction_g_value_41(self):
        """Get gfunction_g_value_41

        Returns:
            float: the value of `gfunction_g_value_41` or None if not set
        """
        return self._data["G-Function G Value 41"]

    @gfunction_g_value_41.setter
    def gfunction_g_value_41(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 41`

        Args:
            value (float): value for IDD Field `G-Function G Value 41`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_41`'.format(value))
        self._data["G-Function G Value 41"] = value

    @property
    def gfunction_lnt_or_ts_value_42(self):
        """Get gfunction_lnt_or_ts_value_42

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_42` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 42"]

    @gfunction_lnt_or_ts_value_42.setter
    def gfunction_lnt_or_ts_value_42(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 42`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 42`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_42`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 42"] = value

    @property
    def gfunction_g_value_42(self):
        """Get gfunction_g_value_42

        Returns:
            float: the value of `gfunction_g_value_42` or None if not set
        """
        return self._data["G-Function G Value 42"]

    @gfunction_g_value_42.setter
    def gfunction_g_value_42(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 42`

        Args:
            value (float): value for IDD Field `G-Function G Value 42`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_42`'.format(value))
        self._data["G-Function G Value 42"] = value

    @property
    def gfunction_lnt_or_ts_value_43(self):
        """Get gfunction_lnt_or_ts_value_43

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_43` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 43"]

    @gfunction_lnt_or_ts_value_43.setter
    def gfunction_lnt_or_ts_value_43(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 43`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 43`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_43`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 43"] = value

    @property
    def gfunction_g_value_43(self):
        """Get gfunction_g_value_43

        Returns:
            float: the value of `gfunction_g_value_43` or None if not set
        """
        return self._data["G-Function G Value 43"]

    @gfunction_g_value_43.setter
    def gfunction_g_value_43(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 43`

        Args:
            value (float): value for IDD Field `G-Function G Value 43`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_43`'.format(value))
        self._data["G-Function G Value 43"] = value

    @property
    def gfunction_lnt_or_ts_value_44(self):
        """Get gfunction_lnt_or_ts_value_44

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_44` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 44"]

    @gfunction_lnt_or_ts_value_44.setter
    def gfunction_lnt_or_ts_value_44(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 44`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 44`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_44`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 44"] = value

    @property
    def gfunction_g_value_44(self):
        """Get gfunction_g_value_44

        Returns:
            float: the value of `gfunction_g_value_44` or None if not set
        """
        return self._data["G-Function G Value 44"]

    @gfunction_g_value_44.setter
    def gfunction_g_value_44(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 44`

        Args:
            value (float): value for IDD Field `G-Function G Value 44`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_44`'.format(value))
        self._data["G-Function G Value 44"] = value

    @property
    def gfunction_lnt_or_ts_value_45(self):
        """Get gfunction_lnt_or_ts_value_45

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_45` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 45"]

    @gfunction_lnt_or_ts_value_45.setter
    def gfunction_lnt_or_ts_value_45(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 45`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 45`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_45`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 45"] = value

    @property
    def gfunction_g_value_45(self):
        """Get gfunction_g_value_45

        Returns:
            float: the value of `gfunction_g_value_45` or None if not set
        """
        return self._data["G-Function G Value 45"]

    @gfunction_g_value_45.setter
    def gfunction_g_value_45(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 45`

        Args:
            value (float): value for IDD Field `G-Function G Value 45`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_45`'.format(value))
        self._data["G-Function G Value 45"] = value

    @property
    def gfunction_lnt_or_ts_value_46(self):
        """Get gfunction_lnt_or_ts_value_46

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_46` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 46"]

    @gfunction_lnt_or_ts_value_46.setter
    def gfunction_lnt_or_ts_value_46(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 46`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 46`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_46`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 46"] = value

    @property
    def gfunction_g_value_46(self):
        """Get gfunction_g_value_46

        Returns:
            float: the value of `gfunction_g_value_46` or None if not set
        """
        return self._data["G-Function G Value 46"]

    @gfunction_g_value_46.setter
    def gfunction_g_value_46(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 46`

        Args:
            value (float): value for IDD Field `G-Function G Value 46`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_46`'.format(value))
        self._data["G-Function G Value 46"] = value

    @property
    def gfunction_lnt_or_ts_value_47(self):
        """Get gfunction_lnt_or_ts_value_47

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_47` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 47"]

    @gfunction_lnt_or_ts_value_47.setter
    def gfunction_lnt_or_ts_value_47(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 47`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 47`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_47`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 47"] = value

    @property
    def gfunction_g_value_47(self):
        """Get gfunction_g_value_47

        Returns:
            float: the value of `gfunction_g_value_47` or None if not set
        """
        return self._data["G-Function G Value 47"]

    @gfunction_g_value_47.setter
    def gfunction_g_value_47(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 47`

        Args:
            value (float): value for IDD Field `G-Function G Value 47`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_47`'.format(value))
        self._data["G-Function G Value 47"] = value

    @property
    def gfunction_lnt_or_ts_value_48(self):
        """Get gfunction_lnt_or_ts_value_48

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_48` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 48"]

    @gfunction_lnt_or_ts_value_48.setter
    def gfunction_lnt_or_ts_value_48(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 48`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 48`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_48`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 48"] = value

    @property
    def gfunction_g_value_48(self):
        """Get gfunction_g_value_48

        Returns:
            float: the value of `gfunction_g_value_48` or None if not set
        """
        return self._data["G-Function G Value 48"]

    @gfunction_g_value_48.setter
    def gfunction_g_value_48(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 48`

        Args:
            value (float): value for IDD Field `G-Function G Value 48`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_48`'.format(value))
        self._data["G-Function G Value 48"] = value

    @property
    def gfunction_lnt_or_ts_value_49(self):
        """Get gfunction_lnt_or_ts_value_49

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_49` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 49"]

    @gfunction_lnt_or_ts_value_49.setter
    def gfunction_lnt_or_ts_value_49(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 49`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 49`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_49`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 49"] = value

    @property
    def gfunction_g_value_49(self):
        """Get gfunction_g_value_49

        Returns:
            float: the value of `gfunction_g_value_49` or None if not set
        """
        return self._data["G-Function G Value 49"]

    @gfunction_g_value_49.setter
    def gfunction_g_value_49(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 49`

        Args:
            value (float): value for IDD Field `G-Function G Value 49`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_49`'.format(value))
        self._data["G-Function G Value 49"] = value

    @property
    def gfunction_lnt_or_ts_value_50(self):
        """Get gfunction_lnt_or_ts_value_50

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_50` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 50"]

    @gfunction_lnt_or_ts_value_50.setter
    def gfunction_lnt_or_ts_value_50(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 50`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 50`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_50`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 50"] = value

    @property
    def gfunction_g_value_50(self):
        """Get gfunction_g_value_50

        Returns:
            float: the value of `gfunction_g_value_50` or None if not set
        """
        return self._data["G-Function G Value 50"]

    @gfunction_g_value_50.setter
    def gfunction_g_value_50(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 50`

        Args:
            value (float): value for IDD Field `G-Function G Value 50`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_50`'.format(value))
        self._data["G-Function G Value 50"] = value

    @property
    def gfunction_lnt_or_ts_value_51(self):
        """Get gfunction_lnt_or_ts_value_51

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_51` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 51"]

    @gfunction_lnt_or_ts_value_51.setter
    def gfunction_lnt_or_ts_value_51(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 51`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 51`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_51`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 51"] = value

    @property
    def gfunction_g_value_51(self):
        """Get gfunction_g_value_51

        Returns:
            float: the value of `gfunction_g_value_51` or None if not set
        """
        return self._data["G-Function G Value 51"]

    @gfunction_g_value_51.setter
    def gfunction_g_value_51(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 51`

        Args:
            value (float): value for IDD Field `G-Function G Value 51`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_51`'.format(value))
        self._data["G-Function G Value 51"] = value

    @property
    def gfunction_lnt_or_ts_value_52(self):
        """Get gfunction_lnt_or_ts_value_52

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_52` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 52"]

    @gfunction_lnt_or_ts_value_52.setter
    def gfunction_lnt_or_ts_value_52(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 52`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 52`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_52`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 52"] = value

    @property
    def gfunction_g_value_52(self):
        """Get gfunction_g_value_52

        Returns:
            float: the value of `gfunction_g_value_52` or None if not set
        """
        return self._data["G-Function G Value 52"]

    @gfunction_g_value_52.setter
    def gfunction_g_value_52(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 52`

        Args:
            value (float): value for IDD Field `G-Function G Value 52`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_52`'.format(value))
        self._data["G-Function G Value 52"] = value

    @property
    def gfunction_lnt_or_ts_value_53(self):
        """Get gfunction_lnt_or_ts_value_53

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_53` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 53"]

    @gfunction_lnt_or_ts_value_53.setter
    def gfunction_lnt_or_ts_value_53(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 53`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 53`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_53`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 53"] = value

    @property
    def gfunction_g_value_53(self):
        """Get gfunction_g_value_53

        Returns:
            float: the value of `gfunction_g_value_53` or None if not set
        """
        return self._data["G-Function G Value 53"]

    @gfunction_g_value_53.setter
    def gfunction_g_value_53(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 53`

        Args:
            value (float): value for IDD Field `G-Function G Value 53`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_53`'.format(value))
        self._data["G-Function G Value 53"] = value

    @property
    def gfunction_lnt_or_ts_value_54(self):
        """Get gfunction_lnt_or_ts_value_54

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_54` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 54"]

    @gfunction_lnt_or_ts_value_54.setter
    def gfunction_lnt_or_ts_value_54(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 54`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 54`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_54`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 54"] = value

    @property
    def gfunction_g_value_54(self):
        """Get gfunction_g_value_54

        Returns:
            float: the value of `gfunction_g_value_54` or None if not set
        """
        return self._data["G-Function G Value 54"]

    @gfunction_g_value_54.setter
    def gfunction_g_value_54(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 54`

        Args:
            value (float): value for IDD Field `G-Function G Value 54`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_54`'.format(value))
        self._data["G-Function G Value 54"] = value

    @property
    def gfunction_lnt_or_ts_value_55(self):
        """Get gfunction_lnt_or_ts_value_55

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_55` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 55"]

    @gfunction_lnt_or_ts_value_55.setter
    def gfunction_lnt_or_ts_value_55(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 55`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 55`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_55`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 55"] = value

    @property
    def gfunction_g_value_55(self):
        """Get gfunction_g_value_55

        Returns:
            float: the value of `gfunction_g_value_55` or None if not set
        """
        return self._data["G-Function G Value 55"]

    @gfunction_g_value_55.setter
    def gfunction_g_value_55(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 55`

        Args:
            value (float): value for IDD Field `G-Function G Value 55`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_55`'.format(value))
        self._data["G-Function G Value 55"] = value

    @property
    def gfunction_lnt_or_ts_value_56(self):
        """Get gfunction_lnt_or_ts_value_56

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_56` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 56"]

    @gfunction_lnt_or_ts_value_56.setter
    def gfunction_lnt_or_ts_value_56(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 56`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 56`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_56`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 56"] = value

    @property
    def gfunction_g_value_56(self):
        """Get gfunction_g_value_56

        Returns:
            float: the value of `gfunction_g_value_56` or None if not set
        """
        return self._data["G-Function G Value 56"]

    @gfunction_g_value_56.setter
    def gfunction_g_value_56(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 56`

        Args:
            value (float): value for IDD Field `G-Function G Value 56`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_56`'.format(value))
        self._data["G-Function G Value 56"] = value

    @property
    def gfunction_lnt_or_ts_value_57(self):
        """Get gfunction_lnt_or_ts_value_57

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_57` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 57"]

    @gfunction_lnt_or_ts_value_57.setter
    def gfunction_lnt_or_ts_value_57(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 57`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 57`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_57`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 57"] = value

    @property
    def gfunction_g_value_57(self):
        """Get gfunction_g_value_57

        Returns:
            float: the value of `gfunction_g_value_57` or None if not set
        """
        return self._data["G-Function G Value 57"]

    @gfunction_g_value_57.setter
    def gfunction_g_value_57(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 57`

        Args:
            value (float): value for IDD Field `G-Function G Value 57`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_57`'.format(value))
        self._data["G-Function G Value 57"] = value

    @property
    def gfunction_lnt_or_ts_value_58(self):
        """Get gfunction_lnt_or_ts_value_58

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_58` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 58"]

    @gfunction_lnt_or_ts_value_58.setter
    def gfunction_lnt_or_ts_value_58(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 58`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 58`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_58`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 58"] = value

    @property
    def gfunction_g_value_58(self):
        """Get gfunction_g_value_58

        Returns:
            float: the value of `gfunction_g_value_58` or None if not set
        """
        return self._data["G-Function G Value 58"]

    @gfunction_g_value_58.setter
    def gfunction_g_value_58(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 58`

        Args:
            value (float): value for IDD Field `G-Function G Value 58`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_58`'.format(value))
        self._data["G-Function G Value 58"] = value

    @property
    def gfunction_lnt_or_ts_value_59(self):
        """Get gfunction_lnt_or_ts_value_59

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_59` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 59"]

    @gfunction_lnt_or_ts_value_59.setter
    def gfunction_lnt_or_ts_value_59(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 59`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 59`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_59`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 59"] = value

    @property
    def gfunction_g_value_59(self):
        """Get gfunction_g_value_59

        Returns:
            float: the value of `gfunction_g_value_59` or None if not set
        """
        return self._data["G-Function G Value 59"]

    @gfunction_g_value_59.setter
    def gfunction_g_value_59(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 59`

        Args:
            value (float): value for IDD Field `G-Function G Value 59`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_59`'.format(value))
        self._data["G-Function G Value 59"] = value

    @property
    def gfunction_lnt_or_ts_value_60(self):
        """Get gfunction_lnt_or_ts_value_60

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_60` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 60"]

    @gfunction_lnt_or_ts_value_60.setter
    def gfunction_lnt_or_ts_value_60(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 60`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 60`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_60`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 60"] = value

    @property
    def gfunction_g_value_60(self):
        """Get gfunction_g_value_60

        Returns:
            float: the value of `gfunction_g_value_60` or None if not set
        """
        return self._data["G-Function G Value 60"]

    @gfunction_g_value_60.setter
    def gfunction_g_value_60(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 60`

        Args:
            value (float): value for IDD Field `G-Function G Value 60`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_60`'.format(value))
        self._data["G-Function G Value 60"] = value

    @property
    def gfunction_lnt_or_ts_value_61(self):
        """Get gfunction_lnt_or_ts_value_61

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_61` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 61"]

    @gfunction_lnt_or_ts_value_61.setter
    def gfunction_lnt_or_ts_value_61(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 61`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 61`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_61`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 61"] = value

    @property
    def gfunction_g_value_61(self):
        """Get gfunction_g_value_61

        Returns:
            float: the value of `gfunction_g_value_61` or None if not set
        """
        return self._data["G-Function G Value 61"]

    @gfunction_g_value_61.setter
    def gfunction_g_value_61(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 61`

        Args:
            value (float): value for IDD Field `G-Function G Value 61`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_61`'.format(value))
        self._data["G-Function G Value 61"] = value

    @property
    def gfunction_lnt_or_ts_value_62(self):
        """Get gfunction_lnt_or_ts_value_62

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_62` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 62"]

    @gfunction_lnt_or_ts_value_62.setter
    def gfunction_lnt_or_ts_value_62(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 62`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 62`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_62`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 62"] = value

    @property
    def gfunction_g_value_62(self):
        """Get gfunction_g_value_62

        Returns:
            float: the value of `gfunction_g_value_62` or None if not set
        """
        return self._data["G-Function G Value 62"]

    @gfunction_g_value_62.setter
    def gfunction_g_value_62(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 62`

        Args:
            value (float): value for IDD Field `G-Function G Value 62`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_62`'.format(value))
        self._data["G-Function G Value 62"] = value

    @property
    def gfunction_lnt_or_ts_value_63(self):
        """Get gfunction_lnt_or_ts_value_63

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_63` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 63"]

    @gfunction_lnt_or_ts_value_63.setter
    def gfunction_lnt_or_ts_value_63(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 63`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 63`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_63`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 63"] = value

    @property
    def gfunction_g_value_63(self):
        """Get gfunction_g_value_63

        Returns:
            float: the value of `gfunction_g_value_63` or None if not set
        """
        return self._data["G-Function G Value 63"]

    @gfunction_g_value_63.setter
    def gfunction_g_value_63(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 63`

        Args:
            value (float): value for IDD Field `G-Function G Value 63`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_63`'.format(value))
        self._data["G-Function G Value 63"] = value

    @property
    def gfunction_lnt_or_ts_value_64(self):
        """Get gfunction_lnt_or_ts_value_64

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_64` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 64"]

    @gfunction_lnt_or_ts_value_64.setter
    def gfunction_lnt_or_ts_value_64(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 64`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 64`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_64`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 64"] = value

    @property
    def gfunction_g_value_64(self):
        """Get gfunction_g_value_64

        Returns:
            float: the value of `gfunction_g_value_64` or None if not set
        """
        return self._data["G-Function G Value 64"]

    @gfunction_g_value_64.setter
    def gfunction_g_value_64(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 64`

        Args:
            value (float): value for IDD Field `G-Function G Value 64`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_64`'.format(value))
        self._data["G-Function G Value 64"] = value

    @property
    def gfunction_lnt_or_ts_value_65(self):
        """Get gfunction_lnt_or_ts_value_65

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_65` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 65"]

    @gfunction_lnt_or_ts_value_65.setter
    def gfunction_lnt_or_ts_value_65(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 65`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 65`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_65`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 65"] = value

    @property
    def gfunction_g_value_65(self):
        """Get gfunction_g_value_65

        Returns:
            float: the value of `gfunction_g_value_65` or None if not set
        """
        return self._data["G-Function G Value 65"]

    @gfunction_g_value_65.setter
    def gfunction_g_value_65(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 65`

        Args:
            value (float): value for IDD Field `G-Function G Value 65`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_65`'.format(value))
        self._data["G-Function G Value 65"] = value

    @property
    def gfunction_lnt_or_ts_value_66(self):
        """Get gfunction_lnt_or_ts_value_66

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_66` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 66"]

    @gfunction_lnt_or_ts_value_66.setter
    def gfunction_lnt_or_ts_value_66(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 66`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 66`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_66`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 66"] = value

    @property
    def gfunction_g_value_66(self):
        """Get gfunction_g_value_66

        Returns:
            float: the value of `gfunction_g_value_66` or None if not set
        """
        return self._data["G-Function G Value 66"]

    @gfunction_g_value_66.setter
    def gfunction_g_value_66(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 66`

        Args:
            value (float): value for IDD Field `G-Function G Value 66`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_66`'.format(value))
        self._data["G-Function G Value 66"] = value

    @property
    def gfunction_lnt_or_ts_value_67(self):
        """Get gfunction_lnt_or_ts_value_67

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_67` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 67"]

    @gfunction_lnt_or_ts_value_67.setter
    def gfunction_lnt_or_ts_value_67(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 67`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 67`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_67`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 67"] = value

    @property
    def gfunction_g_value_67(self):
        """Get gfunction_g_value_67

        Returns:
            float: the value of `gfunction_g_value_67` or None if not set
        """
        return self._data["G-Function G Value 67"]

    @gfunction_g_value_67.setter
    def gfunction_g_value_67(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 67`

        Args:
            value (float): value for IDD Field `G-Function G Value 67`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_67`'.format(value))
        self._data["G-Function G Value 67"] = value

    @property
    def gfunction_lnt_or_ts_value_68(self):
        """Get gfunction_lnt_or_ts_value_68

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_68` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 68"]

    @gfunction_lnt_or_ts_value_68.setter
    def gfunction_lnt_or_ts_value_68(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 68`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 68`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_68`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 68"] = value

    @property
    def gfunction_g_value_68(self):
        """Get gfunction_g_value_68

        Returns:
            float: the value of `gfunction_g_value_68` or None if not set
        """
        return self._data["G-Function G Value 68"]

    @gfunction_g_value_68.setter
    def gfunction_g_value_68(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 68`

        Args:
            value (float): value for IDD Field `G-Function G Value 68`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_68`'.format(value))
        self._data["G-Function G Value 68"] = value

    @property
    def gfunction_lnt_or_ts_value_69(self):
        """Get gfunction_lnt_or_ts_value_69

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_69` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 69"]

    @gfunction_lnt_or_ts_value_69.setter
    def gfunction_lnt_or_ts_value_69(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 69`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 69`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_69`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 69"] = value

    @property
    def gfunction_g_value_69(self):
        """Get gfunction_g_value_69

        Returns:
            float: the value of `gfunction_g_value_69` or None if not set
        """
        return self._data["G-Function G Value 69"]

    @gfunction_g_value_69.setter
    def gfunction_g_value_69(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 69`

        Args:
            value (float): value for IDD Field `G-Function G Value 69`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_69`'.format(value))
        self._data["G-Function G Value 69"] = value

    @property
    def gfunction_lnt_or_ts_value_70(self):
        """Get gfunction_lnt_or_ts_value_70

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_70` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 70"]

    @gfunction_lnt_or_ts_value_70.setter
    def gfunction_lnt_or_ts_value_70(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 70`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 70`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_70`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 70"] = value

    @property
    def gfunction_g_value_70(self):
        """Get gfunction_g_value_70

        Returns:
            float: the value of `gfunction_g_value_70` or None if not set
        """
        return self._data["G-Function G Value 70"]

    @gfunction_g_value_70.setter
    def gfunction_g_value_70(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 70`

        Args:
            value (float): value for IDD Field `G-Function G Value 70`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_70`'.format(value))
        self._data["G-Function G Value 70"] = value

    @property
    def gfunction_lnt_or_ts_value_71(self):
        """Get gfunction_lnt_or_ts_value_71

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_71` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 71"]

    @gfunction_lnt_or_ts_value_71.setter
    def gfunction_lnt_or_ts_value_71(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 71`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 71`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_71`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 71"] = value

    @property
    def gfunction_g_value_71(self):
        """Get gfunction_g_value_71

        Returns:
            float: the value of `gfunction_g_value_71` or None if not set
        """
        return self._data["G-Function G Value 71"]

    @gfunction_g_value_71.setter
    def gfunction_g_value_71(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 71`

        Args:
            value (float): value for IDD Field `G-Function G Value 71`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_71`'.format(value))
        self._data["G-Function G Value 71"] = value

    @property
    def gfunction_lnt_or_ts_value_72(self):
        """Get gfunction_lnt_or_ts_value_72

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_72` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 72"]

    @gfunction_lnt_or_ts_value_72.setter
    def gfunction_lnt_or_ts_value_72(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 72`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 72`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_72`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 72"] = value

    @property
    def gfunction_g_value_72(self):
        """Get gfunction_g_value_72

        Returns:
            float: the value of `gfunction_g_value_72` or None if not set
        """
        return self._data["G-Function G Value 72"]

    @gfunction_g_value_72.setter
    def gfunction_g_value_72(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 72`

        Args:
            value (float): value for IDD Field `G-Function G Value 72`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_72`'.format(value))
        self._data["G-Function G Value 72"] = value

    @property
    def gfunction_lnt_or_ts_value_73(self):
        """Get gfunction_lnt_or_ts_value_73

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_73` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 73"]

    @gfunction_lnt_or_ts_value_73.setter
    def gfunction_lnt_or_ts_value_73(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 73`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 73`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_73`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 73"] = value

    @property
    def gfunction_g_value_73(self):
        """Get gfunction_g_value_73

        Returns:
            float: the value of `gfunction_g_value_73` or None if not set
        """
        return self._data["G-Function G Value 73"]

    @gfunction_g_value_73.setter
    def gfunction_g_value_73(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 73`

        Args:
            value (float): value for IDD Field `G-Function G Value 73`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_73`'.format(value))
        self._data["G-Function G Value 73"] = value

    @property
    def gfunction_lnt_or_ts_value_74(self):
        """Get gfunction_lnt_or_ts_value_74

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_74` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 74"]

    @gfunction_lnt_or_ts_value_74.setter
    def gfunction_lnt_or_ts_value_74(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 74`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 74`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_74`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 74"] = value

    @property
    def gfunction_g_value_74(self):
        """Get gfunction_g_value_74

        Returns:
            float: the value of `gfunction_g_value_74` or None if not set
        """
        return self._data["G-Function G Value 74"]

    @gfunction_g_value_74.setter
    def gfunction_g_value_74(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 74`

        Args:
            value (float): value for IDD Field `G-Function G Value 74`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_74`'.format(value))
        self._data["G-Function G Value 74"] = value

    @property
    def gfunction_lnt_or_ts_value_75(self):
        """Get gfunction_lnt_or_ts_value_75

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_75` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 75"]

    @gfunction_lnt_or_ts_value_75.setter
    def gfunction_lnt_or_ts_value_75(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 75`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 75`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_75`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 75"] = value

    @property
    def gfunction_g_value_75(self):
        """Get gfunction_g_value_75

        Returns:
            float: the value of `gfunction_g_value_75` or None if not set
        """
        return self._data["G-Function G Value 75"]

    @gfunction_g_value_75.setter
    def gfunction_g_value_75(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 75`

        Args:
            value (float): value for IDD Field `G-Function G Value 75`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_75`'.format(value))
        self._data["G-Function G Value 75"] = value

    @property
    def gfunction_lnt_or_ts_value_76(self):
        """Get gfunction_lnt_or_ts_value_76

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_76` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 76"]

    @gfunction_lnt_or_ts_value_76.setter
    def gfunction_lnt_or_ts_value_76(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 76`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 76`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_76`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 76"] = value

    @property
    def gfunction_g_value_76(self):
        """Get gfunction_g_value_76

        Returns:
            float: the value of `gfunction_g_value_76` or None if not set
        """
        return self._data["G-Function G Value 76"]

    @gfunction_g_value_76.setter
    def gfunction_g_value_76(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 76`

        Args:
            value (float): value for IDD Field `G-Function G Value 76`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_76`'.format(value))
        self._data["G-Function G Value 76"] = value

    @property
    def gfunction_lnt_or_ts_value_77(self):
        """Get gfunction_lnt_or_ts_value_77

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_77` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 77"]

    @gfunction_lnt_or_ts_value_77.setter
    def gfunction_lnt_or_ts_value_77(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 77`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 77`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_77`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 77"] = value

    @property
    def gfunction_g_value_77(self):
        """Get gfunction_g_value_77

        Returns:
            float: the value of `gfunction_g_value_77` or None if not set
        """
        return self._data["G-Function G Value 77"]

    @gfunction_g_value_77.setter
    def gfunction_g_value_77(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 77`

        Args:
            value (float): value for IDD Field `G-Function G Value 77`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_77`'.format(value))
        self._data["G-Function G Value 77"] = value

    @property
    def gfunction_lnt_or_ts_value_78(self):
        """Get gfunction_lnt_or_ts_value_78

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_78` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 78"]

    @gfunction_lnt_or_ts_value_78.setter
    def gfunction_lnt_or_ts_value_78(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 78`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 78`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_78`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 78"] = value

    @property
    def gfunction_g_value_78(self):
        """Get gfunction_g_value_78

        Returns:
            float: the value of `gfunction_g_value_78` or None if not set
        """
        return self._data["G-Function G Value 78"]

    @gfunction_g_value_78.setter
    def gfunction_g_value_78(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 78`

        Args:
            value (float): value for IDD Field `G-Function G Value 78`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_78`'.format(value))
        self._data["G-Function G Value 78"] = value

    @property
    def gfunction_lnt_or_ts_value_79(self):
        """Get gfunction_lnt_or_ts_value_79

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_79` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 79"]

    @gfunction_lnt_or_ts_value_79.setter
    def gfunction_lnt_or_ts_value_79(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 79`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 79`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_79`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 79"] = value

    @property
    def gfunction_g_value_79(self):
        """Get gfunction_g_value_79

        Returns:
            float: the value of `gfunction_g_value_79` or None if not set
        """
        return self._data["G-Function G Value 79"]

    @gfunction_g_value_79.setter
    def gfunction_g_value_79(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 79`

        Args:
            value (float): value for IDD Field `G-Function G Value 79`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_79`'.format(value))
        self._data["G-Function G Value 79"] = value

    @property
    def gfunction_lnt_or_ts_value_80(self):
        """Get gfunction_lnt_or_ts_value_80

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_80` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 80"]

    @gfunction_lnt_or_ts_value_80.setter
    def gfunction_lnt_or_ts_value_80(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 80`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 80`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_80`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 80"] = value

    @property
    def gfunction_g_value_80(self):
        """Get gfunction_g_value_80

        Returns:
            float: the value of `gfunction_g_value_80` or None if not set
        """
        return self._data["G-Function G Value 80"]

    @gfunction_g_value_80.setter
    def gfunction_g_value_80(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 80`

        Args:
            value (float): value for IDD Field `G-Function G Value 80`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_80`'.format(value))
        self._data["G-Function G Value 80"] = value

    @property
    def gfunction_lnt_or_ts_value_81(self):
        """Get gfunction_lnt_or_ts_value_81

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_81` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 81"]

    @gfunction_lnt_or_ts_value_81.setter
    def gfunction_lnt_or_ts_value_81(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 81`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 81`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_81`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 81"] = value

    @property
    def gfunction_g_value_81(self):
        """Get gfunction_g_value_81

        Returns:
            float: the value of `gfunction_g_value_81` or None if not set
        """
        return self._data["G-Function G Value 81"]

    @gfunction_g_value_81.setter
    def gfunction_g_value_81(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 81`

        Args:
            value (float): value for IDD Field `G-Function G Value 81`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_81`'.format(value))
        self._data["G-Function G Value 81"] = value

    @property
    def gfunction_lnt_or_ts_value_82(self):
        """Get gfunction_lnt_or_ts_value_82

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_82` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 82"]

    @gfunction_lnt_or_ts_value_82.setter
    def gfunction_lnt_or_ts_value_82(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 82`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 82`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_82`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 82"] = value

    @property
    def gfunction_g_value_82(self):
        """Get gfunction_g_value_82

        Returns:
            float: the value of `gfunction_g_value_82` or None if not set
        """
        return self._data["G-Function G Value 82"]

    @gfunction_g_value_82.setter
    def gfunction_g_value_82(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 82`

        Args:
            value (float): value for IDD Field `G-Function G Value 82`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_82`'.format(value))
        self._data["G-Function G Value 82"] = value

    @property
    def gfunction_lnt_or_ts_value_83(self):
        """Get gfunction_lnt_or_ts_value_83

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_83` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 83"]

    @gfunction_lnt_or_ts_value_83.setter
    def gfunction_lnt_or_ts_value_83(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 83`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 83`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_83`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 83"] = value

    @property
    def gfunction_g_value_83(self):
        """Get gfunction_g_value_83

        Returns:
            float: the value of `gfunction_g_value_83` or None if not set
        """
        return self._data["G-Function G Value 83"]

    @gfunction_g_value_83.setter
    def gfunction_g_value_83(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 83`

        Args:
            value (float): value for IDD Field `G-Function G Value 83`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_83`'.format(value))
        self._data["G-Function G Value 83"] = value

    @property
    def gfunction_lnt_or_ts_value_84(self):
        """Get gfunction_lnt_or_ts_value_84

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_84` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 84"]

    @gfunction_lnt_or_ts_value_84.setter
    def gfunction_lnt_or_ts_value_84(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 84`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 84`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_84`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 84"] = value

    @property
    def gfunction_g_value_84(self):
        """Get gfunction_g_value_84

        Returns:
            float: the value of `gfunction_g_value_84` or None if not set
        """
        return self._data["G-Function G Value 84"]

    @gfunction_g_value_84.setter
    def gfunction_g_value_84(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 84`

        Args:
            value (float): value for IDD Field `G-Function G Value 84`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_84`'.format(value))
        self._data["G-Function G Value 84"] = value

    @property
    def gfunction_lnt_or_ts_value_85(self):
        """Get gfunction_lnt_or_ts_value_85

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_85` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 85"]

    @gfunction_lnt_or_ts_value_85.setter
    def gfunction_lnt_or_ts_value_85(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 85`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 85`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_85`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 85"] = value

    @property
    def gfunction_g_value_85(self):
        """Get gfunction_g_value_85

        Returns:
            float: the value of `gfunction_g_value_85` or None if not set
        """
        return self._data["G-Function G Value 85"]

    @gfunction_g_value_85.setter
    def gfunction_g_value_85(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 85`

        Args:
            value (float): value for IDD Field `G-Function G Value 85`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_85`'.format(value))
        self._data["G-Function G Value 85"] = value

    @property
    def gfunction_lnt_or_ts_value_86(self):
        """Get gfunction_lnt_or_ts_value_86

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_86` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 86"]

    @gfunction_lnt_or_ts_value_86.setter
    def gfunction_lnt_or_ts_value_86(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 86`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 86`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_86`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 86"] = value

    @property
    def gfunction_g_value_86(self):
        """Get gfunction_g_value_86

        Returns:
            float: the value of `gfunction_g_value_86` or None if not set
        """
        return self._data["G-Function G Value 86"]

    @gfunction_g_value_86.setter
    def gfunction_g_value_86(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 86`

        Args:
            value (float): value for IDD Field `G-Function G Value 86`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_86`'.format(value))
        self._data["G-Function G Value 86"] = value

    @property
    def gfunction_lnt_or_ts_value_87(self):
        """Get gfunction_lnt_or_ts_value_87

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_87` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 87"]

    @gfunction_lnt_or_ts_value_87.setter
    def gfunction_lnt_or_ts_value_87(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 87`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 87`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_87`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 87"] = value

    @property
    def gfunction_g_value_87(self):
        """Get gfunction_g_value_87

        Returns:
            float: the value of `gfunction_g_value_87` or None if not set
        """
        return self._data["G-Function G Value 87"]

    @gfunction_g_value_87.setter
    def gfunction_g_value_87(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 87`

        Args:
            value (float): value for IDD Field `G-Function G Value 87`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_87`'.format(value))
        self._data["G-Function G Value 87"] = value

    @property
    def gfunction_lnt_or_ts_value_88(self):
        """Get gfunction_lnt_or_ts_value_88

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_88` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 88"]

    @gfunction_lnt_or_ts_value_88.setter
    def gfunction_lnt_or_ts_value_88(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 88`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 88`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_88`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 88"] = value

    @property
    def gfunction_g_value_88(self):
        """Get gfunction_g_value_88

        Returns:
            float: the value of `gfunction_g_value_88` or None if not set
        """
        return self._data["G-Function G Value 88"]

    @gfunction_g_value_88.setter
    def gfunction_g_value_88(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 88`

        Args:
            value (float): value for IDD Field `G-Function G Value 88`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_88`'.format(value))
        self._data["G-Function G Value 88"] = value

    @property
    def gfunction_lnt_or_ts_value_89(self):
        """Get gfunction_lnt_or_ts_value_89

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_89` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 89"]

    @gfunction_lnt_or_ts_value_89.setter
    def gfunction_lnt_or_ts_value_89(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 89`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 89`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_89`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 89"] = value

    @property
    def gfunction_g_value_89(self):
        """Get gfunction_g_value_89

        Returns:
            float: the value of `gfunction_g_value_89` or None if not set
        """
        return self._data["G-Function G Value 89"]

    @gfunction_g_value_89.setter
    def gfunction_g_value_89(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 89`

        Args:
            value (float): value for IDD Field `G-Function G Value 89`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_89`'.format(value))
        self._data["G-Function G Value 89"] = value

    @property
    def gfunction_lnt_or_ts_value_90(self):
        """Get gfunction_lnt_or_ts_value_90

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_90` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 90"]

    @gfunction_lnt_or_ts_value_90.setter
    def gfunction_lnt_or_ts_value_90(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 90`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 90`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_90`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 90"] = value

    @property
    def gfunction_g_value_90(self):
        """Get gfunction_g_value_90

        Returns:
            float: the value of `gfunction_g_value_90` or None if not set
        """
        return self._data["G-Function G Value 90"]

    @gfunction_g_value_90.setter
    def gfunction_g_value_90(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 90`

        Args:
            value (float): value for IDD Field `G-Function G Value 90`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_90`'.format(value))
        self._data["G-Function G Value 90"] = value

    @property
    def gfunction_lnt_or_ts_value_91(self):
        """Get gfunction_lnt_or_ts_value_91

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_91` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 91"]

    @gfunction_lnt_or_ts_value_91.setter
    def gfunction_lnt_or_ts_value_91(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 91`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 91`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_91`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 91"] = value

    @property
    def gfunction_g_value_91(self):
        """Get gfunction_g_value_91

        Returns:
            float: the value of `gfunction_g_value_91` or None if not set
        """
        return self._data["G-Function G Value 91"]

    @gfunction_g_value_91.setter
    def gfunction_g_value_91(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 91`

        Args:
            value (float): value for IDD Field `G-Function G Value 91`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_91`'.format(value))
        self._data["G-Function G Value 91"] = value

    @property
    def gfunction_lnt_or_ts_value_92(self):
        """Get gfunction_lnt_or_ts_value_92

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_92` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 92"]

    @gfunction_lnt_or_ts_value_92.setter
    def gfunction_lnt_or_ts_value_92(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 92`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 92`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_92`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 92"] = value

    @property
    def gfunction_g_value_92(self):
        """Get gfunction_g_value_92

        Returns:
            float: the value of `gfunction_g_value_92` or None if not set
        """
        return self._data["G-Function G Value 92"]

    @gfunction_g_value_92.setter
    def gfunction_g_value_92(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 92`

        Args:
            value (float): value for IDD Field `G-Function G Value 92`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_92`'.format(value))
        self._data["G-Function G Value 92"] = value

    @property
    def gfunction_lnt_or_ts_value_93(self):
        """Get gfunction_lnt_or_ts_value_93

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_93` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 93"]

    @gfunction_lnt_or_ts_value_93.setter
    def gfunction_lnt_or_ts_value_93(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 93`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 93`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_93`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 93"] = value

    @property
    def gfunction_g_value_93(self):
        """Get gfunction_g_value_93

        Returns:
            float: the value of `gfunction_g_value_93` or None if not set
        """
        return self._data["G-Function G Value 93"]

    @gfunction_g_value_93.setter
    def gfunction_g_value_93(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 93`

        Args:
            value (float): value for IDD Field `G-Function G Value 93`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_93`'.format(value))
        self._data["G-Function G Value 93"] = value

    @property
    def gfunction_lnt_or_ts_value_94(self):
        """Get gfunction_lnt_or_ts_value_94

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_94` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 94"]

    @gfunction_lnt_or_ts_value_94.setter
    def gfunction_lnt_or_ts_value_94(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 94`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 94`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_94`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 94"] = value

    @property
    def gfunction_g_value_94(self):
        """Get gfunction_g_value_94

        Returns:
            float: the value of `gfunction_g_value_94` or None if not set
        """
        return self._data["G-Function G Value 94"]

    @gfunction_g_value_94.setter
    def gfunction_g_value_94(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 94`

        Args:
            value (float): value for IDD Field `G-Function G Value 94`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_94`'.format(value))
        self._data["G-Function G Value 94"] = value

    @property
    def gfunction_lnt_or_ts_value_95(self):
        """Get gfunction_lnt_or_ts_value_95

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_95` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 95"]

    @gfunction_lnt_or_ts_value_95.setter
    def gfunction_lnt_or_ts_value_95(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 95`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 95`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_95`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 95"] = value

    @property
    def gfunction_g_value_95(self):
        """Get gfunction_g_value_95

        Returns:
            float: the value of `gfunction_g_value_95` or None if not set
        """
        return self._data["G-Function G Value 95"]

    @gfunction_g_value_95.setter
    def gfunction_g_value_95(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 95`

        Args:
            value (float): value for IDD Field `G-Function G Value 95`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_95`'.format(value))
        self._data["G-Function G Value 95"] = value

    @property
    def gfunction_lnt_or_ts_value_96(self):
        """Get gfunction_lnt_or_ts_value_96

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_96` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 96"]

    @gfunction_lnt_or_ts_value_96.setter
    def gfunction_lnt_or_ts_value_96(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 96`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 96`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_96`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 96"] = value

    @property
    def gfunction_g_value_96(self):
        """Get gfunction_g_value_96

        Returns:
            float: the value of `gfunction_g_value_96` or None if not set
        """
        return self._data["G-Function G Value 96"]

    @gfunction_g_value_96.setter
    def gfunction_g_value_96(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 96`

        Args:
            value (float): value for IDD Field `G-Function G Value 96`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_96`'.format(value))
        self._data["G-Function G Value 96"] = value

    @property
    def gfunction_lnt_or_ts_value_97(self):
        """Get gfunction_lnt_or_ts_value_97

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_97` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 97"]

    @gfunction_lnt_or_ts_value_97.setter
    def gfunction_lnt_or_ts_value_97(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 97`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 97`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_97`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 97"] = value

    @property
    def gfunction_g_value_97(self):
        """Get gfunction_g_value_97

        Returns:
            float: the value of `gfunction_g_value_97` or None if not set
        """
        return self._data["G-Function G Value 97"]

    @gfunction_g_value_97.setter
    def gfunction_g_value_97(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 97`

        Args:
            value (float): value for IDD Field `G-Function G Value 97`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_97`'.format(value))
        self._data["G-Function G Value 97"] = value

    @property
    def gfunction_lnt_or_ts_value_98(self):
        """Get gfunction_lnt_or_ts_value_98

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_98` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 98"]

    @gfunction_lnt_or_ts_value_98.setter
    def gfunction_lnt_or_ts_value_98(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 98`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 98`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_98`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 98"] = value

    @property
    def gfunction_g_value_98(self):
        """Get gfunction_g_value_98

        Returns:
            float: the value of `gfunction_g_value_98` or None if not set
        """
        return self._data["G-Function G Value 98"]

    @gfunction_g_value_98.setter
    def gfunction_g_value_98(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 98`

        Args:
            value (float): value for IDD Field `G-Function G Value 98`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_98`'.format(value))
        self._data["G-Function G Value 98"] = value

    @property
    def gfunction_lnt_or_ts_value_99(self):
        """Get gfunction_lnt_or_ts_value_99

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_99` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 99"]

    @gfunction_lnt_or_ts_value_99.setter
    def gfunction_lnt_or_ts_value_99(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 99`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 99`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_99`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 99"] = value

    @property
    def gfunction_g_value_99(self):
        """Get gfunction_g_value_99

        Returns:
            float: the value of `gfunction_g_value_99` or None if not set
        """
        return self._data["G-Function G Value 99"]

    @gfunction_g_value_99.setter
    def gfunction_g_value_99(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 99`

        Args:
            value (float): value for IDD Field `G-Function G Value 99`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_99`'.format(value))
        self._data["G-Function G Value 99"] = value

    @property
    def gfunction_lnt_or_ts_value_100(self):
        """Get gfunction_lnt_or_ts_value_100

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_100` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 100"]

    @gfunction_lnt_or_ts_value_100.setter
    def gfunction_lnt_or_ts_value_100(self, value=None):
        """  Corresponds to IDD Field `G-Function Ln(T/Ts) Value 100`

        Args:
            value (float): value for IDD Field `G-Function Ln(T/Ts) Value 100`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_100`'.format(value))
        self._data["G-Function Ln(T/Ts) Value 100"] = value

    @property
    def gfunction_g_value_100(self):
        """Get gfunction_g_value_100

        Returns:
            float: the value of `gfunction_g_value_100` or None if not set
        """
        return self._data["G-Function G Value 100"]

    @gfunction_g_value_100.setter
    def gfunction_g_value_100(self, value=None):
        """  Corresponds to IDD Field `G-Function G Value 100`

        Args:
            value (float): value for IDD Field `G-Function G Value 100`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_100`'.format(value))
        self._data["G-Function G Value 100"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
        return good

    @classmethod
    def _to_str(cls, value):
        """ Represents values either as string or None values as empty string

        Args:
            value: a value
        """
        if value is None:
            return ''
        else:
            return str(value)

    def export(self):
        """ Export values of data object as list of strings"""
        out = []
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class GroundHeatExchangerPond(object):
    """ Corresponds to IDD object `GroundHeatExchanger:Pond`
        A model of a shallow pond with immersed pipe loops.
        Typically used in hybrid geothermal systems and included in the condenser loop.
        This component may also be used as a simple solar collector.
    
    """
    internal_name = "GroundHeatExchanger:Pond"
    field_count = 11
    required_fields = ["Name", "Fluid Inlet Node Name", "Fluid Outlet Node Name", "Pond Depth", "Pond Area", "Hydronic Tubing Inside Diameter", "Hydronic Tubing Outside Diameter", "Hydronic Tubing Thermal Conductivity", "Ground Thermal Conductivity", "Number of Tubing Circuits", "Length of Each Tubing Circuit"]

    def __init__(self):
        """ Init data dictionary object for IDD  `GroundHeatExchanger:Pond`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Fluid Inlet Node Name"] = None
        self._data["Fluid Outlet Node Name"] = None
        self._data["Pond Depth"] = None
        self._data["Pond Area"] = None
        self._data["Hydronic Tubing Inside Diameter"] = None
        self._data["Hydronic Tubing Outside Diameter"] = None
        self._data["Hydronic Tubing Thermal Conductivity"] = None
        self._data["Ground Thermal Conductivity"] = None
        self._data["Number of Tubing Circuits"] = None
        self._data["Length of Each Tubing Circuit"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fluid_inlet_node_name = None
        else:
            self.fluid_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fluid_outlet_node_name = None
        else:
            self.fluid_outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pond_depth = None
        else:
            self.pond_depth = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pond_area = None
        else:
            self.pond_area = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.hydronic_tubing_inside_diameter = None
        else:
            self.hydronic_tubing_inside_diameter = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.hydronic_tubing_outside_diameter = None
        else:
            self.hydronic_tubing_outside_diameter = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.hydronic_tubing_thermal_conductivity = None
        else:
            self.hydronic_tubing_thermal_conductivity = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.ground_thermal_conductivity = None
        else:
            self.ground_thermal_conductivity = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.number_of_tubing_circuits = None
        else:
            self.number_of_tubing_circuits = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.length_of_each_tubing_circuit = None
        else:
            self.length_of_each_tubing_circuit = vals[i]
        i += 1
        if i >= len(vals):
            return

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `Name`

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')
        self._data["Name"] = value

    @property
    def fluid_inlet_node_name(self):
        """Get fluid_inlet_node_name

        Returns:
            str: the value of `fluid_inlet_node_name` or None if not set
        """
        return self._data["Fluid Inlet Node Name"]

    @fluid_inlet_node_name.setter
    def fluid_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Fluid Inlet Node Name`

        Args:
            value (str): value for IDD Field `Fluid Inlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `fluid_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `fluid_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `fluid_inlet_node_name`')
        self._data["Fluid Inlet Node Name"] = value

    @property
    def fluid_outlet_node_name(self):
        """Get fluid_outlet_node_name

        Returns:
            str: the value of `fluid_outlet_node_name` or None if not set
        """
        return self._data["Fluid Outlet Node Name"]

    @fluid_outlet_node_name.setter
    def fluid_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Fluid Outlet Node Name`

        Args:
            value (str): value for IDD Field `Fluid Outlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `fluid_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `fluid_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `fluid_outlet_node_name`')
        self._data["Fluid Outlet Node Name"] = value

    @property
    def pond_depth(self):
        """Get pond_depth

        Returns:
            float: the value of `pond_depth` or None if not set
        """
        return self._data["Pond Depth"]

    @pond_depth.setter
    def pond_depth(self, value=None):
        """  Corresponds to IDD Field `Pond Depth`

        Args:
            value (float): value for IDD Field `Pond Depth`
                Units: m
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `pond_depth`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `pond_depth`')
        self._data["Pond Depth"] = value

    @property
    def pond_area(self):
        """Get pond_area

        Returns:
            float: the value of `pond_area` or None if not set
        """
        return self._data["Pond Area"]

    @pond_area.setter
    def pond_area(self, value=None):
        """  Corresponds to IDD Field `Pond Area`

        Args:
            value (float): value for IDD Field `Pond Area`
                Units: m2
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `pond_area`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `pond_area`')
        self._data["Pond Area"] = value

    @property
    def hydronic_tubing_inside_diameter(self):
        """Get hydronic_tubing_inside_diameter

        Returns:
            float: the value of `hydronic_tubing_inside_diameter` or None if not set
        """
        return self._data["Hydronic Tubing Inside Diameter"]

    @hydronic_tubing_inside_diameter.setter
    def hydronic_tubing_inside_diameter(self, value=None):
        """  Corresponds to IDD Field `Hydronic Tubing Inside Diameter`

        Args:
            value (float): value for IDD Field `Hydronic Tubing Inside Diameter`
                Units: m
                IP-Units: in
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `hydronic_tubing_inside_diameter`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `hydronic_tubing_inside_diameter`')
        self._data["Hydronic Tubing Inside Diameter"] = value

    @property
    def hydronic_tubing_outside_diameter(self):
        """Get hydronic_tubing_outside_diameter

        Returns:
            float: the value of `hydronic_tubing_outside_diameter` or None if not set
        """
        return self._data["Hydronic Tubing Outside Diameter"]

    @hydronic_tubing_outside_diameter.setter
    def hydronic_tubing_outside_diameter(self, value=None):
        """  Corresponds to IDD Field `Hydronic Tubing Outside Diameter`

        Args:
            value (float): value for IDD Field `Hydronic Tubing Outside Diameter`
                Units: m
                IP-Units: in
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `hydronic_tubing_outside_diameter`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `hydronic_tubing_outside_diameter`')
        self._data["Hydronic Tubing Outside Diameter"] = value

    @property
    def hydronic_tubing_thermal_conductivity(self):
        """Get hydronic_tubing_thermal_conductivity

        Returns:
            float: the value of `hydronic_tubing_thermal_conductivity` or None if not set
        """
        return self._data["Hydronic Tubing Thermal Conductivity"]

    @hydronic_tubing_thermal_conductivity.setter
    def hydronic_tubing_thermal_conductivity(self, value=None):
        """  Corresponds to IDD Field `Hydronic Tubing Thermal Conductivity`

        Args:
            value (float): value for IDD Field `Hydronic Tubing Thermal Conductivity`
                Units: W/m-K
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `hydronic_tubing_thermal_conductivity`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `hydronic_tubing_thermal_conductivity`')
        self._data["Hydronic Tubing Thermal Conductivity"] = value

    @property
    def ground_thermal_conductivity(self):
        """Get ground_thermal_conductivity

        Returns:
            float: the value of `ground_thermal_conductivity` or None if not set
        """
        return self._data["Ground Thermal Conductivity"]

    @ground_thermal_conductivity.setter
    def ground_thermal_conductivity(self, value=None):
        """  Corresponds to IDD Field `Ground Thermal Conductivity`

        Args:
            value (float): value for IDD Field `Ground Thermal Conductivity`
                Units: W/m2-K
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `ground_thermal_conductivity`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `ground_thermal_conductivity`')
        self._data["Ground Thermal Conductivity"] = value

    @property
    def number_of_tubing_circuits(self):
        """Get number_of_tubing_circuits

        Returns:
            int: the value of `number_of_tubing_circuits` or None if not set
        """
        return self._data["Number of Tubing Circuits"]

    @number_of_tubing_circuits.setter
    def number_of_tubing_circuits(self, value=None):
        """  Corresponds to IDD Field `Number of Tubing Circuits`

        Args:
            value (int): value for IDD Field `Number of Tubing Circuits`
                value >= 1
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = int(value)
            except ValueError:
                raise ValueError('value {} need to be of type int '
                                 'for field `number_of_tubing_circuits`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `number_of_tubing_circuits`')
        self._data["Number of Tubing Circuits"] = value

    @property
    def length_of_each_tubing_circuit(self):
        """Get length_of_each_tubing_circuit

        Returns:
            float: the value of `length_of_each_tubing_circuit` or None if not set
        """
        return self._data["Length of Each Tubing Circuit"]

    @length_of_each_tubing_circuit.setter
    def length_of_each_tubing_circuit(self, value=None):
        """  Corresponds to IDD Field `Length of Each Tubing Circuit`

        Args:
            value (float): value for IDD Field `Length of Each Tubing Circuit`
                Units: m
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `length_of_each_tubing_circuit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `length_of_each_tubing_circuit`')
        self._data["Length of Each Tubing Circuit"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
        return good

    @classmethod
    def _to_str(cls, value):
        """ Represents values either as string or None values as empty string

        Args:
            value: a value
        """
        if value is None:
            return ''
        else:
            return str(value)

    def export(self):
        """ Export values of data object as list of strings"""
        out = []
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class GroundHeatExchangerSurface(object):
    """ Corresponds to IDD object `GroundHeatExchanger:Surface`
        A hydronic surface/panel consisting of a multi-layer construction with embedded rows of tubes.
        Typically used in hybrid geothermal systems and included in the condenser loop.
        This component may also be used as a simple solar collector.
        The bottom surface may be defined as ground-coupled or exposed to wind (eg. bridge deck).
    
    """
    internal_name = "GroundHeatExchanger:Surface"
    field_count = 10
    required_fields = ["Name", "Construction Name", "Fluid Inlet Node Name", "Fluid Outlet Node Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `GroundHeatExchanger:Surface`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Construction Name"] = None
        self._data["Fluid Inlet Node Name"] = None
        self._data["Fluid Outlet Node Name"] = None
        self._data["Hydronic Tubing Inside Diameter"] = None
        self._data["Number of Tubing Circuits"] = None
        self._data["Hydronic Tube Spacing"] = None
        self._data["Surface Length"] = None
        self._data["Surface Width"] = None
        self._data["Lower Surface Environment"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.construction_name = None
        else:
            self.construction_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fluid_inlet_node_name = None
        else:
            self.fluid_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fluid_outlet_node_name = None
        else:
            self.fluid_outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.hydronic_tubing_inside_diameter = None
        else:
            self.hydronic_tubing_inside_diameter = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.number_of_tubing_circuits = None
        else:
            self.number_of_tubing_circuits = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.hydronic_tube_spacing = None
        else:
            self.hydronic_tube_spacing = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.surface_length = None
        else:
            self.surface_length = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.surface_width = None
        else:
            self.surface_width = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.lower_surface_environment = None
        else:
            self.lower_surface_environment = vals[i]
        i += 1
        if i >= len(vals):
            return

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `Name`

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')
        self._data["Name"] = value

    @property
    def construction_name(self):
        """Get construction_name

        Returns:
            str: the value of `construction_name` or None if not set
        """
        return self._data["Construction Name"]

    @construction_name.setter
    def construction_name(self, value=None):
        """  Corresponds to IDD Field `Construction Name`

        Args:
            value (str): value for IDD Field `Construction Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `construction_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `construction_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `construction_name`')
        self._data["Construction Name"] = value

    @property
    def fluid_inlet_node_name(self):
        """Get fluid_inlet_node_name

        Returns:
            str: the value of `fluid_inlet_node_name` or None if not set
        """
        return self._data["Fluid Inlet Node Name"]

    @fluid_inlet_node_name.setter
    def fluid_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Fluid Inlet Node Name`

        Args:
            value (str): value for IDD Field `Fluid Inlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `fluid_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `fluid_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `fluid_inlet_node_name`')
        self._data["Fluid Inlet Node Name"] = value

    @property
    def fluid_outlet_node_name(self):
        """Get fluid_outlet_node_name

        Returns:
            str: the value of `fluid_outlet_node_name` or None if not set
        """
        return self._data["Fluid Outlet Node Name"]

    @fluid_outlet_node_name.setter
    def fluid_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Fluid Outlet Node Name`

        Args:
            value (str): value for IDD Field `Fluid Outlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `fluid_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `fluid_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `fluid_outlet_node_name`')
        self._data["Fluid Outlet Node Name"] = value

    @property
    def hydronic_tubing_inside_diameter(self):
        """Get hydronic_tubing_inside_diameter

        Returns:
            float: the value of `hydronic_tubing_inside_diameter` or None if not set
        """
        return self._data["Hydronic Tubing Inside Diameter"]

    @hydronic_tubing_inside_diameter.setter
    def hydronic_tubing_inside_diameter(self, value=None):
        """  Corresponds to IDD Field `Hydronic Tubing Inside Diameter`

        Args:
            value (float): value for IDD Field `Hydronic Tubing Inside Diameter`
                Units: m
                IP-Units: in
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `hydronic_tubing_inside_diameter`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `hydronic_tubing_inside_diameter`')
        self._data["Hydronic Tubing Inside Diameter"] = value

    @property
    def number_of_tubing_circuits(self):
        """Get number_of_tubing_circuits

        Returns:
            int: the value of `number_of_tubing_circuits` or None if not set
        """
        return self._data["Number of Tubing Circuits"]

    @number_of_tubing_circuits.setter
    def number_of_tubing_circuits(self, value=None):
        """  Corresponds to IDD Field `Number of Tubing Circuits`

        Args:
            value (int): value for IDD Field `Number of Tubing Circuits`
                value >= 1
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = int(value)
            except ValueError:
                raise ValueError('value {} need to be of type int '
                                 'for field `number_of_tubing_circuits`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `number_of_tubing_circuits`')
        self._data["Number of Tubing Circuits"] = value

    @property
    def hydronic_tube_spacing(self):
        """Get hydronic_tube_spacing

        Returns:
            float: the value of `hydronic_tube_spacing` or None if not set
        """
        return self._data["Hydronic Tube Spacing"]

    @hydronic_tube_spacing.setter
    def hydronic_tube_spacing(self, value=None):
        """  Corresponds to IDD Field `Hydronic Tube Spacing`

        Args:
            value (float): value for IDD Field `Hydronic Tube Spacing`
                Units: m
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `hydronic_tube_spacing`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `hydronic_tube_spacing`')
        self._data["Hydronic Tube Spacing"] = value

    @property
    def surface_length(self):
        """Get surface_length

        Returns:
            float: the value of `surface_length` or None if not set
        """
        return self._data["Surface Length"]

    @surface_length.setter
    def surface_length(self, value=None):
        """  Corresponds to IDD Field `Surface Length`

        Args:
            value (float): value for IDD Field `Surface Length`
                Units: m
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `surface_length`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `surface_length`')
        self._data["Surface Length"] = value

    @property
    def surface_width(self):
        """Get surface_width

        Returns:
            float: the value of `surface_width` or None if not set
        """
        return self._data["Surface Width"]

    @surface_width.setter
    def surface_width(self, value=None):
        """  Corresponds to IDD Field `Surface Width`

        Args:
            value (float): value for IDD Field `Surface Width`
                Units: m
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `surface_width`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `surface_width`')
        self._data["Surface Width"] = value

    @property
    def lower_surface_environment(self):
        """Get lower_surface_environment

        Returns:
            str: the value of `lower_surface_environment` or None if not set
        """
        return self._data["Lower Surface Environment"]

    @lower_surface_environment.setter
    def lower_surface_environment(self, value="Ground"):
        """  Corresponds to IDD Field `Lower Surface Environment`

        Args:
            value (str): value for IDD Field `Lower Surface Environment`
                Accepted values are:
                      - Ground
                      - Exposed
                Default value: Ground
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `lower_surface_environment`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `lower_surface_environment`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `lower_surface_environment`')
            vals = {}
            vals["ground"] = "Ground"
            vals["exposed"] = "Exposed"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `lower_surface_environment`'.format(value))
            value = vals[value_lower]
        self._data["Lower Surface Environment"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
        return good

    @classmethod
    def _to_str(cls, value):
        """ Represents values either as string or None values as empty string

        Args:
            value: a value
        """
        if value is None:
            return ''
        else:
            return str(value)

    def export(self):
        """ Export values of data object as list of strings"""
        out = []
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class GroundHeatExchangerHorizontalTrench(object):
    """ Corresponds to IDD object `GroundHeatExchanger:HorizontalTrench`
        This models a horizontal heat exchanger placed in a series of trenches
        The model uses the PipingSystem:Underground underlying algorithms,
        but provides a more usable input interface.
    
    """
    internal_name = "GroundHeatExchanger:HorizontalTrench"
    field_count = 22
    required_fields = ["Name", "Inlet Node Name", "Outlet Node Name", "Design Flow Rate", "Soil Specific Heat"]

    def __init__(self):
        """ Init data dictionary object for IDD  `GroundHeatExchanger:HorizontalTrench`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Inlet Node Name"] = None
        self._data["Outlet Node Name"] = None
        self._data["Design Flow Rate"] = None
        self._data["Trench Length in Pipe Axial Direction"] = None
        self._data["Number of Trenches"] = None
        self._data["Horizontal Spacing Between Pipes"] = None
        self._data["Pipe Inner Diameter"] = None
        self._data["Pipe Outer Diameter"] = None
        self._data["Burial Depth"] = None
        self._data["Soil Thermal Conductivity"] = None
        self._data["Soil Density"] = None
        self._data["Soil Specific Heat"] = None
        self._data["Pipe Thermal Conductivity"] = None
        self._data["Pipe Density"] = None
        self._data["Pipe Specific Heat"] = None
        self._data["Soil Moisture Content Percent"] = None
        self._data["Soil Moisture Content Percent at Saturation"] = None
        self._data["Kusuda-Achenbach Average Surface Temperature"] = None
        self._data["Kusuda-Achenbach Average Amplitude of Surface Temperature"] = None
        self._data["Kusuda-Achenbach Phase Shift of Minimum Surface Temperature"] = None
        self._data["Evapotranspiration Ground Cover Parameter"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.inlet_node_name = None
        else:
            self.inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outlet_node_name = None
        else:
            self.outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_flow_rate = None
        else:
            self.design_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.trench_length_in_pipe_axial_direction = None
        else:
            self.trench_length_in_pipe_axial_direction = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.number_of_trenches = None
        else:
            self.number_of_trenches = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.horizontal_spacing_between_pipes = None
        else:
            self.horizontal_spacing_between_pipes = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pipe_inner_diameter = None
        else:
            self.pipe_inner_diameter = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pipe_outer_diameter = None
        else:
            self.pipe_outer_diameter = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.burial_depth = None
        else:
            self.burial_depth = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.soil_thermal_conductivity = None
        else:
            self.soil_thermal_conductivity = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.soil_density = None
        else:
            self.soil_density = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.soil_specific_heat = None
        else:
            self.soil_specific_heat = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pipe_thermal_conductivity = None
        else:
            self.pipe_thermal_conductivity = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pipe_density = None
        else:
            self.pipe_density = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pipe_specific_heat = None
        else:
            self.pipe_specific_heat = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.soil_moisture_content_percent = None
        else:
            self.soil_moisture_content_percent = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.soil_moisture_content_percent_at_saturation = None
        else:
            self.soil_moisture_content_percent_at_saturation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.kusudaachenbach_average_surface_temperature = None
        else:
            self.kusudaachenbach_average_surface_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.kusudaachenbach_average_amplitude_of_surface_temperature = None
        else:
            self.kusudaachenbach_average_amplitude_of_surface_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.kusudaachenbach_phase_shift_of_minimum_surface_temperature = None
        else:
            self.kusudaachenbach_phase_shift_of_minimum_surface_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.evapotranspiration_ground_cover_parameter = None
        else:
            self.evapotranspiration_ground_cover_parameter = vals[i]
        i += 1
        if i >= len(vals):
            return

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `Name`

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')
        self._data["Name"] = value

    @property
    def inlet_node_name(self):
        """Get inlet_node_name

        Returns:
            str: the value of `inlet_node_name` or None if not set
        """
        return self._data["Inlet Node Name"]

    @inlet_node_name.setter
    def inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Inlet Node Name`

        Args:
            value (str): value for IDD Field `Inlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `inlet_node_name`')
        self._data["Inlet Node Name"] = value

    @property
    def outlet_node_name(self):
        """Get outlet_node_name

        Returns:
            str: the value of `outlet_node_name` or None if not set
        """
        return self._data["Outlet Node Name"]

    @outlet_node_name.setter
    def outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Outlet Node Name`

        Args:
            value (str): value for IDD Field `Outlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `outlet_node_name`')
        self._data["Outlet Node Name"] = value

    @property
    def design_flow_rate(self):
        """Get design_flow_rate

        Returns:
            float: the value of `design_flow_rate` or None if not set
        """
        return self._data["Design Flow Rate"]

    @design_flow_rate.setter
    def design_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Design Flow Rate`

        Args:
            value (float): value for IDD Field `Design Flow Rate`
                Units: m3/s
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `design_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `design_flow_rate`')
        self._data["Design Flow Rate"] = value

    @property
    def trench_length_in_pipe_axial_direction(self):
        """Get trench_length_in_pipe_axial_direction

        Returns:
            float: the value of `trench_length_in_pipe_axial_direction` or None if not set
        """
        return self._data["Trench Length in Pipe Axial Direction"]

    @trench_length_in_pipe_axial_direction.setter
    def trench_length_in_pipe_axial_direction(self, value=50.0):
        """  Corresponds to IDD Field `Trench Length in Pipe Axial Direction`
        This is the total pipe axial length of the heat exchanger
        If all pipe trenches are parallel, this is the length of a
        single trench.  If a single, long run of pipe is used with one
        trench, this is the full length of the pipe run.

        Args:
            value (float): value for IDD Field `Trench Length in Pipe Axial Direction`
                Units: m
                IP-Units: ft
                Default value: 50.0
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `trench_length_in_pipe_axial_direction`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `trench_length_in_pipe_axial_direction`')
        self._data["Trench Length in Pipe Axial Direction"] = value

    @property
    def number_of_trenches(self):
        """Get number_of_trenches

        Returns:
            int: the value of `number_of_trenches` or None if not set
        """
        return self._data["Number of Trenches"]

    @number_of_trenches.setter
    def number_of_trenches(self, value=1):
        """  Corresponds to IDD Field `Number of Trenches`
        This is the number of horizontal legs that will be used
        in the entire heat exchanger, one pipe per trench

        Args:
            value (int): value for IDD Field `Number of Trenches`
                Default value: 1
                value >= 1
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = int(value)
            except ValueError:
                raise ValueError('value {} need to be of type int '
                                 'for field `number_of_trenches`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `number_of_trenches`')
        self._data["Number of Trenches"] = value

    @property
    def horizontal_spacing_between_pipes(self):
        """Get horizontal_spacing_between_pipes

        Returns:
            float: the value of `horizontal_spacing_between_pipes` or None if not set
        """
        return self._data["Horizontal Spacing Between Pipes"]

    @horizontal_spacing_between_pipes.setter
    def horizontal_spacing_between_pipes(self, value=1.0):
        """  Corresponds to IDD Field `Horizontal Spacing Between Pipes`
        This represents the average horizontal spacing between any two
        trenches for heat exchangers that have multiple trenches

        Args:
            value (float): value for IDD Field `Horizontal Spacing Between Pipes`
                Units: m
                Default value: 1.0
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `horizontal_spacing_between_pipes`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `horizontal_spacing_between_pipes`')
        self._data["Horizontal Spacing Between Pipes"] = value

    @property
    def pipe_inner_diameter(self):
        """Get pipe_inner_diameter

        Returns:
            float: the value of `pipe_inner_diameter` or None if not set
        """
        return self._data["Pipe Inner Diameter"]

    @pipe_inner_diameter.setter
    def pipe_inner_diameter(self, value=0.016):
        """  Corresponds to IDD Field `Pipe Inner Diameter`

        Args:
            value (float): value for IDD Field `Pipe Inner Diameter`
                Units: m
                IP-Units: in
                Default value: 0.016
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `pipe_inner_diameter`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `pipe_inner_diameter`')
        self._data["Pipe Inner Diameter"] = value

    @property
    def pipe_outer_diameter(self):
        """Get pipe_outer_diameter

        Returns:
            float: the value of `pipe_outer_diameter` or None if not set
        """
        return self._data["Pipe Outer Diameter"]

    @pipe_outer_diameter.setter
    def pipe_outer_diameter(self, value=0.026):
        """  Corresponds to IDD Field `Pipe Outer Diameter`

        Args:
            value (float): value for IDD Field `Pipe Outer Diameter`
                Units: m
                IP-Units: in
                Default value: 0.026
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `pipe_outer_diameter`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `pipe_outer_diameter`')
        self._data["Pipe Outer Diameter"] = value

    @property
    def burial_depth(self):
        """Get burial_depth

        Returns:
            float: the value of `burial_depth` or None if not set
        """
        return self._data["Burial Depth"]

    @burial_depth.setter
    def burial_depth(self, value=1.5):
        """  Corresponds to IDD Field `Burial Depth`
        This is the burial depth of the pipes, or the trenches
        containing the pipes

        Args:
            value (float): value for IDD Field `Burial Depth`
                Units: m
                IP-Units: ft
                Default value: 1.5
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `burial_depth`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `burial_depth`')
        self._data["Burial Depth"] = value

    @property
    def soil_thermal_conductivity(self):
        """Get soil_thermal_conductivity

        Returns:
            float: the value of `soil_thermal_conductivity` or None if not set
        """
        return self._data["Soil Thermal Conductivity"]

    @soil_thermal_conductivity.setter
    def soil_thermal_conductivity(self, value=1.08):
        """  Corresponds to IDD Field `Soil Thermal Conductivity`

        Args:
            value (float): value for IDD Field `Soil Thermal Conductivity`
                Units: W/m-K
                Default value: 1.08
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `soil_thermal_conductivity`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `soil_thermal_conductivity`')
        self._data["Soil Thermal Conductivity"] = value

    @property
    def soil_density(self):
        """Get soil_density

        Returns:
            float: the value of `soil_density` or None if not set
        """
        return self._data["Soil Density"]

    @soil_density.setter
    def soil_density(self, value=962.0):
        """  Corresponds to IDD Field `Soil Density`

        Args:
            value (float): value for IDD Field `Soil Density`
                Units: kg/m3
                Default value: 962.0
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `soil_density`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `soil_density`')
        self._data["Soil Density"] = value

    @property
    def soil_specific_heat(self):
        """Get soil_specific_heat

        Returns:
            float: the value of `soil_specific_heat` or None if not set
        """
        return self._data["Soil Specific Heat"]

    @soil_specific_heat.setter
    def soil_specific_heat(self, value=2576.0):
        """  Corresponds to IDD Field `Soil Specific Heat`

        Args:
            value (float): value for IDD Field `Soil Specific Heat`
                Units: J/kg-K
                Default value: 2576.0
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `soil_specific_heat`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `soil_specific_heat`')
        self._data["Soil Specific Heat"] = value

    @property
    def pipe_thermal_conductivity(self):
        """Get pipe_thermal_conductivity

        Returns:
            float: the value of `pipe_thermal_conductivity` or None if not set
        """
        return self._data["Pipe Thermal Conductivity"]

    @pipe_thermal_conductivity.setter
    def pipe_thermal_conductivity(self, value=0.3895):
        """  Corresponds to IDD Field `Pipe Thermal Conductivity`

        Args:
            value (float): value for IDD Field `Pipe Thermal Conductivity`
                Units: W/m-K
                Default value: 0.3895
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `pipe_thermal_conductivity`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `pipe_thermal_conductivity`')
        self._data["Pipe Thermal Conductivity"] = value

    @property
    def pipe_density(self):
        """Get pipe_density

        Returns:
            float: the value of `pipe_density` or None if not set
        """
        return self._data["Pipe Density"]

    @pipe_density.setter
    def pipe_density(self, value=641.0):
        """  Corresponds to IDD Field `Pipe Density`

        Args:
            value (float): value for IDD Field `Pipe Density`
                Units: kg/m3
                Default value: 641.0
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `pipe_density`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `pipe_density`')
        self._data["Pipe Density"] = value

    @property
    def pipe_specific_heat(self):
        """Get pipe_specific_heat

        Returns:
            float: the value of `pipe_specific_heat` or None if not set
        """
        return self._data["Pipe Specific Heat"]

    @pipe_specific_heat.setter
    def pipe_specific_heat(self, value=2405.0):
        """  Corresponds to IDD Field `Pipe Specific Heat`

        Args:
            value (float): value for IDD Field `Pipe Specific Heat`
                Units: J/kg-K
                Default value: 2405.0
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `pipe_specific_heat`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `pipe_specific_heat`')
        self._data["Pipe Specific Heat"] = value

    @property
    def soil_moisture_content_percent(self):
        """Get soil_moisture_content_percent

        Returns:
            float: the value of `soil_moisture_content_percent` or None if not set
        """
        return self._data["Soil Moisture Content Percent"]

    @soil_moisture_content_percent.setter
    def soil_moisture_content_percent(self, value=30.0):
        """  Corresponds to IDD Field `Soil Moisture Content Percent`

        Args:
            value (float): value for IDD Field `Soil Moisture Content Percent`
                Units: percent
                Default value: 30.0
                value >= 0.0
                value <= 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `soil_moisture_content_percent`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `soil_moisture_content_percent`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `soil_moisture_content_percent`')
        self._data["Soil Moisture Content Percent"] = value

    @property
    def soil_moisture_content_percent_at_saturation(self):
        """Get soil_moisture_content_percent_at_saturation

        Returns:
            float: the value of `soil_moisture_content_percent_at_saturation` or None if not set
        """
        return self._data["Soil Moisture Content Percent at Saturation"]

    @soil_moisture_content_percent_at_saturation.setter
    def soil_moisture_content_percent_at_saturation(self, value=50.0):
        """  Corresponds to IDD Field `Soil Moisture Content Percent at Saturation`

        Args:
            value (float): value for IDD Field `Soil Moisture Content Percent at Saturation`
                Units: percent
                Default value: 50.0
                value >= 0.0
                value <= 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `soil_moisture_content_percent_at_saturation`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `soil_moisture_content_percent_at_saturation`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `soil_moisture_content_percent_at_saturation`')
        self._data["Soil Moisture Content Percent at Saturation"] = value

    @property
    def kusudaachenbach_average_surface_temperature(self):
        """Get kusudaachenbach_average_surface_temperature

        Returns:
            float: the value of `kusudaachenbach_average_surface_temperature` or None if not set
        """
        return self._data["Kusuda-Achenbach Average Surface Temperature"]

    @kusudaachenbach_average_surface_temperature.setter
    def kusudaachenbach_average_surface_temperature(self, value=None):
        """  Corresponds to IDD Field `Kusuda-Achenbach Average Surface Temperature`
        This is the parameter for average annual surface temperature
        This is an optional input in that if it is missing, a
        Site:GroundTemperature:Shallow object must be found in the input
        The undisturbed ground temperature will be approximated from this object

        Args:
            value (float): value for IDD Field `Kusuda-Achenbach Average Surface Temperature`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `kusudaachenbach_average_surface_temperature`'.format(value))
        self._data["Kusuda-Achenbach Average Surface Temperature"] = value

    @property
    def kusudaachenbach_average_amplitude_of_surface_temperature(self):
        """Get kusudaachenbach_average_amplitude_of_surface_temperature

        Returns:
            float: the value of `kusudaachenbach_average_amplitude_of_surface_temperature` or None if not set
        """
        return self._data["Kusuda-Achenbach Average Amplitude of Surface Temperature"]

    @kusudaachenbach_average_amplitude_of_surface_temperature.setter
    def kusudaachenbach_average_amplitude_of_surface_temperature(self, value=None):
        """  Corresponds to IDD Field `Kusuda-Achenbach Average Amplitude of Surface Temperature`
        This is the parameter for annual average amplitude from average surface temperature
        This is an optional input in that if it is missing, a
        Site:GroundTemperature:Shallow object must be found in the input
        The undisturbed ground temperature will be approximated from this object

        Args:
            value (float): value for IDD Field `Kusuda-Achenbach Average Amplitude of Surface Temperature`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `kusudaachenbach_average_amplitude_of_surface_temperature`'.format(value))
        self._data["Kusuda-Achenbach Average Amplitude of Surface Temperature"] = value

    @property
    def kusudaachenbach_phase_shift_of_minimum_surface_temperature(self):
        """Get kusudaachenbach_phase_shift_of_minimum_surface_temperature

        Returns:
            float: the value of `kusudaachenbach_phase_shift_of_minimum_surface_temperature` or None if not set
        """
        return self._data["Kusuda-Achenbach Phase Shift of Minimum Surface Temperature"]

    @kusudaachenbach_phase_shift_of_minimum_surface_temperature.setter
    def kusudaachenbach_phase_shift_of_minimum_surface_temperature(self, value=None):
        """  Corresponds to IDD Field `Kusuda-Achenbach Phase Shift of Minimum Surface Temperature`
        This is the parameter for phase shift from minimum surface temperature
        This is an optional input in that if it is missing, a
        Site:GroundTemperature:Shallow object must be found in the input
        The undisturbed ground temperature will be approximated from this object

        Args:
            value (float): value for IDD Field `Kusuda-Achenbach Phase Shift of Minimum Surface Temperature`
                Units: days
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `kusudaachenbach_phase_shift_of_minimum_surface_temperature`'.format(value))
        self._data["Kusuda-Achenbach Phase Shift of Minimum Surface Temperature"] = value

    @property
    def evapotranspiration_ground_cover_parameter(self):
        """Get evapotranspiration_ground_cover_parameter

        Returns:
            float: the value of `evapotranspiration_ground_cover_parameter` or None if not set
        """
        return self._data["Evapotranspiration Ground Cover Parameter"]

    @evapotranspiration_ground_cover_parameter.setter
    def evapotranspiration_ground_cover_parameter(self, value=0.4):
        """  Corresponds to IDD Field `Evapotranspiration Ground Cover Parameter`
        This specifies the ground cover effects during evapotranspiration
        calculations.  The value roughly represents the following cases:
        = 0   : concrete or other solid, non-permeable ground surface material
        = 0.5 : short grass, much like a manicured lawn
        = 1   : standard reference state (12 cm grass)
        = 1.5 : wild growth

        Args:
            value (float): value for IDD Field `Evapotranspiration Ground Cover Parameter`
                Default value: 0.4
                value >= 0.0
                value <= 1.5
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `evapotranspiration_ground_cover_parameter`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `evapotranspiration_ground_cover_parameter`')
            if value > 1.5:
                raise ValueError('value need to be smaller 1.5 '
                                 'for field `evapotranspiration_ground_cover_parameter`')
        self._data["Evapotranspiration Ground Cover Parameter"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
        return good

    @classmethod
    def _to_str(cls, value):
        """ Represents values either as string or None values as empty string

        Args:
            value: a value
        """
        if value is None:
            return ''
        else:
            return str(value)

    def export(self):
        """ Export values of data object as list of strings"""
        out = []
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class HeatExchangerFluidToFluid(object):
    """ Corresponds to IDD object `HeatExchanger:FluidToFluid`
        A fluid/fluid heat exchanger designed to couple the supply side of one loop to the demand side of another loop
        Loops can be either plant or condenser loops but no air side connections are allowed
    
    """
    internal_name = "HeatExchanger:FluidToFluid"
    field_count = 20
    required_fields = ["Name", "Loop Demand Side Inlet Node Name", "Loop Demand Side Outlet Node Name", "Loop Demand Side Design Flow Rate", "Loop Supply Side Inlet Node Name", "Loop Supply Side Outlet Node Name", "Loop Supply Side Design Flow Rate", "Heat Exchange Model Type", "Heat Exchanger U-Factor Times Area Value", "Control Type", "Heat Transfer Metering End Use Type"]

    def __init__(self):
        """ Init data dictionary object for IDD  `HeatExchanger:FluidToFluid`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Loop Demand Side Inlet Node Name"] = None
        self._data["Loop Demand Side Outlet Node Name"] = None
        self._data["Loop Demand Side Design Flow Rate"] = None
        self._data["Loop Supply Side Inlet Node Name"] = None
        self._data["Loop Supply Side Outlet Node Name"] = None
        self._data["Loop Supply Side Design Flow Rate"] = None
        self._data["Heat Exchange Model Type"] = None
        self._data["Heat Exchanger U-Factor Times Area Value"] = None
        self._data["Control Type"] = None
        self._data["Heat Exchanger Setpoint Node Name"] = None
        self._data["Minimum Temperature Difference to Activate Heat Exchanger"] = None
        self._data["Heat Transfer Metering End Use Type"] = None
        self._data["Component Override Loop Supply Side Inlet Node Name"] = None
        self._data["Component Override Loop Demand Side Inlet Node Name"] = None
        self._data["Component Override Cooling Control Temperature Mode"] = None
        self._data["Sizing Factor"] = None
        self._data["Operation Minimum Temperature Limit"] = None
        self._data["Operation Maximum Temperature Limit"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.availability_schedule_name = None
        else:
            self.availability_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.loop_demand_side_inlet_node_name = None
        else:
            self.loop_demand_side_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.loop_demand_side_outlet_node_name = None
        else:
            self.loop_demand_side_outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.loop_demand_side_design_flow_rate = None
        else:
            self.loop_demand_side_design_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.loop_supply_side_inlet_node_name = None
        else:
            self.loop_supply_side_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.loop_supply_side_outlet_node_name = None
        else:
            self.loop_supply_side_outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.loop_supply_side_design_flow_rate = None
        else:
            self.loop_supply_side_design_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heat_exchange_model_type = None
        else:
            self.heat_exchange_model_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heat_exchanger_ufactor_times_area_value = None
        else:
            self.heat_exchanger_ufactor_times_area_value = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.control_type = None
        else:
            self.control_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heat_exchanger_setpoint_node_name = None
        else:
            self.heat_exchanger_setpoint_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_temperature_difference_to_activate_heat_exchanger = None
        else:
            self.minimum_temperature_difference_to_activate_heat_exchanger = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heat_transfer_metering_end_use_type = None
        else:
            self.heat_transfer_metering_end_use_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_override_loop_supply_side_inlet_node_name = None
        else:
            self.component_override_loop_supply_side_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_override_loop_demand_side_inlet_node_name = None
        else:
            self.component_override_loop_demand_side_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_override_cooling_control_temperature_mode = None
        else:
            self.component_override_cooling_control_temperature_mode = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.sizing_factor = None
        else:
            self.sizing_factor = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.operation_minimum_temperature_limit = None
        else:
            self.operation_minimum_temperature_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.operation_maximum_temperature_limit = None
        else:
            self.operation_maximum_temperature_limit = vals[i]
        i += 1
        if i >= len(vals):
            return

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `Name`

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')
        self._data["Name"] = value

    @property
    def availability_schedule_name(self):
        """Get availability_schedule_name

        Returns:
            str: the value of `availability_schedule_name` or None if not set
        """
        return self._data["Availability Schedule Name"]

    @availability_schedule_name.setter
    def availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Availability Schedule Name`
        Availability schedule name for this system. Schedule value > 0 means the system is available.
        If this field is blank, the system is always available.
        default is that heat exchanger is on

        Args:
            value (str): value for IDD Field `Availability Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `availability_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `availability_schedule_name`')
        self._data["Availability Schedule Name"] = value

    @property
    def loop_demand_side_inlet_node_name(self):
        """Get loop_demand_side_inlet_node_name

        Returns:
            str: the value of `loop_demand_side_inlet_node_name` or None if not set
        """
        return self._data["Loop Demand Side Inlet Node Name"]

    @loop_demand_side_inlet_node_name.setter
    def loop_demand_side_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Loop Demand Side Inlet Node Name`
        This connection is to the demand side of a loop and is the inlet to the heat exchanger

        Args:
            value (str): value for IDD Field `Loop Demand Side Inlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `loop_demand_side_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `loop_demand_side_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `loop_demand_side_inlet_node_name`')
        self._data["Loop Demand Side Inlet Node Name"] = value

    @property
    def loop_demand_side_outlet_node_name(self):
        """Get loop_demand_side_outlet_node_name

        Returns:
            str: the value of `loop_demand_side_outlet_node_name` or None if not set
        """
        return self._data["Loop Demand Side Outlet Node Name"]

    @loop_demand_side_outlet_node_name.setter
    def loop_demand_side_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Loop Demand Side Outlet Node Name`
        This connection is to the demand side of a loop

        Args:
            value (str): value for IDD Field `Loop Demand Side Outlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `loop_demand_side_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `loop_demand_side_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `loop_demand_side_outlet_node_name`')
        self._data["Loop Demand Side Outlet Node Name"] = value

    @property
    def loop_demand_side_design_flow_rate(self):
        """Get loop_demand_side_design_flow_rate

        Returns:
            float: the value of `loop_demand_side_design_flow_rate` or None if not set
        """
        return self._data["Loop Demand Side Design Flow Rate"]

    @loop_demand_side_design_flow_rate.setter
    def loop_demand_side_design_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Loop Demand Side Design Flow Rate`

        Args:
            value (float or "Autosize"): value for IDD Field `Loop Demand Side Design Flow Rate`
                Units: m3/s
                IP-Units: gal/min
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Loop Demand Side Design Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `loop_demand_side_design_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `loop_demand_side_design_flow_rate`')
        self._data["Loop Demand Side Design Flow Rate"] = value

    @property
    def loop_supply_side_inlet_node_name(self):
        """Get loop_supply_side_inlet_node_name

        Returns:
            str: the value of `loop_supply_side_inlet_node_name` or None if not set
        """
        return self._data["Loop Supply Side Inlet Node Name"]

    @loop_supply_side_inlet_node_name.setter
    def loop_supply_side_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Loop Supply Side Inlet Node Name`

        Args:
            value (str): value for IDD Field `Loop Supply Side Inlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `loop_supply_side_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `loop_supply_side_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `loop_supply_side_inlet_node_name`')
        self._data["Loop Supply Side Inlet Node Name"] = value

    @property
    def loop_supply_side_outlet_node_name(self):
        """Get loop_supply_side_outlet_node_name

        Returns:
            str: the value of `loop_supply_side_outlet_node_name` or None if not set
        """
        return self._data["Loop Supply Side Outlet Node Name"]

    @loop_supply_side_outlet_node_name.setter
    def loop_supply_side_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Loop Supply Side Outlet Node Name`

        Args:
            value (str): value for IDD Field `Loop Supply Side Outlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `loop_supply_side_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `loop_supply_side_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `loop_supply_side_outlet_node_name`')
        self._data["Loop Supply Side Outlet Node Name"] = value

    @property
    def loop_supply_side_design_flow_rate(self):
        """Get loop_supply_side_design_flow_rate

        Returns:
            float: the value of `loop_supply_side_design_flow_rate` or None if not set
        """
        return self._data["Loop Supply Side Design Flow Rate"]

    @loop_supply_side_design_flow_rate.setter
    def loop_supply_side_design_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Loop Supply Side Design Flow Rate`

        Args:
            value (float or "Autosize"): value for IDD Field `Loop Supply Side Design Flow Rate`
                Units: m3/s
                IP-Units: gal/min
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Loop Supply Side Design Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `loop_supply_side_design_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `loop_supply_side_design_flow_rate`')
        self._data["Loop Supply Side Design Flow Rate"] = value

    @property
    def heat_exchange_model_type(self):
        """Get heat_exchange_model_type

        Returns:
            str: the value of `heat_exchange_model_type` or None if not set
        """
        return self._data["Heat Exchange Model Type"]

    @heat_exchange_model_type.setter
    def heat_exchange_model_type(self, value="Ideal"):
        """  Corresponds to IDD Field `Heat Exchange Model Type`

        Args:
            value (str): value for IDD Field `Heat Exchange Model Type`
                Accepted values are:
                      - CrossFlowBothUnMixed
                      - CrossFlowBothMixed
                      - CrossFlowSupplyMixedDemandUnMixed
                      - CrossFlowSupplyUnMixedDemandMixed
                      - ParallelFlow
                      - CounterFlow
                      - Ideal
                Default value: Ideal
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `heat_exchange_model_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heat_exchange_model_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `heat_exchange_model_type`')
            vals = {}
            vals["crossflowbothunmixed"] = "CrossFlowBothUnMixed"
            vals["crossflowbothmixed"] = "CrossFlowBothMixed"
            vals["crossflowsupplymixeddemandunmixed"] = "CrossFlowSupplyMixedDemandUnMixed"
            vals["crossflowsupplyunmixeddemandmixed"] = "CrossFlowSupplyUnMixedDemandMixed"
            vals["parallelflow"] = "ParallelFlow"
            vals["counterflow"] = "CounterFlow"
            vals["ideal"] = "Ideal"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `heat_exchange_model_type`'.format(value))
            value = vals[value_lower]
        self._data["Heat Exchange Model Type"] = value

    @property
    def heat_exchanger_ufactor_times_area_value(self):
        """Get heat_exchanger_ufactor_times_area_value

        Returns:
            float: the value of `heat_exchanger_ufactor_times_area_value` or None if not set
        """
        return self._data["Heat Exchanger U-Factor Times Area Value"]

    @heat_exchanger_ufactor_times_area_value.setter
    def heat_exchanger_ufactor_times_area_value(self, value=None):
        """  Corresponds to IDD Field `Heat Exchanger U-Factor Times Area Value`

        Args:
            value (float or "Autosize"): value for IDD Field `Heat Exchanger U-Factor Times Area Value`
                Units: W/k
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Heat Exchanger U-Factor Times Area Value"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `heat_exchanger_ufactor_times_area_value`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `heat_exchanger_ufactor_times_area_value`')
        self._data["Heat Exchanger U-Factor Times Area Value"] = value

    @property
    def control_type(self):
        """Get control_type

        Returns:
            str: the value of `control_type` or None if not set
        """
        return self._data["Control Type"]

    @control_type.setter
    def control_type(self, value="UncontrolledOn"):
        """  Corresponds to IDD Field `Control Type`

        Args:
            value (str): value for IDD Field `Control Type`
                Accepted values are:
                      - UncontrolledOn
                      - OperationSchemeModulated
                      - OperationSchemeOnOff
                      - HeatingSetpointModulated
                      - HeatingSetpointOnOff
                      - CoolingSetpointModulated
                      - CoolingSetpointOnOff
                      - DualDeadbandSetpointModulated
                      - DualDeadbandSetpointOnOff
                      - CoolingDifferentialOnOff
                      - CoolingSetpointOnOffWithComponentOverride
                Default value: UncontrolledOn
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `control_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `control_type`')
            vals = {}
            vals["uncontrolledon"] = "UncontrolledOn"
            vals["operationschememodulated"] = "OperationSchemeModulated"
            vals["operationschemeonoff"] = "OperationSchemeOnOff"
            vals["heatingsetpointmodulated"] = "HeatingSetpointModulated"
            vals["heatingsetpointonoff"] = "HeatingSetpointOnOff"
            vals["coolingsetpointmodulated"] = "CoolingSetpointModulated"
            vals["coolingsetpointonoff"] = "CoolingSetpointOnOff"
            vals["dualdeadbandsetpointmodulated"] = "DualDeadbandSetpointModulated"
            vals["dualdeadbandsetpointonoff"] = "DualDeadbandSetpointOnOff"
            vals["coolingdifferentialonoff"] = "CoolingDifferentialOnOff"
            vals["coolingsetpointonoffwithcomponentoverride"] = "CoolingSetpointOnOffWithComponentOverride"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `control_type`'.format(value))
            value = vals[value_lower]
        self._data["Control Type"] = value

    @property
    def heat_exchanger_setpoint_node_name(self):
        """Get heat_exchanger_setpoint_node_name

        Returns:
            str: the value of `heat_exchanger_setpoint_node_name` or None if not set
        """
        return self._data["Heat Exchanger Setpoint Node Name"]

    @heat_exchanger_setpoint_node_name.setter
    def heat_exchanger_setpoint_node_name(self, value=None):
        """  Corresponds to IDD Field `Heat Exchanger Setpoint Node Name`
        Setpoint node is needed with any Control Type that is "*Setpoint*"

        Args:
            value (str): value for IDD Field `Heat Exchanger Setpoint Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `heat_exchanger_setpoint_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heat_exchanger_setpoint_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `heat_exchanger_setpoint_node_name`')
        self._data["Heat Exchanger Setpoint Node Name"] = value

    @property
    def minimum_temperature_difference_to_activate_heat_exchanger(self):
        """Get minimum_temperature_difference_to_activate_heat_exchanger

        Returns:
            float: the value of `minimum_temperature_difference_to_activate_heat_exchanger` or None if not set
        """
        return self._data["Minimum Temperature Difference to Activate Heat Exchanger"]

    @minimum_temperature_difference_to_activate_heat_exchanger.setter
    def minimum_temperature_difference_to_activate_heat_exchanger(self, value=0.01):
        """  Corresponds to IDD Field `Minimum Temperature Difference to Activate Heat Exchanger`
        Tolerance between control temperatures used to determine if heat exchanger should run.

        Args:
            value (float): value for IDD Field `Minimum Temperature Difference to Activate Heat Exchanger`
                Units: deltaC
                Default value: 0.01
                value >= 0.0
                value <= 50.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `minimum_temperature_difference_to_activate_heat_exchanger`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `minimum_temperature_difference_to_activate_heat_exchanger`')
            if value > 50.0:
                raise ValueError('value need to be smaller 50.0 '
                                 'for field `minimum_temperature_difference_to_activate_heat_exchanger`')
        self._data["Minimum Temperature Difference to Activate Heat Exchanger"] = value

    @property
    def heat_transfer_metering_end_use_type(self):
        """Get heat_transfer_metering_end_use_type

        Returns:
            str: the value of `heat_transfer_metering_end_use_type` or None if not set
        """
        return self._data["Heat Transfer Metering End Use Type"]

    @heat_transfer_metering_end_use_type.setter
    def heat_transfer_metering_end_use_type(self, value="LoopToLoop"):
        """  Corresponds to IDD Field `Heat Transfer Metering End Use Type`
        This feild controls end use reporting for heat transfer meters

        Args:
            value (str): value for IDD Field `Heat Transfer Metering End Use Type`
                Accepted values are:
                      - FreeCooling
                      - HeatRecovery
                      - HeatRejection
                      - HeatRecoveryForCooling
                      - HeatRecoveryForHeating
                      - LoopToLoop
                Default value: LoopToLoop
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `heat_transfer_metering_end_use_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heat_transfer_metering_end_use_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `heat_transfer_metering_end_use_type`')
            vals = {}
            vals["freecooling"] = "FreeCooling"
            vals["heatrecovery"] = "HeatRecovery"
            vals["heatrejection"] = "HeatRejection"
            vals["heatrecoveryforcooling"] = "HeatRecoveryForCooling"
            vals["heatrecoveryforheating"] = "HeatRecoveryForHeating"
            vals["looptoloop"] = "LoopToLoop"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `heat_transfer_metering_end_use_type`'.format(value))
            value = vals[value_lower]
        self._data["Heat Transfer Metering End Use Type"] = value

    @property
    def component_override_loop_supply_side_inlet_node_name(self):
        """Get component_override_loop_supply_side_inlet_node_name

        Returns:
            str: the value of `component_override_loop_supply_side_inlet_node_name` or None if not set
        """
        return self._data["Component Override Loop Supply Side Inlet Node Name"]

    @component_override_loop_supply_side_inlet_node_name.setter
    def component_override_loop_supply_side_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Component Override Loop Supply Side Inlet Node Name`
        This field is only used if Control Type is set to CoolingSetpointOnOffWithComponentOverride

        Args:
            value (str): value for IDD Field `Component Override Loop Supply Side Inlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_override_loop_supply_side_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_override_loop_supply_side_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_override_loop_supply_side_inlet_node_name`')
        self._data["Component Override Loop Supply Side Inlet Node Name"] = value

    @property
    def component_override_loop_demand_side_inlet_node_name(self):
        """Get component_override_loop_demand_side_inlet_node_name

        Returns:
            str: the value of `component_override_loop_demand_side_inlet_node_name` or None if not set
        """
        return self._data["Component Override Loop Demand Side Inlet Node Name"]

    @component_override_loop_demand_side_inlet_node_name.setter
    def component_override_loop_demand_side_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Component Override Loop Demand Side Inlet Node Name`
        This field is only used if Control Type is set to CoolingSetpointOnOffWithComponentOverride

        Args:
            value (str): value for IDD Field `Component Override Loop Demand Side Inlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_override_loop_demand_side_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_override_loop_demand_side_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_override_loop_demand_side_inlet_node_name`')
        self._data["Component Override Loop Demand Side Inlet Node Name"] = value

    @property
    def component_override_cooling_control_temperature_mode(self):
        """Get component_override_cooling_control_temperature_mode

        Returns:
            str: the value of `component_override_cooling_control_temperature_mode` or None if not set
        """
        return self._data["Component Override Cooling Control Temperature Mode"]

    @component_override_cooling_control_temperature_mode.setter
    def component_override_cooling_control_temperature_mode(self, value="Loop"):
        """  Corresponds to IDD Field `Component Override Cooling Control Temperature Mode`
        This field is only used if Control Type is set to CoolingSetpointOnOffWithComponentOverride

        Args:
            value (str): value for IDD Field `Component Override Cooling Control Temperature Mode`
                Accepted values are:
                      - WetBulbTemperature
                      - DryBulbTemperature
                      - Loop
                Default value: Loop
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_override_cooling_control_temperature_mode`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_override_cooling_control_temperature_mode`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_override_cooling_control_temperature_mode`')
            vals = {}
            vals["wetbulbtemperature"] = "WetBulbTemperature"
            vals["drybulbtemperature"] = "DryBulbTemperature"
            vals["loop"] = "Loop"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `component_override_cooling_control_temperature_mode`'.format(value))
            value = vals[value_lower]
        self._data["Component Override Cooling Control Temperature Mode"] = value

    @property
    def sizing_factor(self):
        """Get sizing_factor

        Returns:
            float: the value of `sizing_factor` or None if not set
        """
        return self._data["Sizing Factor"]

    @sizing_factor.setter
    def sizing_factor(self, value=1.0):
        """  Corresponds to IDD Field `Sizing Factor`
        Multiplies the autosized flow rates for this device

        Args:
            value (float): value for IDD Field `Sizing Factor`
                Default value: 1.0
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `sizing_factor`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `sizing_factor`')
        self._data["Sizing Factor"] = value

    @property
    def operation_minimum_temperature_limit(self):
        """Get operation_minimum_temperature_limit

        Returns:
            float: the value of `operation_minimum_temperature_limit` or None if not set
        """
        return self._data["Operation Minimum Temperature Limit"]

    @operation_minimum_temperature_limit.setter
    def operation_minimum_temperature_limit(self, value=None):
        """  Corresponds to IDD Field `Operation Minimum Temperature Limit`
        Lower limit on inlet temperatures, heat exchanger will not operate if either inlet is below this limit

        Args:
            value (float): value for IDD Field `Operation Minimum Temperature Limit`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `operation_minimum_temperature_limit`'.format(value))
        self._data["Operation Minimum Temperature Limit"] = value

    @property
    def operation_maximum_temperature_limit(self):
        """Get operation_maximum_temperature_limit

        Returns:
            float: the value of `operation_maximum_temperature_limit` or None if not set
        """
        return self._data["Operation Maximum Temperature Limit"]

    @operation_maximum_temperature_limit.setter
    def operation_maximum_temperature_limit(self, value=None):
        """  Corresponds to IDD Field `Operation Maximum Temperature Limit`
        Upper limit on inlet temperatures, heat exchanger will not operate if either inlet is above this limit

        Args:
            value (float): value for IDD Field `Operation Maximum Temperature Limit`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `operation_maximum_temperature_limit`'.format(value))
        self._data["Operation Maximum Temperature Limit"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
        return good

    @classmethod
    def _to_str(cls, value):
        """ Represents values either as string or None values as empty string

        Args:
            value: a value
        """
        if value is None:
            return ''
        else:
            return str(value)

    def export(self):
        """ Export values of data object as list of strings"""
        out = []
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])