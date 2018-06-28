# V1Fee
> squareconnect.models.v1_fee

### Description

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The fee&#39;s unique ID. | [optional] 
**name** | **str** | The fee&#39;s name. | [optional] 
**rate** | **str** | The rate of the fee, as a string representation of a decimal number. A value of 0.07 corresponds to a rate of 7%. | [optional] 
**calculation_phase** | **str** | Forthcoming | [optional] 
**adjustment_type** | **str** | The type of adjustment the fee applies to a payment. Currently, this value is TAX for all fees. | [optional] 
**applies_to_custom_amounts** | **bool** | If true, the fee applies to custom amounts entered into Square Register that are not associated with a particular item. | [optional] 
**enabled** | **bool** | If true, the fee is applied to all appropriate items. If false, the fee is not applied at all. | [optional] 
**inclusion_type** | **str** | Whether the fee is ADDITIVE or INCLUSIVE. | [optional] 
**type** | **str** | In countries with multiple classifications for sales taxes, indicates which classification the fee falls under. Currently relevant only to Canadian merchants. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


