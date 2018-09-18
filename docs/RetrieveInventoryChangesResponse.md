# RetrieveInventoryChangesResponse
> squareconnect.models.retrieve_inventory_changes_response

### Description



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**list[Error]**](Error.md) | Any errors that occurred during the request. | [optional] 
**changes** | [**list[InventoryChange]**](InventoryChange.md) | The set of inventory changes for the requested object and locations. | [optional] 
**cursor** | **str** | The pagination cursor to be used in a subsequent request. If unset, this is the final response.  See [Paginating results](#paginatingresults) for more information. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


