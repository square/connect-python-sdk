# OrderReturnTax
> squareconnect.models.order_return_tax

### Description

The line item tax being returned.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uid** | **str** | Unique ID that identifies the return tax only within this order.  This field is read-only. | [optional] 
**source_tax_uid** | **str** | &#x60;uid&#x60; of the Tax from the Order which contains the original charge of this tax. | [optional] 
**catalog_object_id** | **str** | The catalog object id referencing [CatalogTax](#type-catalogtax). | [optional] 
**name** | **str** | The tax&#39;s name. | [optional] 
**type** | **str** | Indicates the calculation method used to apply the tax. See [OrderLineItemTaxType](#type-orderlineitemtaxtype) for possible values | [optional] 
**percentage** | **str** | The percentage of the tax, as a string representation of a decimal number.  A value of &#x60;7.25&#x60; corresponds to a percentage of 7.25%. | [optional] 
**applied_money** | [**Money**](Money.md) | The amount of the money applied by the tax in an order. | [optional] 
**scope** | **str** | Indicates the level at which the tax applies. This field is set by the server. If set in a CreateOrder request, it will be ignored on write. See [OrderLineItemTaxScope](#type-orderlineitemtaxscope) for possible values | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


