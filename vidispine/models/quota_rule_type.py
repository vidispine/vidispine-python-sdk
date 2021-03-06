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

class QuotaRuleType(object):
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
        'update_frequency': 'int',
        'last_update': 'datetime',
        'resource': 'list[QuotaRuleTypeResource]',
        'description': 'str',
        'storage_group': 'str',
        'storage': 'str',
        'collection': 'str',
        'tag': 'str',
        'external_id': 'list[ExternalIdentifierType]',
        'user': 'str',
        'group': 'str',
        'id': 'str',
        'library': 'str'
    }

    attribute_map = {
        'update_frequency': 'updateFrequency',
        'last_update': 'lastUpdate',
        'resource': 'resource',
        'description': 'description',
        'storage_group': 'storageGroup',
        'storage': 'storage',
        'collection': 'collection',
        'tag': 'tag',
        'external_id': 'externalId',
        'user': 'user',
        'group': 'group',
        'id': 'id',
        'library': 'library'
    }

    def __init__(self, update_frequency=None, last_update=None, resource=None, description=None, storage_group=None, storage=None, collection=None, tag=None, external_id=None, user=None, group=None, id=None, library=None):  # noqa: E501
        """QuotaRuleType - a model defined in OpenAPI"""  # noqa: E501

        self._update_frequency = None
        self._last_update = None
        self._resource = None
        self._description = None
        self._storage_group = None
        self._storage = None
        self._collection = None
        self._tag = None
        self._external_id = None
        self._user = None
        self._group = None
        self._id = None
        self._library = None
        self.discriminator = None

        if update_frequency is not None:
            self.update_frequency = update_frequency
        if last_update is not None:
            self.last_update = last_update
        if resource is not None:
            self.resource = resource
        if description is not None:
            self.description = description
        if storage_group is not None:
            self.storage_group = storage_group
        if storage is not None:
            self.storage = storage
        if collection is not None:
            self.collection = collection
        if tag is not None:
            self.tag = tag
        if external_id is not None:
            self.external_id = external_id
        if user is not None:
            self.user = user
        if group is not None:
            self.group = group
        if id is not None:
            self.id = id
        if library is not None:
            self.library = library

    @property
    def update_frequency(self):
        """Gets the update_frequency of this QuotaRuleType.  # noqa: E501


        :return: The update_frequency of this QuotaRuleType.  # noqa: E501
        :rtype: int
        """
        return self._update_frequency

    @update_frequency.setter
    def update_frequency(self, update_frequency):
        """Sets the update_frequency of this QuotaRuleType.


        :param update_frequency: The update_frequency of this QuotaRuleType.  # noqa: E501
        :type: int
        """

        self._update_frequency = update_frequency

    @property
    def last_update(self):
        """Gets the last_update of this QuotaRuleType.  # noqa: E501


        :return: The last_update of this QuotaRuleType.  # noqa: E501
        :rtype: datetime
        """
        return self._last_update

    @last_update.setter
    def last_update(self, last_update):
        """Sets the last_update of this QuotaRuleType.


        :param last_update: The last_update of this QuotaRuleType.  # noqa: E501
        :type: datetime
        """

        self._last_update = last_update

    @property
    def resource(self):
        """Gets the resource of this QuotaRuleType.  # noqa: E501


        :return: The resource of this QuotaRuleType.  # noqa: E501
        :rtype: list[QuotaRuleTypeResource]
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """Sets the resource of this QuotaRuleType.


        :param resource: The resource of this QuotaRuleType.  # noqa: E501
        :type: list[QuotaRuleTypeResource]
        """

        self._resource = resource

    @property
    def description(self):
        """Gets the description of this QuotaRuleType.  # noqa: E501


        :return: The description of this QuotaRuleType.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this QuotaRuleType.


        :param description: The description of this QuotaRuleType.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def storage_group(self):
        """Gets the storage_group of this QuotaRuleType.  # noqa: E501


        :return: The storage_group of this QuotaRuleType.  # noqa: E501
        :rtype: str
        """
        return self._storage_group

    @storage_group.setter
    def storage_group(self, storage_group):
        """Sets the storage_group of this QuotaRuleType.


        :param storage_group: The storage_group of this QuotaRuleType.  # noqa: E501
        :type: str
        """
        if storage_group is not None and not re.search(r'([_A-Za-z]+-)?([A-Za-z_][A-Za-z0-9_]*-|(([A-Za-z_][A-Za-z0-9_]*)?\*))([0-9]{1}[0-9]{0,31})', storage_group):  # noqa: E501
            raise ValueError(r"Invalid value for `storage_group`, must be a follow pattern or equal to `/([_A-Za-z]+-)?([A-Za-z_][A-Za-z0-9_]*-|(([A-Za-z_][A-Za-z0-9_]*)?\*))([0-9]{1}[0-9]{0,31})/`")  # noqa: E501

        self._storage_group = storage_group

    @property
    def storage(self):
        """Gets the storage of this QuotaRuleType.  # noqa: E501


        :return: The storage of this QuotaRuleType.  # noqa: E501
        :rtype: str
        """
        return self._storage

    @storage.setter
    def storage(self, storage):
        """Sets the storage of this QuotaRuleType.


        :param storage: The storage of this QuotaRuleType.  # noqa: E501
        :type: str
        """
        if storage is not None and not re.search(r'([_A-Za-z]+-)?([A-Za-z_][A-Za-z0-9_]*-|(([A-Za-z_][A-Za-z0-9_]*)?\*))([0-9]{1}[0-9]{0,31})', storage):  # noqa: E501
            raise ValueError(r"Invalid value for `storage`, must be a follow pattern or equal to `/([_A-Za-z]+-)?([A-Za-z_][A-Za-z0-9_]*-|(([A-Za-z_][A-Za-z0-9_]*)?\*))([0-9]{1}[0-9]{0,31})/`")  # noqa: E501

        self._storage = storage

    @property
    def collection(self):
        """Gets the collection of this QuotaRuleType.  # noqa: E501


        :return: The collection of this QuotaRuleType.  # noqa: E501
        :rtype: str
        """
        return self._collection

    @collection.setter
    def collection(self, collection):
        """Sets the collection of this QuotaRuleType.


        :param collection: The collection of this QuotaRuleType.  # noqa: E501
        :type: str
        """
        if collection is not None and not re.search(r'([_A-Za-z]+-)?([A-Za-z_][A-Za-z0-9_]*-|(([A-Za-z_][A-Za-z0-9_]*)?\*))([0-9]{1}[0-9]{0,31})', collection):  # noqa: E501
            raise ValueError(r"Invalid value for `collection`, must be a follow pattern or equal to `/([_A-Za-z]+-)?([A-Za-z_][A-Za-z0-9_]*-|(([A-Za-z_][A-Za-z0-9_]*)?\*))([0-9]{1}[0-9]{0,31})/`")  # noqa: E501

        self._collection = collection

    @property
    def tag(self):
        """Gets the tag of this QuotaRuleType.  # noqa: E501


        :return: The tag of this QuotaRuleType.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this QuotaRuleType.


        :param tag: The tag of this QuotaRuleType.  # noqa: E501
        :type: str
        """

        self._tag = tag

    @property
    def external_id(self):
        """Gets the external_id of this QuotaRuleType.  # noqa: E501


        :return: The external_id of this QuotaRuleType.  # noqa: E501
        :rtype: list[ExternalIdentifierType]
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this QuotaRuleType.


        :param external_id: The external_id of this QuotaRuleType.  # noqa: E501
        :type: list[ExternalIdentifierType]
        """

        self._external_id = external_id

    @property
    def user(self):
        """Gets the user of this QuotaRuleType.  # noqa: E501


        :return: The user of this QuotaRuleType.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this QuotaRuleType.


        :param user: The user of this QuotaRuleType.  # noqa: E501
        :type: str
        """

        self._user = user

    @property
    def group(self):
        """Gets the group of this QuotaRuleType.  # noqa: E501


        :return: The group of this QuotaRuleType.  # noqa: E501
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this QuotaRuleType.


        :param group: The group of this QuotaRuleType.  # noqa: E501
        :type: str
        """

        self._group = group

    @property
    def id(self):
        """Gets the id of this QuotaRuleType.  # noqa: E501


        :return: The id of this QuotaRuleType.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this QuotaRuleType.


        :param id: The id of this QuotaRuleType.  # noqa: E501
        :type: str
        """
        if id is not None and not re.search(r'([_A-Za-z]+-)?([A-Za-z_][A-Za-z0-9_]*-|(([A-Za-z_][A-Za-z0-9_]*)?\*))([0-9]{1}[0-9]{0,31})', id):  # noqa: E501
            raise ValueError(r"Invalid value for `id`, must be a follow pattern or equal to `/([_A-Za-z]+-)?([A-Za-z_][A-Za-z0-9_]*-|(([A-Za-z_][A-Za-z0-9_]*)?\*))([0-9]{1}[0-9]{0,31})/`")  # noqa: E501

        self._id = id

    @property
    def library(self):
        """Gets the library of this QuotaRuleType.  # noqa: E501


        :return: The library of this QuotaRuleType.  # noqa: E501
        :rtype: str
        """
        return self._library

    @library.setter
    def library(self, library):
        """Sets the library of this QuotaRuleType.


        :param library: The library of this QuotaRuleType.  # noqa: E501
        :type: str
        """
        if library is not None and not re.search(r'([_A-Za-z]+-)?([A-Za-z_][A-Za-z0-9_]*-|(([A-Za-z_][A-Za-z0-9_]*)?\*))([0-9]{1}[0-9]{0,31})', library):  # noqa: E501
            raise ValueError(r"Invalid value for `library`, must be a follow pattern or equal to `/([_A-Za-z]+-)?([A-Za-z_][A-Za-z0-9_]*-|(([A-Za-z_][A-Za-z0-9_]*)?\*))([0-9]{1}[0-9]{0,31})/`")  # noqa: E501

        self._library = library

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
        if not isinstance(other, QuotaRuleType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
