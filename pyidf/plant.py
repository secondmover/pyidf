from collections import OrderedDict

class TemperingValve(object):
    """ Corresponds to IDD object `TemperingValve`
        Temperature-controlled diversion valve used to divert flow around one or more plant
        components such as a hot water heater. It can only be used on one of two branches
        between a Splitter and a Mixer.
    
    """
    internal_name = "TemperingValve"
    field_count = 6
    required_fields = ["Name", "Inlet Node Name", "Outlet Node Name", "Stream 2 Source Node Name", "Temperature Setpoint Node Name", "Pump Outlet Node Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `TemperingValve`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Inlet Node Name"] = None
        self._data["Outlet Node Name"] = None
        self._data["Stream 2 Source Node Name"] = None
        self._data["Temperature Setpoint Node Name"] = None
        self._data["Pump Outlet Node Name"] = None
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
            self.stream_2_source_node_name = None
        else:
            self.stream_2_source_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.temperature_setpoint_node_name = None
        else:
            self.temperature_setpoint_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pump_outlet_node_name = None
        else:
            self.pump_outlet_node_name = vals[i]
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
        Name of a Node

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
        Name of a Node

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
    def stream_2_source_node_name(self):
        """Get stream_2_source_node_name

        Returns:
            str: the value of `stream_2_source_node_name` or None if not set
        """
        return self._data["Stream 2 Source Node Name"]

    @stream_2_source_node_name.setter
    def stream_2_source_node_name(self, value=None):
        """  Corresponds to IDD Field `Stream 2 Source Node Name`
        Name of a Node

        Args:
            value (str): value for IDD Field `Stream 2 Source Node Name`
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
                                 'for field `stream_2_source_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `stream_2_source_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `stream_2_source_node_name`')
        self._data["Stream 2 Source Node Name"] = value

    @property
    def temperature_setpoint_node_name(self):
        """Get temperature_setpoint_node_name

        Returns:
            str: the value of `temperature_setpoint_node_name` or None if not set
        """
        return self._data["Temperature Setpoint Node Name"]

    @temperature_setpoint_node_name.setter
    def temperature_setpoint_node_name(self, value=None):
        """  Corresponds to IDD Field `Temperature Setpoint Node Name`
        Name of a Node

        Args:
            value (str): value for IDD Field `Temperature Setpoint Node Name`
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
                                 'for field `temperature_setpoint_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `temperature_setpoint_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `temperature_setpoint_node_name`')
        self._data["Temperature Setpoint Node Name"] = value

    @property
    def pump_outlet_node_name(self):
        """Get pump_outlet_node_name

        Returns:
            str: the value of `pump_outlet_node_name` or None if not set
        """
        return self._data["Pump Outlet Node Name"]

    @pump_outlet_node_name.setter
    def pump_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Pump Outlet Node Name`

        Args:
            value (str): value for IDD Field `Pump Outlet Node Name`
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
                                 'for field `pump_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `pump_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `pump_outlet_node_name`')
        self._data["Pump Outlet Node Name"] = value

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

class PlantLoop(object):
    """ Corresponds to IDD object `PlantLoop`
        Defines a central plant loop.
    
    """
    internal_name = "PlantLoop"
    field_count = 23
    required_fields = ["Name", "Fluid Type", "Plant Equipment Operation Scheme Name", "Loop Temperature Setpoint Node Name", "Maximum Loop Temperature", "Minimum Loop Temperature", "Maximum Loop Flow Rate", "Plant Side Inlet Node Name", "Plant Side Outlet Node Name", "Plant Side Branch List Name", "Demand Side Inlet Node Name", "Demand Side Outlet Node Name", "Demand Side Branch List Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `PlantLoop`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Fluid Type"] = None
        self._data["User Defined Fluid Type"] = None
        self._data["Plant Equipment Operation Scheme Name"] = None
        self._data["Loop Temperature Setpoint Node Name"] = None
        self._data["Maximum Loop Temperature"] = None
        self._data["Minimum Loop Temperature"] = None
        self._data["Maximum Loop Flow Rate"] = None
        self._data["Minimum Loop Flow Rate"] = None
        self._data["Plant Loop Volume"] = None
        self._data["Plant Side Inlet Node Name"] = None
        self._data["Plant Side Outlet Node Name"] = None
        self._data["Plant Side Branch List Name"] = None
        self._data["Plant Side Connector List Name"] = None
        self._data["Demand Side Inlet Node Name"] = None
        self._data["Demand Side Outlet Node Name"] = None
        self._data["Demand Side Branch List Name"] = None
        self._data["Demand Side Connector List Name"] = None
        self._data["Load Distribution Scheme"] = None
        self._data["Availability Manager List Name"] = None
        self._data["Plant Loop Demand Calculation Scheme"] = None
        self._data["Common Pipe Simulation"] = None
        self._data["Pressure Simulation Type"] = None
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
            self.fluid_type = None
        else:
            self.fluid_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.user_defined_fluid_type = None
        else:
            self.user_defined_fluid_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.plant_equipment_operation_scheme_name = None
        else:
            self.plant_equipment_operation_scheme_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.loop_temperature_setpoint_node_name = None
        else:
            self.loop_temperature_setpoint_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_loop_temperature = None
        else:
            self.maximum_loop_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_loop_temperature = None
        else:
            self.minimum_loop_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_loop_flow_rate = None
        else:
            self.maximum_loop_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_loop_flow_rate = None
        else:
            self.minimum_loop_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.plant_loop_volume = None
        else:
            self.plant_loop_volume = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.plant_side_inlet_node_name = None
        else:
            self.plant_side_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.plant_side_outlet_node_name = None
        else:
            self.plant_side_outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.plant_side_branch_list_name = None
        else:
            self.plant_side_branch_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.plant_side_connector_list_name = None
        else:
            self.plant_side_connector_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.demand_side_inlet_node_name = None
        else:
            self.demand_side_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.demand_side_outlet_node_name = None
        else:
            self.demand_side_outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.demand_side_branch_list_name = None
        else:
            self.demand_side_branch_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.demand_side_connector_list_name = None
        else:
            self.demand_side_connector_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.load_distribution_scheme = None
        else:
            self.load_distribution_scheme = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.availability_manager_list_name = None
        else:
            self.availability_manager_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.plant_loop_demand_calculation_scheme = None
        else:
            self.plant_loop_demand_calculation_scheme = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.common_pipe_simulation = None
        else:
            self.common_pipe_simulation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pressure_simulation_type = None
        else:
            self.pressure_simulation_type = vals[i]
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
    def fluid_type(self):
        """Get fluid_type

        Returns:
            str: the value of `fluid_type` or None if not set
        """
        return self._data["Fluid Type"]

    @fluid_type.setter
    def fluid_type(self, value="Water"):
        """  Corresponds to IDD Field `Fluid Type`

        Args:
            value (str): value for IDD Field `Fluid Type`
                Accepted values are:
                      - Water
                      - Steam
                      - UserDefinedFluidType
                Default value: Water
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
                                 'for field `fluid_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `fluid_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `fluid_type`')
            vals = {}
            vals["water"] = "Water"
            vals["steam"] = "Steam"
            vals["userdefinedfluidtype"] = "UserDefinedFluidType"
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
                                     'field `fluid_type`'.format(value))
            value = vals[value_lower]
        self._data["Fluid Type"] = value

    @property
    def user_defined_fluid_type(self):
        """Get user_defined_fluid_type

        Returns:
            str: the value of `user_defined_fluid_type` or None if not set
        """
        return self._data["User Defined Fluid Type"]

    @user_defined_fluid_type.setter
    def user_defined_fluid_type(self, value=None):
        """  Corresponds to IDD Field `User Defined Fluid Type`
        This field is only required when Fluid Type is UserDefinedFluidType

        Args:
            value (str): value for IDD Field `User Defined Fluid Type`
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
                                 'for field `user_defined_fluid_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `user_defined_fluid_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `user_defined_fluid_type`')
        self._data["User Defined Fluid Type"] = value

    @property
    def plant_equipment_operation_scheme_name(self):
        """Get plant_equipment_operation_scheme_name

        Returns:
            str: the value of `plant_equipment_operation_scheme_name` or None if not set
        """
        return self._data["Plant Equipment Operation Scheme Name"]

    @plant_equipment_operation_scheme_name.setter
    def plant_equipment_operation_scheme_name(self, value=None):
        """  Corresponds to IDD Field `Plant Equipment Operation Scheme Name`

        Args:
            value (str): value for IDD Field `Plant Equipment Operation Scheme Name`
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
                                 'for field `plant_equipment_operation_scheme_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `plant_equipment_operation_scheme_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `plant_equipment_operation_scheme_name`')
        self._data["Plant Equipment Operation Scheme Name"] = value

    @property
    def loop_temperature_setpoint_node_name(self):
        """Get loop_temperature_setpoint_node_name

        Returns:
            str: the value of `loop_temperature_setpoint_node_name` or None if not set
        """
        return self._data["Loop Temperature Setpoint Node Name"]

    @loop_temperature_setpoint_node_name.setter
    def loop_temperature_setpoint_node_name(self, value=None):
        """  Corresponds to IDD Field `Loop Temperature Setpoint Node Name`

        Args:
            value (str): value for IDD Field `Loop Temperature Setpoint Node Name`
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
                                 'for field `loop_temperature_setpoint_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `loop_temperature_setpoint_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `loop_temperature_setpoint_node_name`')
        self._data["Loop Temperature Setpoint Node Name"] = value

    @property
    def maximum_loop_temperature(self):
        """Get maximum_loop_temperature

        Returns:
            float: the value of `maximum_loop_temperature` or None if not set
        """
        return self._data["Maximum Loop Temperature"]

    @maximum_loop_temperature.setter
    def maximum_loop_temperature(self, value=None):
        """  Corresponds to IDD Field `Maximum Loop Temperature`

        Args:
            value (float): value for IDD Field `Maximum Loop Temperature`
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
                                 'for field `maximum_loop_temperature`'.format(value))
        self._data["Maximum Loop Temperature"] = value

    @property
    def minimum_loop_temperature(self):
        """Get minimum_loop_temperature

        Returns:
            float: the value of `minimum_loop_temperature` or None if not set
        """
        return self._data["Minimum Loop Temperature"]

    @minimum_loop_temperature.setter
    def minimum_loop_temperature(self, value=None):
        """  Corresponds to IDD Field `Minimum Loop Temperature`

        Args:
            value (float): value for IDD Field `Minimum Loop Temperature`
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
                                 'for field `minimum_loop_temperature`'.format(value))
        self._data["Minimum Loop Temperature"] = value

    @property
    def maximum_loop_flow_rate(self):
        """Get maximum_loop_flow_rate

        Returns:
            float: the value of `maximum_loop_flow_rate` or None if not set
        """
        return self._data["Maximum Loop Flow Rate"]

    @maximum_loop_flow_rate.setter
    def maximum_loop_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Maximum Loop Flow Rate`

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Loop Flow Rate`
                Units: m3/s
                IP-Units: gal/min
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Maximum Loop Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_loop_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `maximum_loop_flow_rate`')
        self._data["Maximum Loop Flow Rate"] = value

    @property
    def minimum_loop_flow_rate(self):
        """Get minimum_loop_flow_rate

        Returns:
            float: the value of `minimum_loop_flow_rate` or None if not set
        """
        return self._data["Minimum Loop Flow Rate"]

    @minimum_loop_flow_rate.setter
    def minimum_loop_flow_rate(self, value=0.0):
        """  Corresponds to IDD Field `Minimum Loop Flow Rate`

        Args:
            value (float): value for IDD Field `Minimum Loop Flow Rate`
                Units: m3/s
                IP-Units: gal/min
                Default value: 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `minimum_loop_flow_rate`'.format(value))
        self._data["Minimum Loop Flow Rate"] = value

    @property
    def plant_loop_volume(self):
        """Get plant_loop_volume

        Returns:
            float: the value of `plant_loop_volume` or None if not set
        """
        return self._data["Plant Loop Volume"]

    @plant_loop_volume.setter
    def plant_loop_volume(self, value="Autocalculate"):
        """  Corresponds to IDD Field `Plant Loop Volume`

        Args:
            value (float or "Autocalculate"): value for IDD Field `Plant Loop Volume`
                Units: m3
                IP-Units: gal
                Default value: "Autocalculate"
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
                    self._data["Plant Loop Volume"] = "Autocalculate"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `plant_loop_volume`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `plant_loop_volume`')
        self._data["Plant Loop Volume"] = value

    @property
    def plant_side_inlet_node_name(self):
        """Get plant_side_inlet_node_name

        Returns:
            str: the value of `plant_side_inlet_node_name` or None if not set
        """
        return self._data["Plant Side Inlet Node Name"]

    @plant_side_inlet_node_name.setter
    def plant_side_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Plant Side Inlet Node Name`

        Args:
            value (str): value for IDD Field `Plant Side Inlet Node Name`
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
                                 'for field `plant_side_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `plant_side_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `plant_side_inlet_node_name`')
        self._data["Plant Side Inlet Node Name"] = value

    @property
    def plant_side_outlet_node_name(self):
        """Get plant_side_outlet_node_name

        Returns:
            str: the value of `plant_side_outlet_node_name` or None if not set
        """
        return self._data["Plant Side Outlet Node Name"]

    @plant_side_outlet_node_name.setter
    def plant_side_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Plant Side Outlet Node Name`

        Args:
            value (str): value for IDD Field `Plant Side Outlet Node Name`
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
                                 'for field `plant_side_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `plant_side_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `plant_side_outlet_node_name`')
        self._data["Plant Side Outlet Node Name"] = value

    @property
    def plant_side_branch_list_name(self):
        """Get plant_side_branch_list_name

        Returns:
            str: the value of `plant_side_branch_list_name` or None if not set
        """
        return self._data["Plant Side Branch List Name"]

    @plant_side_branch_list_name.setter
    def plant_side_branch_list_name(self, value=None):
        """  Corresponds to IDD Field `Plant Side Branch List Name`

        Args:
            value (str): value for IDD Field `Plant Side Branch List Name`
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
                                 'for field `plant_side_branch_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `plant_side_branch_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `plant_side_branch_list_name`')
        self._data["Plant Side Branch List Name"] = value

    @property
    def plant_side_connector_list_name(self):
        """Get plant_side_connector_list_name

        Returns:
            str: the value of `plant_side_connector_list_name` or None if not set
        """
        return self._data["Plant Side Connector List Name"]

    @plant_side_connector_list_name.setter
    def plant_side_connector_list_name(self, value=None):
        """  Corresponds to IDD Field `Plant Side Connector List Name`

        Args:
            value (str): value for IDD Field `Plant Side Connector List Name`
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
                                 'for field `plant_side_connector_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `plant_side_connector_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `plant_side_connector_list_name`')
        self._data["Plant Side Connector List Name"] = value

    @property
    def demand_side_inlet_node_name(self):
        """Get demand_side_inlet_node_name

        Returns:
            str: the value of `demand_side_inlet_node_name` or None if not set
        """
        return self._data["Demand Side Inlet Node Name"]

    @demand_side_inlet_node_name.setter
    def demand_side_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Demand Side Inlet Node Name`

        Args:
            value (str): value for IDD Field `Demand Side Inlet Node Name`
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
                                 'for field `demand_side_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `demand_side_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `demand_side_inlet_node_name`')
        self._data["Demand Side Inlet Node Name"] = value

    @property
    def demand_side_outlet_node_name(self):
        """Get demand_side_outlet_node_name

        Returns:
            str: the value of `demand_side_outlet_node_name` or None if not set
        """
        return self._data["Demand Side Outlet Node Name"]

    @demand_side_outlet_node_name.setter
    def demand_side_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Demand Side Outlet Node Name`

        Args:
            value (str): value for IDD Field `Demand Side Outlet Node Name`
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
                                 'for field `demand_side_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `demand_side_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `demand_side_outlet_node_name`')
        self._data["Demand Side Outlet Node Name"] = value

    @property
    def demand_side_branch_list_name(self):
        """Get demand_side_branch_list_name

        Returns:
            str: the value of `demand_side_branch_list_name` or None if not set
        """
        return self._data["Demand Side Branch List Name"]

    @demand_side_branch_list_name.setter
    def demand_side_branch_list_name(self, value=None):
        """  Corresponds to IDD Field `Demand Side Branch List Name`

        Args:
            value (str): value for IDD Field `Demand Side Branch List Name`
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
                                 'for field `demand_side_branch_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `demand_side_branch_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `demand_side_branch_list_name`')
        self._data["Demand Side Branch List Name"] = value

    @property
    def demand_side_connector_list_name(self):
        """Get demand_side_connector_list_name

        Returns:
            str: the value of `demand_side_connector_list_name` or None if not set
        """
        return self._data["Demand Side Connector List Name"]

    @demand_side_connector_list_name.setter
    def demand_side_connector_list_name(self, value=None):
        """  Corresponds to IDD Field `Demand Side Connector List Name`

        Args:
            value (str): value for IDD Field `Demand Side Connector List Name`
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
                                 'for field `demand_side_connector_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `demand_side_connector_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `demand_side_connector_list_name`')
        self._data["Demand Side Connector List Name"] = value

    @property
    def load_distribution_scheme(self):
        """Get load_distribution_scheme

        Returns:
            str: the value of `load_distribution_scheme` or None if not set
        """
        return self._data["Load Distribution Scheme"]

    @load_distribution_scheme.setter
    def load_distribution_scheme(self, value="SequentialLoad"):
        """  Corresponds to IDD Field `Load Distribution Scheme`

        Args:
            value (str): value for IDD Field `Load Distribution Scheme`
                Accepted values are:
                      - Optimal
                      - SequentialLoad
                      - UniformLoad
                      - UniformPLR
                      - SequentialUniformPLR
                Default value: SequentialLoad
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
                                 'for field `load_distribution_scheme`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `load_distribution_scheme`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `load_distribution_scheme`')
            vals = {}
            vals["optimal"] = "Optimal"
            vals["sequentialload"] = "SequentialLoad"
            vals["uniformload"] = "UniformLoad"
            vals["uniformplr"] = "UniformPLR"
            vals["sequentialuniformplr"] = "SequentialUniformPLR"
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
                                     'field `load_distribution_scheme`'.format(value))
            value = vals[value_lower]
        self._data["Load Distribution Scheme"] = value

    @property
    def availability_manager_list_name(self):
        """Get availability_manager_list_name

        Returns:
            str: the value of `availability_manager_list_name` or None if not set
        """
        return self._data["Availability Manager List Name"]

    @availability_manager_list_name.setter
    def availability_manager_list_name(self, value=None):
        """  Corresponds to IDD Field `Availability Manager List Name`

        Args:
            value (str): value for IDD Field `Availability Manager List Name`
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
                                 'for field `availability_manager_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `availability_manager_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `availability_manager_list_name`')
        self._data["Availability Manager List Name"] = value

    @property
    def plant_loop_demand_calculation_scheme(self):
        """Get plant_loop_demand_calculation_scheme

        Returns:
            str: the value of `plant_loop_demand_calculation_scheme` or None if not set
        """
        return self._data["Plant Loop Demand Calculation Scheme"]

    @plant_loop_demand_calculation_scheme.setter
    def plant_loop_demand_calculation_scheme(self, value="SingleSetpoint"):
        """  Corresponds to IDD Field `Plant Loop Demand Calculation Scheme`

        Args:
            value (str): value for IDD Field `Plant Loop Demand Calculation Scheme`
                Accepted values are:
                      - SingleSetpoint
                      - DualSetpointDeadband
                Default value: SingleSetpoint
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
                                 'for field `plant_loop_demand_calculation_scheme`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `plant_loop_demand_calculation_scheme`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `plant_loop_demand_calculation_scheme`')
            vals = {}
            vals["singlesetpoint"] = "SingleSetpoint"
            vals["dualsetpointdeadband"] = "DualSetpointDeadband"
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
                                     'field `plant_loop_demand_calculation_scheme`'.format(value))
            value = vals[value_lower]
        self._data["Plant Loop Demand Calculation Scheme"] = value

    @property
    def common_pipe_simulation(self):
        """Get common_pipe_simulation

        Returns:
            str: the value of `common_pipe_simulation` or None if not set
        """
        return self._data["Common Pipe Simulation"]

    @common_pipe_simulation.setter
    def common_pipe_simulation(self, value="None"):
        """  Corresponds to IDD Field `Common Pipe Simulation`
        Specifies a primary-secondary loop configuration. The plant side is the
        primary loop, and the demand side is the secondary loop.
        A secondary supply pump is required on the demand side.
        None = Primary-only, no secondary simulation
        CommonPipe = Primary-secondary with no temperature control at primary-secondary interface
        TwoWayCommonPipe = Primary-secondary with control of secondary supply temperature or
        primary return temperature (requires a setpoint be placed on the
        plant side or demand side inlet node).

        Args:
            value (str): value for IDD Field `Common Pipe Simulation`
                Accepted values are:
                      - CommonPipe
                      - TwoWayCommonPipe
                      - None
                Default value: None
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
                                 'for field `common_pipe_simulation`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `common_pipe_simulation`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `common_pipe_simulation`')
            vals = {}
            vals["commonpipe"] = "CommonPipe"
            vals["twowaycommonpipe"] = "TwoWayCommonPipe"
            vals["none"] = "None"
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
                                     'field `common_pipe_simulation`'.format(value))
            value = vals[value_lower]
        self._data["Common Pipe Simulation"] = value

    @property
    def pressure_simulation_type(self):
        """Get pressure_simulation_type

        Returns:
            str: the value of `pressure_simulation_type` or None if not set
        """
        return self._data["Pressure Simulation Type"]

    @pressure_simulation_type.setter
    def pressure_simulation_type(self, value="None"):
        """  Corresponds to IDD Field `Pressure Simulation Type`

        Args:
            value (str): value for IDD Field `Pressure Simulation Type`
                Accepted values are:
                      - PumpPowerCorrection
                      - LoopFlowCorrection
                      - None
                Default value: None
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
                                 'for field `pressure_simulation_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `pressure_simulation_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `pressure_simulation_type`')
            vals = {}
            vals["pumppowercorrection"] = "PumpPowerCorrection"
            vals["loopflowcorrection"] = "LoopFlowCorrection"
            vals["none"] = "None"
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
                                     'field `pressure_simulation_type`'.format(value))
            value = vals[value_lower]
        self._data["Pressure Simulation Type"] = value

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

class CondenserLoop(object):
    """ Corresponds to IDD object `CondenserLoop`
        Defines a central plant condenser loop. CondenserLoop and PlantLoop are nearly
        identical except some components and operation schemes are applicable to only one
        loop type or the other.
    
    """
    internal_name = "CondenserLoop"
    field_count = 20
    required_fields = ["Name", "Fluid Type", "Condenser Equipment Operation Scheme Name", "Condenser Loop Temperature Setpoint Node Name", "Maximum Loop Temperature", "Minimum Loop Temperature", "Maximum Loop Flow Rate", "Condenser Side Inlet Node Name", "Condenser Side Outlet Node Name", "Condenser Side Branch List Name", "Condenser Side Connector List Name", "Demand Side Inlet Node Name", "Demand Side Outlet Node Name", "Condenser Demand Side Branch List Name", "Condenser Demand Side Connector List Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `CondenserLoop`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Fluid Type"] = None
        self._data["User Defined Fluid Type"] = None
        self._data["Condenser Equipment Operation Scheme Name"] = None
        self._data["Condenser Loop Temperature Setpoint Node Name"] = None
        self._data["Maximum Loop Temperature"] = None
        self._data["Minimum Loop Temperature"] = None
        self._data["Maximum Loop Flow Rate"] = None
        self._data["Minimum Loop Flow Rate"] = None
        self._data["Condenser Loop Volume"] = None
        self._data["Condenser Side Inlet Node Name"] = None
        self._data["Condenser Side Outlet Node Name"] = None
        self._data["Condenser Side Branch List Name"] = None
        self._data["Condenser Side Connector List Name"] = None
        self._data["Demand Side Inlet Node Name"] = None
        self._data["Demand Side Outlet Node Name"] = None
        self._data["Condenser Demand Side Branch List Name"] = None
        self._data["Condenser Demand Side Connector List Name"] = None
        self._data["Load Distribution Scheme"] = None
        self._data["Pressure Simulation Type"] = None
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
            self.fluid_type = None
        else:
            self.fluid_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.user_defined_fluid_type = None
        else:
            self.user_defined_fluid_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.condenser_equipment_operation_scheme_name = None
        else:
            self.condenser_equipment_operation_scheme_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.condenser_loop_temperature_setpoint_node_name = None
        else:
            self.condenser_loop_temperature_setpoint_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_loop_temperature = None
        else:
            self.maximum_loop_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_loop_temperature = None
        else:
            self.minimum_loop_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_loop_flow_rate = None
        else:
            self.maximum_loop_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_loop_flow_rate = None
        else:
            self.minimum_loop_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.condenser_loop_volume = None
        else:
            self.condenser_loop_volume = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.condenser_side_inlet_node_name = None
        else:
            self.condenser_side_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.condenser_side_outlet_node_name = None
        else:
            self.condenser_side_outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.condenser_side_branch_list_name = None
        else:
            self.condenser_side_branch_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.condenser_side_connector_list_name = None
        else:
            self.condenser_side_connector_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.demand_side_inlet_node_name = None
        else:
            self.demand_side_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.demand_side_outlet_node_name = None
        else:
            self.demand_side_outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.condenser_demand_side_branch_list_name = None
        else:
            self.condenser_demand_side_branch_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.condenser_demand_side_connector_list_name = None
        else:
            self.condenser_demand_side_connector_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.load_distribution_scheme = None
        else:
            self.load_distribution_scheme = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pressure_simulation_type = None
        else:
            self.pressure_simulation_type = vals[i]
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
    def fluid_type(self):
        """Get fluid_type

        Returns:
            str: the value of `fluid_type` or None if not set
        """
        return self._data["Fluid Type"]

    @fluid_type.setter
    def fluid_type(self, value="Water"):
        """  Corresponds to IDD Field `Fluid Type`

        Args:
            value (str): value for IDD Field `Fluid Type`
                Accepted values are:
                      - Water
                      - UserDefinedFluidType
                Default value: Water
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
                                 'for field `fluid_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `fluid_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `fluid_type`')
            vals = {}
            vals["water"] = "Water"
            vals["userdefinedfluidtype"] = "UserDefinedFluidType"
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
                                     'field `fluid_type`'.format(value))
            value = vals[value_lower]
        self._data["Fluid Type"] = value

    @property
    def user_defined_fluid_type(self):
        """Get user_defined_fluid_type

        Returns:
            str: the value of `user_defined_fluid_type` or None if not set
        """
        return self._data["User Defined Fluid Type"]

    @user_defined_fluid_type.setter
    def user_defined_fluid_type(self, value=None):
        """  Corresponds to IDD Field `User Defined Fluid Type`
        This field is only required when Fluid Type is UserDefinedFluidType

        Args:
            value (str): value for IDD Field `User Defined Fluid Type`
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
                                 'for field `user_defined_fluid_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `user_defined_fluid_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `user_defined_fluid_type`')
        self._data["User Defined Fluid Type"] = value

    @property
    def condenser_equipment_operation_scheme_name(self):
        """Get condenser_equipment_operation_scheme_name

        Returns:
            str: the value of `condenser_equipment_operation_scheme_name` or None if not set
        """
        return self._data["Condenser Equipment Operation Scheme Name"]

    @condenser_equipment_operation_scheme_name.setter
    def condenser_equipment_operation_scheme_name(self, value=None):
        """  Corresponds to IDD Field `Condenser Equipment Operation Scheme Name`

        Args:
            value (str): value for IDD Field `Condenser Equipment Operation Scheme Name`
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
                                 'for field `condenser_equipment_operation_scheme_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `condenser_equipment_operation_scheme_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `condenser_equipment_operation_scheme_name`')
        self._data["Condenser Equipment Operation Scheme Name"] = value

    @property
    def condenser_loop_temperature_setpoint_node_name(self):
        """Get condenser_loop_temperature_setpoint_node_name

        Returns:
            str: the value of `condenser_loop_temperature_setpoint_node_name` or None if not set
        """
        return self._data["Condenser Loop Temperature Setpoint Node Name"]

    @condenser_loop_temperature_setpoint_node_name.setter
    def condenser_loop_temperature_setpoint_node_name(self, value=None):
        """  Corresponds to IDD Field `Condenser Loop Temperature Setpoint Node Name`

        Args:
            value (str): value for IDD Field `Condenser Loop Temperature Setpoint Node Name`
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
                                 'for field `condenser_loop_temperature_setpoint_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `condenser_loop_temperature_setpoint_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `condenser_loop_temperature_setpoint_node_name`')
        self._data["Condenser Loop Temperature Setpoint Node Name"] = value

    @property
    def maximum_loop_temperature(self):
        """Get maximum_loop_temperature

        Returns:
            float: the value of `maximum_loop_temperature` or None if not set
        """
        return self._data["Maximum Loop Temperature"]

    @maximum_loop_temperature.setter
    def maximum_loop_temperature(self, value=None):
        """  Corresponds to IDD Field `Maximum Loop Temperature`

        Args:
            value (float): value for IDD Field `Maximum Loop Temperature`
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
                                 'for field `maximum_loop_temperature`'.format(value))
        self._data["Maximum Loop Temperature"] = value

    @property
    def minimum_loop_temperature(self):
        """Get minimum_loop_temperature

        Returns:
            float: the value of `minimum_loop_temperature` or None if not set
        """
        return self._data["Minimum Loop Temperature"]

    @minimum_loop_temperature.setter
    def minimum_loop_temperature(self, value=None):
        """  Corresponds to IDD Field `Minimum Loop Temperature`

        Args:
            value (float): value for IDD Field `Minimum Loop Temperature`
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
                                 'for field `minimum_loop_temperature`'.format(value))
        self._data["Minimum Loop Temperature"] = value

    @property
    def maximum_loop_flow_rate(self):
        """Get maximum_loop_flow_rate

        Returns:
            float: the value of `maximum_loop_flow_rate` or None if not set
        """
        return self._data["Maximum Loop Flow Rate"]

    @maximum_loop_flow_rate.setter
    def maximum_loop_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Maximum Loop Flow Rate`

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Loop Flow Rate`
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
                    self._data["Maximum Loop Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_loop_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `maximum_loop_flow_rate`')
        self._data["Maximum Loop Flow Rate"] = value

    @property
    def minimum_loop_flow_rate(self):
        """Get minimum_loop_flow_rate

        Returns:
            float: the value of `minimum_loop_flow_rate` or None if not set
        """
        return self._data["Minimum Loop Flow Rate"]

    @minimum_loop_flow_rate.setter
    def minimum_loop_flow_rate(self, value=0.0):
        """  Corresponds to IDD Field `Minimum Loop Flow Rate`

        Args:
            value (float): value for IDD Field `Minimum Loop Flow Rate`
                Units: m3/s
                IP-Units: gal/min
                Default value: 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `minimum_loop_flow_rate`'.format(value))
        self._data["Minimum Loop Flow Rate"] = value

    @property
    def condenser_loop_volume(self):
        """Get condenser_loop_volume

        Returns:
            float: the value of `condenser_loop_volume` or None if not set
        """
        return self._data["Condenser Loop Volume"]

    @condenser_loop_volume.setter
    def condenser_loop_volume(self, value="Autocalculate"):
        """  Corresponds to IDD Field `Condenser Loop Volume`

        Args:
            value (float or "Autocalculate"): value for IDD Field `Condenser Loop Volume`
                Units: m3
                IP-Units: gal
                Default value: "Autocalculate"
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
                    self._data["Condenser Loop Volume"] = "Autocalculate"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `condenser_loop_volume`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `condenser_loop_volume`')
        self._data["Condenser Loop Volume"] = value

    @property
    def condenser_side_inlet_node_name(self):
        """Get condenser_side_inlet_node_name

        Returns:
            str: the value of `condenser_side_inlet_node_name` or None if not set
        """
        return self._data["Condenser Side Inlet Node Name"]

    @condenser_side_inlet_node_name.setter
    def condenser_side_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Condenser Side Inlet Node Name`

        Args:
            value (str): value for IDD Field `Condenser Side Inlet Node Name`
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
                                 'for field `condenser_side_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `condenser_side_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `condenser_side_inlet_node_name`')
        self._data["Condenser Side Inlet Node Name"] = value

    @property
    def condenser_side_outlet_node_name(self):
        """Get condenser_side_outlet_node_name

        Returns:
            str: the value of `condenser_side_outlet_node_name` or None if not set
        """
        return self._data["Condenser Side Outlet Node Name"]

    @condenser_side_outlet_node_name.setter
    def condenser_side_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Condenser Side Outlet Node Name`

        Args:
            value (str): value for IDD Field `Condenser Side Outlet Node Name`
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
                                 'for field `condenser_side_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `condenser_side_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `condenser_side_outlet_node_name`')
        self._data["Condenser Side Outlet Node Name"] = value

    @property
    def condenser_side_branch_list_name(self):
        """Get condenser_side_branch_list_name

        Returns:
            str: the value of `condenser_side_branch_list_name` or None if not set
        """
        return self._data["Condenser Side Branch List Name"]

    @condenser_side_branch_list_name.setter
    def condenser_side_branch_list_name(self, value=None):
        """  Corresponds to IDD Field `Condenser Side Branch List Name`

        Args:
            value (str): value for IDD Field `Condenser Side Branch List Name`
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
                                 'for field `condenser_side_branch_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `condenser_side_branch_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `condenser_side_branch_list_name`')
        self._data["Condenser Side Branch List Name"] = value

    @property
    def condenser_side_connector_list_name(self):
        """Get condenser_side_connector_list_name

        Returns:
            str: the value of `condenser_side_connector_list_name` or None if not set
        """
        return self._data["Condenser Side Connector List Name"]

    @condenser_side_connector_list_name.setter
    def condenser_side_connector_list_name(self, value=None):
        """  Corresponds to IDD Field `Condenser Side Connector List Name`

        Args:
            value (str): value for IDD Field `Condenser Side Connector List Name`
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
                                 'for field `condenser_side_connector_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `condenser_side_connector_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `condenser_side_connector_list_name`')
        self._data["Condenser Side Connector List Name"] = value

    @property
    def demand_side_inlet_node_name(self):
        """Get demand_side_inlet_node_name

        Returns:
            str: the value of `demand_side_inlet_node_name` or None if not set
        """
        return self._data["Demand Side Inlet Node Name"]

    @demand_side_inlet_node_name.setter
    def demand_side_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Demand Side Inlet Node Name`

        Args:
            value (str): value for IDD Field `Demand Side Inlet Node Name`
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
                                 'for field `demand_side_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `demand_side_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `demand_side_inlet_node_name`')
        self._data["Demand Side Inlet Node Name"] = value

    @property
    def demand_side_outlet_node_name(self):
        """Get demand_side_outlet_node_name

        Returns:
            str: the value of `demand_side_outlet_node_name` or None if not set
        """
        return self._data["Demand Side Outlet Node Name"]

    @demand_side_outlet_node_name.setter
    def demand_side_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Demand Side Outlet Node Name`

        Args:
            value (str): value for IDD Field `Demand Side Outlet Node Name`
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
                                 'for field `demand_side_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `demand_side_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `demand_side_outlet_node_name`')
        self._data["Demand Side Outlet Node Name"] = value

    @property
    def condenser_demand_side_branch_list_name(self):
        """Get condenser_demand_side_branch_list_name

        Returns:
            str: the value of `condenser_demand_side_branch_list_name` or None if not set
        """
        return self._data["Condenser Demand Side Branch List Name"]

    @condenser_demand_side_branch_list_name.setter
    def condenser_demand_side_branch_list_name(self, value=None):
        """  Corresponds to IDD Field `Condenser Demand Side Branch List Name`

        Args:
            value (str): value for IDD Field `Condenser Demand Side Branch List Name`
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
                                 'for field `condenser_demand_side_branch_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `condenser_demand_side_branch_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `condenser_demand_side_branch_list_name`')
        self._data["Condenser Demand Side Branch List Name"] = value

    @property
    def condenser_demand_side_connector_list_name(self):
        """Get condenser_demand_side_connector_list_name

        Returns:
            str: the value of `condenser_demand_side_connector_list_name` or None if not set
        """
        return self._data["Condenser Demand Side Connector List Name"]

    @condenser_demand_side_connector_list_name.setter
    def condenser_demand_side_connector_list_name(self, value=None):
        """  Corresponds to IDD Field `Condenser Demand Side Connector List Name`

        Args:
            value (str): value for IDD Field `Condenser Demand Side Connector List Name`
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
                                 'for field `condenser_demand_side_connector_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `condenser_demand_side_connector_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `condenser_demand_side_connector_list_name`')
        self._data["Condenser Demand Side Connector List Name"] = value

    @property
    def load_distribution_scheme(self):
        """Get load_distribution_scheme

        Returns:
            str: the value of `load_distribution_scheme` or None if not set
        """
        return self._data["Load Distribution Scheme"]

    @load_distribution_scheme.setter
    def load_distribution_scheme(self, value="SequentialLoad"):
        """  Corresponds to IDD Field `Load Distribution Scheme`

        Args:
            value (str): value for IDD Field `Load Distribution Scheme`
                Accepted values are:
                      - Optimal
                      - SequentialLoad
                      - UniformLoad
                      - UniformPLR
                      - SequentialUniformPLR
                Default value: SequentialLoad
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
                                 'for field `load_distribution_scheme`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `load_distribution_scheme`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `load_distribution_scheme`')
            vals = {}
            vals["optimal"] = "Optimal"
            vals["sequentialload"] = "SequentialLoad"
            vals["uniformload"] = "UniformLoad"
            vals["uniformplr"] = "UniformPLR"
            vals["sequentialuniformplr"] = "SequentialUniformPLR"
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
                                     'field `load_distribution_scheme`'.format(value))
            value = vals[value_lower]
        self._data["Load Distribution Scheme"] = value

    @property
    def pressure_simulation_type(self):
        """Get pressure_simulation_type

        Returns:
            str: the value of `pressure_simulation_type` or None if not set
        """
        return self._data["Pressure Simulation Type"]

    @pressure_simulation_type.setter
    def pressure_simulation_type(self, value="None"):
        """  Corresponds to IDD Field `Pressure Simulation Type`

        Args:
            value (str): value for IDD Field `Pressure Simulation Type`
                Accepted values are:
                      - PumpPowerCorrection
                      - LoopFlowCorrection
                      - None
                Default value: None
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
                                 'for field `pressure_simulation_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `pressure_simulation_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `pressure_simulation_type`')
            vals = {}
            vals["pumppowercorrection"] = "PumpPowerCorrection"
            vals["loopflowcorrection"] = "LoopFlowCorrection"
            vals["none"] = "None"
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
                                     'field `pressure_simulation_type`'.format(value))
            value = vals[value_lower]
        self._data["Pressure Simulation Type"] = value

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

class PlantEquipmentList(object):
    """ Corresponds to IDD object `PlantEquipmentList`
        List plant equipment in order of operating priority, 1st in list will be used 1st, etc
        Use only plant equipment in this list.
        If no equipment object types and equipment names are specified, then the corresponding
        PlantEquipmentOperation:* object will assume all available plant equipment for the loop
        should be OFF (not operate) within the specified lower/upper limit.
    
    """
    internal_name = "PlantEquipmentList"
    field_count = 21
    required_fields = ["Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `PlantEquipmentList`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Equipment 1 Object Type"] = None
        self._data["Equipment 1 Name"] = None
        self._data["Equipment 2 Object Type"] = None
        self._data["Equipment 2 Name"] = None
        self._data["Equipment 3 Object Type"] = None
        self._data["Equipment 3 Name"] = None
        self._data["Equipment 4 Object Type"] = None
        self._data["Equipment 4 Name"] = None
        self._data["Equipment 5 Object Type"] = None
        self._data["Equipment 5 Name"] = None
        self._data["Equipment 6 Object Type"] = None
        self._data["Equipment 6 Name"] = None
        self._data["Equipment 7 Object Type"] = None
        self._data["Equipment 7 Name"] = None
        self._data["Equipment 8 Object Type"] = None
        self._data["Equipment 8 Name"] = None
        self._data["Equipment 9 Object Type"] = None
        self._data["Equipment 9 Name"] = None
        self._data["Equipment 10 Object Type"] = None
        self._data["Equipment 10 Name"] = None
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
            self.equipment_1_object_type = None
        else:
            self.equipment_1_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.equipment_1_name = None
        else:
            self.equipment_1_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.equipment_2_object_type = None
        else:
            self.equipment_2_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.equipment_2_name = None
        else:
            self.equipment_2_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.equipment_3_object_type = None
        else:
            self.equipment_3_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.equipment_3_name = None
        else:
            self.equipment_3_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.equipment_4_object_type = None
        else:
            self.equipment_4_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.equipment_4_name = None
        else:
            self.equipment_4_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.equipment_5_object_type = None
        else:
            self.equipment_5_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.equipment_5_name = None
        else:
            self.equipment_5_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.equipment_6_object_type = None
        else:
            self.equipment_6_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.equipment_6_name = None
        else:
            self.equipment_6_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.equipment_7_object_type = None
        else:
            self.equipment_7_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.equipment_7_name = None
        else:
            self.equipment_7_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.equipment_8_object_type = None
        else:
            self.equipment_8_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.equipment_8_name = None
        else:
            self.equipment_8_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.equipment_9_object_type = None
        else:
            self.equipment_9_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.equipment_9_name = None
        else:
            self.equipment_9_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.equipment_10_object_type = None
        else:
            self.equipment_10_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.equipment_10_name = None
        else:
            self.equipment_10_name = vals[i]
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
    def equipment_1_object_type(self):
        """Get equipment_1_object_type

        Returns:
            str: the value of `equipment_1_object_type` or None if not set
        """
        return self._data["Equipment 1 Object Type"]

    @equipment_1_object_type.setter
    def equipment_1_object_type(self, value=None):
        """  Corresponds to IDD Field `Equipment 1 Object Type`

        Args:
            value (str): value for IDD Field `Equipment 1 Object Type`
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
                                 'for field `equipment_1_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_1_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `equipment_1_object_type`')
        self._data["Equipment 1 Object Type"] = value

    @property
    def equipment_1_name(self):
        """Get equipment_1_name

        Returns:
            str: the value of `equipment_1_name` or None if not set
        """
        return self._data["Equipment 1 Name"]

    @equipment_1_name.setter
    def equipment_1_name(self, value=None):
        """  Corresponds to IDD Field `Equipment 1 Name`

        Args:
            value (str): value for IDD Field `Equipment 1 Name`
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
                                 'for field `equipment_1_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_1_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `equipment_1_name`')
        self._data["Equipment 1 Name"] = value

    @property
    def equipment_2_object_type(self):
        """Get equipment_2_object_type

        Returns:
            str: the value of `equipment_2_object_type` or None if not set
        """
        return self._data["Equipment 2 Object Type"]

    @equipment_2_object_type.setter
    def equipment_2_object_type(self, value=None):
        """  Corresponds to IDD Field `Equipment 2 Object Type`

        Args:
            value (str): value for IDD Field `Equipment 2 Object Type`
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
                                 'for field `equipment_2_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_2_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `equipment_2_object_type`')
        self._data["Equipment 2 Object Type"] = value

    @property
    def equipment_2_name(self):
        """Get equipment_2_name

        Returns:
            str: the value of `equipment_2_name` or None if not set
        """
        return self._data["Equipment 2 Name"]

    @equipment_2_name.setter
    def equipment_2_name(self, value=None):
        """  Corresponds to IDD Field `Equipment 2 Name`

        Args:
            value (str): value for IDD Field `Equipment 2 Name`
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
                                 'for field `equipment_2_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_2_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `equipment_2_name`')
        self._data["Equipment 2 Name"] = value

    @property
    def equipment_3_object_type(self):
        """Get equipment_3_object_type

        Returns:
            str: the value of `equipment_3_object_type` or None if not set
        """
        return self._data["Equipment 3 Object Type"]

    @equipment_3_object_type.setter
    def equipment_3_object_type(self, value=None):
        """  Corresponds to IDD Field `Equipment 3 Object Type`

        Args:
            value (str): value for IDD Field `Equipment 3 Object Type`
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
                                 'for field `equipment_3_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_3_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `equipment_3_object_type`')
        self._data["Equipment 3 Object Type"] = value

    @property
    def equipment_3_name(self):
        """Get equipment_3_name

        Returns:
            str: the value of `equipment_3_name` or None if not set
        """
        return self._data["Equipment 3 Name"]

    @equipment_3_name.setter
    def equipment_3_name(self, value=None):
        """  Corresponds to IDD Field `Equipment 3 Name`

        Args:
            value (str): value for IDD Field `Equipment 3 Name`
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
                                 'for field `equipment_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_3_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `equipment_3_name`')
        self._data["Equipment 3 Name"] = value

    @property
    def equipment_4_object_type(self):
        """Get equipment_4_object_type

        Returns:
            str: the value of `equipment_4_object_type` or None if not set
        """
        return self._data["Equipment 4 Object Type"]

    @equipment_4_object_type.setter
    def equipment_4_object_type(self, value=None):
        """  Corresponds to IDD Field `Equipment 4 Object Type`

        Args:
            value (str): value for IDD Field `Equipment 4 Object Type`
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
                                 'for field `equipment_4_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_4_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `equipment_4_object_type`')
        self._data["Equipment 4 Object Type"] = value

    @property
    def equipment_4_name(self):
        """Get equipment_4_name

        Returns:
            str: the value of `equipment_4_name` or None if not set
        """
        return self._data["Equipment 4 Name"]

    @equipment_4_name.setter
    def equipment_4_name(self, value=None):
        """  Corresponds to IDD Field `Equipment 4 Name`

        Args:
            value (str): value for IDD Field `Equipment 4 Name`
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
                                 'for field `equipment_4_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_4_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `equipment_4_name`')
        self._data["Equipment 4 Name"] = value

    @property
    def equipment_5_object_type(self):
        """Get equipment_5_object_type

        Returns:
            str: the value of `equipment_5_object_type` or None if not set
        """
        return self._data["Equipment 5 Object Type"]

    @equipment_5_object_type.setter
    def equipment_5_object_type(self, value=None):
        """  Corresponds to IDD Field `Equipment 5 Object Type`

        Args:
            value (str): value for IDD Field `Equipment 5 Object Type`
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
                                 'for field `equipment_5_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_5_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `equipment_5_object_type`')
        self._data["Equipment 5 Object Type"] = value

    @property
    def equipment_5_name(self):
        """Get equipment_5_name

        Returns:
            str: the value of `equipment_5_name` or None if not set
        """
        return self._data["Equipment 5 Name"]

    @equipment_5_name.setter
    def equipment_5_name(self, value=None):
        """  Corresponds to IDD Field `Equipment 5 Name`

        Args:
            value (str): value for IDD Field `Equipment 5 Name`
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
                                 'for field `equipment_5_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_5_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `equipment_5_name`')
        self._data["Equipment 5 Name"] = value

    @property
    def equipment_6_object_type(self):
        """Get equipment_6_object_type

        Returns:
            str: the value of `equipment_6_object_type` or None if not set
        """
        return self._data["Equipment 6 Object Type"]

    @equipment_6_object_type.setter
    def equipment_6_object_type(self, value=None):
        """  Corresponds to IDD Field `Equipment 6 Object Type`

        Args:
            value (str): value for IDD Field `Equipment 6 Object Type`
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
                                 'for field `equipment_6_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_6_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `equipment_6_object_type`')
        self._data["Equipment 6 Object Type"] = value

    @property
    def equipment_6_name(self):
        """Get equipment_6_name

        Returns:
            str: the value of `equipment_6_name` or None if not set
        """
        return self._data["Equipment 6 Name"]

    @equipment_6_name.setter
    def equipment_6_name(self, value=None):
        """  Corresponds to IDD Field `Equipment 6 Name`

        Args:
            value (str): value for IDD Field `Equipment 6 Name`
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
                                 'for field `equipment_6_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_6_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `equipment_6_name`')
        self._data["Equipment 6 Name"] = value

    @property
    def equipment_7_object_type(self):
        """Get equipment_7_object_type

        Returns:
            str: the value of `equipment_7_object_type` or None if not set
        """
        return self._data["Equipment 7 Object Type"]

    @equipment_7_object_type.setter
    def equipment_7_object_type(self, value=None):
        """  Corresponds to IDD Field `Equipment 7 Object Type`

        Args:
            value (str): value for IDD Field `Equipment 7 Object Type`
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
                                 'for field `equipment_7_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_7_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `equipment_7_object_type`')
        self._data["Equipment 7 Object Type"] = value

    @property
    def equipment_7_name(self):
        """Get equipment_7_name

        Returns:
            str: the value of `equipment_7_name` or None if not set
        """
        return self._data["Equipment 7 Name"]

    @equipment_7_name.setter
    def equipment_7_name(self, value=None):
        """  Corresponds to IDD Field `Equipment 7 Name`

        Args:
            value (str): value for IDD Field `Equipment 7 Name`
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
                                 'for field `equipment_7_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_7_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `equipment_7_name`')
        self._data["Equipment 7 Name"] = value

    @property
    def equipment_8_object_type(self):
        """Get equipment_8_object_type

        Returns:
            str: the value of `equipment_8_object_type` or None if not set
        """
        return self._data["Equipment 8 Object Type"]

    @equipment_8_object_type.setter
    def equipment_8_object_type(self, value=None):
        """  Corresponds to IDD Field `Equipment 8 Object Type`

        Args:
            value (str): value for IDD Field `Equipment 8 Object Type`
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
                                 'for field `equipment_8_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_8_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `equipment_8_object_type`')
        self._data["Equipment 8 Object Type"] = value

    @property
    def equipment_8_name(self):
        """Get equipment_8_name

        Returns:
            str: the value of `equipment_8_name` or None if not set
        """
        return self._data["Equipment 8 Name"]

    @equipment_8_name.setter
    def equipment_8_name(self, value=None):
        """  Corresponds to IDD Field `Equipment 8 Name`

        Args:
            value (str): value for IDD Field `Equipment 8 Name`
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
                                 'for field `equipment_8_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_8_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `equipment_8_name`')
        self._data["Equipment 8 Name"] = value

    @property
    def equipment_9_object_type(self):
        """Get equipment_9_object_type

        Returns:
            str: the value of `equipment_9_object_type` or None if not set
        """
        return self._data["Equipment 9 Object Type"]

    @equipment_9_object_type.setter
    def equipment_9_object_type(self, value=None):
        """  Corresponds to IDD Field `Equipment 9 Object Type`

        Args:
            value (str): value for IDD Field `Equipment 9 Object Type`
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
                                 'for field `equipment_9_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_9_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `equipment_9_object_type`')
        self._data["Equipment 9 Object Type"] = value

    @property
    def equipment_9_name(self):
        """Get equipment_9_name

        Returns:
            str: the value of `equipment_9_name` or None if not set
        """
        return self._data["Equipment 9 Name"]

    @equipment_9_name.setter
    def equipment_9_name(self, value=None):
        """  Corresponds to IDD Field `Equipment 9 Name`

        Args:
            value (str): value for IDD Field `Equipment 9 Name`
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
                                 'for field `equipment_9_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_9_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `equipment_9_name`')
        self._data["Equipment 9 Name"] = value

    @property
    def equipment_10_object_type(self):
        """Get equipment_10_object_type

        Returns:
            str: the value of `equipment_10_object_type` or None if not set
        """
        return self._data["Equipment 10 Object Type"]

    @equipment_10_object_type.setter
    def equipment_10_object_type(self, value=None):
        """  Corresponds to IDD Field `Equipment 10 Object Type`

        Args:
            value (str): value for IDD Field `Equipment 10 Object Type`
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
                                 'for field `equipment_10_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_10_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `equipment_10_object_type`')
        self._data["Equipment 10 Object Type"] = value

    @property
    def equipment_10_name(self):
        """Get equipment_10_name

        Returns:
            str: the value of `equipment_10_name` or None if not set
        """
        return self._data["Equipment 10 Name"]

    @equipment_10_name.setter
    def equipment_10_name(self, value=None):
        """  Corresponds to IDD Field `Equipment 10 Name`

        Args:
            value (str): value for IDD Field `Equipment 10 Name`
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
                                 'for field `equipment_10_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_10_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `equipment_10_name`')
        self._data["Equipment 10 Name"] = value

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

class CondenserEquipmentList(object):
    """ Corresponds to IDD object `CondenserEquipmentList`
        List condenser equipment in order of operating priority, 1st in list will be used 1st, etc
        Use only condenser equipment in this list.
        If no equipment object types and equipment names are specified, then the corresponding
        PlantEquipmentOperation:* object will assume all available condenser equipment for the loop
        should be OFF (not operate) within the specified lower/upper limit.
    
    """
    internal_name = "CondenserEquipmentList"
    field_count = 21
    required_fields = ["Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `CondenserEquipmentList`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Equipment 1 Object Type"] = None
        self._data["Equipment 1 Name"] = None
        self._data["Equipment 2 Object Type"] = None
        self._data["Equipment 2 Name"] = None
        self._data["Equipment 3 Object Type"] = None
        self._data["Equipment 3 Name"] = None
        self._data["Equipment 4 Object Type"] = None
        self._data["Equipment 4 Name"] = None
        self._data["Equipment 5 Object Type"] = None
        self._data["Equipment 5 Name"] = None
        self._data["Equipment 6 Object Type"] = None
        self._data["Equipment 6 Name"] = None
        self._data["Equipment 7 Object Type"] = None
        self._data["Equipment 7 Name"] = None
        self._data["Equipment 8 Object Type"] = None
        self._data["Equipment 8 Name"] = None
        self._data["Equipment 9 Object Type"] = None
        self._data["Equipment 9 Name"] = None
        self._data["Equipment 10 Object Type"] = None
        self._data["Equipment 10 Name"] = None
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
            self.equipment_1_object_type = None
        else:
            self.equipment_1_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.equipment_1_name = None
        else:
            self.equipment_1_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.equipment_2_object_type = None
        else:
            self.equipment_2_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.equipment_2_name = None
        else:
            self.equipment_2_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.equipment_3_object_type = None
        else:
            self.equipment_3_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.equipment_3_name = None
        else:
            self.equipment_3_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.equipment_4_object_type = None
        else:
            self.equipment_4_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.equipment_4_name = None
        else:
            self.equipment_4_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.equipment_5_object_type = None
        else:
            self.equipment_5_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.equipment_5_name = None
        else:
            self.equipment_5_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.equipment_6_object_type = None
        else:
            self.equipment_6_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.equipment_6_name = None
        else:
            self.equipment_6_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.equipment_7_object_type = None
        else:
            self.equipment_7_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.equipment_7_name = None
        else:
            self.equipment_7_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.equipment_8_object_type = None
        else:
            self.equipment_8_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.equipment_8_name = None
        else:
            self.equipment_8_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.equipment_9_object_type = None
        else:
            self.equipment_9_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.equipment_9_name = None
        else:
            self.equipment_9_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.equipment_10_object_type = None
        else:
            self.equipment_10_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.equipment_10_name = None
        else:
            self.equipment_10_name = vals[i]
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
    def equipment_1_object_type(self):
        """Get equipment_1_object_type

        Returns:
            str: the value of `equipment_1_object_type` or None if not set
        """
        return self._data["Equipment 1 Object Type"]

    @equipment_1_object_type.setter
    def equipment_1_object_type(self, value=None):
        """  Corresponds to IDD Field `Equipment 1 Object Type`

        Args:
            value (str): value for IDD Field `Equipment 1 Object Type`
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
                                 'for field `equipment_1_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_1_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `equipment_1_object_type`')
        self._data["Equipment 1 Object Type"] = value

    @property
    def equipment_1_name(self):
        """Get equipment_1_name

        Returns:
            str: the value of `equipment_1_name` or None if not set
        """
        return self._data["Equipment 1 Name"]

    @equipment_1_name.setter
    def equipment_1_name(self, value=None):
        """  Corresponds to IDD Field `Equipment 1 Name`

        Args:
            value (str): value for IDD Field `Equipment 1 Name`
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
                                 'for field `equipment_1_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_1_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `equipment_1_name`')
        self._data["Equipment 1 Name"] = value

    @property
    def equipment_2_object_type(self):
        """Get equipment_2_object_type

        Returns:
            str: the value of `equipment_2_object_type` or None if not set
        """
        return self._data["Equipment 2 Object Type"]

    @equipment_2_object_type.setter
    def equipment_2_object_type(self, value=None):
        """  Corresponds to IDD Field `Equipment 2 Object Type`

        Args:
            value (str): value for IDD Field `Equipment 2 Object Type`
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
                                 'for field `equipment_2_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_2_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `equipment_2_object_type`')
        self._data["Equipment 2 Object Type"] = value

    @property
    def equipment_2_name(self):
        """Get equipment_2_name

        Returns:
            str: the value of `equipment_2_name` or None if not set
        """
        return self._data["Equipment 2 Name"]

    @equipment_2_name.setter
    def equipment_2_name(self, value=None):
        """  Corresponds to IDD Field `Equipment 2 Name`

        Args:
            value (str): value for IDD Field `Equipment 2 Name`
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
                                 'for field `equipment_2_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_2_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `equipment_2_name`')
        self._data["Equipment 2 Name"] = value

    @property
    def equipment_3_object_type(self):
        """Get equipment_3_object_type

        Returns:
            str: the value of `equipment_3_object_type` or None if not set
        """
        return self._data["Equipment 3 Object Type"]

    @equipment_3_object_type.setter
    def equipment_3_object_type(self, value=None):
        """  Corresponds to IDD Field `Equipment 3 Object Type`

        Args:
            value (str): value for IDD Field `Equipment 3 Object Type`
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
                                 'for field `equipment_3_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_3_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `equipment_3_object_type`')
        self._data["Equipment 3 Object Type"] = value

    @property
    def equipment_3_name(self):
        """Get equipment_3_name

        Returns:
            str: the value of `equipment_3_name` or None if not set
        """
        return self._data["Equipment 3 Name"]

    @equipment_3_name.setter
    def equipment_3_name(self, value=None):
        """  Corresponds to IDD Field `Equipment 3 Name`

        Args:
            value (str): value for IDD Field `Equipment 3 Name`
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
                                 'for field `equipment_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_3_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `equipment_3_name`')
        self._data["Equipment 3 Name"] = value

    @property
    def equipment_4_object_type(self):
        """Get equipment_4_object_type

        Returns:
            str: the value of `equipment_4_object_type` or None if not set
        """
        return self._data["Equipment 4 Object Type"]

    @equipment_4_object_type.setter
    def equipment_4_object_type(self, value=None):
        """  Corresponds to IDD Field `Equipment 4 Object Type`

        Args:
            value (str): value for IDD Field `Equipment 4 Object Type`
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
                                 'for field `equipment_4_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_4_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `equipment_4_object_type`')
        self._data["Equipment 4 Object Type"] = value

    @property
    def equipment_4_name(self):
        """Get equipment_4_name

        Returns:
            str: the value of `equipment_4_name` or None if not set
        """
        return self._data["Equipment 4 Name"]

    @equipment_4_name.setter
    def equipment_4_name(self, value=None):
        """  Corresponds to IDD Field `Equipment 4 Name`

        Args:
            value (str): value for IDD Field `Equipment 4 Name`
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
                                 'for field `equipment_4_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_4_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `equipment_4_name`')
        self._data["Equipment 4 Name"] = value

    @property
    def equipment_5_object_type(self):
        """Get equipment_5_object_type

        Returns:
            str: the value of `equipment_5_object_type` or None if not set
        """
        return self._data["Equipment 5 Object Type"]

    @equipment_5_object_type.setter
    def equipment_5_object_type(self, value=None):
        """  Corresponds to IDD Field `Equipment 5 Object Type`

        Args:
            value (str): value for IDD Field `Equipment 5 Object Type`
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
                                 'for field `equipment_5_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_5_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `equipment_5_object_type`')
        self._data["Equipment 5 Object Type"] = value

    @property
    def equipment_5_name(self):
        """Get equipment_5_name

        Returns:
            str: the value of `equipment_5_name` or None if not set
        """
        return self._data["Equipment 5 Name"]

    @equipment_5_name.setter
    def equipment_5_name(self, value=None):
        """  Corresponds to IDD Field `Equipment 5 Name`

        Args:
            value (str): value for IDD Field `Equipment 5 Name`
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
                                 'for field `equipment_5_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_5_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `equipment_5_name`')
        self._data["Equipment 5 Name"] = value

    @property
    def equipment_6_object_type(self):
        """Get equipment_6_object_type

        Returns:
            str: the value of `equipment_6_object_type` or None if not set
        """
        return self._data["Equipment 6 Object Type"]

    @equipment_6_object_type.setter
    def equipment_6_object_type(self, value=None):
        """  Corresponds to IDD Field `Equipment 6 Object Type`

        Args:
            value (str): value for IDD Field `Equipment 6 Object Type`
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
                                 'for field `equipment_6_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_6_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `equipment_6_object_type`')
        self._data["Equipment 6 Object Type"] = value

    @property
    def equipment_6_name(self):
        """Get equipment_6_name

        Returns:
            str: the value of `equipment_6_name` or None if not set
        """
        return self._data["Equipment 6 Name"]

    @equipment_6_name.setter
    def equipment_6_name(self, value=None):
        """  Corresponds to IDD Field `Equipment 6 Name`

        Args:
            value (str): value for IDD Field `Equipment 6 Name`
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
                                 'for field `equipment_6_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_6_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `equipment_6_name`')
        self._data["Equipment 6 Name"] = value

    @property
    def equipment_7_object_type(self):
        """Get equipment_7_object_type

        Returns:
            str: the value of `equipment_7_object_type` or None if not set
        """
        return self._data["Equipment 7 Object Type"]

    @equipment_7_object_type.setter
    def equipment_7_object_type(self, value=None):
        """  Corresponds to IDD Field `Equipment 7 Object Type`

        Args:
            value (str): value for IDD Field `Equipment 7 Object Type`
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
                                 'for field `equipment_7_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_7_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `equipment_7_object_type`')
        self._data["Equipment 7 Object Type"] = value

    @property
    def equipment_7_name(self):
        """Get equipment_7_name

        Returns:
            str: the value of `equipment_7_name` or None if not set
        """
        return self._data["Equipment 7 Name"]

    @equipment_7_name.setter
    def equipment_7_name(self, value=None):
        """  Corresponds to IDD Field `Equipment 7 Name`

        Args:
            value (str): value for IDD Field `Equipment 7 Name`
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
                                 'for field `equipment_7_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_7_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `equipment_7_name`')
        self._data["Equipment 7 Name"] = value

    @property
    def equipment_8_object_type(self):
        """Get equipment_8_object_type

        Returns:
            str: the value of `equipment_8_object_type` or None if not set
        """
        return self._data["Equipment 8 Object Type"]

    @equipment_8_object_type.setter
    def equipment_8_object_type(self, value=None):
        """  Corresponds to IDD Field `Equipment 8 Object Type`

        Args:
            value (str): value for IDD Field `Equipment 8 Object Type`
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
                                 'for field `equipment_8_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_8_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `equipment_8_object_type`')
        self._data["Equipment 8 Object Type"] = value

    @property
    def equipment_8_name(self):
        """Get equipment_8_name

        Returns:
            str: the value of `equipment_8_name` or None if not set
        """
        return self._data["Equipment 8 Name"]

    @equipment_8_name.setter
    def equipment_8_name(self, value=None):
        """  Corresponds to IDD Field `Equipment 8 Name`

        Args:
            value (str): value for IDD Field `Equipment 8 Name`
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
                                 'for field `equipment_8_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_8_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `equipment_8_name`')
        self._data["Equipment 8 Name"] = value

    @property
    def equipment_9_object_type(self):
        """Get equipment_9_object_type

        Returns:
            str: the value of `equipment_9_object_type` or None if not set
        """
        return self._data["Equipment 9 Object Type"]

    @equipment_9_object_type.setter
    def equipment_9_object_type(self, value=None):
        """  Corresponds to IDD Field `Equipment 9 Object Type`

        Args:
            value (str): value for IDD Field `Equipment 9 Object Type`
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
                                 'for field `equipment_9_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_9_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `equipment_9_object_type`')
        self._data["Equipment 9 Object Type"] = value

    @property
    def equipment_9_name(self):
        """Get equipment_9_name

        Returns:
            str: the value of `equipment_9_name` or None if not set
        """
        return self._data["Equipment 9 Name"]

    @equipment_9_name.setter
    def equipment_9_name(self, value=None):
        """  Corresponds to IDD Field `Equipment 9 Name`

        Args:
            value (str): value for IDD Field `Equipment 9 Name`
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
                                 'for field `equipment_9_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_9_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `equipment_9_name`')
        self._data["Equipment 9 Name"] = value

    @property
    def equipment_10_object_type(self):
        """Get equipment_10_object_type

        Returns:
            str: the value of `equipment_10_object_type` or None if not set
        """
        return self._data["Equipment 10 Object Type"]

    @equipment_10_object_type.setter
    def equipment_10_object_type(self, value=None):
        """  Corresponds to IDD Field `Equipment 10 Object Type`

        Args:
            value (str): value for IDD Field `Equipment 10 Object Type`
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
                                 'for field `equipment_10_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_10_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `equipment_10_object_type`')
        self._data["Equipment 10 Object Type"] = value

    @property
    def equipment_10_name(self):
        """Get equipment_10_name

        Returns:
            str: the value of `equipment_10_name` or None if not set
        """
        return self._data["Equipment 10 Name"]

    @equipment_10_name.setter
    def equipment_10_name(self, value=None):
        """  Corresponds to IDD Field `Equipment 10 Name`

        Args:
            value (str): value for IDD Field `Equipment 10 Name`
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
                                 'for field `equipment_10_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_10_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `equipment_10_name`')
        self._data["Equipment 10 Name"] = value

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

class PlantEquipmentOperationUncontrolled(object):
    """ Corresponds to IDD object `PlantEquipmentOperation:Uncontrolled`
        Plant equipment operation scheme for uncontrolled operation. Specifies a group of
        equipment that runs if the loop is active, unless turned off by the loop flow resolver
        to maintain continuity in the fluid loop.
    
    """
    internal_name = "PlantEquipmentOperation:Uncontrolled"
    field_count = 2
    required_fields = ["Name", "Equipment List Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `PlantEquipmentOperation:Uncontrolled`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Equipment List Name"] = None
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
            self.equipment_list_name = None
        else:
            self.equipment_list_name = vals[i]
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
    def equipment_list_name(self):
        """Get equipment_list_name

        Returns:
            str: the value of `equipment_list_name` or None if not set
        """
        return self._data["Equipment List Name"]

    @equipment_list_name.setter
    def equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `Equipment List Name`

        Args:
            value (str): value for IDD Field `Equipment List Name`
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
                                 'for field `equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `equipment_list_name`')
        self._data["Equipment List Name"] = value

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

class PlantEquipmentOperationCoolingLoad(object):
    """ Corresponds to IDD object `PlantEquipmentOperation:CoolingLoad`
        Plant equipment operation scheme for cooling load range operation. Specifies one or
        more groups of equipment which are available to operate for successive cooling load
        ranges.
    
    """
    internal_name = "PlantEquipmentOperation:CoolingLoad"
    field_count = 31
    required_fields = ["Name", "Load Range 1 Lower Limit", "Load Range 1 Upper Limit"]

    def __init__(self):
        """ Init data dictionary object for IDD  `PlantEquipmentOperation:CoolingLoad`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Load Range 1 Lower Limit"] = None
        self._data["Load Range 1 Upper Limit"] = None
        self._data["Range 1 Equipment List Name"] = None
        self._data["Load Range 2 Lower Limit"] = None
        self._data["Load Range 2 Upper Limit"] = None
        self._data["Range 2 Equipment List Name"] = None
        self._data["Load Range 3 Lower Limit"] = None
        self._data["Load Range 3 Upper Limit"] = None
        self._data["Range 3 Equipment List Name"] = None
        self._data["Load Range 4 Lower Limit"] = None
        self._data["Load Range 4 Upper Limit"] = None
        self._data["Range 4 Equipment List Name"] = None
        self._data["Load Range 5 Lower Limit"] = None
        self._data["Load Range 5 Upper Limit"] = None
        self._data["Range 5 Equipment List Name"] = None
        self._data["Load Range 6 Lower Limit"] = None
        self._data["Load Range 6 Upper Limit"] = None
        self._data["Range 6 Equipment List Name"] = None
        self._data["Load Range 7 Lower Limit"] = None
        self._data["Load Range 7 Upper Limit"] = None
        self._data["Range 7 Equipment List Name"] = None
        self._data["Load Range 8 Lower Limit"] = None
        self._data["Load Range 8 Upper Limit"] = None
        self._data["Range 8 Equipment List Name"] = None
        self._data["Load Range 9 Lower Limit"] = None
        self._data["Load Range 9 Upper Limit"] = None
        self._data["Range 9 Equipment List Name"] = None
        self._data["Load Range 10 Lower Limit"] = None
        self._data["Load Range 10 Upper Limit"] = None
        self._data["Range 10 Equipment List Name"] = None
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
            self.load_range_1_lower_limit = None
        else:
            self.load_range_1_lower_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.load_range_1_upper_limit = None
        else:
            self.load_range_1_upper_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.range_1_equipment_list_name = None
        else:
            self.range_1_equipment_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.load_range_2_lower_limit = None
        else:
            self.load_range_2_lower_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.load_range_2_upper_limit = None
        else:
            self.load_range_2_upper_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.range_2_equipment_list_name = None
        else:
            self.range_2_equipment_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.load_range_3_lower_limit = None
        else:
            self.load_range_3_lower_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.load_range_3_upper_limit = None
        else:
            self.load_range_3_upper_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.range_3_equipment_list_name = None
        else:
            self.range_3_equipment_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.load_range_4_lower_limit = None
        else:
            self.load_range_4_lower_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.load_range_4_upper_limit = None
        else:
            self.load_range_4_upper_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.range_4_equipment_list_name = None
        else:
            self.range_4_equipment_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.load_range_5_lower_limit = None
        else:
            self.load_range_5_lower_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.load_range_5_upper_limit = None
        else:
            self.load_range_5_upper_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.range_5_equipment_list_name = None
        else:
            self.range_5_equipment_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.load_range_6_lower_limit = None
        else:
            self.load_range_6_lower_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.load_range_6_upper_limit = None
        else:
            self.load_range_6_upper_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.range_6_equipment_list_name = None
        else:
            self.range_6_equipment_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.load_range_7_lower_limit = None
        else:
            self.load_range_7_lower_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.load_range_7_upper_limit = None
        else:
            self.load_range_7_upper_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.range_7_equipment_list_name = None
        else:
            self.range_7_equipment_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.load_range_8_lower_limit = None
        else:
            self.load_range_8_lower_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.load_range_8_upper_limit = None
        else:
            self.load_range_8_upper_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.range_8_equipment_list_name = None
        else:
            self.range_8_equipment_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.load_range_9_lower_limit = None
        else:
            self.load_range_9_lower_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.load_range_9_upper_limit = None
        else:
            self.load_range_9_upper_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.range_9_equipment_list_name = None
        else:
            self.range_9_equipment_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.load_range_10_lower_limit = None
        else:
            self.load_range_10_lower_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.load_range_10_upper_limit = None
        else:
            self.load_range_10_upper_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.range_10_equipment_list_name = None
        else:
            self.range_10_equipment_list_name = vals[i]
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
    def load_range_1_lower_limit(self):
        """Get load_range_1_lower_limit

        Returns:
            float: the value of `load_range_1_lower_limit` or None if not set
        """
        return self._data["Load Range 1 Lower Limit"]

    @load_range_1_lower_limit.setter
    def load_range_1_lower_limit(self, value=None):
        """  Corresponds to IDD Field `Load Range 1 Lower Limit`

        Args:
            value (float): value for IDD Field `Load Range 1 Lower Limit`
                Units: W
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
                                 'for field `load_range_1_lower_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `load_range_1_lower_limit`')
        self._data["Load Range 1 Lower Limit"] = value

    @property
    def load_range_1_upper_limit(self):
        """Get load_range_1_upper_limit

        Returns:
            float: the value of `load_range_1_upper_limit` or None if not set
        """
        return self._data["Load Range 1 Upper Limit"]

    @load_range_1_upper_limit.setter
    def load_range_1_upper_limit(self, value=None):
        """  Corresponds to IDD Field `Load Range 1 Upper Limit`

        Args:
            value (float): value for IDD Field `Load Range 1 Upper Limit`
                Units: W
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
                                 'for field `load_range_1_upper_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `load_range_1_upper_limit`')
        self._data["Load Range 1 Upper Limit"] = value

    @property
    def range_1_equipment_list_name(self):
        """Get range_1_equipment_list_name

        Returns:
            str: the value of `range_1_equipment_list_name` or None if not set
        """
        return self._data["Range 1 Equipment List Name"]

    @range_1_equipment_list_name.setter
    def range_1_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `Range 1 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 1 Equipment List Name`
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
                                 'for field `range_1_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_1_equipment_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `range_1_equipment_list_name`')
        self._data["Range 1 Equipment List Name"] = value

    @property
    def load_range_2_lower_limit(self):
        """Get load_range_2_lower_limit

        Returns:
            float: the value of `load_range_2_lower_limit` or None if not set
        """
        return self._data["Load Range 2 Lower Limit"]

    @load_range_2_lower_limit.setter
    def load_range_2_lower_limit(self, value=None):
        """  Corresponds to IDD Field `Load Range 2 Lower Limit`

        Args:
            value (float): value for IDD Field `Load Range 2 Lower Limit`
                Units: W
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
                                 'for field `load_range_2_lower_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `load_range_2_lower_limit`')
        self._data["Load Range 2 Lower Limit"] = value

    @property
    def load_range_2_upper_limit(self):
        """Get load_range_2_upper_limit

        Returns:
            float: the value of `load_range_2_upper_limit` or None if not set
        """
        return self._data["Load Range 2 Upper Limit"]

    @load_range_2_upper_limit.setter
    def load_range_2_upper_limit(self, value=None):
        """  Corresponds to IDD Field `Load Range 2 Upper Limit`

        Args:
            value (float): value for IDD Field `Load Range 2 Upper Limit`
                Units: W
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `load_range_2_upper_limit`'.format(value))
        self._data["Load Range 2 Upper Limit"] = value

    @property
    def range_2_equipment_list_name(self):
        """Get range_2_equipment_list_name

        Returns:
            str: the value of `range_2_equipment_list_name` or None if not set
        """
        return self._data["Range 2 Equipment List Name"]

    @range_2_equipment_list_name.setter
    def range_2_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `Range 2 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 2 Equipment List Name`
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
                                 'for field `range_2_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_2_equipment_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `range_2_equipment_list_name`')
        self._data["Range 2 Equipment List Name"] = value

    @property
    def load_range_3_lower_limit(self):
        """Get load_range_3_lower_limit

        Returns:
            float: the value of `load_range_3_lower_limit` or None if not set
        """
        return self._data["Load Range 3 Lower Limit"]

    @load_range_3_lower_limit.setter
    def load_range_3_lower_limit(self, value=None):
        """  Corresponds to IDD Field `Load Range 3 Lower Limit`

        Args:
            value (float): value for IDD Field `Load Range 3 Lower Limit`
                Units: W
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
                                 'for field `load_range_3_lower_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `load_range_3_lower_limit`')
        self._data["Load Range 3 Lower Limit"] = value

    @property
    def load_range_3_upper_limit(self):
        """Get load_range_3_upper_limit

        Returns:
            float: the value of `load_range_3_upper_limit` or None if not set
        """
        return self._data["Load Range 3 Upper Limit"]

    @load_range_3_upper_limit.setter
    def load_range_3_upper_limit(self, value=None):
        """  Corresponds to IDD Field `Load Range 3 Upper Limit`

        Args:
            value (float): value for IDD Field `Load Range 3 Upper Limit`
                Units: W
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
                                 'for field `load_range_3_upper_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `load_range_3_upper_limit`')
        self._data["Load Range 3 Upper Limit"] = value

    @property
    def range_3_equipment_list_name(self):
        """Get range_3_equipment_list_name

        Returns:
            str: the value of `range_3_equipment_list_name` or None if not set
        """
        return self._data["Range 3 Equipment List Name"]

    @range_3_equipment_list_name.setter
    def range_3_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `Range 3 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 3 Equipment List Name`
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
                                 'for field `range_3_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_3_equipment_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `range_3_equipment_list_name`')
        self._data["Range 3 Equipment List Name"] = value

    @property
    def load_range_4_lower_limit(self):
        """Get load_range_4_lower_limit

        Returns:
            float: the value of `load_range_4_lower_limit` or None if not set
        """
        return self._data["Load Range 4 Lower Limit"]

    @load_range_4_lower_limit.setter
    def load_range_4_lower_limit(self, value=None):
        """  Corresponds to IDD Field `Load Range 4 Lower Limit`

        Args:
            value (float): value for IDD Field `Load Range 4 Lower Limit`
                Units: W
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
                                 'for field `load_range_4_lower_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `load_range_4_lower_limit`')
        self._data["Load Range 4 Lower Limit"] = value

    @property
    def load_range_4_upper_limit(self):
        """Get load_range_4_upper_limit

        Returns:
            float: the value of `load_range_4_upper_limit` or None if not set
        """
        return self._data["Load Range 4 Upper Limit"]

    @load_range_4_upper_limit.setter
    def load_range_4_upper_limit(self, value=None):
        """  Corresponds to IDD Field `Load Range 4 Upper Limit`

        Args:
            value (float): value for IDD Field `Load Range 4 Upper Limit`
                Units: W
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
                                 'for field `load_range_4_upper_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `load_range_4_upper_limit`')
        self._data["Load Range 4 Upper Limit"] = value

    @property
    def range_4_equipment_list_name(self):
        """Get range_4_equipment_list_name

        Returns:
            str: the value of `range_4_equipment_list_name` or None if not set
        """
        return self._data["Range 4 Equipment List Name"]

    @range_4_equipment_list_name.setter
    def range_4_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `Range 4 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 4 Equipment List Name`
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
                                 'for field `range_4_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_4_equipment_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `range_4_equipment_list_name`')
        self._data["Range 4 Equipment List Name"] = value

    @property
    def load_range_5_lower_limit(self):
        """Get load_range_5_lower_limit

        Returns:
            float: the value of `load_range_5_lower_limit` or None if not set
        """
        return self._data["Load Range 5 Lower Limit"]

    @load_range_5_lower_limit.setter
    def load_range_5_lower_limit(self, value=None):
        """  Corresponds to IDD Field `Load Range 5 Lower Limit`

        Args:
            value (float): value for IDD Field `Load Range 5 Lower Limit`
                Units: W
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
                                 'for field `load_range_5_lower_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `load_range_5_lower_limit`')
        self._data["Load Range 5 Lower Limit"] = value

    @property
    def load_range_5_upper_limit(self):
        """Get load_range_5_upper_limit

        Returns:
            float: the value of `load_range_5_upper_limit` or None if not set
        """
        return self._data["Load Range 5 Upper Limit"]

    @load_range_5_upper_limit.setter
    def load_range_5_upper_limit(self, value=None):
        """  Corresponds to IDD Field `Load Range 5 Upper Limit`

        Args:
            value (float): value for IDD Field `Load Range 5 Upper Limit`
                Units: W
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
                                 'for field `load_range_5_upper_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `load_range_5_upper_limit`')
        self._data["Load Range 5 Upper Limit"] = value

    @property
    def range_5_equipment_list_name(self):
        """Get range_5_equipment_list_name

        Returns:
            str: the value of `range_5_equipment_list_name` or None if not set
        """
        return self._data["Range 5 Equipment List Name"]

    @range_5_equipment_list_name.setter
    def range_5_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `Range 5 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 5 Equipment List Name`
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
                                 'for field `range_5_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_5_equipment_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `range_5_equipment_list_name`')
        self._data["Range 5 Equipment List Name"] = value

    @property
    def load_range_6_lower_limit(self):
        """Get load_range_6_lower_limit

        Returns:
            float: the value of `load_range_6_lower_limit` or None if not set
        """
        return self._data["Load Range 6 Lower Limit"]

    @load_range_6_lower_limit.setter
    def load_range_6_lower_limit(self, value=None):
        """  Corresponds to IDD Field `Load Range 6 Lower Limit`

        Args:
            value (float): value for IDD Field `Load Range 6 Lower Limit`
                Units: W
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
                                 'for field `load_range_6_lower_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `load_range_6_lower_limit`')
        self._data["Load Range 6 Lower Limit"] = value

    @property
    def load_range_6_upper_limit(self):
        """Get load_range_6_upper_limit

        Returns:
            float: the value of `load_range_6_upper_limit` or None if not set
        """
        return self._data["Load Range 6 Upper Limit"]

    @load_range_6_upper_limit.setter
    def load_range_6_upper_limit(self, value=None):
        """  Corresponds to IDD Field `Load Range 6 Upper Limit`

        Args:
            value (float): value for IDD Field `Load Range 6 Upper Limit`
                Units: W
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
                                 'for field `load_range_6_upper_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `load_range_6_upper_limit`')
        self._data["Load Range 6 Upper Limit"] = value

    @property
    def range_6_equipment_list_name(self):
        """Get range_6_equipment_list_name

        Returns:
            str: the value of `range_6_equipment_list_name` or None if not set
        """
        return self._data["Range 6 Equipment List Name"]

    @range_6_equipment_list_name.setter
    def range_6_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `Range 6 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 6 Equipment List Name`
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
                                 'for field `range_6_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_6_equipment_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `range_6_equipment_list_name`')
        self._data["Range 6 Equipment List Name"] = value

    @property
    def load_range_7_lower_limit(self):
        """Get load_range_7_lower_limit

        Returns:
            float: the value of `load_range_7_lower_limit` or None if not set
        """
        return self._data["Load Range 7 Lower Limit"]

    @load_range_7_lower_limit.setter
    def load_range_7_lower_limit(self, value=None):
        """  Corresponds to IDD Field `Load Range 7 Lower Limit`

        Args:
            value (float): value for IDD Field `Load Range 7 Lower Limit`
                Units: W
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
                                 'for field `load_range_7_lower_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `load_range_7_lower_limit`')
        self._data["Load Range 7 Lower Limit"] = value

    @property
    def load_range_7_upper_limit(self):
        """Get load_range_7_upper_limit

        Returns:
            float: the value of `load_range_7_upper_limit` or None if not set
        """
        return self._data["Load Range 7 Upper Limit"]

    @load_range_7_upper_limit.setter
    def load_range_7_upper_limit(self, value=None):
        """  Corresponds to IDD Field `Load Range 7 Upper Limit`

        Args:
            value (float): value for IDD Field `Load Range 7 Upper Limit`
                Units: W
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
                                 'for field `load_range_7_upper_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `load_range_7_upper_limit`')
        self._data["Load Range 7 Upper Limit"] = value

    @property
    def range_7_equipment_list_name(self):
        """Get range_7_equipment_list_name

        Returns:
            str: the value of `range_7_equipment_list_name` or None if not set
        """
        return self._data["Range 7 Equipment List Name"]

    @range_7_equipment_list_name.setter
    def range_7_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `Range 7 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 7 Equipment List Name`
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
                                 'for field `range_7_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_7_equipment_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `range_7_equipment_list_name`')
        self._data["Range 7 Equipment List Name"] = value

    @property
    def load_range_8_lower_limit(self):
        """Get load_range_8_lower_limit

        Returns:
            float: the value of `load_range_8_lower_limit` or None if not set
        """
        return self._data["Load Range 8 Lower Limit"]

    @load_range_8_lower_limit.setter
    def load_range_8_lower_limit(self, value=None):
        """  Corresponds to IDD Field `Load Range 8 Lower Limit`

        Args:
            value (float): value for IDD Field `Load Range 8 Lower Limit`
                Units: W
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
                                 'for field `load_range_8_lower_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `load_range_8_lower_limit`')
        self._data["Load Range 8 Lower Limit"] = value

    @property
    def load_range_8_upper_limit(self):
        """Get load_range_8_upper_limit

        Returns:
            float: the value of `load_range_8_upper_limit` or None if not set
        """
        return self._data["Load Range 8 Upper Limit"]

    @load_range_8_upper_limit.setter
    def load_range_8_upper_limit(self, value=None):
        """  Corresponds to IDD Field `Load Range 8 Upper Limit`

        Args:
            value (float): value for IDD Field `Load Range 8 Upper Limit`
                Units: W
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
                                 'for field `load_range_8_upper_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `load_range_8_upper_limit`')
        self._data["Load Range 8 Upper Limit"] = value

    @property
    def range_8_equipment_list_name(self):
        """Get range_8_equipment_list_name

        Returns:
            str: the value of `range_8_equipment_list_name` or None if not set
        """
        return self._data["Range 8 Equipment List Name"]

    @range_8_equipment_list_name.setter
    def range_8_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `Range 8 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 8 Equipment List Name`
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
                                 'for field `range_8_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_8_equipment_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `range_8_equipment_list_name`')
        self._data["Range 8 Equipment List Name"] = value

    @property
    def load_range_9_lower_limit(self):
        """Get load_range_9_lower_limit

        Returns:
            float: the value of `load_range_9_lower_limit` or None if not set
        """
        return self._data["Load Range 9 Lower Limit"]

    @load_range_9_lower_limit.setter
    def load_range_9_lower_limit(self, value=None):
        """  Corresponds to IDD Field `Load Range 9 Lower Limit`

        Args:
            value (float): value for IDD Field `Load Range 9 Lower Limit`
                Units: W
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
                                 'for field `load_range_9_lower_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `load_range_9_lower_limit`')
        self._data["Load Range 9 Lower Limit"] = value

    @property
    def load_range_9_upper_limit(self):
        """Get load_range_9_upper_limit

        Returns:
            float: the value of `load_range_9_upper_limit` or None if not set
        """
        return self._data["Load Range 9 Upper Limit"]

    @load_range_9_upper_limit.setter
    def load_range_9_upper_limit(self, value=None):
        """  Corresponds to IDD Field `Load Range 9 Upper Limit`

        Args:
            value (float): value for IDD Field `Load Range 9 Upper Limit`
                Units: W
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
                                 'for field `load_range_9_upper_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `load_range_9_upper_limit`')
        self._data["Load Range 9 Upper Limit"] = value

    @property
    def range_9_equipment_list_name(self):
        """Get range_9_equipment_list_name

        Returns:
            str: the value of `range_9_equipment_list_name` or None if not set
        """
        return self._data["Range 9 Equipment List Name"]

    @range_9_equipment_list_name.setter
    def range_9_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `Range 9 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 9 Equipment List Name`
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
                                 'for field `range_9_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_9_equipment_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `range_9_equipment_list_name`')
        self._data["Range 9 Equipment List Name"] = value

    @property
    def load_range_10_lower_limit(self):
        """Get load_range_10_lower_limit

        Returns:
            float: the value of `load_range_10_lower_limit` or None if not set
        """
        return self._data["Load Range 10 Lower Limit"]

    @load_range_10_lower_limit.setter
    def load_range_10_lower_limit(self, value=None):
        """  Corresponds to IDD Field `Load Range 10 Lower Limit`

        Args:
            value (float): value for IDD Field `Load Range 10 Lower Limit`
                Units: W
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
                                 'for field `load_range_10_lower_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `load_range_10_lower_limit`')
        self._data["Load Range 10 Lower Limit"] = value

    @property
    def load_range_10_upper_limit(self):
        """Get load_range_10_upper_limit

        Returns:
            float: the value of `load_range_10_upper_limit` or None if not set
        """
        return self._data["Load Range 10 Upper Limit"]

    @load_range_10_upper_limit.setter
    def load_range_10_upper_limit(self, value=None):
        """  Corresponds to IDD Field `Load Range 10 Upper Limit`

        Args:
            value (float): value for IDD Field `Load Range 10 Upper Limit`
                Units: W
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
                                 'for field `load_range_10_upper_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `load_range_10_upper_limit`')
        self._data["Load Range 10 Upper Limit"] = value

    @property
    def range_10_equipment_list_name(self):
        """Get range_10_equipment_list_name

        Returns:
            str: the value of `range_10_equipment_list_name` or None if not set
        """
        return self._data["Range 10 Equipment List Name"]

    @range_10_equipment_list_name.setter
    def range_10_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `Range 10 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 10 Equipment List Name`
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
                                 'for field `range_10_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_10_equipment_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `range_10_equipment_list_name`')
        self._data["Range 10 Equipment List Name"] = value

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

class PlantEquipmentOperationHeatingLoad(object):
    """ Corresponds to IDD object `PlantEquipmentOperation:HeatingLoad`
        Plant equipment operation scheme for heating load range operation. Specifies one or
        more groups of equipment which are available to operate for successive heating load
        ranges.
    
    """
    internal_name = "PlantEquipmentOperation:HeatingLoad"
    field_count = 31
    required_fields = ["Name", "Load Range 1 Lower Limit", "Load Range 1 Upper Limit", "Range 1 Equipment List Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `PlantEquipmentOperation:HeatingLoad`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Load Range 1 Lower Limit"] = None
        self._data["Load Range 1 Upper Limit"] = None
        self._data["Range 1 Equipment List Name"] = None
        self._data["Load Range 2 Lower Limit"] = None
        self._data["Load Range 2 Upper Limit"] = None
        self._data["Range 2 Equipment List Name"] = None
        self._data["Load Range 3 Lower Limit"] = None
        self._data["Load Range 3 Upper Limit"] = None
        self._data["Range 3 Equipment List Name"] = None
        self._data["Load Range 4 Lower Limit"] = None
        self._data["Load Range 4 Upper Limit"] = None
        self._data["Range 4 Equipment List Name"] = None
        self._data["Load Range 5 Lower Limit"] = None
        self._data["Load Range 5 Upper Limit"] = None
        self._data["Range 5 Equipment List Name"] = None
        self._data["Load Range 6 Lower Limit"] = None
        self._data["Load Range 6 Upper Limit"] = None
        self._data["Range 6 Equipment List Name"] = None
        self._data["Load Range 7 Lower Limit"] = None
        self._data["Load Range 7 Upper Limit"] = None
        self._data["Range 7 Equipment List Name"] = None
        self._data["Load Range 8 Lower Limit"] = None
        self._data["Load Range 8 Upper Limit"] = None
        self._data["Range 8 Equipment List Name"] = None
        self._data["Load Range 9 Lower Limit"] = None
        self._data["Load Range 9 Upper Limit"] = None
        self._data["Range 9 Equipment List Name"] = None
        self._data["Load Range 10 Lower Limit"] = None
        self._data["Load Range 10 Upper Limit"] = None
        self._data["Range 10 Equipment List Name"] = None
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
            self.load_range_1_lower_limit = None
        else:
            self.load_range_1_lower_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.load_range_1_upper_limit = None
        else:
            self.load_range_1_upper_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.range_1_equipment_list_name = None
        else:
            self.range_1_equipment_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.load_range_2_lower_limit = None
        else:
            self.load_range_2_lower_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.load_range_2_upper_limit = None
        else:
            self.load_range_2_upper_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.range_2_equipment_list_name = None
        else:
            self.range_2_equipment_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.load_range_3_lower_limit = None
        else:
            self.load_range_3_lower_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.load_range_3_upper_limit = None
        else:
            self.load_range_3_upper_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.range_3_equipment_list_name = None
        else:
            self.range_3_equipment_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.load_range_4_lower_limit = None
        else:
            self.load_range_4_lower_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.load_range_4_upper_limit = None
        else:
            self.load_range_4_upper_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.range_4_equipment_list_name = None
        else:
            self.range_4_equipment_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.load_range_5_lower_limit = None
        else:
            self.load_range_5_lower_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.load_range_5_upper_limit = None
        else:
            self.load_range_5_upper_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.range_5_equipment_list_name = None
        else:
            self.range_5_equipment_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.load_range_6_lower_limit = None
        else:
            self.load_range_6_lower_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.load_range_6_upper_limit = None
        else:
            self.load_range_6_upper_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.range_6_equipment_list_name = None
        else:
            self.range_6_equipment_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.load_range_7_lower_limit = None
        else:
            self.load_range_7_lower_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.load_range_7_upper_limit = None
        else:
            self.load_range_7_upper_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.range_7_equipment_list_name = None
        else:
            self.range_7_equipment_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.load_range_8_lower_limit = None
        else:
            self.load_range_8_lower_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.load_range_8_upper_limit = None
        else:
            self.load_range_8_upper_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.range_8_equipment_list_name = None
        else:
            self.range_8_equipment_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.load_range_9_lower_limit = None
        else:
            self.load_range_9_lower_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.load_range_9_upper_limit = None
        else:
            self.load_range_9_upper_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.range_9_equipment_list_name = None
        else:
            self.range_9_equipment_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.load_range_10_lower_limit = None
        else:
            self.load_range_10_lower_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.load_range_10_upper_limit = None
        else:
            self.load_range_10_upper_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.range_10_equipment_list_name = None
        else:
            self.range_10_equipment_list_name = vals[i]
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
    def load_range_1_lower_limit(self):
        """Get load_range_1_lower_limit

        Returns:
            float: the value of `load_range_1_lower_limit` or None if not set
        """
        return self._data["Load Range 1 Lower Limit"]

    @load_range_1_lower_limit.setter
    def load_range_1_lower_limit(self, value=None):
        """  Corresponds to IDD Field `Load Range 1 Lower Limit`

        Args:
            value (float): value for IDD Field `Load Range 1 Lower Limit`
                Units: W
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
                                 'for field `load_range_1_lower_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `load_range_1_lower_limit`')
        self._data["Load Range 1 Lower Limit"] = value

    @property
    def load_range_1_upper_limit(self):
        """Get load_range_1_upper_limit

        Returns:
            float: the value of `load_range_1_upper_limit` or None if not set
        """
        return self._data["Load Range 1 Upper Limit"]

    @load_range_1_upper_limit.setter
    def load_range_1_upper_limit(self, value=None):
        """  Corresponds to IDD Field `Load Range 1 Upper Limit`

        Args:
            value (float): value for IDD Field `Load Range 1 Upper Limit`
                Units: W
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
                                 'for field `load_range_1_upper_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `load_range_1_upper_limit`')
        self._data["Load Range 1 Upper Limit"] = value

    @property
    def range_1_equipment_list_name(self):
        """Get range_1_equipment_list_name

        Returns:
            str: the value of `range_1_equipment_list_name` or None if not set
        """
        return self._data["Range 1 Equipment List Name"]

    @range_1_equipment_list_name.setter
    def range_1_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `Range 1 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 1 Equipment List Name`
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
                                 'for field `range_1_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_1_equipment_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `range_1_equipment_list_name`')
        self._data["Range 1 Equipment List Name"] = value

    @property
    def load_range_2_lower_limit(self):
        """Get load_range_2_lower_limit

        Returns:
            float: the value of `load_range_2_lower_limit` or None if not set
        """
        return self._data["Load Range 2 Lower Limit"]

    @load_range_2_lower_limit.setter
    def load_range_2_lower_limit(self, value=None):
        """  Corresponds to IDD Field `Load Range 2 Lower Limit`

        Args:
            value (float): value for IDD Field `Load Range 2 Lower Limit`
                Units: W
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
                                 'for field `load_range_2_lower_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `load_range_2_lower_limit`')
        self._data["Load Range 2 Lower Limit"] = value

    @property
    def load_range_2_upper_limit(self):
        """Get load_range_2_upper_limit

        Returns:
            float: the value of `load_range_2_upper_limit` or None if not set
        """
        return self._data["Load Range 2 Upper Limit"]

    @load_range_2_upper_limit.setter
    def load_range_2_upper_limit(self, value=None):
        """  Corresponds to IDD Field `Load Range 2 Upper Limit`

        Args:
            value (float): value for IDD Field `Load Range 2 Upper Limit`
                Units: W
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
                                 'for field `load_range_2_upper_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `load_range_2_upper_limit`')
        self._data["Load Range 2 Upper Limit"] = value

    @property
    def range_2_equipment_list_name(self):
        """Get range_2_equipment_list_name

        Returns:
            str: the value of `range_2_equipment_list_name` or None if not set
        """
        return self._data["Range 2 Equipment List Name"]

    @range_2_equipment_list_name.setter
    def range_2_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `Range 2 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 2 Equipment List Name`
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
                                 'for field `range_2_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_2_equipment_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `range_2_equipment_list_name`')
        self._data["Range 2 Equipment List Name"] = value

    @property
    def load_range_3_lower_limit(self):
        """Get load_range_3_lower_limit

        Returns:
            float: the value of `load_range_3_lower_limit` or None if not set
        """
        return self._data["Load Range 3 Lower Limit"]

    @load_range_3_lower_limit.setter
    def load_range_3_lower_limit(self, value=None):
        """  Corresponds to IDD Field `Load Range 3 Lower Limit`

        Args:
            value (float): value for IDD Field `Load Range 3 Lower Limit`
                Units: W
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
                                 'for field `load_range_3_lower_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `load_range_3_lower_limit`')
        self._data["Load Range 3 Lower Limit"] = value

    @property
    def load_range_3_upper_limit(self):
        """Get load_range_3_upper_limit

        Returns:
            float: the value of `load_range_3_upper_limit` or None if not set
        """
        return self._data["Load Range 3 Upper Limit"]

    @load_range_3_upper_limit.setter
    def load_range_3_upper_limit(self, value=None):
        """  Corresponds to IDD Field `Load Range 3 Upper Limit`

        Args:
            value (float): value for IDD Field `Load Range 3 Upper Limit`
                Units: W
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
                                 'for field `load_range_3_upper_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `load_range_3_upper_limit`')
        self._data["Load Range 3 Upper Limit"] = value

    @property
    def range_3_equipment_list_name(self):
        """Get range_3_equipment_list_name

        Returns:
            str: the value of `range_3_equipment_list_name` or None if not set
        """
        return self._data["Range 3 Equipment List Name"]

    @range_3_equipment_list_name.setter
    def range_3_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `Range 3 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 3 Equipment List Name`
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
                                 'for field `range_3_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_3_equipment_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `range_3_equipment_list_name`')
        self._data["Range 3 Equipment List Name"] = value

    @property
    def load_range_4_lower_limit(self):
        """Get load_range_4_lower_limit

        Returns:
            float: the value of `load_range_4_lower_limit` or None if not set
        """
        return self._data["Load Range 4 Lower Limit"]

    @load_range_4_lower_limit.setter
    def load_range_4_lower_limit(self, value=None):
        """  Corresponds to IDD Field `Load Range 4 Lower Limit`

        Args:
            value (float): value for IDD Field `Load Range 4 Lower Limit`
                Units: W
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
                                 'for field `load_range_4_lower_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `load_range_4_lower_limit`')
        self._data["Load Range 4 Lower Limit"] = value

    @property
    def load_range_4_upper_limit(self):
        """Get load_range_4_upper_limit

        Returns:
            float: the value of `load_range_4_upper_limit` or None if not set
        """
        return self._data["Load Range 4 Upper Limit"]

    @load_range_4_upper_limit.setter
    def load_range_4_upper_limit(self, value=None):
        """  Corresponds to IDD Field `Load Range 4 Upper Limit`

        Args:
            value (float): value for IDD Field `Load Range 4 Upper Limit`
                Units: W
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
                                 'for field `load_range_4_upper_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `load_range_4_upper_limit`')
        self._data["Load Range 4 Upper Limit"] = value

    @property
    def range_4_equipment_list_name(self):
        """Get range_4_equipment_list_name

        Returns:
            str: the value of `range_4_equipment_list_name` or None if not set
        """
        return self._data["Range 4 Equipment List Name"]

    @range_4_equipment_list_name.setter
    def range_4_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `Range 4 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 4 Equipment List Name`
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
                                 'for field `range_4_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_4_equipment_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `range_4_equipment_list_name`')
        self._data["Range 4 Equipment List Name"] = value

    @property
    def load_range_5_lower_limit(self):
        """Get load_range_5_lower_limit

        Returns:
            float: the value of `load_range_5_lower_limit` or None if not set
        """
        return self._data["Load Range 5 Lower Limit"]

    @load_range_5_lower_limit.setter
    def load_range_5_lower_limit(self, value=None):
        """  Corresponds to IDD Field `Load Range 5 Lower Limit`

        Args:
            value (float): value for IDD Field `Load Range 5 Lower Limit`
                Units: W
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
                                 'for field `load_range_5_lower_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `load_range_5_lower_limit`')
        self._data["Load Range 5 Lower Limit"] = value

    @property
    def load_range_5_upper_limit(self):
        """Get load_range_5_upper_limit

        Returns:
            float: the value of `load_range_5_upper_limit` or None if not set
        """
        return self._data["Load Range 5 Upper Limit"]

    @load_range_5_upper_limit.setter
    def load_range_5_upper_limit(self, value=None):
        """  Corresponds to IDD Field `Load Range 5 Upper Limit`

        Args:
            value (float): value for IDD Field `Load Range 5 Upper Limit`
                Units: W
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
                                 'for field `load_range_5_upper_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `load_range_5_upper_limit`')
        self._data["Load Range 5 Upper Limit"] = value

    @property
    def range_5_equipment_list_name(self):
        """Get range_5_equipment_list_name

        Returns:
            str: the value of `range_5_equipment_list_name` or None if not set
        """
        return self._data["Range 5 Equipment List Name"]

    @range_5_equipment_list_name.setter
    def range_5_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `Range 5 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 5 Equipment List Name`
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
                                 'for field `range_5_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_5_equipment_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `range_5_equipment_list_name`')
        self._data["Range 5 Equipment List Name"] = value

    @property
    def load_range_6_lower_limit(self):
        """Get load_range_6_lower_limit

        Returns:
            float: the value of `load_range_6_lower_limit` or None if not set
        """
        return self._data["Load Range 6 Lower Limit"]

    @load_range_6_lower_limit.setter
    def load_range_6_lower_limit(self, value=None):
        """  Corresponds to IDD Field `Load Range 6 Lower Limit`

        Args:
            value (float): value for IDD Field `Load Range 6 Lower Limit`
                Units: W
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
                                 'for field `load_range_6_lower_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `load_range_6_lower_limit`')
        self._data["Load Range 6 Lower Limit"] = value

    @property
    def load_range_6_upper_limit(self):
        """Get load_range_6_upper_limit

        Returns:
            float: the value of `load_range_6_upper_limit` or None if not set
        """
        return self._data["Load Range 6 Upper Limit"]

    @load_range_6_upper_limit.setter
    def load_range_6_upper_limit(self, value=None):
        """  Corresponds to IDD Field `Load Range 6 Upper Limit`

        Args:
            value (float): value for IDD Field `Load Range 6 Upper Limit`
                Units: W
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
                                 'for field `load_range_6_upper_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `load_range_6_upper_limit`')
        self._data["Load Range 6 Upper Limit"] = value

    @property
    def range_6_equipment_list_name(self):
        """Get range_6_equipment_list_name

        Returns:
            str: the value of `range_6_equipment_list_name` or None if not set
        """
        return self._data["Range 6 Equipment List Name"]

    @range_6_equipment_list_name.setter
    def range_6_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `Range 6 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 6 Equipment List Name`
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
                                 'for field `range_6_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_6_equipment_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `range_6_equipment_list_name`')
        self._data["Range 6 Equipment List Name"] = value

    @property
    def load_range_7_lower_limit(self):
        """Get load_range_7_lower_limit

        Returns:
            float: the value of `load_range_7_lower_limit` or None if not set
        """
        return self._data["Load Range 7 Lower Limit"]

    @load_range_7_lower_limit.setter
    def load_range_7_lower_limit(self, value=None):
        """  Corresponds to IDD Field `Load Range 7 Lower Limit`

        Args:
            value (float): value for IDD Field `Load Range 7 Lower Limit`
                Units: W
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
                                 'for field `load_range_7_lower_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `load_range_7_lower_limit`')
        self._data["Load Range 7 Lower Limit"] = value

    @property
    def load_range_7_upper_limit(self):
        """Get load_range_7_upper_limit

        Returns:
            float: the value of `load_range_7_upper_limit` or None if not set
        """
        return self._data["Load Range 7 Upper Limit"]

    @load_range_7_upper_limit.setter
    def load_range_7_upper_limit(self, value=None):
        """  Corresponds to IDD Field `Load Range 7 Upper Limit`

        Args:
            value (float): value for IDD Field `Load Range 7 Upper Limit`
                Units: W
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
                                 'for field `load_range_7_upper_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `load_range_7_upper_limit`')
        self._data["Load Range 7 Upper Limit"] = value

    @property
    def range_7_equipment_list_name(self):
        """Get range_7_equipment_list_name

        Returns:
            str: the value of `range_7_equipment_list_name` or None if not set
        """
        return self._data["Range 7 Equipment List Name"]

    @range_7_equipment_list_name.setter
    def range_7_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `Range 7 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 7 Equipment List Name`
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
                                 'for field `range_7_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_7_equipment_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `range_7_equipment_list_name`')
        self._data["Range 7 Equipment List Name"] = value

    @property
    def load_range_8_lower_limit(self):
        """Get load_range_8_lower_limit

        Returns:
            float: the value of `load_range_8_lower_limit` or None if not set
        """
        return self._data["Load Range 8 Lower Limit"]

    @load_range_8_lower_limit.setter
    def load_range_8_lower_limit(self, value=None):
        """  Corresponds to IDD Field `Load Range 8 Lower Limit`

        Args:
            value (float): value for IDD Field `Load Range 8 Lower Limit`
                Units: W
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
                                 'for field `load_range_8_lower_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `load_range_8_lower_limit`')
        self._data["Load Range 8 Lower Limit"] = value

    @property
    def load_range_8_upper_limit(self):
        """Get load_range_8_upper_limit

        Returns:
            float: the value of `load_range_8_upper_limit` or None if not set
        """
        return self._data["Load Range 8 Upper Limit"]

    @load_range_8_upper_limit.setter
    def load_range_8_upper_limit(self, value=None):
        """  Corresponds to IDD Field `Load Range 8 Upper Limit`

        Args:
            value (float): value for IDD Field `Load Range 8 Upper Limit`
                Units: W
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
                                 'for field `load_range_8_upper_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `load_range_8_upper_limit`')
        self._data["Load Range 8 Upper Limit"] = value

    @property
    def range_8_equipment_list_name(self):
        """Get range_8_equipment_list_name

        Returns:
            str: the value of `range_8_equipment_list_name` or None if not set
        """
        return self._data["Range 8 Equipment List Name"]

    @range_8_equipment_list_name.setter
    def range_8_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `Range 8 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 8 Equipment List Name`
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
                                 'for field `range_8_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_8_equipment_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `range_8_equipment_list_name`')
        self._data["Range 8 Equipment List Name"] = value

    @property
    def load_range_9_lower_limit(self):
        """Get load_range_9_lower_limit

        Returns:
            float: the value of `load_range_9_lower_limit` or None if not set
        """
        return self._data["Load Range 9 Lower Limit"]

    @load_range_9_lower_limit.setter
    def load_range_9_lower_limit(self, value=None):
        """  Corresponds to IDD Field `Load Range 9 Lower Limit`

        Args:
            value (float): value for IDD Field `Load Range 9 Lower Limit`
                Units: W
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
                                 'for field `load_range_9_lower_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `load_range_9_lower_limit`')
        self._data["Load Range 9 Lower Limit"] = value

    @property
    def load_range_9_upper_limit(self):
        """Get load_range_9_upper_limit

        Returns:
            float: the value of `load_range_9_upper_limit` or None if not set
        """
        return self._data["Load Range 9 Upper Limit"]

    @load_range_9_upper_limit.setter
    def load_range_9_upper_limit(self, value=None):
        """  Corresponds to IDD Field `Load Range 9 Upper Limit`

        Args:
            value (float): value for IDD Field `Load Range 9 Upper Limit`
                Units: W
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
                                 'for field `load_range_9_upper_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `load_range_9_upper_limit`')
        self._data["Load Range 9 Upper Limit"] = value

    @property
    def range_9_equipment_list_name(self):
        """Get range_9_equipment_list_name

        Returns:
            str: the value of `range_9_equipment_list_name` or None if not set
        """
        return self._data["Range 9 Equipment List Name"]

    @range_9_equipment_list_name.setter
    def range_9_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `Range 9 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 9 Equipment List Name`
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
                                 'for field `range_9_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_9_equipment_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `range_9_equipment_list_name`')
        self._data["Range 9 Equipment List Name"] = value

    @property
    def load_range_10_lower_limit(self):
        """Get load_range_10_lower_limit

        Returns:
            float: the value of `load_range_10_lower_limit` or None if not set
        """
        return self._data["Load Range 10 Lower Limit"]

    @load_range_10_lower_limit.setter
    def load_range_10_lower_limit(self, value=None):
        """  Corresponds to IDD Field `Load Range 10 Lower Limit`

        Args:
            value (float): value for IDD Field `Load Range 10 Lower Limit`
                Units: W
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
                                 'for field `load_range_10_lower_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `load_range_10_lower_limit`')
        self._data["Load Range 10 Lower Limit"] = value

    @property
    def load_range_10_upper_limit(self):
        """Get load_range_10_upper_limit

        Returns:
            float: the value of `load_range_10_upper_limit` or None if not set
        """
        return self._data["Load Range 10 Upper Limit"]

    @load_range_10_upper_limit.setter
    def load_range_10_upper_limit(self, value=None):
        """  Corresponds to IDD Field `Load Range 10 Upper Limit`

        Args:
            value (float): value for IDD Field `Load Range 10 Upper Limit`
                Units: W
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
                                 'for field `load_range_10_upper_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `load_range_10_upper_limit`')
        self._data["Load Range 10 Upper Limit"] = value

    @property
    def range_10_equipment_list_name(self):
        """Get range_10_equipment_list_name

        Returns:
            str: the value of `range_10_equipment_list_name` or None if not set
        """
        return self._data["Range 10 Equipment List Name"]

    @range_10_equipment_list_name.setter
    def range_10_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `Range 10 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 10 Equipment List Name`
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
                                 'for field `range_10_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_10_equipment_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `range_10_equipment_list_name`')
        self._data["Range 10 Equipment List Name"] = value

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

class PlantEquipmentOperationOutdoorDryBulb(object):
    """ Corresponds to IDD object `PlantEquipmentOperation:OutdoorDryBulb`
        Plant equipment operation scheme for outdoor dry-bulb temperature range operation.
        Specifies one or more groups of equipment which are available to operate for
        successive outdoor dry-bulb temperature ranges.
    
    """
    internal_name = "PlantEquipmentOperation:OutdoorDryBulb"
    field_count = 31
    required_fields = ["Name", "Dry-Bulb Temperature Range 1 Lower Limit", "Dry-Bulb Temperature Range 1 Upper Limit", "Range 1 Equipment List Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `PlantEquipmentOperation:OutdoorDryBulb`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Dry-Bulb Temperature Range 1 Lower Limit"] = None
        self._data["Dry-Bulb Temperature Range 1 Upper Limit"] = None
        self._data["Range 1 Equipment List Name"] = None
        self._data["Dry-Bulb Temperature Range 2 Lower Limit"] = None
        self._data["Dry-Bulb Temperature Range 2 Upper Limit"] = None
        self._data["Range 2 Equipment List Name"] = None
        self._data["Dry-Bulb Temperature Range 3 Lower Limit"] = None
        self._data["Dry-Bulb Temperature Range 3 Upper Limit"] = None
        self._data["Range 3 Equipment List Name"] = None
        self._data["Dry-Bulb Temperature Range 4 Lower Limit"] = None
        self._data["Dry-Bulb Temperature Range 4 Upper Limit"] = None
        self._data["Range 4 Equipment List Name"] = None
        self._data["Dry-Bulb Temperature Range 5 Lower Limit"] = None
        self._data["Dry-Bulb Temperature Range 5 Upper Limit"] = None
        self._data["Range 5 Equipment List Name"] = None
        self._data["Dry-Bulb Temperature Range 6 Lower Limit"] = None
        self._data["Dry-Bulb Temperature Range 6 Upper Limit"] = None
        self._data["Range 6 Equipment List Name"] = None
        self._data["Dry-Bulb Temperature Range 7 Lower Limit"] = None
        self._data["Dry-Bulb Temperature Range 7 Upper Limit"] = None
        self._data["Range 7 Equipment List Name"] = None
        self._data["Dry-Bulb Temperature Range 8 Lower Limit"] = None
        self._data["Dry-Bulb Temperature Range 8 Upper Limit"] = None
        self._data["Range 8 Equipment List Name"] = None
        self._data["Dry-Bulb Temperature Range 9 Lower Limit"] = None
        self._data["Dry-Bulb Temperature Range 9 Upper Limit"] = None
        self._data["Range 9 Equipment List Name"] = None
        self._data["Dry-Bulb Temperature Range 10 Lower Limit"] = None
        self._data["Dry-Bulb Temperature Range 10 Upper Limit"] = None
        self._data["Range 10 Equipment List Name"] = None
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
            self.drybulb_temperature_range_1_lower_limit = None
        else:
            self.drybulb_temperature_range_1_lower_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.drybulb_temperature_range_1_upper_limit = None
        else:
            self.drybulb_temperature_range_1_upper_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.range_1_equipment_list_name = None
        else:
            self.range_1_equipment_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.drybulb_temperature_range_2_lower_limit = None
        else:
            self.drybulb_temperature_range_2_lower_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.drybulb_temperature_range_2_upper_limit = None
        else:
            self.drybulb_temperature_range_2_upper_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.range_2_equipment_list_name = None
        else:
            self.range_2_equipment_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.drybulb_temperature_range_3_lower_limit = None
        else:
            self.drybulb_temperature_range_3_lower_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.drybulb_temperature_range_3_upper_limit = None
        else:
            self.drybulb_temperature_range_3_upper_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.range_3_equipment_list_name = None
        else:
            self.range_3_equipment_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.drybulb_temperature_range_4_lower_limit = None
        else:
            self.drybulb_temperature_range_4_lower_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.drybulb_temperature_range_4_upper_limit = None
        else:
            self.drybulb_temperature_range_4_upper_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.range_4_equipment_list_name = None
        else:
            self.range_4_equipment_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.drybulb_temperature_range_5_lower_limit = None
        else:
            self.drybulb_temperature_range_5_lower_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.drybulb_temperature_range_5_upper_limit = None
        else:
            self.drybulb_temperature_range_5_upper_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.range_5_equipment_list_name = None
        else:
            self.range_5_equipment_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.drybulb_temperature_range_6_lower_limit = None
        else:
            self.drybulb_temperature_range_6_lower_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.drybulb_temperature_range_6_upper_limit = None
        else:
            self.drybulb_temperature_range_6_upper_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.range_6_equipment_list_name = None
        else:
            self.range_6_equipment_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.drybulb_temperature_range_7_lower_limit = None
        else:
            self.drybulb_temperature_range_7_lower_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.drybulb_temperature_range_7_upper_limit = None
        else:
            self.drybulb_temperature_range_7_upper_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.range_7_equipment_list_name = None
        else:
            self.range_7_equipment_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.drybulb_temperature_range_8_lower_limit = None
        else:
            self.drybulb_temperature_range_8_lower_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.drybulb_temperature_range_8_upper_limit = None
        else:
            self.drybulb_temperature_range_8_upper_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.range_8_equipment_list_name = None
        else:
            self.range_8_equipment_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.drybulb_temperature_range_9_lower_limit = None
        else:
            self.drybulb_temperature_range_9_lower_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.drybulb_temperature_range_9_upper_limit = None
        else:
            self.drybulb_temperature_range_9_upper_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.range_9_equipment_list_name = None
        else:
            self.range_9_equipment_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.drybulb_temperature_range_10_lower_limit = None
        else:
            self.drybulb_temperature_range_10_lower_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.drybulb_temperature_range_10_upper_limit = None
        else:
            self.drybulb_temperature_range_10_upper_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.range_10_equipment_list_name = None
        else:
            self.range_10_equipment_list_name = vals[i]
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
    def drybulb_temperature_range_1_lower_limit(self):
        """Get drybulb_temperature_range_1_lower_limit

        Returns:
            float: the value of `drybulb_temperature_range_1_lower_limit` or None if not set
        """
        return self._data["Dry-Bulb Temperature Range 1 Lower Limit"]

    @drybulb_temperature_range_1_lower_limit.setter
    def drybulb_temperature_range_1_lower_limit(self, value=None):
        """  Corresponds to IDD Field `Dry-Bulb Temperature Range 1 Lower Limit`

        Args:
            value (float): value for IDD Field `Dry-Bulb Temperature Range 1 Lower Limit`
                Units: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `drybulb_temperature_range_1_lower_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `drybulb_temperature_range_1_lower_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `drybulb_temperature_range_1_lower_limit`')
        self._data["Dry-Bulb Temperature Range 1 Lower Limit"] = value

    @property
    def drybulb_temperature_range_1_upper_limit(self):
        """Get drybulb_temperature_range_1_upper_limit

        Returns:
            float: the value of `drybulb_temperature_range_1_upper_limit` or None if not set
        """
        return self._data["Dry-Bulb Temperature Range 1 Upper Limit"]

    @drybulb_temperature_range_1_upper_limit.setter
    def drybulb_temperature_range_1_upper_limit(self, value=None):
        """  Corresponds to IDD Field `Dry-Bulb Temperature Range 1 Upper Limit`

        Args:
            value (float): value for IDD Field `Dry-Bulb Temperature Range 1 Upper Limit`
                Units: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `drybulb_temperature_range_1_upper_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `drybulb_temperature_range_1_upper_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `drybulb_temperature_range_1_upper_limit`')
        self._data["Dry-Bulb Temperature Range 1 Upper Limit"] = value

    @property
    def range_1_equipment_list_name(self):
        """Get range_1_equipment_list_name

        Returns:
            str: the value of `range_1_equipment_list_name` or None if not set
        """
        return self._data["Range 1 Equipment List Name"]

    @range_1_equipment_list_name.setter
    def range_1_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `Range 1 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 1 Equipment List Name`
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
                                 'for field `range_1_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_1_equipment_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `range_1_equipment_list_name`')
        self._data["Range 1 Equipment List Name"] = value

    @property
    def drybulb_temperature_range_2_lower_limit(self):
        """Get drybulb_temperature_range_2_lower_limit

        Returns:
            float: the value of `drybulb_temperature_range_2_lower_limit` or None if not set
        """
        return self._data["Dry-Bulb Temperature Range 2 Lower Limit"]

    @drybulb_temperature_range_2_lower_limit.setter
    def drybulb_temperature_range_2_lower_limit(self, value=None):
        """  Corresponds to IDD Field `Dry-Bulb Temperature Range 2 Lower Limit`

        Args:
            value (float): value for IDD Field `Dry-Bulb Temperature Range 2 Lower Limit`
                Units: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `drybulb_temperature_range_2_lower_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `drybulb_temperature_range_2_lower_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `drybulb_temperature_range_2_lower_limit`')
        self._data["Dry-Bulb Temperature Range 2 Lower Limit"] = value

    @property
    def drybulb_temperature_range_2_upper_limit(self):
        """Get drybulb_temperature_range_2_upper_limit

        Returns:
            float: the value of `drybulb_temperature_range_2_upper_limit` or None if not set
        """
        return self._data["Dry-Bulb Temperature Range 2 Upper Limit"]

    @drybulb_temperature_range_2_upper_limit.setter
    def drybulb_temperature_range_2_upper_limit(self, value=None):
        """  Corresponds to IDD Field `Dry-Bulb Temperature Range 2 Upper Limit`

        Args:
            value (float): value for IDD Field `Dry-Bulb Temperature Range 2 Upper Limit`
                Units: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `drybulb_temperature_range_2_upper_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `drybulb_temperature_range_2_upper_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `drybulb_temperature_range_2_upper_limit`')
        self._data["Dry-Bulb Temperature Range 2 Upper Limit"] = value

    @property
    def range_2_equipment_list_name(self):
        """Get range_2_equipment_list_name

        Returns:
            str: the value of `range_2_equipment_list_name` or None if not set
        """
        return self._data["Range 2 Equipment List Name"]

    @range_2_equipment_list_name.setter
    def range_2_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `Range 2 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 2 Equipment List Name`
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
                                 'for field `range_2_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_2_equipment_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `range_2_equipment_list_name`')
        self._data["Range 2 Equipment List Name"] = value

    @property
    def drybulb_temperature_range_3_lower_limit(self):
        """Get drybulb_temperature_range_3_lower_limit

        Returns:
            float: the value of `drybulb_temperature_range_3_lower_limit` or None if not set
        """
        return self._data["Dry-Bulb Temperature Range 3 Lower Limit"]

    @drybulb_temperature_range_3_lower_limit.setter
    def drybulb_temperature_range_3_lower_limit(self, value=None):
        """  Corresponds to IDD Field `Dry-Bulb Temperature Range 3 Lower Limit`

        Args:
            value (float): value for IDD Field `Dry-Bulb Temperature Range 3 Lower Limit`
                Units: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `drybulb_temperature_range_3_lower_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `drybulb_temperature_range_3_lower_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `drybulb_temperature_range_3_lower_limit`')
        self._data["Dry-Bulb Temperature Range 3 Lower Limit"] = value

    @property
    def drybulb_temperature_range_3_upper_limit(self):
        """Get drybulb_temperature_range_3_upper_limit

        Returns:
            float: the value of `drybulb_temperature_range_3_upper_limit` or None if not set
        """
        return self._data["Dry-Bulb Temperature Range 3 Upper Limit"]

    @drybulb_temperature_range_3_upper_limit.setter
    def drybulb_temperature_range_3_upper_limit(self, value=None):
        """  Corresponds to IDD Field `Dry-Bulb Temperature Range 3 Upper Limit`

        Args:
            value (float): value for IDD Field `Dry-Bulb Temperature Range 3 Upper Limit`
                Units: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `drybulb_temperature_range_3_upper_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `drybulb_temperature_range_3_upper_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `drybulb_temperature_range_3_upper_limit`')
        self._data["Dry-Bulb Temperature Range 3 Upper Limit"] = value

    @property
    def range_3_equipment_list_name(self):
        """Get range_3_equipment_list_name

        Returns:
            str: the value of `range_3_equipment_list_name` or None if not set
        """
        return self._data["Range 3 Equipment List Name"]

    @range_3_equipment_list_name.setter
    def range_3_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `Range 3 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 3 Equipment List Name`
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
                                 'for field `range_3_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_3_equipment_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `range_3_equipment_list_name`')
        self._data["Range 3 Equipment List Name"] = value

    @property
    def drybulb_temperature_range_4_lower_limit(self):
        """Get drybulb_temperature_range_4_lower_limit

        Returns:
            float: the value of `drybulb_temperature_range_4_lower_limit` or None if not set
        """
        return self._data["Dry-Bulb Temperature Range 4 Lower Limit"]

    @drybulb_temperature_range_4_lower_limit.setter
    def drybulb_temperature_range_4_lower_limit(self, value=None):
        """  Corresponds to IDD Field `Dry-Bulb Temperature Range 4 Lower Limit`

        Args:
            value (float): value for IDD Field `Dry-Bulb Temperature Range 4 Lower Limit`
                Units: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `drybulb_temperature_range_4_lower_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `drybulb_temperature_range_4_lower_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `drybulb_temperature_range_4_lower_limit`')
        self._data["Dry-Bulb Temperature Range 4 Lower Limit"] = value

    @property
    def drybulb_temperature_range_4_upper_limit(self):
        """Get drybulb_temperature_range_4_upper_limit

        Returns:
            float: the value of `drybulb_temperature_range_4_upper_limit` or None if not set
        """
        return self._data["Dry-Bulb Temperature Range 4 Upper Limit"]

    @drybulb_temperature_range_4_upper_limit.setter
    def drybulb_temperature_range_4_upper_limit(self, value=None):
        """  Corresponds to IDD Field `Dry-Bulb Temperature Range 4 Upper Limit`

        Args:
            value (float): value for IDD Field `Dry-Bulb Temperature Range 4 Upper Limit`
                Units: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `drybulb_temperature_range_4_upper_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `drybulb_temperature_range_4_upper_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `drybulb_temperature_range_4_upper_limit`')
        self._data["Dry-Bulb Temperature Range 4 Upper Limit"] = value

    @property
    def range_4_equipment_list_name(self):
        """Get range_4_equipment_list_name

        Returns:
            str: the value of `range_4_equipment_list_name` or None if not set
        """
        return self._data["Range 4 Equipment List Name"]

    @range_4_equipment_list_name.setter
    def range_4_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `Range 4 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 4 Equipment List Name`
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
                                 'for field `range_4_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_4_equipment_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `range_4_equipment_list_name`')
        self._data["Range 4 Equipment List Name"] = value

    @property
    def drybulb_temperature_range_5_lower_limit(self):
        """Get drybulb_temperature_range_5_lower_limit

        Returns:
            float: the value of `drybulb_temperature_range_5_lower_limit` or None if not set
        """
        return self._data["Dry-Bulb Temperature Range 5 Lower Limit"]

    @drybulb_temperature_range_5_lower_limit.setter
    def drybulb_temperature_range_5_lower_limit(self, value=None):
        """  Corresponds to IDD Field `Dry-Bulb Temperature Range 5 Lower Limit`

        Args:
            value (float): value for IDD Field `Dry-Bulb Temperature Range 5 Lower Limit`
                Units: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `drybulb_temperature_range_5_lower_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `drybulb_temperature_range_5_lower_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `drybulb_temperature_range_5_lower_limit`')
        self._data["Dry-Bulb Temperature Range 5 Lower Limit"] = value

    @property
    def drybulb_temperature_range_5_upper_limit(self):
        """Get drybulb_temperature_range_5_upper_limit

        Returns:
            float: the value of `drybulb_temperature_range_5_upper_limit` or None if not set
        """
        return self._data["Dry-Bulb Temperature Range 5 Upper Limit"]

    @drybulb_temperature_range_5_upper_limit.setter
    def drybulb_temperature_range_5_upper_limit(self, value=None):
        """  Corresponds to IDD Field `Dry-Bulb Temperature Range 5 Upper Limit`

        Args:
            value (float): value for IDD Field `Dry-Bulb Temperature Range 5 Upper Limit`
                Units: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `drybulb_temperature_range_5_upper_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `drybulb_temperature_range_5_upper_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `drybulb_temperature_range_5_upper_limit`')
        self._data["Dry-Bulb Temperature Range 5 Upper Limit"] = value

    @property
    def range_5_equipment_list_name(self):
        """Get range_5_equipment_list_name

        Returns:
            str: the value of `range_5_equipment_list_name` or None if not set
        """
        return self._data["Range 5 Equipment List Name"]

    @range_5_equipment_list_name.setter
    def range_5_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `Range 5 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 5 Equipment List Name`
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
                                 'for field `range_5_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_5_equipment_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `range_5_equipment_list_name`')
        self._data["Range 5 Equipment List Name"] = value

    @property
    def drybulb_temperature_range_6_lower_limit(self):
        """Get drybulb_temperature_range_6_lower_limit

        Returns:
            float: the value of `drybulb_temperature_range_6_lower_limit` or None if not set
        """
        return self._data["Dry-Bulb Temperature Range 6 Lower Limit"]

    @drybulb_temperature_range_6_lower_limit.setter
    def drybulb_temperature_range_6_lower_limit(self, value=None):
        """  Corresponds to IDD Field `Dry-Bulb Temperature Range 6 Lower Limit`

        Args:
            value (float): value for IDD Field `Dry-Bulb Temperature Range 6 Lower Limit`
                Units: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `drybulb_temperature_range_6_lower_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `drybulb_temperature_range_6_lower_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `drybulb_temperature_range_6_lower_limit`')
        self._data["Dry-Bulb Temperature Range 6 Lower Limit"] = value

    @property
    def drybulb_temperature_range_6_upper_limit(self):
        """Get drybulb_temperature_range_6_upper_limit

        Returns:
            float: the value of `drybulb_temperature_range_6_upper_limit` or None if not set
        """
        return self._data["Dry-Bulb Temperature Range 6 Upper Limit"]

    @drybulb_temperature_range_6_upper_limit.setter
    def drybulb_temperature_range_6_upper_limit(self, value=None):
        """  Corresponds to IDD Field `Dry-Bulb Temperature Range 6 Upper Limit`

        Args:
            value (float): value for IDD Field `Dry-Bulb Temperature Range 6 Upper Limit`
                Units: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `drybulb_temperature_range_6_upper_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `drybulb_temperature_range_6_upper_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `drybulb_temperature_range_6_upper_limit`')
        self._data["Dry-Bulb Temperature Range 6 Upper Limit"] = value

    @property
    def range_6_equipment_list_name(self):
        """Get range_6_equipment_list_name

        Returns:
            str: the value of `range_6_equipment_list_name` or None if not set
        """
        return self._data["Range 6 Equipment List Name"]

    @range_6_equipment_list_name.setter
    def range_6_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `Range 6 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 6 Equipment List Name`
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
                                 'for field `range_6_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_6_equipment_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `range_6_equipment_list_name`')
        self._data["Range 6 Equipment List Name"] = value

    @property
    def drybulb_temperature_range_7_lower_limit(self):
        """Get drybulb_temperature_range_7_lower_limit

        Returns:
            float: the value of `drybulb_temperature_range_7_lower_limit` or None if not set
        """
        return self._data["Dry-Bulb Temperature Range 7 Lower Limit"]

    @drybulb_temperature_range_7_lower_limit.setter
    def drybulb_temperature_range_7_lower_limit(self, value=None):
        """  Corresponds to IDD Field `Dry-Bulb Temperature Range 7 Lower Limit`

        Args:
            value (float): value for IDD Field `Dry-Bulb Temperature Range 7 Lower Limit`
                Units: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `drybulb_temperature_range_7_lower_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `drybulb_temperature_range_7_lower_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `drybulb_temperature_range_7_lower_limit`')
        self._data["Dry-Bulb Temperature Range 7 Lower Limit"] = value

    @property
    def drybulb_temperature_range_7_upper_limit(self):
        """Get drybulb_temperature_range_7_upper_limit

        Returns:
            float: the value of `drybulb_temperature_range_7_upper_limit` or None if not set
        """
        return self._data["Dry-Bulb Temperature Range 7 Upper Limit"]

    @drybulb_temperature_range_7_upper_limit.setter
    def drybulb_temperature_range_7_upper_limit(self, value=None):
        """  Corresponds to IDD Field `Dry-Bulb Temperature Range 7 Upper Limit`

        Args:
            value (float): value for IDD Field `Dry-Bulb Temperature Range 7 Upper Limit`
                Units: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `drybulb_temperature_range_7_upper_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `drybulb_temperature_range_7_upper_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `drybulb_temperature_range_7_upper_limit`')
        self._data["Dry-Bulb Temperature Range 7 Upper Limit"] = value

    @property
    def range_7_equipment_list_name(self):
        """Get range_7_equipment_list_name

        Returns:
            str: the value of `range_7_equipment_list_name` or None if not set
        """
        return self._data["Range 7 Equipment List Name"]

    @range_7_equipment_list_name.setter
    def range_7_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `Range 7 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 7 Equipment List Name`
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
                                 'for field `range_7_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_7_equipment_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `range_7_equipment_list_name`')
        self._data["Range 7 Equipment List Name"] = value

    @property
    def drybulb_temperature_range_8_lower_limit(self):
        """Get drybulb_temperature_range_8_lower_limit

        Returns:
            float: the value of `drybulb_temperature_range_8_lower_limit` or None if not set
        """
        return self._data["Dry-Bulb Temperature Range 8 Lower Limit"]

    @drybulb_temperature_range_8_lower_limit.setter
    def drybulb_temperature_range_8_lower_limit(self, value=None):
        """  Corresponds to IDD Field `Dry-Bulb Temperature Range 8 Lower Limit`

        Args:
            value (float): value for IDD Field `Dry-Bulb Temperature Range 8 Lower Limit`
                Units: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `drybulb_temperature_range_8_lower_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `drybulb_temperature_range_8_lower_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `drybulb_temperature_range_8_lower_limit`')
        self._data["Dry-Bulb Temperature Range 8 Lower Limit"] = value

    @property
    def drybulb_temperature_range_8_upper_limit(self):
        """Get drybulb_temperature_range_8_upper_limit

        Returns:
            float: the value of `drybulb_temperature_range_8_upper_limit` or None if not set
        """
        return self._data["Dry-Bulb Temperature Range 8 Upper Limit"]

    @drybulb_temperature_range_8_upper_limit.setter
    def drybulb_temperature_range_8_upper_limit(self, value=None):
        """  Corresponds to IDD Field `Dry-Bulb Temperature Range 8 Upper Limit`

        Args:
            value (float): value for IDD Field `Dry-Bulb Temperature Range 8 Upper Limit`
                Units: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `drybulb_temperature_range_8_upper_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `drybulb_temperature_range_8_upper_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `drybulb_temperature_range_8_upper_limit`')
        self._data["Dry-Bulb Temperature Range 8 Upper Limit"] = value

    @property
    def range_8_equipment_list_name(self):
        """Get range_8_equipment_list_name

        Returns:
            str: the value of `range_8_equipment_list_name` or None if not set
        """
        return self._data["Range 8 Equipment List Name"]

    @range_8_equipment_list_name.setter
    def range_8_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `Range 8 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 8 Equipment List Name`
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
                                 'for field `range_8_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_8_equipment_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `range_8_equipment_list_name`')
        self._data["Range 8 Equipment List Name"] = value

    @property
    def drybulb_temperature_range_9_lower_limit(self):
        """Get drybulb_temperature_range_9_lower_limit

        Returns:
            float: the value of `drybulb_temperature_range_9_lower_limit` or None if not set
        """
        return self._data["Dry-Bulb Temperature Range 9 Lower Limit"]

    @drybulb_temperature_range_9_lower_limit.setter
    def drybulb_temperature_range_9_lower_limit(self, value=None):
        """  Corresponds to IDD Field `Dry-Bulb Temperature Range 9 Lower Limit`

        Args:
            value (float): value for IDD Field `Dry-Bulb Temperature Range 9 Lower Limit`
                Units: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `drybulb_temperature_range_9_lower_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `drybulb_temperature_range_9_lower_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `drybulb_temperature_range_9_lower_limit`')
        self._data["Dry-Bulb Temperature Range 9 Lower Limit"] = value

    @property
    def drybulb_temperature_range_9_upper_limit(self):
        """Get drybulb_temperature_range_9_upper_limit

        Returns:
            float: the value of `drybulb_temperature_range_9_upper_limit` or None if not set
        """
        return self._data["Dry-Bulb Temperature Range 9 Upper Limit"]

    @drybulb_temperature_range_9_upper_limit.setter
    def drybulb_temperature_range_9_upper_limit(self, value=None):
        """  Corresponds to IDD Field `Dry-Bulb Temperature Range 9 Upper Limit`

        Args:
            value (float): value for IDD Field `Dry-Bulb Temperature Range 9 Upper Limit`
                Units: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `drybulb_temperature_range_9_upper_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `drybulb_temperature_range_9_upper_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `drybulb_temperature_range_9_upper_limit`')
        self._data["Dry-Bulb Temperature Range 9 Upper Limit"] = value

    @property
    def range_9_equipment_list_name(self):
        """Get range_9_equipment_list_name

        Returns:
            str: the value of `range_9_equipment_list_name` or None if not set
        """
        return self._data["Range 9 Equipment List Name"]

    @range_9_equipment_list_name.setter
    def range_9_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `Range 9 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 9 Equipment List Name`
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
                                 'for field `range_9_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_9_equipment_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `range_9_equipment_list_name`')
        self._data["Range 9 Equipment List Name"] = value

    @property
    def drybulb_temperature_range_10_lower_limit(self):
        """Get drybulb_temperature_range_10_lower_limit

        Returns:
            float: the value of `drybulb_temperature_range_10_lower_limit` or None if not set
        """
        return self._data["Dry-Bulb Temperature Range 10 Lower Limit"]

    @drybulb_temperature_range_10_lower_limit.setter
    def drybulb_temperature_range_10_lower_limit(self, value=None):
        """  Corresponds to IDD Field `Dry-Bulb Temperature Range 10 Lower Limit`

        Args:
            value (float): value for IDD Field `Dry-Bulb Temperature Range 10 Lower Limit`
                Units: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `drybulb_temperature_range_10_lower_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `drybulb_temperature_range_10_lower_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `drybulb_temperature_range_10_lower_limit`')
        self._data["Dry-Bulb Temperature Range 10 Lower Limit"] = value

    @property
    def drybulb_temperature_range_10_upper_limit(self):
        """Get drybulb_temperature_range_10_upper_limit

        Returns:
            float: the value of `drybulb_temperature_range_10_upper_limit` or None if not set
        """
        return self._data["Dry-Bulb Temperature Range 10 Upper Limit"]

    @drybulb_temperature_range_10_upper_limit.setter
    def drybulb_temperature_range_10_upper_limit(self, value=None):
        """  Corresponds to IDD Field `Dry-Bulb Temperature Range 10 Upper Limit`

        Args:
            value (float): value for IDD Field `Dry-Bulb Temperature Range 10 Upper Limit`
                Units: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `drybulb_temperature_range_10_upper_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `drybulb_temperature_range_10_upper_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `drybulb_temperature_range_10_upper_limit`')
        self._data["Dry-Bulb Temperature Range 10 Upper Limit"] = value

    @property
    def range_10_equipment_list_name(self):
        """Get range_10_equipment_list_name

        Returns:
            str: the value of `range_10_equipment_list_name` or None if not set
        """
        return self._data["Range 10 Equipment List Name"]

    @range_10_equipment_list_name.setter
    def range_10_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `Range 10 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 10 Equipment List Name`
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
                                 'for field `range_10_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_10_equipment_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `range_10_equipment_list_name`')
        self._data["Range 10 Equipment List Name"] = value

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

class PlantEquipmentOperationOutdoorWetBulb(object):
    """ Corresponds to IDD object `PlantEquipmentOperation:OutdoorWetBulb`
        Plant equipment operation scheme for outdoor wet-bulb temperature range operation.
        Specifies one or more groups of equipment which are available to operate for
        successive outdoor wet-bulb temperature ranges.
    
    """
    internal_name = "PlantEquipmentOperation:OutdoorWetBulb"
    field_count = 31
    required_fields = ["Name", "Wet-Bulb Temperature Range 1 Lower Limit", "Wet-Bulb Temperature Range 1 Upper Limit", "Range 1 Equipment List Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `PlantEquipmentOperation:OutdoorWetBulb`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Wet-Bulb Temperature Range 1 Lower Limit"] = None
        self._data["Wet-Bulb Temperature Range 1 Upper Limit"] = None
        self._data["Range 1 Equipment List Name"] = None
        self._data["Wet-Bulb Temperature Range 2 Lower Limit"] = None
        self._data["Wet-Bulb Temperature Range 2 Upper Limit"] = None
        self._data["Range 2 Equipment List Name"] = None
        self._data["Wet-Bulb Temperature Range 3 Lower Limit"] = None
        self._data["Wet-Bulb Temperature Range 3 Upper Limit"] = None
        self._data["Range 3 Equipment List Name"] = None
        self._data["Wet-Bulb Temperature Range 4 Lower Limit"] = None
        self._data["Wet-Bulb Temperature Range 4 Upper Limit"] = None
        self._data["Range 4 Equipment List Name"] = None
        self._data["Wet-Bulb Temperature Range 5 Lower Limit"] = None
        self._data["Wet-Bulb Temperature Range 5 Upper Limit"] = None
        self._data["Range 5 Equipment List Name"] = None
        self._data["Wet-Bulb Temperature Range 6 Lower Limit"] = None
        self._data["Wet-Bulb Temperature Range 6 Upper Limit"] = None
        self._data["Range 6 Equipment List Name"] = None
        self._data["Wet-Bulb Temperature Range 7 Lower Limit"] = None
        self._data["Wet-Bulb Temperature Range 7 Upper Limit"] = None
        self._data["Range 7 Equipment List Name"] = None
        self._data["Wet-Bulb Temperature Range 8 Lower Limit"] = None
        self._data["Wet-Bulb Temperature Range 8 Upper Limit"] = None
        self._data["Range 8 Equipment List Name"] = None
        self._data["Wet-Bulb Temperature Range 9 Lower Limit"] = None
        self._data["Wet-Bulb Temperature Range 9 Upper Limit"] = None
        self._data["Range 9 Equipment List Name"] = None
        self._data["Wet-Bulb Temperature Range 10 Lower Limit"] = None
        self._data["Wet-Bulb Temperature Range 10 Upper Limit"] = None
        self._data["Range 10 Equipment List Name"] = None
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
            self.wetbulb_temperature_range_1_lower_limit = None
        else:
            self.wetbulb_temperature_range_1_lower_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wetbulb_temperature_range_1_upper_limit = None
        else:
            self.wetbulb_temperature_range_1_upper_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.range_1_equipment_list_name = None
        else:
            self.range_1_equipment_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wetbulb_temperature_range_2_lower_limit = None
        else:
            self.wetbulb_temperature_range_2_lower_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wetbulb_temperature_range_2_upper_limit = None
        else:
            self.wetbulb_temperature_range_2_upper_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.range_2_equipment_list_name = None
        else:
            self.range_2_equipment_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wetbulb_temperature_range_3_lower_limit = None
        else:
            self.wetbulb_temperature_range_3_lower_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wetbulb_temperature_range_3_upper_limit = None
        else:
            self.wetbulb_temperature_range_3_upper_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.range_3_equipment_list_name = None
        else:
            self.range_3_equipment_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wetbulb_temperature_range_4_lower_limit = None
        else:
            self.wetbulb_temperature_range_4_lower_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wetbulb_temperature_range_4_upper_limit = None
        else:
            self.wetbulb_temperature_range_4_upper_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.range_4_equipment_list_name = None
        else:
            self.range_4_equipment_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wetbulb_temperature_range_5_lower_limit = None
        else:
            self.wetbulb_temperature_range_5_lower_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wetbulb_temperature_range_5_upper_limit = None
        else:
            self.wetbulb_temperature_range_5_upper_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.range_5_equipment_list_name = None
        else:
            self.range_5_equipment_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wetbulb_temperature_range_6_lower_limit = None
        else:
            self.wetbulb_temperature_range_6_lower_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wetbulb_temperature_range_6_upper_limit = None
        else:
            self.wetbulb_temperature_range_6_upper_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.range_6_equipment_list_name = None
        else:
            self.range_6_equipment_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wetbulb_temperature_range_7_lower_limit = None
        else:
            self.wetbulb_temperature_range_7_lower_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wetbulb_temperature_range_7_upper_limit = None
        else:
            self.wetbulb_temperature_range_7_upper_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.range_7_equipment_list_name = None
        else:
            self.range_7_equipment_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wetbulb_temperature_range_8_lower_limit = None
        else:
            self.wetbulb_temperature_range_8_lower_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wetbulb_temperature_range_8_upper_limit = None
        else:
            self.wetbulb_temperature_range_8_upper_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.range_8_equipment_list_name = None
        else:
            self.range_8_equipment_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wetbulb_temperature_range_9_lower_limit = None
        else:
            self.wetbulb_temperature_range_9_lower_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wetbulb_temperature_range_9_upper_limit = None
        else:
            self.wetbulb_temperature_range_9_upper_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.range_9_equipment_list_name = None
        else:
            self.range_9_equipment_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wetbulb_temperature_range_10_lower_limit = None
        else:
            self.wetbulb_temperature_range_10_lower_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wetbulb_temperature_range_10_upper_limit = None
        else:
            self.wetbulb_temperature_range_10_upper_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.range_10_equipment_list_name = None
        else:
            self.range_10_equipment_list_name = vals[i]
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
    def wetbulb_temperature_range_1_lower_limit(self):
        """Get wetbulb_temperature_range_1_lower_limit

        Returns:
            float: the value of `wetbulb_temperature_range_1_lower_limit` or None if not set
        """
        return self._data["Wet-Bulb Temperature Range 1 Lower Limit"]

    @wetbulb_temperature_range_1_lower_limit.setter
    def wetbulb_temperature_range_1_lower_limit(self, value=None):
        """  Corresponds to IDD Field `Wet-Bulb Temperature Range 1 Lower Limit`

        Args:
            value (float): value for IDD Field `Wet-Bulb Temperature Range 1 Lower Limit`
                Units: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `wetbulb_temperature_range_1_lower_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `wetbulb_temperature_range_1_lower_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `wetbulb_temperature_range_1_lower_limit`')
        self._data["Wet-Bulb Temperature Range 1 Lower Limit"] = value

    @property
    def wetbulb_temperature_range_1_upper_limit(self):
        """Get wetbulb_temperature_range_1_upper_limit

        Returns:
            float: the value of `wetbulb_temperature_range_1_upper_limit` or None if not set
        """
        return self._data["Wet-Bulb Temperature Range 1 Upper Limit"]

    @wetbulb_temperature_range_1_upper_limit.setter
    def wetbulb_temperature_range_1_upper_limit(self, value=None):
        """  Corresponds to IDD Field `Wet-Bulb Temperature Range 1 Upper Limit`

        Args:
            value (float): value for IDD Field `Wet-Bulb Temperature Range 1 Upper Limit`
                Units: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `wetbulb_temperature_range_1_upper_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `wetbulb_temperature_range_1_upper_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `wetbulb_temperature_range_1_upper_limit`')
        self._data["Wet-Bulb Temperature Range 1 Upper Limit"] = value

    @property
    def range_1_equipment_list_name(self):
        """Get range_1_equipment_list_name

        Returns:
            str: the value of `range_1_equipment_list_name` or None if not set
        """
        return self._data["Range 1 Equipment List Name"]

    @range_1_equipment_list_name.setter
    def range_1_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `Range 1 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 1 Equipment List Name`
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
                                 'for field `range_1_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_1_equipment_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `range_1_equipment_list_name`')
        self._data["Range 1 Equipment List Name"] = value

    @property
    def wetbulb_temperature_range_2_lower_limit(self):
        """Get wetbulb_temperature_range_2_lower_limit

        Returns:
            float: the value of `wetbulb_temperature_range_2_lower_limit` or None if not set
        """
        return self._data["Wet-Bulb Temperature Range 2 Lower Limit"]

    @wetbulb_temperature_range_2_lower_limit.setter
    def wetbulb_temperature_range_2_lower_limit(self, value=None):
        """  Corresponds to IDD Field `Wet-Bulb Temperature Range 2 Lower Limit`

        Args:
            value (float): value for IDD Field `Wet-Bulb Temperature Range 2 Lower Limit`
                Units: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `wetbulb_temperature_range_2_lower_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `wetbulb_temperature_range_2_lower_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `wetbulb_temperature_range_2_lower_limit`')
        self._data["Wet-Bulb Temperature Range 2 Lower Limit"] = value

    @property
    def wetbulb_temperature_range_2_upper_limit(self):
        """Get wetbulb_temperature_range_2_upper_limit

        Returns:
            float: the value of `wetbulb_temperature_range_2_upper_limit` or None if not set
        """
        return self._data["Wet-Bulb Temperature Range 2 Upper Limit"]

    @wetbulb_temperature_range_2_upper_limit.setter
    def wetbulb_temperature_range_2_upper_limit(self, value=None):
        """  Corresponds to IDD Field `Wet-Bulb Temperature Range 2 Upper Limit`

        Args:
            value (float): value for IDD Field `Wet-Bulb Temperature Range 2 Upper Limit`
                Units: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `wetbulb_temperature_range_2_upper_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `wetbulb_temperature_range_2_upper_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `wetbulb_temperature_range_2_upper_limit`')
        self._data["Wet-Bulb Temperature Range 2 Upper Limit"] = value

    @property
    def range_2_equipment_list_name(self):
        """Get range_2_equipment_list_name

        Returns:
            str: the value of `range_2_equipment_list_name` or None if not set
        """
        return self._data["Range 2 Equipment List Name"]

    @range_2_equipment_list_name.setter
    def range_2_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `Range 2 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 2 Equipment List Name`
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
                                 'for field `range_2_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_2_equipment_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `range_2_equipment_list_name`')
        self._data["Range 2 Equipment List Name"] = value

    @property
    def wetbulb_temperature_range_3_lower_limit(self):
        """Get wetbulb_temperature_range_3_lower_limit

        Returns:
            float: the value of `wetbulb_temperature_range_3_lower_limit` or None if not set
        """
        return self._data["Wet-Bulb Temperature Range 3 Lower Limit"]

    @wetbulb_temperature_range_3_lower_limit.setter
    def wetbulb_temperature_range_3_lower_limit(self, value=None):
        """  Corresponds to IDD Field `Wet-Bulb Temperature Range 3 Lower Limit`

        Args:
            value (float): value for IDD Field `Wet-Bulb Temperature Range 3 Lower Limit`
                Units: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `wetbulb_temperature_range_3_lower_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `wetbulb_temperature_range_3_lower_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `wetbulb_temperature_range_3_lower_limit`')
        self._data["Wet-Bulb Temperature Range 3 Lower Limit"] = value

    @property
    def wetbulb_temperature_range_3_upper_limit(self):
        """Get wetbulb_temperature_range_3_upper_limit

        Returns:
            float: the value of `wetbulb_temperature_range_3_upper_limit` or None if not set
        """
        return self._data["Wet-Bulb Temperature Range 3 Upper Limit"]

    @wetbulb_temperature_range_3_upper_limit.setter
    def wetbulb_temperature_range_3_upper_limit(self, value=None):
        """  Corresponds to IDD Field `Wet-Bulb Temperature Range 3 Upper Limit`

        Args:
            value (float): value for IDD Field `Wet-Bulb Temperature Range 3 Upper Limit`
                Units: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `wetbulb_temperature_range_3_upper_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `wetbulb_temperature_range_3_upper_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `wetbulb_temperature_range_3_upper_limit`')
        self._data["Wet-Bulb Temperature Range 3 Upper Limit"] = value

    @property
    def range_3_equipment_list_name(self):
        """Get range_3_equipment_list_name

        Returns:
            str: the value of `range_3_equipment_list_name` or None if not set
        """
        return self._data["Range 3 Equipment List Name"]

    @range_3_equipment_list_name.setter
    def range_3_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `Range 3 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 3 Equipment List Name`
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
                                 'for field `range_3_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_3_equipment_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `range_3_equipment_list_name`')
        self._data["Range 3 Equipment List Name"] = value

    @property
    def wetbulb_temperature_range_4_lower_limit(self):
        """Get wetbulb_temperature_range_4_lower_limit

        Returns:
            float: the value of `wetbulb_temperature_range_4_lower_limit` or None if not set
        """
        return self._data["Wet-Bulb Temperature Range 4 Lower Limit"]

    @wetbulb_temperature_range_4_lower_limit.setter
    def wetbulb_temperature_range_4_lower_limit(self, value=None):
        """  Corresponds to IDD Field `Wet-Bulb Temperature Range 4 Lower Limit`

        Args:
            value (float): value for IDD Field `Wet-Bulb Temperature Range 4 Lower Limit`
                Units: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `wetbulb_temperature_range_4_lower_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `wetbulb_temperature_range_4_lower_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `wetbulb_temperature_range_4_lower_limit`')
        self._data["Wet-Bulb Temperature Range 4 Lower Limit"] = value

    @property
    def wetbulb_temperature_range_4_upper_limit(self):
        """Get wetbulb_temperature_range_4_upper_limit

        Returns:
            float: the value of `wetbulb_temperature_range_4_upper_limit` or None if not set
        """
        return self._data["Wet-Bulb Temperature Range 4 Upper Limit"]

    @wetbulb_temperature_range_4_upper_limit.setter
    def wetbulb_temperature_range_4_upper_limit(self, value=None):
        """  Corresponds to IDD Field `Wet-Bulb Temperature Range 4 Upper Limit`

        Args:
            value (float): value for IDD Field `Wet-Bulb Temperature Range 4 Upper Limit`
                Units: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `wetbulb_temperature_range_4_upper_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `wetbulb_temperature_range_4_upper_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `wetbulb_temperature_range_4_upper_limit`')
        self._data["Wet-Bulb Temperature Range 4 Upper Limit"] = value

    @property
    def range_4_equipment_list_name(self):
        """Get range_4_equipment_list_name

        Returns:
            str: the value of `range_4_equipment_list_name` or None if not set
        """
        return self._data["Range 4 Equipment List Name"]

    @range_4_equipment_list_name.setter
    def range_4_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `Range 4 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 4 Equipment List Name`
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
                                 'for field `range_4_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_4_equipment_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `range_4_equipment_list_name`')
        self._data["Range 4 Equipment List Name"] = value

    @property
    def wetbulb_temperature_range_5_lower_limit(self):
        """Get wetbulb_temperature_range_5_lower_limit

        Returns:
            float: the value of `wetbulb_temperature_range_5_lower_limit` or None if not set
        """
        return self._data["Wet-Bulb Temperature Range 5 Lower Limit"]

    @wetbulb_temperature_range_5_lower_limit.setter
    def wetbulb_temperature_range_5_lower_limit(self, value=None):
        """  Corresponds to IDD Field `Wet-Bulb Temperature Range 5 Lower Limit`

        Args:
            value (float): value for IDD Field `Wet-Bulb Temperature Range 5 Lower Limit`
                Units: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `wetbulb_temperature_range_5_lower_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `wetbulb_temperature_range_5_lower_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `wetbulb_temperature_range_5_lower_limit`')
        self._data["Wet-Bulb Temperature Range 5 Lower Limit"] = value

    @property
    def wetbulb_temperature_range_5_upper_limit(self):
        """Get wetbulb_temperature_range_5_upper_limit

        Returns:
            float: the value of `wetbulb_temperature_range_5_upper_limit` or None if not set
        """
        return self._data["Wet-Bulb Temperature Range 5 Upper Limit"]

    @wetbulb_temperature_range_5_upper_limit.setter
    def wetbulb_temperature_range_5_upper_limit(self, value=None):
        """  Corresponds to IDD Field `Wet-Bulb Temperature Range 5 Upper Limit`

        Args:
            value (float): value for IDD Field `Wet-Bulb Temperature Range 5 Upper Limit`
                Units: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `wetbulb_temperature_range_5_upper_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `wetbulb_temperature_range_5_upper_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `wetbulb_temperature_range_5_upper_limit`')
        self._data["Wet-Bulb Temperature Range 5 Upper Limit"] = value

    @property
    def range_5_equipment_list_name(self):
        """Get range_5_equipment_list_name

        Returns:
            str: the value of `range_5_equipment_list_name` or None if not set
        """
        return self._data["Range 5 Equipment List Name"]

    @range_5_equipment_list_name.setter
    def range_5_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `Range 5 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 5 Equipment List Name`
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
                                 'for field `range_5_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_5_equipment_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `range_5_equipment_list_name`')
        self._data["Range 5 Equipment List Name"] = value

    @property
    def wetbulb_temperature_range_6_lower_limit(self):
        """Get wetbulb_temperature_range_6_lower_limit

        Returns:
            float: the value of `wetbulb_temperature_range_6_lower_limit` or None if not set
        """
        return self._data["Wet-Bulb Temperature Range 6 Lower Limit"]

    @wetbulb_temperature_range_6_lower_limit.setter
    def wetbulb_temperature_range_6_lower_limit(self, value=None):
        """  Corresponds to IDD Field `Wet-Bulb Temperature Range 6 Lower Limit`

        Args:
            value (float): value for IDD Field `Wet-Bulb Temperature Range 6 Lower Limit`
                Units: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `wetbulb_temperature_range_6_lower_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `wetbulb_temperature_range_6_lower_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `wetbulb_temperature_range_6_lower_limit`')
        self._data["Wet-Bulb Temperature Range 6 Lower Limit"] = value

    @property
    def wetbulb_temperature_range_6_upper_limit(self):
        """Get wetbulb_temperature_range_6_upper_limit

        Returns:
            float: the value of `wetbulb_temperature_range_6_upper_limit` or None if not set
        """
        return self._data["Wet-Bulb Temperature Range 6 Upper Limit"]

    @wetbulb_temperature_range_6_upper_limit.setter
    def wetbulb_temperature_range_6_upper_limit(self, value=None):
        """  Corresponds to IDD Field `Wet-Bulb Temperature Range 6 Upper Limit`

        Args:
            value (float): value for IDD Field `Wet-Bulb Temperature Range 6 Upper Limit`
                Units: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `wetbulb_temperature_range_6_upper_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `wetbulb_temperature_range_6_upper_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `wetbulb_temperature_range_6_upper_limit`')
        self._data["Wet-Bulb Temperature Range 6 Upper Limit"] = value

    @property
    def range_6_equipment_list_name(self):
        """Get range_6_equipment_list_name

        Returns:
            str: the value of `range_6_equipment_list_name` or None if not set
        """
        return self._data["Range 6 Equipment List Name"]

    @range_6_equipment_list_name.setter
    def range_6_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `Range 6 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 6 Equipment List Name`
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
                                 'for field `range_6_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_6_equipment_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `range_6_equipment_list_name`')
        self._data["Range 6 Equipment List Name"] = value

    @property
    def wetbulb_temperature_range_7_lower_limit(self):
        """Get wetbulb_temperature_range_7_lower_limit

        Returns:
            float: the value of `wetbulb_temperature_range_7_lower_limit` or None if not set
        """
        return self._data["Wet-Bulb Temperature Range 7 Lower Limit"]

    @wetbulb_temperature_range_7_lower_limit.setter
    def wetbulb_temperature_range_7_lower_limit(self, value=None):
        """  Corresponds to IDD Field `Wet-Bulb Temperature Range 7 Lower Limit`

        Args:
            value (float): value for IDD Field `Wet-Bulb Temperature Range 7 Lower Limit`
                Units: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `wetbulb_temperature_range_7_lower_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `wetbulb_temperature_range_7_lower_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `wetbulb_temperature_range_7_lower_limit`')
        self._data["Wet-Bulb Temperature Range 7 Lower Limit"] = value

    @property
    def wetbulb_temperature_range_7_upper_limit(self):
        """Get wetbulb_temperature_range_7_upper_limit

        Returns:
            float: the value of `wetbulb_temperature_range_7_upper_limit` or None if not set
        """
        return self._data["Wet-Bulb Temperature Range 7 Upper Limit"]

    @wetbulb_temperature_range_7_upper_limit.setter
    def wetbulb_temperature_range_7_upper_limit(self, value=None):
        """  Corresponds to IDD Field `Wet-Bulb Temperature Range 7 Upper Limit`

        Args:
            value (float): value for IDD Field `Wet-Bulb Temperature Range 7 Upper Limit`
                Units: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `wetbulb_temperature_range_7_upper_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `wetbulb_temperature_range_7_upper_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `wetbulb_temperature_range_7_upper_limit`')
        self._data["Wet-Bulb Temperature Range 7 Upper Limit"] = value

    @property
    def range_7_equipment_list_name(self):
        """Get range_7_equipment_list_name

        Returns:
            str: the value of `range_7_equipment_list_name` or None if not set
        """
        return self._data["Range 7 Equipment List Name"]

    @range_7_equipment_list_name.setter
    def range_7_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `Range 7 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 7 Equipment List Name`
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
                                 'for field `range_7_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_7_equipment_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `range_7_equipment_list_name`')
        self._data["Range 7 Equipment List Name"] = value

    @property
    def wetbulb_temperature_range_8_lower_limit(self):
        """Get wetbulb_temperature_range_8_lower_limit

        Returns:
            float: the value of `wetbulb_temperature_range_8_lower_limit` or None if not set
        """
        return self._data["Wet-Bulb Temperature Range 8 Lower Limit"]

    @wetbulb_temperature_range_8_lower_limit.setter
    def wetbulb_temperature_range_8_lower_limit(self, value=None):
        """  Corresponds to IDD Field `Wet-Bulb Temperature Range 8 Lower Limit`

        Args:
            value (float): value for IDD Field `Wet-Bulb Temperature Range 8 Lower Limit`
                Units: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `wetbulb_temperature_range_8_lower_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `wetbulb_temperature_range_8_lower_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `wetbulb_temperature_range_8_lower_limit`')
        self._data["Wet-Bulb Temperature Range 8 Lower Limit"] = value

    @property
    def wetbulb_temperature_range_8_upper_limit(self):
        """Get wetbulb_temperature_range_8_upper_limit

        Returns:
            float: the value of `wetbulb_temperature_range_8_upper_limit` or None if not set
        """
        return self._data["Wet-Bulb Temperature Range 8 Upper Limit"]

    @wetbulb_temperature_range_8_upper_limit.setter
    def wetbulb_temperature_range_8_upper_limit(self, value=None):
        """  Corresponds to IDD Field `Wet-Bulb Temperature Range 8 Upper Limit`

        Args:
            value (float): value for IDD Field `Wet-Bulb Temperature Range 8 Upper Limit`
                Units: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `wetbulb_temperature_range_8_upper_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `wetbulb_temperature_range_8_upper_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `wetbulb_temperature_range_8_upper_limit`')
        self._data["Wet-Bulb Temperature Range 8 Upper Limit"] = value

    @property
    def range_8_equipment_list_name(self):
        """Get range_8_equipment_list_name

        Returns:
            str: the value of `range_8_equipment_list_name` or None if not set
        """
        return self._data["Range 8 Equipment List Name"]

    @range_8_equipment_list_name.setter
    def range_8_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `Range 8 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 8 Equipment List Name`
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
                                 'for field `range_8_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_8_equipment_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `range_8_equipment_list_name`')
        self._data["Range 8 Equipment List Name"] = value

    @property
    def wetbulb_temperature_range_9_lower_limit(self):
        """Get wetbulb_temperature_range_9_lower_limit

        Returns:
            float: the value of `wetbulb_temperature_range_9_lower_limit` or None if not set
        """
        return self._data["Wet-Bulb Temperature Range 9 Lower Limit"]

    @wetbulb_temperature_range_9_lower_limit.setter
    def wetbulb_temperature_range_9_lower_limit(self, value=None):
        """  Corresponds to IDD Field `Wet-Bulb Temperature Range 9 Lower Limit`

        Args:
            value (float): value for IDD Field `Wet-Bulb Temperature Range 9 Lower Limit`
                Units: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `wetbulb_temperature_range_9_lower_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `wetbulb_temperature_range_9_lower_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `wetbulb_temperature_range_9_lower_limit`')
        self._data["Wet-Bulb Temperature Range 9 Lower Limit"] = value

    @property
    def wetbulb_temperature_range_9_upper_limit(self):
        """Get wetbulb_temperature_range_9_upper_limit

        Returns:
            float: the value of `wetbulb_temperature_range_9_upper_limit` or None if not set
        """
        return self._data["Wet-Bulb Temperature Range 9 Upper Limit"]

    @wetbulb_temperature_range_9_upper_limit.setter
    def wetbulb_temperature_range_9_upper_limit(self, value=None):
        """  Corresponds to IDD Field `Wet-Bulb Temperature Range 9 Upper Limit`

        Args:
            value (float): value for IDD Field `Wet-Bulb Temperature Range 9 Upper Limit`
                Units: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `wetbulb_temperature_range_9_upper_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `wetbulb_temperature_range_9_upper_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `wetbulb_temperature_range_9_upper_limit`')
        self._data["Wet-Bulb Temperature Range 9 Upper Limit"] = value

    @property
    def range_9_equipment_list_name(self):
        """Get range_9_equipment_list_name

        Returns:
            str: the value of `range_9_equipment_list_name` or None if not set
        """
        return self._data["Range 9 Equipment List Name"]

    @range_9_equipment_list_name.setter
    def range_9_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `Range 9 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 9 Equipment List Name`
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
                                 'for field `range_9_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_9_equipment_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `range_9_equipment_list_name`')
        self._data["Range 9 Equipment List Name"] = value

    @property
    def wetbulb_temperature_range_10_lower_limit(self):
        """Get wetbulb_temperature_range_10_lower_limit

        Returns:
            float: the value of `wetbulb_temperature_range_10_lower_limit` or None if not set
        """
        return self._data["Wet-Bulb Temperature Range 10 Lower Limit"]

    @wetbulb_temperature_range_10_lower_limit.setter
    def wetbulb_temperature_range_10_lower_limit(self, value=None):
        """  Corresponds to IDD Field `Wet-Bulb Temperature Range 10 Lower Limit`

        Args:
            value (float): value for IDD Field `Wet-Bulb Temperature Range 10 Lower Limit`
                Units: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `wetbulb_temperature_range_10_lower_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `wetbulb_temperature_range_10_lower_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `wetbulb_temperature_range_10_lower_limit`')
        self._data["Wet-Bulb Temperature Range 10 Lower Limit"] = value

    @property
    def wetbulb_temperature_range_10_upper_limit(self):
        """Get wetbulb_temperature_range_10_upper_limit

        Returns:
            float: the value of `wetbulb_temperature_range_10_upper_limit` or None if not set
        """
        return self._data["Wet-Bulb Temperature Range 10 Upper Limit"]

    @wetbulb_temperature_range_10_upper_limit.setter
    def wetbulb_temperature_range_10_upper_limit(self, value=None):
        """  Corresponds to IDD Field `Wet-Bulb Temperature Range 10 Upper Limit`

        Args:
            value (float): value for IDD Field `Wet-Bulb Temperature Range 10 Upper Limit`
                Units: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `wetbulb_temperature_range_10_upper_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `wetbulb_temperature_range_10_upper_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `wetbulb_temperature_range_10_upper_limit`')
        self._data["Wet-Bulb Temperature Range 10 Upper Limit"] = value

    @property
    def range_10_equipment_list_name(self):
        """Get range_10_equipment_list_name

        Returns:
            str: the value of `range_10_equipment_list_name` or None if not set
        """
        return self._data["Range 10 Equipment List Name"]

    @range_10_equipment_list_name.setter
    def range_10_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `Range 10 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 10 Equipment List Name`
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
                                 'for field `range_10_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_10_equipment_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `range_10_equipment_list_name`')
        self._data["Range 10 Equipment List Name"] = value

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

class PlantEquipmentOperationOutdoorRelativeHumidity(object):
    """ Corresponds to IDD object `PlantEquipmentOperation:OutdoorRelativeHumidity`
        Plant equipment operation scheme for outdoor relative humidity range operation.
        Specifies one or more groups of equipment which are available to operate for
        successive outdoor relative humidity ranges.
    
    """
    internal_name = "PlantEquipmentOperation:OutdoorRelativeHumidity"
    field_count = 31
    required_fields = ["Name", "Relative Humidity Range 1 Lower Limit", "Relative Humidity Range 1 Upper Limit", "Range 1 Equipment List Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `PlantEquipmentOperation:OutdoorRelativeHumidity`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Relative Humidity Range 1 Lower Limit"] = None
        self._data["Relative Humidity Range 1 Upper Limit"] = None
        self._data["Range 1 Equipment List Name"] = None
        self._data["Relative Humidity Range 2 Lower Limit"] = None
        self._data["Relative Humidity Range 2 Upper Limit"] = None
        self._data["Range 2 Equipment List Name"] = None
        self._data["Relative Humidity Range 3 Lower Limit"] = None
        self._data["Relative Humidity Range 3 Upper Limit"] = None
        self._data["Range 3 Equipment List Name"] = None
        self._data["Relative Humidity Range 4 Lower Limit"] = None
        self._data["Relative Humidity Range 4 Upper Limit"] = None
        self._data["Range 4 Equipment List Name"] = None
        self._data["Relative Humidity Range 5 Lower Limit"] = None
        self._data["Relative Humidity Range 5 Upper Limit"] = None
        self._data["Range 5 Equipment List Name"] = None
        self._data["Relative Humidity Range 6 Lower Limit"] = None
        self._data["Relative Humidity Range 6 Upper Limit"] = None
        self._data["Range 6 Equipment List Name"] = None
        self._data["Relative Humidity Range 7 Lower Limit"] = None
        self._data["Relative Humidity Range 7 Upper Limit"] = None
        self._data["Range 7 Equipment List Name"] = None
        self._data["Relative Humidity Range 8 Lower Limit"] = None
        self._data["Relative Humidity Range 8 Upper Limit"] = None
        self._data["Range 8 Equipment List Name"] = None
        self._data["Relative Humidity Range 9 Lower Limit"] = None
        self._data["Relative Humidity Range 9 Upper Limit"] = None
        self._data["Range 9 Equipment List Name"] = None
        self._data["Relative Humidity Range 10 Lower Limit"] = None
        self._data["Relative Humidity Range 10 Upper Limit"] = None
        self._data["Range 10 Equipment List Name"] = None
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
            self.relative_humidity_range_1_lower_limit = None
        else:
            self.relative_humidity_range_1_lower_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.relative_humidity_range_1_upper_limit = None
        else:
            self.relative_humidity_range_1_upper_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.range_1_equipment_list_name = None
        else:
            self.range_1_equipment_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.relative_humidity_range_2_lower_limit = None
        else:
            self.relative_humidity_range_2_lower_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.relative_humidity_range_2_upper_limit = None
        else:
            self.relative_humidity_range_2_upper_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.range_2_equipment_list_name = None
        else:
            self.range_2_equipment_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.relative_humidity_range_3_lower_limit = None
        else:
            self.relative_humidity_range_3_lower_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.relative_humidity_range_3_upper_limit = None
        else:
            self.relative_humidity_range_3_upper_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.range_3_equipment_list_name = None
        else:
            self.range_3_equipment_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.relative_humidity_range_4_lower_limit = None
        else:
            self.relative_humidity_range_4_lower_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.relative_humidity_range_4_upper_limit = None
        else:
            self.relative_humidity_range_4_upper_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.range_4_equipment_list_name = None
        else:
            self.range_4_equipment_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.relative_humidity_range_5_lower_limit = None
        else:
            self.relative_humidity_range_5_lower_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.relative_humidity_range_5_upper_limit = None
        else:
            self.relative_humidity_range_5_upper_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.range_5_equipment_list_name = None
        else:
            self.range_5_equipment_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.relative_humidity_range_6_lower_limit = None
        else:
            self.relative_humidity_range_6_lower_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.relative_humidity_range_6_upper_limit = None
        else:
            self.relative_humidity_range_6_upper_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.range_6_equipment_list_name = None
        else:
            self.range_6_equipment_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.relative_humidity_range_7_lower_limit = None
        else:
            self.relative_humidity_range_7_lower_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.relative_humidity_range_7_upper_limit = None
        else:
            self.relative_humidity_range_7_upper_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.range_7_equipment_list_name = None
        else:
            self.range_7_equipment_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.relative_humidity_range_8_lower_limit = None
        else:
            self.relative_humidity_range_8_lower_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.relative_humidity_range_8_upper_limit = None
        else:
            self.relative_humidity_range_8_upper_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.range_8_equipment_list_name = None
        else:
            self.range_8_equipment_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.relative_humidity_range_9_lower_limit = None
        else:
            self.relative_humidity_range_9_lower_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.relative_humidity_range_9_upper_limit = None
        else:
            self.relative_humidity_range_9_upper_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.range_9_equipment_list_name = None
        else:
            self.range_9_equipment_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.relative_humidity_range_10_lower_limit = None
        else:
            self.relative_humidity_range_10_lower_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.relative_humidity_range_10_upper_limit = None
        else:
            self.relative_humidity_range_10_upper_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.range_10_equipment_list_name = None
        else:
            self.range_10_equipment_list_name = vals[i]
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
    def relative_humidity_range_1_lower_limit(self):
        """Get relative_humidity_range_1_lower_limit

        Returns:
            float: the value of `relative_humidity_range_1_lower_limit` or None if not set
        """
        return self._data["Relative Humidity Range 1 Lower Limit"]

    @relative_humidity_range_1_lower_limit.setter
    def relative_humidity_range_1_lower_limit(self, value=None):
        """  Corresponds to IDD Field `Relative Humidity Range 1 Lower Limit`

        Args:
            value (float): value for IDD Field `Relative Humidity Range 1 Lower Limit`
                Units: percent
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
                                 'for field `relative_humidity_range_1_lower_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_humidity_range_1_lower_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `relative_humidity_range_1_lower_limit`')
        self._data["Relative Humidity Range 1 Lower Limit"] = value

    @property
    def relative_humidity_range_1_upper_limit(self):
        """Get relative_humidity_range_1_upper_limit

        Returns:
            float: the value of `relative_humidity_range_1_upper_limit` or None if not set
        """
        return self._data["Relative Humidity Range 1 Upper Limit"]

    @relative_humidity_range_1_upper_limit.setter
    def relative_humidity_range_1_upper_limit(self, value=None):
        """  Corresponds to IDD Field `Relative Humidity Range 1 Upper Limit`

        Args:
            value (float): value for IDD Field `Relative Humidity Range 1 Upper Limit`
                Units: percent
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
                                 'for field `relative_humidity_range_1_upper_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_humidity_range_1_upper_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `relative_humidity_range_1_upper_limit`')
        self._data["Relative Humidity Range 1 Upper Limit"] = value

    @property
    def range_1_equipment_list_name(self):
        """Get range_1_equipment_list_name

        Returns:
            str: the value of `range_1_equipment_list_name` or None if not set
        """
        return self._data["Range 1 Equipment List Name"]

    @range_1_equipment_list_name.setter
    def range_1_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `Range 1 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 1 Equipment List Name`
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
                                 'for field `range_1_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_1_equipment_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `range_1_equipment_list_name`')
        self._data["Range 1 Equipment List Name"] = value

    @property
    def relative_humidity_range_2_lower_limit(self):
        """Get relative_humidity_range_2_lower_limit

        Returns:
            float: the value of `relative_humidity_range_2_lower_limit` or None if not set
        """
        return self._data["Relative Humidity Range 2 Lower Limit"]

    @relative_humidity_range_2_lower_limit.setter
    def relative_humidity_range_2_lower_limit(self, value=None):
        """  Corresponds to IDD Field `Relative Humidity Range 2 Lower Limit`

        Args:
            value (float): value for IDD Field `Relative Humidity Range 2 Lower Limit`
                Units: percent
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
                                 'for field `relative_humidity_range_2_lower_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_humidity_range_2_lower_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `relative_humidity_range_2_lower_limit`')
        self._data["Relative Humidity Range 2 Lower Limit"] = value

    @property
    def relative_humidity_range_2_upper_limit(self):
        """Get relative_humidity_range_2_upper_limit

        Returns:
            float: the value of `relative_humidity_range_2_upper_limit` or None if not set
        """
        return self._data["Relative Humidity Range 2 Upper Limit"]

    @relative_humidity_range_2_upper_limit.setter
    def relative_humidity_range_2_upper_limit(self, value=None):
        """  Corresponds to IDD Field `Relative Humidity Range 2 Upper Limit`

        Args:
            value (float): value for IDD Field `Relative Humidity Range 2 Upper Limit`
                Units: percent
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
                                 'for field `relative_humidity_range_2_upper_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_humidity_range_2_upper_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `relative_humidity_range_2_upper_limit`')
        self._data["Relative Humidity Range 2 Upper Limit"] = value

    @property
    def range_2_equipment_list_name(self):
        """Get range_2_equipment_list_name

        Returns:
            str: the value of `range_2_equipment_list_name` or None if not set
        """
        return self._data["Range 2 Equipment List Name"]

    @range_2_equipment_list_name.setter
    def range_2_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `Range 2 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 2 Equipment List Name`
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
                                 'for field `range_2_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_2_equipment_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `range_2_equipment_list_name`')
        self._data["Range 2 Equipment List Name"] = value

    @property
    def relative_humidity_range_3_lower_limit(self):
        """Get relative_humidity_range_3_lower_limit

        Returns:
            float: the value of `relative_humidity_range_3_lower_limit` or None if not set
        """
        return self._data["Relative Humidity Range 3 Lower Limit"]

    @relative_humidity_range_3_lower_limit.setter
    def relative_humidity_range_3_lower_limit(self, value=None):
        """  Corresponds to IDD Field `Relative Humidity Range 3 Lower Limit`

        Args:
            value (float): value for IDD Field `Relative Humidity Range 3 Lower Limit`
                Units: percent
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
                                 'for field `relative_humidity_range_3_lower_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_humidity_range_3_lower_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `relative_humidity_range_3_lower_limit`')
        self._data["Relative Humidity Range 3 Lower Limit"] = value

    @property
    def relative_humidity_range_3_upper_limit(self):
        """Get relative_humidity_range_3_upper_limit

        Returns:
            float: the value of `relative_humidity_range_3_upper_limit` or None if not set
        """
        return self._data["Relative Humidity Range 3 Upper Limit"]

    @relative_humidity_range_3_upper_limit.setter
    def relative_humidity_range_3_upper_limit(self, value=None):
        """  Corresponds to IDD Field `Relative Humidity Range 3 Upper Limit`

        Args:
            value (float): value for IDD Field `Relative Humidity Range 3 Upper Limit`
                Units: percent
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
                                 'for field `relative_humidity_range_3_upper_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_humidity_range_3_upper_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `relative_humidity_range_3_upper_limit`')
        self._data["Relative Humidity Range 3 Upper Limit"] = value

    @property
    def range_3_equipment_list_name(self):
        """Get range_3_equipment_list_name

        Returns:
            str: the value of `range_3_equipment_list_name` or None if not set
        """
        return self._data["Range 3 Equipment List Name"]

    @range_3_equipment_list_name.setter
    def range_3_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `Range 3 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 3 Equipment List Name`
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
                                 'for field `range_3_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_3_equipment_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `range_3_equipment_list_name`')
        self._data["Range 3 Equipment List Name"] = value

    @property
    def relative_humidity_range_4_lower_limit(self):
        """Get relative_humidity_range_4_lower_limit

        Returns:
            float: the value of `relative_humidity_range_4_lower_limit` or None if not set
        """
        return self._data["Relative Humidity Range 4 Lower Limit"]

    @relative_humidity_range_4_lower_limit.setter
    def relative_humidity_range_4_lower_limit(self, value=None):
        """  Corresponds to IDD Field `Relative Humidity Range 4 Lower Limit`

        Args:
            value (float): value for IDD Field `Relative Humidity Range 4 Lower Limit`
                Units: percent
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
                                 'for field `relative_humidity_range_4_lower_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_humidity_range_4_lower_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `relative_humidity_range_4_lower_limit`')
        self._data["Relative Humidity Range 4 Lower Limit"] = value

    @property
    def relative_humidity_range_4_upper_limit(self):
        """Get relative_humidity_range_4_upper_limit

        Returns:
            float: the value of `relative_humidity_range_4_upper_limit` or None if not set
        """
        return self._data["Relative Humidity Range 4 Upper Limit"]

    @relative_humidity_range_4_upper_limit.setter
    def relative_humidity_range_4_upper_limit(self, value=None):
        """  Corresponds to IDD Field `Relative Humidity Range 4 Upper Limit`

        Args:
            value (float): value for IDD Field `Relative Humidity Range 4 Upper Limit`
                Units: percent
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
                                 'for field `relative_humidity_range_4_upper_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_humidity_range_4_upper_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `relative_humidity_range_4_upper_limit`')
        self._data["Relative Humidity Range 4 Upper Limit"] = value

    @property
    def range_4_equipment_list_name(self):
        """Get range_4_equipment_list_name

        Returns:
            str: the value of `range_4_equipment_list_name` or None if not set
        """
        return self._data["Range 4 Equipment List Name"]

    @range_4_equipment_list_name.setter
    def range_4_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `Range 4 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 4 Equipment List Name`
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
                                 'for field `range_4_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_4_equipment_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `range_4_equipment_list_name`')
        self._data["Range 4 Equipment List Name"] = value

    @property
    def relative_humidity_range_5_lower_limit(self):
        """Get relative_humidity_range_5_lower_limit

        Returns:
            float: the value of `relative_humidity_range_5_lower_limit` or None if not set
        """
        return self._data["Relative Humidity Range 5 Lower Limit"]

    @relative_humidity_range_5_lower_limit.setter
    def relative_humidity_range_5_lower_limit(self, value=None):
        """  Corresponds to IDD Field `Relative Humidity Range 5 Lower Limit`

        Args:
            value (float): value for IDD Field `Relative Humidity Range 5 Lower Limit`
                Units: percent
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
                                 'for field `relative_humidity_range_5_lower_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_humidity_range_5_lower_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `relative_humidity_range_5_lower_limit`')
        self._data["Relative Humidity Range 5 Lower Limit"] = value

    @property
    def relative_humidity_range_5_upper_limit(self):
        """Get relative_humidity_range_5_upper_limit

        Returns:
            float: the value of `relative_humidity_range_5_upper_limit` or None if not set
        """
        return self._data["Relative Humidity Range 5 Upper Limit"]

    @relative_humidity_range_5_upper_limit.setter
    def relative_humidity_range_5_upper_limit(self, value=None):
        """  Corresponds to IDD Field `Relative Humidity Range 5 Upper Limit`

        Args:
            value (float): value for IDD Field `Relative Humidity Range 5 Upper Limit`
                Units: percent
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
                                 'for field `relative_humidity_range_5_upper_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_humidity_range_5_upper_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `relative_humidity_range_5_upper_limit`')
        self._data["Relative Humidity Range 5 Upper Limit"] = value

    @property
    def range_5_equipment_list_name(self):
        """Get range_5_equipment_list_name

        Returns:
            str: the value of `range_5_equipment_list_name` or None if not set
        """
        return self._data["Range 5 Equipment List Name"]

    @range_5_equipment_list_name.setter
    def range_5_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `Range 5 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 5 Equipment List Name`
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
                                 'for field `range_5_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_5_equipment_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `range_5_equipment_list_name`')
        self._data["Range 5 Equipment List Name"] = value

    @property
    def relative_humidity_range_6_lower_limit(self):
        """Get relative_humidity_range_6_lower_limit

        Returns:
            float: the value of `relative_humidity_range_6_lower_limit` or None if not set
        """
        return self._data["Relative Humidity Range 6 Lower Limit"]

    @relative_humidity_range_6_lower_limit.setter
    def relative_humidity_range_6_lower_limit(self, value=None):
        """  Corresponds to IDD Field `Relative Humidity Range 6 Lower Limit`

        Args:
            value (float): value for IDD Field `Relative Humidity Range 6 Lower Limit`
                Units: percent
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
                                 'for field `relative_humidity_range_6_lower_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_humidity_range_6_lower_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `relative_humidity_range_6_lower_limit`')
        self._data["Relative Humidity Range 6 Lower Limit"] = value

    @property
    def relative_humidity_range_6_upper_limit(self):
        """Get relative_humidity_range_6_upper_limit

        Returns:
            float: the value of `relative_humidity_range_6_upper_limit` or None if not set
        """
        return self._data["Relative Humidity Range 6 Upper Limit"]

    @relative_humidity_range_6_upper_limit.setter
    def relative_humidity_range_6_upper_limit(self, value=None):
        """  Corresponds to IDD Field `Relative Humidity Range 6 Upper Limit`

        Args:
            value (float): value for IDD Field `Relative Humidity Range 6 Upper Limit`
                Units: percent
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
                                 'for field `relative_humidity_range_6_upper_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_humidity_range_6_upper_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `relative_humidity_range_6_upper_limit`')
        self._data["Relative Humidity Range 6 Upper Limit"] = value

    @property
    def range_6_equipment_list_name(self):
        """Get range_6_equipment_list_name

        Returns:
            str: the value of `range_6_equipment_list_name` or None if not set
        """
        return self._data["Range 6 Equipment List Name"]

    @range_6_equipment_list_name.setter
    def range_6_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `Range 6 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 6 Equipment List Name`
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
                                 'for field `range_6_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_6_equipment_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `range_6_equipment_list_name`')
        self._data["Range 6 Equipment List Name"] = value

    @property
    def relative_humidity_range_7_lower_limit(self):
        """Get relative_humidity_range_7_lower_limit

        Returns:
            float: the value of `relative_humidity_range_7_lower_limit` or None if not set
        """
        return self._data["Relative Humidity Range 7 Lower Limit"]

    @relative_humidity_range_7_lower_limit.setter
    def relative_humidity_range_7_lower_limit(self, value=None):
        """  Corresponds to IDD Field `Relative Humidity Range 7 Lower Limit`

        Args:
            value (float): value for IDD Field `Relative Humidity Range 7 Lower Limit`
                Units: percent
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
                                 'for field `relative_humidity_range_7_lower_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_humidity_range_7_lower_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `relative_humidity_range_7_lower_limit`')
        self._data["Relative Humidity Range 7 Lower Limit"] = value

    @property
    def relative_humidity_range_7_upper_limit(self):
        """Get relative_humidity_range_7_upper_limit

        Returns:
            float: the value of `relative_humidity_range_7_upper_limit` or None if not set
        """
        return self._data["Relative Humidity Range 7 Upper Limit"]

    @relative_humidity_range_7_upper_limit.setter
    def relative_humidity_range_7_upper_limit(self, value=None):
        """  Corresponds to IDD Field `Relative Humidity Range 7 Upper Limit`

        Args:
            value (float): value for IDD Field `Relative Humidity Range 7 Upper Limit`
                Units: percent
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
                                 'for field `relative_humidity_range_7_upper_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_humidity_range_7_upper_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `relative_humidity_range_7_upper_limit`')
        self._data["Relative Humidity Range 7 Upper Limit"] = value

    @property
    def range_7_equipment_list_name(self):
        """Get range_7_equipment_list_name

        Returns:
            str: the value of `range_7_equipment_list_name` or None if not set
        """
        return self._data["Range 7 Equipment List Name"]

    @range_7_equipment_list_name.setter
    def range_7_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `Range 7 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 7 Equipment List Name`
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
                                 'for field `range_7_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_7_equipment_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `range_7_equipment_list_name`')
        self._data["Range 7 Equipment List Name"] = value

    @property
    def relative_humidity_range_8_lower_limit(self):
        """Get relative_humidity_range_8_lower_limit

        Returns:
            float: the value of `relative_humidity_range_8_lower_limit` or None if not set
        """
        return self._data["Relative Humidity Range 8 Lower Limit"]

    @relative_humidity_range_8_lower_limit.setter
    def relative_humidity_range_8_lower_limit(self, value=None):
        """  Corresponds to IDD Field `Relative Humidity Range 8 Lower Limit`

        Args:
            value (float): value for IDD Field `Relative Humidity Range 8 Lower Limit`
                Units: percent
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
                                 'for field `relative_humidity_range_8_lower_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_humidity_range_8_lower_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `relative_humidity_range_8_lower_limit`')
        self._data["Relative Humidity Range 8 Lower Limit"] = value

    @property
    def relative_humidity_range_8_upper_limit(self):
        """Get relative_humidity_range_8_upper_limit

        Returns:
            float: the value of `relative_humidity_range_8_upper_limit` or None if not set
        """
        return self._data["Relative Humidity Range 8 Upper Limit"]

    @relative_humidity_range_8_upper_limit.setter
    def relative_humidity_range_8_upper_limit(self, value=None):
        """  Corresponds to IDD Field `Relative Humidity Range 8 Upper Limit`

        Args:
            value (float): value for IDD Field `Relative Humidity Range 8 Upper Limit`
                Units: percent
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
                                 'for field `relative_humidity_range_8_upper_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_humidity_range_8_upper_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `relative_humidity_range_8_upper_limit`')
        self._data["Relative Humidity Range 8 Upper Limit"] = value

    @property
    def range_8_equipment_list_name(self):
        """Get range_8_equipment_list_name

        Returns:
            str: the value of `range_8_equipment_list_name` or None if not set
        """
        return self._data["Range 8 Equipment List Name"]

    @range_8_equipment_list_name.setter
    def range_8_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `Range 8 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 8 Equipment List Name`
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
                                 'for field `range_8_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_8_equipment_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `range_8_equipment_list_name`')
        self._data["Range 8 Equipment List Name"] = value

    @property
    def relative_humidity_range_9_lower_limit(self):
        """Get relative_humidity_range_9_lower_limit

        Returns:
            float: the value of `relative_humidity_range_9_lower_limit` or None if not set
        """
        return self._data["Relative Humidity Range 9 Lower Limit"]

    @relative_humidity_range_9_lower_limit.setter
    def relative_humidity_range_9_lower_limit(self, value=None):
        """  Corresponds to IDD Field `Relative Humidity Range 9 Lower Limit`

        Args:
            value (float): value for IDD Field `Relative Humidity Range 9 Lower Limit`
                Units: percent
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
                                 'for field `relative_humidity_range_9_lower_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_humidity_range_9_lower_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `relative_humidity_range_9_lower_limit`')
        self._data["Relative Humidity Range 9 Lower Limit"] = value

    @property
    def relative_humidity_range_9_upper_limit(self):
        """Get relative_humidity_range_9_upper_limit

        Returns:
            float: the value of `relative_humidity_range_9_upper_limit` or None if not set
        """
        return self._data["Relative Humidity Range 9 Upper Limit"]

    @relative_humidity_range_9_upper_limit.setter
    def relative_humidity_range_9_upper_limit(self, value=None):
        """  Corresponds to IDD Field `Relative Humidity Range 9 Upper Limit`

        Args:
            value (float): value for IDD Field `Relative Humidity Range 9 Upper Limit`
                Units: percent
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
                                 'for field `relative_humidity_range_9_upper_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_humidity_range_9_upper_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `relative_humidity_range_9_upper_limit`')
        self._data["Relative Humidity Range 9 Upper Limit"] = value

    @property
    def range_9_equipment_list_name(self):
        """Get range_9_equipment_list_name

        Returns:
            str: the value of `range_9_equipment_list_name` or None if not set
        """
        return self._data["Range 9 Equipment List Name"]

    @range_9_equipment_list_name.setter
    def range_9_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `Range 9 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 9 Equipment List Name`
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
                                 'for field `range_9_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_9_equipment_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `range_9_equipment_list_name`')
        self._data["Range 9 Equipment List Name"] = value

    @property
    def relative_humidity_range_10_lower_limit(self):
        """Get relative_humidity_range_10_lower_limit

        Returns:
            float: the value of `relative_humidity_range_10_lower_limit` or None if not set
        """
        return self._data["Relative Humidity Range 10 Lower Limit"]

    @relative_humidity_range_10_lower_limit.setter
    def relative_humidity_range_10_lower_limit(self, value=None):
        """  Corresponds to IDD Field `Relative Humidity Range 10 Lower Limit`

        Args:
            value (float): value for IDD Field `Relative Humidity Range 10 Lower Limit`
                Units: percent
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
                                 'for field `relative_humidity_range_10_lower_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_humidity_range_10_lower_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `relative_humidity_range_10_lower_limit`')
        self._data["Relative Humidity Range 10 Lower Limit"] = value

    @property
    def relative_humidity_range_10_upper_limit(self):
        """Get relative_humidity_range_10_upper_limit

        Returns:
            float: the value of `relative_humidity_range_10_upper_limit` or None if not set
        """
        return self._data["Relative Humidity Range 10 Upper Limit"]

    @relative_humidity_range_10_upper_limit.setter
    def relative_humidity_range_10_upper_limit(self, value=None):
        """  Corresponds to IDD Field `Relative Humidity Range 10 Upper Limit`

        Args:
            value (float): value for IDD Field `Relative Humidity Range 10 Upper Limit`
                Units: percent
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
                                 'for field `relative_humidity_range_10_upper_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_humidity_range_10_upper_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `relative_humidity_range_10_upper_limit`')
        self._data["Relative Humidity Range 10 Upper Limit"] = value

    @property
    def range_10_equipment_list_name(self):
        """Get range_10_equipment_list_name

        Returns:
            str: the value of `range_10_equipment_list_name` or None if not set
        """
        return self._data["Range 10 Equipment List Name"]

    @range_10_equipment_list_name.setter
    def range_10_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `Range 10 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 10 Equipment List Name`
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
                                 'for field `range_10_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_10_equipment_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `range_10_equipment_list_name`')
        self._data["Range 10 Equipment List Name"] = value

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

class PlantEquipmentOperationOutdoorDewpoint(object):
    """ Corresponds to IDD object `PlantEquipmentOperation:OutdoorDewpoint`
        Plant equipment operation scheme for outdoor dewpoint temperature range operation.
        Specifies one or more groups of equipment which are available to operate for
        successive outdoor dewpoint temperature ranges.
    
    """
    internal_name = "PlantEquipmentOperation:OutdoorDewpoint"
    field_count = 31
    required_fields = ["Name", "Dewpoint Temperature Range 1 Lower Limit", "Dewpoint Temperature Range 1 Upper Limit", "Range 1 Equipment List Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `PlantEquipmentOperation:OutdoorDewpoint`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Dewpoint Temperature Range 1 Lower Limit"] = None
        self._data["Dewpoint Temperature Range 1 Upper Limit"] = None
        self._data["Range 1 Equipment List Name"] = None
        self._data["Dewpoint Temperature Range 2 Lower Limit"] = None
        self._data["Dewpoint Temperature Range 2 Upper Limit"] = None
        self._data["Range 2 Equipment List Name"] = None
        self._data["Dewpoint Temperature Range 3 Lower Limit"] = None
        self._data["Dewpoint Temperature Range 3 Upper Limit"] = None
        self._data["Range 3 Equipment List Name"] = None
        self._data["Dewpoint Temperature Range 4 Lower Limit"] = None
        self._data["Dewpoint Temperature Range 4 Upper Limit"] = None
        self._data["Range 4 Equipment List Name"] = None
        self._data["Dewpoint Temperature Range 5 Lower Limit"] = None
        self._data["Dewpoint Temperature Range 5 Upper Limit"] = None
        self._data["Range 5 Equipment List Name"] = None
        self._data["Dewpoint Temperature Range 6 Lower Limit"] = None
        self._data["Dewpoint Temperature Range 6 Upper Limit"] = None
        self._data["Range 6 Equipment List Name"] = None
        self._data["Dewpoint Temperature Range 7 Lower Limit"] = None
        self._data["Dewpoint Temperature Range 7 Upper Limit"] = None
        self._data["Range 7 Equipment List Name"] = None
        self._data["Dewpoint Temperature Range 8 Lower Limit"] = None
        self._data["Dewpoint Temperature Range 8 Upper Limit"] = None
        self._data["Range 8 Equipment List Name"] = None
        self._data["Dewpoint Temperature Range 9 Lower Limit"] = None
        self._data["Dewpoint Temperature Range 9 Upper Limit"] = None
        self._data["Range 9 Equipment List Name"] = None
        self._data["Dewpoint Temperature Range 10 Lower Limit"] = None
        self._data["Dewpoint Temperature Range 10 Upper Limit"] = None
        self._data["Range 10 Equipment List Name"] = None
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
            self.dewpoint_temperature_range_1_lower_limit = None
        else:
            self.dewpoint_temperature_range_1_lower_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.dewpoint_temperature_range_1_upper_limit = None
        else:
            self.dewpoint_temperature_range_1_upper_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.range_1_equipment_list_name = None
        else:
            self.range_1_equipment_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.dewpoint_temperature_range_2_lower_limit = None
        else:
            self.dewpoint_temperature_range_2_lower_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.dewpoint_temperature_range_2_upper_limit = None
        else:
            self.dewpoint_temperature_range_2_upper_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.range_2_equipment_list_name = None
        else:
            self.range_2_equipment_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.dewpoint_temperature_range_3_lower_limit = None
        else:
            self.dewpoint_temperature_range_3_lower_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.dewpoint_temperature_range_3_upper_limit = None
        else:
            self.dewpoint_temperature_range_3_upper_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.range_3_equipment_list_name = None
        else:
            self.range_3_equipment_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.dewpoint_temperature_range_4_lower_limit = None
        else:
            self.dewpoint_temperature_range_4_lower_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.dewpoint_temperature_range_4_upper_limit = None
        else:
            self.dewpoint_temperature_range_4_upper_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.range_4_equipment_list_name = None
        else:
            self.range_4_equipment_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.dewpoint_temperature_range_5_lower_limit = None
        else:
            self.dewpoint_temperature_range_5_lower_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.dewpoint_temperature_range_5_upper_limit = None
        else:
            self.dewpoint_temperature_range_5_upper_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.range_5_equipment_list_name = None
        else:
            self.range_5_equipment_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.dewpoint_temperature_range_6_lower_limit = None
        else:
            self.dewpoint_temperature_range_6_lower_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.dewpoint_temperature_range_6_upper_limit = None
        else:
            self.dewpoint_temperature_range_6_upper_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.range_6_equipment_list_name = None
        else:
            self.range_6_equipment_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.dewpoint_temperature_range_7_lower_limit = None
        else:
            self.dewpoint_temperature_range_7_lower_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.dewpoint_temperature_range_7_upper_limit = None
        else:
            self.dewpoint_temperature_range_7_upper_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.range_7_equipment_list_name = None
        else:
            self.range_7_equipment_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.dewpoint_temperature_range_8_lower_limit = None
        else:
            self.dewpoint_temperature_range_8_lower_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.dewpoint_temperature_range_8_upper_limit = None
        else:
            self.dewpoint_temperature_range_8_upper_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.range_8_equipment_list_name = None
        else:
            self.range_8_equipment_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.dewpoint_temperature_range_9_lower_limit = None
        else:
            self.dewpoint_temperature_range_9_lower_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.dewpoint_temperature_range_9_upper_limit = None
        else:
            self.dewpoint_temperature_range_9_upper_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.range_9_equipment_list_name = None
        else:
            self.range_9_equipment_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.dewpoint_temperature_range_10_lower_limit = None
        else:
            self.dewpoint_temperature_range_10_lower_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.dewpoint_temperature_range_10_upper_limit = None
        else:
            self.dewpoint_temperature_range_10_upper_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.range_10_equipment_list_name = None
        else:
            self.range_10_equipment_list_name = vals[i]
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
    def dewpoint_temperature_range_1_lower_limit(self):
        """Get dewpoint_temperature_range_1_lower_limit

        Returns:
            float: the value of `dewpoint_temperature_range_1_lower_limit` or None if not set
        """
        return self._data["Dewpoint Temperature Range 1 Lower Limit"]

    @dewpoint_temperature_range_1_lower_limit.setter
    def dewpoint_temperature_range_1_lower_limit(self, value=None):
        """  Corresponds to IDD Field `Dewpoint Temperature Range 1 Lower Limit`

        Args:
            value (float): value for IDD Field `Dewpoint Temperature Range 1 Lower Limit`
                Units: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `dewpoint_temperature_range_1_lower_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `dewpoint_temperature_range_1_lower_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `dewpoint_temperature_range_1_lower_limit`')
        self._data["Dewpoint Temperature Range 1 Lower Limit"] = value

    @property
    def dewpoint_temperature_range_1_upper_limit(self):
        """Get dewpoint_temperature_range_1_upper_limit

        Returns:
            float: the value of `dewpoint_temperature_range_1_upper_limit` or None if not set
        """
        return self._data["Dewpoint Temperature Range 1 Upper Limit"]

    @dewpoint_temperature_range_1_upper_limit.setter
    def dewpoint_temperature_range_1_upper_limit(self, value=None):
        """  Corresponds to IDD Field `Dewpoint Temperature Range 1 Upper Limit`

        Args:
            value (float): value for IDD Field `Dewpoint Temperature Range 1 Upper Limit`
                Units: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `dewpoint_temperature_range_1_upper_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `dewpoint_temperature_range_1_upper_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `dewpoint_temperature_range_1_upper_limit`')
        self._data["Dewpoint Temperature Range 1 Upper Limit"] = value

    @property
    def range_1_equipment_list_name(self):
        """Get range_1_equipment_list_name

        Returns:
            str: the value of `range_1_equipment_list_name` or None if not set
        """
        return self._data["Range 1 Equipment List Name"]

    @range_1_equipment_list_name.setter
    def range_1_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `Range 1 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 1 Equipment List Name`
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
                                 'for field `range_1_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_1_equipment_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `range_1_equipment_list_name`')
        self._data["Range 1 Equipment List Name"] = value

    @property
    def dewpoint_temperature_range_2_lower_limit(self):
        """Get dewpoint_temperature_range_2_lower_limit

        Returns:
            float: the value of `dewpoint_temperature_range_2_lower_limit` or None if not set
        """
        return self._data["Dewpoint Temperature Range 2 Lower Limit"]

    @dewpoint_temperature_range_2_lower_limit.setter
    def dewpoint_temperature_range_2_lower_limit(self, value=None):
        """  Corresponds to IDD Field `Dewpoint Temperature Range 2 Lower Limit`

        Args:
            value (float): value for IDD Field `Dewpoint Temperature Range 2 Lower Limit`
                Units: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `dewpoint_temperature_range_2_lower_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `dewpoint_temperature_range_2_lower_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `dewpoint_temperature_range_2_lower_limit`')
        self._data["Dewpoint Temperature Range 2 Lower Limit"] = value

    @property
    def dewpoint_temperature_range_2_upper_limit(self):
        """Get dewpoint_temperature_range_2_upper_limit

        Returns:
            float: the value of `dewpoint_temperature_range_2_upper_limit` or None if not set
        """
        return self._data["Dewpoint Temperature Range 2 Upper Limit"]

    @dewpoint_temperature_range_2_upper_limit.setter
    def dewpoint_temperature_range_2_upper_limit(self, value=None):
        """  Corresponds to IDD Field `Dewpoint Temperature Range 2 Upper Limit`

        Args:
            value (float): value for IDD Field `Dewpoint Temperature Range 2 Upper Limit`
                Units: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `dewpoint_temperature_range_2_upper_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `dewpoint_temperature_range_2_upper_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `dewpoint_temperature_range_2_upper_limit`')
        self._data["Dewpoint Temperature Range 2 Upper Limit"] = value

    @property
    def range_2_equipment_list_name(self):
        """Get range_2_equipment_list_name

        Returns:
            str: the value of `range_2_equipment_list_name` or None if not set
        """
        return self._data["Range 2 Equipment List Name"]

    @range_2_equipment_list_name.setter
    def range_2_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `Range 2 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 2 Equipment List Name`
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
                                 'for field `range_2_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_2_equipment_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `range_2_equipment_list_name`')
        self._data["Range 2 Equipment List Name"] = value

    @property
    def dewpoint_temperature_range_3_lower_limit(self):
        """Get dewpoint_temperature_range_3_lower_limit

        Returns:
            float: the value of `dewpoint_temperature_range_3_lower_limit` or None if not set
        """
        return self._data["Dewpoint Temperature Range 3 Lower Limit"]

    @dewpoint_temperature_range_3_lower_limit.setter
    def dewpoint_temperature_range_3_lower_limit(self, value=None):
        """  Corresponds to IDD Field `Dewpoint Temperature Range 3 Lower Limit`

        Args:
            value (float): value for IDD Field `Dewpoint Temperature Range 3 Lower Limit`
                Units: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `dewpoint_temperature_range_3_lower_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `dewpoint_temperature_range_3_lower_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `dewpoint_temperature_range_3_lower_limit`')
        self._data["Dewpoint Temperature Range 3 Lower Limit"] = value

    @property
    def dewpoint_temperature_range_3_upper_limit(self):
        """Get dewpoint_temperature_range_3_upper_limit

        Returns:
            float: the value of `dewpoint_temperature_range_3_upper_limit` or None if not set
        """
        return self._data["Dewpoint Temperature Range 3 Upper Limit"]

    @dewpoint_temperature_range_3_upper_limit.setter
    def dewpoint_temperature_range_3_upper_limit(self, value=None):
        """  Corresponds to IDD Field `Dewpoint Temperature Range 3 Upper Limit`

        Args:
            value (float): value for IDD Field `Dewpoint Temperature Range 3 Upper Limit`
                Units: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `dewpoint_temperature_range_3_upper_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `dewpoint_temperature_range_3_upper_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `dewpoint_temperature_range_3_upper_limit`')
        self._data["Dewpoint Temperature Range 3 Upper Limit"] = value

    @property
    def range_3_equipment_list_name(self):
        """Get range_3_equipment_list_name

        Returns:
            str: the value of `range_3_equipment_list_name` or None if not set
        """
        return self._data["Range 3 Equipment List Name"]

    @range_3_equipment_list_name.setter
    def range_3_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `Range 3 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 3 Equipment List Name`
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
                                 'for field `range_3_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_3_equipment_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `range_3_equipment_list_name`')
        self._data["Range 3 Equipment List Name"] = value

    @property
    def dewpoint_temperature_range_4_lower_limit(self):
        """Get dewpoint_temperature_range_4_lower_limit

        Returns:
            float: the value of `dewpoint_temperature_range_4_lower_limit` or None if not set
        """
        return self._data["Dewpoint Temperature Range 4 Lower Limit"]

    @dewpoint_temperature_range_4_lower_limit.setter
    def dewpoint_temperature_range_4_lower_limit(self, value=None):
        """  Corresponds to IDD Field `Dewpoint Temperature Range 4 Lower Limit`

        Args:
            value (float): value for IDD Field `Dewpoint Temperature Range 4 Lower Limit`
                Units: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `dewpoint_temperature_range_4_lower_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `dewpoint_temperature_range_4_lower_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `dewpoint_temperature_range_4_lower_limit`')
        self._data["Dewpoint Temperature Range 4 Lower Limit"] = value

    @property
    def dewpoint_temperature_range_4_upper_limit(self):
        """Get dewpoint_temperature_range_4_upper_limit

        Returns:
            float: the value of `dewpoint_temperature_range_4_upper_limit` or None if not set
        """
        return self._data["Dewpoint Temperature Range 4 Upper Limit"]

    @dewpoint_temperature_range_4_upper_limit.setter
    def dewpoint_temperature_range_4_upper_limit(self, value=None):
        """  Corresponds to IDD Field `Dewpoint Temperature Range 4 Upper Limit`

        Args:
            value (float): value for IDD Field `Dewpoint Temperature Range 4 Upper Limit`
                Units: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `dewpoint_temperature_range_4_upper_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `dewpoint_temperature_range_4_upper_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `dewpoint_temperature_range_4_upper_limit`')
        self._data["Dewpoint Temperature Range 4 Upper Limit"] = value

    @property
    def range_4_equipment_list_name(self):
        """Get range_4_equipment_list_name

        Returns:
            str: the value of `range_4_equipment_list_name` or None if not set
        """
        return self._data["Range 4 Equipment List Name"]

    @range_4_equipment_list_name.setter
    def range_4_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `Range 4 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 4 Equipment List Name`
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
                                 'for field `range_4_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_4_equipment_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `range_4_equipment_list_name`')
        self._data["Range 4 Equipment List Name"] = value

    @property
    def dewpoint_temperature_range_5_lower_limit(self):
        """Get dewpoint_temperature_range_5_lower_limit

        Returns:
            float: the value of `dewpoint_temperature_range_5_lower_limit` or None if not set
        """
        return self._data["Dewpoint Temperature Range 5 Lower Limit"]

    @dewpoint_temperature_range_5_lower_limit.setter
    def dewpoint_temperature_range_5_lower_limit(self, value=None):
        """  Corresponds to IDD Field `Dewpoint Temperature Range 5 Lower Limit`

        Args:
            value (float): value for IDD Field `Dewpoint Temperature Range 5 Lower Limit`
                Units: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `dewpoint_temperature_range_5_lower_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `dewpoint_temperature_range_5_lower_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `dewpoint_temperature_range_5_lower_limit`')
        self._data["Dewpoint Temperature Range 5 Lower Limit"] = value

    @property
    def dewpoint_temperature_range_5_upper_limit(self):
        """Get dewpoint_temperature_range_5_upper_limit

        Returns:
            float: the value of `dewpoint_temperature_range_5_upper_limit` or None if not set
        """
        return self._data["Dewpoint Temperature Range 5 Upper Limit"]

    @dewpoint_temperature_range_5_upper_limit.setter
    def dewpoint_temperature_range_5_upper_limit(self, value=None):
        """  Corresponds to IDD Field `Dewpoint Temperature Range 5 Upper Limit`

        Args:
            value (float): value for IDD Field `Dewpoint Temperature Range 5 Upper Limit`
                Units: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `dewpoint_temperature_range_5_upper_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `dewpoint_temperature_range_5_upper_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `dewpoint_temperature_range_5_upper_limit`')
        self._data["Dewpoint Temperature Range 5 Upper Limit"] = value

    @property
    def range_5_equipment_list_name(self):
        """Get range_5_equipment_list_name

        Returns:
            str: the value of `range_5_equipment_list_name` or None if not set
        """
        return self._data["Range 5 Equipment List Name"]

    @range_5_equipment_list_name.setter
    def range_5_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `Range 5 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 5 Equipment List Name`
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
                                 'for field `range_5_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_5_equipment_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `range_5_equipment_list_name`')
        self._data["Range 5 Equipment List Name"] = value

    @property
    def dewpoint_temperature_range_6_lower_limit(self):
        """Get dewpoint_temperature_range_6_lower_limit

        Returns:
            float: the value of `dewpoint_temperature_range_6_lower_limit` or None if not set
        """
        return self._data["Dewpoint Temperature Range 6 Lower Limit"]

    @dewpoint_temperature_range_6_lower_limit.setter
    def dewpoint_temperature_range_6_lower_limit(self, value=None):
        """  Corresponds to IDD Field `Dewpoint Temperature Range 6 Lower Limit`

        Args:
            value (float): value for IDD Field `Dewpoint Temperature Range 6 Lower Limit`
                Units: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `dewpoint_temperature_range_6_lower_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `dewpoint_temperature_range_6_lower_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `dewpoint_temperature_range_6_lower_limit`')
        self._data["Dewpoint Temperature Range 6 Lower Limit"] = value

    @property
    def dewpoint_temperature_range_6_upper_limit(self):
        """Get dewpoint_temperature_range_6_upper_limit

        Returns:
            float: the value of `dewpoint_temperature_range_6_upper_limit` or None if not set
        """
        return self._data["Dewpoint Temperature Range 6 Upper Limit"]

    @dewpoint_temperature_range_6_upper_limit.setter
    def dewpoint_temperature_range_6_upper_limit(self, value=None):
        """  Corresponds to IDD Field `Dewpoint Temperature Range 6 Upper Limit`

        Args:
            value (float): value for IDD Field `Dewpoint Temperature Range 6 Upper Limit`
                Units: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `dewpoint_temperature_range_6_upper_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `dewpoint_temperature_range_6_upper_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `dewpoint_temperature_range_6_upper_limit`')
        self._data["Dewpoint Temperature Range 6 Upper Limit"] = value

    @property
    def range_6_equipment_list_name(self):
        """Get range_6_equipment_list_name

        Returns:
            str: the value of `range_6_equipment_list_name` or None if not set
        """
        return self._data["Range 6 Equipment List Name"]

    @range_6_equipment_list_name.setter
    def range_6_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `Range 6 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 6 Equipment List Name`
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
                                 'for field `range_6_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_6_equipment_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `range_6_equipment_list_name`')
        self._data["Range 6 Equipment List Name"] = value

    @property
    def dewpoint_temperature_range_7_lower_limit(self):
        """Get dewpoint_temperature_range_7_lower_limit

        Returns:
            float: the value of `dewpoint_temperature_range_7_lower_limit` or None if not set
        """
        return self._data["Dewpoint Temperature Range 7 Lower Limit"]

    @dewpoint_temperature_range_7_lower_limit.setter
    def dewpoint_temperature_range_7_lower_limit(self, value=None):
        """  Corresponds to IDD Field `Dewpoint Temperature Range 7 Lower Limit`

        Args:
            value (float): value for IDD Field `Dewpoint Temperature Range 7 Lower Limit`
                Units: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `dewpoint_temperature_range_7_lower_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `dewpoint_temperature_range_7_lower_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `dewpoint_temperature_range_7_lower_limit`')
        self._data["Dewpoint Temperature Range 7 Lower Limit"] = value

    @property
    def dewpoint_temperature_range_7_upper_limit(self):
        """Get dewpoint_temperature_range_7_upper_limit

        Returns:
            float: the value of `dewpoint_temperature_range_7_upper_limit` or None if not set
        """
        return self._data["Dewpoint Temperature Range 7 Upper Limit"]

    @dewpoint_temperature_range_7_upper_limit.setter
    def dewpoint_temperature_range_7_upper_limit(self, value=None):
        """  Corresponds to IDD Field `Dewpoint Temperature Range 7 Upper Limit`

        Args:
            value (float): value for IDD Field `Dewpoint Temperature Range 7 Upper Limit`
                Units: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `dewpoint_temperature_range_7_upper_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `dewpoint_temperature_range_7_upper_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `dewpoint_temperature_range_7_upper_limit`')
        self._data["Dewpoint Temperature Range 7 Upper Limit"] = value

    @property
    def range_7_equipment_list_name(self):
        """Get range_7_equipment_list_name

        Returns:
            str: the value of `range_7_equipment_list_name` or None if not set
        """
        return self._data["Range 7 Equipment List Name"]

    @range_7_equipment_list_name.setter
    def range_7_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `Range 7 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 7 Equipment List Name`
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
                                 'for field `range_7_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_7_equipment_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `range_7_equipment_list_name`')
        self._data["Range 7 Equipment List Name"] = value

    @property
    def dewpoint_temperature_range_8_lower_limit(self):
        """Get dewpoint_temperature_range_8_lower_limit

        Returns:
            float: the value of `dewpoint_temperature_range_8_lower_limit` or None if not set
        """
        return self._data["Dewpoint Temperature Range 8 Lower Limit"]

    @dewpoint_temperature_range_8_lower_limit.setter
    def dewpoint_temperature_range_8_lower_limit(self, value=None):
        """  Corresponds to IDD Field `Dewpoint Temperature Range 8 Lower Limit`

        Args:
            value (float): value for IDD Field `Dewpoint Temperature Range 8 Lower Limit`
                Units: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `dewpoint_temperature_range_8_lower_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `dewpoint_temperature_range_8_lower_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `dewpoint_temperature_range_8_lower_limit`')
        self._data["Dewpoint Temperature Range 8 Lower Limit"] = value

    @property
    def dewpoint_temperature_range_8_upper_limit(self):
        """Get dewpoint_temperature_range_8_upper_limit

        Returns:
            float: the value of `dewpoint_temperature_range_8_upper_limit` or None if not set
        """
        return self._data["Dewpoint Temperature Range 8 Upper Limit"]

    @dewpoint_temperature_range_8_upper_limit.setter
    def dewpoint_temperature_range_8_upper_limit(self, value=None):
        """  Corresponds to IDD Field `Dewpoint Temperature Range 8 Upper Limit`

        Args:
            value (float): value for IDD Field `Dewpoint Temperature Range 8 Upper Limit`
                Units: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `dewpoint_temperature_range_8_upper_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `dewpoint_temperature_range_8_upper_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `dewpoint_temperature_range_8_upper_limit`')
        self._data["Dewpoint Temperature Range 8 Upper Limit"] = value

    @property
    def range_8_equipment_list_name(self):
        """Get range_8_equipment_list_name

        Returns:
            str: the value of `range_8_equipment_list_name` or None if not set
        """
        return self._data["Range 8 Equipment List Name"]

    @range_8_equipment_list_name.setter
    def range_8_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `Range 8 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 8 Equipment List Name`
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
                                 'for field `range_8_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_8_equipment_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `range_8_equipment_list_name`')
        self._data["Range 8 Equipment List Name"] = value

    @property
    def dewpoint_temperature_range_9_lower_limit(self):
        """Get dewpoint_temperature_range_9_lower_limit

        Returns:
            float: the value of `dewpoint_temperature_range_9_lower_limit` or None if not set
        """
        return self._data["Dewpoint Temperature Range 9 Lower Limit"]

    @dewpoint_temperature_range_9_lower_limit.setter
    def dewpoint_temperature_range_9_lower_limit(self, value=None):
        """  Corresponds to IDD Field `Dewpoint Temperature Range 9 Lower Limit`

        Args:
            value (float): value for IDD Field `Dewpoint Temperature Range 9 Lower Limit`
                Units: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `dewpoint_temperature_range_9_lower_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `dewpoint_temperature_range_9_lower_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `dewpoint_temperature_range_9_lower_limit`')
        self._data["Dewpoint Temperature Range 9 Lower Limit"] = value

    @property
    def dewpoint_temperature_range_9_upper_limit(self):
        """Get dewpoint_temperature_range_9_upper_limit

        Returns:
            float: the value of `dewpoint_temperature_range_9_upper_limit` or None if not set
        """
        return self._data["Dewpoint Temperature Range 9 Upper Limit"]

    @dewpoint_temperature_range_9_upper_limit.setter
    def dewpoint_temperature_range_9_upper_limit(self, value=None):
        """  Corresponds to IDD Field `Dewpoint Temperature Range 9 Upper Limit`

        Args:
            value (float): value for IDD Field `Dewpoint Temperature Range 9 Upper Limit`
                Units: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `dewpoint_temperature_range_9_upper_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `dewpoint_temperature_range_9_upper_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `dewpoint_temperature_range_9_upper_limit`')
        self._data["Dewpoint Temperature Range 9 Upper Limit"] = value

    @property
    def range_9_equipment_list_name(self):
        """Get range_9_equipment_list_name

        Returns:
            str: the value of `range_9_equipment_list_name` or None if not set
        """
        return self._data["Range 9 Equipment List Name"]

    @range_9_equipment_list_name.setter
    def range_9_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `Range 9 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 9 Equipment List Name`
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
                                 'for field `range_9_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_9_equipment_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `range_9_equipment_list_name`')
        self._data["Range 9 Equipment List Name"] = value

    @property
    def dewpoint_temperature_range_10_lower_limit(self):
        """Get dewpoint_temperature_range_10_lower_limit

        Returns:
            float: the value of `dewpoint_temperature_range_10_lower_limit` or None if not set
        """
        return self._data["Dewpoint Temperature Range 10 Lower Limit"]

    @dewpoint_temperature_range_10_lower_limit.setter
    def dewpoint_temperature_range_10_lower_limit(self, value=None):
        """  Corresponds to IDD Field `Dewpoint Temperature Range 10 Lower Limit`

        Args:
            value (float): value for IDD Field `Dewpoint Temperature Range 10 Lower Limit`
                Units: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `dewpoint_temperature_range_10_lower_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `dewpoint_temperature_range_10_lower_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `dewpoint_temperature_range_10_lower_limit`')
        self._data["Dewpoint Temperature Range 10 Lower Limit"] = value

    @property
    def dewpoint_temperature_range_10_upper_limit(self):
        """Get dewpoint_temperature_range_10_upper_limit

        Returns:
            float: the value of `dewpoint_temperature_range_10_upper_limit` or None if not set
        """
        return self._data["Dewpoint Temperature Range 10 Upper Limit"]

    @dewpoint_temperature_range_10_upper_limit.setter
    def dewpoint_temperature_range_10_upper_limit(self, value=None):
        """  Corresponds to IDD Field `Dewpoint Temperature Range 10 Upper Limit`

        Args:
            value (float): value for IDD Field `Dewpoint Temperature Range 10 Upper Limit`
                Units: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `dewpoint_temperature_range_10_upper_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `dewpoint_temperature_range_10_upper_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `dewpoint_temperature_range_10_upper_limit`')
        self._data["Dewpoint Temperature Range 10 Upper Limit"] = value

    @property
    def range_10_equipment_list_name(self):
        """Get range_10_equipment_list_name

        Returns:
            str: the value of `range_10_equipment_list_name` or None if not set
        """
        return self._data["Range 10 Equipment List Name"]

    @range_10_equipment_list_name.setter
    def range_10_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `Range 10 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 10 Equipment List Name`
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
                                 'for field `range_10_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_10_equipment_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `range_10_equipment_list_name`')
        self._data["Range 10 Equipment List Name"] = value

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

class PlantEquipmentOperationComponentSetpoint(object):
    """ Corresponds to IDD object `PlantEquipmentOperation:ComponentSetpoint`
        Plant equipment operation scheme for component setpoint operation. Specifies one or
        pieces of equipment which are controlled to meet the temperature setpoint at the
        component outlet node.
    
    """
    internal_name = "PlantEquipmentOperation:ComponentSetpoint"
    field_count = 61
    required_fields = ["Name", "Equipment 1 Object Type", "Equipment 1 Name", "Demand Calculation 1 Node Name", "Setpoint 1 Node Name", "Component 1 Flow Rate", "Operation 1 Type"]

    def __init__(self):
        """ Init data dictionary object for IDD  `PlantEquipmentOperation:ComponentSetpoint`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Equipment 1 Object Type"] = None
        self._data["Equipment 1 Name"] = None
        self._data["Demand Calculation 1 Node Name"] = None
        self._data["Setpoint 1 Node Name"] = None
        self._data["Component 1 Flow Rate"] = None
        self._data["Operation 1 Type"] = None
        self._data["Equipment 2 Object Type"] = None
        self._data["Equipment 2 Name"] = None
        self._data["Demand Calculation 2 Node Name"] = None
        self._data["Setpoint 2 Node Name"] = None
        self._data["Component 2 Flow Rate"] = None
        self._data["Operation 2 Type"] = None
        self._data["Equipment 3 Object Type"] = None
        self._data["Equipment 3 Name"] = None
        self._data["Demand Calculation 3 Node Name"] = None
        self._data["Setpoint 3 Node Name"] = None
        self._data["Component 3 Flow Rate"] = None
        self._data["Operation 3 Type"] = None
        self._data["Equipment 4 Object Type"] = None
        self._data["Equipment 4 Name"] = None
        self._data["Demand Calculation 4 Node Name"] = None
        self._data["Setpoint 4 Node Name"] = None
        self._data["Component 4 Flow Rate"] = None
        self._data["Operation 4 Type"] = None
        self._data["Equipment 5 Object Type"] = None
        self._data["Equipment 5 Name"] = None
        self._data["Demand Calculation 5 Node Name"] = None
        self._data["Setpoint 5 Node Name"] = None
        self._data["Component 5 Flow Rate"] = None
        self._data["Operation 5 Type"] = None
        self._data["Equipment 6 Object Type"] = None
        self._data["Equipment 6 Name"] = None
        self._data["Demand Calculation 6 Node Name"] = None
        self._data["Setpoint 6 Node Name"] = None
        self._data["Component 6 Flow Rate"] = None
        self._data["Operation 6 Type"] = None
        self._data["Equipment 7 Object Type"] = None
        self._data["Equipment 7 Name"] = None
        self._data["Demand Calculation 7 Node Name"] = None
        self._data["Setpoint 7 Node Name"] = None
        self._data["Component 7 Flow Rate"] = None
        self._data["Operation 7 Type"] = None
        self._data["Equipment 8 Object Type"] = None
        self._data["Equipment 8 Name"] = None
        self._data["Demand Calculation 8 Node Name"] = None
        self._data["Setpoint 8 Node Name"] = None
        self._data["Component 8 Flow Rate"] = None
        self._data["Operation 8 Type"] = None
        self._data["Equipment 9 Object Type"] = None
        self._data["Equipment 9 Name"] = None
        self._data["Demand Calculation 9 Node Name"] = None
        self._data["Setpoint 9 Node Name"] = None
        self._data["Component 9 Flow Rate"] = None
        self._data["Operation 9 Type"] = None
        self._data["Equipment 10 Object Type"] = None
        self._data["Equipment 10 Name"] = None
        self._data["Demand Calculation 10 Node Name"] = None
        self._data["Setpoint 10 Node Name"] = None
        self._data["Component 10 Flow Rate"] = None
        self._data["Operation 10 Type"] = None
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
            self.equipment_1_object_type = None
        else:
            self.equipment_1_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.equipment_1_name = None
        else:
            self.equipment_1_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.demand_calculation_1_node_name = None
        else:
            self.demand_calculation_1_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.setpoint_1_node_name = None
        else:
            self.setpoint_1_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_1_flow_rate = None
        else:
            self.component_1_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.operation_1_type = None
        else:
            self.operation_1_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.equipment_2_object_type = None
        else:
            self.equipment_2_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.equipment_2_name = None
        else:
            self.equipment_2_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.demand_calculation_2_node_name = None
        else:
            self.demand_calculation_2_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.setpoint_2_node_name = None
        else:
            self.setpoint_2_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_2_flow_rate = None
        else:
            self.component_2_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.operation_2_type = None
        else:
            self.operation_2_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.equipment_3_object_type = None
        else:
            self.equipment_3_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.equipment_3_name = None
        else:
            self.equipment_3_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.demand_calculation_3_node_name = None
        else:
            self.demand_calculation_3_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.setpoint_3_node_name = None
        else:
            self.setpoint_3_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_3_flow_rate = None
        else:
            self.component_3_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.operation_3_type = None
        else:
            self.operation_3_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.equipment_4_object_type = None
        else:
            self.equipment_4_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.equipment_4_name = None
        else:
            self.equipment_4_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.demand_calculation_4_node_name = None
        else:
            self.demand_calculation_4_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.setpoint_4_node_name = None
        else:
            self.setpoint_4_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_4_flow_rate = None
        else:
            self.component_4_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.operation_4_type = None
        else:
            self.operation_4_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.equipment_5_object_type = None
        else:
            self.equipment_5_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.equipment_5_name = None
        else:
            self.equipment_5_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.demand_calculation_5_node_name = None
        else:
            self.demand_calculation_5_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.setpoint_5_node_name = None
        else:
            self.setpoint_5_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_5_flow_rate = None
        else:
            self.component_5_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.operation_5_type = None
        else:
            self.operation_5_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.equipment_6_object_type = None
        else:
            self.equipment_6_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.equipment_6_name = None
        else:
            self.equipment_6_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.demand_calculation_6_node_name = None
        else:
            self.demand_calculation_6_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.setpoint_6_node_name = None
        else:
            self.setpoint_6_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_6_flow_rate = None
        else:
            self.component_6_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.operation_6_type = None
        else:
            self.operation_6_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.equipment_7_object_type = None
        else:
            self.equipment_7_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.equipment_7_name = None
        else:
            self.equipment_7_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.demand_calculation_7_node_name = None
        else:
            self.demand_calculation_7_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.setpoint_7_node_name = None
        else:
            self.setpoint_7_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_7_flow_rate = None
        else:
            self.component_7_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.operation_7_type = None
        else:
            self.operation_7_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.equipment_8_object_type = None
        else:
            self.equipment_8_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.equipment_8_name = None
        else:
            self.equipment_8_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.demand_calculation_8_node_name = None
        else:
            self.demand_calculation_8_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.setpoint_8_node_name = None
        else:
            self.setpoint_8_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_8_flow_rate = None
        else:
            self.component_8_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.operation_8_type = None
        else:
            self.operation_8_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.equipment_9_object_type = None
        else:
            self.equipment_9_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.equipment_9_name = None
        else:
            self.equipment_9_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.demand_calculation_9_node_name = None
        else:
            self.demand_calculation_9_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.setpoint_9_node_name = None
        else:
            self.setpoint_9_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_9_flow_rate = None
        else:
            self.component_9_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.operation_9_type = None
        else:
            self.operation_9_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.equipment_10_object_type = None
        else:
            self.equipment_10_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.equipment_10_name = None
        else:
            self.equipment_10_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.demand_calculation_10_node_name = None
        else:
            self.demand_calculation_10_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.setpoint_10_node_name = None
        else:
            self.setpoint_10_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_10_flow_rate = None
        else:
            self.component_10_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.operation_10_type = None
        else:
            self.operation_10_type = vals[i]
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
    def equipment_1_object_type(self):
        """Get equipment_1_object_type

        Returns:
            str: the value of `equipment_1_object_type` or None if not set
        """
        return self._data["Equipment 1 Object Type"]

    @equipment_1_object_type.setter
    def equipment_1_object_type(self, value=None):
        """  Corresponds to IDD Field `Equipment 1 Object Type`

        Args:
            value (str): value for IDD Field `Equipment 1 Object Type`
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
                                 'for field `equipment_1_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_1_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `equipment_1_object_type`')
        self._data["Equipment 1 Object Type"] = value

    @property
    def equipment_1_name(self):
        """Get equipment_1_name

        Returns:
            str: the value of `equipment_1_name` or None if not set
        """
        return self._data["Equipment 1 Name"]

    @equipment_1_name.setter
    def equipment_1_name(self, value=None):
        """  Corresponds to IDD Field `Equipment 1 Name`

        Args:
            value (str): value for IDD Field `Equipment 1 Name`
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
                                 'for field `equipment_1_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_1_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `equipment_1_name`')
        self._data["Equipment 1 Name"] = value

    @property
    def demand_calculation_1_node_name(self):
        """Get demand_calculation_1_node_name

        Returns:
            str: the value of `demand_calculation_1_node_name` or None if not set
        """
        return self._data["Demand Calculation 1 Node Name"]

    @demand_calculation_1_node_name.setter
    def demand_calculation_1_node_name(self, value=None):
        """  Corresponds to IDD Field `Demand Calculation 1 Node Name`

        Args:
            value (str): value for IDD Field `Demand Calculation 1 Node Name`
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
                                 'for field `demand_calculation_1_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `demand_calculation_1_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `demand_calculation_1_node_name`')
        self._data["Demand Calculation 1 Node Name"] = value

    @property
    def setpoint_1_node_name(self):
        """Get setpoint_1_node_name

        Returns:
            str: the value of `setpoint_1_node_name` or None if not set
        """
        return self._data["Setpoint 1 Node Name"]

    @setpoint_1_node_name.setter
    def setpoint_1_node_name(self, value=None):
        """  Corresponds to IDD Field `Setpoint 1 Node Name`

        Args:
            value (str): value for IDD Field `Setpoint 1 Node Name`
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
                                 'for field `setpoint_1_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `setpoint_1_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `setpoint_1_node_name`')
        self._data["Setpoint 1 Node Name"] = value

    @property
    def component_1_flow_rate(self):
        """Get component_1_flow_rate

        Returns:
            float: the value of `component_1_flow_rate` or None if not set
        """
        return self._data["Component 1 Flow Rate"]

    @component_1_flow_rate.setter
    def component_1_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Component 1 Flow Rate`

        Args:
            value (float or "Autosize"): value for IDD Field `Component 1 Flow Rate`
                Units: m3/s
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Component 1 Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `component_1_flow_rate`'.format(value))
        self._data["Component 1 Flow Rate"] = value

    @property
    def operation_1_type(self):
        """Get operation_1_type

        Returns:
            str: the value of `operation_1_type` or None if not set
        """
        return self._data["Operation 1 Type"]

    @operation_1_type.setter
    def operation_1_type(self, value=None):
        """  Corresponds to IDD Field `Operation 1 Type`

        Args:
            value (str): value for IDD Field `Operation 1 Type`
                Accepted values are:
                      - Heating
                      - Cooling
                      - Dual
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
                                 'for field `operation_1_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `operation_1_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `operation_1_type`')
            vals = {}
            vals["heating"] = "Heating"
            vals["cooling"] = "Cooling"
            vals["dual"] = "Dual"
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
                                     'field `operation_1_type`'.format(value))
            value = vals[value_lower]
        self._data["Operation 1 Type"] = value

    @property
    def equipment_2_object_type(self):
        """Get equipment_2_object_type

        Returns:
            str: the value of `equipment_2_object_type` or None if not set
        """
        return self._data["Equipment 2 Object Type"]

    @equipment_2_object_type.setter
    def equipment_2_object_type(self, value=None):
        """  Corresponds to IDD Field `Equipment 2 Object Type`

        Args:
            value (str): value for IDD Field `Equipment 2 Object Type`
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
                                 'for field `equipment_2_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_2_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `equipment_2_object_type`')
        self._data["Equipment 2 Object Type"] = value

    @property
    def equipment_2_name(self):
        """Get equipment_2_name

        Returns:
            str: the value of `equipment_2_name` or None if not set
        """
        return self._data["Equipment 2 Name"]

    @equipment_2_name.setter
    def equipment_2_name(self, value=None):
        """  Corresponds to IDD Field `Equipment 2 Name`

        Args:
            value (str): value for IDD Field `Equipment 2 Name`
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
                                 'for field `equipment_2_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_2_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `equipment_2_name`')
        self._data["Equipment 2 Name"] = value

    @property
    def demand_calculation_2_node_name(self):
        """Get demand_calculation_2_node_name

        Returns:
            str: the value of `demand_calculation_2_node_name` or None if not set
        """
        return self._data["Demand Calculation 2 Node Name"]

    @demand_calculation_2_node_name.setter
    def demand_calculation_2_node_name(self, value=None):
        """  Corresponds to IDD Field `Demand Calculation 2 Node Name`

        Args:
            value (str): value for IDD Field `Demand Calculation 2 Node Name`
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
                                 'for field `demand_calculation_2_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `demand_calculation_2_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `demand_calculation_2_node_name`')
        self._data["Demand Calculation 2 Node Name"] = value

    @property
    def setpoint_2_node_name(self):
        """Get setpoint_2_node_name

        Returns:
            str: the value of `setpoint_2_node_name` or None if not set
        """
        return self._data["Setpoint 2 Node Name"]

    @setpoint_2_node_name.setter
    def setpoint_2_node_name(self, value=None):
        """  Corresponds to IDD Field `Setpoint 2 Node Name`

        Args:
            value (str): value for IDD Field `Setpoint 2 Node Name`
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
                                 'for field `setpoint_2_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `setpoint_2_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `setpoint_2_node_name`')
        self._data["Setpoint 2 Node Name"] = value

    @property
    def component_2_flow_rate(self):
        """Get component_2_flow_rate

        Returns:
            float: the value of `component_2_flow_rate` or None if not set
        """
        return self._data["Component 2 Flow Rate"]

    @component_2_flow_rate.setter
    def component_2_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Component 2 Flow Rate`

        Args:
            value (float or "Autosize"): value for IDD Field `Component 2 Flow Rate`
                Units: m3/s
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Component 2 Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `component_2_flow_rate`'.format(value))
        self._data["Component 2 Flow Rate"] = value

    @property
    def operation_2_type(self):
        """Get operation_2_type

        Returns:
            str: the value of `operation_2_type` or None if not set
        """
        return self._data["Operation 2 Type"]

    @operation_2_type.setter
    def operation_2_type(self, value=None):
        """  Corresponds to IDD Field `Operation 2 Type`

        Args:
            value (str): value for IDD Field `Operation 2 Type`
                Accepted values are:
                      - Heating
                      - Cooling
                      - Dual
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
                                 'for field `operation_2_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `operation_2_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `operation_2_type`')
            vals = {}
            vals["heating"] = "Heating"
            vals["cooling"] = "Cooling"
            vals["dual"] = "Dual"
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
                                     'field `operation_2_type`'.format(value))
            value = vals[value_lower]
        self._data["Operation 2 Type"] = value

    @property
    def equipment_3_object_type(self):
        """Get equipment_3_object_type

        Returns:
            str: the value of `equipment_3_object_type` or None if not set
        """
        return self._data["Equipment 3 Object Type"]

    @equipment_3_object_type.setter
    def equipment_3_object_type(self, value=None):
        """  Corresponds to IDD Field `Equipment 3 Object Type`

        Args:
            value (str): value for IDD Field `Equipment 3 Object Type`
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
                                 'for field `equipment_3_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_3_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `equipment_3_object_type`')
        self._data["Equipment 3 Object Type"] = value

    @property
    def equipment_3_name(self):
        """Get equipment_3_name

        Returns:
            str: the value of `equipment_3_name` or None if not set
        """
        return self._data["Equipment 3 Name"]

    @equipment_3_name.setter
    def equipment_3_name(self, value=None):
        """  Corresponds to IDD Field `Equipment 3 Name`

        Args:
            value (str): value for IDD Field `Equipment 3 Name`
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
                                 'for field `equipment_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_3_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `equipment_3_name`')
        self._data["Equipment 3 Name"] = value

    @property
    def demand_calculation_3_node_name(self):
        """Get demand_calculation_3_node_name

        Returns:
            str: the value of `demand_calculation_3_node_name` or None if not set
        """
        return self._data["Demand Calculation 3 Node Name"]

    @demand_calculation_3_node_name.setter
    def demand_calculation_3_node_name(self, value=None):
        """  Corresponds to IDD Field `Demand Calculation 3 Node Name`

        Args:
            value (str): value for IDD Field `Demand Calculation 3 Node Name`
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
                                 'for field `demand_calculation_3_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `demand_calculation_3_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `demand_calculation_3_node_name`')
        self._data["Demand Calculation 3 Node Name"] = value

    @property
    def setpoint_3_node_name(self):
        """Get setpoint_3_node_name

        Returns:
            str: the value of `setpoint_3_node_name` or None if not set
        """
        return self._data["Setpoint 3 Node Name"]

    @setpoint_3_node_name.setter
    def setpoint_3_node_name(self, value=None):
        """  Corresponds to IDD Field `Setpoint 3 Node Name`

        Args:
            value (str): value for IDD Field `Setpoint 3 Node Name`
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
                                 'for field `setpoint_3_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `setpoint_3_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `setpoint_3_node_name`')
        self._data["Setpoint 3 Node Name"] = value

    @property
    def component_3_flow_rate(self):
        """Get component_3_flow_rate

        Returns:
            float: the value of `component_3_flow_rate` or None if not set
        """
        return self._data["Component 3 Flow Rate"]

    @component_3_flow_rate.setter
    def component_3_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Component 3 Flow Rate`

        Args:
            value (float or "Autosize"): value for IDD Field `Component 3 Flow Rate`
                Units: m3/s
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Component 3 Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `component_3_flow_rate`'.format(value))
        self._data["Component 3 Flow Rate"] = value

    @property
    def operation_3_type(self):
        """Get operation_3_type

        Returns:
            str: the value of `operation_3_type` or None if not set
        """
        return self._data["Operation 3 Type"]

    @operation_3_type.setter
    def operation_3_type(self, value=None):
        """  Corresponds to IDD Field `Operation 3 Type`

        Args:
            value (str): value for IDD Field `Operation 3 Type`
                Accepted values are:
                      - Heating
                      - Cooling
                      - Dual
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
                                 'for field `operation_3_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `operation_3_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `operation_3_type`')
            vals = {}
            vals["heating"] = "Heating"
            vals["cooling"] = "Cooling"
            vals["dual"] = "Dual"
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
                                     'field `operation_3_type`'.format(value))
            value = vals[value_lower]
        self._data["Operation 3 Type"] = value

    @property
    def equipment_4_object_type(self):
        """Get equipment_4_object_type

        Returns:
            str: the value of `equipment_4_object_type` or None if not set
        """
        return self._data["Equipment 4 Object Type"]

    @equipment_4_object_type.setter
    def equipment_4_object_type(self, value=None):
        """  Corresponds to IDD Field `Equipment 4 Object Type`

        Args:
            value (str): value for IDD Field `Equipment 4 Object Type`
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
                                 'for field `equipment_4_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_4_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `equipment_4_object_type`')
        self._data["Equipment 4 Object Type"] = value

    @property
    def equipment_4_name(self):
        """Get equipment_4_name

        Returns:
            str: the value of `equipment_4_name` or None if not set
        """
        return self._data["Equipment 4 Name"]

    @equipment_4_name.setter
    def equipment_4_name(self, value=None):
        """  Corresponds to IDD Field `Equipment 4 Name`

        Args:
            value (str): value for IDD Field `Equipment 4 Name`
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
                                 'for field `equipment_4_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_4_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `equipment_4_name`')
        self._data["Equipment 4 Name"] = value

    @property
    def demand_calculation_4_node_name(self):
        """Get demand_calculation_4_node_name

        Returns:
            str: the value of `demand_calculation_4_node_name` or None if not set
        """
        return self._data["Demand Calculation 4 Node Name"]

    @demand_calculation_4_node_name.setter
    def demand_calculation_4_node_name(self, value=None):
        """  Corresponds to IDD Field `Demand Calculation 4 Node Name`

        Args:
            value (str): value for IDD Field `Demand Calculation 4 Node Name`
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
                                 'for field `demand_calculation_4_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `demand_calculation_4_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `demand_calculation_4_node_name`')
        self._data["Demand Calculation 4 Node Name"] = value

    @property
    def setpoint_4_node_name(self):
        """Get setpoint_4_node_name

        Returns:
            str: the value of `setpoint_4_node_name` or None if not set
        """
        return self._data["Setpoint 4 Node Name"]

    @setpoint_4_node_name.setter
    def setpoint_4_node_name(self, value=None):
        """  Corresponds to IDD Field `Setpoint 4 Node Name`

        Args:
            value (str): value for IDD Field `Setpoint 4 Node Name`
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
                                 'for field `setpoint_4_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `setpoint_4_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `setpoint_4_node_name`')
        self._data["Setpoint 4 Node Name"] = value

    @property
    def component_4_flow_rate(self):
        """Get component_4_flow_rate

        Returns:
            float: the value of `component_4_flow_rate` or None if not set
        """
        return self._data["Component 4 Flow Rate"]

    @component_4_flow_rate.setter
    def component_4_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Component 4 Flow Rate`

        Args:
            value (float or "Autosize"): value for IDD Field `Component 4 Flow Rate`
                Units: m3/s
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Component 4 Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `component_4_flow_rate`'.format(value))
        self._data["Component 4 Flow Rate"] = value

    @property
    def operation_4_type(self):
        """Get operation_4_type

        Returns:
            str: the value of `operation_4_type` or None if not set
        """
        return self._data["Operation 4 Type"]

    @operation_4_type.setter
    def operation_4_type(self, value=None):
        """  Corresponds to IDD Field `Operation 4 Type`

        Args:
            value (str): value for IDD Field `Operation 4 Type`
                Accepted values are:
                      - Heating
                      - Cooling
                      - Dual
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
                                 'for field `operation_4_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `operation_4_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `operation_4_type`')
            vals = {}
            vals["heating"] = "Heating"
            vals["cooling"] = "Cooling"
            vals["dual"] = "Dual"
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
                                     'field `operation_4_type`'.format(value))
            value = vals[value_lower]
        self._data["Operation 4 Type"] = value

    @property
    def equipment_5_object_type(self):
        """Get equipment_5_object_type

        Returns:
            str: the value of `equipment_5_object_type` or None if not set
        """
        return self._data["Equipment 5 Object Type"]

    @equipment_5_object_type.setter
    def equipment_5_object_type(self, value=None):
        """  Corresponds to IDD Field `Equipment 5 Object Type`

        Args:
            value (str): value for IDD Field `Equipment 5 Object Type`
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
                                 'for field `equipment_5_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_5_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `equipment_5_object_type`')
        self._data["Equipment 5 Object Type"] = value

    @property
    def equipment_5_name(self):
        """Get equipment_5_name

        Returns:
            str: the value of `equipment_5_name` or None if not set
        """
        return self._data["Equipment 5 Name"]

    @equipment_5_name.setter
    def equipment_5_name(self, value=None):
        """  Corresponds to IDD Field `Equipment 5 Name`

        Args:
            value (str): value for IDD Field `Equipment 5 Name`
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
                                 'for field `equipment_5_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_5_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `equipment_5_name`')
        self._data["Equipment 5 Name"] = value

    @property
    def demand_calculation_5_node_name(self):
        """Get demand_calculation_5_node_name

        Returns:
            str: the value of `demand_calculation_5_node_name` or None if not set
        """
        return self._data["Demand Calculation 5 Node Name"]

    @demand_calculation_5_node_name.setter
    def demand_calculation_5_node_name(self, value=None):
        """  Corresponds to IDD Field `Demand Calculation 5 Node Name`

        Args:
            value (str): value for IDD Field `Demand Calculation 5 Node Name`
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
                                 'for field `demand_calculation_5_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `demand_calculation_5_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `demand_calculation_5_node_name`')
        self._data["Demand Calculation 5 Node Name"] = value

    @property
    def setpoint_5_node_name(self):
        """Get setpoint_5_node_name

        Returns:
            str: the value of `setpoint_5_node_name` or None if not set
        """
        return self._data["Setpoint 5 Node Name"]

    @setpoint_5_node_name.setter
    def setpoint_5_node_name(self, value=None):
        """  Corresponds to IDD Field `Setpoint 5 Node Name`

        Args:
            value (str): value for IDD Field `Setpoint 5 Node Name`
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
                                 'for field `setpoint_5_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `setpoint_5_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `setpoint_5_node_name`')
        self._data["Setpoint 5 Node Name"] = value

    @property
    def component_5_flow_rate(self):
        """Get component_5_flow_rate

        Returns:
            float: the value of `component_5_flow_rate` or None if not set
        """
        return self._data["Component 5 Flow Rate"]

    @component_5_flow_rate.setter
    def component_5_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Component 5 Flow Rate`

        Args:
            value (float or "Autosize"): value for IDD Field `Component 5 Flow Rate`
                Units: m3/s
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Component 5 Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `component_5_flow_rate`'.format(value))
        self._data["Component 5 Flow Rate"] = value

    @property
    def operation_5_type(self):
        """Get operation_5_type

        Returns:
            str: the value of `operation_5_type` or None if not set
        """
        return self._data["Operation 5 Type"]

    @operation_5_type.setter
    def operation_5_type(self, value=None):
        """  Corresponds to IDD Field `Operation 5 Type`

        Args:
            value (str): value for IDD Field `Operation 5 Type`
                Accepted values are:
                      - Heating
                      - Cooling
                      - Dual
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
                                 'for field `operation_5_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `operation_5_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `operation_5_type`')
            vals = {}
            vals["heating"] = "Heating"
            vals["cooling"] = "Cooling"
            vals["dual"] = "Dual"
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
                                     'field `operation_5_type`'.format(value))
            value = vals[value_lower]
        self._data["Operation 5 Type"] = value

    @property
    def equipment_6_object_type(self):
        """Get equipment_6_object_type

        Returns:
            str: the value of `equipment_6_object_type` or None if not set
        """
        return self._data["Equipment 6 Object Type"]

    @equipment_6_object_type.setter
    def equipment_6_object_type(self, value=None):
        """  Corresponds to IDD Field `Equipment 6 Object Type`

        Args:
            value (str): value for IDD Field `Equipment 6 Object Type`
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
                                 'for field `equipment_6_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_6_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `equipment_6_object_type`')
        self._data["Equipment 6 Object Type"] = value

    @property
    def equipment_6_name(self):
        """Get equipment_6_name

        Returns:
            str: the value of `equipment_6_name` or None if not set
        """
        return self._data["Equipment 6 Name"]

    @equipment_6_name.setter
    def equipment_6_name(self, value=None):
        """  Corresponds to IDD Field `Equipment 6 Name`

        Args:
            value (str): value for IDD Field `Equipment 6 Name`
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
                                 'for field `equipment_6_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_6_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `equipment_6_name`')
        self._data["Equipment 6 Name"] = value

    @property
    def demand_calculation_6_node_name(self):
        """Get demand_calculation_6_node_name

        Returns:
            str: the value of `demand_calculation_6_node_name` or None if not set
        """
        return self._data["Demand Calculation 6 Node Name"]

    @demand_calculation_6_node_name.setter
    def demand_calculation_6_node_name(self, value=None):
        """  Corresponds to IDD Field `Demand Calculation 6 Node Name`

        Args:
            value (str): value for IDD Field `Demand Calculation 6 Node Name`
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
                                 'for field `demand_calculation_6_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `demand_calculation_6_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `demand_calculation_6_node_name`')
        self._data["Demand Calculation 6 Node Name"] = value

    @property
    def setpoint_6_node_name(self):
        """Get setpoint_6_node_name

        Returns:
            str: the value of `setpoint_6_node_name` or None if not set
        """
        return self._data["Setpoint 6 Node Name"]

    @setpoint_6_node_name.setter
    def setpoint_6_node_name(self, value=None):
        """  Corresponds to IDD Field `Setpoint 6 Node Name`

        Args:
            value (str): value for IDD Field `Setpoint 6 Node Name`
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
                                 'for field `setpoint_6_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `setpoint_6_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `setpoint_6_node_name`')
        self._data["Setpoint 6 Node Name"] = value

    @property
    def component_6_flow_rate(self):
        """Get component_6_flow_rate

        Returns:
            float: the value of `component_6_flow_rate` or None if not set
        """
        return self._data["Component 6 Flow Rate"]

    @component_6_flow_rate.setter
    def component_6_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Component 6 Flow Rate`

        Args:
            value (float or "Autosize"): value for IDD Field `Component 6 Flow Rate`
                Units: m3/s
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Component 6 Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `component_6_flow_rate`'.format(value))
        self._data["Component 6 Flow Rate"] = value

    @property
    def operation_6_type(self):
        """Get operation_6_type

        Returns:
            str: the value of `operation_6_type` or None if not set
        """
        return self._data["Operation 6 Type"]

    @operation_6_type.setter
    def operation_6_type(self, value=None):
        """  Corresponds to IDD Field `Operation 6 Type`

        Args:
            value (str): value for IDD Field `Operation 6 Type`
                Accepted values are:
                      - Heating
                      - Cooling
                      - Dual
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
                                 'for field `operation_6_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `operation_6_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `operation_6_type`')
            vals = {}
            vals["heating"] = "Heating"
            vals["cooling"] = "Cooling"
            vals["dual"] = "Dual"
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
                                     'field `operation_6_type`'.format(value))
            value = vals[value_lower]
        self._data["Operation 6 Type"] = value

    @property
    def equipment_7_object_type(self):
        """Get equipment_7_object_type

        Returns:
            str: the value of `equipment_7_object_type` or None if not set
        """
        return self._data["Equipment 7 Object Type"]

    @equipment_7_object_type.setter
    def equipment_7_object_type(self, value=None):
        """  Corresponds to IDD Field `Equipment 7 Object Type`

        Args:
            value (str): value for IDD Field `Equipment 7 Object Type`
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
                                 'for field `equipment_7_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_7_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `equipment_7_object_type`')
        self._data["Equipment 7 Object Type"] = value

    @property
    def equipment_7_name(self):
        """Get equipment_7_name

        Returns:
            str: the value of `equipment_7_name` or None if not set
        """
        return self._data["Equipment 7 Name"]

    @equipment_7_name.setter
    def equipment_7_name(self, value=None):
        """  Corresponds to IDD Field `Equipment 7 Name`

        Args:
            value (str): value for IDD Field `Equipment 7 Name`
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
                                 'for field `equipment_7_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_7_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `equipment_7_name`')
        self._data["Equipment 7 Name"] = value

    @property
    def demand_calculation_7_node_name(self):
        """Get demand_calculation_7_node_name

        Returns:
            str: the value of `demand_calculation_7_node_name` or None if not set
        """
        return self._data["Demand Calculation 7 Node Name"]

    @demand_calculation_7_node_name.setter
    def demand_calculation_7_node_name(self, value=None):
        """  Corresponds to IDD Field `Demand Calculation 7 Node Name`

        Args:
            value (str): value for IDD Field `Demand Calculation 7 Node Name`
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
                                 'for field `demand_calculation_7_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `demand_calculation_7_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `demand_calculation_7_node_name`')
        self._data["Demand Calculation 7 Node Name"] = value

    @property
    def setpoint_7_node_name(self):
        """Get setpoint_7_node_name

        Returns:
            str: the value of `setpoint_7_node_name` or None if not set
        """
        return self._data["Setpoint 7 Node Name"]

    @setpoint_7_node_name.setter
    def setpoint_7_node_name(self, value=None):
        """  Corresponds to IDD Field `Setpoint 7 Node Name`

        Args:
            value (str): value for IDD Field `Setpoint 7 Node Name`
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
                                 'for field `setpoint_7_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `setpoint_7_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `setpoint_7_node_name`')
        self._data["Setpoint 7 Node Name"] = value

    @property
    def component_7_flow_rate(self):
        """Get component_7_flow_rate

        Returns:
            float: the value of `component_7_flow_rate` or None if not set
        """
        return self._data["Component 7 Flow Rate"]

    @component_7_flow_rate.setter
    def component_7_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Component 7 Flow Rate`

        Args:
            value (float or "Autosize"): value for IDD Field `Component 7 Flow Rate`
                Units: m3/s
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Component 7 Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `component_7_flow_rate`'.format(value))
        self._data["Component 7 Flow Rate"] = value

    @property
    def operation_7_type(self):
        """Get operation_7_type

        Returns:
            str: the value of `operation_7_type` or None if not set
        """
        return self._data["Operation 7 Type"]

    @operation_7_type.setter
    def operation_7_type(self, value=None):
        """  Corresponds to IDD Field `Operation 7 Type`

        Args:
            value (str): value for IDD Field `Operation 7 Type`
                Accepted values are:
                      - Heating
                      - Cooling
                      - Dual
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
                                 'for field `operation_7_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `operation_7_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `operation_7_type`')
            vals = {}
            vals["heating"] = "Heating"
            vals["cooling"] = "Cooling"
            vals["dual"] = "Dual"
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
                                     'field `operation_7_type`'.format(value))
            value = vals[value_lower]
        self._data["Operation 7 Type"] = value

    @property
    def equipment_8_object_type(self):
        """Get equipment_8_object_type

        Returns:
            str: the value of `equipment_8_object_type` or None if not set
        """
        return self._data["Equipment 8 Object Type"]

    @equipment_8_object_type.setter
    def equipment_8_object_type(self, value=None):
        """  Corresponds to IDD Field `Equipment 8 Object Type`

        Args:
            value (str): value for IDD Field `Equipment 8 Object Type`
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
                                 'for field `equipment_8_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_8_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `equipment_8_object_type`')
        self._data["Equipment 8 Object Type"] = value

    @property
    def equipment_8_name(self):
        """Get equipment_8_name

        Returns:
            str: the value of `equipment_8_name` or None if not set
        """
        return self._data["Equipment 8 Name"]

    @equipment_8_name.setter
    def equipment_8_name(self, value=None):
        """  Corresponds to IDD Field `Equipment 8 Name`

        Args:
            value (str): value for IDD Field `Equipment 8 Name`
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
                                 'for field `equipment_8_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_8_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `equipment_8_name`')
        self._data["Equipment 8 Name"] = value

    @property
    def demand_calculation_8_node_name(self):
        """Get demand_calculation_8_node_name

        Returns:
            str: the value of `demand_calculation_8_node_name` or None if not set
        """
        return self._data["Demand Calculation 8 Node Name"]

    @demand_calculation_8_node_name.setter
    def demand_calculation_8_node_name(self, value=None):
        """  Corresponds to IDD Field `Demand Calculation 8 Node Name`

        Args:
            value (str): value for IDD Field `Demand Calculation 8 Node Name`
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
                                 'for field `demand_calculation_8_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `demand_calculation_8_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `demand_calculation_8_node_name`')
        self._data["Demand Calculation 8 Node Name"] = value

    @property
    def setpoint_8_node_name(self):
        """Get setpoint_8_node_name

        Returns:
            str: the value of `setpoint_8_node_name` or None if not set
        """
        return self._data["Setpoint 8 Node Name"]

    @setpoint_8_node_name.setter
    def setpoint_8_node_name(self, value=None):
        """  Corresponds to IDD Field `Setpoint 8 Node Name`

        Args:
            value (str): value for IDD Field `Setpoint 8 Node Name`
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
                                 'for field `setpoint_8_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `setpoint_8_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `setpoint_8_node_name`')
        self._data["Setpoint 8 Node Name"] = value

    @property
    def component_8_flow_rate(self):
        """Get component_8_flow_rate

        Returns:
            float: the value of `component_8_flow_rate` or None if not set
        """
        return self._data["Component 8 Flow Rate"]

    @component_8_flow_rate.setter
    def component_8_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Component 8 Flow Rate`

        Args:
            value (float or "Autosize"): value for IDD Field `Component 8 Flow Rate`
                Units: m3/s
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Component 8 Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `component_8_flow_rate`'.format(value))
        self._data["Component 8 Flow Rate"] = value

    @property
    def operation_8_type(self):
        """Get operation_8_type

        Returns:
            str: the value of `operation_8_type` or None if not set
        """
        return self._data["Operation 8 Type"]

    @operation_8_type.setter
    def operation_8_type(self, value=None):
        """  Corresponds to IDD Field `Operation 8 Type`

        Args:
            value (str): value for IDD Field `Operation 8 Type`
                Accepted values are:
                      - Heating
                      - Cooling
                      - Dual
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
                                 'for field `operation_8_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `operation_8_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `operation_8_type`')
            vals = {}
            vals["heating"] = "Heating"
            vals["cooling"] = "Cooling"
            vals["dual"] = "Dual"
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
                                     'field `operation_8_type`'.format(value))
            value = vals[value_lower]
        self._data["Operation 8 Type"] = value

    @property
    def equipment_9_object_type(self):
        """Get equipment_9_object_type

        Returns:
            str: the value of `equipment_9_object_type` or None if not set
        """
        return self._data["Equipment 9 Object Type"]

    @equipment_9_object_type.setter
    def equipment_9_object_type(self, value=None):
        """  Corresponds to IDD Field `Equipment 9 Object Type`

        Args:
            value (str): value for IDD Field `Equipment 9 Object Type`
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
                                 'for field `equipment_9_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_9_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `equipment_9_object_type`')
        self._data["Equipment 9 Object Type"] = value

    @property
    def equipment_9_name(self):
        """Get equipment_9_name

        Returns:
            str: the value of `equipment_9_name` or None if not set
        """
        return self._data["Equipment 9 Name"]

    @equipment_9_name.setter
    def equipment_9_name(self, value=None):
        """  Corresponds to IDD Field `Equipment 9 Name`

        Args:
            value (str): value for IDD Field `Equipment 9 Name`
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
                                 'for field `equipment_9_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_9_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `equipment_9_name`')
        self._data["Equipment 9 Name"] = value

    @property
    def demand_calculation_9_node_name(self):
        """Get demand_calculation_9_node_name

        Returns:
            str: the value of `demand_calculation_9_node_name` or None if not set
        """
        return self._data["Demand Calculation 9 Node Name"]

    @demand_calculation_9_node_name.setter
    def demand_calculation_9_node_name(self, value=None):
        """  Corresponds to IDD Field `Demand Calculation 9 Node Name`

        Args:
            value (str): value for IDD Field `Demand Calculation 9 Node Name`
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
                                 'for field `demand_calculation_9_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `demand_calculation_9_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `demand_calculation_9_node_name`')
        self._data["Demand Calculation 9 Node Name"] = value

    @property
    def setpoint_9_node_name(self):
        """Get setpoint_9_node_name

        Returns:
            str: the value of `setpoint_9_node_name` or None if not set
        """
        return self._data["Setpoint 9 Node Name"]

    @setpoint_9_node_name.setter
    def setpoint_9_node_name(self, value=None):
        """  Corresponds to IDD Field `Setpoint 9 Node Name`

        Args:
            value (str): value for IDD Field `Setpoint 9 Node Name`
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
                                 'for field `setpoint_9_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `setpoint_9_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `setpoint_9_node_name`')
        self._data["Setpoint 9 Node Name"] = value

    @property
    def component_9_flow_rate(self):
        """Get component_9_flow_rate

        Returns:
            float: the value of `component_9_flow_rate` or None if not set
        """
        return self._data["Component 9 Flow Rate"]

    @component_9_flow_rate.setter
    def component_9_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Component 9 Flow Rate`

        Args:
            value (float or "Autosize"): value for IDD Field `Component 9 Flow Rate`
                Units: m3/s
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Component 9 Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `component_9_flow_rate`'.format(value))
        self._data["Component 9 Flow Rate"] = value

    @property
    def operation_9_type(self):
        """Get operation_9_type

        Returns:
            str: the value of `operation_9_type` or None if not set
        """
        return self._data["Operation 9 Type"]

    @operation_9_type.setter
    def operation_9_type(self, value=None):
        """  Corresponds to IDD Field `Operation 9 Type`

        Args:
            value (str): value for IDD Field `Operation 9 Type`
                Accepted values are:
                      - Heating
                      - Cooling
                      - Dual
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
                                 'for field `operation_9_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `operation_9_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `operation_9_type`')
            vals = {}
            vals["heating"] = "Heating"
            vals["cooling"] = "Cooling"
            vals["dual"] = "Dual"
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
                                     'field `operation_9_type`'.format(value))
            value = vals[value_lower]
        self._data["Operation 9 Type"] = value

    @property
    def equipment_10_object_type(self):
        """Get equipment_10_object_type

        Returns:
            str: the value of `equipment_10_object_type` or None if not set
        """
        return self._data["Equipment 10 Object Type"]

    @equipment_10_object_type.setter
    def equipment_10_object_type(self, value=None):
        """  Corresponds to IDD Field `Equipment 10 Object Type`

        Args:
            value (str): value for IDD Field `Equipment 10 Object Type`
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
                                 'for field `equipment_10_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_10_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `equipment_10_object_type`')
        self._data["Equipment 10 Object Type"] = value

    @property
    def equipment_10_name(self):
        """Get equipment_10_name

        Returns:
            str: the value of `equipment_10_name` or None if not set
        """
        return self._data["Equipment 10 Name"]

    @equipment_10_name.setter
    def equipment_10_name(self, value=None):
        """  Corresponds to IDD Field `Equipment 10 Name`

        Args:
            value (str): value for IDD Field `Equipment 10 Name`
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
                                 'for field `equipment_10_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_10_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `equipment_10_name`')
        self._data["Equipment 10 Name"] = value

    @property
    def demand_calculation_10_node_name(self):
        """Get demand_calculation_10_node_name

        Returns:
            str: the value of `demand_calculation_10_node_name` or None if not set
        """
        return self._data["Demand Calculation 10 Node Name"]

    @demand_calculation_10_node_name.setter
    def demand_calculation_10_node_name(self, value=None):
        """  Corresponds to IDD Field `Demand Calculation 10 Node Name`

        Args:
            value (str): value for IDD Field `Demand Calculation 10 Node Name`
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
                                 'for field `demand_calculation_10_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `demand_calculation_10_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `demand_calculation_10_node_name`')
        self._data["Demand Calculation 10 Node Name"] = value

    @property
    def setpoint_10_node_name(self):
        """Get setpoint_10_node_name

        Returns:
            str: the value of `setpoint_10_node_name` or None if not set
        """
        return self._data["Setpoint 10 Node Name"]

    @setpoint_10_node_name.setter
    def setpoint_10_node_name(self, value=None):
        """  Corresponds to IDD Field `Setpoint 10 Node Name`

        Args:
            value (str): value for IDD Field `Setpoint 10 Node Name`
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
                                 'for field `setpoint_10_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `setpoint_10_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `setpoint_10_node_name`')
        self._data["Setpoint 10 Node Name"] = value

    @property
    def component_10_flow_rate(self):
        """Get component_10_flow_rate

        Returns:
            float: the value of `component_10_flow_rate` or None if not set
        """
        return self._data["Component 10 Flow Rate"]

    @component_10_flow_rate.setter
    def component_10_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Component 10 Flow Rate`

        Args:
            value (float or "Autosize"): value for IDD Field `Component 10 Flow Rate`
                Units: m3/s
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Component 10 Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `component_10_flow_rate`'.format(value))
        self._data["Component 10 Flow Rate"] = value

    @property
    def operation_10_type(self):
        """Get operation_10_type

        Returns:
            str: the value of `operation_10_type` or None if not set
        """
        return self._data["Operation 10 Type"]

    @operation_10_type.setter
    def operation_10_type(self, value=None):
        """  Corresponds to IDD Field `Operation 10 Type`

        Args:
            value (str): value for IDD Field `Operation 10 Type`
                Accepted values are:
                      - Heating
                      - Cooling
                      - Dual
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
                                 'for field `operation_10_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `operation_10_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `operation_10_type`')
            vals = {}
            vals["heating"] = "Heating"
            vals["cooling"] = "Cooling"
            vals["dual"] = "Dual"
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
                                     'field `operation_10_type`'.format(value))
            value = vals[value_lower]
        self._data["Operation 10 Type"] = value

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

class PlantEquipmentOperationOutdoorDryBulbDifference(object):
    """ Corresponds to IDD object `PlantEquipmentOperation:OutdoorDryBulbDifference`
        Plant equipment operation scheme for outdoor dry-bulb temperature difference
        operation. Specifies one or more groups of equipment which are available to operate
        for successive ranges based the difference between a reference node temperature and
        the outdoor dry-bulb temperature.
    
    """
    internal_name = "PlantEquipmentOperation:OutdoorDryBulbDifference"
    field_count = 32
    required_fields = ["Name", "Reference Temperature Node Name", "Dry-Bulb Temperature Difference Range 1 Lower Limit", "Dry-Bulb Temperature Difference Range 1 Upper Limit", "Range 1 Equipment List Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `PlantEquipmentOperation:OutdoorDryBulbDifference`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Reference Temperature Node Name"] = None
        self._data["Dry-Bulb Temperature Difference Range 1 Lower Limit"] = None
        self._data["Dry-Bulb Temperature Difference Range 1 Upper Limit"] = None
        self._data["Range 1 Equipment List Name"] = None
        self._data["Dry-Bulb Temperature Difference Range 2 Lower Limit"] = None
        self._data["Dry-Bulb Temperature Difference Range 2 Upper Limit"] = None
        self._data["Range 2 Equipment List Name"] = None
        self._data["Dry-Bulb Temperature Difference Range 3 Lower Limit"] = None
        self._data["Dry-Bulb Temperature Difference Range 3 Upper Limit"] = None
        self._data["Range 3 Equipment List Name"] = None
        self._data["Dry-Bulb Temperature Difference Range 4 Lower Limit"] = None
        self._data["Dry-Bulb Temperature Difference Range 4 Upper Limit"] = None
        self._data["Range 4 Equipment List Name"] = None
        self._data["Dry-Bulb Temperature Difference Range 5 Lower Limit"] = None
        self._data["Dry-Bulb Temperature Difference Range 5 Upper Limit"] = None
        self._data["Range 5 Equipment List Name"] = None
        self._data["Dry-Bulb Temperature Difference Range 6 Lower Limit"] = None
        self._data["Dry-Bulb Temperature Difference Range 6 Upper Limit"] = None
        self._data["Range 6 Equipment List Name"] = None
        self._data["Dry-Bulb Temperature Difference Range 7 Lower Limit"] = None
        self._data["Dry-Bulb Temperature Difference Range 7 Upper Limit"] = None
        self._data["Range 7 Equipment List Name"] = None
        self._data["Dry-Bulb Temperature Difference Range 8 Lower Limit"] = None
        self._data["Dry-Bulb Temperature Difference Range 8 Upper Limit"] = None
        self._data["Range 8 Equipment List Name"] = None
        self._data["Dry-Bulb Temperature Difference Range 9 Lower Limit"] = None
        self._data["Dry-Bulb Temperature Difference Range 9 Upper Limit"] = None
        self._data["Range 9 Equipment List Name"] = None
        self._data["Dry-Bulb Temperature Difference Range 10 Lower Limit"] = None
        self._data["Dry-Bulb Temperature Difference Range 10 Upper Limit"] = None
        self._data["Range 10 Equipment List Name"] = None
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
            self.reference_temperature_node_name = None
        else:
            self.reference_temperature_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.drybulb_temperature_difference_range_1_lower_limit = None
        else:
            self.drybulb_temperature_difference_range_1_lower_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.drybulb_temperature_difference_range_1_upper_limit = None
        else:
            self.drybulb_temperature_difference_range_1_upper_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.range_1_equipment_list_name = None
        else:
            self.range_1_equipment_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.drybulb_temperature_difference_range_2_lower_limit = None
        else:
            self.drybulb_temperature_difference_range_2_lower_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.drybulb_temperature_difference_range_2_upper_limit = None
        else:
            self.drybulb_temperature_difference_range_2_upper_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.range_2_equipment_list_name = None
        else:
            self.range_2_equipment_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.drybulb_temperature_difference_range_3_lower_limit = None
        else:
            self.drybulb_temperature_difference_range_3_lower_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.drybulb_temperature_difference_range_3_upper_limit = None
        else:
            self.drybulb_temperature_difference_range_3_upper_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.range_3_equipment_list_name = None
        else:
            self.range_3_equipment_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.drybulb_temperature_difference_range_4_lower_limit = None
        else:
            self.drybulb_temperature_difference_range_4_lower_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.drybulb_temperature_difference_range_4_upper_limit = None
        else:
            self.drybulb_temperature_difference_range_4_upper_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.range_4_equipment_list_name = None
        else:
            self.range_4_equipment_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.drybulb_temperature_difference_range_5_lower_limit = None
        else:
            self.drybulb_temperature_difference_range_5_lower_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.drybulb_temperature_difference_range_5_upper_limit = None
        else:
            self.drybulb_temperature_difference_range_5_upper_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.range_5_equipment_list_name = None
        else:
            self.range_5_equipment_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.drybulb_temperature_difference_range_6_lower_limit = None
        else:
            self.drybulb_temperature_difference_range_6_lower_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.drybulb_temperature_difference_range_6_upper_limit = None
        else:
            self.drybulb_temperature_difference_range_6_upper_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.range_6_equipment_list_name = None
        else:
            self.range_6_equipment_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.drybulb_temperature_difference_range_7_lower_limit = None
        else:
            self.drybulb_temperature_difference_range_7_lower_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.drybulb_temperature_difference_range_7_upper_limit = None
        else:
            self.drybulb_temperature_difference_range_7_upper_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.range_7_equipment_list_name = None
        else:
            self.range_7_equipment_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.drybulb_temperature_difference_range_8_lower_limit = None
        else:
            self.drybulb_temperature_difference_range_8_lower_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.drybulb_temperature_difference_range_8_upper_limit = None
        else:
            self.drybulb_temperature_difference_range_8_upper_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.range_8_equipment_list_name = None
        else:
            self.range_8_equipment_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.drybulb_temperature_difference_range_9_lower_limit = None
        else:
            self.drybulb_temperature_difference_range_9_lower_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.drybulb_temperature_difference_range_9_upper_limit = None
        else:
            self.drybulb_temperature_difference_range_9_upper_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.range_9_equipment_list_name = None
        else:
            self.range_9_equipment_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.drybulb_temperature_difference_range_10_lower_limit = None
        else:
            self.drybulb_temperature_difference_range_10_lower_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.drybulb_temperature_difference_range_10_upper_limit = None
        else:
            self.drybulb_temperature_difference_range_10_upper_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.range_10_equipment_list_name = None
        else:
            self.range_10_equipment_list_name = vals[i]
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
    def reference_temperature_node_name(self):
        """Get reference_temperature_node_name

        Returns:
            str: the value of `reference_temperature_node_name` or None if not set
        """
        return self._data["Reference Temperature Node Name"]

    @reference_temperature_node_name.setter
    def reference_temperature_node_name(self, value=None):
        """  Corresponds to IDD Field `Reference Temperature Node Name`

        Args:
            value (str): value for IDD Field `Reference Temperature Node Name`
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
                                 'for field `reference_temperature_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `reference_temperature_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `reference_temperature_node_name`')
        self._data["Reference Temperature Node Name"] = value

    @property
    def drybulb_temperature_difference_range_1_lower_limit(self):
        """Get drybulb_temperature_difference_range_1_lower_limit

        Returns:
            float: the value of `drybulb_temperature_difference_range_1_lower_limit` or None if not set
        """
        return self._data["Dry-Bulb Temperature Difference Range 1 Lower Limit"]

    @drybulb_temperature_difference_range_1_lower_limit.setter
    def drybulb_temperature_difference_range_1_lower_limit(self, value=None):
        """  Corresponds to IDD Field `Dry-Bulb Temperature Difference Range 1 Lower Limit`

        Args:
            value (float): value for IDD Field `Dry-Bulb Temperature Difference Range 1 Lower Limit`
                Units: deltaC
                value >= -50.0
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
                                 'for field `drybulb_temperature_difference_range_1_lower_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `drybulb_temperature_difference_range_1_lower_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `drybulb_temperature_difference_range_1_lower_limit`')
        self._data["Dry-Bulb Temperature Difference Range 1 Lower Limit"] = value

    @property
    def drybulb_temperature_difference_range_1_upper_limit(self):
        """Get drybulb_temperature_difference_range_1_upper_limit

        Returns:
            float: the value of `drybulb_temperature_difference_range_1_upper_limit` or None if not set
        """
        return self._data["Dry-Bulb Temperature Difference Range 1 Upper Limit"]

    @drybulb_temperature_difference_range_1_upper_limit.setter
    def drybulb_temperature_difference_range_1_upper_limit(self, value=None):
        """  Corresponds to IDD Field `Dry-Bulb Temperature Difference Range 1 Upper Limit`

        Args:
            value (float): value for IDD Field `Dry-Bulb Temperature Difference Range 1 Upper Limit`
                Units: deltaC
                value >= -50.0
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
                                 'for field `drybulb_temperature_difference_range_1_upper_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `drybulb_temperature_difference_range_1_upper_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `drybulb_temperature_difference_range_1_upper_limit`')
        self._data["Dry-Bulb Temperature Difference Range 1 Upper Limit"] = value

    @property
    def range_1_equipment_list_name(self):
        """Get range_1_equipment_list_name

        Returns:
            str: the value of `range_1_equipment_list_name` or None if not set
        """
        return self._data["Range 1 Equipment List Name"]

    @range_1_equipment_list_name.setter
    def range_1_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `Range 1 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 1 Equipment List Name`
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
                                 'for field `range_1_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_1_equipment_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `range_1_equipment_list_name`')
        self._data["Range 1 Equipment List Name"] = value

    @property
    def drybulb_temperature_difference_range_2_lower_limit(self):
        """Get drybulb_temperature_difference_range_2_lower_limit

        Returns:
            float: the value of `drybulb_temperature_difference_range_2_lower_limit` or None if not set
        """
        return self._data["Dry-Bulb Temperature Difference Range 2 Lower Limit"]

    @drybulb_temperature_difference_range_2_lower_limit.setter
    def drybulb_temperature_difference_range_2_lower_limit(self, value=None):
        """  Corresponds to IDD Field `Dry-Bulb Temperature Difference Range 2 Lower Limit`

        Args:
            value (float): value for IDD Field `Dry-Bulb Temperature Difference Range 2 Lower Limit`
                Units: deltaC
                value >= -50.0
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
                                 'for field `drybulb_temperature_difference_range_2_lower_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `drybulb_temperature_difference_range_2_lower_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `drybulb_temperature_difference_range_2_lower_limit`')
        self._data["Dry-Bulb Temperature Difference Range 2 Lower Limit"] = value

    @property
    def drybulb_temperature_difference_range_2_upper_limit(self):
        """Get drybulb_temperature_difference_range_2_upper_limit

        Returns:
            float: the value of `drybulb_temperature_difference_range_2_upper_limit` or None if not set
        """
        return self._data["Dry-Bulb Temperature Difference Range 2 Upper Limit"]

    @drybulb_temperature_difference_range_2_upper_limit.setter
    def drybulb_temperature_difference_range_2_upper_limit(self, value=None):
        """  Corresponds to IDD Field `Dry-Bulb Temperature Difference Range 2 Upper Limit`

        Args:
            value (float): value for IDD Field `Dry-Bulb Temperature Difference Range 2 Upper Limit`
                Units: deltaC
                value >= -50.0
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
                                 'for field `drybulb_temperature_difference_range_2_upper_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `drybulb_temperature_difference_range_2_upper_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `drybulb_temperature_difference_range_2_upper_limit`')
        self._data["Dry-Bulb Temperature Difference Range 2 Upper Limit"] = value

    @property
    def range_2_equipment_list_name(self):
        """Get range_2_equipment_list_name

        Returns:
            str: the value of `range_2_equipment_list_name` or None if not set
        """
        return self._data["Range 2 Equipment List Name"]

    @range_2_equipment_list_name.setter
    def range_2_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `Range 2 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 2 Equipment List Name`
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
                                 'for field `range_2_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_2_equipment_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `range_2_equipment_list_name`')
        self._data["Range 2 Equipment List Name"] = value

    @property
    def drybulb_temperature_difference_range_3_lower_limit(self):
        """Get drybulb_temperature_difference_range_3_lower_limit

        Returns:
            float: the value of `drybulb_temperature_difference_range_3_lower_limit` or None if not set
        """
        return self._data["Dry-Bulb Temperature Difference Range 3 Lower Limit"]

    @drybulb_temperature_difference_range_3_lower_limit.setter
    def drybulb_temperature_difference_range_3_lower_limit(self, value=None):
        """  Corresponds to IDD Field `Dry-Bulb Temperature Difference Range 3 Lower Limit`

        Args:
            value (float): value for IDD Field `Dry-Bulb Temperature Difference Range 3 Lower Limit`
                Units: deltaC
                value >= -50.0
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
                                 'for field `drybulb_temperature_difference_range_3_lower_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `drybulb_temperature_difference_range_3_lower_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `drybulb_temperature_difference_range_3_lower_limit`')
        self._data["Dry-Bulb Temperature Difference Range 3 Lower Limit"] = value

    @property
    def drybulb_temperature_difference_range_3_upper_limit(self):
        """Get drybulb_temperature_difference_range_3_upper_limit

        Returns:
            float: the value of `drybulb_temperature_difference_range_3_upper_limit` or None if not set
        """
        return self._data["Dry-Bulb Temperature Difference Range 3 Upper Limit"]

    @drybulb_temperature_difference_range_3_upper_limit.setter
    def drybulb_temperature_difference_range_3_upper_limit(self, value=None):
        """  Corresponds to IDD Field `Dry-Bulb Temperature Difference Range 3 Upper Limit`

        Args:
            value (float): value for IDD Field `Dry-Bulb Temperature Difference Range 3 Upper Limit`
                Units: deltaC
                value >= -50.0
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
                                 'for field `drybulb_temperature_difference_range_3_upper_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `drybulb_temperature_difference_range_3_upper_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `drybulb_temperature_difference_range_3_upper_limit`')
        self._data["Dry-Bulb Temperature Difference Range 3 Upper Limit"] = value

    @property
    def range_3_equipment_list_name(self):
        """Get range_3_equipment_list_name

        Returns:
            str: the value of `range_3_equipment_list_name` or None if not set
        """
        return self._data["Range 3 Equipment List Name"]

    @range_3_equipment_list_name.setter
    def range_3_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `Range 3 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 3 Equipment List Name`
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
                                 'for field `range_3_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_3_equipment_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `range_3_equipment_list_name`')
        self._data["Range 3 Equipment List Name"] = value

    @property
    def drybulb_temperature_difference_range_4_lower_limit(self):
        """Get drybulb_temperature_difference_range_4_lower_limit

        Returns:
            float: the value of `drybulb_temperature_difference_range_4_lower_limit` or None if not set
        """
        return self._data["Dry-Bulb Temperature Difference Range 4 Lower Limit"]

    @drybulb_temperature_difference_range_4_lower_limit.setter
    def drybulb_temperature_difference_range_4_lower_limit(self, value=None):
        """  Corresponds to IDD Field `Dry-Bulb Temperature Difference Range 4 Lower Limit`

        Args:
            value (float): value for IDD Field `Dry-Bulb Temperature Difference Range 4 Lower Limit`
                Units: deltaC
                value >= -50.0
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
                                 'for field `drybulb_temperature_difference_range_4_lower_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `drybulb_temperature_difference_range_4_lower_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `drybulb_temperature_difference_range_4_lower_limit`')
        self._data["Dry-Bulb Temperature Difference Range 4 Lower Limit"] = value

    @property
    def drybulb_temperature_difference_range_4_upper_limit(self):
        """Get drybulb_temperature_difference_range_4_upper_limit

        Returns:
            float: the value of `drybulb_temperature_difference_range_4_upper_limit` or None if not set
        """
        return self._data["Dry-Bulb Temperature Difference Range 4 Upper Limit"]

    @drybulb_temperature_difference_range_4_upper_limit.setter
    def drybulb_temperature_difference_range_4_upper_limit(self, value=None):
        """  Corresponds to IDD Field `Dry-Bulb Temperature Difference Range 4 Upper Limit`

        Args:
            value (float): value for IDD Field `Dry-Bulb Temperature Difference Range 4 Upper Limit`
                Units: deltaC
                value >= -50.0
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
                                 'for field `drybulb_temperature_difference_range_4_upper_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `drybulb_temperature_difference_range_4_upper_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `drybulb_temperature_difference_range_4_upper_limit`')
        self._data["Dry-Bulb Temperature Difference Range 4 Upper Limit"] = value

    @property
    def range_4_equipment_list_name(self):
        """Get range_4_equipment_list_name

        Returns:
            str: the value of `range_4_equipment_list_name` or None if not set
        """
        return self._data["Range 4 Equipment List Name"]

    @range_4_equipment_list_name.setter
    def range_4_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `Range 4 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 4 Equipment List Name`
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
                                 'for field `range_4_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_4_equipment_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `range_4_equipment_list_name`')
        self._data["Range 4 Equipment List Name"] = value

    @property
    def drybulb_temperature_difference_range_5_lower_limit(self):
        """Get drybulb_temperature_difference_range_5_lower_limit

        Returns:
            float: the value of `drybulb_temperature_difference_range_5_lower_limit` or None if not set
        """
        return self._data["Dry-Bulb Temperature Difference Range 5 Lower Limit"]

    @drybulb_temperature_difference_range_5_lower_limit.setter
    def drybulb_temperature_difference_range_5_lower_limit(self, value=None):
        """  Corresponds to IDD Field `Dry-Bulb Temperature Difference Range 5 Lower Limit`

        Args:
            value (float): value for IDD Field `Dry-Bulb Temperature Difference Range 5 Lower Limit`
                Units: deltaC
                value >= -50.0
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
                                 'for field `drybulb_temperature_difference_range_5_lower_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `drybulb_temperature_difference_range_5_lower_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `drybulb_temperature_difference_range_5_lower_limit`')
        self._data["Dry-Bulb Temperature Difference Range 5 Lower Limit"] = value

    @property
    def drybulb_temperature_difference_range_5_upper_limit(self):
        """Get drybulb_temperature_difference_range_5_upper_limit

        Returns:
            float: the value of `drybulb_temperature_difference_range_5_upper_limit` or None if not set
        """
        return self._data["Dry-Bulb Temperature Difference Range 5 Upper Limit"]

    @drybulb_temperature_difference_range_5_upper_limit.setter
    def drybulb_temperature_difference_range_5_upper_limit(self, value=None):
        """  Corresponds to IDD Field `Dry-Bulb Temperature Difference Range 5 Upper Limit`

        Args:
            value (float): value for IDD Field `Dry-Bulb Temperature Difference Range 5 Upper Limit`
                Units: deltaC
                value >= -50.0
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
                                 'for field `drybulb_temperature_difference_range_5_upper_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `drybulb_temperature_difference_range_5_upper_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `drybulb_temperature_difference_range_5_upper_limit`')
        self._data["Dry-Bulb Temperature Difference Range 5 Upper Limit"] = value

    @property
    def range_5_equipment_list_name(self):
        """Get range_5_equipment_list_name

        Returns:
            str: the value of `range_5_equipment_list_name` or None if not set
        """
        return self._data["Range 5 Equipment List Name"]

    @range_5_equipment_list_name.setter
    def range_5_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `Range 5 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 5 Equipment List Name`
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
                                 'for field `range_5_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_5_equipment_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `range_5_equipment_list_name`')
        self._data["Range 5 Equipment List Name"] = value

    @property
    def drybulb_temperature_difference_range_6_lower_limit(self):
        """Get drybulb_temperature_difference_range_6_lower_limit

        Returns:
            float: the value of `drybulb_temperature_difference_range_6_lower_limit` or None if not set
        """
        return self._data["Dry-Bulb Temperature Difference Range 6 Lower Limit"]

    @drybulb_temperature_difference_range_6_lower_limit.setter
    def drybulb_temperature_difference_range_6_lower_limit(self, value=None):
        """  Corresponds to IDD Field `Dry-Bulb Temperature Difference Range 6 Lower Limit`

        Args:
            value (float): value for IDD Field `Dry-Bulb Temperature Difference Range 6 Lower Limit`
                Units: deltaC
                value >= -50.0
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
                                 'for field `drybulb_temperature_difference_range_6_lower_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `drybulb_temperature_difference_range_6_lower_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `drybulb_temperature_difference_range_6_lower_limit`')
        self._data["Dry-Bulb Temperature Difference Range 6 Lower Limit"] = value

    @property
    def drybulb_temperature_difference_range_6_upper_limit(self):
        """Get drybulb_temperature_difference_range_6_upper_limit

        Returns:
            float: the value of `drybulb_temperature_difference_range_6_upper_limit` or None if not set
        """
        return self._data["Dry-Bulb Temperature Difference Range 6 Upper Limit"]

    @drybulb_temperature_difference_range_6_upper_limit.setter
    def drybulb_temperature_difference_range_6_upper_limit(self, value=None):
        """  Corresponds to IDD Field `Dry-Bulb Temperature Difference Range 6 Upper Limit`

        Args:
            value (float): value for IDD Field `Dry-Bulb Temperature Difference Range 6 Upper Limit`
                Units: deltaC
                value >= -50.0
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
                                 'for field `drybulb_temperature_difference_range_6_upper_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `drybulb_temperature_difference_range_6_upper_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `drybulb_temperature_difference_range_6_upper_limit`')
        self._data["Dry-Bulb Temperature Difference Range 6 Upper Limit"] = value

    @property
    def range_6_equipment_list_name(self):
        """Get range_6_equipment_list_name

        Returns:
            str: the value of `range_6_equipment_list_name` or None if not set
        """
        return self._data["Range 6 Equipment List Name"]

    @range_6_equipment_list_name.setter
    def range_6_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `Range 6 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 6 Equipment List Name`
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
                                 'for field `range_6_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_6_equipment_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `range_6_equipment_list_name`')
        self._data["Range 6 Equipment List Name"] = value

    @property
    def drybulb_temperature_difference_range_7_lower_limit(self):
        """Get drybulb_temperature_difference_range_7_lower_limit

        Returns:
            float: the value of `drybulb_temperature_difference_range_7_lower_limit` or None if not set
        """
        return self._data["Dry-Bulb Temperature Difference Range 7 Lower Limit"]

    @drybulb_temperature_difference_range_7_lower_limit.setter
    def drybulb_temperature_difference_range_7_lower_limit(self, value=None):
        """  Corresponds to IDD Field `Dry-Bulb Temperature Difference Range 7 Lower Limit`

        Args:
            value (float): value for IDD Field `Dry-Bulb Temperature Difference Range 7 Lower Limit`
                Units: deltaC
                value >= -50.0
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
                                 'for field `drybulb_temperature_difference_range_7_lower_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `drybulb_temperature_difference_range_7_lower_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `drybulb_temperature_difference_range_7_lower_limit`')
        self._data["Dry-Bulb Temperature Difference Range 7 Lower Limit"] = value

    @property
    def drybulb_temperature_difference_range_7_upper_limit(self):
        """Get drybulb_temperature_difference_range_7_upper_limit

        Returns:
            float: the value of `drybulb_temperature_difference_range_7_upper_limit` or None if not set
        """
        return self._data["Dry-Bulb Temperature Difference Range 7 Upper Limit"]

    @drybulb_temperature_difference_range_7_upper_limit.setter
    def drybulb_temperature_difference_range_7_upper_limit(self, value=None):
        """  Corresponds to IDD Field `Dry-Bulb Temperature Difference Range 7 Upper Limit`

        Args:
            value (float): value for IDD Field `Dry-Bulb Temperature Difference Range 7 Upper Limit`
                Units: deltaC
                value >= -50.0
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
                                 'for field `drybulb_temperature_difference_range_7_upper_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `drybulb_temperature_difference_range_7_upper_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `drybulb_temperature_difference_range_7_upper_limit`')
        self._data["Dry-Bulb Temperature Difference Range 7 Upper Limit"] = value

    @property
    def range_7_equipment_list_name(self):
        """Get range_7_equipment_list_name

        Returns:
            str: the value of `range_7_equipment_list_name` or None if not set
        """
        return self._data["Range 7 Equipment List Name"]

    @range_7_equipment_list_name.setter
    def range_7_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `Range 7 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 7 Equipment List Name`
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
                                 'for field `range_7_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_7_equipment_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `range_7_equipment_list_name`')
        self._data["Range 7 Equipment List Name"] = value

    @property
    def drybulb_temperature_difference_range_8_lower_limit(self):
        """Get drybulb_temperature_difference_range_8_lower_limit

        Returns:
            float: the value of `drybulb_temperature_difference_range_8_lower_limit` or None if not set
        """
        return self._data["Dry-Bulb Temperature Difference Range 8 Lower Limit"]

    @drybulb_temperature_difference_range_8_lower_limit.setter
    def drybulb_temperature_difference_range_8_lower_limit(self, value=None):
        """  Corresponds to IDD Field `Dry-Bulb Temperature Difference Range 8 Lower Limit`

        Args:
            value (float): value for IDD Field `Dry-Bulb Temperature Difference Range 8 Lower Limit`
                Units: deltaC
                value >= -50.0
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
                                 'for field `drybulb_temperature_difference_range_8_lower_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `drybulb_temperature_difference_range_8_lower_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `drybulb_temperature_difference_range_8_lower_limit`')
        self._data["Dry-Bulb Temperature Difference Range 8 Lower Limit"] = value

    @property
    def drybulb_temperature_difference_range_8_upper_limit(self):
        """Get drybulb_temperature_difference_range_8_upper_limit

        Returns:
            float: the value of `drybulb_temperature_difference_range_8_upper_limit` or None if not set
        """
        return self._data["Dry-Bulb Temperature Difference Range 8 Upper Limit"]

    @drybulb_temperature_difference_range_8_upper_limit.setter
    def drybulb_temperature_difference_range_8_upper_limit(self, value=None):
        """  Corresponds to IDD Field `Dry-Bulb Temperature Difference Range 8 Upper Limit`

        Args:
            value (float): value for IDD Field `Dry-Bulb Temperature Difference Range 8 Upper Limit`
                Units: deltaC
                value >= -50.0
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
                                 'for field `drybulb_temperature_difference_range_8_upper_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `drybulb_temperature_difference_range_8_upper_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `drybulb_temperature_difference_range_8_upper_limit`')
        self._data["Dry-Bulb Temperature Difference Range 8 Upper Limit"] = value

    @property
    def range_8_equipment_list_name(self):
        """Get range_8_equipment_list_name

        Returns:
            str: the value of `range_8_equipment_list_name` or None if not set
        """
        return self._data["Range 8 Equipment List Name"]

    @range_8_equipment_list_name.setter
    def range_8_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `Range 8 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 8 Equipment List Name`
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
                                 'for field `range_8_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_8_equipment_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `range_8_equipment_list_name`')
        self._data["Range 8 Equipment List Name"] = value

    @property
    def drybulb_temperature_difference_range_9_lower_limit(self):
        """Get drybulb_temperature_difference_range_9_lower_limit

        Returns:
            float: the value of `drybulb_temperature_difference_range_9_lower_limit` or None if not set
        """
        return self._data["Dry-Bulb Temperature Difference Range 9 Lower Limit"]

    @drybulb_temperature_difference_range_9_lower_limit.setter
    def drybulb_temperature_difference_range_9_lower_limit(self, value=None):
        """  Corresponds to IDD Field `Dry-Bulb Temperature Difference Range 9 Lower Limit`

        Args:
            value (float): value for IDD Field `Dry-Bulb Temperature Difference Range 9 Lower Limit`
                Units: deltaC
                value >= -50.0
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
                                 'for field `drybulb_temperature_difference_range_9_lower_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `drybulb_temperature_difference_range_9_lower_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `drybulb_temperature_difference_range_9_lower_limit`')
        self._data["Dry-Bulb Temperature Difference Range 9 Lower Limit"] = value

    @property
    def drybulb_temperature_difference_range_9_upper_limit(self):
        """Get drybulb_temperature_difference_range_9_upper_limit

        Returns:
            float: the value of `drybulb_temperature_difference_range_9_upper_limit` or None if not set
        """
        return self._data["Dry-Bulb Temperature Difference Range 9 Upper Limit"]

    @drybulb_temperature_difference_range_9_upper_limit.setter
    def drybulb_temperature_difference_range_9_upper_limit(self, value=None):
        """  Corresponds to IDD Field `Dry-Bulb Temperature Difference Range 9 Upper Limit`

        Args:
            value (float): value for IDD Field `Dry-Bulb Temperature Difference Range 9 Upper Limit`
                Units: deltaC
                value >= -50.0
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
                                 'for field `drybulb_temperature_difference_range_9_upper_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `drybulb_temperature_difference_range_9_upper_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `drybulb_temperature_difference_range_9_upper_limit`')
        self._data["Dry-Bulb Temperature Difference Range 9 Upper Limit"] = value

    @property
    def range_9_equipment_list_name(self):
        """Get range_9_equipment_list_name

        Returns:
            str: the value of `range_9_equipment_list_name` or None if not set
        """
        return self._data["Range 9 Equipment List Name"]

    @range_9_equipment_list_name.setter
    def range_9_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `Range 9 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 9 Equipment List Name`
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
                                 'for field `range_9_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_9_equipment_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `range_9_equipment_list_name`')
        self._data["Range 9 Equipment List Name"] = value

    @property
    def drybulb_temperature_difference_range_10_lower_limit(self):
        """Get drybulb_temperature_difference_range_10_lower_limit

        Returns:
            float: the value of `drybulb_temperature_difference_range_10_lower_limit` or None if not set
        """
        return self._data["Dry-Bulb Temperature Difference Range 10 Lower Limit"]

    @drybulb_temperature_difference_range_10_lower_limit.setter
    def drybulb_temperature_difference_range_10_lower_limit(self, value=None):
        """  Corresponds to IDD Field `Dry-Bulb Temperature Difference Range 10 Lower Limit`

        Args:
            value (float): value for IDD Field `Dry-Bulb Temperature Difference Range 10 Lower Limit`
                Units: deltaC
                value >= -50.0
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
                                 'for field `drybulb_temperature_difference_range_10_lower_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `drybulb_temperature_difference_range_10_lower_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `drybulb_temperature_difference_range_10_lower_limit`')
        self._data["Dry-Bulb Temperature Difference Range 10 Lower Limit"] = value

    @property
    def drybulb_temperature_difference_range_10_upper_limit(self):
        """Get drybulb_temperature_difference_range_10_upper_limit

        Returns:
            float: the value of `drybulb_temperature_difference_range_10_upper_limit` or None if not set
        """
        return self._data["Dry-Bulb Temperature Difference Range 10 Upper Limit"]

    @drybulb_temperature_difference_range_10_upper_limit.setter
    def drybulb_temperature_difference_range_10_upper_limit(self, value=None):
        """  Corresponds to IDD Field `Dry-Bulb Temperature Difference Range 10 Upper Limit`

        Args:
            value (float): value for IDD Field `Dry-Bulb Temperature Difference Range 10 Upper Limit`
                Units: deltaC
                value >= -50.0
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
                                 'for field `drybulb_temperature_difference_range_10_upper_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `drybulb_temperature_difference_range_10_upper_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `drybulb_temperature_difference_range_10_upper_limit`')
        self._data["Dry-Bulb Temperature Difference Range 10 Upper Limit"] = value

    @property
    def range_10_equipment_list_name(self):
        """Get range_10_equipment_list_name

        Returns:
            str: the value of `range_10_equipment_list_name` or None if not set
        """
        return self._data["Range 10 Equipment List Name"]

    @range_10_equipment_list_name.setter
    def range_10_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `Range 10 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 10 Equipment List Name`
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
                                 'for field `range_10_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_10_equipment_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `range_10_equipment_list_name`')
        self._data["Range 10 Equipment List Name"] = value

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

class PlantEquipmentOperationOutdoorWetBulbDifference(object):
    """ Corresponds to IDD object `PlantEquipmentOperation:OutdoorWetBulbDifference`
        Plant equipment operation scheme for outdoor wet-bulb temperature difference
        operation. Specifies one or more groups of equipment which are available to operate
        for successive ranges based the difference between a reference node temperature and
        the outdoor wet-bulb temperature.
    
    """
    internal_name = "PlantEquipmentOperation:OutdoorWetBulbDifference"
    field_count = 32
    required_fields = ["Name", "Reference Temperature Node Name", "Wet-Bulb Temperature Difference Range 1 Lower Limit", "Wet-Bulb Temperature Difference Range 1 Upper Limit", "Range 1 Equipment List Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `PlantEquipmentOperation:OutdoorWetBulbDifference`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Reference Temperature Node Name"] = None
        self._data["Wet-Bulb Temperature Difference Range 1 Lower Limit"] = None
        self._data["Wet-Bulb Temperature Difference Range 1 Upper Limit"] = None
        self._data["Range 1 Equipment List Name"] = None
        self._data["Wet-Bulb Temperature Difference Range 2 Lower Limit"] = None
        self._data["Wet-Bulb Temperature Difference Range 2 Upper Limit"] = None
        self._data["Range 2 Equipment List Name"] = None
        self._data["Wet-Bulb Temperature Difference Range 3 Lower Limit"] = None
        self._data["Wet-Bulb Temperature Difference Range 3 Upper Limit"] = None
        self._data["Range 3 Equipment List Name"] = None
        self._data["Wet-Bulb Temperature Difference Range 4 Lower Limit"] = None
        self._data["Wet-Bulb Temperature Difference Range 4 Upper Limit"] = None
        self._data["Range 4 Equipment List Name"] = None
        self._data["Wet-Bulb Temperature Difference Range 5 Lower Limit"] = None
        self._data["Wet-Bulb Temperature Difference Range 5 Upper Limit"] = None
        self._data["Range 5 Equipment List Name"] = None
        self._data["Wet-Bulb Temperature Difference Range 6 Lower Limit"] = None
        self._data["Wet-Bulb Temperature Difference Range 6 Upper Limit"] = None
        self._data["Range 6 Equipment List Name"] = None
        self._data["Wet-Bulb Temperature Difference Range 7 Lower Limit"] = None
        self._data["Wet-Bulb Temperature Difference Range 7 Upper Limit"] = None
        self._data["Range 7 Equipment List Name"] = None
        self._data["Wet-Bulb Temperature Difference Range 8 Lower Limit"] = None
        self._data["Wet-Bulb Temperature Difference Range 8 Upper Limit"] = None
        self._data["Range 8 Equipment List Name"] = None
        self._data["Wet-Bulb Temperature Difference Range 9 Lower Limit"] = None
        self._data["Wet-Bulb Temperature Difference Range 9 Upper Limit"] = None
        self._data["Range 9 Equipment List Name"] = None
        self._data["Wet-Bulb Temperature Difference Range 10 Lower Limit"] = None
        self._data["Wet-Bulb Temperature Difference Range 10 Upper Limit"] = None
        self._data["Range 10 Equipment List Name"] = None
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
            self.reference_temperature_node_name = None
        else:
            self.reference_temperature_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wetbulb_temperature_difference_range_1_lower_limit = None
        else:
            self.wetbulb_temperature_difference_range_1_lower_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wetbulb_temperature_difference_range_1_upper_limit = None
        else:
            self.wetbulb_temperature_difference_range_1_upper_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.range_1_equipment_list_name = None
        else:
            self.range_1_equipment_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wetbulb_temperature_difference_range_2_lower_limit = None
        else:
            self.wetbulb_temperature_difference_range_2_lower_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wetbulb_temperature_difference_range_2_upper_limit = None
        else:
            self.wetbulb_temperature_difference_range_2_upper_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.range_2_equipment_list_name = None
        else:
            self.range_2_equipment_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wetbulb_temperature_difference_range_3_lower_limit = None
        else:
            self.wetbulb_temperature_difference_range_3_lower_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wetbulb_temperature_difference_range_3_upper_limit = None
        else:
            self.wetbulb_temperature_difference_range_3_upper_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.range_3_equipment_list_name = None
        else:
            self.range_3_equipment_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wetbulb_temperature_difference_range_4_lower_limit = None
        else:
            self.wetbulb_temperature_difference_range_4_lower_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wetbulb_temperature_difference_range_4_upper_limit = None
        else:
            self.wetbulb_temperature_difference_range_4_upper_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.range_4_equipment_list_name = None
        else:
            self.range_4_equipment_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wetbulb_temperature_difference_range_5_lower_limit = None
        else:
            self.wetbulb_temperature_difference_range_5_lower_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wetbulb_temperature_difference_range_5_upper_limit = None
        else:
            self.wetbulb_temperature_difference_range_5_upper_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.range_5_equipment_list_name = None
        else:
            self.range_5_equipment_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wetbulb_temperature_difference_range_6_lower_limit = None
        else:
            self.wetbulb_temperature_difference_range_6_lower_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wetbulb_temperature_difference_range_6_upper_limit = None
        else:
            self.wetbulb_temperature_difference_range_6_upper_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.range_6_equipment_list_name = None
        else:
            self.range_6_equipment_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wetbulb_temperature_difference_range_7_lower_limit = None
        else:
            self.wetbulb_temperature_difference_range_7_lower_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wetbulb_temperature_difference_range_7_upper_limit = None
        else:
            self.wetbulb_temperature_difference_range_7_upper_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.range_7_equipment_list_name = None
        else:
            self.range_7_equipment_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wetbulb_temperature_difference_range_8_lower_limit = None
        else:
            self.wetbulb_temperature_difference_range_8_lower_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wetbulb_temperature_difference_range_8_upper_limit = None
        else:
            self.wetbulb_temperature_difference_range_8_upper_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.range_8_equipment_list_name = None
        else:
            self.range_8_equipment_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wetbulb_temperature_difference_range_9_lower_limit = None
        else:
            self.wetbulb_temperature_difference_range_9_lower_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wetbulb_temperature_difference_range_9_upper_limit = None
        else:
            self.wetbulb_temperature_difference_range_9_upper_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.range_9_equipment_list_name = None
        else:
            self.range_9_equipment_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wetbulb_temperature_difference_range_10_lower_limit = None
        else:
            self.wetbulb_temperature_difference_range_10_lower_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wetbulb_temperature_difference_range_10_upper_limit = None
        else:
            self.wetbulb_temperature_difference_range_10_upper_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.range_10_equipment_list_name = None
        else:
            self.range_10_equipment_list_name = vals[i]
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
    def reference_temperature_node_name(self):
        """Get reference_temperature_node_name

        Returns:
            str: the value of `reference_temperature_node_name` or None if not set
        """
        return self._data["Reference Temperature Node Name"]

    @reference_temperature_node_name.setter
    def reference_temperature_node_name(self, value=None):
        """  Corresponds to IDD Field `Reference Temperature Node Name`

        Args:
            value (str): value for IDD Field `Reference Temperature Node Name`
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
                                 'for field `reference_temperature_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `reference_temperature_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `reference_temperature_node_name`')
        self._data["Reference Temperature Node Name"] = value

    @property
    def wetbulb_temperature_difference_range_1_lower_limit(self):
        """Get wetbulb_temperature_difference_range_1_lower_limit

        Returns:
            float: the value of `wetbulb_temperature_difference_range_1_lower_limit` or None if not set
        """
        return self._data["Wet-Bulb Temperature Difference Range 1 Lower Limit"]

    @wetbulb_temperature_difference_range_1_lower_limit.setter
    def wetbulb_temperature_difference_range_1_lower_limit(self, value=None):
        """  Corresponds to IDD Field `Wet-Bulb Temperature Difference Range 1 Lower Limit`

        Args:
            value (float): value for IDD Field `Wet-Bulb Temperature Difference Range 1 Lower Limit`
                Units: deltaC
                value >= -50.0
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
                                 'for field `wetbulb_temperature_difference_range_1_lower_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `wetbulb_temperature_difference_range_1_lower_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `wetbulb_temperature_difference_range_1_lower_limit`')
        self._data["Wet-Bulb Temperature Difference Range 1 Lower Limit"] = value

    @property
    def wetbulb_temperature_difference_range_1_upper_limit(self):
        """Get wetbulb_temperature_difference_range_1_upper_limit

        Returns:
            float: the value of `wetbulb_temperature_difference_range_1_upper_limit` or None if not set
        """
        return self._data["Wet-Bulb Temperature Difference Range 1 Upper Limit"]

    @wetbulb_temperature_difference_range_1_upper_limit.setter
    def wetbulb_temperature_difference_range_1_upper_limit(self, value=None):
        """  Corresponds to IDD Field `Wet-Bulb Temperature Difference Range 1 Upper Limit`

        Args:
            value (float): value for IDD Field `Wet-Bulb Temperature Difference Range 1 Upper Limit`
                Units: deltaC
                value >= -50.0
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
                                 'for field `wetbulb_temperature_difference_range_1_upper_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `wetbulb_temperature_difference_range_1_upper_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `wetbulb_temperature_difference_range_1_upper_limit`')
        self._data["Wet-Bulb Temperature Difference Range 1 Upper Limit"] = value

    @property
    def range_1_equipment_list_name(self):
        """Get range_1_equipment_list_name

        Returns:
            str: the value of `range_1_equipment_list_name` or None if not set
        """
        return self._data["Range 1 Equipment List Name"]

    @range_1_equipment_list_name.setter
    def range_1_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `Range 1 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 1 Equipment List Name`
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
                                 'for field `range_1_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_1_equipment_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `range_1_equipment_list_name`')
        self._data["Range 1 Equipment List Name"] = value

    @property
    def wetbulb_temperature_difference_range_2_lower_limit(self):
        """Get wetbulb_temperature_difference_range_2_lower_limit

        Returns:
            float: the value of `wetbulb_temperature_difference_range_2_lower_limit` or None if not set
        """
        return self._data["Wet-Bulb Temperature Difference Range 2 Lower Limit"]

    @wetbulb_temperature_difference_range_2_lower_limit.setter
    def wetbulb_temperature_difference_range_2_lower_limit(self, value=None):
        """  Corresponds to IDD Field `Wet-Bulb Temperature Difference Range 2 Lower Limit`

        Args:
            value (float): value for IDD Field `Wet-Bulb Temperature Difference Range 2 Lower Limit`
                Units: deltaC
                value >= -50.0
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
                                 'for field `wetbulb_temperature_difference_range_2_lower_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `wetbulb_temperature_difference_range_2_lower_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `wetbulb_temperature_difference_range_2_lower_limit`')
        self._data["Wet-Bulb Temperature Difference Range 2 Lower Limit"] = value

    @property
    def wetbulb_temperature_difference_range_2_upper_limit(self):
        """Get wetbulb_temperature_difference_range_2_upper_limit

        Returns:
            float: the value of `wetbulb_temperature_difference_range_2_upper_limit` or None if not set
        """
        return self._data["Wet-Bulb Temperature Difference Range 2 Upper Limit"]

    @wetbulb_temperature_difference_range_2_upper_limit.setter
    def wetbulb_temperature_difference_range_2_upper_limit(self, value=None):
        """  Corresponds to IDD Field `Wet-Bulb Temperature Difference Range 2 Upper Limit`

        Args:
            value (float): value for IDD Field `Wet-Bulb Temperature Difference Range 2 Upper Limit`
                Units: deltaC
                value >= -50.0
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
                                 'for field `wetbulb_temperature_difference_range_2_upper_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `wetbulb_temperature_difference_range_2_upper_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `wetbulb_temperature_difference_range_2_upper_limit`')
        self._data["Wet-Bulb Temperature Difference Range 2 Upper Limit"] = value

    @property
    def range_2_equipment_list_name(self):
        """Get range_2_equipment_list_name

        Returns:
            str: the value of `range_2_equipment_list_name` or None if not set
        """
        return self._data["Range 2 Equipment List Name"]

    @range_2_equipment_list_name.setter
    def range_2_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `Range 2 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 2 Equipment List Name`
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
                                 'for field `range_2_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_2_equipment_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `range_2_equipment_list_name`')
        self._data["Range 2 Equipment List Name"] = value

    @property
    def wetbulb_temperature_difference_range_3_lower_limit(self):
        """Get wetbulb_temperature_difference_range_3_lower_limit

        Returns:
            float: the value of `wetbulb_temperature_difference_range_3_lower_limit` or None if not set
        """
        return self._data["Wet-Bulb Temperature Difference Range 3 Lower Limit"]

    @wetbulb_temperature_difference_range_3_lower_limit.setter
    def wetbulb_temperature_difference_range_3_lower_limit(self, value=None):
        """  Corresponds to IDD Field `Wet-Bulb Temperature Difference Range 3 Lower Limit`

        Args:
            value (float): value for IDD Field `Wet-Bulb Temperature Difference Range 3 Lower Limit`
                Units: deltaC
                value >= -50.0
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
                                 'for field `wetbulb_temperature_difference_range_3_lower_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `wetbulb_temperature_difference_range_3_lower_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `wetbulb_temperature_difference_range_3_lower_limit`')
        self._data["Wet-Bulb Temperature Difference Range 3 Lower Limit"] = value

    @property
    def wetbulb_temperature_difference_range_3_upper_limit(self):
        """Get wetbulb_temperature_difference_range_3_upper_limit

        Returns:
            float: the value of `wetbulb_temperature_difference_range_3_upper_limit` or None if not set
        """
        return self._data["Wet-Bulb Temperature Difference Range 3 Upper Limit"]

    @wetbulb_temperature_difference_range_3_upper_limit.setter
    def wetbulb_temperature_difference_range_3_upper_limit(self, value=None):
        """  Corresponds to IDD Field `Wet-Bulb Temperature Difference Range 3 Upper Limit`

        Args:
            value (float): value for IDD Field `Wet-Bulb Temperature Difference Range 3 Upper Limit`
                Units: deltaC
                value >= -50.0
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
                                 'for field `wetbulb_temperature_difference_range_3_upper_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `wetbulb_temperature_difference_range_3_upper_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `wetbulb_temperature_difference_range_3_upper_limit`')
        self._data["Wet-Bulb Temperature Difference Range 3 Upper Limit"] = value

    @property
    def range_3_equipment_list_name(self):
        """Get range_3_equipment_list_name

        Returns:
            str: the value of `range_3_equipment_list_name` or None if not set
        """
        return self._data["Range 3 Equipment List Name"]

    @range_3_equipment_list_name.setter
    def range_3_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `Range 3 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 3 Equipment List Name`
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
                                 'for field `range_3_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_3_equipment_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `range_3_equipment_list_name`')
        self._data["Range 3 Equipment List Name"] = value

    @property
    def wetbulb_temperature_difference_range_4_lower_limit(self):
        """Get wetbulb_temperature_difference_range_4_lower_limit

        Returns:
            float: the value of `wetbulb_temperature_difference_range_4_lower_limit` or None if not set
        """
        return self._data["Wet-Bulb Temperature Difference Range 4 Lower Limit"]

    @wetbulb_temperature_difference_range_4_lower_limit.setter
    def wetbulb_temperature_difference_range_4_lower_limit(self, value=None):
        """  Corresponds to IDD Field `Wet-Bulb Temperature Difference Range 4 Lower Limit`

        Args:
            value (float): value for IDD Field `Wet-Bulb Temperature Difference Range 4 Lower Limit`
                Units: deltaC
                value >= -50.0
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
                                 'for field `wetbulb_temperature_difference_range_4_lower_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `wetbulb_temperature_difference_range_4_lower_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `wetbulb_temperature_difference_range_4_lower_limit`')
        self._data["Wet-Bulb Temperature Difference Range 4 Lower Limit"] = value

    @property
    def wetbulb_temperature_difference_range_4_upper_limit(self):
        """Get wetbulb_temperature_difference_range_4_upper_limit

        Returns:
            float: the value of `wetbulb_temperature_difference_range_4_upper_limit` or None if not set
        """
        return self._data["Wet-Bulb Temperature Difference Range 4 Upper Limit"]

    @wetbulb_temperature_difference_range_4_upper_limit.setter
    def wetbulb_temperature_difference_range_4_upper_limit(self, value=None):
        """  Corresponds to IDD Field `Wet-Bulb Temperature Difference Range 4 Upper Limit`

        Args:
            value (float): value for IDD Field `Wet-Bulb Temperature Difference Range 4 Upper Limit`
                Units: deltaC
                value >= -50.0
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
                                 'for field `wetbulb_temperature_difference_range_4_upper_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `wetbulb_temperature_difference_range_4_upper_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `wetbulb_temperature_difference_range_4_upper_limit`')
        self._data["Wet-Bulb Temperature Difference Range 4 Upper Limit"] = value

    @property
    def range_4_equipment_list_name(self):
        """Get range_4_equipment_list_name

        Returns:
            str: the value of `range_4_equipment_list_name` or None if not set
        """
        return self._data["Range 4 Equipment List Name"]

    @range_4_equipment_list_name.setter
    def range_4_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `Range 4 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 4 Equipment List Name`
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
                                 'for field `range_4_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_4_equipment_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `range_4_equipment_list_name`')
        self._data["Range 4 Equipment List Name"] = value

    @property
    def wetbulb_temperature_difference_range_5_lower_limit(self):
        """Get wetbulb_temperature_difference_range_5_lower_limit

        Returns:
            float: the value of `wetbulb_temperature_difference_range_5_lower_limit` or None if not set
        """
        return self._data["Wet-Bulb Temperature Difference Range 5 Lower Limit"]

    @wetbulb_temperature_difference_range_5_lower_limit.setter
    def wetbulb_temperature_difference_range_5_lower_limit(self, value=None):
        """  Corresponds to IDD Field `Wet-Bulb Temperature Difference Range 5 Lower Limit`

        Args:
            value (float): value for IDD Field `Wet-Bulb Temperature Difference Range 5 Lower Limit`
                Units: deltaC
                value >= -50.0
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
                                 'for field `wetbulb_temperature_difference_range_5_lower_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `wetbulb_temperature_difference_range_5_lower_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `wetbulb_temperature_difference_range_5_lower_limit`')
        self._data["Wet-Bulb Temperature Difference Range 5 Lower Limit"] = value

    @property
    def wetbulb_temperature_difference_range_5_upper_limit(self):
        """Get wetbulb_temperature_difference_range_5_upper_limit

        Returns:
            float: the value of `wetbulb_temperature_difference_range_5_upper_limit` or None if not set
        """
        return self._data["Wet-Bulb Temperature Difference Range 5 Upper Limit"]

    @wetbulb_temperature_difference_range_5_upper_limit.setter
    def wetbulb_temperature_difference_range_5_upper_limit(self, value=None):
        """  Corresponds to IDD Field `Wet-Bulb Temperature Difference Range 5 Upper Limit`

        Args:
            value (float): value for IDD Field `Wet-Bulb Temperature Difference Range 5 Upper Limit`
                Units: deltaC
                value >= -50.0
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
                                 'for field `wetbulb_temperature_difference_range_5_upper_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `wetbulb_temperature_difference_range_5_upper_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `wetbulb_temperature_difference_range_5_upper_limit`')
        self._data["Wet-Bulb Temperature Difference Range 5 Upper Limit"] = value

    @property
    def range_5_equipment_list_name(self):
        """Get range_5_equipment_list_name

        Returns:
            str: the value of `range_5_equipment_list_name` or None if not set
        """
        return self._data["Range 5 Equipment List Name"]

    @range_5_equipment_list_name.setter
    def range_5_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `Range 5 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 5 Equipment List Name`
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
                                 'for field `range_5_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_5_equipment_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `range_5_equipment_list_name`')
        self._data["Range 5 Equipment List Name"] = value

    @property
    def wetbulb_temperature_difference_range_6_lower_limit(self):
        """Get wetbulb_temperature_difference_range_6_lower_limit

        Returns:
            float: the value of `wetbulb_temperature_difference_range_6_lower_limit` or None if not set
        """
        return self._data["Wet-Bulb Temperature Difference Range 6 Lower Limit"]

    @wetbulb_temperature_difference_range_6_lower_limit.setter
    def wetbulb_temperature_difference_range_6_lower_limit(self, value=None):
        """  Corresponds to IDD Field `Wet-Bulb Temperature Difference Range 6 Lower Limit`

        Args:
            value (float): value for IDD Field `Wet-Bulb Temperature Difference Range 6 Lower Limit`
                Units: deltaC
                value >= -50.0
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
                                 'for field `wetbulb_temperature_difference_range_6_lower_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `wetbulb_temperature_difference_range_6_lower_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `wetbulb_temperature_difference_range_6_lower_limit`')
        self._data["Wet-Bulb Temperature Difference Range 6 Lower Limit"] = value

    @property
    def wetbulb_temperature_difference_range_6_upper_limit(self):
        """Get wetbulb_temperature_difference_range_6_upper_limit

        Returns:
            float: the value of `wetbulb_temperature_difference_range_6_upper_limit` or None if not set
        """
        return self._data["Wet-Bulb Temperature Difference Range 6 Upper Limit"]

    @wetbulb_temperature_difference_range_6_upper_limit.setter
    def wetbulb_temperature_difference_range_6_upper_limit(self, value=None):
        """  Corresponds to IDD Field `Wet-Bulb Temperature Difference Range 6 Upper Limit`

        Args:
            value (float): value for IDD Field `Wet-Bulb Temperature Difference Range 6 Upper Limit`
                Units: deltaC
                value >= -50.0
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
                                 'for field `wetbulb_temperature_difference_range_6_upper_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `wetbulb_temperature_difference_range_6_upper_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `wetbulb_temperature_difference_range_6_upper_limit`')
        self._data["Wet-Bulb Temperature Difference Range 6 Upper Limit"] = value

    @property
    def range_6_equipment_list_name(self):
        """Get range_6_equipment_list_name

        Returns:
            str: the value of `range_6_equipment_list_name` or None if not set
        """
        return self._data["Range 6 Equipment List Name"]

    @range_6_equipment_list_name.setter
    def range_6_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `Range 6 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 6 Equipment List Name`
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
                                 'for field `range_6_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_6_equipment_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `range_6_equipment_list_name`')
        self._data["Range 6 Equipment List Name"] = value

    @property
    def wetbulb_temperature_difference_range_7_lower_limit(self):
        """Get wetbulb_temperature_difference_range_7_lower_limit

        Returns:
            float: the value of `wetbulb_temperature_difference_range_7_lower_limit` or None if not set
        """
        return self._data["Wet-Bulb Temperature Difference Range 7 Lower Limit"]

    @wetbulb_temperature_difference_range_7_lower_limit.setter
    def wetbulb_temperature_difference_range_7_lower_limit(self, value=None):
        """  Corresponds to IDD Field `Wet-Bulb Temperature Difference Range 7 Lower Limit`

        Args:
            value (float): value for IDD Field `Wet-Bulb Temperature Difference Range 7 Lower Limit`
                Units: deltaC
                value >= -50.0
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
                                 'for field `wetbulb_temperature_difference_range_7_lower_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `wetbulb_temperature_difference_range_7_lower_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `wetbulb_temperature_difference_range_7_lower_limit`')
        self._data["Wet-Bulb Temperature Difference Range 7 Lower Limit"] = value

    @property
    def wetbulb_temperature_difference_range_7_upper_limit(self):
        """Get wetbulb_temperature_difference_range_7_upper_limit

        Returns:
            float: the value of `wetbulb_temperature_difference_range_7_upper_limit` or None if not set
        """
        return self._data["Wet-Bulb Temperature Difference Range 7 Upper Limit"]

    @wetbulb_temperature_difference_range_7_upper_limit.setter
    def wetbulb_temperature_difference_range_7_upper_limit(self, value=None):
        """  Corresponds to IDD Field `Wet-Bulb Temperature Difference Range 7 Upper Limit`

        Args:
            value (float): value for IDD Field `Wet-Bulb Temperature Difference Range 7 Upper Limit`
                Units: deltaC
                value >= -50.0
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
                                 'for field `wetbulb_temperature_difference_range_7_upper_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `wetbulb_temperature_difference_range_7_upper_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `wetbulb_temperature_difference_range_7_upper_limit`')
        self._data["Wet-Bulb Temperature Difference Range 7 Upper Limit"] = value

    @property
    def range_7_equipment_list_name(self):
        """Get range_7_equipment_list_name

        Returns:
            str: the value of `range_7_equipment_list_name` or None if not set
        """
        return self._data["Range 7 Equipment List Name"]

    @range_7_equipment_list_name.setter
    def range_7_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `Range 7 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 7 Equipment List Name`
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
                                 'for field `range_7_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_7_equipment_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `range_7_equipment_list_name`')
        self._data["Range 7 Equipment List Name"] = value

    @property
    def wetbulb_temperature_difference_range_8_lower_limit(self):
        """Get wetbulb_temperature_difference_range_8_lower_limit

        Returns:
            float: the value of `wetbulb_temperature_difference_range_8_lower_limit` or None if not set
        """
        return self._data["Wet-Bulb Temperature Difference Range 8 Lower Limit"]

    @wetbulb_temperature_difference_range_8_lower_limit.setter
    def wetbulb_temperature_difference_range_8_lower_limit(self, value=None):
        """  Corresponds to IDD Field `Wet-Bulb Temperature Difference Range 8 Lower Limit`

        Args:
            value (float): value for IDD Field `Wet-Bulb Temperature Difference Range 8 Lower Limit`
                Units: deltaC
                value >= -50.0
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
                                 'for field `wetbulb_temperature_difference_range_8_lower_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `wetbulb_temperature_difference_range_8_lower_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `wetbulb_temperature_difference_range_8_lower_limit`')
        self._data["Wet-Bulb Temperature Difference Range 8 Lower Limit"] = value

    @property
    def wetbulb_temperature_difference_range_8_upper_limit(self):
        """Get wetbulb_temperature_difference_range_8_upper_limit

        Returns:
            float: the value of `wetbulb_temperature_difference_range_8_upper_limit` or None if not set
        """
        return self._data["Wet-Bulb Temperature Difference Range 8 Upper Limit"]

    @wetbulb_temperature_difference_range_8_upper_limit.setter
    def wetbulb_temperature_difference_range_8_upper_limit(self, value=None):
        """  Corresponds to IDD Field `Wet-Bulb Temperature Difference Range 8 Upper Limit`

        Args:
            value (float): value for IDD Field `Wet-Bulb Temperature Difference Range 8 Upper Limit`
                Units: deltaC
                value >= -50.0
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
                                 'for field `wetbulb_temperature_difference_range_8_upper_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `wetbulb_temperature_difference_range_8_upper_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `wetbulb_temperature_difference_range_8_upper_limit`')
        self._data["Wet-Bulb Temperature Difference Range 8 Upper Limit"] = value

    @property
    def range_8_equipment_list_name(self):
        """Get range_8_equipment_list_name

        Returns:
            str: the value of `range_8_equipment_list_name` or None if not set
        """
        return self._data["Range 8 Equipment List Name"]

    @range_8_equipment_list_name.setter
    def range_8_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `Range 8 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 8 Equipment List Name`
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
                                 'for field `range_8_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_8_equipment_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `range_8_equipment_list_name`')
        self._data["Range 8 Equipment List Name"] = value

    @property
    def wetbulb_temperature_difference_range_9_lower_limit(self):
        """Get wetbulb_temperature_difference_range_9_lower_limit

        Returns:
            float: the value of `wetbulb_temperature_difference_range_9_lower_limit` or None if not set
        """
        return self._data["Wet-Bulb Temperature Difference Range 9 Lower Limit"]

    @wetbulb_temperature_difference_range_9_lower_limit.setter
    def wetbulb_temperature_difference_range_9_lower_limit(self, value=None):
        """  Corresponds to IDD Field `Wet-Bulb Temperature Difference Range 9 Lower Limit`

        Args:
            value (float): value for IDD Field `Wet-Bulb Temperature Difference Range 9 Lower Limit`
                Units: deltaC
                value >= -50.0
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
                                 'for field `wetbulb_temperature_difference_range_9_lower_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `wetbulb_temperature_difference_range_9_lower_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `wetbulb_temperature_difference_range_9_lower_limit`')
        self._data["Wet-Bulb Temperature Difference Range 9 Lower Limit"] = value

    @property
    def wetbulb_temperature_difference_range_9_upper_limit(self):
        """Get wetbulb_temperature_difference_range_9_upper_limit

        Returns:
            float: the value of `wetbulb_temperature_difference_range_9_upper_limit` or None if not set
        """
        return self._data["Wet-Bulb Temperature Difference Range 9 Upper Limit"]

    @wetbulb_temperature_difference_range_9_upper_limit.setter
    def wetbulb_temperature_difference_range_9_upper_limit(self, value=None):
        """  Corresponds to IDD Field `Wet-Bulb Temperature Difference Range 9 Upper Limit`

        Args:
            value (float): value for IDD Field `Wet-Bulb Temperature Difference Range 9 Upper Limit`
                Units: deltaC
                value >= -50.0
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
                                 'for field `wetbulb_temperature_difference_range_9_upper_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `wetbulb_temperature_difference_range_9_upper_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `wetbulb_temperature_difference_range_9_upper_limit`')
        self._data["Wet-Bulb Temperature Difference Range 9 Upper Limit"] = value

    @property
    def range_9_equipment_list_name(self):
        """Get range_9_equipment_list_name

        Returns:
            str: the value of `range_9_equipment_list_name` or None if not set
        """
        return self._data["Range 9 Equipment List Name"]

    @range_9_equipment_list_name.setter
    def range_9_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `Range 9 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 9 Equipment List Name`
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
                                 'for field `range_9_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_9_equipment_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `range_9_equipment_list_name`')
        self._data["Range 9 Equipment List Name"] = value

    @property
    def wetbulb_temperature_difference_range_10_lower_limit(self):
        """Get wetbulb_temperature_difference_range_10_lower_limit

        Returns:
            float: the value of `wetbulb_temperature_difference_range_10_lower_limit` or None if not set
        """
        return self._data["Wet-Bulb Temperature Difference Range 10 Lower Limit"]

    @wetbulb_temperature_difference_range_10_lower_limit.setter
    def wetbulb_temperature_difference_range_10_lower_limit(self, value=None):
        """  Corresponds to IDD Field `Wet-Bulb Temperature Difference Range 10 Lower Limit`

        Args:
            value (float): value for IDD Field `Wet-Bulb Temperature Difference Range 10 Lower Limit`
                Units: deltaC
                value >= -50.0
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
                                 'for field `wetbulb_temperature_difference_range_10_lower_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `wetbulb_temperature_difference_range_10_lower_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `wetbulb_temperature_difference_range_10_lower_limit`')
        self._data["Wet-Bulb Temperature Difference Range 10 Lower Limit"] = value

    @property
    def wetbulb_temperature_difference_range_10_upper_limit(self):
        """Get wetbulb_temperature_difference_range_10_upper_limit

        Returns:
            float: the value of `wetbulb_temperature_difference_range_10_upper_limit` or None if not set
        """
        return self._data["Wet-Bulb Temperature Difference Range 10 Upper Limit"]

    @wetbulb_temperature_difference_range_10_upper_limit.setter
    def wetbulb_temperature_difference_range_10_upper_limit(self, value=None):
        """  Corresponds to IDD Field `Wet-Bulb Temperature Difference Range 10 Upper Limit`

        Args:
            value (float): value for IDD Field `Wet-Bulb Temperature Difference Range 10 Upper Limit`
                Units: deltaC
                value >= -50.0
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
                                 'for field `wetbulb_temperature_difference_range_10_upper_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `wetbulb_temperature_difference_range_10_upper_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `wetbulb_temperature_difference_range_10_upper_limit`')
        self._data["Wet-Bulb Temperature Difference Range 10 Upper Limit"] = value

    @property
    def range_10_equipment_list_name(self):
        """Get range_10_equipment_list_name

        Returns:
            str: the value of `range_10_equipment_list_name` or None if not set
        """
        return self._data["Range 10 Equipment List Name"]

    @range_10_equipment_list_name.setter
    def range_10_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `Range 10 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 10 Equipment List Name`
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
                                 'for field `range_10_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_10_equipment_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `range_10_equipment_list_name`')
        self._data["Range 10 Equipment List Name"] = value

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

class PlantEquipmentOperationOutdoorDewpointDifference(object):
    """ Corresponds to IDD object `PlantEquipmentOperation:OutdoorDewpointDifference`
        Plant equipment operation scheme for outdoor dewpoint temperature difference
        operation. Specifies one or more groups of equipment which are available to operate
        for successive ranges based the difference between a reference node temperature and
        the outdoor dewpoint temperature.
    
    """
    internal_name = "PlantEquipmentOperation:OutdoorDewpointDifference"
    field_count = 32
    required_fields = ["Name", "Reference Temperature Node Name", "Dewpoint Temperature Difference Range 1 Lower Limit", "Dewpoint Temperature Difference Range 1 Upper Limit", "Range 1 Equipment List Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `PlantEquipmentOperation:OutdoorDewpointDifference`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Reference Temperature Node Name"] = None
        self._data["Dewpoint Temperature Difference Range 1 Lower Limit"] = None
        self._data["Dewpoint Temperature Difference Range 1 Upper Limit"] = None
        self._data["Range 1 Equipment List Name"] = None
        self._data["Dewpoint Temperature Difference Range 2 Lower Limit"] = None
        self._data["Dewpoint Temperature Difference Range 2 Upper Limit"] = None
        self._data["Range 2 Equipment List Name"] = None
        self._data["Dewpoint Temperature Difference Range 3 Lower Limit"] = None
        self._data["Dewpoint Temperature Difference Range 3 Upper Limit"] = None
        self._data["Range 3 Equipment List Name"] = None
        self._data["Dewpoint Temperature Difference Range 4 Lower Limit"] = None
        self._data["Dewpoint Temperature Difference Range 4 Upper Limit"] = None
        self._data["Range 4 Equipment List Name"] = None
        self._data["Dewpoint Temperature Difference Range 5 Lower Limit"] = None
        self._data["Dewpoint Temperature Difference Range 5 Upper Limit"] = None
        self._data["Range 5 Equipment List Name"] = None
        self._data["Dewpoint Temperature Difference Range 6 Lower Limit"] = None
        self._data["Dewpoint Temperature Difference Range 6 Upper Limit"] = None
        self._data["Range 6 Equipment List Name"] = None
        self._data["Dewpoint Temperature Difference Range 7 Lower Limit"] = None
        self._data["Dewpoint Temperature Difference Range 7 Upper Limit"] = None
        self._data["Range 7 Equipment List Name"] = None
        self._data["Dewpoint Temperature Difference Range 8 Lower Limit"] = None
        self._data["Dewpoint Temperature Difference Range 8 Upper Limit"] = None
        self._data["Range 8 Equipment List Name"] = None
        self._data["Dewpoint Temperature Difference Range 9 Lower Limit"] = None
        self._data["Dewpoint Temperature Difference Range 9 Upper Limit"] = None
        self._data["Range 9 Equipment List Name"] = None
        self._data["Dewpoint Temperature Difference Range 10 Lower Limit"] = None
        self._data["Dewpoint Temperature Difference Range 10 Upper Limit"] = None
        self._data["Range 10 Equipment List Name"] = None
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
            self.reference_temperature_node_name = None
        else:
            self.reference_temperature_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.dewpoint_temperature_difference_range_1_lower_limit = None
        else:
            self.dewpoint_temperature_difference_range_1_lower_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.dewpoint_temperature_difference_range_1_upper_limit = None
        else:
            self.dewpoint_temperature_difference_range_1_upper_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.range_1_equipment_list_name = None
        else:
            self.range_1_equipment_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.dewpoint_temperature_difference_range_2_lower_limit = None
        else:
            self.dewpoint_temperature_difference_range_2_lower_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.dewpoint_temperature_difference_range_2_upper_limit = None
        else:
            self.dewpoint_temperature_difference_range_2_upper_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.range_2_equipment_list_name = None
        else:
            self.range_2_equipment_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.dewpoint_temperature_difference_range_3_lower_limit = None
        else:
            self.dewpoint_temperature_difference_range_3_lower_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.dewpoint_temperature_difference_range_3_upper_limit = None
        else:
            self.dewpoint_temperature_difference_range_3_upper_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.range_3_equipment_list_name = None
        else:
            self.range_3_equipment_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.dewpoint_temperature_difference_range_4_lower_limit = None
        else:
            self.dewpoint_temperature_difference_range_4_lower_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.dewpoint_temperature_difference_range_4_upper_limit = None
        else:
            self.dewpoint_temperature_difference_range_4_upper_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.range_4_equipment_list_name = None
        else:
            self.range_4_equipment_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.dewpoint_temperature_difference_range_5_lower_limit = None
        else:
            self.dewpoint_temperature_difference_range_5_lower_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.dewpoint_temperature_difference_range_5_upper_limit = None
        else:
            self.dewpoint_temperature_difference_range_5_upper_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.range_5_equipment_list_name = None
        else:
            self.range_5_equipment_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.dewpoint_temperature_difference_range_6_lower_limit = None
        else:
            self.dewpoint_temperature_difference_range_6_lower_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.dewpoint_temperature_difference_range_6_upper_limit = None
        else:
            self.dewpoint_temperature_difference_range_6_upper_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.range_6_equipment_list_name = None
        else:
            self.range_6_equipment_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.dewpoint_temperature_difference_range_7_lower_limit = None
        else:
            self.dewpoint_temperature_difference_range_7_lower_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.dewpoint_temperature_difference_range_7_upper_limit = None
        else:
            self.dewpoint_temperature_difference_range_7_upper_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.range_7_equipment_list_name = None
        else:
            self.range_7_equipment_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.dewpoint_temperature_difference_range_8_lower_limit = None
        else:
            self.dewpoint_temperature_difference_range_8_lower_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.dewpoint_temperature_difference_range_8_upper_limit = None
        else:
            self.dewpoint_temperature_difference_range_8_upper_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.range_8_equipment_list_name = None
        else:
            self.range_8_equipment_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.dewpoint_temperature_difference_range_9_lower_limit = None
        else:
            self.dewpoint_temperature_difference_range_9_lower_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.dewpoint_temperature_difference_range_9_upper_limit = None
        else:
            self.dewpoint_temperature_difference_range_9_upper_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.range_9_equipment_list_name = None
        else:
            self.range_9_equipment_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.dewpoint_temperature_difference_range_10_lower_limit = None
        else:
            self.dewpoint_temperature_difference_range_10_lower_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.dewpoint_temperature_difference_range_10_upper_limit = None
        else:
            self.dewpoint_temperature_difference_range_10_upper_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.range_10_equipment_list_name = None
        else:
            self.range_10_equipment_list_name = vals[i]
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
    def reference_temperature_node_name(self):
        """Get reference_temperature_node_name

        Returns:
            str: the value of `reference_temperature_node_name` or None if not set
        """
        return self._data["Reference Temperature Node Name"]

    @reference_temperature_node_name.setter
    def reference_temperature_node_name(self, value=None):
        """  Corresponds to IDD Field `Reference Temperature Node Name`

        Args:
            value (str): value for IDD Field `Reference Temperature Node Name`
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
                                 'for field `reference_temperature_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `reference_temperature_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `reference_temperature_node_name`')
        self._data["Reference Temperature Node Name"] = value

    @property
    def dewpoint_temperature_difference_range_1_lower_limit(self):
        """Get dewpoint_temperature_difference_range_1_lower_limit

        Returns:
            float: the value of `dewpoint_temperature_difference_range_1_lower_limit` or None if not set
        """
        return self._data["Dewpoint Temperature Difference Range 1 Lower Limit"]

    @dewpoint_temperature_difference_range_1_lower_limit.setter
    def dewpoint_temperature_difference_range_1_lower_limit(self, value=None):
        """  Corresponds to IDD Field `Dewpoint Temperature Difference Range 1 Lower Limit`

        Args:
            value (float): value for IDD Field `Dewpoint Temperature Difference Range 1 Lower Limit`
                Units: deltaC
                value >= -50.0
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
                                 'for field `dewpoint_temperature_difference_range_1_lower_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `dewpoint_temperature_difference_range_1_lower_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `dewpoint_temperature_difference_range_1_lower_limit`')
        self._data["Dewpoint Temperature Difference Range 1 Lower Limit"] = value

    @property
    def dewpoint_temperature_difference_range_1_upper_limit(self):
        """Get dewpoint_temperature_difference_range_1_upper_limit

        Returns:
            float: the value of `dewpoint_temperature_difference_range_1_upper_limit` or None if not set
        """
        return self._data["Dewpoint Temperature Difference Range 1 Upper Limit"]

    @dewpoint_temperature_difference_range_1_upper_limit.setter
    def dewpoint_temperature_difference_range_1_upper_limit(self, value=None):
        """  Corresponds to IDD Field `Dewpoint Temperature Difference Range 1 Upper Limit`

        Args:
            value (float): value for IDD Field `Dewpoint Temperature Difference Range 1 Upper Limit`
                Units: deltaC
                value >= -50.0
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
                                 'for field `dewpoint_temperature_difference_range_1_upper_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `dewpoint_temperature_difference_range_1_upper_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `dewpoint_temperature_difference_range_1_upper_limit`')
        self._data["Dewpoint Temperature Difference Range 1 Upper Limit"] = value

    @property
    def range_1_equipment_list_name(self):
        """Get range_1_equipment_list_name

        Returns:
            str: the value of `range_1_equipment_list_name` or None if not set
        """
        return self._data["Range 1 Equipment List Name"]

    @range_1_equipment_list_name.setter
    def range_1_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `Range 1 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 1 Equipment List Name`
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
                                 'for field `range_1_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_1_equipment_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `range_1_equipment_list_name`')
        self._data["Range 1 Equipment List Name"] = value

    @property
    def dewpoint_temperature_difference_range_2_lower_limit(self):
        """Get dewpoint_temperature_difference_range_2_lower_limit

        Returns:
            float: the value of `dewpoint_temperature_difference_range_2_lower_limit` or None if not set
        """
        return self._data["Dewpoint Temperature Difference Range 2 Lower Limit"]

    @dewpoint_temperature_difference_range_2_lower_limit.setter
    def dewpoint_temperature_difference_range_2_lower_limit(self, value=None):
        """  Corresponds to IDD Field `Dewpoint Temperature Difference Range 2 Lower Limit`

        Args:
            value (float): value for IDD Field `Dewpoint Temperature Difference Range 2 Lower Limit`
                Units: deltaC
                value >= -50.0
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
                                 'for field `dewpoint_temperature_difference_range_2_lower_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `dewpoint_temperature_difference_range_2_lower_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `dewpoint_temperature_difference_range_2_lower_limit`')
        self._data["Dewpoint Temperature Difference Range 2 Lower Limit"] = value

    @property
    def dewpoint_temperature_difference_range_2_upper_limit(self):
        """Get dewpoint_temperature_difference_range_2_upper_limit

        Returns:
            float: the value of `dewpoint_temperature_difference_range_2_upper_limit` or None if not set
        """
        return self._data["Dewpoint Temperature Difference Range 2 Upper Limit"]

    @dewpoint_temperature_difference_range_2_upper_limit.setter
    def dewpoint_temperature_difference_range_2_upper_limit(self, value=None):
        """  Corresponds to IDD Field `Dewpoint Temperature Difference Range 2 Upper Limit`

        Args:
            value (float): value for IDD Field `Dewpoint Temperature Difference Range 2 Upper Limit`
                Units: deltaC
                value >= -50.0
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
                                 'for field `dewpoint_temperature_difference_range_2_upper_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `dewpoint_temperature_difference_range_2_upper_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `dewpoint_temperature_difference_range_2_upper_limit`')
        self._data["Dewpoint Temperature Difference Range 2 Upper Limit"] = value

    @property
    def range_2_equipment_list_name(self):
        """Get range_2_equipment_list_name

        Returns:
            str: the value of `range_2_equipment_list_name` or None if not set
        """
        return self._data["Range 2 Equipment List Name"]

    @range_2_equipment_list_name.setter
    def range_2_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `Range 2 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 2 Equipment List Name`
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
                                 'for field `range_2_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_2_equipment_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `range_2_equipment_list_name`')
        self._data["Range 2 Equipment List Name"] = value

    @property
    def dewpoint_temperature_difference_range_3_lower_limit(self):
        """Get dewpoint_temperature_difference_range_3_lower_limit

        Returns:
            float: the value of `dewpoint_temperature_difference_range_3_lower_limit` or None if not set
        """
        return self._data["Dewpoint Temperature Difference Range 3 Lower Limit"]

    @dewpoint_temperature_difference_range_3_lower_limit.setter
    def dewpoint_temperature_difference_range_3_lower_limit(self, value=None):
        """  Corresponds to IDD Field `Dewpoint Temperature Difference Range 3 Lower Limit`

        Args:
            value (float): value for IDD Field `Dewpoint Temperature Difference Range 3 Lower Limit`
                Units: deltaC
                value >= -50.0
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
                                 'for field `dewpoint_temperature_difference_range_3_lower_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `dewpoint_temperature_difference_range_3_lower_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `dewpoint_temperature_difference_range_3_lower_limit`')
        self._data["Dewpoint Temperature Difference Range 3 Lower Limit"] = value

    @property
    def dewpoint_temperature_difference_range_3_upper_limit(self):
        """Get dewpoint_temperature_difference_range_3_upper_limit

        Returns:
            float: the value of `dewpoint_temperature_difference_range_3_upper_limit` or None if not set
        """
        return self._data["Dewpoint Temperature Difference Range 3 Upper Limit"]

    @dewpoint_temperature_difference_range_3_upper_limit.setter
    def dewpoint_temperature_difference_range_3_upper_limit(self, value=None):
        """  Corresponds to IDD Field `Dewpoint Temperature Difference Range 3 Upper Limit`

        Args:
            value (float): value for IDD Field `Dewpoint Temperature Difference Range 3 Upper Limit`
                Units: deltaC
                value >= -50.0
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
                                 'for field `dewpoint_temperature_difference_range_3_upper_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `dewpoint_temperature_difference_range_3_upper_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `dewpoint_temperature_difference_range_3_upper_limit`')
        self._data["Dewpoint Temperature Difference Range 3 Upper Limit"] = value

    @property
    def range_3_equipment_list_name(self):
        """Get range_3_equipment_list_name

        Returns:
            str: the value of `range_3_equipment_list_name` or None if not set
        """
        return self._data["Range 3 Equipment List Name"]

    @range_3_equipment_list_name.setter
    def range_3_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `Range 3 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 3 Equipment List Name`
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
                                 'for field `range_3_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_3_equipment_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `range_3_equipment_list_name`')
        self._data["Range 3 Equipment List Name"] = value

    @property
    def dewpoint_temperature_difference_range_4_lower_limit(self):
        """Get dewpoint_temperature_difference_range_4_lower_limit

        Returns:
            float: the value of `dewpoint_temperature_difference_range_4_lower_limit` or None if not set
        """
        return self._data["Dewpoint Temperature Difference Range 4 Lower Limit"]

    @dewpoint_temperature_difference_range_4_lower_limit.setter
    def dewpoint_temperature_difference_range_4_lower_limit(self, value=None):
        """  Corresponds to IDD Field `Dewpoint Temperature Difference Range 4 Lower Limit`

        Args:
            value (float): value for IDD Field `Dewpoint Temperature Difference Range 4 Lower Limit`
                Units: deltaC
                value >= -50.0
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
                                 'for field `dewpoint_temperature_difference_range_4_lower_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `dewpoint_temperature_difference_range_4_lower_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `dewpoint_temperature_difference_range_4_lower_limit`')
        self._data["Dewpoint Temperature Difference Range 4 Lower Limit"] = value

    @property
    def dewpoint_temperature_difference_range_4_upper_limit(self):
        """Get dewpoint_temperature_difference_range_4_upper_limit

        Returns:
            float: the value of `dewpoint_temperature_difference_range_4_upper_limit` or None if not set
        """
        return self._data["Dewpoint Temperature Difference Range 4 Upper Limit"]

    @dewpoint_temperature_difference_range_4_upper_limit.setter
    def dewpoint_temperature_difference_range_4_upper_limit(self, value=None):
        """  Corresponds to IDD Field `Dewpoint Temperature Difference Range 4 Upper Limit`

        Args:
            value (float): value for IDD Field `Dewpoint Temperature Difference Range 4 Upper Limit`
                Units: deltaC
                value >= -50.0
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
                                 'for field `dewpoint_temperature_difference_range_4_upper_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `dewpoint_temperature_difference_range_4_upper_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `dewpoint_temperature_difference_range_4_upper_limit`')
        self._data["Dewpoint Temperature Difference Range 4 Upper Limit"] = value

    @property
    def range_4_equipment_list_name(self):
        """Get range_4_equipment_list_name

        Returns:
            str: the value of `range_4_equipment_list_name` or None if not set
        """
        return self._data["Range 4 Equipment List Name"]

    @range_4_equipment_list_name.setter
    def range_4_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `Range 4 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 4 Equipment List Name`
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
                                 'for field `range_4_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_4_equipment_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `range_4_equipment_list_name`')
        self._data["Range 4 Equipment List Name"] = value

    @property
    def dewpoint_temperature_difference_range_5_lower_limit(self):
        """Get dewpoint_temperature_difference_range_5_lower_limit

        Returns:
            float: the value of `dewpoint_temperature_difference_range_5_lower_limit` or None if not set
        """
        return self._data["Dewpoint Temperature Difference Range 5 Lower Limit"]

    @dewpoint_temperature_difference_range_5_lower_limit.setter
    def dewpoint_temperature_difference_range_5_lower_limit(self, value=None):
        """  Corresponds to IDD Field `Dewpoint Temperature Difference Range 5 Lower Limit`

        Args:
            value (float): value for IDD Field `Dewpoint Temperature Difference Range 5 Lower Limit`
                Units: deltaC
                value >= -50.0
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
                                 'for field `dewpoint_temperature_difference_range_5_lower_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `dewpoint_temperature_difference_range_5_lower_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `dewpoint_temperature_difference_range_5_lower_limit`')
        self._data["Dewpoint Temperature Difference Range 5 Lower Limit"] = value

    @property
    def dewpoint_temperature_difference_range_5_upper_limit(self):
        """Get dewpoint_temperature_difference_range_5_upper_limit

        Returns:
            float: the value of `dewpoint_temperature_difference_range_5_upper_limit` or None if not set
        """
        return self._data["Dewpoint Temperature Difference Range 5 Upper Limit"]

    @dewpoint_temperature_difference_range_5_upper_limit.setter
    def dewpoint_temperature_difference_range_5_upper_limit(self, value=None):
        """  Corresponds to IDD Field `Dewpoint Temperature Difference Range 5 Upper Limit`

        Args:
            value (float): value for IDD Field `Dewpoint Temperature Difference Range 5 Upper Limit`
                Units: deltaC
                value >= -50.0
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
                                 'for field `dewpoint_temperature_difference_range_5_upper_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `dewpoint_temperature_difference_range_5_upper_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `dewpoint_temperature_difference_range_5_upper_limit`')
        self._data["Dewpoint Temperature Difference Range 5 Upper Limit"] = value

    @property
    def range_5_equipment_list_name(self):
        """Get range_5_equipment_list_name

        Returns:
            str: the value of `range_5_equipment_list_name` or None if not set
        """
        return self._data["Range 5 Equipment List Name"]

    @range_5_equipment_list_name.setter
    def range_5_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `Range 5 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 5 Equipment List Name`
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
                                 'for field `range_5_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_5_equipment_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `range_5_equipment_list_name`')
        self._data["Range 5 Equipment List Name"] = value

    @property
    def dewpoint_temperature_difference_range_6_lower_limit(self):
        """Get dewpoint_temperature_difference_range_6_lower_limit

        Returns:
            float: the value of `dewpoint_temperature_difference_range_6_lower_limit` or None if not set
        """
        return self._data["Dewpoint Temperature Difference Range 6 Lower Limit"]

    @dewpoint_temperature_difference_range_6_lower_limit.setter
    def dewpoint_temperature_difference_range_6_lower_limit(self, value=None):
        """  Corresponds to IDD Field `Dewpoint Temperature Difference Range 6 Lower Limit`

        Args:
            value (float): value for IDD Field `Dewpoint Temperature Difference Range 6 Lower Limit`
                Units: deltaC
                value >= -50.0
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
                                 'for field `dewpoint_temperature_difference_range_6_lower_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `dewpoint_temperature_difference_range_6_lower_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `dewpoint_temperature_difference_range_6_lower_limit`')
        self._data["Dewpoint Temperature Difference Range 6 Lower Limit"] = value

    @property
    def dewpoint_temperature_difference_range_6_upper_limit(self):
        """Get dewpoint_temperature_difference_range_6_upper_limit

        Returns:
            float: the value of `dewpoint_temperature_difference_range_6_upper_limit` or None if not set
        """
        return self._data["Dewpoint Temperature Difference Range 6 Upper Limit"]

    @dewpoint_temperature_difference_range_6_upper_limit.setter
    def dewpoint_temperature_difference_range_6_upper_limit(self, value=None):
        """  Corresponds to IDD Field `Dewpoint Temperature Difference Range 6 Upper Limit`

        Args:
            value (float): value for IDD Field `Dewpoint Temperature Difference Range 6 Upper Limit`
                Units: deltaC
                value >= -50.0
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
                                 'for field `dewpoint_temperature_difference_range_6_upper_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `dewpoint_temperature_difference_range_6_upper_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `dewpoint_temperature_difference_range_6_upper_limit`')
        self._data["Dewpoint Temperature Difference Range 6 Upper Limit"] = value

    @property
    def range_6_equipment_list_name(self):
        """Get range_6_equipment_list_name

        Returns:
            str: the value of `range_6_equipment_list_name` or None if not set
        """
        return self._data["Range 6 Equipment List Name"]

    @range_6_equipment_list_name.setter
    def range_6_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `Range 6 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 6 Equipment List Name`
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
                                 'for field `range_6_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_6_equipment_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `range_6_equipment_list_name`')
        self._data["Range 6 Equipment List Name"] = value

    @property
    def dewpoint_temperature_difference_range_7_lower_limit(self):
        """Get dewpoint_temperature_difference_range_7_lower_limit

        Returns:
            float: the value of `dewpoint_temperature_difference_range_7_lower_limit` or None if not set
        """
        return self._data["Dewpoint Temperature Difference Range 7 Lower Limit"]

    @dewpoint_temperature_difference_range_7_lower_limit.setter
    def dewpoint_temperature_difference_range_7_lower_limit(self, value=None):
        """  Corresponds to IDD Field `Dewpoint Temperature Difference Range 7 Lower Limit`

        Args:
            value (float): value for IDD Field `Dewpoint Temperature Difference Range 7 Lower Limit`
                Units: deltaC
                value >= -50.0
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
                                 'for field `dewpoint_temperature_difference_range_7_lower_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `dewpoint_temperature_difference_range_7_lower_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `dewpoint_temperature_difference_range_7_lower_limit`')
        self._data["Dewpoint Temperature Difference Range 7 Lower Limit"] = value

    @property
    def dewpoint_temperature_difference_range_7_upper_limit(self):
        """Get dewpoint_temperature_difference_range_7_upper_limit

        Returns:
            float: the value of `dewpoint_temperature_difference_range_7_upper_limit` or None if not set
        """
        return self._data["Dewpoint Temperature Difference Range 7 Upper Limit"]

    @dewpoint_temperature_difference_range_7_upper_limit.setter
    def dewpoint_temperature_difference_range_7_upper_limit(self, value=None):
        """  Corresponds to IDD Field `Dewpoint Temperature Difference Range 7 Upper Limit`

        Args:
            value (float): value for IDD Field `Dewpoint Temperature Difference Range 7 Upper Limit`
                Units: deltaC
                value >= -50.0
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
                                 'for field `dewpoint_temperature_difference_range_7_upper_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `dewpoint_temperature_difference_range_7_upper_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `dewpoint_temperature_difference_range_7_upper_limit`')
        self._data["Dewpoint Temperature Difference Range 7 Upper Limit"] = value

    @property
    def range_7_equipment_list_name(self):
        """Get range_7_equipment_list_name

        Returns:
            str: the value of `range_7_equipment_list_name` or None if not set
        """
        return self._data["Range 7 Equipment List Name"]

    @range_7_equipment_list_name.setter
    def range_7_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `Range 7 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 7 Equipment List Name`
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
                                 'for field `range_7_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_7_equipment_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `range_7_equipment_list_name`')
        self._data["Range 7 Equipment List Name"] = value

    @property
    def dewpoint_temperature_difference_range_8_lower_limit(self):
        """Get dewpoint_temperature_difference_range_8_lower_limit

        Returns:
            float: the value of `dewpoint_temperature_difference_range_8_lower_limit` or None if not set
        """
        return self._data["Dewpoint Temperature Difference Range 8 Lower Limit"]

    @dewpoint_temperature_difference_range_8_lower_limit.setter
    def dewpoint_temperature_difference_range_8_lower_limit(self, value=None):
        """  Corresponds to IDD Field `Dewpoint Temperature Difference Range 8 Lower Limit`

        Args:
            value (float): value for IDD Field `Dewpoint Temperature Difference Range 8 Lower Limit`
                Units: deltaC
                value >= -50.0
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
                                 'for field `dewpoint_temperature_difference_range_8_lower_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `dewpoint_temperature_difference_range_8_lower_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `dewpoint_temperature_difference_range_8_lower_limit`')
        self._data["Dewpoint Temperature Difference Range 8 Lower Limit"] = value

    @property
    def dewpoint_temperature_difference_range_8_upper_limit(self):
        """Get dewpoint_temperature_difference_range_8_upper_limit

        Returns:
            float: the value of `dewpoint_temperature_difference_range_8_upper_limit` or None if not set
        """
        return self._data["Dewpoint Temperature Difference Range 8 Upper Limit"]

    @dewpoint_temperature_difference_range_8_upper_limit.setter
    def dewpoint_temperature_difference_range_8_upper_limit(self, value=None):
        """  Corresponds to IDD Field `Dewpoint Temperature Difference Range 8 Upper Limit`

        Args:
            value (float): value for IDD Field `Dewpoint Temperature Difference Range 8 Upper Limit`
                Units: deltaC
                value >= -50.0
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
                                 'for field `dewpoint_temperature_difference_range_8_upper_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `dewpoint_temperature_difference_range_8_upper_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `dewpoint_temperature_difference_range_8_upper_limit`')
        self._data["Dewpoint Temperature Difference Range 8 Upper Limit"] = value

    @property
    def range_8_equipment_list_name(self):
        """Get range_8_equipment_list_name

        Returns:
            str: the value of `range_8_equipment_list_name` or None if not set
        """
        return self._data["Range 8 Equipment List Name"]

    @range_8_equipment_list_name.setter
    def range_8_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `Range 8 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 8 Equipment List Name`
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
                                 'for field `range_8_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_8_equipment_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `range_8_equipment_list_name`')
        self._data["Range 8 Equipment List Name"] = value

    @property
    def dewpoint_temperature_difference_range_9_lower_limit(self):
        """Get dewpoint_temperature_difference_range_9_lower_limit

        Returns:
            float: the value of `dewpoint_temperature_difference_range_9_lower_limit` or None if not set
        """
        return self._data["Dewpoint Temperature Difference Range 9 Lower Limit"]

    @dewpoint_temperature_difference_range_9_lower_limit.setter
    def dewpoint_temperature_difference_range_9_lower_limit(self, value=None):
        """  Corresponds to IDD Field `Dewpoint Temperature Difference Range 9 Lower Limit`

        Args:
            value (float): value for IDD Field `Dewpoint Temperature Difference Range 9 Lower Limit`
                Units: deltaC
                value >= -50.0
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
                                 'for field `dewpoint_temperature_difference_range_9_lower_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `dewpoint_temperature_difference_range_9_lower_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `dewpoint_temperature_difference_range_9_lower_limit`')
        self._data["Dewpoint Temperature Difference Range 9 Lower Limit"] = value

    @property
    def dewpoint_temperature_difference_range_9_upper_limit(self):
        """Get dewpoint_temperature_difference_range_9_upper_limit

        Returns:
            float: the value of `dewpoint_temperature_difference_range_9_upper_limit` or None if not set
        """
        return self._data["Dewpoint Temperature Difference Range 9 Upper Limit"]

    @dewpoint_temperature_difference_range_9_upper_limit.setter
    def dewpoint_temperature_difference_range_9_upper_limit(self, value=None):
        """  Corresponds to IDD Field `Dewpoint Temperature Difference Range 9 Upper Limit`

        Args:
            value (float): value for IDD Field `Dewpoint Temperature Difference Range 9 Upper Limit`
                Units: deltaC
                value >= -50.0
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
                                 'for field `dewpoint_temperature_difference_range_9_upper_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `dewpoint_temperature_difference_range_9_upper_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `dewpoint_temperature_difference_range_9_upper_limit`')
        self._data["Dewpoint Temperature Difference Range 9 Upper Limit"] = value

    @property
    def range_9_equipment_list_name(self):
        """Get range_9_equipment_list_name

        Returns:
            str: the value of `range_9_equipment_list_name` or None if not set
        """
        return self._data["Range 9 Equipment List Name"]

    @range_9_equipment_list_name.setter
    def range_9_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `Range 9 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 9 Equipment List Name`
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
                                 'for field `range_9_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_9_equipment_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `range_9_equipment_list_name`')
        self._data["Range 9 Equipment List Name"] = value

    @property
    def dewpoint_temperature_difference_range_10_lower_limit(self):
        """Get dewpoint_temperature_difference_range_10_lower_limit

        Returns:
            float: the value of `dewpoint_temperature_difference_range_10_lower_limit` or None if not set
        """
        return self._data["Dewpoint Temperature Difference Range 10 Lower Limit"]

    @dewpoint_temperature_difference_range_10_lower_limit.setter
    def dewpoint_temperature_difference_range_10_lower_limit(self, value=None):
        """  Corresponds to IDD Field `Dewpoint Temperature Difference Range 10 Lower Limit`

        Args:
            value (float): value for IDD Field `Dewpoint Temperature Difference Range 10 Lower Limit`
                Units: deltaC
                value >= -50.0
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
                                 'for field `dewpoint_temperature_difference_range_10_lower_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `dewpoint_temperature_difference_range_10_lower_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `dewpoint_temperature_difference_range_10_lower_limit`')
        self._data["Dewpoint Temperature Difference Range 10 Lower Limit"] = value

    @property
    def dewpoint_temperature_difference_range_10_upper_limit(self):
        """Get dewpoint_temperature_difference_range_10_upper_limit

        Returns:
            float: the value of `dewpoint_temperature_difference_range_10_upper_limit` or None if not set
        """
        return self._data["Dewpoint Temperature Difference Range 10 Upper Limit"]

    @dewpoint_temperature_difference_range_10_upper_limit.setter
    def dewpoint_temperature_difference_range_10_upper_limit(self, value=None):
        """  Corresponds to IDD Field `Dewpoint Temperature Difference Range 10 Upper Limit`

        Args:
            value (float): value for IDD Field `Dewpoint Temperature Difference Range 10 Upper Limit`
                Units: deltaC
                value >= -50.0
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
                                 'for field `dewpoint_temperature_difference_range_10_upper_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `dewpoint_temperature_difference_range_10_upper_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `dewpoint_temperature_difference_range_10_upper_limit`')
        self._data["Dewpoint Temperature Difference Range 10 Upper Limit"] = value

    @property
    def range_10_equipment_list_name(self):
        """Get range_10_equipment_list_name

        Returns:
            str: the value of `range_10_equipment_list_name` or None if not set
        """
        return self._data["Range 10 Equipment List Name"]

    @range_10_equipment_list_name.setter
    def range_10_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `Range 10 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 10 Equipment List Name`
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
                                 'for field `range_10_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_10_equipment_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `range_10_equipment_list_name`')
        self._data["Range 10 Equipment List Name"] = value

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

class PlantEquipmentOperationSchemes(object):
    """ Corresponds to IDD object `PlantEquipmentOperationSchemes`
        Operation schemes are listed in "priority" order.  Note that each scheme
        must address the entire load and/or condition ranges for the simulation.
        The actual one selected for use will be the first that is "Scheduled"
        on.  That is, if control scheme 1 is not "on" and control scheme 2
        is -- then control scheme 2 is selected.
        Only plant equipment should be listed on a Control Scheme for this item.
    
    """
    internal_name = "PlantEquipmentOperationSchemes"
    field_count = 25
    required_fields = ["Name", "Control Scheme 1 Object Type", "Control Scheme 1 Name", "Control Scheme 1 Schedule Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `PlantEquipmentOperationSchemes`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Control Scheme 1 Object Type"] = None
        self._data["Control Scheme 1 Name"] = None
        self._data["Control Scheme 1 Schedule Name"] = None
        self._data["Control Scheme 2 Object Type"] = None
        self._data["Control Scheme 2 Name"] = None
        self._data["Control Scheme 2 Schedule Name"] = None
        self._data["Control Scheme 3 Object Type"] = None
        self._data["Control Scheme 3 Name"] = None
        self._data["Control Scheme 3 Schedule Name"] = None
        self._data["Control Scheme 4 Object Type"] = None
        self._data["Control Scheme 4 Name"] = None
        self._data["Control Scheme 4 Schedule Name"] = None
        self._data["Control Scheme 5 Object Type"] = None
        self._data["Control Scheme 5 Name"] = None
        self._data["Control Scheme 5 Schedule Name"] = None
        self._data["Control Scheme 6 Object Type"] = None
        self._data["Control Scheme 6 Name"] = None
        self._data["Control Scheme 6 Schedule Name"] = None
        self._data["Control Scheme 7 Object Type"] = None
        self._data["Control Scheme 7 Name"] = None
        self._data["Control Scheme 7 Schedule Name"] = None
        self._data["Control Scheme 8 Object Type"] = None
        self._data["Control Scheme 8 Name"] = None
        self._data["Control Scheme 8 Schedule Name"] = None
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
            self.control_scheme_1_object_type = None
        else:
            self.control_scheme_1_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.control_scheme_1_name = None
        else:
            self.control_scheme_1_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.control_scheme_1_schedule_name = None
        else:
            self.control_scheme_1_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.control_scheme_2_object_type = None
        else:
            self.control_scheme_2_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.control_scheme_2_name = None
        else:
            self.control_scheme_2_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.control_scheme_2_schedule_name = None
        else:
            self.control_scheme_2_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.control_scheme_3_object_type = None
        else:
            self.control_scheme_3_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.control_scheme_3_name = None
        else:
            self.control_scheme_3_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.control_scheme_3_schedule_name = None
        else:
            self.control_scheme_3_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.control_scheme_4_object_type = None
        else:
            self.control_scheme_4_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.control_scheme_4_name = None
        else:
            self.control_scheme_4_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.control_scheme_4_schedule_name = None
        else:
            self.control_scheme_4_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.control_scheme_5_object_type = None
        else:
            self.control_scheme_5_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.control_scheme_5_name = None
        else:
            self.control_scheme_5_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.control_scheme_5_schedule_name = None
        else:
            self.control_scheme_5_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.control_scheme_6_object_type = None
        else:
            self.control_scheme_6_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.control_scheme_6_name = None
        else:
            self.control_scheme_6_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.control_scheme_6_schedule_name = None
        else:
            self.control_scheme_6_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.control_scheme_7_object_type = None
        else:
            self.control_scheme_7_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.control_scheme_7_name = None
        else:
            self.control_scheme_7_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.control_scheme_7_schedule_name = None
        else:
            self.control_scheme_7_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.control_scheme_8_object_type = None
        else:
            self.control_scheme_8_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.control_scheme_8_name = None
        else:
            self.control_scheme_8_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.control_scheme_8_schedule_name = None
        else:
            self.control_scheme_8_schedule_name = vals[i]
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
    def control_scheme_1_object_type(self):
        """Get control_scheme_1_object_type

        Returns:
            str: the value of `control_scheme_1_object_type` or None if not set
        """
        return self._data["Control Scheme 1 Object Type"]

    @control_scheme_1_object_type.setter
    def control_scheme_1_object_type(self, value=None):
        """  Corresponds to IDD Field `Control Scheme 1 Object Type`

        Args:
            value (str): value for IDD Field `Control Scheme 1 Object Type`
                Accepted values are:
                      - PlantEquipmentOperation:CoolingLoad
                      - PlantEquipmentOperation:HeatingLoad
                      - PlantEquipmentOperation:Uncontrolled
                      - PlantEquipmentOperation:ComponentSetpoint
                      - PlantEquipmentOperation:UserDefined
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
                                 'for field `control_scheme_1_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_scheme_1_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `control_scheme_1_object_type`')
            vals = {}
            vals["plantequipmentoperation:coolingload"] = "PlantEquipmentOperation:CoolingLoad"
            vals["plantequipmentoperation:heatingload"] = "PlantEquipmentOperation:HeatingLoad"
            vals["plantequipmentoperation:uncontrolled"] = "PlantEquipmentOperation:Uncontrolled"
            vals["plantequipmentoperation:componentsetpoint"] = "PlantEquipmentOperation:ComponentSetpoint"
            vals["plantequipmentoperation:userdefined"] = "PlantEquipmentOperation:UserDefined"
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
                                     'field `control_scheme_1_object_type`'.format(value))
            value = vals[value_lower]
        self._data["Control Scheme 1 Object Type"] = value

    @property
    def control_scheme_1_name(self):
        """Get control_scheme_1_name

        Returns:
            str: the value of `control_scheme_1_name` or None if not set
        """
        return self._data["Control Scheme 1 Name"]

    @control_scheme_1_name.setter
    def control_scheme_1_name(self, value=None):
        """  Corresponds to IDD Field `Control Scheme 1 Name`

        Args:
            value (str): value for IDD Field `Control Scheme 1 Name`
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
                                 'for field `control_scheme_1_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_scheme_1_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `control_scheme_1_name`')
        self._data["Control Scheme 1 Name"] = value

    @property
    def control_scheme_1_schedule_name(self):
        """Get control_scheme_1_schedule_name

        Returns:
            str: the value of `control_scheme_1_schedule_name` or None if not set
        """
        return self._data["Control Scheme 1 Schedule Name"]

    @control_scheme_1_schedule_name.setter
    def control_scheme_1_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Control Scheme 1 Schedule Name`

        Args:
            value (str): value for IDD Field `Control Scheme 1 Schedule Name`
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
                                 'for field `control_scheme_1_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_scheme_1_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `control_scheme_1_schedule_name`')
        self._data["Control Scheme 1 Schedule Name"] = value

    @property
    def control_scheme_2_object_type(self):
        """Get control_scheme_2_object_type

        Returns:
            str: the value of `control_scheme_2_object_type` or None if not set
        """
        return self._data["Control Scheme 2 Object Type"]

    @control_scheme_2_object_type.setter
    def control_scheme_2_object_type(self, value=None):
        """  Corresponds to IDD Field `Control Scheme 2 Object Type`

        Args:
            value (str): value for IDD Field `Control Scheme 2 Object Type`
                Accepted values are:
                      - PlantEquipmentOperation:CoolingLoad
                      - PlantEquipmentOperation:HeatingLoad
                      - PlantEquipmentOperation:Uncontrolled
                      - PlantEquipmentOperation:ComponentSetpoint
                      - PlantEquipmentOperation:UserDefined
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
                                 'for field `control_scheme_2_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_scheme_2_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `control_scheme_2_object_type`')
            vals = {}
            vals["plantequipmentoperation:coolingload"] = "PlantEquipmentOperation:CoolingLoad"
            vals["plantequipmentoperation:heatingload"] = "PlantEquipmentOperation:HeatingLoad"
            vals["plantequipmentoperation:uncontrolled"] = "PlantEquipmentOperation:Uncontrolled"
            vals["plantequipmentoperation:componentsetpoint"] = "PlantEquipmentOperation:ComponentSetpoint"
            vals["plantequipmentoperation:userdefined"] = "PlantEquipmentOperation:UserDefined"
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
                                     'field `control_scheme_2_object_type`'.format(value))
            value = vals[value_lower]
        self._data["Control Scheme 2 Object Type"] = value

    @property
    def control_scheme_2_name(self):
        """Get control_scheme_2_name

        Returns:
            str: the value of `control_scheme_2_name` or None if not set
        """
        return self._data["Control Scheme 2 Name"]

    @control_scheme_2_name.setter
    def control_scheme_2_name(self, value=None):
        """  Corresponds to IDD Field `Control Scheme 2 Name`

        Args:
            value (str): value for IDD Field `Control Scheme 2 Name`
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
                                 'for field `control_scheme_2_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_scheme_2_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `control_scheme_2_name`')
        self._data["Control Scheme 2 Name"] = value

    @property
    def control_scheme_2_schedule_name(self):
        """Get control_scheme_2_schedule_name

        Returns:
            str: the value of `control_scheme_2_schedule_name` or None if not set
        """
        return self._data["Control Scheme 2 Schedule Name"]

    @control_scheme_2_schedule_name.setter
    def control_scheme_2_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Control Scheme 2 Schedule Name`

        Args:
            value (str): value for IDD Field `Control Scheme 2 Schedule Name`
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
                                 'for field `control_scheme_2_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_scheme_2_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `control_scheme_2_schedule_name`')
        self._data["Control Scheme 2 Schedule Name"] = value

    @property
    def control_scheme_3_object_type(self):
        """Get control_scheme_3_object_type

        Returns:
            str: the value of `control_scheme_3_object_type` or None if not set
        """
        return self._data["Control Scheme 3 Object Type"]

    @control_scheme_3_object_type.setter
    def control_scheme_3_object_type(self, value=None):
        """  Corresponds to IDD Field `Control Scheme 3 Object Type`

        Args:
            value (str): value for IDD Field `Control Scheme 3 Object Type`
                Accepted values are:
                      - PlantEquipmentOperation:CoolingLoad
                      - PlantEquipmentOperation:HeatingLoad
                      - PlantEquipmentOperation:Uncontrolled
                      - PlantEquipmentOperation:ComponentSetpoint
                      - PlantEquipmentOperation:UserDefined
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
                                 'for field `control_scheme_3_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_scheme_3_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `control_scheme_3_object_type`')
            vals = {}
            vals["plantequipmentoperation:coolingload"] = "PlantEquipmentOperation:CoolingLoad"
            vals["plantequipmentoperation:heatingload"] = "PlantEquipmentOperation:HeatingLoad"
            vals["plantequipmentoperation:uncontrolled"] = "PlantEquipmentOperation:Uncontrolled"
            vals["plantequipmentoperation:componentsetpoint"] = "PlantEquipmentOperation:ComponentSetpoint"
            vals["plantequipmentoperation:userdefined"] = "PlantEquipmentOperation:UserDefined"
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
                                     'field `control_scheme_3_object_type`'.format(value))
            value = vals[value_lower]
        self._data["Control Scheme 3 Object Type"] = value

    @property
    def control_scheme_3_name(self):
        """Get control_scheme_3_name

        Returns:
            str: the value of `control_scheme_3_name` or None if not set
        """
        return self._data["Control Scheme 3 Name"]

    @control_scheme_3_name.setter
    def control_scheme_3_name(self, value=None):
        """  Corresponds to IDD Field `Control Scheme 3 Name`

        Args:
            value (str): value for IDD Field `Control Scheme 3 Name`
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
                                 'for field `control_scheme_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_scheme_3_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `control_scheme_3_name`')
        self._data["Control Scheme 3 Name"] = value

    @property
    def control_scheme_3_schedule_name(self):
        """Get control_scheme_3_schedule_name

        Returns:
            str: the value of `control_scheme_3_schedule_name` or None if not set
        """
        return self._data["Control Scheme 3 Schedule Name"]

    @control_scheme_3_schedule_name.setter
    def control_scheme_3_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Control Scheme 3 Schedule Name`

        Args:
            value (str): value for IDD Field `Control Scheme 3 Schedule Name`
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
                                 'for field `control_scheme_3_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_scheme_3_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `control_scheme_3_schedule_name`')
        self._data["Control Scheme 3 Schedule Name"] = value

    @property
    def control_scheme_4_object_type(self):
        """Get control_scheme_4_object_type

        Returns:
            str: the value of `control_scheme_4_object_type` or None if not set
        """
        return self._data["Control Scheme 4 Object Type"]

    @control_scheme_4_object_type.setter
    def control_scheme_4_object_type(self, value=None):
        """  Corresponds to IDD Field `Control Scheme 4 Object Type`

        Args:
            value (str): value for IDD Field `Control Scheme 4 Object Type`
                Accepted values are:
                      - PlantEquipmentOperation:CoolingLoad
                      - PlantEquipmentOperation:HeatingLoad
                      - PlantEquipmentOperation:Uncontrolled
                      - PlantEquipmentOperation:ComponentSetpoint
                      - PlantEquipmentOperation:UserDefined
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
                                 'for field `control_scheme_4_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_scheme_4_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `control_scheme_4_object_type`')
            vals = {}
            vals["plantequipmentoperation:coolingload"] = "PlantEquipmentOperation:CoolingLoad"
            vals["plantequipmentoperation:heatingload"] = "PlantEquipmentOperation:HeatingLoad"
            vals["plantequipmentoperation:uncontrolled"] = "PlantEquipmentOperation:Uncontrolled"
            vals["plantequipmentoperation:componentsetpoint"] = "PlantEquipmentOperation:ComponentSetpoint"
            vals["plantequipmentoperation:userdefined"] = "PlantEquipmentOperation:UserDefined"
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
                                     'field `control_scheme_4_object_type`'.format(value))
            value = vals[value_lower]
        self._data["Control Scheme 4 Object Type"] = value

    @property
    def control_scheme_4_name(self):
        """Get control_scheme_4_name

        Returns:
            str: the value of `control_scheme_4_name` or None if not set
        """
        return self._data["Control Scheme 4 Name"]

    @control_scheme_4_name.setter
    def control_scheme_4_name(self, value=None):
        """  Corresponds to IDD Field `Control Scheme 4 Name`

        Args:
            value (str): value for IDD Field `Control Scheme 4 Name`
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
                                 'for field `control_scheme_4_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_scheme_4_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `control_scheme_4_name`')
        self._data["Control Scheme 4 Name"] = value

    @property
    def control_scheme_4_schedule_name(self):
        """Get control_scheme_4_schedule_name

        Returns:
            str: the value of `control_scheme_4_schedule_name` or None if not set
        """
        return self._data["Control Scheme 4 Schedule Name"]

    @control_scheme_4_schedule_name.setter
    def control_scheme_4_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Control Scheme 4 Schedule Name`

        Args:
            value (str): value for IDD Field `Control Scheme 4 Schedule Name`
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
                                 'for field `control_scheme_4_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_scheme_4_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `control_scheme_4_schedule_name`')
        self._data["Control Scheme 4 Schedule Name"] = value

    @property
    def control_scheme_5_object_type(self):
        """Get control_scheme_5_object_type

        Returns:
            str: the value of `control_scheme_5_object_type` or None if not set
        """
        return self._data["Control Scheme 5 Object Type"]

    @control_scheme_5_object_type.setter
    def control_scheme_5_object_type(self, value=None):
        """  Corresponds to IDD Field `Control Scheme 5 Object Type`

        Args:
            value (str): value for IDD Field `Control Scheme 5 Object Type`
                Accepted values are:
                      - PlantEquipmentOperation:CoolingLoad
                      - PlantEquipmentOperation:HeatingLoad
                      - PlantEquipmentOperation:Uncontrolled
                      - PlantEquipmentOperation:ComponentSetpoint
                      - PlantEquipmentOperation:UserDefined
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
                                 'for field `control_scheme_5_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_scheme_5_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `control_scheme_5_object_type`')
            vals = {}
            vals["plantequipmentoperation:coolingload"] = "PlantEquipmentOperation:CoolingLoad"
            vals["plantequipmentoperation:heatingload"] = "PlantEquipmentOperation:HeatingLoad"
            vals["plantequipmentoperation:uncontrolled"] = "PlantEquipmentOperation:Uncontrolled"
            vals["plantequipmentoperation:componentsetpoint"] = "PlantEquipmentOperation:ComponentSetpoint"
            vals["plantequipmentoperation:userdefined"] = "PlantEquipmentOperation:UserDefined"
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
                                     'field `control_scheme_5_object_type`'.format(value))
            value = vals[value_lower]
        self._data["Control Scheme 5 Object Type"] = value

    @property
    def control_scheme_5_name(self):
        """Get control_scheme_5_name

        Returns:
            str: the value of `control_scheme_5_name` or None if not set
        """
        return self._data["Control Scheme 5 Name"]

    @control_scheme_5_name.setter
    def control_scheme_5_name(self, value=None):
        """  Corresponds to IDD Field `Control Scheme 5 Name`

        Args:
            value (str): value for IDD Field `Control Scheme 5 Name`
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
                                 'for field `control_scheme_5_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_scheme_5_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `control_scheme_5_name`')
        self._data["Control Scheme 5 Name"] = value

    @property
    def control_scheme_5_schedule_name(self):
        """Get control_scheme_5_schedule_name

        Returns:
            str: the value of `control_scheme_5_schedule_name` or None if not set
        """
        return self._data["Control Scheme 5 Schedule Name"]

    @control_scheme_5_schedule_name.setter
    def control_scheme_5_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Control Scheme 5 Schedule Name`

        Args:
            value (str): value for IDD Field `Control Scheme 5 Schedule Name`
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
                                 'for field `control_scheme_5_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_scheme_5_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `control_scheme_5_schedule_name`')
        self._data["Control Scheme 5 Schedule Name"] = value

    @property
    def control_scheme_6_object_type(self):
        """Get control_scheme_6_object_type

        Returns:
            str: the value of `control_scheme_6_object_type` or None if not set
        """
        return self._data["Control Scheme 6 Object Type"]

    @control_scheme_6_object_type.setter
    def control_scheme_6_object_type(self, value=None):
        """  Corresponds to IDD Field `Control Scheme 6 Object Type`

        Args:
            value (str): value for IDD Field `Control Scheme 6 Object Type`
                Accepted values are:
                      - PlantEquipmentOperation:CoolingLoad
                      - PlantEquipmentOperation:HeatingLoad
                      - PlantEquipmentOperation:Uncontrolled
                      - PlantEquipmentOperation:ComponentSetpoint
                      - PlantEquipmentOperation:UserDefined
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
                                 'for field `control_scheme_6_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_scheme_6_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `control_scheme_6_object_type`')
            vals = {}
            vals["plantequipmentoperation:coolingload"] = "PlantEquipmentOperation:CoolingLoad"
            vals["plantequipmentoperation:heatingload"] = "PlantEquipmentOperation:HeatingLoad"
            vals["plantequipmentoperation:uncontrolled"] = "PlantEquipmentOperation:Uncontrolled"
            vals["plantequipmentoperation:componentsetpoint"] = "PlantEquipmentOperation:ComponentSetpoint"
            vals["plantequipmentoperation:userdefined"] = "PlantEquipmentOperation:UserDefined"
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
                                     'field `control_scheme_6_object_type`'.format(value))
            value = vals[value_lower]
        self._data["Control Scheme 6 Object Type"] = value

    @property
    def control_scheme_6_name(self):
        """Get control_scheme_6_name

        Returns:
            str: the value of `control_scheme_6_name` or None if not set
        """
        return self._data["Control Scheme 6 Name"]

    @control_scheme_6_name.setter
    def control_scheme_6_name(self, value=None):
        """  Corresponds to IDD Field `Control Scheme 6 Name`

        Args:
            value (str): value for IDD Field `Control Scheme 6 Name`
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
                                 'for field `control_scheme_6_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_scheme_6_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `control_scheme_6_name`')
        self._data["Control Scheme 6 Name"] = value

    @property
    def control_scheme_6_schedule_name(self):
        """Get control_scheme_6_schedule_name

        Returns:
            str: the value of `control_scheme_6_schedule_name` or None if not set
        """
        return self._data["Control Scheme 6 Schedule Name"]

    @control_scheme_6_schedule_name.setter
    def control_scheme_6_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Control Scheme 6 Schedule Name`

        Args:
            value (str): value for IDD Field `Control Scheme 6 Schedule Name`
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
                                 'for field `control_scheme_6_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_scheme_6_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `control_scheme_6_schedule_name`')
        self._data["Control Scheme 6 Schedule Name"] = value

    @property
    def control_scheme_7_object_type(self):
        """Get control_scheme_7_object_type

        Returns:
            str: the value of `control_scheme_7_object_type` or None if not set
        """
        return self._data["Control Scheme 7 Object Type"]

    @control_scheme_7_object_type.setter
    def control_scheme_7_object_type(self, value=None):
        """  Corresponds to IDD Field `Control Scheme 7 Object Type`

        Args:
            value (str): value for IDD Field `Control Scheme 7 Object Type`
                Accepted values are:
                      - PlantEquipmentOperation:CoolingLoad
                      - PlantEquipmentOperation:HeatingLoad
                      - PlantEquipmentOperation:Uncontrolled
                      - PlantEquipmentOperation:ComponentSetpoint
                      - PlantEquipmentOperation:UserDefined
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
                                 'for field `control_scheme_7_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_scheme_7_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `control_scheme_7_object_type`')
            vals = {}
            vals["plantequipmentoperation:coolingload"] = "PlantEquipmentOperation:CoolingLoad"
            vals["plantequipmentoperation:heatingload"] = "PlantEquipmentOperation:HeatingLoad"
            vals["plantequipmentoperation:uncontrolled"] = "PlantEquipmentOperation:Uncontrolled"
            vals["plantequipmentoperation:componentsetpoint"] = "PlantEquipmentOperation:ComponentSetpoint"
            vals["plantequipmentoperation:userdefined"] = "PlantEquipmentOperation:UserDefined"
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
                                     'field `control_scheme_7_object_type`'.format(value))
            value = vals[value_lower]
        self._data["Control Scheme 7 Object Type"] = value

    @property
    def control_scheme_7_name(self):
        """Get control_scheme_7_name

        Returns:
            str: the value of `control_scheme_7_name` or None if not set
        """
        return self._data["Control Scheme 7 Name"]

    @control_scheme_7_name.setter
    def control_scheme_7_name(self, value=None):
        """  Corresponds to IDD Field `Control Scheme 7 Name`

        Args:
            value (str): value for IDD Field `Control Scheme 7 Name`
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
                                 'for field `control_scheme_7_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_scheme_7_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `control_scheme_7_name`')
        self._data["Control Scheme 7 Name"] = value

    @property
    def control_scheme_7_schedule_name(self):
        """Get control_scheme_7_schedule_name

        Returns:
            str: the value of `control_scheme_7_schedule_name` or None if not set
        """
        return self._data["Control Scheme 7 Schedule Name"]

    @control_scheme_7_schedule_name.setter
    def control_scheme_7_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Control Scheme 7 Schedule Name`

        Args:
            value (str): value for IDD Field `Control Scheme 7 Schedule Name`
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
                                 'for field `control_scheme_7_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_scheme_7_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `control_scheme_7_schedule_name`')
        self._data["Control Scheme 7 Schedule Name"] = value

    @property
    def control_scheme_8_object_type(self):
        """Get control_scheme_8_object_type

        Returns:
            str: the value of `control_scheme_8_object_type` or None if not set
        """
        return self._data["Control Scheme 8 Object Type"]

    @control_scheme_8_object_type.setter
    def control_scheme_8_object_type(self, value=None):
        """  Corresponds to IDD Field `Control Scheme 8 Object Type`

        Args:
            value (str): value for IDD Field `Control Scheme 8 Object Type`
                Accepted values are:
                      - PlantEquipmentOperation:CoolingLoad
                      - PlantEquipmentOperation:HeatingLoad
                      - PlantEquipmentOperation:Uncontrolled
                      - PlantEquipmentOperation:ComponentSetpoint
                      - PlantEquipmentOperation:UserDefined
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
                                 'for field `control_scheme_8_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_scheme_8_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `control_scheme_8_object_type`')
            vals = {}
            vals["plantequipmentoperation:coolingload"] = "PlantEquipmentOperation:CoolingLoad"
            vals["plantequipmentoperation:heatingload"] = "PlantEquipmentOperation:HeatingLoad"
            vals["plantequipmentoperation:uncontrolled"] = "PlantEquipmentOperation:Uncontrolled"
            vals["plantequipmentoperation:componentsetpoint"] = "PlantEquipmentOperation:ComponentSetpoint"
            vals["plantequipmentoperation:userdefined"] = "PlantEquipmentOperation:UserDefined"
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
                                     'field `control_scheme_8_object_type`'.format(value))
            value = vals[value_lower]
        self._data["Control Scheme 8 Object Type"] = value

    @property
    def control_scheme_8_name(self):
        """Get control_scheme_8_name

        Returns:
            str: the value of `control_scheme_8_name` or None if not set
        """
        return self._data["Control Scheme 8 Name"]

    @control_scheme_8_name.setter
    def control_scheme_8_name(self, value=None):
        """  Corresponds to IDD Field `Control Scheme 8 Name`

        Args:
            value (str): value for IDD Field `Control Scheme 8 Name`
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
                                 'for field `control_scheme_8_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_scheme_8_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `control_scheme_8_name`')
        self._data["Control Scheme 8 Name"] = value

    @property
    def control_scheme_8_schedule_name(self):
        """Get control_scheme_8_schedule_name

        Returns:
            str: the value of `control_scheme_8_schedule_name` or None if not set
        """
        return self._data["Control Scheme 8 Schedule Name"]

    @control_scheme_8_schedule_name.setter
    def control_scheme_8_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Control Scheme 8 Schedule Name`

        Args:
            value (str): value for IDD Field `Control Scheme 8 Schedule Name`
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
                                 'for field `control_scheme_8_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_scheme_8_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `control_scheme_8_schedule_name`')
        self._data["Control Scheme 8 Schedule Name"] = value

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

class CondenserEquipmentOperationSchemes(object):
    """ Corresponds to IDD object `CondenserEquipmentOperationSchemes`
        Operation schemes are listed in "priority" order.  Note that each scheme
        must address the entire load and/or condition ranges for the simulation.
        The actual one selected for use will be the first that is "Scheduled"
        on.  That is, if control scheme 1 is not "on" and control scheme 2
        is -- then control scheme 2 is selected.
        Only condenser equipment should be listed on a Control Scheme for this item.
    
    """
    internal_name = "CondenserEquipmentOperationSchemes"
    field_count = 25
    required_fields = ["Name", "Control Scheme 1 Object Type", "Control Scheme 1 Name", "Control Scheme 1 Schedule Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `CondenserEquipmentOperationSchemes`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Control Scheme 1 Object Type"] = None
        self._data["Control Scheme 1 Name"] = None
        self._data["Control Scheme 1 Schedule Name"] = None
        self._data["Control Scheme 2 Object Type"] = None
        self._data["Control Scheme 2 Name"] = None
        self._data["Control Scheme 2 Schedule Name"] = None
        self._data["Control Scheme 3 Object Type"] = None
        self._data["Control Scheme 3 Name"] = None
        self._data["Control Scheme 3 Schedule Name"] = None
        self._data["Control Scheme 4 Object Type"] = None
        self._data["Control Scheme 4 Name"] = None
        self._data["Control Scheme 4 Schedule Name"] = None
        self._data["Control Scheme 5 Object Type"] = None
        self._data["Control Scheme 5 Name"] = None
        self._data["Control Scheme 5 Schedule Name"] = None
        self._data["Control Scheme 6 Object Type"] = None
        self._data["Control Scheme 6 Name"] = None
        self._data["Control Scheme 6 Schedule Name"] = None
        self._data["Control Scheme 7 Object Type"] = None
        self._data["Control Scheme 7 Name"] = None
        self._data["Control Scheme 7 Schedule Name"] = None
        self._data["Control Scheme 8 Object Type"] = None
        self._data["Control Scheme 8 Name"] = None
        self._data["Control Scheme 8 Schedule Name"] = None
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
            self.control_scheme_1_object_type = None
        else:
            self.control_scheme_1_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.control_scheme_1_name = None
        else:
            self.control_scheme_1_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.control_scheme_1_schedule_name = None
        else:
            self.control_scheme_1_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.control_scheme_2_object_type = None
        else:
            self.control_scheme_2_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.control_scheme_2_name = None
        else:
            self.control_scheme_2_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.control_scheme_2_schedule_name = None
        else:
            self.control_scheme_2_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.control_scheme_3_object_type = None
        else:
            self.control_scheme_3_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.control_scheme_3_name = None
        else:
            self.control_scheme_3_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.control_scheme_3_schedule_name = None
        else:
            self.control_scheme_3_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.control_scheme_4_object_type = None
        else:
            self.control_scheme_4_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.control_scheme_4_name = None
        else:
            self.control_scheme_4_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.control_scheme_4_schedule_name = None
        else:
            self.control_scheme_4_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.control_scheme_5_object_type = None
        else:
            self.control_scheme_5_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.control_scheme_5_name = None
        else:
            self.control_scheme_5_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.control_scheme_5_schedule_name = None
        else:
            self.control_scheme_5_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.control_scheme_6_object_type = None
        else:
            self.control_scheme_6_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.control_scheme_6_name = None
        else:
            self.control_scheme_6_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.control_scheme_6_schedule_name = None
        else:
            self.control_scheme_6_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.control_scheme_7_object_type = None
        else:
            self.control_scheme_7_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.control_scheme_7_name = None
        else:
            self.control_scheme_7_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.control_scheme_7_schedule_name = None
        else:
            self.control_scheme_7_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.control_scheme_8_object_type = None
        else:
            self.control_scheme_8_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.control_scheme_8_name = None
        else:
            self.control_scheme_8_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.control_scheme_8_schedule_name = None
        else:
            self.control_scheme_8_schedule_name = vals[i]
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
    def control_scheme_1_object_type(self):
        """Get control_scheme_1_object_type

        Returns:
            str: the value of `control_scheme_1_object_type` or None if not set
        """
        return self._data["Control Scheme 1 Object Type"]

    @control_scheme_1_object_type.setter
    def control_scheme_1_object_type(self, value=None):
        """  Corresponds to IDD Field `Control Scheme 1 Object Type`

        Args:
            value (str): value for IDD Field `Control Scheme 1 Object Type`
                Accepted values are:
                      - PlantEquipmentOperation:Uncontrolled
                      - PlantEquipmentOperation:CoolingLoad
                      - PlantEquipmentOperation:HeatingLoad
                      - PlantEquipmentOperation:OutdoorDryBulb
                      - PlantEquipmentOperation:OutdoorWetBulb
                      - PlantEquipmentOperation:OutdoorRelativeHumidity
                      - PlantEquipmentOperation:OutdoorDewpoint
                      - PlantEquipmentOperation:OutdoorDryBulbDifference
                      - PlantEquipmentOperation:OutdoorWetBulbDifference
                      - PlantEquipmentOperation:OutdoorDewpointDifference
                      - PlantEquipmentOperation:UserDefined
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
                                 'for field `control_scheme_1_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_scheme_1_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `control_scheme_1_object_type`')
            vals = {}
            vals["plantequipmentoperation:uncontrolled"] = "PlantEquipmentOperation:Uncontrolled"
            vals["plantequipmentoperation:coolingload"] = "PlantEquipmentOperation:CoolingLoad"
            vals["plantequipmentoperation:heatingload"] = "PlantEquipmentOperation:HeatingLoad"
            vals["plantequipmentoperation:outdoordrybulb"] = "PlantEquipmentOperation:OutdoorDryBulb"
            vals["plantequipmentoperation:outdoorwetbulb"] = "PlantEquipmentOperation:OutdoorWetBulb"
            vals["plantequipmentoperation:outdoorrelativehumidity"] = "PlantEquipmentOperation:OutdoorRelativeHumidity"
            vals["plantequipmentoperation:outdoordewpoint"] = "PlantEquipmentOperation:OutdoorDewpoint"
            vals["plantequipmentoperation:outdoordrybulbdifference"] = "PlantEquipmentOperation:OutdoorDryBulbDifference"
            vals["plantequipmentoperation:outdoorwetbulbdifference"] = "PlantEquipmentOperation:OutdoorWetBulbDifference"
            vals["plantequipmentoperation:outdoordewpointdifference"] = "PlantEquipmentOperation:OutdoorDewpointDifference"
            vals["plantequipmentoperation:userdefined"] = "PlantEquipmentOperation:UserDefined"
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
                                     'field `control_scheme_1_object_type`'.format(value))
            value = vals[value_lower]
        self._data["Control Scheme 1 Object Type"] = value

    @property
    def control_scheme_1_name(self):
        """Get control_scheme_1_name

        Returns:
            str: the value of `control_scheme_1_name` or None if not set
        """
        return self._data["Control Scheme 1 Name"]

    @control_scheme_1_name.setter
    def control_scheme_1_name(self, value=None):
        """  Corresponds to IDD Field `Control Scheme 1 Name`

        Args:
            value (str): value for IDD Field `Control Scheme 1 Name`
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
                                 'for field `control_scheme_1_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_scheme_1_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `control_scheme_1_name`')
        self._data["Control Scheme 1 Name"] = value

    @property
    def control_scheme_1_schedule_name(self):
        """Get control_scheme_1_schedule_name

        Returns:
            str: the value of `control_scheme_1_schedule_name` or None if not set
        """
        return self._data["Control Scheme 1 Schedule Name"]

    @control_scheme_1_schedule_name.setter
    def control_scheme_1_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Control Scheme 1 Schedule Name`

        Args:
            value (str): value for IDD Field `Control Scheme 1 Schedule Name`
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
                                 'for field `control_scheme_1_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_scheme_1_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `control_scheme_1_schedule_name`')
        self._data["Control Scheme 1 Schedule Name"] = value

    @property
    def control_scheme_2_object_type(self):
        """Get control_scheme_2_object_type

        Returns:
            str: the value of `control_scheme_2_object_type` or None if not set
        """
        return self._data["Control Scheme 2 Object Type"]

    @control_scheme_2_object_type.setter
    def control_scheme_2_object_type(self, value=None):
        """  Corresponds to IDD Field `Control Scheme 2 Object Type`

        Args:
            value (str): value for IDD Field `Control Scheme 2 Object Type`
                Accepted values are:
                      - PlantEquipmentOperation:Uncontrolled
                      - PlantEquipmentOperation:CoolingLoad
                      - PlantEquipmentOperation:HeatingLoad
                      - PlantEquipmentOperation:OutdoorDryBulb
                      - PlantEquipmentOperation:OutdoorWetBulb
                      - PlantEquipmentOperation:OutdoorRelativeHumidity
                      - PlantEquipmentOperation:OutdoorDewpoint
                      - PlantEquipmentOperation:OutdoorDryBulbDifference
                      - PlantEquipmentOperation:OutdoorWetBulbDifference
                      - PlantEquipmentOperation:OutdoorDewpointDifference
                      - PlantEquipmentOperation:UserDefined
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
                                 'for field `control_scheme_2_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_scheme_2_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `control_scheme_2_object_type`')
            vals = {}
            vals["plantequipmentoperation:uncontrolled"] = "PlantEquipmentOperation:Uncontrolled"
            vals["plantequipmentoperation:coolingload"] = "PlantEquipmentOperation:CoolingLoad"
            vals["plantequipmentoperation:heatingload"] = "PlantEquipmentOperation:HeatingLoad"
            vals["plantequipmentoperation:outdoordrybulb"] = "PlantEquipmentOperation:OutdoorDryBulb"
            vals["plantequipmentoperation:outdoorwetbulb"] = "PlantEquipmentOperation:OutdoorWetBulb"
            vals["plantequipmentoperation:outdoorrelativehumidity"] = "PlantEquipmentOperation:OutdoorRelativeHumidity"
            vals["plantequipmentoperation:outdoordewpoint"] = "PlantEquipmentOperation:OutdoorDewpoint"
            vals["plantequipmentoperation:outdoordrybulbdifference"] = "PlantEquipmentOperation:OutdoorDryBulbDifference"
            vals["plantequipmentoperation:outdoorwetbulbdifference"] = "PlantEquipmentOperation:OutdoorWetBulbDifference"
            vals["plantequipmentoperation:outdoordewpointdifference"] = "PlantEquipmentOperation:OutdoorDewpointDifference"
            vals["plantequipmentoperation:userdefined"] = "PlantEquipmentOperation:UserDefined"
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
                                     'field `control_scheme_2_object_type`'.format(value))
            value = vals[value_lower]
        self._data["Control Scheme 2 Object Type"] = value

    @property
    def control_scheme_2_name(self):
        """Get control_scheme_2_name

        Returns:
            str: the value of `control_scheme_2_name` or None if not set
        """
        return self._data["Control Scheme 2 Name"]

    @control_scheme_2_name.setter
    def control_scheme_2_name(self, value=None):
        """  Corresponds to IDD Field `Control Scheme 2 Name`

        Args:
            value (str): value for IDD Field `Control Scheme 2 Name`
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
                                 'for field `control_scheme_2_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_scheme_2_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `control_scheme_2_name`')
        self._data["Control Scheme 2 Name"] = value

    @property
    def control_scheme_2_schedule_name(self):
        """Get control_scheme_2_schedule_name

        Returns:
            str: the value of `control_scheme_2_schedule_name` or None if not set
        """
        return self._data["Control Scheme 2 Schedule Name"]

    @control_scheme_2_schedule_name.setter
    def control_scheme_2_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Control Scheme 2 Schedule Name`

        Args:
            value (str): value for IDD Field `Control Scheme 2 Schedule Name`
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
                                 'for field `control_scheme_2_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_scheme_2_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `control_scheme_2_schedule_name`')
        self._data["Control Scheme 2 Schedule Name"] = value

    @property
    def control_scheme_3_object_type(self):
        """Get control_scheme_3_object_type

        Returns:
            str: the value of `control_scheme_3_object_type` or None if not set
        """
        return self._data["Control Scheme 3 Object Type"]

    @control_scheme_3_object_type.setter
    def control_scheme_3_object_type(self, value=None):
        """  Corresponds to IDD Field `Control Scheme 3 Object Type`

        Args:
            value (str): value for IDD Field `Control Scheme 3 Object Type`
                Accepted values are:
                      - PlantEquipmentOperation:Uncontrolled
                      - PlantEquipmentOperation:CoolingLoad
                      - PlantEquipmentOperation:HeatingLoad
                      - PlantEquipmentOperation:OutdoorDryBulb
                      - PlantEquipmentOperation:OutdoorWetBulb
                      - PlantEquipmentOperation:OutdoorRelativeHumidity
                      - PlantEquipmentOperation:OutdoorDewpoint
                      - PlantEquipmentOperation:OutdoorDryBulbDifference
                      - PlantEquipmentOperation:OutdoorWetBulbDifference
                      - PlantEquipmentOperation:OutdoorDewpointDifference
                      - PlantEquipmentOperation:UserDefined
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
                                 'for field `control_scheme_3_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_scheme_3_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `control_scheme_3_object_type`')
            vals = {}
            vals["plantequipmentoperation:uncontrolled"] = "PlantEquipmentOperation:Uncontrolled"
            vals["plantequipmentoperation:coolingload"] = "PlantEquipmentOperation:CoolingLoad"
            vals["plantequipmentoperation:heatingload"] = "PlantEquipmentOperation:HeatingLoad"
            vals["plantequipmentoperation:outdoordrybulb"] = "PlantEquipmentOperation:OutdoorDryBulb"
            vals["plantequipmentoperation:outdoorwetbulb"] = "PlantEquipmentOperation:OutdoorWetBulb"
            vals["plantequipmentoperation:outdoorrelativehumidity"] = "PlantEquipmentOperation:OutdoorRelativeHumidity"
            vals["plantequipmentoperation:outdoordewpoint"] = "PlantEquipmentOperation:OutdoorDewpoint"
            vals["plantequipmentoperation:outdoordrybulbdifference"] = "PlantEquipmentOperation:OutdoorDryBulbDifference"
            vals["plantequipmentoperation:outdoorwetbulbdifference"] = "PlantEquipmentOperation:OutdoorWetBulbDifference"
            vals["plantequipmentoperation:outdoordewpointdifference"] = "PlantEquipmentOperation:OutdoorDewpointDifference"
            vals["plantequipmentoperation:userdefined"] = "PlantEquipmentOperation:UserDefined"
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
                                     'field `control_scheme_3_object_type`'.format(value))
            value = vals[value_lower]
        self._data["Control Scheme 3 Object Type"] = value

    @property
    def control_scheme_3_name(self):
        """Get control_scheme_3_name

        Returns:
            str: the value of `control_scheme_3_name` or None if not set
        """
        return self._data["Control Scheme 3 Name"]

    @control_scheme_3_name.setter
    def control_scheme_3_name(self, value=None):
        """  Corresponds to IDD Field `Control Scheme 3 Name`

        Args:
            value (str): value for IDD Field `Control Scheme 3 Name`
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
                                 'for field `control_scheme_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_scheme_3_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `control_scheme_3_name`')
        self._data["Control Scheme 3 Name"] = value

    @property
    def control_scheme_3_schedule_name(self):
        """Get control_scheme_3_schedule_name

        Returns:
            str: the value of `control_scheme_3_schedule_name` or None if not set
        """
        return self._data["Control Scheme 3 Schedule Name"]

    @control_scheme_3_schedule_name.setter
    def control_scheme_3_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Control Scheme 3 Schedule Name`

        Args:
            value (str): value for IDD Field `Control Scheme 3 Schedule Name`
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
                                 'for field `control_scheme_3_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_scheme_3_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `control_scheme_3_schedule_name`')
        self._data["Control Scheme 3 Schedule Name"] = value

    @property
    def control_scheme_4_object_type(self):
        """Get control_scheme_4_object_type

        Returns:
            str: the value of `control_scheme_4_object_type` or None if not set
        """
        return self._data["Control Scheme 4 Object Type"]

    @control_scheme_4_object_type.setter
    def control_scheme_4_object_type(self, value=None):
        """  Corresponds to IDD Field `Control Scheme 4 Object Type`

        Args:
            value (str): value for IDD Field `Control Scheme 4 Object Type`
                Accepted values are:
                      - PlantEquipmentOperation:Uncontrolled
                      - PlantEquipmentOperation:CoolingLoad
                      - PlantEquipmentOperation:HeatingLoad
                      - PlantEquipmentOperation:OutdoorDryBulb
                      - PlantEquipmentOperation:OutdoorWetBulb
                      - PlantEquipmentOperation:OutdoorRelativeHumidity
                      - PlantEquipmentOperation:OutdoorDewpoint
                      - PlantEquipmentOperation:OutdoorDryBulbDifference
                      - PlantEquipmentOperation:OutdoorWetBulbDifference
                      - PlantEquipmentOperation:OutdoorDewpointDifference
                      - PlantEquipmentOperation:UserDefined
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
                                 'for field `control_scheme_4_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_scheme_4_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `control_scheme_4_object_type`')
            vals = {}
            vals["plantequipmentoperation:uncontrolled"] = "PlantEquipmentOperation:Uncontrolled"
            vals["plantequipmentoperation:coolingload"] = "PlantEquipmentOperation:CoolingLoad"
            vals["plantequipmentoperation:heatingload"] = "PlantEquipmentOperation:HeatingLoad"
            vals["plantequipmentoperation:outdoordrybulb"] = "PlantEquipmentOperation:OutdoorDryBulb"
            vals["plantequipmentoperation:outdoorwetbulb"] = "PlantEquipmentOperation:OutdoorWetBulb"
            vals["plantequipmentoperation:outdoorrelativehumidity"] = "PlantEquipmentOperation:OutdoorRelativeHumidity"
            vals["plantequipmentoperation:outdoordewpoint"] = "PlantEquipmentOperation:OutdoorDewpoint"
            vals["plantequipmentoperation:outdoordrybulbdifference"] = "PlantEquipmentOperation:OutdoorDryBulbDifference"
            vals["plantequipmentoperation:outdoorwetbulbdifference"] = "PlantEquipmentOperation:OutdoorWetBulbDifference"
            vals["plantequipmentoperation:outdoordewpointdifference"] = "PlantEquipmentOperation:OutdoorDewpointDifference"
            vals["plantequipmentoperation:userdefined"] = "PlantEquipmentOperation:UserDefined"
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
                                     'field `control_scheme_4_object_type`'.format(value))
            value = vals[value_lower]
        self._data["Control Scheme 4 Object Type"] = value

    @property
    def control_scheme_4_name(self):
        """Get control_scheme_4_name

        Returns:
            str: the value of `control_scheme_4_name` or None if not set
        """
        return self._data["Control Scheme 4 Name"]

    @control_scheme_4_name.setter
    def control_scheme_4_name(self, value=None):
        """  Corresponds to IDD Field `Control Scheme 4 Name`

        Args:
            value (str): value for IDD Field `Control Scheme 4 Name`
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
                                 'for field `control_scheme_4_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_scheme_4_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `control_scheme_4_name`')
        self._data["Control Scheme 4 Name"] = value

    @property
    def control_scheme_4_schedule_name(self):
        """Get control_scheme_4_schedule_name

        Returns:
            str: the value of `control_scheme_4_schedule_name` or None if not set
        """
        return self._data["Control Scheme 4 Schedule Name"]

    @control_scheme_4_schedule_name.setter
    def control_scheme_4_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Control Scheme 4 Schedule Name`

        Args:
            value (str): value for IDD Field `Control Scheme 4 Schedule Name`
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
                                 'for field `control_scheme_4_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_scheme_4_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `control_scheme_4_schedule_name`')
        self._data["Control Scheme 4 Schedule Name"] = value

    @property
    def control_scheme_5_object_type(self):
        """Get control_scheme_5_object_type

        Returns:
            str: the value of `control_scheme_5_object_type` or None if not set
        """
        return self._data["Control Scheme 5 Object Type"]

    @control_scheme_5_object_type.setter
    def control_scheme_5_object_type(self, value=None):
        """  Corresponds to IDD Field `Control Scheme 5 Object Type`

        Args:
            value (str): value for IDD Field `Control Scheme 5 Object Type`
                Accepted values are:
                      - PlantEquipmentOperation:Uncontrolled
                      - PlantEquipmentOperation:CoolingLoad
                      - PlantEquipmentOperation:HeatingLoad
                      - PlantEquipmentOperation:OutdoorDryBulb
                      - PlantEquipmentOperation:OutdoorWetBulb
                      - PlantEquipmentOperation:OutdoorRelativeHumidity
                      - PlantEquipmentOperation:OutdoorDewpoint
                      - PlantEquipmentOperation:OutdoorDryBulbDifference
                      - PlantEquipmentOperation:OutdoorWetBulbDifference
                      - PlantEquipmentOperation:OutdoorDewpointDifference
                      - PlantEquipmentOperation:UserDefined
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
                                 'for field `control_scheme_5_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_scheme_5_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `control_scheme_5_object_type`')
            vals = {}
            vals["plantequipmentoperation:uncontrolled"] = "PlantEquipmentOperation:Uncontrolled"
            vals["plantequipmentoperation:coolingload"] = "PlantEquipmentOperation:CoolingLoad"
            vals["plantequipmentoperation:heatingload"] = "PlantEquipmentOperation:HeatingLoad"
            vals["plantequipmentoperation:outdoordrybulb"] = "PlantEquipmentOperation:OutdoorDryBulb"
            vals["plantequipmentoperation:outdoorwetbulb"] = "PlantEquipmentOperation:OutdoorWetBulb"
            vals["plantequipmentoperation:outdoorrelativehumidity"] = "PlantEquipmentOperation:OutdoorRelativeHumidity"
            vals["plantequipmentoperation:outdoordewpoint"] = "PlantEquipmentOperation:OutdoorDewpoint"
            vals["plantequipmentoperation:outdoordrybulbdifference"] = "PlantEquipmentOperation:OutdoorDryBulbDifference"
            vals["plantequipmentoperation:outdoorwetbulbdifference"] = "PlantEquipmentOperation:OutdoorWetBulbDifference"
            vals["plantequipmentoperation:outdoordewpointdifference"] = "PlantEquipmentOperation:OutdoorDewpointDifference"
            vals["plantequipmentoperation:userdefined"] = "PlantEquipmentOperation:UserDefined"
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
                                     'field `control_scheme_5_object_type`'.format(value))
            value = vals[value_lower]
        self._data["Control Scheme 5 Object Type"] = value

    @property
    def control_scheme_5_name(self):
        """Get control_scheme_5_name

        Returns:
            str: the value of `control_scheme_5_name` or None if not set
        """
        return self._data["Control Scheme 5 Name"]

    @control_scheme_5_name.setter
    def control_scheme_5_name(self, value=None):
        """  Corresponds to IDD Field `Control Scheme 5 Name`

        Args:
            value (str): value for IDD Field `Control Scheme 5 Name`
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
                                 'for field `control_scheme_5_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_scheme_5_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `control_scheme_5_name`')
        self._data["Control Scheme 5 Name"] = value

    @property
    def control_scheme_5_schedule_name(self):
        """Get control_scheme_5_schedule_name

        Returns:
            str: the value of `control_scheme_5_schedule_name` or None if not set
        """
        return self._data["Control Scheme 5 Schedule Name"]

    @control_scheme_5_schedule_name.setter
    def control_scheme_5_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Control Scheme 5 Schedule Name`

        Args:
            value (str): value for IDD Field `Control Scheme 5 Schedule Name`
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
                                 'for field `control_scheme_5_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_scheme_5_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `control_scheme_5_schedule_name`')
        self._data["Control Scheme 5 Schedule Name"] = value

    @property
    def control_scheme_6_object_type(self):
        """Get control_scheme_6_object_type

        Returns:
            str: the value of `control_scheme_6_object_type` or None if not set
        """
        return self._data["Control Scheme 6 Object Type"]

    @control_scheme_6_object_type.setter
    def control_scheme_6_object_type(self, value=None):
        """  Corresponds to IDD Field `Control Scheme 6 Object Type`

        Args:
            value (str): value for IDD Field `Control Scheme 6 Object Type`
                Accepted values are:
                      - PlantEquipmentOperation:Uncontrolled
                      - PlantEquipmentOperation:CoolingLoad
                      - PlantEquipmentOperation:HeatingLoad
                      - PlantEquipmentOperation:OutdoorDryBulb
                      - PlantEquipmentOperation:OutdoorWetBulb
                      - PlantEquipmentOperation:OutdoorRelativeHumidity
                      - PlantEquipmentOperation:OutdoorDewpoint
                      - PlantEquipmentOperation:OutdoorDryBulbDifference
                      - PlantEquipmentOperation:OutdoorWetBulbDifference
                      - PlantEquipmentOperation:OutdoorDewpointDifference
                      - PlantEquipmentOperation:UserDefined
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
                                 'for field `control_scheme_6_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_scheme_6_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `control_scheme_6_object_type`')
            vals = {}
            vals["plantequipmentoperation:uncontrolled"] = "PlantEquipmentOperation:Uncontrolled"
            vals["plantequipmentoperation:coolingload"] = "PlantEquipmentOperation:CoolingLoad"
            vals["plantequipmentoperation:heatingload"] = "PlantEquipmentOperation:HeatingLoad"
            vals["plantequipmentoperation:outdoordrybulb"] = "PlantEquipmentOperation:OutdoorDryBulb"
            vals["plantequipmentoperation:outdoorwetbulb"] = "PlantEquipmentOperation:OutdoorWetBulb"
            vals["plantequipmentoperation:outdoorrelativehumidity"] = "PlantEquipmentOperation:OutdoorRelativeHumidity"
            vals["plantequipmentoperation:outdoordewpoint"] = "PlantEquipmentOperation:OutdoorDewpoint"
            vals["plantequipmentoperation:outdoordrybulbdifference"] = "PlantEquipmentOperation:OutdoorDryBulbDifference"
            vals["plantequipmentoperation:outdoorwetbulbdifference"] = "PlantEquipmentOperation:OutdoorWetBulbDifference"
            vals["plantequipmentoperation:outdoordewpointdifference"] = "PlantEquipmentOperation:OutdoorDewpointDifference"
            vals["plantequipmentoperation:userdefined"] = "PlantEquipmentOperation:UserDefined"
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
                                     'field `control_scheme_6_object_type`'.format(value))
            value = vals[value_lower]
        self._data["Control Scheme 6 Object Type"] = value

    @property
    def control_scheme_6_name(self):
        """Get control_scheme_6_name

        Returns:
            str: the value of `control_scheme_6_name` or None if not set
        """
        return self._data["Control Scheme 6 Name"]

    @control_scheme_6_name.setter
    def control_scheme_6_name(self, value=None):
        """  Corresponds to IDD Field `Control Scheme 6 Name`

        Args:
            value (str): value for IDD Field `Control Scheme 6 Name`
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
                                 'for field `control_scheme_6_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_scheme_6_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `control_scheme_6_name`')
        self._data["Control Scheme 6 Name"] = value

    @property
    def control_scheme_6_schedule_name(self):
        """Get control_scheme_6_schedule_name

        Returns:
            str: the value of `control_scheme_6_schedule_name` or None if not set
        """
        return self._data["Control Scheme 6 Schedule Name"]

    @control_scheme_6_schedule_name.setter
    def control_scheme_6_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Control Scheme 6 Schedule Name`

        Args:
            value (str): value for IDD Field `Control Scheme 6 Schedule Name`
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
                                 'for field `control_scheme_6_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_scheme_6_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `control_scheme_6_schedule_name`')
        self._data["Control Scheme 6 Schedule Name"] = value

    @property
    def control_scheme_7_object_type(self):
        """Get control_scheme_7_object_type

        Returns:
            str: the value of `control_scheme_7_object_type` or None if not set
        """
        return self._data["Control Scheme 7 Object Type"]

    @control_scheme_7_object_type.setter
    def control_scheme_7_object_type(self, value=None):
        """  Corresponds to IDD Field `Control Scheme 7 Object Type`

        Args:
            value (str): value for IDD Field `Control Scheme 7 Object Type`
                Accepted values are:
                      - PlantEquipmentOperation:Uncontrolled
                      - PlantEquipmentOperation:CoolingLoad
                      - PlantEquipmentOperation:HeatingLoad
                      - PlantEquipmentOperation:OutdoorDryBulb
                      - PlantEquipmentOperation:OutdoorWetBulb
                      - PlantEquipmentOperation:OutdoorRelativeHumidity
                      - PlantEquipmentOperation:OutdoorDewpoint
                      - PlantEquipmentOperation:OutdoorDryBulbDifference
                      - PlantEquipmentOperation:OutdoorWetBulbDifference
                      - PlantEquipmentOperation:OutdoorDewpointDifference
                      - PlantEquipmentOperation:UserDefined
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
                                 'for field `control_scheme_7_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_scheme_7_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `control_scheme_7_object_type`')
            vals = {}
            vals["plantequipmentoperation:uncontrolled"] = "PlantEquipmentOperation:Uncontrolled"
            vals["plantequipmentoperation:coolingload"] = "PlantEquipmentOperation:CoolingLoad"
            vals["plantequipmentoperation:heatingload"] = "PlantEquipmentOperation:HeatingLoad"
            vals["plantequipmentoperation:outdoordrybulb"] = "PlantEquipmentOperation:OutdoorDryBulb"
            vals["plantequipmentoperation:outdoorwetbulb"] = "PlantEquipmentOperation:OutdoorWetBulb"
            vals["plantequipmentoperation:outdoorrelativehumidity"] = "PlantEquipmentOperation:OutdoorRelativeHumidity"
            vals["plantequipmentoperation:outdoordewpoint"] = "PlantEquipmentOperation:OutdoorDewpoint"
            vals["plantequipmentoperation:outdoordrybulbdifference"] = "PlantEquipmentOperation:OutdoorDryBulbDifference"
            vals["plantequipmentoperation:outdoorwetbulbdifference"] = "PlantEquipmentOperation:OutdoorWetBulbDifference"
            vals["plantequipmentoperation:outdoordewpointdifference"] = "PlantEquipmentOperation:OutdoorDewpointDifference"
            vals["plantequipmentoperation:userdefined"] = "PlantEquipmentOperation:UserDefined"
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
                                     'field `control_scheme_7_object_type`'.format(value))
            value = vals[value_lower]
        self._data["Control Scheme 7 Object Type"] = value

    @property
    def control_scheme_7_name(self):
        """Get control_scheme_7_name

        Returns:
            str: the value of `control_scheme_7_name` or None if not set
        """
        return self._data["Control Scheme 7 Name"]

    @control_scheme_7_name.setter
    def control_scheme_7_name(self, value=None):
        """  Corresponds to IDD Field `Control Scheme 7 Name`

        Args:
            value (str): value for IDD Field `Control Scheme 7 Name`
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
                                 'for field `control_scheme_7_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_scheme_7_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `control_scheme_7_name`')
        self._data["Control Scheme 7 Name"] = value

    @property
    def control_scheme_7_schedule_name(self):
        """Get control_scheme_7_schedule_name

        Returns:
            str: the value of `control_scheme_7_schedule_name` or None if not set
        """
        return self._data["Control Scheme 7 Schedule Name"]

    @control_scheme_7_schedule_name.setter
    def control_scheme_7_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Control Scheme 7 Schedule Name`

        Args:
            value (str): value for IDD Field `Control Scheme 7 Schedule Name`
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
                                 'for field `control_scheme_7_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_scheme_7_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `control_scheme_7_schedule_name`')
        self._data["Control Scheme 7 Schedule Name"] = value

    @property
    def control_scheme_8_object_type(self):
        """Get control_scheme_8_object_type

        Returns:
            str: the value of `control_scheme_8_object_type` or None if not set
        """
        return self._data["Control Scheme 8 Object Type"]

    @control_scheme_8_object_type.setter
    def control_scheme_8_object_type(self, value=None):
        """  Corresponds to IDD Field `Control Scheme 8 Object Type`

        Args:
            value (str): value for IDD Field `Control Scheme 8 Object Type`
                Accepted values are:
                      - PlantEquipmentOperation:Uncontrolled
                      - PlantEquipmentOperation:CoolingLoad
                      - PlantEquipmentOperation:HeatingLoad
                      - PlantEquipmentOperation:OutdoorDryBulb
                      - PlantEquipmentOperation:OutdoorWetBulb
                      - PlantEquipmentOperation:OutdoorRelativeHumidity
                      - PlantEquipmentOperation:OutdoorDewpoint
                      - PlantEquipmentOperation:OutdoorDryBulbDifference
                      - PlantEquipmentOperation:OutdoorWetBulbDifference
                      - PlantEquipmentOperation:OutdoorDewpointDifference
                      - PlantEquipmentOperation:UserDefined
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
                                 'for field `control_scheme_8_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_scheme_8_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `control_scheme_8_object_type`')
            vals = {}
            vals["plantequipmentoperation:uncontrolled"] = "PlantEquipmentOperation:Uncontrolled"
            vals["plantequipmentoperation:coolingload"] = "PlantEquipmentOperation:CoolingLoad"
            vals["plantequipmentoperation:heatingload"] = "PlantEquipmentOperation:HeatingLoad"
            vals["plantequipmentoperation:outdoordrybulb"] = "PlantEquipmentOperation:OutdoorDryBulb"
            vals["plantequipmentoperation:outdoorwetbulb"] = "PlantEquipmentOperation:OutdoorWetBulb"
            vals["plantequipmentoperation:outdoorrelativehumidity"] = "PlantEquipmentOperation:OutdoorRelativeHumidity"
            vals["plantequipmentoperation:outdoordewpoint"] = "PlantEquipmentOperation:OutdoorDewpoint"
            vals["plantequipmentoperation:outdoordrybulbdifference"] = "PlantEquipmentOperation:OutdoorDryBulbDifference"
            vals["plantequipmentoperation:outdoorwetbulbdifference"] = "PlantEquipmentOperation:OutdoorWetBulbDifference"
            vals["plantequipmentoperation:outdoordewpointdifference"] = "PlantEquipmentOperation:OutdoorDewpointDifference"
            vals["plantequipmentoperation:userdefined"] = "PlantEquipmentOperation:UserDefined"
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
                                     'field `control_scheme_8_object_type`'.format(value))
            value = vals[value_lower]
        self._data["Control Scheme 8 Object Type"] = value

    @property
    def control_scheme_8_name(self):
        """Get control_scheme_8_name

        Returns:
            str: the value of `control_scheme_8_name` or None if not set
        """
        return self._data["Control Scheme 8 Name"]

    @control_scheme_8_name.setter
    def control_scheme_8_name(self, value=None):
        """  Corresponds to IDD Field `Control Scheme 8 Name`

        Args:
            value (str): value for IDD Field `Control Scheme 8 Name`
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
                                 'for field `control_scheme_8_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_scheme_8_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `control_scheme_8_name`')
        self._data["Control Scheme 8 Name"] = value

    @property
    def control_scheme_8_schedule_name(self):
        """Get control_scheme_8_schedule_name

        Returns:
            str: the value of `control_scheme_8_schedule_name` or None if not set
        """
        return self._data["Control Scheme 8 Schedule Name"]

    @control_scheme_8_schedule_name.setter
    def control_scheme_8_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Control Scheme 8 Schedule Name`

        Args:
            value (str): value for IDD Field `Control Scheme 8 Schedule Name`
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
                                 'for field `control_scheme_8_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_scheme_8_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `control_scheme_8_schedule_name`')
        self._data["Control Scheme 8 Schedule Name"] = value

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