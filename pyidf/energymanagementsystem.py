from collections import OrderedDict

class EnergyManagementSystemSensor(object):
    """ Corresponds to IDD object `EnergyManagementSystem:Sensor`
        Declares EMS variable as a sensor
        a list of output variables and meters that can be reported are available after a run on
        the report (.rdd) or meter dictionary file (.mdd) if the Output:VariableDictionary
        has been requested.
    """
    internal_name = "EnergyManagementSystem:Sensor"
    field_count = 3

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `EnergyManagementSystem:Sensor`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Output:Variable or Output:Meter Index Key Name"] = None
        self._data["Output:Variable or Output:Meter Name"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outputvariable_or_outputmeter_index_key_name = None
        else:
            self.outputvariable_or_outputmeter_index_key_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outputvariable_or_outputmeter_name = None
        else:
            self.outputvariable_or_outputmeter_name = vals[i]
        i += 1

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `name`
        This name becomes a variable for use in Erl programs
        no spaces allowed in name

        Args:
            value (str): value for IDD Field `name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')

        self._data["Name"] = value

    @property
    def outputvariable_or_outputmeter_index_key_name(self):
        """Get outputvariable_or_outputmeter_index_key_name

        Returns:
            str: the value of `outputvariable_or_outputmeter_index_key_name` or None if not set
        """
        return self._data["Output:Variable or Output:Meter Index Key Name"]

    @outputvariable_or_outputmeter_index_key_name.setter
    def outputvariable_or_outputmeter_index_key_name(self, value=None):
        """  Corresponds to IDD Field `outputvariable_or_outputmeter_index_key_name`

        Args:
            value (str): value for IDD Field `outputvariable_or_outputmeter_index_key_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outputvariable_or_outputmeter_index_key_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outputvariable_or_outputmeter_index_key_name`')

        self._data["Output:Variable or Output:Meter Index Key Name"] = value

    @property
    def outputvariable_or_outputmeter_name(self):
        """Get outputvariable_or_outputmeter_name

        Returns:
            str: the value of `outputvariable_or_outputmeter_name` or None if not set
        """
        return self._data["Output:Variable or Output:Meter Name"]

    @outputvariable_or_outputmeter_name.setter
    def outputvariable_or_outputmeter_name(self, value=None):
        """  Corresponds to IDD Field `outputvariable_or_outputmeter_name`

        Args:
            value (str): value for IDD Field `outputvariable_or_outputmeter_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outputvariable_or_outputmeter_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outputvariable_or_outputmeter_name`')

        self._data["Output:Variable or Output:Meter Name"] = value

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

    def __str__(self):
        out = []
        out.append(self._to_str(self.name))
        out.append(self._to_str(self.outputvariable_or_outputmeter_index_key_name))
        out.append(self._to_str(self.outputvariable_or_outputmeter_name))
        return ",".join(out)

class EnergyManagementSystemActuator(object):
    """ Corresponds to IDD object `EnergyManagementSystem:Actuator`
        Hardware portion of EMS used to set up actuators in the model
    """
    internal_name = "EnergyManagementSystem:Actuator"
    field_count = 4

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `EnergyManagementSystem:Actuator`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Actuated Component Unique Name"] = None
        self._data["Actuated Component Type"] = None
        self._data["Actuated Component Control Type"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.actuated_component_unique_name = None
        else:
            self.actuated_component_unique_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.actuated_component_type = None
        else:
            self.actuated_component_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.actuated_component_control_type = None
        else:
            self.actuated_component_control_type = vals[i]
        i += 1

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `name`
        This name becomes a variable for use in Erl programs
        no spaces allowed in name

        Args:
            value (str): value for IDD Field `name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')

        self._data["Name"] = value

    @property
    def actuated_component_unique_name(self):
        """Get actuated_component_unique_name

        Returns:
            str: the value of `actuated_component_unique_name` or None if not set
        """
        return self._data["Actuated Component Unique Name"]

    @actuated_component_unique_name.setter
    def actuated_component_unique_name(self, value=None):
        """  Corresponds to IDD Field `actuated_component_unique_name`

        Args:
            value (str): value for IDD Field `actuated_component_unique_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `actuated_component_unique_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `actuated_component_unique_name`')

        self._data["Actuated Component Unique Name"] = value

    @property
    def actuated_component_type(self):
        """Get actuated_component_type

        Returns:
            str: the value of `actuated_component_type` or None if not set
        """
        return self._data["Actuated Component Type"]

    @actuated_component_type.setter
    def actuated_component_type(self, value=None):
        """  Corresponds to IDD Field `actuated_component_type`

        Args:
            value (str): value for IDD Field `actuated_component_type`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `actuated_component_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `actuated_component_type`')

        self._data["Actuated Component Type"] = value

    @property
    def actuated_component_control_type(self):
        """Get actuated_component_control_type

        Returns:
            str: the value of `actuated_component_control_type` or None if not set
        """
        return self._data["Actuated Component Control Type"]

    @actuated_component_control_type.setter
    def actuated_component_control_type(self, value=None):
        """  Corresponds to IDD Field `actuated_component_control_type`

        Args:
            value (str): value for IDD Field `actuated_component_control_type`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `actuated_component_control_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `actuated_component_control_type`')

        self._data["Actuated Component Control Type"] = value

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

    def __str__(self):
        out = []
        out.append(self._to_str(self.name))
        out.append(self._to_str(self.actuated_component_unique_name))
        out.append(self._to_str(self.actuated_component_type))
        out.append(self._to_str(self.actuated_component_control_type))
        return ",".join(out)

class EnergyManagementSystemProgramCallingManager(object):
    """ Corresponds to IDD object `EnergyManagementSystem:ProgramCallingManager`
        Input EMS program. a program needs a name
        a description of when it should be called
        and then lines of program code for EMS Runtime language
    """
    internal_name = "EnergyManagementSystem:ProgramCallingManager"
    field_count = 27

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `EnergyManagementSystem:ProgramCallingManager`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["EnergyPlus Model Calling Point"] = None
        self._data["Program Name 1"] = None
        self._data["Program Name 2"] = None
        self._data["Program Name 3"] = None
        self._data["Program Name 4"] = None
        self._data["Program Name 5"] = None
        self._data["Program Name 6"] = None
        self._data["Program Name 7"] = None
        self._data["Program Name 8"] = None
        self._data["Program Name 9"] = None
        self._data["Program Name 10"] = None
        self._data["Program Name 11"] = None
        self._data["Program Name 12"] = None
        self._data["Program Name 13"] = None
        self._data["Program Name 14"] = None
        self._data["Program Name 15"] = None
        self._data["Program Name 16"] = None
        self._data["Program Name 17"] = None
        self._data["Program Name 18"] = None
        self._data["Program Name 19"] = None
        self._data["Program Name 20"] = None
        self._data["Program Name 21"] = None
        self._data["Program Name 22"] = None
        self._data["Program Name 23"] = None
        self._data["Program Name 24"] = None
        self._data["Program Name 25"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.energyplus_model_calling_point = None
        else:
            self.energyplus_model_calling_point = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.program_name_1 = None
        else:
            self.program_name_1 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.program_name_2 = None
        else:
            self.program_name_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.program_name_3 = None
        else:
            self.program_name_3 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.program_name_4 = None
        else:
            self.program_name_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.program_name_5 = None
        else:
            self.program_name_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.program_name_6 = None
        else:
            self.program_name_6 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.program_name_7 = None
        else:
            self.program_name_7 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.program_name_8 = None
        else:
            self.program_name_8 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.program_name_9 = None
        else:
            self.program_name_9 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.program_name_10 = None
        else:
            self.program_name_10 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.program_name_11 = None
        else:
            self.program_name_11 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.program_name_12 = None
        else:
            self.program_name_12 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.program_name_13 = None
        else:
            self.program_name_13 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.program_name_14 = None
        else:
            self.program_name_14 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.program_name_15 = None
        else:
            self.program_name_15 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.program_name_16 = None
        else:
            self.program_name_16 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.program_name_17 = None
        else:
            self.program_name_17 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.program_name_18 = None
        else:
            self.program_name_18 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.program_name_19 = None
        else:
            self.program_name_19 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.program_name_20 = None
        else:
            self.program_name_20 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.program_name_21 = None
        else:
            self.program_name_21 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.program_name_22 = None
        else:
            self.program_name_22 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.program_name_23 = None
        else:
            self.program_name_23 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.program_name_24 = None
        else:
            self.program_name_24 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.program_name_25 = None
        else:
            self.program_name_25 = vals[i]
        i += 1

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `name`
        no spaces allowed in name

        Args:
            value (str): value for IDD Field `name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')

        self._data["Name"] = value

    @property
    def energyplus_model_calling_point(self):
        """Get energyplus_model_calling_point

        Returns:
            str: the value of `energyplus_model_calling_point` or None if not set
        """
        return self._data["EnergyPlus Model Calling Point"]

    @energyplus_model_calling_point.setter
    def energyplus_model_calling_point(self, value=None):
        """  Corresponds to IDD Field `energyplus_model_calling_point`

        Args:
            value (str): value for IDD Field `energyplus_model_calling_point`
                Accepted values are:
                      - BeginNewEnvironment
                      - AfterNewEnvironmentWarmUpIsComplete
                      - BeginTimestepBeforePredictor
                      - AfterPredictorBeforeHVACManagers
                      - AfterPredictorAfterHVACManagers
                      - InsideHVACSystemIterationLoop
                      - EndOfZoneTimestepBeforeZoneReporting
                      - EndOfZoneTimestepAfterZoneReporting
                      - EndOfSystemTimestepBeforeHVACReporting
                      - EndOfSystemTimestepAfterHVACReporting
                      - EndOfZoneSizing
                      - EndOfSystemSizing
                      - AfterComponentInputReadIn
                      - UserDefinedComponentModel
                      - UnitarySystemSizing
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `energyplus_model_calling_point`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `energyplus_model_calling_point`')
            vals = set()
            vals.add("BeginNewEnvironment")
            vals.add("AfterNewEnvironmentWarmUpIsComplete")
            vals.add("BeginTimestepBeforePredictor")
            vals.add("AfterPredictorBeforeHVACManagers")
            vals.add("AfterPredictorAfterHVACManagers")
            vals.add("InsideHVACSystemIterationLoop")
            vals.add("EndOfZoneTimestepBeforeZoneReporting")
            vals.add("EndOfZoneTimestepAfterZoneReporting")
            vals.add("EndOfSystemTimestepBeforeHVACReporting")
            vals.add("EndOfSystemTimestepAfterHVACReporting")
            vals.add("EndOfZoneSizing")
            vals.add("EndOfSystemSizing")
            vals.add("AfterComponentInputReadIn")
            vals.add("UserDefinedComponentModel")
            vals.add("UnitarySystemSizing")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `energyplus_model_calling_point`'.format(value))

        self._data["EnergyPlus Model Calling Point"] = value

    @property
    def program_name_1(self):
        """Get program_name_1

        Returns:
            str: the value of `program_name_1` or None if not set
        """
        return self._data["Program Name 1"]

    @program_name_1.setter
    def program_name_1(self, value=None):
        """  Corresponds to IDD Field `program_name_1`
        no spaces allowed in name

        Args:
            value (str): value for IDD Field `program_name_1`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_name_1`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_name_1`')

        self._data["Program Name 1"] = value

    @property
    def program_name_2(self):
        """Get program_name_2

        Returns:
            str: the value of `program_name_2` or None if not set
        """
        return self._data["Program Name 2"]

    @program_name_2.setter
    def program_name_2(self, value=None):
        """  Corresponds to IDD Field `program_name_2`
        no spaces allowed in name

        Args:
            value (str): value for IDD Field `program_name_2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_name_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_name_2`')

        self._data["Program Name 2"] = value

    @property
    def program_name_3(self):
        """Get program_name_3

        Returns:
            str: the value of `program_name_3` or None if not set
        """
        return self._data["Program Name 3"]

    @program_name_3.setter
    def program_name_3(self, value=None):
        """  Corresponds to IDD Field `program_name_3`
        no spaces allowed in name

        Args:
            value (str): value for IDD Field `program_name_3`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_name_3`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_name_3`')

        self._data["Program Name 3"] = value

    @property
    def program_name_4(self):
        """Get program_name_4

        Returns:
            str: the value of `program_name_4` or None if not set
        """
        return self._data["Program Name 4"]

    @program_name_4.setter
    def program_name_4(self, value=None):
        """  Corresponds to IDD Field `program_name_4`
        no spaces allowed in name

        Args:
            value (str): value for IDD Field `program_name_4`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_name_4`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_name_4`')

        self._data["Program Name 4"] = value

    @property
    def program_name_5(self):
        """Get program_name_5

        Returns:
            str: the value of `program_name_5` or None if not set
        """
        return self._data["Program Name 5"]

    @program_name_5.setter
    def program_name_5(self, value=None):
        """  Corresponds to IDD Field `program_name_5`
        no spaces allowed in name

        Args:
            value (str): value for IDD Field `program_name_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_name_5`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_name_5`')

        self._data["Program Name 5"] = value

    @property
    def program_name_6(self):
        """Get program_name_6

        Returns:
            str: the value of `program_name_6` or None if not set
        """
        return self._data["Program Name 6"]

    @program_name_6.setter
    def program_name_6(self, value=None):
        """  Corresponds to IDD Field `program_name_6`
        no spaces allowed in name

        Args:
            value (str): value for IDD Field `program_name_6`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_name_6`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_name_6`')

        self._data["Program Name 6"] = value

    @property
    def program_name_7(self):
        """Get program_name_7

        Returns:
            str: the value of `program_name_7` or None if not set
        """
        return self._data["Program Name 7"]

    @program_name_7.setter
    def program_name_7(self, value=None):
        """  Corresponds to IDD Field `program_name_7`
        no spaces allowed in name

        Args:
            value (str): value for IDD Field `program_name_7`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_name_7`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_name_7`')

        self._data["Program Name 7"] = value

    @property
    def program_name_8(self):
        """Get program_name_8

        Returns:
            str: the value of `program_name_8` or None if not set
        """
        return self._data["Program Name 8"]

    @program_name_8.setter
    def program_name_8(self, value=None):
        """  Corresponds to IDD Field `program_name_8`
        no spaces allowed in name

        Args:
            value (str): value for IDD Field `program_name_8`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_name_8`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_name_8`')

        self._data["Program Name 8"] = value

    @property
    def program_name_9(self):
        """Get program_name_9

        Returns:
            str: the value of `program_name_9` or None if not set
        """
        return self._data["Program Name 9"]

    @program_name_9.setter
    def program_name_9(self, value=None):
        """  Corresponds to IDD Field `program_name_9`
        no spaces allowed in name

        Args:
            value (str): value for IDD Field `program_name_9`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_name_9`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_name_9`')

        self._data["Program Name 9"] = value

    @property
    def program_name_10(self):
        """Get program_name_10

        Returns:
            str: the value of `program_name_10` or None if not set
        """
        return self._data["Program Name 10"]

    @program_name_10.setter
    def program_name_10(self, value=None):
        """  Corresponds to IDD Field `program_name_10`
        no spaces allowed in name

        Args:
            value (str): value for IDD Field `program_name_10`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_name_10`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_name_10`')

        self._data["Program Name 10"] = value

    @property
    def program_name_11(self):
        """Get program_name_11

        Returns:
            str: the value of `program_name_11` or None if not set
        """
        return self._data["Program Name 11"]

    @program_name_11.setter
    def program_name_11(self, value=None):
        """  Corresponds to IDD Field `program_name_11`
        no spaces allowed in name

        Args:
            value (str): value for IDD Field `program_name_11`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_name_11`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_name_11`')

        self._data["Program Name 11"] = value

    @property
    def program_name_12(self):
        """Get program_name_12

        Returns:
            str: the value of `program_name_12` or None if not set
        """
        return self._data["Program Name 12"]

    @program_name_12.setter
    def program_name_12(self, value=None):
        """  Corresponds to IDD Field `program_name_12`
        no spaces allowed in name

        Args:
            value (str): value for IDD Field `program_name_12`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_name_12`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_name_12`')

        self._data["Program Name 12"] = value

    @property
    def program_name_13(self):
        """Get program_name_13

        Returns:
            str: the value of `program_name_13` or None if not set
        """
        return self._data["Program Name 13"]

    @program_name_13.setter
    def program_name_13(self, value=None):
        """  Corresponds to IDD Field `program_name_13`
        no spaces allowed in name

        Args:
            value (str): value for IDD Field `program_name_13`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_name_13`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_name_13`')

        self._data["Program Name 13"] = value

    @property
    def program_name_14(self):
        """Get program_name_14

        Returns:
            str: the value of `program_name_14` or None if not set
        """
        return self._data["Program Name 14"]

    @program_name_14.setter
    def program_name_14(self, value=None):
        """  Corresponds to IDD Field `program_name_14`
        no spaces allowed in name

        Args:
            value (str): value for IDD Field `program_name_14`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_name_14`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_name_14`')

        self._data["Program Name 14"] = value

    @property
    def program_name_15(self):
        """Get program_name_15

        Returns:
            str: the value of `program_name_15` or None if not set
        """
        return self._data["Program Name 15"]

    @program_name_15.setter
    def program_name_15(self, value=None):
        """  Corresponds to IDD Field `program_name_15`
        no spaces allowed in name

        Args:
            value (str): value for IDD Field `program_name_15`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_name_15`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_name_15`')

        self._data["Program Name 15"] = value

    @property
    def program_name_16(self):
        """Get program_name_16

        Returns:
            str: the value of `program_name_16` or None if not set
        """
        return self._data["Program Name 16"]

    @program_name_16.setter
    def program_name_16(self, value=None):
        """  Corresponds to IDD Field `program_name_16`
        no spaces allowed in name

        Args:
            value (str): value for IDD Field `program_name_16`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_name_16`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_name_16`')

        self._data["Program Name 16"] = value

    @property
    def program_name_17(self):
        """Get program_name_17

        Returns:
            str: the value of `program_name_17` or None if not set
        """
        return self._data["Program Name 17"]

    @program_name_17.setter
    def program_name_17(self, value=None):
        """  Corresponds to IDD Field `program_name_17`
        no spaces allowed in name

        Args:
            value (str): value for IDD Field `program_name_17`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_name_17`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_name_17`')

        self._data["Program Name 17"] = value

    @property
    def program_name_18(self):
        """Get program_name_18

        Returns:
            str: the value of `program_name_18` or None if not set
        """
        return self._data["Program Name 18"]

    @program_name_18.setter
    def program_name_18(self, value=None):
        """  Corresponds to IDD Field `program_name_18`
        no spaces allowed in name

        Args:
            value (str): value for IDD Field `program_name_18`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_name_18`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_name_18`')

        self._data["Program Name 18"] = value

    @property
    def program_name_19(self):
        """Get program_name_19

        Returns:
            str: the value of `program_name_19` or None if not set
        """
        return self._data["Program Name 19"]

    @program_name_19.setter
    def program_name_19(self, value=None):
        """  Corresponds to IDD Field `program_name_19`
        no spaces allowed in name

        Args:
            value (str): value for IDD Field `program_name_19`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_name_19`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_name_19`')

        self._data["Program Name 19"] = value

    @property
    def program_name_20(self):
        """Get program_name_20

        Returns:
            str: the value of `program_name_20` or None if not set
        """
        return self._data["Program Name 20"]

    @program_name_20.setter
    def program_name_20(self, value=None):
        """  Corresponds to IDD Field `program_name_20`
        no spaces allowed in name

        Args:
            value (str): value for IDD Field `program_name_20`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_name_20`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_name_20`')

        self._data["Program Name 20"] = value

    @property
    def program_name_21(self):
        """Get program_name_21

        Returns:
            str: the value of `program_name_21` or None if not set
        """
        return self._data["Program Name 21"]

    @program_name_21.setter
    def program_name_21(self, value=None):
        """  Corresponds to IDD Field `program_name_21`
        no spaces allowed in name

        Args:
            value (str): value for IDD Field `program_name_21`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_name_21`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_name_21`')

        self._data["Program Name 21"] = value

    @property
    def program_name_22(self):
        """Get program_name_22

        Returns:
            str: the value of `program_name_22` or None if not set
        """
        return self._data["Program Name 22"]

    @program_name_22.setter
    def program_name_22(self, value=None):
        """  Corresponds to IDD Field `program_name_22`
        no spaces allowed in name

        Args:
            value (str): value for IDD Field `program_name_22`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_name_22`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_name_22`')

        self._data["Program Name 22"] = value

    @property
    def program_name_23(self):
        """Get program_name_23

        Returns:
            str: the value of `program_name_23` or None if not set
        """
        return self._data["Program Name 23"]

    @program_name_23.setter
    def program_name_23(self, value=None):
        """  Corresponds to IDD Field `program_name_23`
        no spaces allowed in name

        Args:
            value (str): value for IDD Field `program_name_23`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_name_23`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_name_23`')

        self._data["Program Name 23"] = value

    @property
    def program_name_24(self):
        """Get program_name_24

        Returns:
            str: the value of `program_name_24` or None if not set
        """
        return self._data["Program Name 24"]

    @program_name_24.setter
    def program_name_24(self, value=None):
        """  Corresponds to IDD Field `program_name_24`
        no spaces allowed in name

        Args:
            value (str): value for IDD Field `program_name_24`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_name_24`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_name_24`')

        self._data["Program Name 24"] = value

    @property
    def program_name_25(self):
        """Get program_name_25

        Returns:
            str: the value of `program_name_25` or None if not set
        """
        return self._data["Program Name 25"]

    @program_name_25.setter
    def program_name_25(self, value=None):
        """  Corresponds to IDD Field `program_name_25`
        no spaces allowed in name

        Args:
            value (str): value for IDD Field `program_name_25`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_name_25`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_name_25`')

        self._data["Program Name 25"] = value

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

    def __str__(self):
        out = []
        out.append(self._to_str(self.name))
        out.append(self._to_str(self.energyplus_model_calling_point))
        out.append(self._to_str(self.program_name_1))
        out.append(self._to_str(self.program_name_2))
        out.append(self._to_str(self.program_name_3))
        out.append(self._to_str(self.program_name_4))
        out.append(self._to_str(self.program_name_5))
        out.append(self._to_str(self.program_name_6))
        out.append(self._to_str(self.program_name_7))
        out.append(self._to_str(self.program_name_8))
        out.append(self._to_str(self.program_name_9))
        out.append(self._to_str(self.program_name_10))
        out.append(self._to_str(self.program_name_11))
        out.append(self._to_str(self.program_name_12))
        out.append(self._to_str(self.program_name_13))
        out.append(self._to_str(self.program_name_14))
        out.append(self._to_str(self.program_name_15))
        out.append(self._to_str(self.program_name_16))
        out.append(self._to_str(self.program_name_17))
        out.append(self._to_str(self.program_name_18))
        out.append(self._to_str(self.program_name_19))
        out.append(self._to_str(self.program_name_20))
        out.append(self._to_str(self.program_name_21))
        out.append(self._to_str(self.program_name_22))
        out.append(self._to_str(self.program_name_23))
        out.append(self._to_str(self.program_name_24))
        out.append(self._to_str(self.program_name_25))
        return ",".join(out)

class EnergyManagementSystemProgram(object):
    """ Corresponds to IDD object `EnergyManagementSystem:Program`
        This input defines an Erl program
        Each field after the name is a line of EMS Runtime Language
    """
    internal_name = "EnergyManagementSystem:Program"
    field_count = 49

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `EnergyManagementSystem:Program`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Program Line 1"] = None
        self._data["Program Line 2"] = None
        self._data["Program Line 2"] = None
        self._data["Program Line 2"] = None
        self._data["Program Line 2"] = None
        self._data["Program Line 2"] = None
        self._data["Program Line 2"] = None
        self._data["Program Line 2"] = None
        self._data["Program Line 2"] = None
        self._data["Program Line 2"] = None
        self._data["Program Line 2"] = None
        self._data["Program Line 2"] = None
        self._data["Program Line 2"] = None
        self._data["Program Line 2"] = None
        self._data["Program Line 2"] = None
        self._data["Program Line 2"] = None
        self._data["Program Line 2"] = None
        self._data["Program Line 2"] = None
        self._data["Program Line 2"] = None
        self._data["Program Line 2"] = None
        self._data["Program Line 2"] = None
        self._data["Program Line 2"] = None
        self._data["Program Line 2"] = None
        self._data["Program Line 2"] = None
        self._data["Program Line 2"] = None
        self._data["Program Line 2"] = None
        self._data["Program Line 2"] = None
        self._data["Program Line 2"] = None
        self._data["Program Line 2"] = None
        self._data["Program Line 2"] = None
        self._data["Program Line 2"] = None
        self._data["Program Line 2"] = None
        self._data["Program Line 2"] = None
        self._data["Program Line 2"] = None
        self._data["Program Line 2"] = None
        self._data["Program Line 2"] = None
        self._data["Program Line 2"] = None
        self._data["Program Line 2"] = None
        self._data["Program Line 2"] = None
        self._data["Program Line 2"] = None
        self._data["Program Line 2"] = None
        self._data["Program Line 2"] = None
        self._data["Program Line 2"] = None
        self._data["Program Line 2"] = None
        self._data["Program Line 2"] = None
        self._data["Program Line 2"] = None
        self._data["Program Line 2"] = None
        self._data["Program Line 2"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.program_line_1 = None
        else:
            self.program_line_1 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.program_line_2 = None
        else:
            self.program_line_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.program_line_2 = None
        else:
            self.program_line_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.program_line_2 = None
        else:
            self.program_line_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.program_line_2 = None
        else:
            self.program_line_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.program_line_2 = None
        else:
            self.program_line_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.program_line_2 = None
        else:
            self.program_line_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.program_line_2 = None
        else:
            self.program_line_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.program_line_2 = None
        else:
            self.program_line_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.program_line_2 = None
        else:
            self.program_line_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.program_line_2 = None
        else:
            self.program_line_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.program_line_2 = None
        else:
            self.program_line_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.program_line_2 = None
        else:
            self.program_line_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.program_line_2 = None
        else:
            self.program_line_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.program_line_2 = None
        else:
            self.program_line_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.program_line_2 = None
        else:
            self.program_line_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.program_line_2 = None
        else:
            self.program_line_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.program_line_2 = None
        else:
            self.program_line_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.program_line_2 = None
        else:
            self.program_line_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.program_line_2 = None
        else:
            self.program_line_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.program_line_2 = None
        else:
            self.program_line_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.program_line_2 = None
        else:
            self.program_line_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.program_line_2 = None
        else:
            self.program_line_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.program_line_2 = None
        else:
            self.program_line_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.program_line_2 = None
        else:
            self.program_line_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.program_line_2 = None
        else:
            self.program_line_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.program_line_2 = None
        else:
            self.program_line_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.program_line_2 = None
        else:
            self.program_line_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.program_line_2 = None
        else:
            self.program_line_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.program_line_2 = None
        else:
            self.program_line_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.program_line_2 = None
        else:
            self.program_line_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.program_line_2 = None
        else:
            self.program_line_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.program_line_2 = None
        else:
            self.program_line_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.program_line_2 = None
        else:
            self.program_line_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.program_line_2 = None
        else:
            self.program_line_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.program_line_2 = None
        else:
            self.program_line_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.program_line_2 = None
        else:
            self.program_line_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.program_line_2 = None
        else:
            self.program_line_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.program_line_2 = None
        else:
            self.program_line_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.program_line_2 = None
        else:
            self.program_line_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.program_line_2 = None
        else:
            self.program_line_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.program_line_2 = None
        else:
            self.program_line_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.program_line_2 = None
        else:
            self.program_line_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.program_line_2 = None
        else:
            self.program_line_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.program_line_2 = None
        else:
            self.program_line_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.program_line_2 = None
        else:
            self.program_line_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.program_line_2 = None
        else:
            self.program_line_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.program_line_2 = None
        else:
            self.program_line_2 = vals[i]
        i += 1

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `name`
        no spaces allowed in name

        Args:
            value (str): value for IDD Field `name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')

        self._data["Name"] = value

    @property
    def program_line_1(self):
        """Get program_line_1

        Returns:
            str: the value of `program_line_1` or None if not set
        """
        return self._data["Program Line 1"]

    @program_line_1.setter
    def program_line_1(self, value=None):
        """  Corresponds to IDD Field `program_line_1`

        Args:
            value (str): value for IDD Field `program_line_1`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_line_1`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_line_1`')

        self._data["Program Line 1"] = value

    @property
    def program_line_2(self):
        """Get program_line_2

        Returns:
            str: the value of `program_line_2` or None if not set
        """
        return self._data["Program Line 2"]

    @program_line_2.setter
    def program_line_2(self, value=None):
        """  Corresponds to IDD Field `program_line_2`

        Args:
            value (str): value for IDD Field `program_line_2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_line_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_line_2`')

        self._data["Program Line 2"] = value

    @property
    def program_line_2(self):
        """Get program_line_2

        Returns:
            str: the value of `program_line_2` or None if not set
        """
        return self._data["Program Line 2"]

    @program_line_2.setter
    def program_line_2(self, value=None):
        """  Corresponds to IDD Field `program_line_2`

        Args:
            value (str): value for IDD Field `program_line_2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_line_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_line_2`')

        self._data["Program Line 2"] = value

    @property
    def program_line_2(self):
        """Get program_line_2

        Returns:
            str: the value of `program_line_2` or None if not set
        """
        return self._data["Program Line 2"]

    @program_line_2.setter
    def program_line_2(self, value=None):
        """  Corresponds to IDD Field `program_line_2`

        Args:
            value (str): value for IDD Field `program_line_2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_line_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_line_2`')

        self._data["Program Line 2"] = value

    @property
    def program_line_2(self):
        """Get program_line_2

        Returns:
            str: the value of `program_line_2` or None if not set
        """
        return self._data["Program Line 2"]

    @program_line_2.setter
    def program_line_2(self, value=None):
        """  Corresponds to IDD Field `program_line_2`

        Args:
            value (str): value for IDD Field `program_line_2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_line_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_line_2`')

        self._data["Program Line 2"] = value

    @property
    def program_line_2(self):
        """Get program_line_2

        Returns:
            str: the value of `program_line_2` or None if not set
        """
        return self._data["Program Line 2"]

    @program_line_2.setter
    def program_line_2(self, value=None):
        """  Corresponds to IDD Field `program_line_2`

        Args:
            value (str): value for IDD Field `program_line_2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_line_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_line_2`')

        self._data["Program Line 2"] = value

    @property
    def program_line_2(self):
        """Get program_line_2

        Returns:
            str: the value of `program_line_2` or None if not set
        """
        return self._data["Program Line 2"]

    @program_line_2.setter
    def program_line_2(self, value=None):
        """  Corresponds to IDD Field `program_line_2`

        Args:
            value (str): value for IDD Field `program_line_2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_line_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_line_2`')

        self._data["Program Line 2"] = value

    @property
    def program_line_2(self):
        """Get program_line_2

        Returns:
            str: the value of `program_line_2` or None if not set
        """
        return self._data["Program Line 2"]

    @program_line_2.setter
    def program_line_2(self, value=None):
        """  Corresponds to IDD Field `program_line_2`

        Args:
            value (str): value for IDD Field `program_line_2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_line_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_line_2`')

        self._data["Program Line 2"] = value

    @property
    def program_line_2(self):
        """Get program_line_2

        Returns:
            str: the value of `program_line_2` or None if not set
        """
        return self._data["Program Line 2"]

    @program_line_2.setter
    def program_line_2(self, value=None):
        """  Corresponds to IDD Field `program_line_2`

        Args:
            value (str): value for IDD Field `program_line_2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_line_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_line_2`')

        self._data["Program Line 2"] = value

    @property
    def program_line_2(self):
        """Get program_line_2

        Returns:
            str: the value of `program_line_2` or None if not set
        """
        return self._data["Program Line 2"]

    @program_line_2.setter
    def program_line_2(self, value=None):
        """  Corresponds to IDD Field `program_line_2`

        Args:
            value (str): value for IDD Field `program_line_2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_line_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_line_2`')

        self._data["Program Line 2"] = value

    @property
    def program_line_2(self):
        """Get program_line_2

        Returns:
            str: the value of `program_line_2` or None if not set
        """
        return self._data["Program Line 2"]

    @program_line_2.setter
    def program_line_2(self, value=None):
        """  Corresponds to IDD Field `program_line_2`

        Args:
            value (str): value for IDD Field `program_line_2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_line_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_line_2`')

        self._data["Program Line 2"] = value

    @property
    def program_line_2(self):
        """Get program_line_2

        Returns:
            str: the value of `program_line_2` or None if not set
        """
        return self._data["Program Line 2"]

    @program_line_2.setter
    def program_line_2(self, value=None):
        """  Corresponds to IDD Field `program_line_2`

        Args:
            value (str): value for IDD Field `program_line_2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_line_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_line_2`')

        self._data["Program Line 2"] = value

    @property
    def program_line_2(self):
        """Get program_line_2

        Returns:
            str: the value of `program_line_2` or None if not set
        """
        return self._data["Program Line 2"]

    @program_line_2.setter
    def program_line_2(self, value=None):
        """  Corresponds to IDD Field `program_line_2`

        Args:
            value (str): value for IDD Field `program_line_2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_line_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_line_2`')

        self._data["Program Line 2"] = value

    @property
    def program_line_2(self):
        """Get program_line_2

        Returns:
            str: the value of `program_line_2` or None if not set
        """
        return self._data["Program Line 2"]

    @program_line_2.setter
    def program_line_2(self, value=None):
        """  Corresponds to IDD Field `program_line_2`

        Args:
            value (str): value for IDD Field `program_line_2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_line_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_line_2`')

        self._data["Program Line 2"] = value

    @property
    def program_line_2(self):
        """Get program_line_2

        Returns:
            str: the value of `program_line_2` or None if not set
        """
        return self._data["Program Line 2"]

    @program_line_2.setter
    def program_line_2(self, value=None):
        """  Corresponds to IDD Field `program_line_2`

        Args:
            value (str): value for IDD Field `program_line_2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_line_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_line_2`')

        self._data["Program Line 2"] = value

    @property
    def program_line_2(self):
        """Get program_line_2

        Returns:
            str: the value of `program_line_2` or None if not set
        """
        return self._data["Program Line 2"]

    @program_line_2.setter
    def program_line_2(self, value=None):
        """  Corresponds to IDD Field `program_line_2`

        Args:
            value (str): value for IDD Field `program_line_2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_line_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_line_2`')

        self._data["Program Line 2"] = value

    @property
    def program_line_2(self):
        """Get program_line_2

        Returns:
            str: the value of `program_line_2` or None if not set
        """
        return self._data["Program Line 2"]

    @program_line_2.setter
    def program_line_2(self, value=None):
        """  Corresponds to IDD Field `program_line_2`

        Args:
            value (str): value for IDD Field `program_line_2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_line_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_line_2`')

        self._data["Program Line 2"] = value

    @property
    def program_line_2(self):
        """Get program_line_2

        Returns:
            str: the value of `program_line_2` or None if not set
        """
        return self._data["Program Line 2"]

    @program_line_2.setter
    def program_line_2(self, value=None):
        """  Corresponds to IDD Field `program_line_2`

        Args:
            value (str): value for IDD Field `program_line_2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_line_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_line_2`')

        self._data["Program Line 2"] = value

    @property
    def program_line_2(self):
        """Get program_line_2

        Returns:
            str: the value of `program_line_2` or None if not set
        """
        return self._data["Program Line 2"]

    @program_line_2.setter
    def program_line_2(self, value=None):
        """  Corresponds to IDD Field `program_line_2`

        Args:
            value (str): value for IDD Field `program_line_2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_line_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_line_2`')

        self._data["Program Line 2"] = value

    @property
    def program_line_2(self):
        """Get program_line_2

        Returns:
            str: the value of `program_line_2` or None if not set
        """
        return self._data["Program Line 2"]

    @program_line_2.setter
    def program_line_2(self, value=None):
        """  Corresponds to IDD Field `program_line_2`

        Args:
            value (str): value for IDD Field `program_line_2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_line_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_line_2`')

        self._data["Program Line 2"] = value

    @property
    def program_line_2(self):
        """Get program_line_2

        Returns:
            str: the value of `program_line_2` or None if not set
        """
        return self._data["Program Line 2"]

    @program_line_2.setter
    def program_line_2(self, value=None):
        """  Corresponds to IDD Field `program_line_2`

        Args:
            value (str): value for IDD Field `program_line_2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_line_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_line_2`')

        self._data["Program Line 2"] = value

    @property
    def program_line_2(self):
        """Get program_line_2

        Returns:
            str: the value of `program_line_2` or None if not set
        """
        return self._data["Program Line 2"]

    @program_line_2.setter
    def program_line_2(self, value=None):
        """  Corresponds to IDD Field `program_line_2`

        Args:
            value (str): value for IDD Field `program_line_2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_line_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_line_2`')

        self._data["Program Line 2"] = value

    @property
    def program_line_2(self):
        """Get program_line_2

        Returns:
            str: the value of `program_line_2` or None if not set
        """
        return self._data["Program Line 2"]

    @program_line_2.setter
    def program_line_2(self, value=None):
        """  Corresponds to IDD Field `program_line_2`

        Args:
            value (str): value for IDD Field `program_line_2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_line_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_line_2`')

        self._data["Program Line 2"] = value

    @property
    def program_line_2(self):
        """Get program_line_2

        Returns:
            str: the value of `program_line_2` or None if not set
        """
        return self._data["Program Line 2"]

    @program_line_2.setter
    def program_line_2(self, value=None):
        """  Corresponds to IDD Field `program_line_2`

        Args:
            value (str): value for IDD Field `program_line_2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_line_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_line_2`')

        self._data["Program Line 2"] = value

    @property
    def program_line_2(self):
        """Get program_line_2

        Returns:
            str: the value of `program_line_2` or None if not set
        """
        return self._data["Program Line 2"]

    @program_line_2.setter
    def program_line_2(self, value=None):
        """  Corresponds to IDD Field `program_line_2`

        Args:
            value (str): value for IDD Field `program_line_2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_line_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_line_2`')

        self._data["Program Line 2"] = value

    @property
    def program_line_2(self):
        """Get program_line_2

        Returns:
            str: the value of `program_line_2` or None if not set
        """
        return self._data["Program Line 2"]

    @program_line_2.setter
    def program_line_2(self, value=None):
        """  Corresponds to IDD Field `program_line_2`

        Args:
            value (str): value for IDD Field `program_line_2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_line_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_line_2`')

        self._data["Program Line 2"] = value

    @property
    def program_line_2(self):
        """Get program_line_2

        Returns:
            str: the value of `program_line_2` or None if not set
        """
        return self._data["Program Line 2"]

    @program_line_2.setter
    def program_line_2(self, value=None):
        """  Corresponds to IDD Field `program_line_2`

        Args:
            value (str): value for IDD Field `program_line_2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_line_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_line_2`')

        self._data["Program Line 2"] = value

    @property
    def program_line_2(self):
        """Get program_line_2

        Returns:
            str: the value of `program_line_2` or None if not set
        """
        return self._data["Program Line 2"]

    @program_line_2.setter
    def program_line_2(self, value=None):
        """  Corresponds to IDD Field `program_line_2`

        Args:
            value (str): value for IDD Field `program_line_2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_line_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_line_2`')

        self._data["Program Line 2"] = value

    @property
    def program_line_2(self):
        """Get program_line_2

        Returns:
            str: the value of `program_line_2` or None if not set
        """
        return self._data["Program Line 2"]

    @program_line_2.setter
    def program_line_2(self, value=None):
        """  Corresponds to IDD Field `program_line_2`

        Args:
            value (str): value for IDD Field `program_line_2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_line_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_line_2`')

        self._data["Program Line 2"] = value

    @property
    def program_line_2(self):
        """Get program_line_2

        Returns:
            str: the value of `program_line_2` or None if not set
        """
        return self._data["Program Line 2"]

    @program_line_2.setter
    def program_line_2(self, value=None):
        """  Corresponds to IDD Field `program_line_2`

        Args:
            value (str): value for IDD Field `program_line_2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_line_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_line_2`')

        self._data["Program Line 2"] = value

    @property
    def program_line_2(self):
        """Get program_line_2

        Returns:
            str: the value of `program_line_2` or None if not set
        """
        return self._data["Program Line 2"]

    @program_line_2.setter
    def program_line_2(self, value=None):
        """  Corresponds to IDD Field `program_line_2`

        Args:
            value (str): value for IDD Field `program_line_2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_line_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_line_2`')

        self._data["Program Line 2"] = value

    @property
    def program_line_2(self):
        """Get program_line_2

        Returns:
            str: the value of `program_line_2` or None if not set
        """
        return self._data["Program Line 2"]

    @program_line_2.setter
    def program_line_2(self, value=None):
        """  Corresponds to IDD Field `program_line_2`

        Args:
            value (str): value for IDD Field `program_line_2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_line_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_line_2`')

        self._data["Program Line 2"] = value

    @property
    def program_line_2(self):
        """Get program_line_2

        Returns:
            str: the value of `program_line_2` or None if not set
        """
        return self._data["Program Line 2"]

    @program_line_2.setter
    def program_line_2(self, value=None):
        """  Corresponds to IDD Field `program_line_2`

        Args:
            value (str): value for IDD Field `program_line_2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_line_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_line_2`')

        self._data["Program Line 2"] = value

    @property
    def program_line_2(self):
        """Get program_line_2

        Returns:
            str: the value of `program_line_2` or None if not set
        """
        return self._data["Program Line 2"]

    @program_line_2.setter
    def program_line_2(self, value=None):
        """  Corresponds to IDD Field `program_line_2`

        Args:
            value (str): value for IDD Field `program_line_2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_line_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_line_2`')

        self._data["Program Line 2"] = value

    @property
    def program_line_2(self):
        """Get program_line_2

        Returns:
            str: the value of `program_line_2` or None if not set
        """
        return self._data["Program Line 2"]

    @program_line_2.setter
    def program_line_2(self, value=None):
        """  Corresponds to IDD Field `program_line_2`

        Args:
            value (str): value for IDD Field `program_line_2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_line_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_line_2`')

        self._data["Program Line 2"] = value

    @property
    def program_line_2(self):
        """Get program_line_2

        Returns:
            str: the value of `program_line_2` or None if not set
        """
        return self._data["Program Line 2"]

    @program_line_2.setter
    def program_line_2(self, value=None):
        """  Corresponds to IDD Field `program_line_2`

        Args:
            value (str): value for IDD Field `program_line_2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_line_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_line_2`')

        self._data["Program Line 2"] = value

    @property
    def program_line_2(self):
        """Get program_line_2

        Returns:
            str: the value of `program_line_2` or None if not set
        """
        return self._data["Program Line 2"]

    @program_line_2.setter
    def program_line_2(self, value=None):
        """  Corresponds to IDD Field `program_line_2`

        Args:
            value (str): value for IDD Field `program_line_2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_line_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_line_2`')

        self._data["Program Line 2"] = value

    @property
    def program_line_2(self):
        """Get program_line_2

        Returns:
            str: the value of `program_line_2` or None if not set
        """
        return self._data["Program Line 2"]

    @program_line_2.setter
    def program_line_2(self, value=None):
        """  Corresponds to IDD Field `program_line_2`

        Args:
            value (str): value for IDD Field `program_line_2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_line_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_line_2`')

        self._data["Program Line 2"] = value

    @property
    def program_line_2(self):
        """Get program_line_2

        Returns:
            str: the value of `program_line_2` or None if not set
        """
        return self._data["Program Line 2"]

    @program_line_2.setter
    def program_line_2(self, value=None):
        """  Corresponds to IDD Field `program_line_2`

        Args:
            value (str): value for IDD Field `program_line_2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_line_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_line_2`')

        self._data["Program Line 2"] = value

    @property
    def program_line_2(self):
        """Get program_line_2

        Returns:
            str: the value of `program_line_2` or None if not set
        """
        return self._data["Program Line 2"]

    @program_line_2.setter
    def program_line_2(self, value=None):
        """  Corresponds to IDD Field `program_line_2`

        Args:
            value (str): value for IDD Field `program_line_2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_line_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_line_2`')

        self._data["Program Line 2"] = value

    @property
    def program_line_2(self):
        """Get program_line_2

        Returns:
            str: the value of `program_line_2` or None if not set
        """
        return self._data["Program Line 2"]

    @program_line_2.setter
    def program_line_2(self, value=None):
        """  Corresponds to IDD Field `program_line_2`

        Args:
            value (str): value for IDD Field `program_line_2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_line_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_line_2`')

        self._data["Program Line 2"] = value

    @property
    def program_line_2(self):
        """Get program_line_2

        Returns:
            str: the value of `program_line_2` or None if not set
        """
        return self._data["Program Line 2"]

    @program_line_2.setter
    def program_line_2(self, value=None):
        """  Corresponds to IDD Field `program_line_2`

        Args:
            value (str): value for IDD Field `program_line_2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_line_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_line_2`')

        self._data["Program Line 2"] = value

    @property
    def program_line_2(self):
        """Get program_line_2

        Returns:
            str: the value of `program_line_2` or None if not set
        """
        return self._data["Program Line 2"]

    @program_line_2.setter
    def program_line_2(self, value=None):
        """  Corresponds to IDD Field `program_line_2`

        Args:
            value (str): value for IDD Field `program_line_2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_line_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_line_2`')

        self._data["Program Line 2"] = value

    @property
    def program_line_2(self):
        """Get program_line_2

        Returns:
            str: the value of `program_line_2` or None if not set
        """
        return self._data["Program Line 2"]

    @program_line_2.setter
    def program_line_2(self, value=None):
        """  Corresponds to IDD Field `program_line_2`

        Args:
            value (str): value for IDD Field `program_line_2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_line_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_line_2`')

        self._data["Program Line 2"] = value

    @property
    def program_line_2(self):
        """Get program_line_2

        Returns:
            str: the value of `program_line_2` or None if not set
        """
        return self._data["Program Line 2"]

    @program_line_2.setter
    def program_line_2(self, value=None):
        """  Corresponds to IDD Field `program_line_2`

        Args:
            value (str): value for IDD Field `program_line_2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_line_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_line_2`')

        self._data["Program Line 2"] = value

    @property
    def program_line_2(self):
        """Get program_line_2

        Returns:
            str: the value of `program_line_2` or None if not set
        """
        return self._data["Program Line 2"]

    @program_line_2.setter
    def program_line_2(self, value=None):
        """  Corresponds to IDD Field `program_line_2`

        Args:
            value (str): value for IDD Field `program_line_2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_line_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_line_2`')

        self._data["Program Line 2"] = value

    @property
    def program_line_2(self):
        """Get program_line_2

        Returns:
            str: the value of `program_line_2` or None if not set
        """
        return self._data["Program Line 2"]

    @program_line_2.setter
    def program_line_2(self, value=None):
        """  Corresponds to IDD Field `program_line_2`

        Args:
            value (str): value for IDD Field `program_line_2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_line_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_line_2`')

        self._data["Program Line 2"] = value

    @property
    def program_line_2(self):
        """Get program_line_2

        Returns:
            str: the value of `program_line_2` or None if not set
        """
        return self._data["Program Line 2"]

    @program_line_2.setter
    def program_line_2(self, value=None):
        """  Corresponds to IDD Field `program_line_2`

        Args:
            value (str): value for IDD Field `program_line_2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_line_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_line_2`')

        self._data["Program Line 2"] = value

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

    def __str__(self):
        out = []
        out.append(self._to_str(self.name))
        out.append(self._to_str(self.program_line_1))
        out.append(self._to_str(self.program_line_2))
        out.append(self._to_str(self.program_line_2))
        out.append(self._to_str(self.program_line_2))
        out.append(self._to_str(self.program_line_2))
        out.append(self._to_str(self.program_line_2))
        out.append(self._to_str(self.program_line_2))
        out.append(self._to_str(self.program_line_2))
        out.append(self._to_str(self.program_line_2))
        out.append(self._to_str(self.program_line_2))
        out.append(self._to_str(self.program_line_2))
        out.append(self._to_str(self.program_line_2))
        out.append(self._to_str(self.program_line_2))
        out.append(self._to_str(self.program_line_2))
        out.append(self._to_str(self.program_line_2))
        out.append(self._to_str(self.program_line_2))
        out.append(self._to_str(self.program_line_2))
        out.append(self._to_str(self.program_line_2))
        out.append(self._to_str(self.program_line_2))
        out.append(self._to_str(self.program_line_2))
        out.append(self._to_str(self.program_line_2))
        out.append(self._to_str(self.program_line_2))
        out.append(self._to_str(self.program_line_2))
        out.append(self._to_str(self.program_line_2))
        out.append(self._to_str(self.program_line_2))
        out.append(self._to_str(self.program_line_2))
        out.append(self._to_str(self.program_line_2))
        out.append(self._to_str(self.program_line_2))
        out.append(self._to_str(self.program_line_2))
        out.append(self._to_str(self.program_line_2))
        out.append(self._to_str(self.program_line_2))
        out.append(self._to_str(self.program_line_2))
        out.append(self._to_str(self.program_line_2))
        out.append(self._to_str(self.program_line_2))
        out.append(self._to_str(self.program_line_2))
        out.append(self._to_str(self.program_line_2))
        out.append(self._to_str(self.program_line_2))
        out.append(self._to_str(self.program_line_2))
        out.append(self._to_str(self.program_line_2))
        out.append(self._to_str(self.program_line_2))
        out.append(self._to_str(self.program_line_2))
        out.append(self._to_str(self.program_line_2))
        out.append(self._to_str(self.program_line_2))
        out.append(self._to_str(self.program_line_2))
        out.append(self._to_str(self.program_line_2))
        out.append(self._to_str(self.program_line_2))
        out.append(self._to_str(self.program_line_2))
        out.append(self._to_str(self.program_line_2))
        return ",".join(out)

class EnergyManagementSystemSubroutine(object):
    """ Corresponds to IDD object `EnergyManagementSystem:Subroutine`
        This input defines an Erl program subroutine
        Each field after the name is a line of EMS Runtime Language
    """
    internal_name = "EnergyManagementSystem:Subroutine"
    field_count = 11

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `EnergyManagementSystem:Subroutine`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Program Line 1"] = None
        self._data["Program Line 2"] = None
        self._data["Program Line 2"] = None
        self._data["Program Line 2"] = None
        self._data["Program Line 2"] = None
        self._data["Program Line 2"] = None
        self._data["Program Line 2"] = None
        self._data["Program Line 2"] = None
        self._data["Program Line 2"] = None
        self._data["Program Line 2"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.program_line_1 = None
        else:
            self.program_line_1 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.program_line_2 = None
        else:
            self.program_line_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.program_line_2 = None
        else:
            self.program_line_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.program_line_2 = None
        else:
            self.program_line_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.program_line_2 = None
        else:
            self.program_line_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.program_line_2 = None
        else:
            self.program_line_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.program_line_2 = None
        else:
            self.program_line_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.program_line_2 = None
        else:
            self.program_line_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.program_line_2 = None
        else:
            self.program_line_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.program_line_2 = None
        else:
            self.program_line_2 = vals[i]
        i += 1

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `name`
        no spaces allowed in name

        Args:
            value (str): value for IDD Field `name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')

        self._data["Name"] = value

    @property
    def program_line_1(self):
        """Get program_line_1

        Returns:
            str: the value of `program_line_1` or None if not set
        """
        return self._data["Program Line 1"]

    @program_line_1.setter
    def program_line_1(self, value=None):
        """  Corresponds to IDD Field `program_line_1`

        Args:
            value (str): value for IDD Field `program_line_1`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_line_1`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_line_1`')

        self._data["Program Line 1"] = value

    @property
    def program_line_2(self):
        """Get program_line_2

        Returns:
            str: the value of `program_line_2` or None if not set
        """
        return self._data["Program Line 2"]

    @program_line_2.setter
    def program_line_2(self, value=None):
        """  Corresponds to IDD Field `program_line_2`
        repeats

        Args:
            value (str): value for IDD Field `program_line_2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_line_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_line_2`')

        self._data["Program Line 2"] = value

    @property
    def program_line_2(self):
        """Get program_line_2

        Returns:
            str: the value of `program_line_2` or None if not set
        """
        return self._data["Program Line 2"]

    @program_line_2.setter
    def program_line_2(self, value=None):
        """  Corresponds to IDD Field `program_line_2`
        repeats

        Args:
            value (str): value for IDD Field `program_line_2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_line_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_line_2`')

        self._data["Program Line 2"] = value

    @property
    def program_line_2(self):
        """Get program_line_2

        Returns:
            str: the value of `program_line_2` or None if not set
        """
        return self._data["Program Line 2"]

    @program_line_2.setter
    def program_line_2(self, value=None):
        """  Corresponds to IDD Field `program_line_2`
        repeats

        Args:
            value (str): value for IDD Field `program_line_2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_line_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_line_2`')

        self._data["Program Line 2"] = value

    @property
    def program_line_2(self):
        """Get program_line_2

        Returns:
            str: the value of `program_line_2` or None if not set
        """
        return self._data["Program Line 2"]

    @program_line_2.setter
    def program_line_2(self, value=None):
        """  Corresponds to IDD Field `program_line_2`
        repeats

        Args:
            value (str): value for IDD Field `program_line_2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_line_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_line_2`')

        self._data["Program Line 2"] = value

    @property
    def program_line_2(self):
        """Get program_line_2

        Returns:
            str: the value of `program_line_2` or None if not set
        """
        return self._data["Program Line 2"]

    @program_line_2.setter
    def program_line_2(self, value=None):
        """  Corresponds to IDD Field `program_line_2`
        repeats

        Args:
            value (str): value for IDD Field `program_line_2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_line_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_line_2`')

        self._data["Program Line 2"] = value

    @property
    def program_line_2(self):
        """Get program_line_2

        Returns:
            str: the value of `program_line_2` or None if not set
        """
        return self._data["Program Line 2"]

    @program_line_2.setter
    def program_line_2(self, value=None):
        """  Corresponds to IDD Field `program_line_2`
        repeats

        Args:
            value (str): value for IDD Field `program_line_2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_line_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_line_2`')

        self._data["Program Line 2"] = value

    @property
    def program_line_2(self):
        """Get program_line_2

        Returns:
            str: the value of `program_line_2` or None if not set
        """
        return self._data["Program Line 2"]

    @program_line_2.setter
    def program_line_2(self, value=None):
        """  Corresponds to IDD Field `program_line_2`
        repeats

        Args:
            value (str): value for IDD Field `program_line_2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_line_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_line_2`')

        self._data["Program Line 2"] = value

    @property
    def program_line_2(self):
        """Get program_line_2

        Returns:
            str: the value of `program_line_2` or None if not set
        """
        return self._data["Program Line 2"]

    @program_line_2.setter
    def program_line_2(self, value=None):
        """  Corresponds to IDD Field `program_line_2`
        repeats

        Args:
            value (str): value for IDD Field `program_line_2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_line_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_line_2`')

        self._data["Program Line 2"] = value

    @property
    def program_line_2(self):
        """Get program_line_2

        Returns:
            str: the value of `program_line_2` or None if not set
        """
        return self._data["Program Line 2"]

    @program_line_2.setter
    def program_line_2(self, value=None):
        """  Corresponds to IDD Field `program_line_2`
        repeats

        Args:
            value (str): value for IDD Field `program_line_2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `program_line_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `program_line_2`')

        self._data["Program Line 2"] = value

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

    def __str__(self):
        out = []
        out.append(self._to_str(self.name))
        out.append(self._to_str(self.program_line_1))
        out.append(self._to_str(self.program_line_2))
        out.append(self._to_str(self.program_line_2))
        out.append(self._to_str(self.program_line_2))
        out.append(self._to_str(self.program_line_2))
        out.append(self._to_str(self.program_line_2))
        out.append(self._to_str(self.program_line_2))
        out.append(self._to_str(self.program_line_2))
        out.append(self._to_str(self.program_line_2))
        out.append(self._to_str(self.program_line_2))
        return ",".join(out)

class EnergyManagementSystemGlobalVariable(object):
    """ Corresponds to IDD object `EnergyManagementSystem:GlobalVariable`
        Declares Erl variable as having global scope
        No spaces allowed in names used for Erl variables
    """
    internal_name = "EnergyManagementSystem:GlobalVariable"
    field_count = 49

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `EnergyManagementSystem:GlobalVariable`
        """
        self._data = OrderedDict()
        self._data["Erl Variable 1 Name"] = None
        self._data["Erl Variable 2 Name"] = None
        self._data["Erl Variable 3 Name"] = None
        self._data["Erl Variable 3 Name"] = None
        self._data["Erl Variable 3 Name"] = None
        self._data["Erl Variable 3 Name"] = None
        self._data["Erl Variable 3 Name"] = None
        self._data["Erl Variable 3 Name"] = None
        self._data["Erl Variable 3 Name"] = None
        self._data["Erl Variable 3 Name"] = None
        self._data["Erl Variable 3 Name"] = None
        self._data["Erl Variable 3 Name"] = None
        self._data["Erl Variable 3 Name"] = None
        self._data["Erl Variable 3 Name"] = None
        self._data["Erl Variable 3 Name"] = None
        self._data["Erl Variable 3 Name"] = None
        self._data["Erl Variable 3 Name"] = None
        self._data["Erl Variable 3 Name"] = None
        self._data["Erl Variable 3 Name"] = None
        self._data["Erl Variable 3 Name"] = None
        self._data["Erl Variable 3 Name"] = None
        self._data["Erl Variable 3 Name"] = None
        self._data["Erl Variable 3 Name"] = None
        self._data["Erl Variable 3 Name"] = None
        self._data["Erl Variable 3 Name"] = None
        self._data["Erl Variable 3 Name"] = None
        self._data["Erl Variable 3 Name"] = None
        self._data["Erl Variable 3 Name"] = None
        self._data["Erl Variable 3 Name"] = None
        self._data["Erl Variable 3 Name"] = None
        self._data["Erl Variable 3 Name"] = None
        self._data["Erl Variable 3 Name"] = None
        self._data["Erl Variable 3 Name"] = None
        self._data["Erl Variable 3 Name"] = None
        self._data["Erl Variable 3 Name"] = None
        self._data["Erl Variable 3 Name"] = None
        self._data["Erl Variable 3 Name"] = None
        self._data["Erl Variable 3 Name"] = None
        self._data["Erl Variable 3 Name"] = None
        self._data["Erl Variable 3 Name"] = None
        self._data["Erl Variable 3 Name"] = None
        self._data["Erl Variable 3 Name"] = None
        self._data["Erl Variable 3 Name"] = None
        self._data["Erl Variable 3 Name"] = None
        self._data["Erl Variable 3 Name"] = None
        self._data["Erl Variable 3 Name"] = None
        self._data["Erl Variable 3 Name"] = None
        self._data["Erl Variable 3 Name"] = None
        self._data["Erl Variable 3 Name"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.erl_variable_1_name = None
        else:
            self.erl_variable_1_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.erl_variable_2_name = None
        else:
            self.erl_variable_2_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.erl_variable_3_name = None
        else:
            self.erl_variable_3_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.erl_variable_3_name = None
        else:
            self.erl_variable_3_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.erl_variable_3_name = None
        else:
            self.erl_variable_3_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.erl_variable_3_name = None
        else:
            self.erl_variable_3_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.erl_variable_3_name = None
        else:
            self.erl_variable_3_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.erl_variable_3_name = None
        else:
            self.erl_variable_3_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.erl_variable_3_name = None
        else:
            self.erl_variable_3_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.erl_variable_3_name = None
        else:
            self.erl_variable_3_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.erl_variable_3_name = None
        else:
            self.erl_variable_3_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.erl_variable_3_name = None
        else:
            self.erl_variable_3_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.erl_variable_3_name = None
        else:
            self.erl_variable_3_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.erl_variable_3_name = None
        else:
            self.erl_variable_3_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.erl_variable_3_name = None
        else:
            self.erl_variable_3_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.erl_variable_3_name = None
        else:
            self.erl_variable_3_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.erl_variable_3_name = None
        else:
            self.erl_variable_3_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.erl_variable_3_name = None
        else:
            self.erl_variable_3_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.erl_variable_3_name = None
        else:
            self.erl_variable_3_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.erl_variable_3_name = None
        else:
            self.erl_variable_3_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.erl_variable_3_name = None
        else:
            self.erl_variable_3_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.erl_variable_3_name = None
        else:
            self.erl_variable_3_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.erl_variable_3_name = None
        else:
            self.erl_variable_3_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.erl_variable_3_name = None
        else:
            self.erl_variable_3_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.erl_variable_3_name = None
        else:
            self.erl_variable_3_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.erl_variable_3_name = None
        else:
            self.erl_variable_3_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.erl_variable_3_name = None
        else:
            self.erl_variable_3_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.erl_variable_3_name = None
        else:
            self.erl_variable_3_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.erl_variable_3_name = None
        else:
            self.erl_variable_3_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.erl_variable_3_name = None
        else:
            self.erl_variable_3_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.erl_variable_3_name = None
        else:
            self.erl_variable_3_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.erl_variable_3_name = None
        else:
            self.erl_variable_3_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.erl_variable_3_name = None
        else:
            self.erl_variable_3_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.erl_variable_3_name = None
        else:
            self.erl_variable_3_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.erl_variable_3_name = None
        else:
            self.erl_variable_3_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.erl_variable_3_name = None
        else:
            self.erl_variable_3_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.erl_variable_3_name = None
        else:
            self.erl_variable_3_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.erl_variable_3_name = None
        else:
            self.erl_variable_3_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.erl_variable_3_name = None
        else:
            self.erl_variable_3_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.erl_variable_3_name = None
        else:
            self.erl_variable_3_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.erl_variable_3_name = None
        else:
            self.erl_variable_3_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.erl_variable_3_name = None
        else:
            self.erl_variable_3_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.erl_variable_3_name = None
        else:
            self.erl_variable_3_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.erl_variable_3_name = None
        else:
            self.erl_variable_3_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.erl_variable_3_name = None
        else:
            self.erl_variable_3_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.erl_variable_3_name = None
        else:
            self.erl_variable_3_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.erl_variable_3_name = None
        else:
            self.erl_variable_3_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.erl_variable_3_name = None
        else:
            self.erl_variable_3_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.erl_variable_3_name = None
        else:
            self.erl_variable_3_name = vals[i]
        i += 1

    @property
    def erl_variable_1_name(self):
        """Get erl_variable_1_name

        Returns:
            str: the value of `erl_variable_1_name` or None if not set
        """
        return self._data["Erl Variable 1 Name"]

    @erl_variable_1_name.setter
    def erl_variable_1_name(self, value=None):
        """  Corresponds to IDD Field `erl_variable_1_name`
        no spaces allowed in name

        Args:
            value (str): value for IDD Field `erl_variable_1_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `erl_variable_1_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `erl_variable_1_name`')

        self._data["Erl Variable 1 Name"] = value

    @property
    def erl_variable_2_name(self):
        """Get erl_variable_2_name

        Returns:
            str: the value of `erl_variable_2_name` or None if not set
        """
        return self._data["Erl Variable 2 Name"]

    @erl_variable_2_name.setter
    def erl_variable_2_name(self, value=None):
        """  Corresponds to IDD Field `erl_variable_2_name`

        Args:
            value (str): value for IDD Field `erl_variable_2_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `erl_variable_2_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `erl_variable_2_name`')

        self._data["Erl Variable 2 Name"] = value

    @property
    def erl_variable_3_name(self):
        """Get erl_variable_3_name

        Returns:
            str: the value of `erl_variable_3_name` or None if not set
        """
        return self._data["Erl Variable 3 Name"]

    @erl_variable_3_name.setter
    def erl_variable_3_name(self, value=None):
        """  Corresponds to IDD Field `erl_variable_3_name`
        repeats

        Args:
            value (str): value for IDD Field `erl_variable_3_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `erl_variable_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `erl_variable_3_name`')

        self._data["Erl Variable 3 Name"] = value

    @property
    def erl_variable_3_name(self):
        """Get erl_variable_3_name

        Returns:
            str: the value of `erl_variable_3_name` or None if not set
        """
        return self._data["Erl Variable 3 Name"]

    @erl_variable_3_name.setter
    def erl_variable_3_name(self, value=None):
        """  Corresponds to IDD Field `erl_variable_3_name`
        repeats

        Args:
            value (str): value for IDD Field `erl_variable_3_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `erl_variable_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `erl_variable_3_name`')

        self._data["Erl Variable 3 Name"] = value

    @property
    def erl_variable_3_name(self):
        """Get erl_variable_3_name

        Returns:
            str: the value of `erl_variable_3_name` or None if not set
        """
        return self._data["Erl Variable 3 Name"]

    @erl_variable_3_name.setter
    def erl_variable_3_name(self, value=None):
        """  Corresponds to IDD Field `erl_variable_3_name`
        repeats

        Args:
            value (str): value for IDD Field `erl_variable_3_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `erl_variable_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `erl_variable_3_name`')

        self._data["Erl Variable 3 Name"] = value

    @property
    def erl_variable_3_name(self):
        """Get erl_variable_3_name

        Returns:
            str: the value of `erl_variable_3_name` or None if not set
        """
        return self._data["Erl Variable 3 Name"]

    @erl_variable_3_name.setter
    def erl_variable_3_name(self, value=None):
        """  Corresponds to IDD Field `erl_variable_3_name`
        repeats

        Args:
            value (str): value for IDD Field `erl_variable_3_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `erl_variable_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `erl_variable_3_name`')

        self._data["Erl Variable 3 Name"] = value

    @property
    def erl_variable_3_name(self):
        """Get erl_variable_3_name

        Returns:
            str: the value of `erl_variable_3_name` or None if not set
        """
        return self._data["Erl Variable 3 Name"]

    @erl_variable_3_name.setter
    def erl_variable_3_name(self, value=None):
        """  Corresponds to IDD Field `erl_variable_3_name`
        repeats

        Args:
            value (str): value for IDD Field `erl_variable_3_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `erl_variable_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `erl_variable_3_name`')

        self._data["Erl Variable 3 Name"] = value

    @property
    def erl_variable_3_name(self):
        """Get erl_variable_3_name

        Returns:
            str: the value of `erl_variable_3_name` or None if not set
        """
        return self._data["Erl Variable 3 Name"]

    @erl_variable_3_name.setter
    def erl_variable_3_name(self, value=None):
        """  Corresponds to IDD Field `erl_variable_3_name`
        repeats

        Args:
            value (str): value for IDD Field `erl_variable_3_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `erl_variable_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `erl_variable_3_name`')

        self._data["Erl Variable 3 Name"] = value

    @property
    def erl_variable_3_name(self):
        """Get erl_variable_3_name

        Returns:
            str: the value of `erl_variable_3_name` or None if not set
        """
        return self._data["Erl Variable 3 Name"]

    @erl_variable_3_name.setter
    def erl_variable_3_name(self, value=None):
        """  Corresponds to IDD Field `erl_variable_3_name`
        repeats

        Args:
            value (str): value for IDD Field `erl_variable_3_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `erl_variable_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `erl_variable_3_name`')

        self._data["Erl Variable 3 Name"] = value

    @property
    def erl_variable_3_name(self):
        """Get erl_variable_3_name

        Returns:
            str: the value of `erl_variable_3_name` or None if not set
        """
        return self._data["Erl Variable 3 Name"]

    @erl_variable_3_name.setter
    def erl_variable_3_name(self, value=None):
        """  Corresponds to IDD Field `erl_variable_3_name`
        repeats

        Args:
            value (str): value for IDD Field `erl_variable_3_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `erl_variable_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `erl_variable_3_name`')

        self._data["Erl Variable 3 Name"] = value

    @property
    def erl_variable_3_name(self):
        """Get erl_variable_3_name

        Returns:
            str: the value of `erl_variable_3_name` or None if not set
        """
        return self._data["Erl Variable 3 Name"]

    @erl_variable_3_name.setter
    def erl_variable_3_name(self, value=None):
        """  Corresponds to IDD Field `erl_variable_3_name`
        repeats

        Args:
            value (str): value for IDD Field `erl_variable_3_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `erl_variable_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `erl_variable_3_name`')

        self._data["Erl Variable 3 Name"] = value

    @property
    def erl_variable_3_name(self):
        """Get erl_variable_3_name

        Returns:
            str: the value of `erl_variable_3_name` or None if not set
        """
        return self._data["Erl Variable 3 Name"]

    @erl_variable_3_name.setter
    def erl_variable_3_name(self, value=None):
        """  Corresponds to IDD Field `erl_variable_3_name`
        repeats

        Args:
            value (str): value for IDD Field `erl_variable_3_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `erl_variable_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `erl_variable_3_name`')

        self._data["Erl Variable 3 Name"] = value

    @property
    def erl_variable_3_name(self):
        """Get erl_variable_3_name

        Returns:
            str: the value of `erl_variable_3_name` or None if not set
        """
        return self._data["Erl Variable 3 Name"]

    @erl_variable_3_name.setter
    def erl_variable_3_name(self, value=None):
        """  Corresponds to IDD Field `erl_variable_3_name`
        repeats

        Args:
            value (str): value for IDD Field `erl_variable_3_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `erl_variable_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `erl_variable_3_name`')

        self._data["Erl Variable 3 Name"] = value

    @property
    def erl_variable_3_name(self):
        """Get erl_variable_3_name

        Returns:
            str: the value of `erl_variable_3_name` or None if not set
        """
        return self._data["Erl Variable 3 Name"]

    @erl_variable_3_name.setter
    def erl_variable_3_name(self, value=None):
        """  Corresponds to IDD Field `erl_variable_3_name`
        repeats

        Args:
            value (str): value for IDD Field `erl_variable_3_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `erl_variable_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `erl_variable_3_name`')

        self._data["Erl Variable 3 Name"] = value

    @property
    def erl_variable_3_name(self):
        """Get erl_variable_3_name

        Returns:
            str: the value of `erl_variable_3_name` or None if not set
        """
        return self._data["Erl Variable 3 Name"]

    @erl_variable_3_name.setter
    def erl_variable_3_name(self, value=None):
        """  Corresponds to IDD Field `erl_variable_3_name`
        repeats

        Args:
            value (str): value for IDD Field `erl_variable_3_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `erl_variable_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `erl_variable_3_name`')

        self._data["Erl Variable 3 Name"] = value

    @property
    def erl_variable_3_name(self):
        """Get erl_variable_3_name

        Returns:
            str: the value of `erl_variable_3_name` or None if not set
        """
        return self._data["Erl Variable 3 Name"]

    @erl_variable_3_name.setter
    def erl_variable_3_name(self, value=None):
        """  Corresponds to IDD Field `erl_variable_3_name`
        repeats

        Args:
            value (str): value for IDD Field `erl_variable_3_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `erl_variable_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `erl_variable_3_name`')

        self._data["Erl Variable 3 Name"] = value

    @property
    def erl_variable_3_name(self):
        """Get erl_variable_3_name

        Returns:
            str: the value of `erl_variable_3_name` or None if not set
        """
        return self._data["Erl Variable 3 Name"]

    @erl_variable_3_name.setter
    def erl_variable_3_name(self, value=None):
        """  Corresponds to IDD Field `erl_variable_3_name`
        repeats

        Args:
            value (str): value for IDD Field `erl_variable_3_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `erl_variable_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `erl_variable_3_name`')

        self._data["Erl Variable 3 Name"] = value

    @property
    def erl_variable_3_name(self):
        """Get erl_variable_3_name

        Returns:
            str: the value of `erl_variable_3_name` or None if not set
        """
        return self._data["Erl Variable 3 Name"]

    @erl_variable_3_name.setter
    def erl_variable_3_name(self, value=None):
        """  Corresponds to IDD Field `erl_variable_3_name`
        repeats

        Args:
            value (str): value for IDD Field `erl_variable_3_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `erl_variable_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `erl_variable_3_name`')

        self._data["Erl Variable 3 Name"] = value

    @property
    def erl_variable_3_name(self):
        """Get erl_variable_3_name

        Returns:
            str: the value of `erl_variable_3_name` or None if not set
        """
        return self._data["Erl Variable 3 Name"]

    @erl_variable_3_name.setter
    def erl_variable_3_name(self, value=None):
        """  Corresponds to IDD Field `erl_variable_3_name`
        repeats

        Args:
            value (str): value for IDD Field `erl_variable_3_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `erl_variable_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `erl_variable_3_name`')

        self._data["Erl Variable 3 Name"] = value

    @property
    def erl_variable_3_name(self):
        """Get erl_variable_3_name

        Returns:
            str: the value of `erl_variable_3_name` or None if not set
        """
        return self._data["Erl Variable 3 Name"]

    @erl_variable_3_name.setter
    def erl_variable_3_name(self, value=None):
        """  Corresponds to IDD Field `erl_variable_3_name`
        repeats

        Args:
            value (str): value for IDD Field `erl_variable_3_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `erl_variable_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `erl_variable_3_name`')

        self._data["Erl Variable 3 Name"] = value

    @property
    def erl_variable_3_name(self):
        """Get erl_variable_3_name

        Returns:
            str: the value of `erl_variable_3_name` or None if not set
        """
        return self._data["Erl Variable 3 Name"]

    @erl_variable_3_name.setter
    def erl_variable_3_name(self, value=None):
        """  Corresponds to IDD Field `erl_variable_3_name`
        repeats

        Args:
            value (str): value for IDD Field `erl_variable_3_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `erl_variable_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `erl_variable_3_name`')

        self._data["Erl Variable 3 Name"] = value

    @property
    def erl_variable_3_name(self):
        """Get erl_variable_3_name

        Returns:
            str: the value of `erl_variable_3_name` or None if not set
        """
        return self._data["Erl Variable 3 Name"]

    @erl_variable_3_name.setter
    def erl_variable_3_name(self, value=None):
        """  Corresponds to IDD Field `erl_variable_3_name`
        repeats

        Args:
            value (str): value for IDD Field `erl_variable_3_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `erl_variable_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `erl_variable_3_name`')

        self._data["Erl Variable 3 Name"] = value

    @property
    def erl_variable_3_name(self):
        """Get erl_variable_3_name

        Returns:
            str: the value of `erl_variable_3_name` or None if not set
        """
        return self._data["Erl Variable 3 Name"]

    @erl_variable_3_name.setter
    def erl_variable_3_name(self, value=None):
        """  Corresponds to IDD Field `erl_variable_3_name`
        repeats

        Args:
            value (str): value for IDD Field `erl_variable_3_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `erl_variable_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `erl_variable_3_name`')

        self._data["Erl Variable 3 Name"] = value

    @property
    def erl_variable_3_name(self):
        """Get erl_variable_3_name

        Returns:
            str: the value of `erl_variable_3_name` or None if not set
        """
        return self._data["Erl Variable 3 Name"]

    @erl_variable_3_name.setter
    def erl_variable_3_name(self, value=None):
        """  Corresponds to IDD Field `erl_variable_3_name`
        repeats

        Args:
            value (str): value for IDD Field `erl_variable_3_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `erl_variable_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `erl_variable_3_name`')

        self._data["Erl Variable 3 Name"] = value

    @property
    def erl_variable_3_name(self):
        """Get erl_variable_3_name

        Returns:
            str: the value of `erl_variable_3_name` or None if not set
        """
        return self._data["Erl Variable 3 Name"]

    @erl_variable_3_name.setter
    def erl_variable_3_name(self, value=None):
        """  Corresponds to IDD Field `erl_variable_3_name`
        repeats

        Args:
            value (str): value for IDD Field `erl_variable_3_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `erl_variable_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `erl_variable_3_name`')

        self._data["Erl Variable 3 Name"] = value

    @property
    def erl_variable_3_name(self):
        """Get erl_variable_3_name

        Returns:
            str: the value of `erl_variable_3_name` or None if not set
        """
        return self._data["Erl Variable 3 Name"]

    @erl_variable_3_name.setter
    def erl_variable_3_name(self, value=None):
        """  Corresponds to IDD Field `erl_variable_3_name`
        repeats

        Args:
            value (str): value for IDD Field `erl_variable_3_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `erl_variable_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `erl_variable_3_name`')

        self._data["Erl Variable 3 Name"] = value

    @property
    def erl_variable_3_name(self):
        """Get erl_variable_3_name

        Returns:
            str: the value of `erl_variable_3_name` or None if not set
        """
        return self._data["Erl Variable 3 Name"]

    @erl_variable_3_name.setter
    def erl_variable_3_name(self, value=None):
        """  Corresponds to IDD Field `erl_variable_3_name`
        repeats

        Args:
            value (str): value for IDD Field `erl_variable_3_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `erl_variable_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `erl_variable_3_name`')

        self._data["Erl Variable 3 Name"] = value

    @property
    def erl_variable_3_name(self):
        """Get erl_variable_3_name

        Returns:
            str: the value of `erl_variable_3_name` or None if not set
        """
        return self._data["Erl Variable 3 Name"]

    @erl_variable_3_name.setter
    def erl_variable_3_name(self, value=None):
        """  Corresponds to IDD Field `erl_variable_3_name`
        repeats

        Args:
            value (str): value for IDD Field `erl_variable_3_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `erl_variable_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `erl_variable_3_name`')

        self._data["Erl Variable 3 Name"] = value

    @property
    def erl_variable_3_name(self):
        """Get erl_variable_3_name

        Returns:
            str: the value of `erl_variable_3_name` or None if not set
        """
        return self._data["Erl Variable 3 Name"]

    @erl_variable_3_name.setter
    def erl_variable_3_name(self, value=None):
        """  Corresponds to IDD Field `erl_variable_3_name`
        repeats

        Args:
            value (str): value for IDD Field `erl_variable_3_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `erl_variable_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `erl_variable_3_name`')

        self._data["Erl Variable 3 Name"] = value

    @property
    def erl_variable_3_name(self):
        """Get erl_variable_3_name

        Returns:
            str: the value of `erl_variable_3_name` or None if not set
        """
        return self._data["Erl Variable 3 Name"]

    @erl_variable_3_name.setter
    def erl_variable_3_name(self, value=None):
        """  Corresponds to IDD Field `erl_variable_3_name`
        repeats

        Args:
            value (str): value for IDD Field `erl_variable_3_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `erl_variable_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `erl_variable_3_name`')

        self._data["Erl Variable 3 Name"] = value

    @property
    def erl_variable_3_name(self):
        """Get erl_variable_3_name

        Returns:
            str: the value of `erl_variable_3_name` or None if not set
        """
        return self._data["Erl Variable 3 Name"]

    @erl_variable_3_name.setter
    def erl_variable_3_name(self, value=None):
        """  Corresponds to IDD Field `erl_variable_3_name`
        repeats

        Args:
            value (str): value for IDD Field `erl_variable_3_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `erl_variable_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `erl_variable_3_name`')

        self._data["Erl Variable 3 Name"] = value

    @property
    def erl_variable_3_name(self):
        """Get erl_variable_3_name

        Returns:
            str: the value of `erl_variable_3_name` or None if not set
        """
        return self._data["Erl Variable 3 Name"]

    @erl_variable_3_name.setter
    def erl_variable_3_name(self, value=None):
        """  Corresponds to IDD Field `erl_variable_3_name`
        repeats

        Args:
            value (str): value for IDD Field `erl_variable_3_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `erl_variable_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `erl_variable_3_name`')

        self._data["Erl Variable 3 Name"] = value

    @property
    def erl_variable_3_name(self):
        """Get erl_variable_3_name

        Returns:
            str: the value of `erl_variable_3_name` or None if not set
        """
        return self._data["Erl Variable 3 Name"]

    @erl_variable_3_name.setter
    def erl_variable_3_name(self, value=None):
        """  Corresponds to IDD Field `erl_variable_3_name`
        repeats

        Args:
            value (str): value for IDD Field `erl_variable_3_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `erl_variable_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `erl_variable_3_name`')

        self._data["Erl Variable 3 Name"] = value

    @property
    def erl_variable_3_name(self):
        """Get erl_variable_3_name

        Returns:
            str: the value of `erl_variable_3_name` or None if not set
        """
        return self._data["Erl Variable 3 Name"]

    @erl_variable_3_name.setter
    def erl_variable_3_name(self, value=None):
        """  Corresponds to IDD Field `erl_variable_3_name`
        repeats

        Args:
            value (str): value for IDD Field `erl_variable_3_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `erl_variable_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `erl_variable_3_name`')

        self._data["Erl Variable 3 Name"] = value

    @property
    def erl_variable_3_name(self):
        """Get erl_variable_3_name

        Returns:
            str: the value of `erl_variable_3_name` or None if not set
        """
        return self._data["Erl Variable 3 Name"]

    @erl_variable_3_name.setter
    def erl_variable_3_name(self, value=None):
        """  Corresponds to IDD Field `erl_variable_3_name`
        repeats

        Args:
            value (str): value for IDD Field `erl_variable_3_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `erl_variable_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `erl_variable_3_name`')

        self._data["Erl Variable 3 Name"] = value

    @property
    def erl_variable_3_name(self):
        """Get erl_variable_3_name

        Returns:
            str: the value of `erl_variable_3_name` or None if not set
        """
        return self._data["Erl Variable 3 Name"]

    @erl_variable_3_name.setter
    def erl_variable_3_name(self, value=None):
        """  Corresponds to IDD Field `erl_variable_3_name`
        repeats

        Args:
            value (str): value for IDD Field `erl_variable_3_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `erl_variable_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `erl_variable_3_name`')

        self._data["Erl Variable 3 Name"] = value

    @property
    def erl_variable_3_name(self):
        """Get erl_variable_3_name

        Returns:
            str: the value of `erl_variable_3_name` or None if not set
        """
        return self._data["Erl Variable 3 Name"]

    @erl_variable_3_name.setter
    def erl_variable_3_name(self, value=None):
        """  Corresponds to IDD Field `erl_variable_3_name`
        repeats

        Args:
            value (str): value for IDD Field `erl_variable_3_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `erl_variable_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `erl_variable_3_name`')

        self._data["Erl Variable 3 Name"] = value

    @property
    def erl_variable_3_name(self):
        """Get erl_variable_3_name

        Returns:
            str: the value of `erl_variable_3_name` or None if not set
        """
        return self._data["Erl Variable 3 Name"]

    @erl_variable_3_name.setter
    def erl_variable_3_name(self, value=None):
        """  Corresponds to IDD Field `erl_variable_3_name`
        repeats

        Args:
            value (str): value for IDD Field `erl_variable_3_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `erl_variable_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `erl_variable_3_name`')

        self._data["Erl Variable 3 Name"] = value

    @property
    def erl_variable_3_name(self):
        """Get erl_variable_3_name

        Returns:
            str: the value of `erl_variable_3_name` or None if not set
        """
        return self._data["Erl Variable 3 Name"]

    @erl_variable_3_name.setter
    def erl_variable_3_name(self, value=None):
        """  Corresponds to IDD Field `erl_variable_3_name`
        repeats

        Args:
            value (str): value for IDD Field `erl_variable_3_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `erl_variable_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `erl_variable_3_name`')

        self._data["Erl Variable 3 Name"] = value

    @property
    def erl_variable_3_name(self):
        """Get erl_variable_3_name

        Returns:
            str: the value of `erl_variable_3_name` or None if not set
        """
        return self._data["Erl Variable 3 Name"]

    @erl_variable_3_name.setter
    def erl_variable_3_name(self, value=None):
        """  Corresponds to IDD Field `erl_variable_3_name`
        repeats

        Args:
            value (str): value for IDD Field `erl_variable_3_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `erl_variable_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `erl_variable_3_name`')

        self._data["Erl Variable 3 Name"] = value

    @property
    def erl_variable_3_name(self):
        """Get erl_variable_3_name

        Returns:
            str: the value of `erl_variable_3_name` or None if not set
        """
        return self._data["Erl Variable 3 Name"]

    @erl_variable_3_name.setter
    def erl_variable_3_name(self, value=None):
        """  Corresponds to IDD Field `erl_variable_3_name`
        repeats

        Args:
            value (str): value for IDD Field `erl_variable_3_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `erl_variable_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `erl_variable_3_name`')

        self._data["Erl Variable 3 Name"] = value

    @property
    def erl_variable_3_name(self):
        """Get erl_variable_3_name

        Returns:
            str: the value of `erl_variable_3_name` or None if not set
        """
        return self._data["Erl Variable 3 Name"]

    @erl_variable_3_name.setter
    def erl_variable_3_name(self, value=None):
        """  Corresponds to IDD Field `erl_variable_3_name`
        repeats

        Args:
            value (str): value for IDD Field `erl_variable_3_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `erl_variable_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `erl_variable_3_name`')

        self._data["Erl Variable 3 Name"] = value

    @property
    def erl_variable_3_name(self):
        """Get erl_variable_3_name

        Returns:
            str: the value of `erl_variable_3_name` or None if not set
        """
        return self._data["Erl Variable 3 Name"]

    @erl_variable_3_name.setter
    def erl_variable_3_name(self, value=None):
        """  Corresponds to IDD Field `erl_variable_3_name`
        repeats

        Args:
            value (str): value for IDD Field `erl_variable_3_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `erl_variable_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `erl_variable_3_name`')

        self._data["Erl Variable 3 Name"] = value

    @property
    def erl_variable_3_name(self):
        """Get erl_variable_3_name

        Returns:
            str: the value of `erl_variable_3_name` or None if not set
        """
        return self._data["Erl Variable 3 Name"]

    @erl_variable_3_name.setter
    def erl_variable_3_name(self, value=None):
        """  Corresponds to IDD Field `erl_variable_3_name`
        repeats

        Args:
            value (str): value for IDD Field `erl_variable_3_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `erl_variable_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `erl_variable_3_name`')

        self._data["Erl Variable 3 Name"] = value

    @property
    def erl_variable_3_name(self):
        """Get erl_variable_3_name

        Returns:
            str: the value of `erl_variable_3_name` or None if not set
        """
        return self._data["Erl Variable 3 Name"]

    @erl_variable_3_name.setter
    def erl_variable_3_name(self, value=None):
        """  Corresponds to IDD Field `erl_variable_3_name`
        repeats

        Args:
            value (str): value for IDD Field `erl_variable_3_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `erl_variable_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `erl_variable_3_name`')

        self._data["Erl Variable 3 Name"] = value

    @property
    def erl_variable_3_name(self):
        """Get erl_variable_3_name

        Returns:
            str: the value of `erl_variable_3_name` or None if not set
        """
        return self._data["Erl Variable 3 Name"]

    @erl_variable_3_name.setter
    def erl_variable_3_name(self, value=None):
        """  Corresponds to IDD Field `erl_variable_3_name`
        repeats

        Args:
            value (str): value for IDD Field `erl_variable_3_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `erl_variable_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `erl_variable_3_name`')

        self._data["Erl Variable 3 Name"] = value

    @property
    def erl_variable_3_name(self):
        """Get erl_variable_3_name

        Returns:
            str: the value of `erl_variable_3_name` or None if not set
        """
        return self._data["Erl Variable 3 Name"]

    @erl_variable_3_name.setter
    def erl_variable_3_name(self, value=None):
        """  Corresponds to IDD Field `erl_variable_3_name`
        repeats

        Args:
            value (str): value for IDD Field `erl_variable_3_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `erl_variable_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `erl_variable_3_name`')

        self._data["Erl Variable 3 Name"] = value

    @property
    def erl_variable_3_name(self):
        """Get erl_variable_3_name

        Returns:
            str: the value of `erl_variable_3_name` or None if not set
        """
        return self._data["Erl Variable 3 Name"]

    @erl_variable_3_name.setter
    def erl_variable_3_name(self, value=None):
        """  Corresponds to IDD Field `erl_variable_3_name`
        repeats

        Args:
            value (str): value for IDD Field `erl_variable_3_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `erl_variable_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `erl_variable_3_name`')

        self._data["Erl Variable 3 Name"] = value

    @property
    def erl_variable_3_name(self):
        """Get erl_variable_3_name

        Returns:
            str: the value of `erl_variable_3_name` or None if not set
        """
        return self._data["Erl Variable 3 Name"]

    @erl_variable_3_name.setter
    def erl_variable_3_name(self, value=None):
        """  Corresponds to IDD Field `erl_variable_3_name`
        repeats

        Args:
            value (str): value for IDD Field `erl_variable_3_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `erl_variable_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `erl_variable_3_name`')

        self._data["Erl Variable 3 Name"] = value

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

    def __str__(self):
        out = []
        out.append(self._to_str(self.erl_variable_1_name))
        out.append(self._to_str(self.erl_variable_2_name))
        out.append(self._to_str(self.erl_variable_3_name))
        out.append(self._to_str(self.erl_variable_3_name))
        out.append(self._to_str(self.erl_variable_3_name))
        out.append(self._to_str(self.erl_variable_3_name))
        out.append(self._to_str(self.erl_variable_3_name))
        out.append(self._to_str(self.erl_variable_3_name))
        out.append(self._to_str(self.erl_variable_3_name))
        out.append(self._to_str(self.erl_variable_3_name))
        out.append(self._to_str(self.erl_variable_3_name))
        out.append(self._to_str(self.erl_variable_3_name))
        out.append(self._to_str(self.erl_variable_3_name))
        out.append(self._to_str(self.erl_variable_3_name))
        out.append(self._to_str(self.erl_variable_3_name))
        out.append(self._to_str(self.erl_variable_3_name))
        out.append(self._to_str(self.erl_variable_3_name))
        out.append(self._to_str(self.erl_variable_3_name))
        out.append(self._to_str(self.erl_variable_3_name))
        out.append(self._to_str(self.erl_variable_3_name))
        out.append(self._to_str(self.erl_variable_3_name))
        out.append(self._to_str(self.erl_variable_3_name))
        out.append(self._to_str(self.erl_variable_3_name))
        out.append(self._to_str(self.erl_variable_3_name))
        out.append(self._to_str(self.erl_variable_3_name))
        out.append(self._to_str(self.erl_variable_3_name))
        out.append(self._to_str(self.erl_variable_3_name))
        out.append(self._to_str(self.erl_variable_3_name))
        out.append(self._to_str(self.erl_variable_3_name))
        out.append(self._to_str(self.erl_variable_3_name))
        out.append(self._to_str(self.erl_variable_3_name))
        out.append(self._to_str(self.erl_variable_3_name))
        out.append(self._to_str(self.erl_variable_3_name))
        out.append(self._to_str(self.erl_variable_3_name))
        out.append(self._to_str(self.erl_variable_3_name))
        out.append(self._to_str(self.erl_variable_3_name))
        out.append(self._to_str(self.erl_variable_3_name))
        out.append(self._to_str(self.erl_variable_3_name))
        out.append(self._to_str(self.erl_variable_3_name))
        out.append(self._to_str(self.erl_variable_3_name))
        out.append(self._to_str(self.erl_variable_3_name))
        out.append(self._to_str(self.erl_variable_3_name))
        out.append(self._to_str(self.erl_variable_3_name))
        out.append(self._to_str(self.erl_variable_3_name))
        out.append(self._to_str(self.erl_variable_3_name))
        out.append(self._to_str(self.erl_variable_3_name))
        out.append(self._to_str(self.erl_variable_3_name))
        out.append(self._to_str(self.erl_variable_3_name))
        out.append(self._to_str(self.erl_variable_3_name))
        return ",".join(out)

class EnergyManagementSystemOutputVariable(object):
    """ Corresponds to IDD object `EnergyManagementSystem:OutputVariable`
        This object sets up an EnergyPlus output variable from an Erl variable
    """
    internal_name = "EnergyManagementSystem:OutputVariable"
    field_count = 6

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `EnergyManagementSystem:OutputVariable`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["EMS Variable Name"] = None
        self._data["Type of Data in Variable"] = None
        self._data["Update Frequency"] = None
        self._data["EMS Program or Subroutine Name"] = None
        self._data["Units"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.ems_variable_name = None
        else:
            self.ems_variable_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.type_of_data_in_variable = None
        else:
            self.type_of_data_in_variable = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.update_frequency = None
        else:
            self.update_frequency = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.ems_program_or_subroutine_name = None
        else:
            self.ems_program_or_subroutine_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.units = None
        else:
            self.units = vals[i]
        i += 1

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `name`

        Args:
            value (str): value for IDD Field `name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')

        self._data["Name"] = value

    @property
    def ems_variable_name(self):
        """Get ems_variable_name

        Returns:
            str: the value of `ems_variable_name` or None if not set
        """
        return self._data["EMS Variable Name"]

    @ems_variable_name.setter
    def ems_variable_name(self, value=None):
        """  Corresponds to IDD Field `ems_variable_name`
        must be an acceptable EMS variable

        Args:
            value (str): value for IDD Field `ems_variable_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `ems_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ems_variable_name`')

        self._data["EMS Variable Name"] = value

    @property
    def type_of_data_in_variable(self):
        """Get type_of_data_in_variable

        Returns:
            str: the value of `type_of_data_in_variable` or None if not set
        """
        return self._data["Type of Data in Variable"]

    @type_of_data_in_variable.setter
    def type_of_data_in_variable(self, value=None):
        """  Corresponds to IDD Field `type_of_data_in_variable`

        Args:
            value (str): value for IDD Field `type_of_data_in_variable`
                Accepted values are:
                      - Averaged
                      - Summed
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `type_of_data_in_variable`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `type_of_data_in_variable`')
            vals = set()
            vals.add("Averaged")
            vals.add("Summed")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `type_of_data_in_variable`'.format(value))

        self._data["Type of Data in Variable"] = value

    @property
    def update_frequency(self):
        """Get update_frequency

        Returns:
            str: the value of `update_frequency` or None if not set
        """
        return self._data["Update Frequency"]

    @update_frequency.setter
    def update_frequency(self, value=None):
        """  Corresponds to IDD Field `update_frequency`

        Args:
            value (str): value for IDD Field `update_frequency`
                Accepted values are:
                      - ZoneTimestep
                      - SystemTimestep
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `update_frequency`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `update_frequency`')
            vals = set()
            vals.add("ZoneTimestep")
            vals.add("SystemTimestep")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `update_frequency`'.format(value))

        self._data["Update Frequency"] = value

    @property
    def ems_program_or_subroutine_name(self):
        """Get ems_program_or_subroutine_name

        Returns:
            str: the value of `ems_program_or_subroutine_name` or None if not set
        """
        return self._data["EMS Program or Subroutine Name"]

    @ems_program_or_subroutine_name.setter
    def ems_program_or_subroutine_name(self, value=None):
        """  Corresponds to IDD Field `ems_program_or_subroutine_name`
        optional for global scope variables, required for local scope variables

        Args:
            value (str): value for IDD Field `ems_program_or_subroutine_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `ems_program_or_subroutine_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ems_program_or_subroutine_name`')

        self._data["EMS Program or Subroutine Name"] = value

    @property
    def units(self):
        """Get units

        Returns:
            str: the value of `units` or None if not set
        """
        return self._data["Units"]

    @units.setter
    def units(self, value=None):
        """  Corresponds to IDD Field `units`
        optional but will result in dimensionless units for blank
        EnergyPlus units are standard SI units

        Args:
            value (str): value for IDD Field `units`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `units`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `units`')

        self._data["Units"] = value

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

    def __str__(self):
        out = []
        out.append(self._to_str(self.name))
        out.append(self._to_str(self.ems_variable_name))
        out.append(self._to_str(self.type_of_data_in_variable))
        out.append(self._to_str(self.update_frequency))
        out.append(self._to_str(self.ems_program_or_subroutine_name))
        out.append(self._to_str(self.units))
        return ",".join(out)

class EnergyManagementSystemMeteredOutputVariable(object):
    """ Corresponds to IDD object `EnergyManagementSystem:MeteredOutputVariable`
        This object sets up an EnergyPlus output variable from an Erl variable
    """
    internal_name = "EnergyManagementSystem:MeteredOutputVariable"
    field_count = 9

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `EnergyManagementSystem:MeteredOutputVariable`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["EMS Variable Name"] = None
        self._data["Update Frequency"] = None
        self._data["EMS Program or Subroutine Name"] = None
        self._data["Resource Type"] = None
        self._data["Group Type"] = None
        self._data["End-Use Category"] = None
        self._data["End-Use Subcategory"] = None
        self._data["Units"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.ems_variable_name = None
        else:
            self.ems_variable_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.update_frequency = None
        else:
            self.update_frequency = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.ems_program_or_subroutine_name = None
        else:
            self.ems_program_or_subroutine_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.resource_type = None
        else:
            self.resource_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.group_type = None
        else:
            self.group_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.enduse_category = None
        else:
            self.enduse_category = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.enduse_subcategory = None
        else:
            self.enduse_subcategory = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.units = None
        else:
            self.units = vals[i]
        i += 1

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `name`

        Args:
            value (str): value for IDD Field `name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')

        self._data["Name"] = value

    @property
    def ems_variable_name(self):
        """Get ems_variable_name

        Returns:
            str: the value of `ems_variable_name` or None if not set
        """
        return self._data["EMS Variable Name"]

    @ems_variable_name.setter
    def ems_variable_name(self, value=None):
        """  Corresponds to IDD Field `ems_variable_name`
        must be an acceptable EMS variable, no spaces

        Args:
            value (str): value for IDD Field `ems_variable_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `ems_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ems_variable_name`')

        self._data["EMS Variable Name"] = value

    @property
    def update_frequency(self):
        """Get update_frequency

        Returns:
            str: the value of `update_frequency` or None if not set
        """
        return self._data["Update Frequency"]

    @update_frequency.setter
    def update_frequency(self, value=None):
        """  Corresponds to IDD Field `update_frequency`

        Args:
            value (str): value for IDD Field `update_frequency`
                Accepted values are:
                      - ZoneTimestep
                      - SystemTimestep
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `update_frequency`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `update_frequency`')
            vals = set()
            vals.add("ZoneTimestep")
            vals.add("SystemTimestep")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `update_frequency`'.format(value))

        self._data["Update Frequency"] = value

    @property
    def ems_program_or_subroutine_name(self):
        """Get ems_program_or_subroutine_name

        Returns:
            str: the value of `ems_program_or_subroutine_name` or None if not set
        """
        return self._data["EMS Program or Subroutine Name"]

    @ems_program_or_subroutine_name.setter
    def ems_program_or_subroutine_name(self, value=None):
        """  Corresponds to IDD Field `ems_program_or_subroutine_name`
        optional for global scope variables, required for local scope variables

        Args:
            value (str): value for IDD Field `ems_program_or_subroutine_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `ems_program_or_subroutine_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ems_program_or_subroutine_name`')

        self._data["EMS Program or Subroutine Name"] = value

    @property
    def resource_type(self):
        """Get resource_type

        Returns:
            str: the value of `resource_type` or None if not set
        """
        return self._data["Resource Type"]

    @resource_type.setter
    def resource_type(self, value=None):
        """  Corresponds to IDD Field `resource_type`
        choose the type of fuel, water, electricity, pollution or heat rate that should be metered.

        Args:
            value (str): value for IDD Field `resource_type`
                Accepted values are:
                      - Electricity
                      - NaturalGas
                      - Gasoline
                      - Diesel
                      - Coal
                      - FuelOil#1
                      - FuelOil#2
                      - Propane
                      - OtherFuel1
                      - OtherFuel2
                      - WaterUse
                      - OnSiteWaterProduced
                      - MainsWaterSupply
                      - RainWaterCollected
                      - WellWaterDrawn
                      - CondensateWaterCollected
                      - EnergyTransfer
                      - Steam
                      - DistrictCooling
                      - DistrictHeating
                      - ElectricityProducedOnSite
                      - SolarWaterHeating
                      - SolarAirHeating
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `resource_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `resource_type`')
            vals = set()
            vals.add("Electricity")
            vals.add("NaturalGas")
            vals.add("Gasoline")
            vals.add("Diesel")
            vals.add("Coal")
            vals.add("FuelOil#1")
            vals.add("FuelOil#2")
            vals.add("Propane")
            vals.add("OtherFuel1")
            vals.add("OtherFuel2")
            vals.add("WaterUse")
            vals.add("OnSiteWaterProduced")
            vals.add("MainsWaterSupply")
            vals.add("RainWaterCollected")
            vals.add("WellWaterDrawn")
            vals.add("CondensateWaterCollected")
            vals.add("EnergyTransfer")
            vals.add("Steam")
            vals.add("DistrictCooling")
            vals.add("DistrictHeating")
            vals.add("ElectricityProducedOnSite")
            vals.add("SolarWaterHeating")
            vals.add("SolarAirHeating")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `resource_type`'.format(value))

        self._data["Resource Type"] = value

    @property
    def group_type(self):
        """Get group_type

        Returns:
            str: the value of `group_type` or None if not set
        """
        return self._data["Group Type"]

    @group_type.setter
    def group_type(self, value=None):
        """  Corresponds to IDD Field `group_type`
        choose a general classification, building (internal services), HVAC (air sytems), or plant (hydronic systems)

        Args:
            value (str): value for IDD Field `group_type`
                Accepted values are:
                      - Building
                      - HVAC
                      - Plant
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `group_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `group_type`')
            vals = set()
            vals.add("Building")
            vals.add("HVAC")
            vals.add("Plant")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `group_type`'.format(value))

        self._data["Group Type"] = value

    @property
    def enduse_category(self):
        """Get enduse_category

        Returns:
            str: the value of `enduse_category` or None if not set
        """
        return self._data["End-Use Category"]

    @enduse_category.setter
    def enduse_category(self, value=None):
        """  Corresponds to IDD Field `enduse_category`
        choose how the metered output should be classified for end-use category

        Args:
            value (str): value for IDD Field `enduse_category`
                Accepted values are:
                      - Heating
                      - Cooling
                      - InteriorLights
                      - ExteriorLights
                      - InteriorEquipment
                      - ExteriorEquipment
                      - Fans
                      - Pumps
                      - HeatRejection
                      - Humidifier
                      - HeatRecovery
                      - WaterSystems
                      - Refrigeration
                      - OnSiteGeneration
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `enduse_category`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `enduse_category`')
            vals = set()
            vals.add("Heating")
            vals.add("Cooling")
            vals.add("InteriorLights")
            vals.add("ExteriorLights")
            vals.add("InteriorEquipment")
            vals.add("ExteriorEquipment")
            vals.add("Fans")
            vals.add("Pumps")
            vals.add("HeatRejection")
            vals.add("Humidifier")
            vals.add("HeatRecovery")
            vals.add("WaterSystems")
            vals.add("Refrigeration")
            vals.add("OnSiteGeneration")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `enduse_category`'.format(value))

        self._data["End-Use Category"] = value

    @property
    def enduse_subcategory(self):
        """Get enduse_subcategory

        Returns:
            str: the value of `enduse_subcategory` or None if not set
        """
        return self._data["End-Use Subcategory"]

    @enduse_subcategory.setter
    def enduse_subcategory(self, value=None):
        """  Corresponds to IDD Field `enduse_subcategory`
        enter a user-defined subcategory for this metered output

        Args:
            value (str): value for IDD Field `enduse_subcategory`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `enduse_subcategory`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `enduse_subcategory`')

        self._data["End-Use Subcategory"] = value

    @property
    def units(self):
        """Get units

        Returns:
            str: the value of `units` or None if not set
        """
        return self._data["Units"]

    @units.setter
    def units(self, value=None):
        """  Corresponds to IDD Field `units`
        optional but will result in dimensionless units for blank
        EnergyPlus units are standard SI units

        Args:
            value (str): value for IDD Field `units`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `units`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `units`')

        self._data["Units"] = value

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

    def __str__(self):
        out = []
        out.append(self._to_str(self.name))
        out.append(self._to_str(self.ems_variable_name))
        out.append(self._to_str(self.update_frequency))
        out.append(self._to_str(self.ems_program_or_subroutine_name))
        out.append(self._to_str(self.resource_type))
        out.append(self._to_str(self.group_type))
        out.append(self._to_str(self.enduse_category))
        out.append(self._to_str(self.enduse_subcategory))
        out.append(self._to_str(self.units))
        return ",".join(out)

class EnergyManagementSystemTrendVariable(object):
    """ Corresponds to IDD object `EnergyManagementSystem:TrendVariable`
        This object sets up an EMS trend variable from an Erl variable
        A trend variable logs values across timesteps
    """
    internal_name = "EnergyManagementSystem:TrendVariable"
    field_count = 3

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `EnergyManagementSystem:TrendVariable`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["EMS Variable Name"] = None
        self._data["Number of Timesteps to be Logged"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.ems_variable_name = None
        else:
            self.ems_variable_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.number_of_timesteps_to_be_logged = None
        else:
            self.number_of_timesteps_to_be_logged = vals[i]
        i += 1

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `name`
        no spaces allowed in name

        Args:
            value (str): value for IDD Field `name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')

        self._data["Name"] = value

    @property
    def ems_variable_name(self):
        """Get ems_variable_name

        Returns:
            str: the value of `ems_variable_name` or None if not set
        """
        return self._data["EMS Variable Name"]

    @ems_variable_name.setter
    def ems_variable_name(self, value=None):
        """  Corresponds to IDD Field `ems_variable_name`
        must be a global scope EMS variable

        Args:
            value (str): value for IDD Field `ems_variable_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `ems_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ems_variable_name`')

        self._data["EMS Variable Name"] = value

    @property
    def number_of_timesteps_to_be_logged(self):
        """Get number_of_timesteps_to_be_logged

        Returns:
            int: the value of `number_of_timesteps_to_be_logged` or None if not set
        """
        return self._data["Number of Timesteps to be Logged"]

    @number_of_timesteps_to_be_logged.setter
    def number_of_timesteps_to_be_logged(self, value=None):
        """  Corresponds to IDD Field `number_of_timesteps_to_be_logged`

        Args:
            value (int): value for IDD Field `number_of_timesteps_to_be_logged`
                value >= 1
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = int(value)
            except:
                raise ValueError('value {} need to be of type int '
                                 'for field `number_of_timesteps_to_be_logged`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `number_of_timesteps_to_be_logged`')

        self._data["Number of Timesteps to be Logged"] = value

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

    def __str__(self):
        out = []
        out.append(self._to_str(self.name))
        out.append(self._to_str(self.ems_variable_name))
        out.append(self._to_str(self.number_of_timesteps_to_be_logged))
        return ",".join(out)

class EnergyManagementSystemInternalVariable(object):
    """ Corresponds to IDD object `EnergyManagementSystem:InternalVariable`
        Declares EMS variable as an internal data variable
    """
    internal_name = "EnergyManagementSystem:InternalVariable"
    field_count = 3

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `EnergyManagementSystem:InternalVariable`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Internal Data Index Key Name"] = None
        self._data["Internal Data Type"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.internal_data_index_key_name = None
        else:
            self.internal_data_index_key_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.internal_data_type = None
        else:
            self.internal_data_type = vals[i]
        i += 1

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `name`
        This name becomes a variable for use in Erl programs
        no spaces allowed in name

        Args:
            value (str): value for IDD Field `name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')

        self._data["Name"] = value

    @property
    def internal_data_index_key_name(self):
        """Get internal_data_index_key_name

        Returns:
            str: the value of `internal_data_index_key_name` or None if not set
        """
        return self._data["Internal Data Index Key Name"]

    @internal_data_index_key_name.setter
    def internal_data_index_key_name(self, value=None):
        """  Corresponds to IDD Field `internal_data_index_key_name`

        Args:
            value (str): value for IDD Field `internal_data_index_key_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `internal_data_index_key_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `internal_data_index_key_name`')

        self._data["Internal Data Index Key Name"] = value

    @property
    def internal_data_type(self):
        """Get internal_data_type

        Returns:
            str: the value of `internal_data_type` or None if not set
        """
        return self._data["Internal Data Type"]

    @internal_data_type.setter
    def internal_data_type(self, value=None):
        """  Corresponds to IDD Field `internal_data_type`

        Args:
            value (str): value for IDD Field `internal_data_type`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `internal_data_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `internal_data_type`')

        self._data["Internal Data Type"] = value

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

    def __str__(self):
        out = []
        out.append(self._to_str(self.name))
        out.append(self._to_str(self.internal_data_index_key_name))
        out.append(self._to_str(self.internal_data_type))
        return ",".join(out)

class EnergyManagementSystemCurveOrTableIndexVariable(object):
    """ Corresponds to IDD object `EnergyManagementSystem:CurveOrTableIndexVariable`
        Declares EMS variable that identifies a curve or table
    """
    internal_name = "EnergyManagementSystem:CurveOrTableIndexVariable"
    field_count = 2

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `EnergyManagementSystem:CurveOrTableIndexVariable`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Curve or Table Object Name"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.curve_or_table_object_name = None
        else:
            self.curve_or_table_object_name = vals[i]
        i += 1

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `name`
        This name becomes a variable for use in Erl programs
        no spaces allowed in name

        Args:
            value (str): value for IDD Field `name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')

        self._data["Name"] = value

    @property
    def curve_or_table_object_name(self):
        """Get curve_or_table_object_name

        Returns:
            str: the value of `curve_or_table_object_name` or None if not set
        """
        return self._data["Curve or Table Object Name"]

    @curve_or_table_object_name.setter
    def curve_or_table_object_name(self, value=None):
        """  Corresponds to IDD Field `curve_or_table_object_name`

        Args:
            value (str): value for IDD Field `curve_or_table_object_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `curve_or_table_object_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `curve_or_table_object_name`')

        self._data["Curve or Table Object Name"] = value

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

    def __str__(self):
        out = []
        out.append(self._to_str(self.name))
        out.append(self._to_str(self.curve_or_table_object_name))
        return ",".join(out)

class EnergyManagementSystemConstructionIndexVariable(object):
    """ Corresponds to IDD object `EnergyManagementSystem:ConstructionIndexVariable`
        Declares EMS variable that identifies a construction
    """
    internal_name = "EnergyManagementSystem:ConstructionIndexVariable"
    field_count = 2

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `EnergyManagementSystem:ConstructionIndexVariable`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Construction Object Name"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.construction_object_name = None
        else:
            self.construction_object_name = vals[i]
        i += 1

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `name`
        This name becomes a variable for use in Erl programs
        no spaces allowed in name

        Args:
            value (str): value for IDD Field `name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')

        self._data["Name"] = value

    @property
    def construction_object_name(self):
        """Get construction_object_name

        Returns:
            str: the value of `construction_object_name` or None if not set
        """
        return self._data["Construction Object Name"]

    @construction_object_name.setter
    def construction_object_name(self, value=None):
        """  Corresponds to IDD Field `construction_object_name`

        Args:
            value (str): value for IDD Field `construction_object_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `construction_object_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `construction_object_name`')

        self._data["Construction Object Name"] = value

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

    def __str__(self):
        out = []
        out.append(self._to_str(self.name))
        out.append(self._to_str(self.construction_object_name))
        return ",".join(out)