#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, Your Name <YourName@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = r'''
---
module: rz_mod_1.oy
short_description: Test creating ansible module, just do echo
description
  - Echo json input
  - Description 2
  - Description 3
requirements:
  - python >= 3.0
options:
  custom_opt_1:
    description: 
      - This is a description of custom_opt_1
      - Additional description
    type: bool
    required: true
  custom_opt_2:
    description:
      - This is a description of custom_opt_2
    type: str
    required: true
  custom_opt_3:
    descipriotn: This is a description of custom_opp_3
    type: int
  custom_opt_4:
    description: This is a description of custom_app_4
    type: str
    choise: [present, absent]
    default: present
  custom_opt_5:
    description: This is a description of custom_app_5
    type: dict
    required: false
  custom_opt_6:
    description: This is a description of custom_app_6
    type: dict
    suboptions:
      sub_1:
        description: This is a description (str) of sub-dic of custom_app_6
        type: str
        required: true
      sub_2:
        description: This is a description (int) of sub-dic of custom_app_6
        type: int
        required: false
notes:
  - this is note 1
  - this is note 2
'''

EXAMPLES = r'''
# Option 1
- name: testi option 1
  rz_mod_1:
    custom_opt_1: yes
    custom_opt_2: this-is-a-string
    custom_opt_3: 123
    custom_opt_4: present
    custom_opt_5:
      key1: val2
      key2: val2
    custom_opt_6:
      sub_1: val-string-sub-1
      sub_2: 333
'''

RETURN = r'''
output_1:
  description: output-type-str
  returned: success
  type: str
  sample: "Sample of output_1"
output_2
  description: output-type-int
  returned: success
  type: int
  sample: 321
output_3
  description: output-type-list
  returned: success
  type: list
output_4
  description: output-type-dict
  returned: success
  type: dict
output_5
  description: output-type-complex
  returned: success
  type: str
  contains:
    o_sub_1:
      description: This is an output (str) of output_5.o_sub_1
      returned: success
      type: string
    o_sub_2:
      description: This is an output (int) of output_5.o_sub_2
      returned: success
      type: int
'''

from ansible.module_utils.basic import AnsibleModule

def run_module():
  module = AnsibleModule(
    argument_spec=dict(
      custom_opt_1 = dict(type='bool', required=True),
      custom_opt_2 = dict(type='str', required=True),
    ),
    supports_check_mode=True,
  )
  result = {
    'changed': True,
    'msg1': "output-m-1",
    'msg2': "output-m-2",
  }
  module.exit_json(changed=True)

def main():
  run_module()

if __name__ == '__main__':
  main()
