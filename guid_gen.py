"""
GUID generator example
By Toyomasa Watarai

Copyright (c) 2016 ARM Limited
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
    http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
#! /usr/bin/env python
# codeing: utf-8

import uuid
import re

head1 = [
    'const uint8_t arm_uc_vendor_id[] = {',
    'const uint8_t arm_uc_class_id[] = {',
    'const uint8_t arm_uc_device_id[] = {'
]

head2 = [
    'const uint16_t arm_uc_vendor_id_size = sizeof(arm_uc_vendor_id);',
    'const uint16_t arm_uc_class_id_size = sizeof(arm_uc_class_id);',
    'const uint16_t arm_uc_device_id_size = sizeof(arm_uc_device_id);'
]

def print_guid(x, idx):
    print '//', x
    print head1[idx]
    words = re.split('(..)',x.hex)[1::2]
    for hex in words[:-1]:
        print '0x' + hex + ',',
    print '0x' + words[-1]
    print '};'
    print head2[idx]
    print

print_guid(uuid.uuid4(), 0)
print_guid(uuid.uuid4(), 1)
print_guid(uuid.uuid4(), 2)
