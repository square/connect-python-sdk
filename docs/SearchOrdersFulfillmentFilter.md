# SearchOrdersFulfillmentFilter
> squareconnect.models.search_orders_fulfillment_filter

### Description

Filter based on [Order Fulfillment](#type-orderfulfillment) information.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fulfillment_types** | **list[str]** | List of [fulfillment types](#type-orderfulfillmenttype) to filter for. Will return orders if any of its fulfillments match any of the fulfillment types listed in this field. See [OrderFulfillmentType](#type-orderfulfillmenttype) for possible values | 
**fulfillment_states** | **list[str]** | List of [fulfillment states](#type-orderfulfillmentstate) to filter for. Will return orders if any of its fulfillments match any of the fulfillment states listed in this field. See [OrderFulfillmentState](#type-orderfulfillmentstate) for possible values | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


