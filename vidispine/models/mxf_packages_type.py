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

class MXFPackagesType(object):
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
        'material_track_name': 'str',
        'tape_track_name': 'str',
        'material_package': 'MaterialPackageType',
        'tape_package': 'TapePackageType',
        'project_edit_rate': 'FrameRateType'
    }

    attribute_map = {
        'material_track_name': 'materialTrackName',
        'tape_track_name': 'tapeTrackName',
        'material_package': 'materialPackage',
        'tape_package': 'tapePackage',
        'project_edit_rate': 'projectEditRate'
    }

    def __init__(self, material_track_name=None, tape_track_name=None, material_package=None, tape_package=None, project_edit_rate=None):  # noqa: E501
        """MXFPackagesType - a model defined in OpenAPI"""  # noqa: E501

        self._material_track_name = None
        self._tape_track_name = None
        self._material_package = None
        self._tape_package = None
        self._project_edit_rate = None
        self.discriminator = None

        self.material_track_name = material_track_name
        if tape_track_name is not None:
            self.tape_track_name = tape_track_name
        self.material_package = material_package
        if tape_package is not None:
            self.tape_package = tape_package
        if project_edit_rate is not None:
            self.project_edit_rate = project_edit_rate

    @property
    def material_track_name(self):
        """Gets the material_track_name of this MXFPackagesType.  # noqa: E501


        :return: The material_track_name of this MXFPackagesType.  # noqa: E501
        :rtype: str
        """
        return self._material_track_name

    @material_track_name.setter
    def material_track_name(self, material_track_name):
        """Sets the material_track_name of this MXFPackagesType.


        :param material_track_name: The material_track_name of this MXFPackagesType.  # noqa: E501
        :type: str
        """
        if material_track_name is None:
            raise ValueError("Invalid value for `material_track_name`, must not be `None`")  # noqa: E501

        self._material_track_name = material_track_name

    @property
    def tape_track_name(self):
        """Gets the tape_track_name of this MXFPackagesType.  # noqa: E501


        :return: The tape_track_name of this MXFPackagesType.  # noqa: E501
        :rtype: str
        """
        return self._tape_track_name

    @tape_track_name.setter
    def tape_track_name(self, tape_track_name):
        """Sets the tape_track_name of this MXFPackagesType.


        :param tape_track_name: The tape_track_name of this MXFPackagesType.  # noqa: E501
        :type: str
        """

        self._tape_track_name = tape_track_name

    @property
    def material_package(self):
        """Gets the material_package of this MXFPackagesType.  # noqa: E501


        :return: The material_package of this MXFPackagesType.  # noqa: E501
        :rtype: MaterialPackageType
        """
        return self._material_package

    @material_package.setter
    def material_package(self, material_package):
        """Sets the material_package of this MXFPackagesType.


        :param material_package: The material_package of this MXFPackagesType.  # noqa: E501
        :type: MaterialPackageType
        """
        if material_package is None:
            raise ValueError("Invalid value for `material_package`, must not be `None`")  # noqa: E501

        self._material_package = material_package

    @property
    def tape_package(self):
        """Gets the tape_package of this MXFPackagesType.  # noqa: E501


        :return: The tape_package of this MXFPackagesType.  # noqa: E501
        :rtype: TapePackageType
        """
        return self._tape_package

    @tape_package.setter
    def tape_package(self, tape_package):
        """Sets the tape_package of this MXFPackagesType.


        :param tape_package: The tape_package of this MXFPackagesType.  # noqa: E501
        :type: TapePackageType
        """

        self._tape_package = tape_package

    @property
    def project_edit_rate(self):
        """Gets the project_edit_rate of this MXFPackagesType.  # noqa: E501


        :return: The project_edit_rate of this MXFPackagesType.  # noqa: E501
        :rtype: FrameRateType
        """
        return self._project_edit_rate

    @project_edit_rate.setter
    def project_edit_rate(self, project_edit_rate):
        """Sets the project_edit_rate of this MXFPackagesType.


        :param project_edit_rate: The project_edit_rate of this MXFPackagesType.  # noqa: E501
        :type: FrameRateType
        """

        self._project_edit_rate = project_edit_rate

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
        if not isinstance(other, MXFPackagesType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other