# V1Merchant
> squareconnect.models.v1_merchant

### Description

Defines the fields that are included in the response body of a request to the **RetrieveBusiness** endpoint.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The merchant account&#39;s unique identifier. | [optional] 
**name** | **str** | The name associated with the merchant account. | [optional] 
**email** | **str** | The email address associated with the merchant account. | [optional] 
**account_type** | **str** | Indicates whether the merchant account corresponds to a single-location account (LOCATION) or a business account (BUSINESS). This value is almost always LOCATION. | [optional] 
**account_capabilities** | **list[str]** | Capabilities that are enabled for the merchant&#39;s Square account. Capabilities that are not listed in this array are not enabled for the account. | [optional] 
**country_code** | **str** | The country associated with the merchant account, in ISO 3166-1-alpha-2 format. | [optional] 
**language_code** | **str** | The language associated with the merchant account, in BCP 47 format. | [optional] 
**currency_code** | **str** | The currency associated with the merchant account, in ISO 4217 format. For example, the currency code for US dollars is USD. | [optional] 
**business_name** | **str** | The name of the merchant&#39;s business. | [optional] 
**business_address** | [**Address**](Address.md) | The address of the merchant&#39;s business. | [optional] 
**business_phone** | [**V1PhoneNumber**](V1PhoneNumber.md) | The phone number of the merchant&#39;s business. | [optional] 
**business_type** | **str** | The type of business operated by the merchant. | [optional] 
**shipping_address_** | [**Address**](Address.md) | The merchant&#39;s shipping address. | [optional] 
**location_details** | [**V1MerchantLocationDetails**](V1MerchantLocationDetails.md) |  | [optional] 
**market_url** | **str** | The URL of the merchant&#39;s online store. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


