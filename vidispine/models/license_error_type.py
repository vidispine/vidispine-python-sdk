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

class LicenseErrorType(object):
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
        'license_error': 'str'
    }

    attribute_map = {
        'license_error': 'licenseError'
    }

    def __init__(self, license_error=None):  # noqa: E501
        """LicenseErrorType - a model defined in OpenAPI"""  # noqa: E501

        self._license_error = None
        self.discriminator = None

        if license_error is not None:
            self.license_error = license_error

    @property
    def license_error(self):
        """Gets the license_error of this LicenseErrorType.  # noqa: E501


        :return: The license_error of this LicenseErrorType.  # noqa: E501
        :rtype: str
        """
        return self._license_error

    @license_error.setter
    def license_error(self, license_error):
        """Sets the license_error of this LicenseErrorType.


        :param license_error: The license_error of this LicenseErrorType.  # noqa: E501
        :type: str
        """

        self._license_error = license_error

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
        if not isinstance(other, LicenseErrorType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
