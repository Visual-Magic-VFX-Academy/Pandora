# -*- coding: utf-8 -*-
#
####################################################
#
# Pandora - Renderfarm Manager
#
# https://prism-pipeline.com/pandora/
#
# contact: contact@prism-pipeline.com
#
####################################################
#
#
# Copyright (C) 2016-2020 Richard Frangenberg
#
# Licensed under GNU GPL-3.0-or-later
#
# This file is part of Pandora.
#
# Pandora is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Pandora is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Pandora.  If not, see <https://www.gnu.org/licenses/>.


class Pandora_Maya_Variables(object):
    def __init__(self, core, plugin):
        self.version = "v1.0.3.2"
        self.pluginName = "Maya"
        self.pluginType = "App"
        self.appShortName = "Maya"
        self.appType = "3d"
        self.hasQtParent = True
        self.sceneFormats = [".ma", ".mb"]
        self.appSpecificFormats = self.sceneFormats
        self.appColor = [44, 121, 207]
        self.platforms = ["Windows"]
        self.executableName = "Render.exe"
        self.frameString = ""
