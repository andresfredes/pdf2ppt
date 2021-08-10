# Copyright 2021, Andres Fredes, <andres.hector.fredes@gmail.com>
# 
# This file is part of pdf2ppt.
# 
#     pdf2ppt is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
# 
#     pdf2ppt is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
# 
#     You should have received a copy of the GNU General Public License
#     along with pdf2ppt.  If not, see <https://www.gnu.org/licenses/>.

WINDOW = {
    "XPOS":0,
    "YPOS":0,
    "WIDTH":500,
    "HEIGHT":100,
}

# Index of "Blank" slide layout in a typical install of Powerpoint
BLANK_SLIDE = 6

# Template file location
PPT_TEMPLATE = "./template2.pptx"

# 16:9 ratio range - to allow for floating point rounding / non-pixel perfect
# images to still be loosely categorised as 16:9
RATIO_16_9 = {
    "MIN": 1.75,
    "MAX": 1.80,
}

SLIDE = {
    "WIDTH": 28.0,
    "HEIGHT": 15.75,
}