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

class MetadataFieldResultTypeGroup(object):
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
        'definition': 'MetadataFieldGroupType',
        'end': 'str',
        'uuid': 'str',
        'source': 'MetadataEntryTypeSource',
        'value': 'MetadataGroupValueType',
        'start': 'str',
        'name': 'str'
    }

    attribute_map = {
        'definition': 'definition',
        'end': 'end',
        'uuid': 'uuid',
        'source': 'source',
        'value': 'value',
        'start': 'start',
        'name': 'name'
    }

    def __init__(self, definition=None, end=None, uuid=None, source=None, value=None, start=None, name=None):  # noqa: E501
        """MetadataFieldResultTypeGroup - a model defined in OpenAPI"""  # noqa: E501

        self._definition = None
        self._end = None
        self._uuid = None
        self._source = None
        self._value = None
        self._start = None
        self._name = None
        self.discriminator = None

        if definition is not None:
            self.definition = definition
        self.end = end
        self.uuid = uuid
        if source is not None:
            self.source = source
        if value is not None:
            self.value = value
        self.start = start
        self.name = name

    @property
    def definition(self):
        """Gets the definition of this MetadataFieldResultTypeGroup.  # noqa: E501


        :return: The definition of this MetadataFieldResultTypeGroup.  # noqa: E501
        :rtype: MetadataFieldGroupType
        """
        return self._definition

    @definition.setter
    def definition(self, definition):
        """Sets the definition of this MetadataFieldResultTypeGroup.


        :param definition: The definition of this MetadataFieldResultTypeGroup.  # noqa: E501
        :type: MetadataFieldGroupType
        """

        self._definition = definition

    @property
    def end(self):
        """Gets the end of this MetadataFieldResultTypeGroup.  # noqa: E501


        :return: The end of this MetadataFieldResultTypeGroup.  # noqa: E501
        :rtype: str
        """
        return self._end

    @end.setter
    def end(self, end):
        """Sets the end of this MetadataFieldResultTypeGroup.


        :param end: The end of this MetadataFieldResultTypeGroup.  # noqa: E501
        :type: str
        """
        if end is None:
            raise ValueError("Invalid value for `end`, must not be `None`")  # noqa: E501

        self._end = end

    @property
    def uuid(self):
        """Gets the uuid of this MetadataFieldResultTypeGroup.  # noqa: E501


        :return: The uuid of this MetadataFieldResultTypeGroup.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this MetadataFieldResultTypeGroup.


        :param uuid: The uuid of this MetadataFieldResultTypeGroup.  # noqa: E501
        :type: str
        """
        if uuid is None:
            raise ValueError("Invalid value for `uuid`, must not be `None`")  # noqa: E501

        self._uuid = uuid

    @property
    def source(self):
        """Gets the source of this MetadataFieldResultTypeGroup.  # noqa: E501


        :return: The source of this MetadataFieldResultTypeGroup.  # noqa: E501
        :rtype: MetadataEntryTypeSource
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this MetadataFieldResultTypeGroup.


        :param source: The source of this MetadataFieldResultTypeGroup.  # noqa: E501
        :type: MetadataEntryTypeSource
        """

        self._source = source

    @property
    def value(self):
        """Gets the value of this MetadataFieldResultTypeGroup.  # noqa: E501


        :return: The value of this MetadataFieldResultTypeGroup.  # noqa: E501
        :rtype: MetadataGroupValueType
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this MetadataFieldResultTypeGroup.


        :param value: The value of this MetadataFieldResultTypeGroup.  # noqa: E501
        :type: MetadataGroupValueType
        """

        self._value = value

    @property
    def start(self):
        """Gets the start of this MetadataFieldResultTypeGroup.  # noqa: E501


        :return: The start of this MetadataFieldResultTypeGroup.  # noqa: E501
        :rtype: str
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this MetadataFieldResultTypeGroup.


        :param start: The start of this MetadataFieldResultTypeGroup.  # noqa: E501
        :type: str
        """
        if start is None:
            raise ValueError("Invalid value for `start`, must not be `None`")  # noqa: E501

        self._start = start

    @property
    def name(self):
        """Gets the name of this MetadataFieldResultTypeGroup.  # noqa: E501


        :return: The name of this MetadataFieldResultTypeGroup.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MetadataFieldResultTypeGroup.


        :param name: The name of this MetadataFieldResultTypeGroup.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

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
        if not isinstance(other, MetadataFieldResultTypeGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
