# V1Item
> squareconnect.models.v1_item

### Description

V1Item

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The item&#39;s ID. Must be unique among all entity IDs ever provided on behalf of the merchant. You can never reuse an ID. This value can include alphanumeric characters, dashes (-), and underscores (_). | [optional] 
**name** | **str** | The item&#39;s name. | [optional] 
**description** | **str** | The item&#39;s description. | [optional] 
**type** | **str** | The item&#39;s type. This value is NORMAL for almost all items. See [V1ItemType](#type-v1itemtype) for possible values | [optional] 
**color** | **str** | The color of the discount&#39;s display label in Square Register, if not the default color. The default color is 9da2a6. See [V1ItemColor](#type-v1itemcolor) for possible values | [optional] 
**abbreviation** | **str** | The text of the item&#39;s display label in Square Register. Only up to the first five characters of the string are used. | [optional] 
**visibility** | **str** | Indicates whether the item is viewable from the merchant&#39;s online store (PUBLIC) or PRIVATE. See [V1ItemVisibility](#type-v1itemvisibility) for possible values | [optional] 
**available_online** | **bool** | If true, the item can be added to shipping orders from the merchant&#39;s online store. | [optional] 
**master_image** | [**V1ItemImage**](V1ItemImage.md) | The item&#39;s master image, if any. | [optional] 
**category** | [**V1Category**](V1Category.md) | The category the item belongs to, if any. | [optional] 
**variations** | [**list[V1Variation]**](V1Variation.md) | The item&#39;s variations. You must specify at least one variation. | [optional] 
**modifier_lists** | [**list[V1ModifierList]**](V1ModifierList.md) | The modifier lists that apply to the item, if any. | [optional] 
**fees** | [**list[V1Fee]**](V1Fee.md) | The fees that apply to the item, if any. | [optional] 
**taxable** | **bool** | Deprecated. This field is not used. | [optional] 
**category_id** | **str** | The ID of the item&#39;s category, if any. | [optional] 
**available_for_pickup** | **bool** | If true, the item can be added to pickup orders from the merchant&#39;s online store. Default value: false | [optional] 
**v2_id** | **str** | The ID of the CatalogObject in the Connect v2 API. Objects that are shared across multiple locations share the same v2 ID. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


