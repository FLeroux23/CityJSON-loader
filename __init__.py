# -*- coding: utf-8 -*-
"""
/***************************************************************************
 CityJsonLoader
                                 A QGIS plugin
 This plugin allows for CityJSON files to be loaded in QGIS
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2018-06-08
        copyright            : (C) 2018 by 3D Geoinformation
        email                : s.vitalis@tudelft.nl
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
    """Load CityJsonLoader class from file CityJsonLoader.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .cityjson_loader import CityJsonLoader
    return CityJsonLoader(iface)
