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

class VersionType(object):
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
        'system_info': 'SystemInfoType',
        'component': 'list[CompType]',
        'license_info': 'LicenseType'
    }

    attribute_map = {
        'system_info': 'systemInfo',
        'component': 'component',
        'license_info': 'licenseInfo'
    }

    def __init__(self, system_info=None, component=None, license_info=None):  # noqa: E501
        """VersionType - a model defined in OpenAPI"""  # noqa: E501

        self._system_info = None
        self._component = None
        self._license_info = None
        self.discriminator = None

        if system_info is not None:
            self.system_info = system_info
        if component is not None:
            self.component = component
        if license_info is not None:
            self.license_info = license_info

    @property
    def system_info(self):
        """Gets the system_info of this VersionType.  # noqa: E501


        :return: The system_info of this VersionType.  # noqa: E501
        :rtype: SystemInfoType
        """
        return self._system_info

    @system_info.setter
    def system_info(self, system_info):
        """Sets the system_info of this VersionType.


        :param system_info: The system_info of this VersionType.  # noqa: E501
        :type: SystemInfoType
        """

        self._system_info = system_info

    @property
    def component(self):
        """Gets the component of this VersionType.  # noqa: E501


        :return: The component of this VersionType.  # noqa: E501
        :rtype: list[CompType]
        """
        return self._component

    @component.setter
    def component(self, component):
        """Sets the component of this VersionType.


        :param component: The component of this VersionType.  # noqa: E501
        :type: list[CompType]
        """

        self._component = component

    @property
    def license_info(self):
        """Gets the license_info of this VersionType.  # noqa: E501


        :return: The license_info of this VersionType.  # noqa: E501
        :rtype: LicenseType
        """
        return self._license_info

    @license_info.setter
    def license_info(self, license_info):
        """Sets the license_info of this VersionType.


        :param license_info: The license_info of this VersionType.  # noqa: E501
        :type: LicenseType
        """

        self._license_info = license_info

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
        if not isinstance(other, VersionType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
