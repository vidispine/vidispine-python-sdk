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

class DeletionLockType(object):
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
        'is_expired': 'bool',
        'entity_type': 'str',
        'expiry_time': 'datetime',
        'modified': 'datetime',
        'is_inherited': 'bool',
        'user': 'str',
        'entity_id': 'str',
        'is_effective': 'bool',
        'id': 'str',
        'metadata': 'SimpleMetadataType'
    }

    attribute_map = {
        'is_expired': 'isExpired',
        'entity_type': 'entityType',
        'expiry_time': 'expiryTime',
        'modified': 'modified',
        'is_inherited': 'isInherited',
        'user': 'user',
        'entity_id': 'entityId',
        'is_effective': 'isEffective',
        'id': 'id',
        'metadata': 'metadata'
    }

    def __init__(self, is_expired=None, entity_type=None, expiry_time=None, modified=None, is_inherited=None, user=None, entity_id=None, is_effective=None, id=None, metadata=None):  # noqa: E501
        """DeletionLockType - a model defined in OpenAPI"""  # noqa: E501

        self._is_expired = None
        self._entity_type = None
        self._expiry_time = None
        self._modified = None
        self._is_inherited = None
        self._user = None
        self._entity_id = None
        self._is_effective = None
        self._id = None
        self._metadata = None
        self.discriminator = None

        if is_expired is not None:
            self.is_expired = is_expired
        self.entity_type = entity_type
        self.expiry_time = expiry_time
        self.modified = modified
        if is_inherited is not None:
            self.is_inherited = is_inherited
        self.user = user
        self.entity_id = entity_id
        if is_effective is not None:
            self.is_effective = is_effective
        self.id = id
        if metadata is not None:
            self.metadata = metadata

    @property
    def is_expired(self):
        """Gets the is_expired of this DeletionLockType.  # noqa: E501


        :return: The is_expired of this DeletionLockType.  # noqa: E501
        :rtype: bool
        """
        return self._is_expired

    @is_expired.setter
    def is_expired(self, is_expired):
        """Sets the is_expired of this DeletionLockType.


        :param is_expired: The is_expired of this DeletionLockType.  # noqa: E501
        :type: bool
        """

        self._is_expired = is_expired

    @property
    def entity_type(self):
        """Gets the entity_type of this DeletionLockType.  # noqa: E501


        :return: The entity_type of this DeletionLockType.  # noqa: E501
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """Sets the entity_type of this DeletionLockType.


        :param entity_type: The entity_type of this DeletionLockType.  # noqa: E501
        :type: str
        """
        if entity_type is None:
            raise ValueError("Invalid value for `entity_type`, must not be `None`")  # noqa: E501

        self._entity_type = entity_type

    @property
    def expiry_time(self):
        """Gets the expiry_time of this DeletionLockType.  # noqa: E501


        :return: The expiry_time of this DeletionLockType.  # noqa: E501
        :rtype: datetime
        """
        return self._expiry_time

    @expiry_time.setter
    def expiry_time(self, expiry_time):
        """Sets the expiry_time of this DeletionLockType.


        :param expiry_time: The expiry_time of this DeletionLockType.  # noqa: E501
        :type: datetime
        """
        if expiry_time is None:
            raise ValueError("Invalid value for `expiry_time`, must not be `None`")  # noqa: E501

        self._expiry_time = expiry_time

    @property
    def modified(self):
        """Gets the modified of this DeletionLockType.  # noqa: E501


        :return: The modified of this DeletionLockType.  # noqa: E501
        :rtype: datetime
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this DeletionLockType.


        :param modified: The modified of this DeletionLockType.  # noqa: E501
        :type: datetime
        """
        if modified is None:
            raise ValueError("Invalid value for `modified`, must not be `None`")  # noqa: E501

        self._modified = modified

    @property
    def is_inherited(self):
        """Gets the is_inherited of this DeletionLockType.  # noqa: E501


        :return: The is_inherited of this DeletionLockType.  # noqa: E501
        :rtype: bool
        """
        return self._is_inherited

    @is_inherited.setter
    def is_inherited(self, is_inherited):
        """Sets the is_inherited of this DeletionLockType.


        :param is_inherited: The is_inherited of this DeletionLockType.  # noqa: E501
        :type: bool
        """

        self._is_inherited = is_inherited

    @property
    def user(self):
        """Gets the user of this DeletionLockType.  # noqa: E501


        :return: The user of this DeletionLockType.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this DeletionLockType.


        :param user: The user of this DeletionLockType.  # noqa: E501
        :type: str
        """
        if user is None:
            raise ValueError("Invalid value for `user`, must not be `None`")  # noqa: E501

        self._user = user

    @property
    def entity_id(self):
        """Gets the entity_id of this DeletionLockType.  # noqa: E501


        :return: The entity_id of this DeletionLockType.  # noqa: E501
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """Sets the entity_id of this DeletionLockType.


        :param entity_id: The entity_id of this DeletionLockType.  # noqa: E501
        :type: str
        """
        if entity_id is None:
            raise ValueError("Invalid value for `entity_id`, must not be `None`")  # noqa: E501

        self._entity_id = entity_id

    @property
    def is_effective(self):
        """Gets the is_effective of this DeletionLockType.  # noqa: E501


        :return: The is_effective of this DeletionLockType.  # noqa: E501
        :rtype: bool
        """
        return self._is_effective

    @is_effective.setter
    def is_effective(self, is_effective):
        """Sets the is_effective of this DeletionLockType.


        :param is_effective: The is_effective of this DeletionLockType.  # noqa: E501
        :type: bool
        """

        self._is_effective = is_effective

    @property
    def id(self):
        """Gets the id of this DeletionLockType.  # noqa: E501


        :return: The id of this DeletionLockType.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DeletionLockType.


        :param id: The id of this DeletionLockType.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def metadata(self):
        """Gets the metadata of this DeletionLockType.  # noqa: E501


        :return: The metadata of this DeletionLockType.  # noqa: E501
        :rtype: SimpleMetadataType
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this DeletionLockType.


        :param metadata: The metadata of this DeletionLockType.  # noqa: E501
        :type: SimpleMetadataType
        """

        self._metadata = metadata

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
        if not isinstance(other, DeletionLockType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
