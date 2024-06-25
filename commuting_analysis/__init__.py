# -*- coding: utf-8 -*-
"""
/***************************************************************************
 CommutingAnalysis
                                 A QGIS plugin
 This plugin analysis and visualises coummting data.
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2018-11-23
        copyright            : (C) 2018-2024 by Kristian Bergstrand
        email                : kristian.bergstrand@sweco.se
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
    """Load CommutingAnalysis class from file CommutingAnalysis.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .commuting_analysis import CommutingAnalysis
    return CommutingAnalysis(iface)