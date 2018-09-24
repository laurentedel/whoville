# coding: utf-8

"""
    Cloudbreak API

    Cloudbreak is a powerful left surf that breaks over a coral reef, a mile off southwest the island of Tavarua, Fiji. Cloudbreak is a cloud agnostic Hadoop as a Service API. Abstracts the provisioning and ease management and monitoring of on-demand clusters. SequenceIQ's Cloudbreak is a RESTful application development platform with the goal of helping developers to build solutions for deploying Hadoop YARN clusters in different environments. Once it is deployed in your favourite servlet container it exposes a REST API allowing to span up Hadoop clusters of arbitary sizes and cloud providers. Provisioning Hadoop has never been easier. Cloudbreak is built on the foundation of cloud providers API (Amazon AWS, Microsoft Azure, Google Cloud Platform, Openstack), Apache Ambari, Docker lightweight containers, Swarm and Consul. For further product documentation follow the link: <a href=\"http://hortonworks.com/apache/cloudbreak/\">http://hortonworks.com/apache/cloudbreak/</a>

    OpenAPI spec version: 2.7.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class SpecialParametersJson(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'special_parameters': 'dict(str, bool)',
        'platform_specific_special_parameters': 'dict(str, dict(str, bool))'
    }

    attribute_map = {
        'special_parameters': 'specialParameters',
        'platform_specific_special_parameters': 'platformSpecificSpecialParameters'
    }

    def __init__(self, special_parameters=None, platform_specific_special_parameters=None):
        """
        SpecialParametersJson - a model defined in Swagger
        """

        self._special_parameters = None
        self._platform_specific_special_parameters = None

        if special_parameters is not None:
          self.special_parameters = special_parameters
        if platform_specific_special_parameters is not None:
          self.platform_specific_special_parameters = platform_specific_special_parameters

    @property
    def special_parameters(self):
        """
        Gets the special_parameters of this SpecialParametersJson.
        custom parameters

        :return: The special_parameters of this SpecialParametersJson.
        :rtype: dict(str, bool)
        """
        return self._special_parameters

    @special_parameters.setter
    def special_parameters(self, special_parameters):
        """
        Sets the special_parameters of this SpecialParametersJson.
        custom parameters

        :param special_parameters: The special_parameters of this SpecialParametersJson.
        :type: dict(str, bool)
        """

        self._special_parameters = special_parameters

    @property
    def platform_specific_special_parameters(self):
        """
        Gets the platform_specific_special_parameters of this SpecialParametersJson.
        platform specific custom parameters

        :return: The platform_specific_special_parameters of this SpecialParametersJson.
        :rtype: dict(str, dict(str, bool))
        """
        return self._platform_specific_special_parameters

    @platform_specific_special_parameters.setter
    def platform_specific_special_parameters(self, platform_specific_special_parameters):
        """
        Sets the platform_specific_special_parameters of this SpecialParametersJson.
        platform specific custom parameters

        :param platform_specific_special_parameters: The platform_specific_special_parameters of this SpecialParametersJson.
        :type: dict(str, dict(str, bool))
        """

        self._platform_specific_special_parameters = platform_specific_special_parameters

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, SpecialParametersJson):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
