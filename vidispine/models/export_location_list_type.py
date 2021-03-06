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

class ExportLocationListType(object):
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
        'export_location': 'list[ExportLocationType]'
    }

    attribute_map = {
        'export_location': 'exportLocation'
    }

    def __init__(self, export_location=None):  # noqa: E501
        """ExportLocationListType - a model defined in OpenAPI"""  # noqa: E501

        self._export_location = None
        self.discriminator = None

        if export_location is not None:
            self.export_location = export_location

    @property
    def export_location(self):
        """Gets the export_location of this ExportLocationListType.  # noqa: E501


        :return: The export_location of this ExportLocationListType.  # noqa: E501
        :rtype: list[ExportLocationType]
        """
        return self._export_location

    @export_location.setter
    def export_location(self, export_location):
        """Sets the export_location of this ExportLocationListType.


        :param export_location: The export_location of this ExportLocationListType.  # noqa: E501
        :type: list[ExportLocationType]
        """

        self._export_location = export_location

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
        if not isinstance(other, ExportLocationListType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
