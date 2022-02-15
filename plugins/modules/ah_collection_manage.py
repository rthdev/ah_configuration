#!/usr/bin/python
# coding: utf-8 -*-

# (c) 2020, Sean Sullivan <@sean-m-sullivan>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type


ANSIBLE_METADATA = {"metadata_version": "1.1", "status": ["preview"], "supported_by": "community"}


DOCUMENTATION = """
---
module: ah_collection_manage
author: "Sean Sullivan (@sean-m-sullivan)"
short_description: update, or destroy Automation Hub Collections.
description:
    - Update, or destroy Automation Hub Collections. See
      U(https://www.ansible.com/) for an overview.
options:
    namespace:
      description:
        - Namespace name. Must be lower case containing only alphanumeric characters and underscores.
      required: True
      type: str
    name:
      description:
        - Collection name. Must be lower case containing only alphanumeric characters and underscores.
      required: True
      type: str
    version:
      description:
        - Collection Version. Must be lower case containing only alphanumeric characters and underscores.
      type: str
    state:
      description:
        - Desired state of the resource.
        - If present will return data on a collection.
        - If present with version, will return data on a collection version.
        - If absent without version, will delete the collection and all versions.
        - If absent with version, will delete only specified version.
      choices: ["present", "absent"]
      default: "present"
      type: str

extends_documentation_fragment: redhat_cop.ah_configuration.auth
"""


EXAMPLES = """
- name: Remove collection
  ah_collection_manage:
    namespace: test_collection
    name: test
    version: 4.1.2
    state: absent
"""

from ..module_utils.ah_module import AHModule


def main():
    # Any additional arguments that are not fields of the item can be added here
    argument_spec = dict(
        namespace=dict(required=True),
        name=dict(required=True),
        version=dict(),
        state=dict(choices=["present", "absent"], default="present"),
    )

    # Create a module for ourselves
    module = AHModule(argument_spec=argument_spec)

    # Extract our parameters
    namespace = module.params.get("namespace")
    name = module.params.get("name")
    version = module.params.get("version")
    state = module.params.get("state")

    new_fields = {}

    # Attempt to look up an existing item based on the provided data
    if version:
      #existing_item = module.get_endpoint("collections/{0}/{1}/versions/{2}".format(namespace, name, version), None, **{"return_none_on_404": True})
      collection_endpoint = "collections/{0}/{1}/versions/{2}".format(namespace, name, version)
    else:
      collection_endpoint = "collections/{0}/{1}".format(namespace, name)
      #existing_item = module.get_endpoint("collections/{0}/{1}".format(namespace, name), None, **{"return_none_on_404": True})


    existing_item = module.get_endpoint(collection_endpoint, **{"return_none_on_404": True})
    if existing_item is None:
        if version:
              module.fail_json(msg='Could not find Collection {0}.{1} with_version {2}'.format(namespace, name, version))
        else:
              module.fail_json(msg='Could not find Collection {0}.{1}'.format(namespace, name))
    else:
        response = existing_item['json']

    if state == "absent":
        # If the state was absent we can let the module delete it if needed, the module will handle exiting from this
        response["task"] = module.delete_endpoint(existing_item['json']['href'])['json']['task']
        response["deleted"] = True
        response["changed"] = True


    # If the state was present and we can Return information about the collection
    module.exit_json(**response)


if __name__ == "__main__":
    main()
