# Transaction
> squareconnect.models.transaction

### Description

Represents a transaction processed with Square, either with the Connect API or with Square Register.  The `tenders` field of this object lists all methods of payment used to pay in the transaction.

## Properties
Name | Type | Notes
------------ | ------------- | -------------
**id** | **str** | [optional] 
**location_id** | **str** | [optional] 
**created_at** | **str** | [optional] 
**tenders** | [**list[Tender]**](Tender.md) | [optional] 
**refunds** | [**list[Refund]**](Refund.md) | [optional] 
**reference_id** | **str** | [optional] 
**product** | **str** | [optional] 
**client_id** | **str** | [optional] 
**order** | [**Order**](Order.md) | [optional] 
**shipping_address** | [**Address**](Address.md) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


