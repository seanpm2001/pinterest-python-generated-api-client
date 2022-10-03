# pinterest.generated.client
Pinterest's REST API

The `pinterest.generated.client` package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 5.5.0
- Package version: 0.1.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://developers.pinterest.com/](https://developers.pinterest.com/)

## Requirements.

Python >=3.6

## Installation & Usage

This python library package is generated without supporting files like setup.py or requirements files

To be able to use it, you will need these dependencies in your own package that uses this library:

* urllib3 >= 1.25.3
* python-dateutil

## Getting Started

In your own code, to use this library to connect and interact with pinterest.generated.client,
you can run the following:

```python

import time
import pinterest.generated.client
from pprint import pprint
from pinterest.generated.client.api import campaigns_api
from pinterest.generated.client.model.campaign_create_request import CampaignCreateRequest
from pinterest.generated.client.model.campaign_create_response import CampaignCreateResponse
from pinterest.generated.client.model.campaign_response import CampaignResponse
from pinterest.generated.client.model.campaign_update_request import CampaignUpdateRequest
from pinterest.generated.client.model.campaign_update_response import CampaignUpdateResponse
from pinterest.generated.client.model.error import Error
from pinterest.generated.client.model.paginated import Paginated
# Defining the host is optional and defaults to https://api.pinterest.com/v5
# See configuration.py for a list of all supported configuration parameters.
configuration = pinterest.generated.client.Configuration(
    host = "https://api.pinterest.com/v5"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: pinterest_oauth2
configuration = pinterest.generated.client.Configuration(
    host = "https://api.pinterest.com/v5"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


# Enter a context with an instance of the API client
with pinterest.generated.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaigns_api.CampaignsApi(api_client)
    ad_account_id = "4" # str | Unique identifier of an ad account.
campaign_create_request = [
        CampaignCreateRequest(),
    ] # [CampaignCreateRequest] | Array of campaigns.

    try:
        # Create campaigns
        api_response = api_instance.campaigns_create(ad_account_id, campaign_create_request)
        pprint(api_response)
    except pinterest.generated.client.ApiException as e:
        print("Exception when calling CampaignsApi->campaigns_create: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://api.pinterest.com/v5*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*CampaignsApi* | [**campaigns_create**](pinterest/generated/client/docs/CampaignsApi.md#campaigns_create) | **POST** /ad_accounts/{ad_account_id}/campaigns | Create campaigns
*CampaignsApi* | [**campaigns_get**](pinterest/generated/client/docs/CampaignsApi.md#campaigns_get) | **GET** /ad_accounts/{ad_account_id}/campaigns/{campaign_id} | Get campaign
*CampaignsApi* | [**campaigns_list**](pinterest/generated/client/docs/CampaignsApi.md#campaigns_list) | **GET** /ad_accounts/{ad_account_id}/campaigns | List campaigns
*CampaignsApi* | [**campaigns_update**](pinterest/generated/client/docs/CampaignsApi.md#campaigns_update) | **PATCH** /ad_accounts/{ad_account_id}/campaigns | Update campaigns
*OauthApi* | [**oauth_token**](pinterest/generated/client/docs/OauthApi.md#oauth_token) | **POST** /oauth/token | Generate OAuth access token


## Documentation For Models

 - [CampaignCommon](pinterest/generated/client/docs/CampaignCommon.md)
 - [CampaignCreateCommon](pinterest/generated/client/docs/CampaignCreateCommon.md)
 - [CampaignCreateCommonAllOf](pinterest/generated/client/docs/CampaignCreateCommonAllOf.md)
 - [CampaignCreateRequest](pinterest/generated/client/docs/CampaignCreateRequest.md)
 - [CampaignCreateRequestAllOf](pinterest/generated/client/docs/CampaignCreateRequestAllOf.md)
 - [CampaignCreateResponse](pinterest/generated/client/docs/CampaignCreateResponse.md)
 - [CampaignCreateResponseData](pinterest/generated/client/docs/CampaignCreateResponseData.md)
 - [CampaignCreateResponseDataAllOf](pinterest/generated/client/docs/CampaignCreateResponseDataAllOf.md)
 - [CampaignCreateResponseItem](pinterest/generated/client/docs/CampaignCreateResponseItem.md)
 - [CampaignId](pinterest/generated/client/docs/CampaignId.md)
 - [CampaignResponse](pinterest/generated/client/docs/CampaignResponse.md)
 - [CampaignResponseAllOf](pinterest/generated/client/docs/CampaignResponseAllOf.md)
 - [CampaignUpdateRequest](pinterest/generated/client/docs/CampaignUpdateRequest.md)
 - [CampaignUpdateRequestAllOf](pinterest/generated/client/docs/CampaignUpdateRequestAllOf.md)
 - [CampaignUpdateResponse](pinterest/generated/client/docs/CampaignUpdateResponse.md)
 - [EntityStatus](pinterest/generated/client/docs/EntityStatus.md)
 - [Error](pinterest/generated/client/docs/Error.md)
 - [Exception](pinterest/generated/client/docs/Exception.md)
 - [OauthAccessTokenResponse](pinterest/generated/client/docs/OauthAccessTokenResponse.md)
 - [OauthAccessTokenResponseCode](pinterest/generated/client/docs/OauthAccessTokenResponseCode.md)
 - [OauthAccessTokenResponseCodeAllOf](pinterest/generated/client/docs/OauthAccessTokenResponseCodeAllOf.md)
 - [OauthAccessTokenResponseRefresh](pinterest/generated/client/docs/OauthAccessTokenResponseRefresh.md)
 - [ObjectiveType](pinterest/generated/client/docs/ObjectiveType.md)
 - [Paginated](pinterest/generated/client/docs/Paginated.md)
 - [TrackingUrls](pinterest/generated/client/docs/TrackingUrls.md)


## Documentation For Authorization


## basic

- **Type**: HTTP basic authentication


## pinterest_oauth2

- **Type**: OAuth
- **Flow**: accessCode
- **Authorization URL**: https://www.pinterest.com/oauth/
- **Scopes**: 
 - **ads:read**: See all of your advertising data, including ads, ad groups, campaigns etc.
 - **ads:write**: Create, update, or delete ads, ad groups, campaigns etc.
 - **boards:read**: See your public boards, including group boards you join
 - **boards:read_secret**: See your secret boards
 - **boards:write**: Create, update, or delete your public boards
 - **boards:write_secret**: Create, update, or delete your secret boards
 - **catalogs:read**: See all of your catalogs data
 - **catalogs:write**: Create, update, or delete your catalogs data
 - **pins:read**: See your public Pins
 - **pins:read_secret**: See your secret Pins
 - **pins:write**: Create, update, or delete your public Pins
 - **pins:write_secret**: Create, update, or delete your secret Pins
 - **user_accounts:read**: See your user accounts


## Author

pinterest-api@pinterest.com


## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in pinterest.generated.client.apis and pinterest.generated.client.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from pinterest.generated.client.api.default_api import DefaultApi`
- `from pinterest.generated.client.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import pinterest.generated.client
from pinterest.generated.client.apis import *
from pinterest.generated.client.models import *
```
