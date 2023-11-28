# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.height import Height  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_controller_get_height(self):
        """Test case for controller_get_height

        Returns a list of heights.
        """
        response = self.client.open(
            '/air_pollution_height//heights',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_controller_get_height_details(self):
        """Test case for controller_get_height_details

        Returns complete details of the specified height
        """
        response = self.client.open(
            '/air_pollution_height//heights/{heightId}'.format(height_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_controller_get_height_pm_average(self):
        """Test case for controller_get_height_pm_average

        Returns the average collected PMs for specific height.
        """
        response = self.client.open(
            '/air_pollution_height//heights/{heightId}/avgPMS7'.format(height_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_controller_get_pms_in_height(self):
        """Test case for controller_get_pms_in_height

        Returns a list of collected PMs for specific height.
        """
        response = self.client.open(
            '/air_pollution_height//heights/{heightId}/pm'.format(height_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
