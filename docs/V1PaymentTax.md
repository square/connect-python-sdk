# V1PaymentTax
> squareconnect.models.v1_payment_tax

### Description

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**list[Error]**](Error.md) | Any errors that occurred during the request. | [optional] 
**name** | **str** | The merchant-defined name of the tax. | [optional] 
**applied_money** | [**V1Money**](V1Money.md) | The amount of money that this tax adds to the payment. | [optional] 
**rate** | **str** | The rate of the tax, as a string representation of a decimal number. A value of 0.07 corresponds to a rate of 7%. | [optional] 
**inclusion_type** | **str** | Whether the tax is an ADDITIVE tax or an INCLUSIVE tax. | [optional] 
**fee_id** | **str** | The ID of the tax, if available. Taxes applied in older versions of Square Register might not have an ID. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


