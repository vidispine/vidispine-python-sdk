# coding: utf-8

"""
    Vidispine API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 5.x
    Contact: info@vidispine.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six
from . import *

class AutoProjectionRuleType(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'input_filters': 'AutoProjectionRuleTypeInputFilters',
        'step': 'list[AutoProjectionStepType]',
        'triggers': 'AutoProjectionRuleTypeTriggers',
        'name': 'str',
        'description': 'str'
    }

    attribute_map = {
        'input_filters': 'inputFilters',
        'step': 'step',
        'triggers': 'triggers',
        'name': 'name',
        'description': 'description'
    }

    def __init__(self, input_filters=None, step=None, triggers=None, name=None, description=None):  # noqa: E501
        """AutoProjectionRuleType - a model defined in OpenAPI"""  # noqa: E501

        self._input_filters = None
        self._step = None
        self._triggers = None
        self._name = None
        self._description = None
        self.discriminator = None

        if input_filters is not None:
            self.input_filters = input_filters
        if step is not None:
            self.step = step
        if triggers is not None:
            self.triggers = triggers
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description

    @property
    def input_filters(self):
        """Gets the input_filters of this AutoProjectionRuleType.  # noqa: E501


        :return: The input_filters of this AutoProjectionRuleType.  # noqa: E501
        :rtype: AutoProjectionRuleTypeInputFilters
        """
        return self._input_filters

    @input_filters.setter
    def input_filters(self, input_filters):
        """Sets the input_filters of this AutoProjectionRuleType.


        :param input_filters: The input_filters of this AutoProjectionRuleType.  # noqa: E501
        :type: AutoProjectionRuleTypeInputFilters
        """

        self._input_filters = input_filters

    @property
    def step(self):
        """Gets the step of this AutoProjectionRuleType.  # noqa: E501


        :return: The step of this AutoProjectionRuleType.  # noqa: E501
        :rtype: list[AutoProjectionStepType]
        """
        return self._step

    @step.setter
    def step(self, step):
        """Sets the step of this AutoProjectionRuleType.


        :param step: The step of this AutoProjectionRuleType.  # noqa: E501
        :type: list[AutoProjectionStepType]
        """

        self._step = step

    @property
    def triggers(self):
        """Gets the triggers of this AutoProjectionRuleType.  # noqa: E501


        :return: The triggers of this AutoProjectionRuleType.  # noqa: E501
        :rtype: AutoProjectionRuleTypeTriggers
        """
        return self._triggers

    @triggers.setter
    def triggers(self, triggers):
        """Sets the triggers of this AutoProjectionRuleType.


        :param triggers: The triggers of this AutoProjectionRuleType.  # noqa: E501
        :type: AutoProjectionRuleTypeTriggers
        """

        self._triggers = triggers

    @property
    def name(self):
        """Gets the name of this AutoProjectionRuleType.  # noqa: E501


        :return: The name of this AutoProjectionRuleType.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AutoProjectionRuleType.


        :param name: The name of this AutoProjectionRuleType.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this AutoProjectionRuleType.  # noqa: E501


        :return: The description of this AutoProjectionRuleType.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AutoProjectionRuleType.


        :param description: The description of this AutoProjectionRuleType.  # noqa: E501
        :type: str
        """

        self._description = description

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AutoProjectionRuleType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
