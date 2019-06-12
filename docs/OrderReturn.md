# OrderReturn
> squareconnect.models.order_return

### Description

The set of line items, service charges, taxes, discounts, tips, etc. being returned in an Order.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uid** | **str** | Unique ID that identifies the return only within this order.  This field is read-only. | [optional] 
**source_order_id** | **str** | Order which contains the original sale of these returned line items. This will be unset for unlinked returns. | [optional] 
**return_line_items** | [**list[OrderReturnLineItem]**](OrderReturnLineItem.md) | Collection of line items which are being returned. | [optional] 
**return_service_charges** | [**list[OrderReturnServiceCharge]**](OrderReturnServiceCharge.md) | Collection of service charges which are being returned.  This field is read-only. | [optional] 
**return_taxes** | [**list[OrderReturnTax]**](OrderReturnTax.md) | Collection of taxes which are being returned. | [optional] 
**return_discounts** | [**list[OrderReturnDiscount]**](OrderReturnDiscount.md) | Collection of discounts which are being returned. | [optional] 
**rounding_adjustment** | [**OrderRoundingAdjustment**](OrderRoundingAdjustment.md) | A positive or negative rounding adjustment to the total value being returned. Commonly used to apply Cash Rounding when the minimum unit of account is smaller than the lowest physical denomination of currency. | [optional] 
**return_amounts** | [**OrderMoneyAmounts**](OrderMoneyAmounts.md) | Aggregate monetary value being returned by this Return entry. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


