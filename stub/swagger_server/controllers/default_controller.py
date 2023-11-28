import connexion
import six

from swagger_server.models.height import Height  # noqa: E501
from swagger_server import util


def controller_get_height():  # noqa: E501
    """Returns a list of heights.

     # noqa: E501


    :rtype: List[Height]
    """
    return 'do some magic!'


def controller_get_height_details(height_id):  # noqa: E501
    """Returns complete details of the specified height

     # noqa: E501

    :param height_id: 
    :type height_id: int

    :rtype: Height
    """
    return 'do some magic!'


def controller_get_height_pm_average(height_id):  # noqa: E501
    """Returns the average collected PMs for specific height.

     # noqa: E501

    :param height_id: 
    :type height_id: int

    :rtype: float
    """
    return 'do some magic!'


def controller_get_pms_in_height(height_id):  # noqa: E501
    """Returns a list of collected PMs for specific height.

     # noqa: E501

    :param height_id: 
    :type height_id: int

    :rtype: float
    """
    return 'do some magic!'
