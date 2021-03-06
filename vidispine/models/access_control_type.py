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

class AccessControlType(object):
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
        'group': 'str',
        'recursive': 'bool',
        'permission': 'str',
        'applies_to': 'list[object]',
        'grantor': 'str',
        'priority': 'int',
        'user': 'str',
        'operation': 'AccessControlTypeOperation',
        'id': 'str'
    }

    attribute_map = {
        'loc': 'loc',
        'group': 'group',
        'recursive': 'recursive',
        'permission': 'permission',
        'applies_to': 'appliesTo',
        'grantor': 'grantor',
        'priority': 'priority',
        'user': 'user',
        'operation': 'operation',
        'id': 'id'
    }

    def __init__(self, loc=None, group=None, recursive=None, permission=None, applies_to=None, grantor=None, priority=None, user=None, operation=None, id=None):  # noqa: E501
        """AccessControlType - a model defined in OpenAPI"""  # noqa: E501

        self._loc = None
        self._group = None
        self._recursive = None
        self._permission = None
        self._applies_to = None
        self._grantor = None
        self._priority = None
        self._user = None
        self._operation = None
        self._id = None
        self.discriminator = None

        if loc is not None:
            self.loc = loc
        if group is not None:
            self.group = group
        if recursive is not None:
            self.recursive = recursive
        self.permission = permission
        if applies_to is not None:
            self.applies_to = applies_to
        if grantor is not None:
            self.grantor = grantor
        if priority is not None:
            self.priority = priority
        if user is not None:
            self.user = user
        if operation is not None:
            self.operation = operation
        if id is not None:
            self.id = id

    @property
    def loc(self):
        """Gets the loc of this AccessControlType.  # noqa: E501


        :return: The loc of this AccessControlType.  # noqa: E501
        :rtype: str
        """
        return self._loc

    @loc.setter
    def loc(self, loc):
        """Sets the loc of this AccessControlType.


        :param loc: The loc of this AccessControlType.  # noqa: E501
        :type: str
        """

        self._loc = loc

    @property
    def group(self):
        """Gets the group of this AccessControlType.  # noqa: E501


        :return: The group of this AccessControlType.  # noqa: E501
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this AccessControlType.


        :param group: The group of this AccessControlType.  # noqa: E501
        :type: str
        """

        self._group = group

    @property
    def recursive(self):
        """Gets the recursive of this AccessControlType.  # noqa: E501


        :return: The recursive of this AccessControlType.  # noqa: E501
        :rtype: bool
        """
        return self._recursive

    @recursive.setter
    def recursive(self, recursive):
        """Sets the recursive of this AccessControlType.


        :param recursive: The recursive of this AccessControlType.  # noqa: E501
        :type: bool
        """

        self._recursive = recursive

    @property
    def permission(self):
        """Gets the permission of this AccessControlType.  # noqa: E501


        :return: The permission of this AccessControlType.  # noqa: E501
        :rtype: str
        """
        return self._permission

    @permission.setter
    def permission(self, permission):
        """Sets the permission of this AccessControlType.


        :param permission: The permission of this AccessControlType.  # noqa: E501
        :type: str
        """
        if permission is None:
            raise ValueError("Invalid value for `permission`, must not be `None`")  # noqa: E501

        self._permission = permission

    @property
    def applies_to(self):
        """Gets the applies_to of this AccessControlType.  # noqa: E501


        :return: The applies_to of this AccessControlType.  # noqa: E501
        :rtype: list[object]
        """
        return self._applies_to

    @applies_to.setter
    def applies_to(self, applies_to):
        """Sets the applies_to of this AccessControlType.


        :param applies_to: The applies_to of this AccessControlType.  # noqa: E501
        :type: list[object]
        """

        self._applies_to = applies_to

    @property
    def grantor(self):
        """Gets the grantor of this AccessControlType.  # noqa: E501


        :return: The grantor of this AccessControlType.  # noqa: E501
        :rtype: str
        """
        return self._grantor

    @grantor.setter
    def grantor(self, grantor):
        """Sets the grantor of this AccessControlType.


        :param grantor: The grantor of this AccessControlType.  # noqa: E501
        :type: str
        """

        self._grantor = grantor

    @property
    def priority(self):
        """Gets the priority of this AccessControlType.  # noqa: E501


        :return: The priority of this AccessControlType.  # noqa: E501
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this AccessControlType.


        :param priority: The priority of this AccessControlType.  # noqa: E501
        :type: int
        """

        self._priority = priority

    @property
    def user(self):
        """Gets the user of this AccessControlType.  # noqa: E501


        :return: The user of this AccessControlType.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this AccessControlType.


        :param user: The user of this AccessControlType.  # noqa: E501
        :type: str
        """

        self._user = user

    @property
    def operation(self):
        """Gets the operation of this AccessControlType.  # noqa: E501


        :return: The operation of this AccessControlType.  # noqa: E501
        :rtype: AccessControlTypeOperation
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """Sets the operation of this AccessControlType.


        :param operation: The operation of this AccessControlType.  # noqa: E501
        :type: AccessControlTypeOperation
        """

        self._operation = operation

    @property
    def id(self):
        """Gets the id of this AccessControlType.  # noqa: E501


        :return: The id of this AccessControlType.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AccessControlType.


        :param id: The id of this AccessControlType.  # noqa: E501
        :type: str
        """
        if id is not None and not re.search(r'([_A-Za-z]+-)?([A-Za-z_][A-Za-z0-9_]*-|(([A-Za-z_][A-Za-z0-9_]*)?\*))([0-9]{1}[0-9]{0,31})', id):  # noqa: E501
            raise ValueError(r"Invalid value for `id`, must be a follow pattern or equal to `/([_A-Za-z]+-)?([A-Za-z_][A-Za-z0-9_]*-|(([A-Za-z_][A-Za-z0-9_]*)?\*))([0-9]{1}[0-9]{0,31})/`")  # noqa: E501

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
        if not isinstance(other, AccessControlType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
