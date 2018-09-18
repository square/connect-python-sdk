# BatchRetrieveInventoryCountsRequest
> squareconnect.models.batch_retrieve_inventory_counts_request

### Description



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**catalog_object_ids** | **list[str]** | Filters results by [CatalogObject](#type-catalogobject) ID. Only applied when set. Default: unset. | [optional] 
**location_ids** | **list[str]** | Filters results by [Location](#type-location) ID. Only applied when set. Default: unset. | [optional] 
**updated_after** | **str** | Provided as an RFC 3339 timestamp. Returns results whose &#x60;calculated_at&#x60; value is after the given time. Default: UNIX epoch (&#x60;1970-01-01T00:00:00Z&#x60;). | [optional] 
**cursor** | **str** | A pagination cursor returned by a previous call to this endpoint. Provide this to retrieve the next set of results for the original query.  See [Paginating results](#paginatingresults) for more information. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


