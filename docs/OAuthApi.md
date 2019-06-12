# OAuthApi
> squareconnect.apis.o_auth_api

All endpoints are relative to [Square Connect V2 Documentation](https://docs.connect.squareup.com/api/connect/v2/#navsection-endpoints)


Method | HTTP request 
------------- | -------------
[**obtain_token**](OAuthApi.md#obtain_token) | **POST** /oauth2/token
[**renew_token**](OAuthApi.md#renew_token) | **POST** /oauth2/clients/{client_id}/access-token/renew
[**revoke_token**](OAuthApi.md#revoke_token) | **POST** /oauth2/revoke


# **obtain_token**
> ObtainTokenResponse obtain_token(body)

### Description

Returns an OAuth access token.   The endpoint supports distinct methods of obtaining OAuth access tokens.  Applications specify a method by adding the `grant_type` parameter  in the request and also provide relevant information.  For more information, see [OAuth access token management](/authz/oauth/how-it-works#oauth-access-token-management).   __Note:__ Regardless of the method application specified, the endpoint always returns two items; an OAuth access token and  a refresh token in the response.   __OAuth tokens should only live on secure servers. Application clients should never interact directly with OAuth tokens__.

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **body** | [**ObtainTokenRequest**](ObtainTokenRequest.md)| 

### Return type

[**ObtainTokenResponse**](ObtainTokenResponse.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **renew_token**
> RenewTokenResponse renew_token(client_id, body)

### Description

`RenewToken` is deprecated. For information about refreshing OAuth access tokens, see  [Renew OAuth Token](/authz/oauth/cookbook/oauth-renew).   Renews an OAuth access token before it expires.  OAuth access tokens besides your application's personal access token expire after __30 days__. You can also renew expired tokens within __15 days__ of their expiration. You cannot renew an access token that has been expired for more than 15 days. Instead, the associated user must re-complete the OAuth flow from the beginning.  __Important:__ The `Authorization` header for this endpoint must have the following format:  ``` Authorization: Client APPLICATION_SECRET ```  Replace `APPLICATION_SECRET` with the application secret on the Credentials page in the [application dashboard](https://connect.squareup.com/apps).

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| 
 **body** | [**RenewTokenRequest**](RenewTokenRequest.md)| 

### Return type

[**RenewTokenResponse**](RenewTokenResponse.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_token**
> RevokeTokenResponse revoke_token(body)

### Description

Revokes an access token generated with the OAuth flow.  If an account has more than one OAuth access token for your application, this endpoint revokes all of them, regardless of which token you specify. When an OAuth access token is revoked, all of the active subscriptions associated with that OAuth token are canceled immediately.  __Important:__ The `Authorization` header for this endpoint must have the following format:  ``` Authorization: Client APPLICATION_SECRET ```  Replace `APPLICATION_SECRET` with the application secret on the Credentials page in the [application dashboard](https://connect.squareup.com/apps).

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **body** | [**RevokeTokenRequest**](RevokeTokenRequest.md)| 

### Return type

[**RevokeTokenResponse**](RevokeTokenResponse.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

