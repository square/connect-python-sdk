# Tender
> squareconnect.models.tender

### Description

Represents a tender (i.e., a method of payment) used in a Square transaction.

## Properties
Name | Type | Notes
------------ | ------------- | -------------
**id** | **str** | [optional] 
**location_id** | **str** | [optional] 
**transaction_id** | **str** | [optional] 
**created_at** | **str** | [optional] 
**note** | **str** | [optional] 
**amount_money** | [**Money**](Money.md) | [optional] 
**processing_fee_money** | [**Money**](Money.md) | [optional] 
**customer_id** | **str** | [optional] 
**type** | **str** | 
**card_details** | [**TenderCardDetails**](TenderCardDetails.md) | [optional] 
**cash_details** | [**TenderCashDetails**](TenderCashDetails.md) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


