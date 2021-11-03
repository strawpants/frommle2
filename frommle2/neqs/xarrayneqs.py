# This file is part of frommle2.
# frommle2 is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 3 of the License, or (at your option) any later version.

# frommle2 is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public
# License along with Frommle; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA

# Author Roelof Rietbroek (r.rietbroek@utwente.nl), 2021




import xarray as xr
import numpy as np


@xr.register_dataset_accessor("neqs")
class NEQSAccessor:
    def __init__(self, xarray_obj):
        self._obj = xarray_obj

    
    def extend(self):
        """Truncate minimum and /or maximum degree"""
        self.test="blah" 
        return self._obj

