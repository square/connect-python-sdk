# Tender
> squareconnect.models.tender

### Description

Represents a tender (i.e., a method of payment) used in a Square transaction.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The tender&#39;s unique ID. | [optional] 
**location_id** | **str** | The ID of the transaction&#39;s associated location. | [optional] 
**transaction_id** | **str** | The ID of the tender&#39;s associated transaction. | [optional] 
**created_at** | **str** | The time when the tender was created, in RFC 3339 format. | [optional] 
**note** | **str** | An optional note associated with the tender at the time of payment. | [optional] 
**amount_money** | [**Money**](Money.md) | The amount of the tender. | [optional] 
**tip_money** | [**Money**](Money.md) | The tip&#39;s amount of the tender. | [optional] 
**processing_fee_money** | [**Money**](Money.md) | The amount of any Square processing fees applied to the tender.  This field is not immediately populated when a new transaction is created. It is usually available after about ten seconds. | [optional] 
**customer_id** | **str** | If the tender is associated with a customer or represents a customer&#39;s card on file, this is the ID of the associated customer. | [optional] 
**type** | **str** | The type of tender, such as &#x60;CARD&#x60; or &#x60;CASH&#x60;. | 
**card_details** | [**TenderCardDetails**](TenderCardDetails.md) | The details of the card tender.  This value is present only if the value of &#x60;type&#x60; is &#x60;CARD&#x60;. | [optional] 
**cash_details** | [**TenderCashDetails**](TenderCashDetails.md) | The details of the cash tender.  This value is present only if the value of &#x60;type&#x60; is &#x60;CASH&#x60;. | [optional] 
**additional_recipients** | [**list[AdditionalRecipient]**](AdditionalRecipient.md) | Additional recipients (other than the merchant) receiving a portion of this tender. For example, fees assessed on the purchase by a third party integration. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


