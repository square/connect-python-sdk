# V1Merchant
> squareconnect.models.v1_merchant

### Description

Defines the fields that are included in the response body of a request to the **RetrieveBusiness** endpoint.

## Properties
Name | Type | Notes
------------ | ------------- | -------------
**id** | **str** | [optional] 
**name** | **str** | [optional] 
**email** | **str** | [optional] 
**account_type** | **str** | [optional] 
**account_capabilities** | **list[str]** | [optional] 
**country_code** | **str** | [optional] 
**language_code** | **str** | [optional] 
**currency_code** | **str** | [optional] 
**business_name** | **str** | [optional] 
**business_address** | [**Address**](Address.md) | [optional] 
**business_phone** | [**V1PhoneNumber**](V1PhoneNumber.md) | [optional] 
**business_type** | **str** | [optional] 
**shipping_address_** | [**Address**](Address.md) | [optional] 
**location_details** | [**V1MerchantLocationDetails**](V1MerchantLocationDetails.md) | [optional] 
**market_url** | **str** | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


