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

class StorageRuleType(object):
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
        'group': 'list[str]',
        'precedence': 'str',
        'applies_to': 'StorageRuleTypeAppliesTo',
        'storage': 'list[str]',
        'priority': 'list[StorageRuleTypePriority]',
        'storage_count': 'int',
        'inherited': 'bool',
        '_not': 'StorageRuleTypeNot',
        'id': 'str',
        'pool': 'StorageRuleTypePool'
    }

    attribute_map = {
        'group': 'group',
        'precedence': 'precedence',
        'applies_to': 'appliesTo',
        'storage': 'storage',
        'priority': 'priority',
        'storage_count': 'storageCount',
        'inherited': 'inherited',
        '_not': 'not',
        'id': 'id',
        'pool': 'pool'
    }

    def __init__(self, group=None, precedence=None, applies_to=None, storage=None, priority=None, storage_count=None, inherited=None, _not=None, id=None, pool=None):  # noqa: E501
        """StorageRuleType - a model defined in OpenAPI"""  # noqa: E501

        self._group = None
        self._precedence = None
        self._applies_to = None
        self._storage = None
        self._priority = None
        self._storage_count = None
        self._inherited = None
        self.__not = None
        self._id = None
        self._pool = None
        self.discriminator = None

        if group is not None:
            self.group = group
        if precedence is not None:
            self.precedence = precedence
        if applies_to is not None:
            self.applies_to = applies_to
        if storage is not None:
            self.storage = storage
        if priority is not None:
            self.priority = priority
        if storage_count is not None:
            self.storage_count = storage_count
        if inherited is not None:
            self.inherited = inherited
        if _not is not None:
            self._not = _not
        if id is not None:
            self.id = id
        if pool is not None:
            self.pool = pool

    @property
    def group(self):
        """Gets the group of this StorageRuleType.  # noqa: E501


        :return: The group of this StorageRuleType.  # noqa: E501
        :rtype: list[str]
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this StorageRuleType.


        :param group: The group of this StorageRuleType.  # noqa: E501
        :type: list[str]
        """

        self._group = group

    @property
    def precedence(self):
        """Gets the precedence of this StorageRuleType.  # noqa: E501


        :return: The precedence of this StorageRuleType.  # noqa: E501
        :rtype: str
        """
        return self._precedence

    @precedence.setter
    def precedence(self, precedence):
        """Sets the precedence of this StorageRuleType.


        :param precedence: The precedence of this StorageRuleType.  # noqa: E501
        :type: str
        """

        self._precedence = precedence

    @property
    def applies_to(self):
        """Gets the applies_to of this StorageRuleType.  # noqa: E501


        :return: The applies_to of this StorageRuleType.  # noqa: E501
        :rtype: StorageRuleTypeAppliesTo
        """
        return self._applies_to

    @applies_to.setter
    def applies_to(self, applies_to):
        """Sets the applies_to of this StorageRuleType.


        :param applies_to: The applies_to of this StorageRuleType.  # noqa: E501
        :type: StorageRuleTypeAppliesTo
        """

        self._applies_to = applies_to

    @property
    def storage(self):
        """Gets the storage of this StorageRuleType.  # noqa: E501


        :return: The storage of this StorageRuleType.  # noqa: E501
        :rtype: list[str]
        """
        return self._storage

    @storage.setter
    def storage(self, storage):
        """Sets the storage of this StorageRuleType.


        :param storage: The storage of this StorageRuleType.  # noqa: E501
        :type: list[str]
        """

        self._storage = storage

    @property
    def priority(self):
        """Gets the priority of this StorageRuleType.  # noqa: E501


        :return: The priority of this StorageRuleType.  # noqa: E501
        :rtype: list[StorageRuleTypePriority]
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this StorageRuleType.


        :param priority: The priority of this StorageRuleType.  # noqa: E501
        :type: list[StorageRuleTypePriority]
        """

        self._priority = priority

    @property
    def storage_count(self):
        """Gets the storage_count of this StorageRuleType.  # noqa: E501


        :return: The storage_count of this StorageRuleType.  # noqa: E501
        :rtype: int
        """
        return self._storage_count

    @storage_count.setter
    def storage_count(self, storage_count):
        """Sets the storage_count of this StorageRuleType.


        :param storage_count: The storage_count of this StorageRuleType.  # noqa: E501
        :type: int
        """

        self._storage_count = storage_count

    @property
    def inherited(self):
        """Gets the inherited of this StorageRuleType.  # noqa: E501


        :return: The inherited of this StorageRuleType.  # noqa: E501
        :rtype: bool
        """
        return self._inherited

    @inherited.setter
    def inherited(self, inherited):
        """Sets the inherited of this StorageRuleType.


        :param inherited: The inherited of this StorageRuleType.  # noqa: E501
        :type: bool
        """

        self._inherited = inherited

    @property
    def _not(self):
        """Gets the _not of this StorageRuleType.  # noqa: E501


        :return: The _not of this StorageRuleType.  # noqa: E501
        :rtype: StorageRuleTypeNot
        """
        return self.__not

    @_not.setter
    def _not(self, _not):
        """Sets the _not of this StorageRuleType.


        :param _not: The _not of this StorageRuleType.  # noqa: E501
        :type: StorageRuleTypeNot
        """

        self.__not = _not

    @property
    def id(self):
        """Gets the id of this StorageRuleType.  # noqa: E501


        :return: The id of this StorageRuleType.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this StorageRuleType.


        :param id: The id of this StorageRuleType.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def pool(self):
        """Gets the pool of this StorageRuleType.  # noqa: E501


        :return: The pool of this StorageRuleType.  # noqa: E501
        :rtype: StorageRuleTypePool
        """
        return self._pool

    @pool.setter
    def pool(self, pool):
        """Sets the pool of this StorageRuleType.


        :param pool: The pool of this StorageRuleType.  # noqa: E501
        :type: StorageRuleTypePool
        """

        self._pool = pool

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
        if not isinstance(other, StorageRuleType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other