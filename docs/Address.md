# Address
> squareconnect.models.address

### Description

Represents a physical address.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_line_1** | **str** | The first line of the address.  Fields that start with &#x60;address_line&#x60; provide the address&#39;s most specific details, like street number, street name, and building name. They do *not* provide less specific details like city, state/province, or country (these details are provided in other fields). | [optional] 
**address_line_2** | **str** | The second line of the address, if any. | [optional] 
**address_line_3** | **str** | The third line of the address, if any. | [optional] 
**locality** | **str** | The city or town of the address. | [optional] 
**sublocality** | **str** | A civil region within the address&#39;s &#x60;locality&#x60;, if any. | [optional] 
**sublocality_2** | **str** | A civil region within the address&#39;s &#x60;sublocality&#x60;, if any. | [optional] 
**sublocality_3** | **str** | A civil region within the address&#39;s &#x60;sublocality_2&#x60;, if any. | [optional] 
**administrative_district_level_1** | **str** | A civil entity within the address&#39;s country. In the US, this is the state. | [optional] 
**administrative_district_level_2** | **str** | A civil entity within the address&#39;s &#x60;administrative_district_level_1&#x60;. In the US, this is the county. | [optional] 
**administrative_district_level_3** | **str** | A civil entity within the address&#39;s &#x60;administrative_district_level_2&#x60;, if any. | [optional] 
**postal_code** | **str** | The address&#39;s postal code. | [optional] 
**country** | **str** | The address&#39;s country, in ISO 3166-1-alpha-2 format. | [optional] 
**first_name** | **str** | Optional first name when it&#39;s representing recipient. | [optional] 
**last_name** | **str** | Optional last name when it&#39;s representing recipient. | [optional] 
**organization** | **str** | Optional organization name when it&#39;s representing recipient. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


