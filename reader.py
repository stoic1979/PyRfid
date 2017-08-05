#
# Script for reading RFID from USB RFID Reader
#
# Copyright (C) 2017  Navjot Singh <weavebytes@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

#!/usr/bin/env python

from evdev import InputDevice, ecodes, list_devices
from select import select


# input device may be event1, event2 or eventN
INPUT_DEVICE = "/dev/input/event7"

# barcode length, change it if neded
MAX_BARCODE = 10

keys = "X^1234567890XXXXqwertzuiopXXXXasdfghjklXXXXXyxcvbnmXXXXXXXXXXXXXXXXXXXXXXX"
dev = InputDevice(INPUT_DEVICE)

barcode = ""
while True:
    r,w,x = select([dev], [], [])

    for event in dev.read():
        if event.type == 1 and event.value == 1:
             barcode += (keys[event.code])

    if (len (barcode)) >= MAX_BARCODE:
        break;

print "barcode: [%s]" % barcode
