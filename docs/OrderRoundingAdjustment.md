# OrderRoundingAdjustment
> squareconnect.models.order_rounding_adjustment

### Description

A rounding adjustment of the money being returned. Commonly used to apply Cash Rounding when the minimum unit of account is smaller than the lowest physical denomination of currency.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uid** | **str** | The rounding adjustment&#39;s Unique identifier, unique only within this order. This field is read-only. | [optional] 
**name** | **str** | The name of the rounding adjustment from the original sale Order. | [optional] 
**amount_money** | [**Money**](Money.md) | Actual rounding adjustment amount. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


