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

class FileType(object):
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
        'range': 'list[FileTypeRange]',
        'hash': 'str',
        'sequence': 'bool',
        'timestamp': 'datetime',
        'storage': 'str',
        'uri': 'list[str]',
        'storage_definition': 'StorageType',
        'item': 'list[FileTypeItem]',
        'state': 'str',
        'type': 'str',
        'path': 'str',
        'metadata': 'SimpleMetadataType',
        'refresh_flag': 'int',
        'id': 'str',
        'size': 'int'
    }

    attribute_map = {
        'range': 'range',
        'hash': 'hash',
        'sequence': 'sequence',
        'timestamp': 'timestamp',
        'storage': 'storage',
        'uri': 'uri',
        'storage_definition': 'storageDefinition',
        'item': 'item',
        'state': 'state',
        'type': 'type',
        'path': 'path',
        'metadata': 'metadata',
        'refresh_flag': 'refreshFlag',
        'id': 'id',
        'size': 'size'
    }

    def __init__(self, range=None, hash=None, sequence=None, timestamp=None, storage=None, uri=None, storage_definition=None, item=None, state=None, type=None, path=None, metadata=None, refresh_flag=None, id=None, size=None):  # noqa: E501
        """FileType - a model defined in OpenAPI"""  # noqa: E501

        self._range = None
        self._hash = None
        self._sequence = None
        self._timestamp = None
        self._storage = None
        self._uri = None
        self._storage_definition = None
        self._item = None
        self._state = None
        self._type = None
        self._path = None
        self._metadata = None
        self._refresh_flag = None
        self._id = None
        self._size = None
        self.discriminator = None

        if range is not None:
            self.range = range
        if hash is not None:
            self.hash = hash
        if sequence is not None:
            self.sequence = sequence
        if timestamp is not None:
            self.timestamp = timestamp
        if storage is not None:
            self.storage = storage
        if uri is not None:
            self.uri = uri
        if storage_definition is not None:
            self.storage_definition = storage_definition
        if item is not None:
            self.item = item
        self.state = state
        if type is not None:
            self.type = type
        if path is not None:
            self.path = path
        if metadata is not None:
            self.metadata = metadata
        if refresh_flag is not None:
            self.refresh_flag = refresh_flag
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size

    @property
    def range(self):
        """Gets the range of this FileType.  # noqa: E501


        :return: The range of this FileType.  # noqa: E501
        :rtype: list[FileTypeRange]
        """
        return self._range

    @range.setter
    def range(self, range):
        """Sets the range of this FileType.


        :param range: The range of this FileType.  # noqa: E501
        :type: list[FileTypeRange]
        """

        self._range = range

    @property
    def hash(self):
        """Gets the hash of this FileType.  # noqa: E501


        :return: The hash of this FileType.  # noqa: E501
        :rtype: str
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        """Sets the hash of this FileType.


        :param hash: The hash of this FileType.  # noqa: E501
        :type: str
        """

        self._hash = hash

    @property
    def sequence(self):
        """Gets the sequence of this FileType.  # noqa: E501


        :return: The sequence of this FileType.  # noqa: E501
        :rtype: bool
        """
        return self._sequence

    @sequence.setter
    def sequence(self, sequence):
        """Sets the sequence of this FileType.


        :param sequence: The sequence of this FileType.  # noqa: E501
        :type: bool
        """

        self._sequence = sequence

    @property
    def timestamp(self):
        """Gets the timestamp of this FileType.  # noqa: E501


        :return: The timestamp of this FileType.  # noqa: E501
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this FileType.


        :param timestamp: The timestamp of this FileType.  # noqa: E501
        :type: datetime
        """

        self._timestamp = timestamp

    @property
    def storage(self):
        """Gets the storage of this FileType.  # noqa: E501


        :return: The storage of this FileType.  # noqa: E501
        :rtype: str
        """
        return self._storage

    @storage.setter
    def storage(self, storage):
        """Sets the storage of this FileType.


        :param storage: The storage of this FileType.  # noqa: E501
        :type: str
        """
        if storage is not None and not re.search(r'([_A-Za-z]+-)?([A-Za-z_][A-Za-z0-9_]*-|(([A-Za-z_][A-Za-z0-9_]*)?\*))([0-9]{1}[0-9]{0,31})', storage):  # noqa: E501
            raise ValueError(r"Invalid value for `storage`, must be a follow pattern or equal to `/([_A-Za-z]+-)?([A-Za-z_][A-Za-z0-9_]*-|(([A-Za-z_][A-Za-z0-9_]*)?\*))([0-9]{1}[0-9]{0,31})/`")  # noqa: E501

        self._storage = storage

    @property
    def uri(self):
        """Gets the uri of this FileType.  # noqa: E501


        :return: The uri of this FileType.  # noqa: E501
        :rtype: list[str]
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this FileType.


        :param uri: The uri of this FileType.  # noqa: E501
        :type: list[str]
        """

        self._uri = uri

    @property
    def storage_definition(self):
        """Gets the storage_definition of this FileType.  # noqa: E501


        :return: The storage_definition of this FileType.  # noqa: E501
        :rtype: StorageType
        """
        return self._storage_definition

    @storage_definition.setter
    def storage_definition(self, storage_definition):
        """Sets the storage_definition of this FileType.


        :param storage_definition: The storage_definition of this FileType.  # noqa: E501
        :type: StorageType
        """

        self._storage_definition = storage_definition

    @property
    def item(self):
        """Gets the item of this FileType.  # noqa: E501


        :return: The item of this FileType.  # noqa: E501
        :rtype: list[FileTypeItem]
        """
        return self._item

    @item.setter
    def item(self, item):
        """Sets the item of this FileType.


        :param item: The item of this FileType.  # noqa: E501
        :type: list[FileTypeItem]
        """

        self._item = item

    @property
    def state(self):
        """Gets the state of this FileType.  # noqa: E501


        :return: The state of this FileType.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this FileType.


        :param state: The state of this FileType.  # noqa: E501
        :type: str
        """
        if state is None:
            raise ValueError("Invalid value for `state`, must not be `None`")  # noqa: E501

        self._state = state

    @property
    def type(self):
        """Gets the type of this FileType.  # noqa: E501


        :return: The type of this FileType.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this FileType.


        :param type: The type of this FileType.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def path(self):
        """Gets the path of this FileType.  # noqa: E501


        :return: The path of this FileType.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this FileType.


        :param path: The path of this FileType.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def metadata(self):
        """Gets the metadata of this FileType.  # noqa: E501


        :return: The metadata of this FileType.  # noqa: E501
        :rtype: SimpleMetadataType
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this FileType.


        :param metadata: The metadata of this FileType.  # noqa: E501
        :type: SimpleMetadataType
        """

        self._metadata = metadata

    @property
    def refresh_flag(self):
        """Gets the refresh_flag of this FileType.  # noqa: E501


        :return: The refresh_flag of this FileType.  # noqa: E501
        :rtype: int
        """
        return self._refresh_flag

    @refresh_flag.setter
    def refresh_flag(self, refresh_flag):
        """Sets the refresh_flag of this FileType.


        :param refresh_flag: The refresh_flag of this FileType.  # noqa: E501
        :type: int
        """

        self._refresh_flag = refresh_flag

    @property
    def id(self):
        """Gets the id of this FileType.  # noqa: E501


        :return: The id of this FileType.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FileType.


        :param id: The id of this FileType.  # noqa: E501
        :type: str
        """
        if id is not None and not re.search(r'([_A-Za-z]+-)?([A-Za-z_][A-Za-z0-9_]*-|(([A-Za-z_][A-Za-z0-9_]*)?\*))([0-9]{1}[0-9]{0,31})', id):  # noqa: E501
            raise ValueError(r"Invalid value for `id`, must be a follow pattern or equal to `/([_A-Za-z]+-)?([A-Za-z_][A-Za-z0-9_]*-|(([A-Za-z_][A-Za-z0-9_]*)?\*))([0-9]{1}[0-9]{0,31})/`")  # noqa: E501

        self._id = id

    @property
    def size(self):
        """Gets the size of this FileType.  # noqa: E501


        :return: The size of this FileType.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this FileType.


        :param size: The size of this FileType.  # noqa: E501
        :type: int
        """

        self._size = size

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
        if not isinstance(other, FileType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
