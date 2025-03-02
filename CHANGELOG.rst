=========================================
redhat_cop.ah_configuration Release Notes
=========================================

.. contents:: Topics


v0.7.0
======

Major Changes
-------------

- Added ability to add remote repositories in ah_ee_repository module.
- Adds ah_ee_registry module
- Adds ah_ee_registry_index module
- Adds ah_ee_registry_sync module
- Adds ee_registry role
- Adds ee_registry_index role
- Adds ee_registry_sync role
- module ah_collection can now upload and delete collections

Minor Changes
-------------

- Added group permissions for remote registry management - add_containerregistryremote, change_containerregistryremote, delete_containerregistryremote.
- ah_hostname becomes an alias for ah_host in modules
- ah_hostname is now the default option for roles, though ah_host remains an alias

Breaking Changes / Porting Guide
--------------------------------

- Options for state in ah_ee_image and ah_ee_repository modules changed from 'updated' to 'present' as a bug fix.
- module ah_collection_upload has been removed.

New Modules
-----------

- redhat_cop.ah_configuration.ah_ee_registry - Manage private automation hub execution environment remote registries.

v0.6.1
======

Minor Changes
-------------

- added namespace state absent module parameter
- added new permision options to the ah_group_perm module and group role.
- ah_ee_namespace and ah_ee_repository - adding the ``new_name`` parameter so that users can rename namespaces and repositories (https://github.com/redhat-cop/ah_configuration/issues/44)
- removed dependency for ansible.galaxy module which wasn't accessible in 2.12 Ansible

v0.5.5
======

Bugfixes
--------

- Add the `no_log` attribute to the `password` and `proxy_password` fields of the `ah_repository` module (Resolves

v0.5.0
======

Major Changes
-------------

- Added execution_environment plugins
- Added user, group and group_perm plugins

v0.4.3
======

Minor Changes
-------------

- Added meta/runtime.yml file which is now a requirement for collections to be released on Galaxy
- Added requirements_file option to ah_repository module

v0.4.1
======

Bugfixes
--------

- Now retries auto-approving on the publish role in case there is a delay in the collection making it to be ready for approval.

v0.4.0
======

Major Changes
-------------

- Added ah_repository_sync module to sync remote repositories for Automation Hub.

v0.3.1
======

Bugfixes
--------

- Fixes issue in ah_repository where not specifying a requirements list causedd a failure.

v0.3.0
======

Major Changes
-------------

- Added ah_repository module to configure the remote repositories for Automation Hub.

v0.2.0
======

Major Changes
-------------

- Added ah_approval module to approve a colelction which has been uploaded.
- Added ah_collection_uploads module
- Publish role - Ability to approve role added
- Publish role - rewritten to use internal modules

Breaking Changes / Porting Guide
--------------------------------

- Publish role - repo_name variable renamed to collection_name.

v0.1.0
======

Major Changes
-------------

- Initial release of ansible_config, namespace, publish roles and ah_namespace, ah_token modules
