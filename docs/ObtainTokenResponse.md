# ObtainTokenResponse
> squareconnect.models.obtain_token_response

### Description



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | A valid OAuth access token. OAuth access tokens are 64 bytes long. Provide the access token in a header with every request to Connect API endpoints. See the [Build with OAuth](/authz/oauth/build-with-the-api) guide for more information. | [optional] 
**token_type** | **str** | This value is always _bearer_. | [optional] 
**expires_at** | **str** | The date when access_token expires, in [ISO 8601](http://www.iso.org/iso/home/standards/iso8601.htm) format. | [optional] 
**merchant_id** | **str** | The ID of the authorizing merchant&#39;s business. | [optional] 
**subscription_id** | **str** | __LEGACY FIELD__. The ID of a subscription plan the merchant signed up for. Only present if the merchant signed up for a subscription during authorization. | [optional] 
**plan_id** | **str** | __LEGACY FIELD__. The ID of the subscription plan the merchant signed up for. Only present if the merchant signed up for a subscription during authorization. | [optional] 
**id_token** | **str** | Then OpenID token belonging to this this person. Only present if the OPENID scope is included in the authorize request. | [optional] 
**refresh_token** | **str** | A refresh token. For more information, see [OAuth access token management](/authz/oauth/how-it-works#oauth-access-token-management). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


