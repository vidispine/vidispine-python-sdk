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

class FileSequestionDefinitionType(object):
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
        'regex': 'str',
        'num_group': 'int',
        'id_group': 'int',
        'timeout': 'int',
        'num_format': 'str'
    }

    attribute_map = {
        'regex': 'regex',
        'num_group': 'numGroup',
        'id_group': 'idGroup',
        'timeout': 'timeout',
        'num_format': 'numFormat'
    }

    def __init__(self, regex=None, num_group=None, id_group=None, timeout=None, num_format=None):  # noqa: E501
        """FileSequestionDefinitionType - a model defined in OpenAPI"""  # noqa: E501

        self._regex = None
        self._num_group = None
        self._id_group = None
        self._timeout = None
        self._num_format = None
        self.discriminator = None

        self.regex = regex
        self.num_group = num_group
        self.id_group = id_group
        self.timeout = timeout
        if num_format is not None:
            self.num_format = num_format

    @property
    def regex(self):
        """Gets the regex of this FileSequestionDefinitionType.  # noqa: E501


        :return: The regex of this FileSequestionDefinitionType.  # noqa: E501
        :rtype: str
        """
        return self._regex

    @regex.setter
    def regex(self, regex):
        """Sets the regex of this FileSequestionDefinitionType.


        :param regex: The regex of this FileSequestionDefinitionType.  # noqa: E501
        :type: str
        """
        if regex is None:
            raise ValueError("Invalid value for `regex`, must not be `None`")  # noqa: E501

        self._regex = regex

    @property
    def num_group(self):
        """Gets the num_group of this FileSequestionDefinitionType.  # noqa: E501


        :return: The num_group of this FileSequestionDefinitionType.  # noqa: E501
        :rtype: int
        """
        return self._num_group

    @num_group.setter
    def num_group(self, num_group):
        """Sets the num_group of this FileSequestionDefinitionType.


        :param num_group: The num_group of this FileSequestionDefinitionType.  # noqa: E501
        :type: int
        """
        if num_group is None:
            raise ValueError("Invalid value for `num_group`, must not be `None`")  # noqa: E501

        self._num_group = num_group

    @property
    def id_group(self):
        """Gets the id_group of this FileSequestionDefinitionType.  # noqa: E501


        :return: The id_group of this FileSequestionDefinitionType.  # noqa: E501
        :rtype: int
        """
        return self._id_group

    @id_group.setter
    def id_group(self, id_group):
        """Sets the id_group of this FileSequestionDefinitionType.


        :param id_group: The id_group of this FileSequestionDefinitionType.  # noqa: E501
        :type: int
        """
        if id_group is None:
            raise ValueError("Invalid value for `id_group`, must not be `None`")  # noqa: E501

        self._id_group = id_group

    @property
    def timeout(self):
        """Gets the timeout of this FileSequestionDefinitionType.  # noqa: E501


        :return: The timeout of this FileSequestionDefinitionType.  # noqa: E501
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this FileSequestionDefinitionType.


        :param timeout: The timeout of this FileSequestionDefinitionType.  # noqa: E501
        :type: int
        """
        if timeout is None:
            raise ValueError("Invalid value for `timeout`, must not be `None`")  # noqa: E501

        self._timeout = timeout

    @property
    def num_format(self):
        """Gets the num_format of this FileSequestionDefinitionType.  # noqa: E501


        :return: The num_format of this FileSequestionDefinitionType.  # noqa: E501
        :rtype: str
        """
        return self._num_format

    @num_format.setter
    def num_format(self, num_format):
        """Sets the num_format of this FileSequestionDefinitionType.


        :param num_format: The num_format of this FileSequestionDefinitionType.  # noqa: E501
        :type: str
        """

        self._num_format = num_format

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
        if not isinstance(other, FileSequestionDefinitionType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
