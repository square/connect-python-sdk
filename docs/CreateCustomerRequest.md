# CreateCustomerRequest
> squareconnect.models.create_customer_request

### Description

Defines the body parameters that can be provided in a request to the [CreateCustomer](#endpoint-createcustomer) endpoint.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**given_name** | **str** | The customer&#39;s given (i.e., first) name. | [optional] 
**family_name** | **str** | The customer&#39;s family (i.e., last) name. | [optional] 
**company_name** | **str** | The name of the customer&#39;s company. | [optional] 
**nickname** | **str** | A nickname for the customer. | [optional] 
**email_address** | **str** | The customer&#39;s email address. | [optional] 
**address** | [**Address**](Address.md) | The customer&#39;s physical address. | [optional] 
**phone_number** | **str** | The customer&#39;s phone number. | [optional] 
**reference_id** | **str** | An optional second ID you can set to associate the customer with an entity in another system. | [optional] 
**note** | **str** | An optional note to associate with the customer. | [optional] 
**birthday** | **str** | The customer birthday in RFC-3339 format. Year is optional, timezone and times are not allowed. Example: &#x60;0000-09-01T00:00:00-00:00&#x60; for a birthday on September 1st. &#x60;1998-09-01T00:00:00-00:00&#x60; for a birthday on September 1st 1998. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


