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

class TaskGroupTypeJob(object):
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
        'priority': 'list[str]',
        'group': 'list[str]',
        'type': 'list[str]',
        'user': 'list[str]',
        'data': 'list[TaskGroupTypeData]'
    }

    attribute_map = {
        'priority': 'priority',
        'group': 'group',
        'type': 'type',
        'user': 'user',
        'data': 'data'
    }

    def __init__(self, priority=None, group=None, type=None, user=None, data=None):  # noqa: E501
        """TaskGroupTypeJob - a model defined in OpenAPI"""  # noqa: E501

        self._priority = None
        self._group = None
        self._type = None
        self._user = None
        self._data = None
        self.discriminator = None

        if priority is not None:
            self.priority = priority
        if group is not None:
            self.group = group
        if type is not None:
            self.type = type
        if user is not None:
            self.user = user
        if data is not None:
            self.data = data

    @property
    def priority(self):
        """Gets the priority of this TaskGroupTypeJob.  # noqa: E501


        :return: The priority of this TaskGroupTypeJob.  # noqa: E501
        :rtype: list[str]
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this TaskGroupTypeJob.


        :param priority: The priority of this TaskGroupTypeJob.  # noqa: E501
        :type: list[str]
        """

        self._priority = priority

    @property
    def group(self):
        """Gets the group of this TaskGroupTypeJob.  # noqa: E501


        :return: The group of this TaskGroupTypeJob.  # noqa: E501
        :rtype: list[str]
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this TaskGroupTypeJob.


        :param group: The group of this TaskGroupTypeJob.  # noqa: E501
        :type: list[str]
        """

        self._group = group

    @property
    def type(self):
        """Gets the type of this TaskGroupTypeJob.  # noqa: E501


        :return: The type of this TaskGroupTypeJob.  # noqa: E501
        :rtype: list[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TaskGroupTypeJob.


        :param type: The type of this TaskGroupTypeJob.  # noqa: E501
        :type: list[str]
        """

        self._type = type

    @property
    def user(self):
        """Gets the user of this TaskGroupTypeJob.  # noqa: E501


        :return: The user of this TaskGroupTypeJob.  # noqa: E501
        :rtype: list[str]
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this TaskGroupTypeJob.


        :param user: The user of this TaskGroupTypeJob.  # noqa: E501
        :type: list[str]
        """

        self._user = user

    @property
    def data(self):
        """Gets the data of this TaskGroupTypeJob.  # noqa: E501


        :return: The data of this TaskGroupTypeJob.  # noqa: E501
        :rtype: list[TaskGroupTypeData]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this TaskGroupTypeJob.


        :param data: The data of this TaskGroupTypeJob.  # noqa: E501
        :type: list[TaskGroupTypeData]
        """

        self._data = data

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
        if not isinstance(other, TaskGroupTypeJob):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other