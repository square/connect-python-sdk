# Error
> squareconnect.models.error

### Description

Represents an error encountered during a request to the Connect API.  See [Handling errors](#handlingerrors) for more information.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** | The error&#39;s high-level category. See [ErrorCategory](#type-errorcategory) for possible values. | 
**code** | **str** | The error&#39;s specific code. See [ErrorCode](#type-errorcode) for possible values | 
**detail** | **str** | A human-readable description of the error for debugging purposes. | [optional] 
**field** | **str** | The name of the field provided in the original request that the error pertains to, if any. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


