# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Generic, Optional, TypeVar, Union
import warnings

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.core.polling import AsyncNoPolling, AsyncPollingMethod, async_poller
from azure.mgmt.core.polling.async_arm_polling import AsyncARMPolling

from ... import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class PrivateEndpointConnectionsOperations:
    """PrivateEndpointConnectionsOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.appconfiguration.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def list_by_configuration_store(
        self,
        resource_group_name: str,
        config_store_name: str,
        **kwargs
    ) -> "models.PrivateEndpointConnectionListResult":
        """Lists all private endpoint connections for a configuration store.

        :param resource_group_name: The name of the resource group to which the container registry
     belongs.
        :type resource_group_name: str
        :param config_store_name: The name of the configuration store.
        :type config_store_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PrivateEndpointConnectionListResult or the result of cls(response)
        :rtype: ~azure.mgmt.appconfiguration.models.PrivateEndpointConnectionListResult
        :raises: ~azure.mgmt.appconfiguration.models.ErrorException:
        """
        cls: ClsType["models.PrivateEndpointConnectionListResult"] = kwargs.pop('cls', None)
        error_map = kwargs.pop('error_map', {})
        api_version = "2019-11-01-preview"

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list_by_configuration_store.metadata['url']
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
                    'configStoreName': self._serialize.url("config_store_name", config_store_name, 'str', max_length=50, min_length=5, pattern=r'^[a-zA-Z0-9_-]*$'),
                }
                url = self._client.format_url(url, **path_format_arguments)
            else:
                url = next_link

            # Construct parameters
            query_parameters: Dict[str, Any] = {}
            query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

            # Construct headers
            header_parameters: Dict[str, Any] = {}
            header_parameters['Accept'] = 'application/json'

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize('PrivateEndpointConnectionListResult', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise models.ErrorException.from_response(response, self._deserialize)

            return pipeline_response

        return AsyncItemPaged(
            get_next, extract_data
        )
    list_by_configuration_store.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AppConfiguration/configurationStores/{configStoreName}/privateEndpointConnections'}

    async def get(
        self,
        resource_group_name: str,
        config_store_name: str,
        private_endpoint_connection_name: str,
        **kwargs
    ) -> "models.PrivateEndpointConnection":
        """Gets the specified private endpoint connection associated with the configuration store.

        :param resource_group_name: The name of the resource group to which the container registry
         belongs.
        :type resource_group_name: str
        :param config_store_name: The name of the configuration store.
        :type config_store_name: str
        :param private_endpoint_connection_name: Private endpoint connection name.
        :type private_endpoint_connection_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PrivateEndpointConnection or the result of cls(response)
        :rtype: ~azure.mgmt.appconfiguration.models.PrivateEndpointConnection
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls: ClsType["models.PrivateEndpointConnection"] = kwargs.pop('cls', None)
        error_map = kwargs.pop('error_map', {})
        api_version = "2019-11-01-preview"

        # Construct URL
        url = self.get.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'configStoreName': self._serialize.url("config_store_name", config_store_name, 'str', max_length=50, min_length=5, pattern=r'^[a-zA-Z0-9_-]*$'),
            'privateEndpointConnectionName': self._serialize.url("private_endpoint_connection_name", private_endpoint_connection_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters: Dict[str, Any] = {}
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters: Dict[str, Any] = {}
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        deserialized = self._deserialize('PrivateEndpointConnection', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AppConfiguration/configurationStores/{configStoreName}/privateEndpointConnections/{privateEndpointConnectionName}'}

    async def _create_or_update_initial(
        self,
        resource_group_name: str,
        config_store_name: str,
        private_endpoint_connection_name: str,
        private_endpoint: Optional["models.PrivateEndpoint"] = None,
        private_link_service_connection_state: Optional["models.PrivateLinkServiceConnectionState"] = None,
        **kwargs
    ) -> "models.PrivateEndpointConnection":
        cls: ClsType["models.PrivateEndpointConnection"] = kwargs.pop('cls', None)
        error_map = kwargs.pop('error_map', {})

        _private_endpoint_connection = models.PrivateEndpointConnection(private_endpoint=private_endpoint, private_link_service_connection_state=private_link_service_connection_state)
        api_version = "2019-11-01-preview"

        # Construct URL
        url = self._create_or_update_initial.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'configStoreName': self._serialize.url("config_store_name", config_store_name, 'str', max_length=50, min_length=5, pattern=r'^[a-zA-Z0-9_-]*$'),
            'privateEndpointConnectionName': self._serialize.url("private_endpoint_connection_name", private_endpoint_connection_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters: Dict[str, Any] = {}
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters: Dict[str, Any] = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json'

        # Construct body
        body_content = self._serialize.body(_private_endpoint_connection, 'PrivateEndpointConnection')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('PrivateEndpointConnection', pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize('PrivateEndpointConnection', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    _create_or_update_initial.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AppConfiguration/configurationStores/{configStoreName}/privateEndpointConnections/{privateEndpointConnectionName}'}

    async def create_or_update(
        self,
        resource_group_name: str,
        config_store_name: str,
        private_endpoint_connection_name: str,
        private_endpoint: Optional["models.PrivateEndpoint"] = None,
        private_link_service_connection_state: Optional["models.PrivateLinkServiceConnectionState"] = None,
        **kwargs
    ) -> "models.PrivateEndpointConnection":
        """Update the state of the specified private endpoint connection associated with the configuration store.

        :param resource_group_name: The name of the resource group to which the container registry
     belongs.
        :type resource_group_name: str
        :param config_store_name: The name of the configuration store.
        :type config_store_name: str
        :param private_endpoint_connection_name: Private endpoint connection name.
        :type private_endpoint_connection_name: str
        :param private_endpoint: Private endpoint which a connection belongs to.
        :type private_endpoint: ~azure.mgmt.appconfiguration.models.PrivateEndpoint
        :param private_link_service_connection_state: The state of a private link service connection.
        :type private_link_service_connection_state: ~azure.mgmt.appconfiguration.models.PrivateLinkServiceConnectionState
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :return: An instance of LROPoller that returns PrivateEndpointConnection
        :rtype: ~azure.core.polling.LROPoller[~azure.mgmt.appconfiguration.models.PrivateEndpointConnection]

        :raises ~azure.mgmt.appconfiguration.models.ErrorException:
        """
        polling: Union[bool, AsyncPollingMethod] = kwargs.pop('polling', True)
        cls: ClsType["models.PrivateEndpointConnection"] = kwargs.pop('cls', None)
        raw_result = await self._create_or_update_initial(
            resource_group_name=resource_group_name,
            config_store_name=config_store_name,
            private_endpoint_connection_name=private_endpoint_connection_name,
            private_endpoint=private_endpoint,
            private_link_service_connection_state=private_link_service_connection_state,
            cls=lambda x,y,z: x,
            **kwargs
        )

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize('PrivateEndpointConnection', pipeline_response)

            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized

        lro_delay = kwargs.get(
            'polling_interval',
            self._config.polling_interval
        )
        if polling is True: polling_method = AsyncARMPolling(lro_delay,  **kwargs)
        elif polling is False: polling_method = AsyncNoPolling()
        else: polling_method = polling
        return await async_poller(self._client, raw_result, get_long_running_output, polling_method)
    create_or_update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AppConfiguration/configurationStores/{configStoreName}/privateEndpointConnections/{privateEndpointConnectionName}'}

    async def _delete_initial(
        self,
        resource_group_name: str,
        config_store_name: str,
        private_endpoint_connection_name: str,
        **kwargs
    ) -> None:
        cls: ClsType[None] = kwargs.pop('cls', None)
        error_map = kwargs.pop('error_map', {})
        api_version = "2019-11-01-preview"

        # Construct URL
        url = self._delete_initial.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'configStoreName': self._serialize.url("config_store_name", config_store_name, 'str', max_length=50, min_length=5, pattern=r'^[a-zA-Z0-9_-]*$'),
            'privateEndpointConnectionName': self._serialize.url("private_endpoint_connection_name", private_endpoint_connection_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters: Dict[str, Any] = {}
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters: Dict[str, Any] = {}

        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 202, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(pipeline_response, None, {})

    _delete_initial.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AppConfiguration/configurationStores/{configStoreName}/privateEndpointConnections/{privateEndpointConnectionName}'}

    async def delete(
        self,
        resource_group_name: str,
        config_store_name: str,
        private_endpoint_connection_name: str,
        **kwargs
    ) -> None:
        """Deletes a private endpoint connection.

        :param resource_group_name: The name of the resource group to which the container registry
     belongs.
        :type resource_group_name: str
        :param config_store_name: The name of the configuration store.
        :type config_store_name: str
        :param private_endpoint_connection_name: Private endpoint connection name.
        :type private_endpoint_connection_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]

        :raises ~azure.mgmt.appconfiguration.models.ErrorException:
        """
        polling: Union[bool, AsyncPollingMethod] = kwargs.pop('polling', True)
        cls: ClsType[None] = kwargs.pop('cls', None)
        raw_result = await self._delete_initial(
            resource_group_name=resource_group_name,
            config_store_name=config_store_name,
            private_endpoint_connection_name=private_endpoint_connection_name,
            cls=lambda x,y,z: x,
            **kwargs
        )

        def get_long_running_output(pipeline_response):
            if cls:
                return cls(pipeline_response, None, {})

        lro_delay = kwargs.get(
            'polling_interval',
            self._config.polling_interval
        )
        if polling is True: polling_method = AsyncARMPolling(lro_delay,  **kwargs)
        elif polling is False: polling_method = AsyncNoPolling()
        else: polling_method = polling
        return await async_poller(self._client, raw_result, get_long_running_output, polling_method)
    delete.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AppConfiguration/configurationStores/{configStoreName}/privateEndpointConnections/{privateEndpointConnectionName}'}
