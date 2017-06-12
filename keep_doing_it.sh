#!/bin/sh -eu

# This file is part of hashtable.
#
# Copyright (c) 2017, Martin Stensgård.
# All rights reserved.
#
# hashtable is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, only version 3 of the License.
#
# hashtable is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with hashtable. If not, see <http://www.gnu.org/licenses/>.

#find | entr -c sh -c './build.sh && ./test_one'
#find | entr -c sh -c './build.sh && ./hashtable.py one'
ls -d * | entr -c sh -c './build.sh && ./check.py'
