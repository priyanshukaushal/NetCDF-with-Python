# -*- coding: utf-8 -*-
"""
/***************************************************************************
 netcdf_visualizer
                                 A QGIS plugin
 converts netcdf data to raster data
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2022-03-11
        copyright            : (C) 2022 by Priyanshu Kaushal
        email                : priyanshu.kaushal2001@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load netcdf_visualizer class from file netcdf_visualizer.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .netcdf_visualizer import netcdf_visualizer
    return netcdf_visualizer(iface)