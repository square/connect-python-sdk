# V1PaymentItemization
> squareconnect.models.v1_payment_itemization

### Description

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The item&#39;s name. | [optional] 
**quantity** | **float** | The quantity of the item purchased. This can be a decimal value. | [optional] 
**itemization_type** | **str** | The type of purchase that the itemization represents, such as an ITEM or CUSTOM_AMOUNT | [optional] 
**item_detail** | [**V1PaymentItemDetail**](V1PaymentItemDetail.md) | Details of the item, including its unique identifier and the identifier of the item variation purchased. | [optional] 
**notes** | **str** | Notes entered by the merchant about the item at the time of payment, if any. | [optional] 
**item_variation_name** | **str** | The name of the item variation purchased, if any. | [optional] 
**total_money** | [**V1Money**](V1Money.md) | The total cost of the item, including all taxes and discounts. | [optional] 
**single_quantity_money** | [**V1Money**](V1Money.md) | The cost of a single unit of this item. | [optional] 
**gross_sales_money** | [**V1Money**](V1Money.md) | The total cost of the itemization and its modifiers, not including taxes or discounts. | [optional] 
**discount_money** | [**V1Money**](V1Money.md) | The total of all discounts applied to the itemization. This value is always negative or zero. | [optional] 
**net_sales_money** | [**V1Money**](V1Money.md) | The sum of gross_sales_money and discount_money. | [optional] 
**taxes** | [**list[V1PaymentTax]**](V1PaymentTax.md) | All taxes applied to this itemization. | [optional] 
**discounts** | [**list[V1PaymentDiscount]**](V1PaymentDiscount.md) | All discounts applied to this itemization. | [optional] 
**modifiers** | [**list[V1PaymentModifier]**](V1PaymentModifier.md) | All modifier options applied to this itemization. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


