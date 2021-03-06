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

class TransferLogEntryType(object):
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
        'destination_uri': 'str',
        'status': 'str',
        'source_uri': 'str',
        'destination_shape': 'str',
        'timestamp': 'datetime',
        'referred_id': 'int',
        'source_file': 'str',
        'destination_file': 'str',
        'method': 'str',
        'job': 'str',
        'source_shape': 'str',
        'source_item': 'str',
        'destination_storage': 'str',
        'destination_item': 'str',
        'id': 'int',
        'source_storage': 'str'
    }

    attribute_map = {
        'destination_uri': 'destinationUri',
        'status': 'status',
        'source_uri': 'sourceUri',
        'destination_shape': 'destinationShape',
        'timestamp': 'timestamp',
        'referred_id': 'referredId',
        'source_file': 'sourceFile',
        'destination_file': 'destinationFile',
        'method': 'method',
        'job': 'job',
        'source_shape': 'sourceShape',
        'source_item': 'sourceItem',
        'destination_storage': 'destinationStorage',
        'destination_item': 'destinationItem',
        'id': 'id',
        'source_storage': 'sourceStorage'
    }

    def __init__(self, destination_uri=None, status=None, source_uri=None, destination_shape=None, timestamp=None, referred_id=None, source_file=None, destination_file=None, method=None, job=None, source_shape=None, source_item=None, destination_storage=None, destination_item=None, id=None, source_storage=None):  # noqa: E501
        """TransferLogEntryType - a model defined in OpenAPI"""  # noqa: E501

        self._destination_uri = None
        self._status = None
        self._source_uri = None
        self._destination_shape = None
        self._timestamp = None
        self._referred_id = None
        self._source_file = None
        self._destination_file = None
        self._method = None
        self._job = None
        self._source_shape = None
        self._source_item = None
        self._destination_storage = None
        self._destination_item = None
        self._id = None
        self._source_storage = None
        self.discriminator = None

        if destination_uri is not None:
            self.destination_uri = destination_uri
        if status is not None:
            self.status = status
        if source_uri is not None:
            self.source_uri = source_uri
        if destination_shape is not None:
            self.destination_shape = destination_shape
        if timestamp is not None:
            self.timestamp = timestamp
        if referred_id is not None:
            self.referred_id = referred_id
        if source_file is not None:
            self.source_file = source_file
        if destination_file is not None:
            self.destination_file = destination_file
        if method is not None:
            self.method = method
        if job is not None:
            self.job = job
        if source_shape is not None:
            self.source_shape = source_shape
        if source_item is not None:
            self.source_item = source_item
        if destination_storage is not None:
            self.destination_storage = destination_storage
        if destination_item is not None:
            self.destination_item = destination_item
        if id is not None:
            self.id = id
        if source_storage is not None:
            self.source_storage = source_storage

    @property
    def destination_uri(self):
        """Gets the destination_uri of this TransferLogEntryType.  # noqa: E501


        :return: The destination_uri of this TransferLogEntryType.  # noqa: E501
        :rtype: str
        """
        return self._destination_uri

    @destination_uri.setter
    def destination_uri(self, destination_uri):
        """Sets the destination_uri of this TransferLogEntryType.


        :param destination_uri: The destination_uri of this TransferLogEntryType.  # noqa: E501
        :type: str
        """

        self._destination_uri = destination_uri

    @property
    def status(self):
        """Gets the status of this TransferLogEntryType.  # noqa: E501


        :return: The status of this TransferLogEntryType.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TransferLogEntryType.


        :param status: The status of this TransferLogEntryType.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def source_uri(self):
        """Gets the source_uri of this TransferLogEntryType.  # noqa: E501


        :return: The source_uri of this TransferLogEntryType.  # noqa: E501
        :rtype: str
        """
        return self._source_uri

    @source_uri.setter
    def source_uri(self, source_uri):
        """Sets the source_uri of this TransferLogEntryType.


        :param source_uri: The source_uri of this TransferLogEntryType.  # noqa: E501
        :type: str
        """

        self._source_uri = source_uri

    @property
    def destination_shape(self):
        """Gets the destination_shape of this TransferLogEntryType.  # noqa: E501


        :return: The destination_shape of this TransferLogEntryType.  # noqa: E501
        :rtype: str
        """
        return self._destination_shape

    @destination_shape.setter
    def destination_shape(self, destination_shape):
        """Sets the destination_shape of this TransferLogEntryType.


        :param destination_shape: The destination_shape of this TransferLogEntryType.  # noqa: E501
        :type: str
        """
        if destination_shape is not None and not re.search(r'([_A-Za-z]+-)?([A-Za-z_][A-Za-z0-9_]*-|(([A-Za-z_][A-Za-z0-9_]*)?\*))([0-9]{1}[0-9]{0,31})', destination_shape):  # noqa: E501
            raise ValueError(r"Invalid value for `destination_shape`, must be a follow pattern or equal to `/([_A-Za-z]+-)?([A-Za-z_][A-Za-z0-9_]*-|(([A-Za-z_][A-Za-z0-9_]*)?\*))([0-9]{1}[0-9]{0,31})/`")  # noqa: E501

        self._destination_shape = destination_shape

    @property
    def timestamp(self):
        """Gets the timestamp of this TransferLogEntryType.  # noqa: E501


        :return: The timestamp of this TransferLogEntryType.  # noqa: E501
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this TransferLogEntryType.


        :param timestamp: The timestamp of this TransferLogEntryType.  # noqa: E501
        :type: datetime
        """

        self._timestamp = timestamp

    @property
    def referred_id(self):
        """Gets the referred_id of this TransferLogEntryType.  # noqa: E501


        :return: The referred_id of this TransferLogEntryType.  # noqa: E501
        :rtype: int
        """
        return self._referred_id

    @referred_id.setter
    def referred_id(self, referred_id):
        """Sets the referred_id of this TransferLogEntryType.


        :param referred_id: The referred_id of this TransferLogEntryType.  # noqa: E501
        :type: int
        """

        self._referred_id = referred_id

    @property
    def source_file(self):
        """Gets the source_file of this TransferLogEntryType.  # noqa: E501


        :return: The source_file of this TransferLogEntryType.  # noqa: E501
        :rtype: str
        """
        return self._source_file

    @source_file.setter
    def source_file(self, source_file):
        """Sets the source_file of this TransferLogEntryType.


        :param source_file: The source_file of this TransferLogEntryType.  # noqa: E501
        :type: str
        """
        if source_file is not None and not re.search(r'([_A-Za-z]+-)?([A-Za-z_][A-Za-z0-9_]*-|(([A-Za-z_][A-Za-z0-9_]*)?\*))([0-9]{1}[0-9]{0,31})', source_file):  # noqa: E501
            raise ValueError(r"Invalid value for `source_file`, must be a follow pattern or equal to `/([_A-Za-z]+-)?([A-Za-z_][A-Za-z0-9_]*-|(([A-Za-z_][A-Za-z0-9_]*)?\*))([0-9]{1}[0-9]{0,31})/`")  # noqa: E501

        self._source_file = source_file

    @property
    def destination_file(self):
        """Gets the destination_file of this TransferLogEntryType.  # noqa: E501


        :return: The destination_file of this TransferLogEntryType.  # noqa: E501
        :rtype: str
        """
        return self._destination_file

    @destination_file.setter
    def destination_file(self, destination_file):
        """Sets the destination_file of this TransferLogEntryType.


        :param destination_file: The destination_file of this TransferLogEntryType.  # noqa: E501
        :type: str
        """
        if destination_file is not None and not re.search(r'([_A-Za-z]+-)?([A-Za-z_][A-Za-z0-9_]*-|(([A-Za-z_][A-Za-z0-9_]*)?\*))([0-9]{1}[0-9]{0,31})', destination_file):  # noqa: E501
            raise ValueError(r"Invalid value for `destination_file`, must be a follow pattern or equal to `/([_A-Za-z]+-)?([A-Za-z_][A-Za-z0-9_]*-|(([A-Za-z_][A-Za-z0-9_]*)?\*))([0-9]{1}[0-9]{0,31})/`")  # noqa: E501

        self._destination_file = destination_file

    @property
    def method(self):
        """Gets the method of this TransferLogEntryType.  # noqa: E501


        :return: The method of this TransferLogEntryType.  # noqa: E501
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this TransferLogEntryType.


        :param method: The method of this TransferLogEntryType.  # noqa: E501
        :type: str
        """

        self._method = method

    @property
    def job(self):
        """Gets the job of this TransferLogEntryType.  # noqa: E501


        :return: The job of this TransferLogEntryType.  # noqa: E501
        :rtype: str
        """
        return self._job

    @job.setter
    def job(self, job):
        """Sets the job of this TransferLogEntryType.


        :param job: The job of this TransferLogEntryType.  # noqa: E501
        :type: str
        """
        if job is not None and not re.search(r'([_A-Za-z]+-)?([A-Za-z_][A-Za-z0-9_]*-|(([A-Za-z_][A-Za-z0-9_]*)?\*))([0-9]{1}[0-9]{0,31})', job):  # noqa: E501
            raise ValueError(r"Invalid value for `job`, must be a follow pattern or equal to `/([_A-Za-z]+-)?([A-Za-z_][A-Za-z0-9_]*-|(([A-Za-z_][A-Za-z0-9_]*)?\*))([0-9]{1}[0-9]{0,31})/`")  # noqa: E501

        self._job = job

    @property
    def source_shape(self):
        """Gets the source_shape of this TransferLogEntryType.  # noqa: E501


        :return: The source_shape of this TransferLogEntryType.  # noqa: E501
        :rtype: str
        """
        return self._source_shape

    @source_shape.setter
    def source_shape(self, source_shape):
        """Sets the source_shape of this TransferLogEntryType.


        :param source_shape: The source_shape of this TransferLogEntryType.  # noqa: E501
        :type: str
        """
        if source_shape is not None and not re.search(r'([_A-Za-z]+-)?([A-Za-z_][A-Za-z0-9_]*-|(([A-Za-z_][A-Za-z0-9_]*)?\*))([0-9]{1}[0-9]{0,31})', source_shape):  # noqa: E501
            raise ValueError(r"Invalid value for `source_shape`, must be a follow pattern or equal to `/([_A-Za-z]+-)?([A-Za-z_][A-Za-z0-9_]*-|(([A-Za-z_][A-Za-z0-9_]*)?\*))([0-9]{1}[0-9]{0,31})/`")  # noqa: E501

        self._source_shape = source_shape

    @property
    def source_item(self):
        """Gets the source_item of this TransferLogEntryType.  # noqa: E501


        :return: The source_item of this TransferLogEntryType.  # noqa: E501
        :rtype: str
        """
        return self._source_item

    @source_item.setter
    def source_item(self, source_item):
        """Sets the source_item of this TransferLogEntryType.


        :param source_item: The source_item of this TransferLogEntryType.  # noqa: E501
        :type: str
        """
        if source_item is not None and not re.search(r'([_A-Za-z]+-)?([A-Za-z_][A-Za-z0-9_]*-|(([A-Za-z_][A-Za-z0-9_]*)?\*))([0-9]{1}[0-9]{0,31})', source_item):  # noqa: E501
            raise ValueError(r"Invalid value for `source_item`, must be a follow pattern or equal to `/([_A-Za-z]+-)?([A-Za-z_][A-Za-z0-9_]*-|(([A-Za-z_][A-Za-z0-9_]*)?\*))([0-9]{1}[0-9]{0,31})/`")  # noqa: E501

        self._source_item = source_item

    @property
    def destination_storage(self):
        """Gets the destination_storage of this TransferLogEntryType.  # noqa: E501


        :return: The destination_storage of this TransferLogEntryType.  # noqa: E501
        :rtype: str
        """
        return self._destination_storage

    @destination_storage.setter
    def destination_storage(self, destination_storage):
        """Sets the destination_storage of this TransferLogEntryType.


        :param destination_storage: The destination_storage of this TransferLogEntryType.  # noqa: E501
        :type: str
        """
        if destination_storage is not None and not re.search(r'([_A-Za-z]+-)?([A-Za-z_][A-Za-z0-9_]*-|(([A-Za-z_][A-Za-z0-9_]*)?\*))([0-9]{1}[0-9]{0,31})', destination_storage):  # noqa: E501
            raise ValueError(r"Invalid value for `destination_storage`, must be a follow pattern or equal to `/([_A-Za-z]+-)?([A-Za-z_][A-Za-z0-9_]*-|(([A-Za-z_][A-Za-z0-9_]*)?\*))([0-9]{1}[0-9]{0,31})/`")  # noqa: E501

        self._destination_storage = destination_storage

    @property
    def destination_item(self):
        """Gets the destination_item of this TransferLogEntryType.  # noqa: E501


        :return: The destination_item of this TransferLogEntryType.  # noqa: E501
        :rtype: str
        """
        return self._destination_item

    @destination_item.setter
    def destination_item(self, destination_item):
        """Sets the destination_item of this TransferLogEntryType.


        :param destination_item: The destination_item of this TransferLogEntryType.  # noqa: E501
        :type: str
        """
        if destination_item is not None and not re.search(r'([_A-Za-z]+-)?([A-Za-z_][A-Za-z0-9_]*-|(([A-Za-z_][A-Za-z0-9_]*)?\*))([0-9]{1}[0-9]{0,31})', destination_item):  # noqa: E501
            raise ValueError(r"Invalid value for `destination_item`, must be a follow pattern or equal to `/([_A-Za-z]+-)?([A-Za-z_][A-Za-z0-9_]*-|(([A-Za-z_][A-Za-z0-9_]*)?\*))([0-9]{1}[0-9]{0,31})/`")  # noqa: E501

        self._destination_item = destination_item

    @property
    def id(self):
        """Gets the id of this TransferLogEntryType.  # noqa: E501


        :return: The id of this TransferLogEntryType.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TransferLogEntryType.


        :param id: The id of this TransferLogEntryType.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def source_storage(self):
        """Gets the source_storage of this TransferLogEntryType.  # noqa: E501


        :return: The source_storage of this TransferLogEntryType.  # noqa: E501
        :rtype: str
        """
        return self._source_storage

    @source_storage.setter
    def source_storage(self, source_storage):
        """Sets the source_storage of this TransferLogEntryType.


        :param source_storage: The source_storage of this TransferLogEntryType.  # noqa: E501
        :type: str
        """
        if source_storage is not None and not re.search(r'([_A-Za-z]+-)?([A-Za-z_][A-Za-z0-9_]*-|(([A-Za-z_][A-Za-z0-9_]*)?\*))([0-9]{1}[0-9]{0,31})', source_storage):  # noqa: E501
            raise ValueError(r"Invalid value for `source_storage`, must be a follow pattern or equal to `/([_A-Za-z]+-)?([A-Za-z_][A-Za-z0-9_]*-|(([A-Za-z_][A-Za-z0-9_]*)?\*))([0-9]{1}[0-9]{0,31})/`")  # noqa: E501

        self._source_storage = source_storage

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
        if not isinstance(other, TransferLogEntryType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
