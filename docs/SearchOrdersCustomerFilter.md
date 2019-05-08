# SearchOrdersCustomerFilter
> squareconnect.models.search_orders_customer_filter

### Description

Filter based on Order `customer_id` and any Tender `customer_id` associated with the Order. Does not filter based on the [FulfillmentRecipient](#type-orderfulfillmentrecipient) `customer_id`.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_ids** | **list[str]** | Filter by orders with any of the listed &#x60;customer_id&#x60;s.  Max: 10 &#x60;customer_id&#x60;s. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


