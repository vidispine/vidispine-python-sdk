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

class CollectionType(object):
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
        'absolute_time': 'bool',
        'loc': 'str',
        'merged_access': 'AccessControlMergedType',
        'name': 'str',
        'project': 'ProjectType',
        'sequence': 'list[SequenceType]',
        'terse': 'object',
        'content': 'list[CollectionContentType]',
        'external_id': 'list[ExternalIdentifierType]',
        'id': 'str',
        'metadata': 'MetadataType'
    }

    attribute_map = {
        'absolute_time': 'absoluteTime',
        'loc': 'loc',
        'merged_access': 'merged-access',
        'name': 'name',
        'project': 'project',
        'sequence': 'sequence',
        'terse': 'terse',
        'content': 'content',
        'external_id': 'externalId',
        'id': 'id',
        'metadata': 'metadata'
    }

    def __init__(self, absolute_time=None, loc=None, merged_access=None, name=None, project=None, sequence=None, terse=None, content=None, external_id=None, id=None, metadata=None):  # noqa: E501
        """CollectionType - a model defined in OpenAPI"""  # noqa: E501

        self._absolute_time = None
        self._loc = None
        self._merged_access = None
        self._name = None
        self._project = None
        self._sequence = None
        self._terse = None
        self._content = None
        self._external_id = None
        self._id = None
        self._metadata = None
        self.discriminator = None

        if absolute_time is not None:
            self.absolute_time = absolute_time
        if loc is not None:
            self.loc = loc
        if merged_access is not None:
            self.merged_access = merged_access
        if name is not None:
            self.name = name
        if project is not None:
            self.project = project
        if sequence is not None:
            self.sequence = sequence
        if terse is not None:
            self.terse = terse
        if content is not None:
            self.content = content
        if external_id is not None:
            self.external_id = external_id
        if id is not None:
            self.id = id
        if metadata is not None:
            self.metadata = metadata

    @property
    def absolute_time(self):
        """Gets the absolute_time of this CollectionType.  # noqa: E501


        :return: The absolute_time of this CollectionType.  # noqa: E501
        :rtype: bool
        """
        return self._absolute_time

    @absolute_time.setter
    def absolute_time(self, absolute_time):
        """Sets the absolute_time of this CollectionType.


        :param absolute_time: The absolute_time of this CollectionType.  # noqa: E501
        :type: bool
        """

        self._absolute_time = absolute_time

    @property
    def loc(self):
        """Gets the loc of this CollectionType.  # noqa: E501


        :return: The loc of this CollectionType.  # noqa: E501
        :rtype: str
        """
        return self._loc

    @loc.setter
    def loc(self, loc):
        """Sets the loc of this CollectionType.


        :param loc: The loc of this CollectionType.  # noqa: E501
        :type: str
        """

        self._loc = loc

    @property
    def merged_access(self):
        """Gets the merged_access of this CollectionType.  # noqa: E501


        :return: The merged_access of this CollectionType.  # noqa: E501
        :rtype: AccessControlMergedType
        """
        return self._merged_access

    @merged_access.setter
    def merged_access(self, merged_access):
        """Sets the merged_access of this CollectionType.


        :param merged_access: The merged_access of this CollectionType.  # noqa: E501
        :type: AccessControlMergedType
        """

        self._merged_access = merged_access

    @property
    def name(self):
        """Gets the name of this CollectionType.  # noqa: E501


        :return: The name of this CollectionType.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CollectionType.


        :param name: The name of this CollectionType.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def project(self):
        """Gets the project of this CollectionType.  # noqa: E501


        :return: The project of this CollectionType.  # noqa: E501
        :rtype: ProjectType
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this CollectionType.


        :param project: The project of this CollectionType.  # noqa: E501
        :type: ProjectType
        """

        self._project = project

    @property
    def sequence(self):
        """Gets the sequence of this CollectionType.  # noqa: E501


        :return: The sequence of this CollectionType.  # noqa: E501
        :rtype: list[SequenceType]
        """
        return self._sequence

    @sequence.setter
    def sequence(self, sequence):
        """Sets the sequence of this CollectionType.


        :param sequence: The sequence of this CollectionType.  # noqa: E501
        :type: list[SequenceType]
        """

        self._sequence = sequence

    @property
    def terse(self):
        """Gets the terse of this CollectionType.  # noqa: E501


        :return: The terse of this CollectionType.  # noqa: E501
        :rtype: object
        """
        return self._terse

    @terse.setter
    def terse(self, terse):
        """Sets the terse of this CollectionType.


        :param terse: The terse of this CollectionType.  # noqa: E501
        :type: object
        """

        self._terse = terse

    @property
    def content(self):
        """Gets the content of this CollectionType.  # noqa: E501


        :return: The content of this CollectionType.  # noqa: E501
        :rtype: list[CollectionContentType]
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this CollectionType.


        :param content: The content of this CollectionType.  # noqa: E501
        :type: list[CollectionContentType]
        """

        self._content = content

    @property
    def external_id(self):
        """Gets the external_id of this CollectionType.  # noqa: E501


        :return: The external_id of this CollectionType.  # noqa: E501
        :rtype: list[ExternalIdentifierType]
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this CollectionType.


        :param external_id: The external_id of this CollectionType.  # noqa: E501
        :type: list[ExternalIdentifierType]
        """

        self._external_id = external_id

    @property
    def id(self):
        """Gets the id of this CollectionType.  # noqa: E501


        :return: The id of this CollectionType.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CollectionType.


        :param id: The id of this CollectionType.  # noqa: E501
        :type: str
        """
        if id is not None and not re.search(r'([_A-Za-z]+-)?([A-Za-z_][A-Za-z0-9_]*-|(([A-Za-z_][A-Za-z0-9_]*)?\*))([0-9]{1}[0-9]{0,31})', id):  # noqa: E501
            raise ValueError(r"Invalid value for `id`, must be a follow pattern or equal to `/([_A-Za-z]+-)?([A-Za-z_][A-Za-z0-9_]*-|(([A-Za-z_][A-Za-z0-9_]*)?\*))([0-9]{1}[0-9]{0,31})/`")  # noqa: E501

        self._id = id

    @property
    def metadata(self):
        """Gets the metadata of this CollectionType.  # noqa: E501


        :return: The metadata of this CollectionType.  # noqa: E501
        :rtype: MetadataType
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this CollectionType.


        :param metadata: The metadata of this CollectionType.  # noqa: E501
        :type: MetadataType
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
        if not isinstance(other, CollectionType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other