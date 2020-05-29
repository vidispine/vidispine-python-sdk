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

class MetadataEntryTypeSource(object):
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
        'loc': 'str',
        'type': 'str',
        'id': 'str'
    }

    attribute_map = {
        'loc': 'loc',
        'type': 'type',
        'id': 'id'
    }

    def __init__(self, loc=None, type=None, id=None):  # noqa: E501
        """MetadataEntryTypeSource - a model defined in OpenAPI"""  # noqa: E501

        self._loc = None
        self._type = None
        self._id = None
        self.discriminator = None

        self.loc = loc
        self.type = type
        self.id = id

    @property
    def loc(self):
        """Gets the loc of this MetadataEntryTypeSource.  # noqa: E501


        :return: The loc of this MetadataEntryTypeSource.  # noqa: E501
        :rtype: str
        """
        return self._loc

    @loc.setter
    def loc(self, loc):
        """Sets the loc of this MetadataEntryTypeSource.


        :param loc: The loc of this MetadataEntryTypeSource.  # noqa: E501
        :type: str
        """
        if loc is None:
            raise ValueError("Invalid value for `loc`, must not be `None`")  # noqa: E501

        self._loc = loc

    @property
    def type(self):
        """Gets the type of this MetadataEntryTypeSource.  # noqa: E501


        :return: The type of this MetadataEntryTypeSource.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this MetadataEntryTypeSource.


        :param type: The type of this MetadataEntryTypeSource.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def id(self):
        """Gets the id of this MetadataEntryTypeSource.  # noqa: E501


        :return: The id of this MetadataEntryTypeSource.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MetadataEntryTypeSource.


        :param id: The id of this MetadataEntryTypeSource.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

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
        if not isinstance(other, MetadataEntryTypeSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
