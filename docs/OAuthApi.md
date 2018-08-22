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

Exchanges the authorization code for an access token.  After a merchant authorizes your application with the permissions form, an authorization code is sent to the application's redirect URL (See [Implementing OAuth](https://docs.connect.squareup.com/api/oauth#implementingoauth) for information about how to set up the redirect URL).

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

Renews an OAuth access token before it expires.  OAuth access tokens besides your application's personal access token expire after __30 days__. You can also renew expired tokens within __15 days__ of their expiration. You cannot renew an access token that has been expired for more than 15 days. Instead, the associated merchant must complete the [OAuth flow](https://docs.connect.squareup.com/api/oauth#implementingoauth) from the beginning.  __Important:__ The `Authorization` header you provide to this endpoint must have the following format:  ``` Authorization: Client APPLICATION_SECRET ```  Replace `APPLICATION_SECRET` with your application's secret, available from the [application dashboard](https://connect.squareup.com/apps).

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

Revokes an access token generated with the OAuth flow.  If a merchant has more than one access token for your application, this endpoint revokes all of them, regardless of which token you specify. If you revoke a merchant's access token, all of the merchant's active subscriptions associated with your application are canceled immediately.  __Important:__ The `Authorization` header you provide to this endpoint must have the following format:  ``` Authorization: Client APPLICATION_SECRET ```  Replace `APPLICATION_SECRET` with your application's secret, available from the [application dashboard](https://connect.squareup.com/apps).

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **body** | [**RevokeTokenRequest**](RevokeTokenRequest.md)| 

### Return type

[**RevokeTokenResponse**](RevokeTokenResponse.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

