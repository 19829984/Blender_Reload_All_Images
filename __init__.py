# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
from . import operator_reload_all_img
import bpy

bl_info = {
    "name": "Reload All Images",
    "author": "Bowen Wu",
    "description": "Simple tool to reload all images you have in Blender",
    "blender": (2, 80, 3),
    "version": (1, 0, 0),
    "location": "",
    "warning": "",
    "category": "Import-Export"
}


def register():
    operator_reload_all_img.register()


def unregister():
    bpy.ops.timelapse.pause_modal_operator()
    operator_reload_all_img.register()
