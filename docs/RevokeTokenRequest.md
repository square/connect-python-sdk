# RevokeTokenRequest
> squareconnect.models.revoke_token_request

### Description



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** | Your application&#39;s ID, available from the [application dashboard](https://connect.squareup.com/apps). | [optional] 
**access_token** | **str** | The access token of the merchant whose token you want to revoke. Do not provide a value for merchant_id if you provide this parameter. | [optional] 
**merchant_id** | **str** | The ID of the merchant whose token you want to revoke. Do not provide a value for access_token if you provide this parameter. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


