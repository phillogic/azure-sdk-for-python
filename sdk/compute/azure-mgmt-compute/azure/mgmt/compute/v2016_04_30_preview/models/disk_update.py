# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .resource_update import ResourceUpdate


class DiskUpdate(ResourceUpdate):
    """Disk update resource.

    :param tags: Resource tags
    :type tags: dict[str, str]
    :param account_type: the storage account type of the disk. Possible values
     include: 'Standard_LRS', 'Premium_LRS'
    :type account_type: str or
     ~azure.mgmt.compute.v2016_04_30_preview.models.StorageAccountTypes
    :param os_type: the Operating System type. Possible values include:
     'Windows', 'Linux'
    :type os_type: str or
     ~azure.mgmt.compute.v2016_04_30_preview.models.OperatingSystemTypes
    :param creation_data: disk source information. CreationData information
     cannot be changed after the disk has been created.
    :type creation_data:
     ~azure.mgmt.compute.v2016_04_30_preview.models.CreationData
    :param disk_size_gb: If creationData.createOption is Empty, this field is
     mandatory and it indicates the size of the VHD to create. If this field is
     present for updates or creation with other options, it indicates a resize.
     Resizes are only allowed if the disk is not attached to a running VM, and
     can only increase the disk's size.
    :type disk_size_gb: int
    :param encryption_settings: Encryption settings for disk or snapshot
    :type encryption_settings:
     ~azure.mgmt.compute.v2016_04_30_preview.models.EncryptionSettings
    """

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
        'account_type': {'key': 'properties.accountType', 'type': 'StorageAccountTypes'},
        'os_type': {'key': 'properties.osType', 'type': 'OperatingSystemTypes'},
        'creation_data': {'key': 'properties.creationData', 'type': 'CreationData'},
        'disk_size_gb': {'key': 'properties.diskSizeGB', 'type': 'int'},
        'encryption_settings': {'key': 'properties.encryptionSettings', 'type': 'EncryptionSettings'},
    }

    def __init__(self, **kwargs):
        super(DiskUpdate, self).__init__(**kwargs)
        self.account_type = kwargs.get('account_type', None)
        self.os_type = kwargs.get('os_type', None)
        self.creation_data = kwargs.get('creation_data', None)
        self.disk_size_gb = kwargs.get('disk_size_gb', None)
        self.encryption_settings = kwargs.get('encryption_settings', None)