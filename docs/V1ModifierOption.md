# V1ModifierOption
> squareconnect.models.v1_modifier_option

### Description

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The modifier option&#39;s unique ID. | [optional] 
**name** | **str** | The modifier option&#39;s name. | [optional] 
**price_money** | [**V1Money**](V1Money.md) | The modifier option&#39;s price. | [optional] 
**on_by_default** | **bool** | If true, the modifier option is the default option in a modifier list for which selection_type is SINGLE. | [optional] 
**ordinal** | **int** | Indicates the modifier option&#39;s list position when displayed in Square Register and the merchant dashboard. If more than one modifier option in the same modifier list has the same ordinal value, those options are displayed in alphabetical order. | [optional] 
**modifier_list_id** | **str** | The ID of the modifier list the option belongs to. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


