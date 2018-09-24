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


class CloudbreakFlexUsage(object):
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
        'controller': 'FlexUsageControllerJson',
        'products': 'list[FlexUsageProductJson]'
    }

    attribute_map = {
        'controller': 'controller',
        'products': 'products'
    }

    def __init__(self, controller=None, products=None):
        """
        CloudbreakFlexUsage - a model defined in Swagger
        """

        self._controller = None
        self._products = None

        if controller is not None:
          self.controller = controller
        if products is not None:
          self.products = products

    @property
    def controller(self):
        """
        Gets the controller of this CloudbreakFlexUsage.

        :return: The controller of this CloudbreakFlexUsage.
        :rtype: FlexUsageControllerJson
        """
        return self._controller

    @controller.setter
    def controller(self, controller):
        """
        Sets the controller of this CloudbreakFlexUsage.

        :param controller: The controller of this CloudbreakFlexUsage.
        :type: FlexUsageControllerJson
        """

        self._controller = controller

    @property
    def products(self):
        """
        Gets the products of this CloudbreakFlexUsage.

        :return: The products of this CloudbreakFlexUsage.
        :rtype: list[FlexUsageProductJson]
        """
        return self._products

    @products.setter
    def products(self, products):
        """
        Sets the products of this CloudbreakFlexUsage.

        :param products: The products of this CloudbreakFlexUsage.
        :type: list[FlexUsageProductJson]
        """

        self._products = products

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
        if not isinstance(other, CloudbreakFlexUsage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
