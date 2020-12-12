#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Port enabler for devices with RLANs

Copyright (c) 2020 Cisco and/or its affiliates.

This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at

               https://developer.cisco.com/docs/licenses

All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.

"""

__author__ = "Eric Pylko"
__email__ = "erpylko@cisco.com"
__version__ = "0.1.0"
__copyright__ = "Copyright (c) 2020 Cisco and/or its affiliates."
__license__ = "Cisco Sample Code License, Version 1.1"

from dnacentersdk import api

#
# Specify your DNAC info.
#
DNAC='YOUR_DNAC_URL'
USER='YOUR_DNAC_ADMIN_USER'
PASS='YOUR_DNAC_ADMIN_PASSWORD''

#
# wireless controller specifications
#
controller_id="YOUR_C9800_IP"
controller_type="MANAGED_DEVICE_IP"

#
# specify what devices we want returned from DNAC
#
devicefamily = "Unified AP"

#
# specify what AP types you want to manipulate
#
aptypes = {'AIR-AP1815W-B-K9','C9105AXI-B'}

#
# info about your template
#
template="enablePorts"

#
# open connection to DNAC center
#
dnac = api.DNACenterAPI(base_url=DNAC, username=USER, password=PASS)

#
# get template info from DNAC and pull out the templateID
#
templates = (dnac.configuration_templates.gets_the_templates_available())
template_dict = list(filter(lambda x:x["name"]==template,templates))[0]
template_id = template_dict['templateId']

#
# get the devices
#
devices = dnac.devices.get_device_list(family=devicefamily)

count = 0
for device in devices.response:
    if device.platformId in aptypes:
        print ("Processing",device.hostname)
        count += 1
        target_info = [{
            "id": controller_id,
            "type": controller_type,
            "params": {"ap": device.hostname}
        }]
        status = dnac.configuration_templates.deploy_template(
            forcePushTemplate=True,
            templateId=template_id,
            targetInfo=target_info)
        # there should probably be some sort of status check here

print ("Processed",count,"APs")
