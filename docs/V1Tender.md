# V1Tender
> squareconnect.models.v1_tender

### Description

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The tender&#39;s unique ID. | [optional] 
**type** | **str** | The type of tender. | [optional] 
**name** | **str** | A human-readable description of the tender. | [optional] 
**employee_id** | **str** | The ID of the employee that processed the tender. | [optional] 
**receipt_url** | **str** | The URL of the receipt for the tender. | [optional] 
**card_brand** | **str** | The brand of credit card provided. | [optional] 
**pan_suffix** | **str** | The last four digits of the provided credit card&#39;s account number. | [optional] 
**entry_method** | **str** | The tender&#39;s unique ID. | [optional] 
**payment_note** | **str** | Notes entered by the merchant about the tender at the time of payment, if any. Typically only present for tender with the type: OTHER. | [optional] 
**total_money** | [**V1Money**](V1Money.md) | The total amount of money provided in this form of tender. | [optional] 
**tendered_money** | [**V1Money**](V1Money.md) | The amount of total_money applied to the payment. | [optional] 
**change_back_money** | [**V1Money**](V1Money.md) | The amount of total_money returned to the buyer as change. | [optional] 
**refunded_money** | [**V1Money**](V1Money.md) | The total of all refunds applied to this tender. This amount is always negative or zero. | [optional] 
**is_exchange** | **bool** | Indicates whether or not the tender is associated with an exchange. If is_exchange is true, the tender represents the value of goods returned in an exchange not the actual money paid. The exchange value reduces the tender amounts needed to pay for items purchased in the exchange. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


