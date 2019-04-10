# V1ModifierList
> squareconnect.models.v1_modifier_list

### Description

V1ModifierList

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The modifier list&#39;s unique ID. | [optional] 
**name** | **str** | The modifier list&#39;s name. | [optional] 
**selection_type** | **str** | Indicates whether MULTIPLE options or a SINGLE option from the modifier list can be applied to a single item. See [V1ModifierListSelectionType](#type-v1modifierlistselectiontype) for possible values | [optional] 
**modifier_options** | [**list[V1ModifierOption]**](V1ModifierOption.md) | The options included in the modifier list. | [optional] 
**v2_id** | **str** | The ID of the CatalogObject in the Connect v2 API. Objects that are shared across multiple locations share the same v2 ID. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


