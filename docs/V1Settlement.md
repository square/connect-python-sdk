# V1Settlement
> squareconnect.models.v1_settlement

### Description

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The settlement&#39;s unique identifier. | [optional] 
**status** | **str** | The settlement&#39;s current status. | [optional] 
**total_money** | [**V1Money**](V1Money.md) | The amount of money involved in the settlement. A positive amount indicates a deposit, and a negative amount indicates a withdrawal. This amount is never zero. | [optional] 
**initiated_at** | **str** | The time when the settlement was submitted for deposit or withdrawal, in ISO 8601 format. | [optional] 
**bank_account_id** | **str** | The Square-issued unique identifier for the bank account associated with the settlement. | [optional] 
**entries** | [**list[V1SettlementEntry]**](V1SettlementEntry.md) | The entries included in this settlement. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


