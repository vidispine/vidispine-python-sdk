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

class TaskDefinitionType(object):
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
        'description': 'str',
        'script': 'str',
        'extradata': 'str',
        'dependency': 'TaskDefinitionDependency',
        'step': 'int',
        'cleanup': 'bool',
        'flags': 'int',
        'critical': 'bool',
        'parallel_dependency': 'TaskDefinitionDependency',
        'id': 'int',
        'job_type': 'str',
        'metadata': 'SimpleMetadataType'
    }

    attribute_map = {
        'description': 'description',
        'script': 'script',
        'extradata': 'extradata',
        'dependency': 'dependency',
        'step': 'step',
        'cleanup': 'cleanup',
        'flags': 'flags',
        'critical': 'critical',
        'parallel_dependency': 'parallelDependency',
        'id': 'id',
        'job_type': 'jobType',
        'metadata': 'metadata'
    }

    def __init__(self, description=None, script=None, extradata=None, dependency=None, step=None, cleanup=None, flags=None, critical=None, parallel_dependency=None, id=None, job_type=None, metadata=None):  # noqa: E501
        """TaskDefinitionType - a model defined in OpenAPI"""  # noqa: E501

        self._description = None
        self._script = None
        self._extradata = None
        self._dependency = None
        self._step = None
        self._cleanup = None
        self._flags = None
        self._critical = None
        self._parallel_dependency = None
        self._id = None
        self._job_type = None
        self._metadata = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if script is not None:
            self.script = script
        if extradata is not None:
            self.extradata = extradata
        if dependency is not None:
            self.dependency = dependency
        if step is not None:
            self.step = step
        if cleanup is not None:
            self.cleanup = cleanup
        if flags is not None:
            self.flags = flags
        if critical is not None:
            self.critical = critical
        if parallel_dependency is not None:
            self.parallel_dependency = parallel_dependency
        if id is not None:
            self.id = id
        if job_type is not None:
            self.job_type = job_type
        if metadata is not None:
            self.metadata = metadata

    @property
    def description(self):
        """Gets the description of this TaskDefinitionType.  # noqa: E501


        :return: The description of this TaskDefinitionType.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TaskDefinitionType.


        :param description: The description of this TaskDefinitionType.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def script(self):
        """Gets the script of this TaskDefinitionType.  # noqa: E501


        :return: The script of this TaskDefinitionType.  # noqa: E501
        :rtype: str
        """
        return self._script

    @script.setter
    def script(self, script):
        """Sets the script of this TaskDefinitionType.


        :param script: The script of this TaskDefinitionType.  # noqa: E501
        :type: str
        """

        self._script = script

    @property
    def extradata(self):
        """Gets the extradata of this TaskDefinitionType.  # noqa: E501


        :return: The extradata of this TaskDefinitionType.  # noqa: E501
        :rtype: str
        """
        return self._extradata

    @extradata.setter
    def extradata(self, extradata):
        """Sets the extradata of this TaskDefinitionType.


        :param extradata: The extradata of this TaskDefinitionType.  # noqa: E501
        :type: str
        """

        self._extradata = extradata

    @property
    def dependency(self):
        """Gets the dependency of this TaskDefinitionType.  # noqa: E501


        :return: The dependency of this TaskDefinitionType.  # noqa: E501
        :rtype: TaskDefinitionDependency
        """
        return self._dependency

    @dependency.setter
    def dependency(self, dependency):
        """Sets the dependency of this TaskDefinitionType.


        :param dependency: The dependency of this TaskDefinitionType.  # noqa: E501
        :type: TaskDefinitionDependency
        """

        self._dependency = dependency

    @property
    def step(self):
        """Gets the step of this TaskDefinitionType.  # noqa: E501


        :return: The step of this TaskDefinitionType.  # noqa: E501
        :rtype: int
        """
        return self._step

    @step.setter
    def step(self, step):
        """Sets the step of this TaskDefinitionType.


        :param step: The step of this TaskDefinitionType.  # noqa: E501
        :type: int
        """

        self._step = step

    @property
    def cleanup(self):
        """Gets the cleanup of this TaskDefinitionType.  # noqa: E501


        :return: The cleanup of this TaskDefinitionType.  # noqa: E501
        :rtype: bool
        """
        return self._cleanup

    @cleanup.setter
    def cleanup(self, cleanup):
        """Sets the cleanup of this TaskDefinitionType.


        :param cleanup: The cleanup of this TaskDefinitionType.  # noqa: E501
        :type: bool
        """

        self._cleanup = cleanup

    @property
    def flags(self):
        """Gets the flags of this TaskDefinitionType.  # noqa: E501


        :return: The flags of this TaskDefinitionType.  # noqa: E501
        :rtype: int
        """
        return self._flags

    @flags.setter
    def flags(self, flags):
        """Sets the flags of this TaskDefinitionType.


        :param flags: The flags of this TaskDefinitionType.  # noqa: E501
        :type: int
        """

        self._flags = flags

    @property
    def critical(self):
        """Gets the critical of this TaskDefinitionType.  # noqa: E501


        :return: The critical of this TaskDefinitionType.  # noqa: E501
        :rtype: bool
        """
        return self._critical

    @critical.setter
    def critical(self, critical):
        """Sets the critical of this TaskDefinitionType.


        :param critical: The critical of this TaskDefinitionType.  # noqa: E501
        :type: bool
        """

        self._critical = critical

    @property
    def parallel_dependency(self):
        """Gets the parallel_dependency of this TaskDefinitionType.  # noqa: E501


        :return: The parallel_dependency of this TaskDefinitionType.  # noqa: E501
        :rtype: TaskDefinitionDependency
        """
        return self._parallel_dependency

    @parallel_dependency.setter
    def parallel_dependency(self, parallel_dependency):
        """Sets the parallel_dependency of this TaskDefinitionType.


        :param parallel_dependency: The parallel_dependency of this TaskDefinitionType.  # noqa: E501
        :type: TaskDefinitionDependency
        """

        self._parallel_dependency = parallel_dependency

    @property
    def id(self):
        """Gets the id of this TaskDefinitionType.  # noqa: E501


        :return: The id of this TaskDefinitionType.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TaskDefinitionType.


        :param id: The id of this TaskDefinitionType.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def job_type(self):
        """Gets the job_type of this TaskDefinitionType.  # noqa: E501


        :return: The job_type of this TaskDefinitionType.  # noqa: E501
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        """Sets the job_type of this TaskDefinitionType.


        :param job_type: The job_type of this TaskDefinitionType.  # noqa: E501
        :type: str
        """

        self._job_type = job_type

    @property
    def metadata(self):
        """Gets the metadata of this TaskDefinitionType.  # noqa: E501


        :return: The metadata of this TaskDefinitionType.  # noqa: E501
        :rtype: SimpleMetadataType
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this TaskDefinitionType.


        :param metadata: The metadata of this TaskDefinitionType.  # noqa: E501
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
        if not isinstance(other, TaskDefinitionType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
