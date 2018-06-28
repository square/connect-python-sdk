# Customer
> squareconnect.models.customer

### Description

Represents one of a business's customers, which can have one or more cards on file associated with it.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The customer&#39;s unique ID. | 
**created_at** | **str** | The time when the customer was created, in RFC 3339 format. | 
**updated_at** | **str** | The time when the customer was last updated, in RFC 3339 format. | 
**cards** | [**list[Card]**](Card.md) | The non-confidential details of the customer&#39;s cards on file. | [optional] 
**given_name** | **str** | The customer&#39;s given (i.e., first) name. | [optional] 
**family_name** | **str** | The customer&#39;s family (i.e., last) name. | [optional] 
**nickname** | **str** | The customer&#39;s nickname. | [optional] 
**company_name** | **str** | The name of the customer&#39;s company. | [optional] 
**email_address** | **str** | The customer&#39;s email address. | [optional] 
**address** | [**Address**](Address.md) | The customer&#39;s physical address. | [optional] 
**phone_number** | **str** | The customer&#39;s phone number. | [optional] 
**reference_id** | **str** | A second ID you can set to associate the customer with an entity in another system. | [optional] 
**note** | **str** | A note to associate with the customer. | [optional] 
**preferences** | [**CustomerPreferences**](CustomerPreferences.md) | The customer&#39;s preferences. | [optional] 
**groups** | [**list[CustomerGroupInfo]**](CustomerGroupInfo.md) | The groups the customer belongs to. | [optional] 
**creation_source** | **str** | A creation source represents the method used to create the customer profile. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


