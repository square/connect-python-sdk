# CatalogQuery
> squareconnect.models.catalog_query

### Description

A query to be applied to a [SearchCatalogObjectsRequest](#type-searchcatalogobjectsrequest) request. Only one query field may be present.  Where an attribute name is required, it should be specified as the name of any field marked \"searchable\" from the structured data types for the desired result object type(s) ([CatalogItem](#type-catalogitem), [CatalogItemVariation](#type-catalogitemvariation), [CatalogCategory](#type-catalogcategory), [CatalogTax](#type-catalogtax), [CatalogDiscount](#type-catalogdiscount), [CatalogModifierList](#type-catalogmodifierlist), or [CatalogModifier](#type-catalogmodifier)).  For example, a query that should return Items may specify an attribute names from any of the searchable fields of the [CatalogItem](#type-catalogitem) data type, namely `\"name\"`, `\"description\"`, and `\"abbreviation\"`.

## Properties
Name | Type | Notes
------------ | ------------- | -------------
**sorted_attribute_query** | [**CatalogQuerySortedAttribute**](CatalogQuerySortedAttribute.md) | [optional] 
**exact_query** | [**CatalogQueryExact**](CatalogQueryExact.md) | [optional] 
**prefix_query** | [**CatalogQueryPrefix**](CatalogQueryPrefix.md) | [optional] 
**range_query** | [**CatalogQueryRange**](CatalogQueryRange.md) | [optional] 
**text_query** | [**CatalogQueryText**](CatalogQueryText.md) | [optional] 
**items_for_tax_query** | [**CatalogQueryItemsForTax**](CatalogQueryItemsForTax.md) | [optional] 
**items_for_modifier_list_query** | [**CatalogQueryItemsForModifierList**](CatalogQueryItemsForModifierList.md) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


