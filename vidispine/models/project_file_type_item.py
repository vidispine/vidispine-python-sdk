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

class ProjectFileTypeItem(object):
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
        'shape': 'str',
        'id': 'str',
        'match': 'str',
        'permission': 'str'
    }

    attribute_map = {
        'shape': 'shape',
        'id': 'id',
        'match': 'match',
        'permission': 'permission'
    }

    def __init__(self, shape=None, id=None, match=None, permission=None):  # noqa: E501
        """ProjectFileTypeItem - a model defined in OpenAPI"""  # noqa: E501

        self._shape = None
        self._id = None
        self._match = None
        self._permission = None
        self.discriminator = None

        if shape is not None:
            self.shape = shape
        if id is not None:
            self.id = id
        if match is not None:
            self.match = match
        if permission is not None:
            self.permission = permission

    @property
    def shape(self):
        """Gets the shape of this ProjectFileTypeItem.  # noqa: E501


        :return: The shape of this ProjectFileTypeItem.  # noqa: E501
        :rtype: str
        """
        return self._shape

    @shape.setter
    def shape(self, shape):
        """Sets the shape of this ProjectFileTypeItem.


        :param shape: The shape of this ProjectFileTypeItem.  # noqa: E501
        :type: str
        """
        if shape is not None and not re.search(r'([_A-Za-z]+-)?([A-Za-z_][A-Za-z0-9_]*-|(([A-Za-z_][A-Za-z0-9_]*)?\*))([0-9]{1}[0-9]{0,31})', shape):  # noqa: E501
            raise ValueError(r"Invalid value for `shape`, must be a follow pattern or equal to `/([_A-Za-z]+-)?([A-Za-z_][A-Za-z0-9_]*-|(([A-Za-z_][A-Za-z0-9_]*)?\*))([0-9]{1}[0-9]{0,31})/`")  # noqa: E501

        self._shape = shape

    @property
    def id(self):
        """Gets the id of this ProjectFileTypeItem.  # noqa: E501


        :return: The id of this ProjectFileTypeItem.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ProjectFileTypeItem.


        :param id: The id of this ProjectFileTypeItem.  # noqa: E501
        :type: str
        """
        if id is not None and not re.search(r'([_A-Za-z]+-)?([A-Za-z_][A-Za-z0-9_]*-|(([A-Za-z_][A-Za-z0-9_]*)?\*))([0-9]{1}[0-9]{0,31})', id):  # noqa: E501
            raise ValueError(r"Invalid value for `id`, must be a follow pattern or equal to `/([_A-Za-z]+-)?([A-Za-z_][A-Za-z0-9_]*-|(([A-Za-z_][A-Za-z0-9_]*)?\*))([0-9]{1}[0-9]{0,31})/`")  # noqa: E501

        self._id = id

    @property
    def match(self):
        """Gets the match of this ProjectFileTypeItem.  # noqa: E501


        :return: The match of this ProjectFileTypeItem.  # noqa: E501
        :rtype: str
        """
        return self._match

    @match.setter
    def match(self, match):
        """Sets the match of this ProjectFileTypeItem.


        :param match: The match of this ProjectFileTypeItem.  # noqa: E501
        :type: str
        """

        self._match = match

    @property
    def permission(self):
        """Gets the permission of this ProjectFileTypeItem.  # noqa: E501


        :return: The permission of this ProjectFileTypeItem.  # noqa: E501
        :rtype: str
        """
        return self._permission

    @permission.setter
    def permission(self, permission):
        """Sets the permission of this ProjectFileTypeItem.


        :param permission: The permission of this ProjectFileTypeItem.  # noqa: E501
        :type: str
        """

        self._permission = permission

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
        if not isinstance(other, ProjectFileTypeItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
