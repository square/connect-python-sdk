# CreateCheckoutRequest
> squareconnect.models.create_checkout_request

### Description

Defines the parameters that can be included in the body of a request to the [CreateCheckout](#endpoint-createcheckout) endpoint.

## Properties
Name | Type | Notes
------------ | ------------- | -------------
**idempotency_key** | **str** | 
**order** | [**CreateOrderRequestOrder**](CreateOrderRequestOrder.md) | 
**ask_for_shipping_address** | **bool** | [optional] 
**merchant_support_email** | **str** | [optional] 
**pre_populate_buyer_email** | **str** | [optional] 
**pre_populate_shipping_address** | [**Address**](Address.md) | [optional] 
**redirect_url** | **str** | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


