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

class JobType(object):
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
        'status': 'str',
        'total_steps': 'int',
        'log': 'JobTypeLog',
        'started': 'datetime',
        'data': 'list[StorageGroupTypeData]',
        'waiting': 'JobTypeWaiting',
        'current_step': 'JobTypeCurrentStep',
        'job_id': 'str',
        'priority': 'str',
        'sub_job': 'list[JobType]',
        'finished': 'datetime',
        'user': 'str',
        'type': 'str'
    }

    attribute_map = {
        'status': 'status',
        'total_steps': 'totalSteps',
        'log': 'log',
        'started': 'started',
        'data': 'data',
        'waiting': 'waiting',
        'current_step': 'currentStep',
        'job_id': 'jobId',
        'priority': 'priority',
        'sub_job': 'subJob',
        'finished': 'finished',
        'user': 'user',
        'type': 'type'
    }

    def __init__(self, status=None, total_steps=None, log=None, started=None, data=None, waiting=None, current_step=None, job_id=None, priority=None, sub_job=None, finished=None, user=None, type=None):  # noqa: E501
        """JobType - a model defined in OpenAPI"""  # noqa: E501

        self._status = None
        self._total_steps = None
        self._log = None
        self._started = None
        self._data = None
        self._waiting = None
        self._current_step = None
        self._job_id = None
        self._priority = None
        self._sub_job = None
        self._finished = None
        self._user = None
        self._type = None
        self.discriminator = None

        self.status = status
        if total_steps is not None:
            self.total_steps = total_steps
        if log is not None:
            self.log = log
        if started is not None:
            self.started = started
        if data is not None:
            self.data = data
        if waiting is not None:
            self.waiting = waiting
        if current_step is not None:
            self.current_step = current_step
        self.job_id = job_id
        self.priority = priority
        if sub_job is not None:
            self.sub_job = sub_job
        if finished is not None:
            self.finished = finished
        if user is not None:
            self.user = user
        self.type = type

    @property
    def status(self):
        """Gets the status of this JobType.  # noqa: E501


        :return: The status of this JobType.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this JobType.


        :param status: The status of this JobType.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def total_steps(self):
        """Gets the total_steps of this JobType.  # noqa: E501


        :return: The total_steps of this JobType.  # noqa: E501
        :rtype: int
        """
        return self._total_steps

    @total_steps.setter
    def total_steps(self, total_steps):
        """Sets the total_steps of this JobType.


        :param total_steps: The total_steps of this JobType.  # noqa: E501
        :type: int
        """

        self._total_steps = total_steps

    @property
    def log(self):
        """Gets the log of this JobType.  # noqa: E501


        :return: The log of this JobType.  # noqa: E501
        :rtype: JobTypeLog
        """
        return self._log

    @log.setter
    def log(self, log):
        """Sets the log of this JobType.


        :param log: The log of this JobType.  # noqa: E501
        :type: JobTypeLog
        """

        self._log = log

    @property
    def started(self):
        """Gets the started of this JobType.  # noqa: E501


        :return: The started of this JobType.  # noqa: E501
        :rtype: datetime
        """
        return self._started

    @started.setter
    def started(self, started):
        """Sets the started of this JobType.


        :param started: The started of this JobType.  # noqa: E501
        :type: datetime
        """

        self._started = started

    @property
    def data(self):
        """Gets the data of this JobType.  # noqa: E501


        :return: The data of this JobType.  # noqa: E501
        :rtype: list[StorageGroupTypeData]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this JobType.


        :param data: The data of this JobType.  # noqa: E501
        :type: list[StorageGroupTypeData]
        """

        self._data = data

    @property
    def waiting(self):
        """Gets the waiting of this JobType.  # noqa: E501


        :return: The waiting of this JobType.  # noqa: E501
        :rtype: JobTypeWaiting
        """
        return self._waiting

    @waiting.setter
    def waiting(self, waiting):
        """Sets the waiting of this JobType.


        :param waiting: The waiting of this JobType.  # noqa: E501
        :type: JobTypeWaiting
        """

        self._waiting = waiting

    @property
    def current_step(self):
        """Gets the current_step of this JobType.  # noqa: E501


        :return: The current_step of this JobType.  # noqa: E501
        :rtype: JobTypeCurrentStep
        """
        return self._current_step

    @current_step.setter
    def current_step(self, current_step):
        """Sets the current_step of this JobType.


        :param current_step: The current_step of this JobType.  # noqa: E501
        :type: JobTypeCurrentStep
        """

        self._current_step = current_step

    @property
    def job_id(self):
        """Gets the job_id of this JobType.  # noqa: E501


        :return: The job_id of this JobType.  # noqa: E501
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this JobType.


        :param job_id: The job_id of this JobType.  # noqa: E501
        :type: str
        """
        if job_id is None:
            raise ValueError("Invalid value for `job_id`, must not be `None`")  # noqa: E501
        if job_id is not None and not re.search(r'([_A-Za-z]+-)?([A-Za-z_][A-Za-z0-9_]*-|(([A-Za-z_][A-Za-z0-9_]*)?\*))([0-9]{1}[0-9]{0,31})', job_id):  # noqa: E501
            raise ValueError(r"Invalid value for `job_id`, must be a follow pattern or equal to `/([_A-Za-z]+-)?([A-Za-z_][A-Za-z0-9_]*-|(([A-Za-z_][A-Za-z0-9_]*)?\*))([0-9]{1}[0-9]{0,31})/`")  # noqa: E501

        self._job_id = job_id

    @property
    def priority(self):
        """Gets the priority of this JobType.  # noqa: E501


        :return: The priority of this JobType.  # noqa: E501
        :rtype: str
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this JobType.


        :param priority: The priority of this JobType.  # noqa: E501
        :type: str
        """
        if priority is None:
            raise ValueError("Invalid value for `priority`, must not be `None`")  # noqa: E501

        self._priority = priority

    @property
    def sub_job(self):
        """Gets the sub_job of this JobType.  # noqa: E501


        :return: The sub_job of this JobType.  # noqa: E501
        :rtype: list[JobType]
        """
        return self._sub_job

    @sub_job.setter
    def sub_job(self, sub_job):
        """Sets the sub_job of this JobType.


        :param sub_job: The sub_job of this JobType.  # noqa: E501
        :type: list[JobType]
        """

        self._sub_job = sub_job

    @property
    def finished(self):
        """Gets the finished of this JobType.  # noqa: E501


        :return: The finished of this JobType.  # noqa: E501
        :rtype: datetime
        """
        return self._finished

    @finished.setter
    def finished(self, finished):
        """Sets the finished of this JobType.


        :param finished: The finished of this JobType.  # noqa: E501
        :type: datetime
        """

        self._finished = finished

    @property
    def user(self):
        """Gets the user of this JobType.  # noqa: E501


        :return: The user of this JobType.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this JobType.


        :param user: The user of this JobType.  # noqa: E501
        :type: str
        """

        self._user = user

    @property
    def type(self):
        """Gets the type of this JobType.  # noqa: E501


        :return: The type of this JobType.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this JobType.


        :param type: The type of this JobType.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

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
        if not isinstance(other, JobType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other