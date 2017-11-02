# CatalogObject
> squareconnect.models.catalog_object

### Description

The wrapper object for object types in the Catalog data model. The type of a particular `CatalogObject` is determined by the value of `type` and only the corresponding data field may be set.  - if type = `ITEM`, only `item_data` will be populated and it will contain a valid [CatalogItem](#type-catalogitem) object. - if type = `ITEM_VARIATION`, only `item_variation_data` will be populated and it will contain a valid [CatalogItemVariation](#type-catalogitemvariation) object. - if type = `MODIFIER`, only `modifier_data` will be populated and it will contain a valid [CatalogModifier](#type-catalogmodifier) object. - if type = `MODIFIER_LIST`, only `modifier_list_data` will be populated and it will contain a valid [CatalogModifierList](#type-catalogmodifierlist) object. - if type = `CATEGORY`, only `category_data` will be populated and it will contain a valid [CatalogCategory](#type-catalogcategory) object. - if type = `DISCOUNT`, only `discount_data` will be populated and it will contain a valid [CatalogDiscount](#type-catalogdiscount) object. - if type = `TAX`, only `tax_data` will be populated and it will contain a valid [CatalogTax](#type-catalogtax) object.  For a more detailed discussion of the Catalog data model, please see the [Catalog Overview](https://docs.connect.squareup.com/articles/catalog-overview).

## Properties
Name | Type | Notes
------------ | ------------- | -------------
**type** | **str** | 
**id** | **str** | 
**updated_at** | **str** | [optional] 
**version** | **int** | [optional] 
**is_deleted** | **bool** | [optional] 
**catalog_v1_ids** | [**list[CatalogV1Id]**](CatalogV1Id.md) | [optional] 
**present_at_all_locations** | **bool** | [optional] 
**present_at_location_ids** | **list[str]** | [optional] 
**absent_at_location_ids** | **list[str]** | [optional] 
**item_data** | [**CatalogItem**](CatalogItem.md) | [optional] 
**category_data** | [**CatalogCategory**](CatalogCategory.md) | [optional] 
**item_variation_data** | [**CatalogItemVariation**](CatalogItemVariation.md) | [optional] 
**tax_data** | [**CatalogTax**](CatalogTax.md) | [optional] 
**discount_data** | [**CatalogDiscount**](CatalogDiscount.md) | [optional] 
**modifier_list_data** | [**CatalogModifierList**](CatalogModifierList.md) | [optional] 
**modifier_data** | [**CatalogModifier**](CatalogModifier.md) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


