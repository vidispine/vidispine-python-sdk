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

class UserListType(object):
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
        'hits': 'int',
        'user': 'list[UserType]'
    }

    attribute_map = {
        'hits': 'hits',
        'user': 'user'
    }

    def __init__(self, hits=None, user=None):  # noqa: E501
        """UserListType - a model defined in OpenAPI"""  # noqa: E501

        self._hits = None
        self._user = None
        self.discriminator = None

        if hits is not None:
            self.hits = hits
        if user is not None:
            self.user = user

    @property
    def hits(self):
        """Gets the hits of this UserListType.  # noqa: E501


        :return: The hits of this UserListType.  # noqa: E501
        :rtype: int
        """
        return self._hits

    @hits.setter
    def hits(self, hits):
        """Sets the hits of this UserListType.


        :param hits: The hits of this UserListType.  # noqa: E501
        :type: int
        """

        self._hits = hits

    @property
    def user(self):
        """Gets the user of this UserListType.  # noqa: E501


        :return: The user of this UserListType.  # noqa: E501
        :rtype: list[UserType]
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this UserListType.


        :param user: The user of this UserListType.  # noqa: E501
        :type: list[UserType]
        """

        self._user = user

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
        if not isinstance(other, UserListType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
