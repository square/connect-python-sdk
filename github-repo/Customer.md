# Customer
> squareconnect.models.customer

### Description

Represents one of a business's customers, which can have one or more cards on file associated with it.

## Properties
Name | Type | Notes
------------ | ------------- | -------------
**id** | **str** | 
**created_at** | **str** | 
**updated_at** | **str** | 
**cards** | [**list[Card]**](Card.md) | [optional] 
**given_name** | **str** | [optional] 
**family_name** | **str** | [optional] 
**nickname** | **str** | [optional] 
**company_name** | **str** | [optional] 
**email_address** | **str** | [optional] 
**address** | [**Address**](Address.md) | [optional] 
**phone_number** | **str** | [optional] 
**reference_id** | **str** | [optional] 
**note** | **str** | [optional] 
**preferences** | [**CustomerPreferences**](CustomerPreferences.md) | [optional] 
**groups** | [**list[CustomerGroupInfo]**](CustomerGroupInfo.md) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


