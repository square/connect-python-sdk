# ListCatalogResponse
> squareconnect.models.list_catalog_response

### Description



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**list[Error]**](Error.md) | The set of [Error](#type-error)s encountered. | [optional] 
**cursor** | **str** | The pagination cursor to be used in a subsequent request. If unset, this is the final response. See [Paginating results](#paginatingresults) for more information. | [optional] 
**objects** | [**list[CatalogObject]**](CatalogObject.md) | The [CatalogObject](#type-catalogobject)s returned. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


