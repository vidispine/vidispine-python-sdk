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

class StorageType(object):
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
        'low_watermark': 'int',
        'projection': 'str',
        'sequence': 'list[StorageFileSequenceType]',
        'sequence_timeout': 'int',
        'bandwidth': 'int',
        'free_capacity': 'int',
        'id': 'str',
        'capacity': 'int',
        'high_watermark': 'int',
        'auto_detect': 'bool',
        'high_watermark_percentage': 'int',
        'priority': 'str',
        'state': 'str',
        'show_importables': 'bool',
        'type': 'str',
        'method': 'list[StorageMethodType]',
        'low_watermark_percentage': 'int',
        'metadata': 'SimpleMetadataType',
        'timestamp': 'datetime',
        'scan_interval': 'int',
        'bean': 'str',
        'archive_script': 'str'
    }

    attribute_map = {
        'low_watermark': 'lowWatermark',
        'projection': 'projection',
        'sequence': 'sequence',
        'sequence_timeout': 'sequenceTimeout',
        'bandwidth': 'bandwidth',
        'free_capacity': 'freeCapacity',
        'id': 'id',
        'capacity': 'capacity',
        'high_watermark': 'highWatermark',
        'auto_detect': 'autoDetect',
        'high_watermark_percentage': 'highWatermarkPercentage',
        'priority': 'priority',
        'state': 'state',
        'show_importables': 'showImportables',
        'type': 'type',
        'method': 'method',
        'low_watermark_percentage': 'lowWatermarkPercentage',
        'metadata': 'metadata',
        'timestamp': 'timestamp',
        'scan_interval': 'scanInterval',
        'bean': 'bean',
        'archive_script': 'archiveScript'
    }

    def __init__(self, low_watermark=None, projection=None, sequence=None, sequence_timeout=None, bandwidth=None, free_capacity=None, id=None, capacity=None, high_watermark=None, auto_detect=None, high_watermark_percentage=None, priority=None, state=None, show_importables=None, type=None, method=None, low_watermark_percentage=None, metadata=None, timestamp=None, scan_interval=None, bean=None, archive_script=None):  # noqa: E501
        """StorageType - a model defined in OpenAPI"""  # noqa: E501

        self._low_watermark = None
        self._projection = None
        self._sequence = None
        self._sequence_timeout = None
        self._bandwidth = None
        self._free_capacity = None
        self._id = None
        self._capacity = None
        self._high_watermark = None
        self._auto_detect = None
        self._high_watermark_percentage = None
        self._priority = None
        self._state = None
        self._show_importables = None
        self._type = None
        self._method = None
        self._low_watermark_percentage = None
        self._metadata = None
        self._timestamp = None
        self._scan_interval = None
        self._bean = None
        self._archive_script = None
        self.discriminator = None

        if low_watermark is not None:
            self.low_watermark = low_watermark
        if projection is not None:
            self.projection = projection
        if sequence is not None:
            self.sequence = sequence
        if sequence_timeout is not None:
            self.sequence_timeout = sequence_timeout
        if bandwidth is not None:
            self.bandwidth = bandwidth
        if free_capacity is not None:
            self.free_capacity = free_capacity
        if id is not None:
            self.id = id
        if capacity is not None:
            self.capacity = capacity
        if high_watermark is not None:
            self.high_watermark = high_watermark
        if auto_detect is not None:
            self.auto_detect = auto_detect
        if high_watermark_percentage is not None:
            self.high_watermark_percentage = high_watermark_percentage
        if priority is not None:
            self.priority = priority
        if state is not None:
            self.state = state
        if show_importables is not None:
            self.show_importables = show_importables
        if type is not None:
            self.type = type
        if method is not None:
            self.method = method
        if low_watermark_percentage is not None:
            self.low_watermark_percentage = low_watermark_percentage
        if metadata is not None:
            self.metadata = metadata
        if timestamp is not None:
            self.timestamp = timestamp
        if scan_interval is not None:
            self.scan_interval = scan_interval
        if bean is not None:
            self.bean = bean
        if archive_script is not None:
            self.archive_script = archive_script

    @property
    def low_watermark(self):
        """Gets the low_watermark of this StorageType.  # noqa: E501


        :return: The low_watermark of this StorageType.  # noqa: E501
        :rtype: int
        """
        return self._low_watermark

    @low_watermark.setter
    def low_watermark(self, low_watermark):
        """Sets the low_watermark of this StorageType.


        :param low_watermark: The low_watermark of this StorageType.  # noqa: E501
        :type: int
        """

        self._low_watermark = low_watermark

    @property
    def projection(self):
        """Gets the projection of this StorageType.  # noqa: E501


        :return: The projection of this StorageType.  # noqa: E501
        :rtype: str
        """
        return self._projection

    @projection.setter
    def projection(self, projection):
        """Sets the projection of this StorageType.


        :param projection: The projection of this StorageType.  # noqa: E501
        :type: str
        """

        self._projection = projection

    @property
    def sequence(self):
        """Gets the sequence of this StorageType.  # noqa: E501


        :return: The sequence of this StorageType.  # noqa: E501
        :rtype: list[StorageFileSequenceType]
        """
        return self._sequence

    @sequence.setter
    def sequence(self, sequence):
        """Sets the sequence of this StorageType.


        :param sequence: The sequence of this StorageType.  # noqa: E501
        :type: list[StorageFileSequenceType]
        """

        self._sequence = sequence

    @property
    def sequence_timeout(self):
        """Gets the sequence_timeout of this StorageType.  # noqa: E501


        :return: The sequence_timeout of this StorageType.  # noqa: E501
        :rtype: int
        """
        return self._sequence_timeout

    @sequence_timeout.setter
    def sequence_timeout(self, sequence_timeout):
        """Sets the sequence_timeout of this StorageType.


        :param sequence_timeout: The sequence_timeout of this StorageType.  # noqa: E501
        :type: int
        """

        self._sequence_timeout = sequence_timeout

    @property
    def bandwidth(self):
        """Gets the bandwidth of this StorageType.  # noqa: E501


        :return: The bandwidth of this StorageType.  # noqa: E501
        :rtype: int
        """
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, bandwidth):
        """Sets the bandwidth of this StorageType.


        :param bandwidth: The bandwidth of this StorageType.  # noqa: E501
        :type: int
        """

        self._bandwidth = bandwidth

    @property
    def free_capacity(self):
        """Gets the free_capacity of this StorageType.  # noqa: E501


        :return: The free_capacity of this StorageType.  # noqa: E501
        :rtype: int
        """
        return self._free_capacity

    @free_capacity.setter
    def free_capacity(self, free_capacity):
        """Sets the free_capacity of this StorageType.


        :param free_capacity: The free_capacity of this StorageType.  # noqa: E501
        :type: int
        """

        self._free_capacity = free_capacity

    @property
    def id(self):
        """Gets the id of this StorageType.  # noqa: E501


        :return: The id of this StorageType.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this StorageType.


        :param id: The id of this StorageType.  # noqa: E501
        :type: str
        """
        if id is not None and not re.search(r'([_A-Za-z]+-)?([A-Za-z_][A-Za-z0-9_]*-|(([A-Za-z_][A-Za-z0-9_]*)?\*))([0-9]{1}[0-9]{0,31})', id):  # noqa: E501
            raise ValueError(r"Invalid value for `id`, must be a follow pattern or equal to `/([_A-Za-z]+-)?([A-Za-z_][A-Za-z0-9_]*-|(([A-Za-z_][A-Za-z0-9_]*)?\*))([0-9]{1}[0-9]{0,31})/`")  # noqa: E501

        self._id = id

    @property
    def capacity(self):
        """Gets the capacity of this StorageType.  # noqa: E501


        :return: The capacity of this StorageType.  # noqa: E501
        :rtype: int
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """Sets the capacity of this StorageType.


        :param capacity: The capacity of this StorageType.  # noqa: E501
        :type: int
        """

        self._capacity = capacity

    @property
    def high_watermark(self):
        """Gets the high_watermark of this StorageType.  # noqa: E501


        :return: The high_watermark of this StorageType.  # noqa: E501
        :rtype: int
        """
        return self._high_watermark

    @high_watermark.setter
    def high_watermark(self, high_watermark):
        """Sets the high_watermark of this StorageType.


        :param high_watermark: The high_watermark of this StorageType.  # noqa: E501
        :type: int
        """

        self._high_watermark = high_watermark

    @property
    def auto_detect(self):
        """Gets the auto_detect of this StorageType.  # noqa: E501


        :return: The auto_detect of this StorageType.  # noqa: E501
        :rtype: bool
        """
        return self._auto_detect

    @auto_detect.setter
    def auto_detect(self, auto_detect):
        """Sets the auto_detect of this StorageType.


        :param auto_detect: The auto_detect of this StorageType.  # noqa: E501
        :type: bool
        """

        self._auto_detect = auto_detect

    @property
    def high_watermark_percentage(self):
        """Gets the high_watermark_percentage of this StorageType.  # noqa: E501


        :return: The high_watermark_percentage of this StorageType.  # noqa: E501
        :rtype: int
        """
        return self._high_watermark_percentage

    @high_watermark_percentage.setter
    def high_watermark_percentage(self, high_watermark_percentage):
        """Sets the high_watermark_percentage of this StorageType.


        :param high_watermark_percentage: The high_watermark_percentage of this StorageType.  # noqa: E501
        :type: int
        """

        self._high_watermark_percentage = high_watermark_percentage

    @property
    def priority(self):
        """Gets the priority of this StorageType.  # noqa: E501


        :return: The priority of this StorageType.  # noqa: E501
        :rtype: str
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this StorageType.


        :param priority: The priority of this StorageType.  # noqa: E501
        :type: str
        """

        self._priority = priority

    @property
    def state(self):
        """Gets the state of this StorageType.  # noqa: E501


        :return: The state of this StorageType.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this StorageType.


        :param state: The state of this StorageType.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def show_importables(self):
        """Gets the show_importables of this StorageType.  # noqa: E501


        :return: The show_importables of this StorageType.  # noqa: E501
        :rtype: bool
        """
        return self._show_importables

    @show_importables.setter
    def show_importables(self, show_importables):
        """Sets the show_importables of this StorageType.


        :param show_importables: The show_importables of this StorageType.  # noqa: E501
        :type: bool
        """

        self._show_importables = show_importables

    @property
    def type(self):
        """Gets the type of this StorageType.  # noqa: E501


        :return: The type of this StorageType.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this StorageType.


        :param type: The type of this StorageType.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def method(self):
        """Gets the method of this StorageType.  # noqa: E501


        :return: The method of this StorageType.  # noqa: E501
        :rtype: list[StorageMethodType]
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this StorageType.


        :param method: The method of this StorageType.  # noqa: E501
        :type: list[StorageMethodType]
        """

        self._method = method

    @property
    def low_watermark_percentage(self):
        """Gets the low_watermark_percentage of this StorageType.  # noqa: E501


        :return: The low_watermark_percentage of this StorageType.  # noqa: E501
        :rtype: int
        """
        return self._low_watermark_percentage

    @low_watermark_percentage.setter
    def low_watermark_percentage(self, low_watermark_percentage):
        """Sets the low_watermark_percentage of this StorageType.


        :param low_watermark_percentage: The low_watermark_percentage of this StorageType.  # noqa: E501
        :type: int
        """

        self._low_watermark_percentage = low_watermark_percentage

    @property
    def metadata(self):
        """Gets the metadata of this StorageType.  # noqa: E501


        :return: The metadata of this StorageType.  # noqa: E501
        :rtype: SimpleMetadataType
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this StorageType.


        :param metadata: The metadata of this StorageType.  # noqa: E501
        :type: SimpleMetadataType
        """

        self._metadata = metadata

    @property
    def timestamp(self):
        """Gets the timestamp of this StorageType.  # noqa: E501


        :return: The timestamp of this StorageType.  # noqa: E501
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this StorageType.


        :param timestamp: The timestamp of this StorageType.  # noqa: E501
        :type: datetime
        """

        self._timestamp = timestamp

    @property
    def scan_interval(self):
        """Gets the scan_interval of this StorageType.  # noqa: E501


        :return: The scan_interval of this StorageType.  # noqa: E501
        :rtype: int
        """
        return self._scan_interval

    @scan_interval.setter
    def scan_interval(self, scan_interval):
        """Sets the scan_interval of this StorageType.


        :param scan_interval: The scan_interval of this StorageType.  # noqa: E501
        :type: int
        """

        self._scan_interval = scan_interval

    @property
    def bean(self):
        """Gets the bean of this StorageType.  # noqa: E501


        :return: The bean of this StorageType.  # noqa: E501
        :rtype: str
        """
        return self._bean

    @bean.setter
    def bean(self, bean):
        """Sets the bean of this StorageType.


        :param bean: The bean of this StorageType.  # noqa: E501
        :type: str
        """

        self._bean = bean

    @property
    def archive_script(self):
        """Gets the archive_script of this StorageType.  # noqa: E501


        :return: The archive_script of this StorageType.  # noqa: E501
        :rtype: str
        """
        return self._archive_script

    @archive_script.setter
    def archive_script(self, archive_script):
        """Sets the archive_script of this StorageType.


        :param archive_script: The archive_script of this StorageType.  # noqa: E501
        :type: str
        """

        self._archive_script = archive_script

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
        if not isinstance(other, StorageType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
