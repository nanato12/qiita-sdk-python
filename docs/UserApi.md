# qiita.v2.UserApi

All URIs are relative to *https://qiita.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_comment**](UserApi.md#create_comment) | **POST** /api/v2/items/{item_id}/comments | Create comment
[**create_item**](UserApi.md#create_item) | **POST** /api/v2/items | Create item
[**create_item_like**](UserApi.md#create_item_like) | **PUT** /api/v2/items/{item_id}/like | Create item like
[**create_item_stock**](UserApi.md#create_item_stock) | **PUT** /api/v2/items/{item_id}/stock | Create item stock
[**delete_api_v2_access_tokens_access_token**](UserApi.md#delete_api_v2_access_tokens_access_token) | **DELETE** /api/v2/access_tokens/{access_token} | 
[**delete_comment**](UserApi.md#delete_comment) | **DELETE** /api/v2/comments/{comment_id} | Delete comment
[**delete_item**](UserApi.md#delete_item) | **DELETE** /api/v2/items/{item_id} | Get item stockers
[**delete_item_like**](UserApi.md#delete_item_like) | **DELETE** /api/v2/items/{item_id}/like | Delete item like
[**delete_item_stock**](UserApi.md#delete_item_stock) | **DELETE** /api/v2/items/{item_id}/stock | Delete item stock
[**follow**](UserApi.md#follow) | **PUT** /api/v2/users/{user_id}/following | Follow
[**get_authenticated_user**](UserApi.md#get_authenticated_user) | **GET** /api/v2/authenticated_user | Get authenticated user
[**get_authenticated_user_items**](UserApi.md#get_authenticated_user_items) | **GET** /api/v2/authenticated_user/items | Get authenticated user items
[**get_comment**](UserApi.md#get_comment) | **GET** /api/v2/comments/{comment_id} | Get comment
[**get_item**](UserApi.md#get_item) | **GET** /api/v2/items/{item_id} | Get item
[**get_item_comments**](UserApi.md#get_item_comments) | **GET** /api/v2/items/{item_id}/comments | Get item comments
[**get_item_likes**](UserApi.md#get_item_likes) | **GET** /api/v2/items/{item_id}/likes | Get item likes
[**get_item_stockers**](UserApi.md#get_item_stockers) | **GET** /api/v2/items/{item_id}/stockers | Get item stockers
[**get_items**](UserApi.md#get_items) | **GET** /api/v2/items | Get items
[**get_oauth_authorize**](UserApi.md#get_oauth_authorize) | **GET** /api/v2/oauth/authorize | Get OAuth authorize
[**get_user**](UserApi.md#get_user) | **GET** /api/v2/users/{user_id} | Get user
[**get_user_followees**](UserApi.md#get_user_followees) | **GET** /api/v2/users/{user_id}/followees | Get user followees
[**get_user_followers**](UserApi.md#get_user_followers) | **GET** /api/v2/users/{user_id}/followers | Get user followers
[**get_users**](UserApi.md#get_users) | **GET** /api/v2/users | Get users
[**is_item_like**](UserApi.md#is_item_like) | **GET** /api/v2/items/{item_id}/like | Is item like
[**is_item_stock**](UserApi.md#is_item_stock) | **GET** /api/v2/items/{item_id}/stock | Is item stock
[**is_user_following**](UserApi.md#is_user_following) | **GET** /api/v2/users/{user_id}/following | Is user following
[**issue_access_tokens**](UserApi.md#issue_access_tokens) | **POST** /api/v2/access_tokens | Issue access token
[**unfollow**](UserApi.md#unfollow) | **DELETE** /api/v2/users/{user_id}/following | Unfollow
[**update_comment**](UserApi.md#update_comment) | **PATCH** /api/v2/comments/{comment_id} | Update comment
[**update_item**](UserApi.md#update_item) | **PATCH** /api/v2/items/{item_id} | 


# **create_comment**
> Comment create_comment(item_id, create_comment_request=create_comment_request)

Create comment

記事に対してコメントを投稿します。

### Example

* Bearer Authentication (Bearer):

```python
import qiita.v2
from qiita.v2.models.comment import Comment
from qiita.v2.models.create_comment_request import CreateCommentRequest
from qiita.v2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://qiita.com
# See configuration.py for a list of all supported configuration parameters.
configuration = qiita.v2.Configuration(
    host = "https://qiita.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = qiita.v2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qiita.v2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qiita.v2.UserApi(api_client)
    item_id = 'item_id_example' # str | Article ID
    create_comment_request = qiita.v2.CreateCommentRequest() # CreateCommentRequest |  (optional)

    try:
        # Create comment
        api_response = api_instance.create_comment(item_id, create_comment_request=create_comment_request)
        print("The response of UserApi->create_comment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->create_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| Article ID | 
 **create_comment_request** | [**CreateCommentRequest**](CreateCommentRequest.md)|  | [optional] 

### Return type

[**Comment**](Comment.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_item**
> Item create_item(create_item_request=create_item_request)

Create item

新たに記事を作成します。  Create a new article.

### Example

* Bearer Authentication (Bearer):

```python
import qiita.v2
from qiita.v2.models.create_item_request import CreateItemRequest
from qiita.v2.models.item import Item
from qiita.v2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://qiita.com
# See configuration.py for a list of all supported configuration parameters.
configuration = qiita.v2.Configuration(
    host = "https://qiita.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = qiita.v2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qiita.v2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qiita.v2.UserApi(api_client)
    create_item_request = qiita.v2.CreateItemRequest() # CreateItemRequest |  (optional)

    try:
        # Create item
        api_response = api_instance.create_item(create_item_request=create_item_request)
        print("The response of UserApi->create_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->create_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_item_request** | [**CreateItemRequest**](CreateItemRequest.md)|  | [optional] 

### Return type

[**Item**](Item.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_item_like**
> create_item_like(item_id)

Create item like

Qiita TeamのいいねAPIは2020年11月4日より廃止となりました。今後は絵文字リアクションAPIをご利用ください。 記事に「いいね」を付けます。

### Example

* Bearer Authentication (Bearer):

```python
import qiita.v2
from qiita.v2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://qiita.com
# See configuration.py for a list of all supported configuration parameters.
configuration = qiita.v2.Configuration(
    host = "https://qiita.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = qiita.v2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qiita.v2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qiita.v2.UserApi(api_client)
    item_id = 'item_id_example' # str | Article ID

    try:
        # Create item like
        api_instance.create_item_like(item_id)
    except Exception as e:
        print("Exception when calling UserApi->create_item_like: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| Article ID | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_item_stock**
> create_item_stock(item_id)

Create item stock

記事をストックします。

### Example

* Bearer Authentication (Bearer):

```python
import qiita.v2
from qiita.v2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://qiita.com
# See configuration.py for a list of all supported configuration parameters.
configuration = qiita.v2.Configuration(
    host = "https://qiita.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = qiita.v2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qiita.v2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qiita.v2.UserApi(api_client)
    item_id = 'item_id_example' # str | Article ID

    try:
        # Create item stock
        api_instance.create_item_stock(item_id)
    except Exception as e:
        print("Exception when calling UserApi->create_item_stock: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| Article ID | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_api_v2_access_tokens_access_token**
> delete_api_v2_access_tokens_access_token(access_token)



指定されたアクセストークンを失効させ、それ以降利用できないようにします。 

### Example

* Bearer Authentication (Bearer):

```python
import qiita.v2
from qiita.v2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://qiita.com
# See configuration.py for a list of all supported configuration parameters.
configuration = qiita.v2.Configuration(
    host = "https://qiita.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = qiita.v2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qiita.v2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qiita.v2.UserApi(api_client)
    access_token = 'ea5d0a593b2655e9568f144fb1826342292f5c6b' # str | アクセストークンを表現する文字列

    try:
        # 
        api_instance.delete_api_v2_access_tokens_access_token(access_token)
    except Exception as e:
        print("Exception when calling UserApi->delete_api_v2_access_tokens_access_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| アクセストークンを表現する文字列 | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_comment**
> delete_comment(comment_id)

Delete comment

コメントを削除します。

### Example

* Bearer Authentication (Bearer):

```python
import qiita.v2
from qiita.v2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://qiita.com
# See configuration.py for a list of all supported configuration parameters.
configuration = qiita.v2.Configuration(
    host = "https://qiita.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = qiita.v2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qiita.v2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qiita.v2.UserApi(api_client)
    comment_id = '3391f50c35f953abfc4f' # str | コメントの一意なID

    try:
        # Delete comment
        api_instance.delete_comment(comment_id)
    except Exception as e:
        print("Exception when calling UserApi->delete_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comment_id** | **str**| コメントの一意なID | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_item**
> delete_item(item_id)

Get item stockers

記事を削除します。

### Example

* Bearer Authentication (Bearer):

```python
import qiita.v2
from qiita.v2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://qiita.com
# See configuration.py for a list of all supported configuration parameters.
configuration = qiita.v2.Configuration(
    host = "https://qiita.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = qiita.v2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qiita.v2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qiita.v2.UserApi(api_client)
    item_id = 'item_id_example' # str | Article ID

    try:
        # Get item stockers
        api_instance.delete_item(item_id)
    except Exception as e:
        print("Exception when calling UserApi->delete_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| Article ID | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_item_like**
> delete_item_like(item_id)

Delete item like

Qiita TeamのいいねAPIは2020年11月4日より廃止となりました。今後は絵文字リアクションAPIをご利用ください。 記事への「いいね」を取り消します。

### Example

* Bearer Authentication (Bearer):

```python
import qiita.v2
from qiita.v2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://qiita.com
# See configuration.py for a list of all supported configuration parameters.
configuration = qiita.v2.Configuration(
    host = "https://qiita.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = qiita.v2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qiita.v2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qiita.v2.UserApi(api_client)
    item_id = 'item_id_example' # str | Article ID

    try:
        # Delete item like
        api_instance.delete_item_like(item_id)
    except Exception as e:
        print("Exception when calling UserApi->delete_item_like: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| Article ID | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_item_stock**
> delete_item_stock(item_id)

Delete item stock

記事をストックから取り除きます。

### Example

* Bearer Authentication (Bearer):

```python
import qiita.v2
from qiita.v2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://qiita.com
# See configuration.py for a list of all supported configuration parameters.
configuration = qiita.v2.Configuration(
    host = "https://qiita.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = qiita.v2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qiita.v2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qiita.v2.UserApi(api_client)
    item_id = 'item_id_example' # str | Article ID

    try:
        # Delete item stock
        api_instance.delete_item_stock(item_id)
    except Exception as e:
        print("Exception when calling UserApi->delete_item_stock: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| Article ID | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **follow**
> follow(user_id)

Follow

ユーザーをフォローします。

### Example

* Bearer Authentication (Bearer):

```python
import qiita.v2
from qiita.v2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://qiita.com
# See configuration.py for a list of all supported configuration parameters.
configuration = qiita.v2.Configuration(
    host = "https://qiita.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = qiita.v2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qiita.v2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qiita.v2.UserApi(api_client)
    user_id = 'user_id_example' # str | ユーザーID

    try:
        # Follow
        api_instance.follow(user_id)
    except Exception as e:
        print("Exception when calling UserApi->follow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ユーザーID | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_authenticated_user**
> AuthenticatedUser get_authenticated_user()

Get authenticated user

アクセストークンに紐付いたユーザーを返します。

### Example

* Bearer Authentication (Bearer):

```python
import qiita.v2
from qiita.v2.models.authenticated_user import AuthenticatedUser
from qiita.v2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://qiita.com
# See configuration.py for a list of all supported configuration parameters.
configuration = qiita.v2.Configuration(
    host = "https://qiita.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = qiita.v2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qiita.v2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qiita.v2.UserApi(api_client)

    try:
        # Get authenticated user
        api_response = api_instance.get_authenticated_user()
        print("The response of UserApi->get_authenticated_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_authenticated_user: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AuthenticatedUser**](AuthenticatedUser.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_authenticated_user_items**
> Item get_authenticated_user_items(page=page, per_page=per_page)

Get authenticated user items

認証中のユーザーの記事の一覧を作成日時の降順で返します。

### Example

* Bearer Authentication (Bearer):

```python
import qiita.v2
from qiita.v2.models.item import Item
from qiita.v2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://qiita.com
# See configuration.py for a list of all supported configuration parameters.
configuration = qiita.v2.Configuration(
    host = "https://qiita.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = qiita.v2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qiita.v2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qiita.v2.UserApi(api_client)
    page = 1 # int | ページ番号 (1から100まで) (optional)
    per_page = 20 # int | 1ページあたりに含まれる要素数 (1から100まで) (optional)

    try:
        # Get authenticated user items
        api_response = api_instance.get_authenticated_user_items(page=page, per_page=per_page)
        print("The response of UserApi->get_authenticated_user_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_authenticated_user_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| ページ番号 (1から100まで) | [optional] 
 **per_page** | **int**| 1ページあたりに含まれる要素数 (1から100まで) | [optional] 

### Return type

[**Item**](Item.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_comment**
> Comment get_comment(comment_id)

Get comment

コメントを取得します。

### Example

* Bearer Authentication (Bearer):

```python
import qiita.v2
from qiita.v2.models.comment import Comment
from qiita.v2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://qiita.com
# See configuration.py for a list of all supported configuration parameters.
configuration = qiita.v2.Configuration(
    host = "https://qiita.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = qiita.v2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qiita.v2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qiita.v2.UserApi(api_client)
    comment_id = '3391f50c35f953abfc4f' # str | コメントの一意なID

    try:
        # Get comment
        api_response = api_instance.get_comment(comment_id)
        print("The response of UserApi->get_comment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comment_id** | **str**| コメントの一意なID | 

### Return type

[**Comment**](Comment.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item**
> Item get_item(item_id)

Get item

記事を取得します。

### Example

* Bearer Authentication (Bearer):

```python
import qiita.v2
from qiita.v2.models.item import Item
from qiita.v2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://qiita.com
# See configuration.py for a list of all supported configuration parameters.
configuration = qiita.v2.Configuration(
    host = "https://qiita.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = qiita.v2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qiita.v2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qiita.v2.UserApi(api_client)
    item_id = 'item_id_example' # str | Article ID

    try:
        # Get item
        api_response = api_instance.get_item(item_id)
        print("The response of UserApi->get_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| Article ID | 

### Return type

[**Item**](Item.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_comments**
> List[Comment] get_item_comments(item_id)

Get item comments

投稿に付けられたコメント一覧を投稿日時の降順で取得します。

### Example

* Bearer Authentication (Bearer):

```python
import qiita.v2
from qiita.v2.models.comment import Comment
from qiita.v2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://qiita.com
# See configuration.py for a list of all supported configuration parameters.
configuration = qiita.v2.Configuration(
    host = "https://qiita.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = qiita.v2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qiita.v2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qiita.v2.UserApi(api_client)
    item_id = 'item_id_example' # str | Article ID

    try:
        # Get item comments
        api_response = api_instance.get_item_comments(item_id)
        print("The response of UserApi->get_item_comments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_item_comments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| Article ID | 

### Return type

[**List[Comment]**](Comment.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_likes**
> List[LikeHistory] get_item_likes(item_id)

Get item likes

Qiita TeamのいいねAPIは2020年11月4日より廃止となりました。今後は絵文字リアクションAPIをご利用ください。  記事につけられた「いいね」を作成日時の降順で返します。

### Example

* Bearer Authentication (Bearer):

```python
import qiita.v2
from qiita.v2.models.like_history import LikeHistory
from qiita.v2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://qiita.com
# See configuration.py for a list of all supported configuration parameters.
configuration = qiita.v2.Configuration(
    host = "https://qiita.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = qiita.v2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qiita.v2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qiita.v2.UserApi(api_client)
    item_id = 'item_id_example' # str | Article ID

    try:
        # Get item likes
        api_response = api_instance.get_item_likes(item_id)
        print("The response of UserApi->get_item_likes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_item_likes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| Article ID | 

### Return type

[**List[LikeHistory]**](LikeHistory.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_stockers**
> List[User] get_item_stockers(item_id, page=page, per_page=per_page)

Get item stockers

記事をストックしているユーザー一覧を、ストックした日時の降順で返します。

### Example

* Bearer Authentication (Bearer):

```python
import qiita.v2
from qiita.v2.models.user import User
from qiita.v2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://qiita.com
# See configuration.py for a list of all supported configuration parameters.
configuration = qiita.v2.Configuration(
    host = "https://qiita.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = qiita.v2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qiita.v2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qiita.v2.UserApi(api_client)
    item_id = 'item_id_example' # str | Article ID
    page = 1 # int | ページ番号 (1から100まで) (optional)
    per_page = 20 # int | 1ページあたりに含まれる要素数 (1から100まで) (optional)

    try:
        # Get item stockers
        api_response = api_instance.get_item_stockers(item_id, page=page, per_page=per_page)
        print("The response of UserApi->get_item_stockers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_item_stockers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| Article ID | 
 **page** | **int**| ページ番号 (1から100まで) | [optional] 
 **per_page** | **int**| 1ページあたりに含まれる要素数 (1から100まで) | [optional] 

### Return type

[**List[User]**](User.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_items**
> List[Item] get_items(page=page, per_page=per_page, query=query)

Get items

記事の一覧を作成日時の降順で返します。

### Example

* Bearer Authentication (Bearer):

```python
import qiita.v2
from qiita.v2.models.item import Item
from qiita.v2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://qiita.com
# See configuration.py for a list of all supported configuration parameters.
configuration = qiita.v2.Configuration(
    host = "https://qiita.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = qiita.v2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qiita.v2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qiita.v2.UserApi(api_client)
    page = 1 # int | ページ番号 (1から100まで) (optional)
    per_page = 20 # int | 1ページあたりに含まれる要素数 (1から100まで) (optional)
    query = 'qiita user:Qiita' # str | 検索クエリ (optional)

    try:
        # Get items
        api_response = api_instance.get_items(page=page, per_page=per_page, query=query)
        print("The response of UserApi->get_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| ページ番号 (1から100まで) | [optional] 
 **per_page** | **int**| 1ページあたりに含まれる要素数 (1から100まで) | [optional] 
 **query** | **str**| 検索クエリ | [optional] 

### Return type

[**List[Item]**](Item.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_oauth_authorize**
> get_oauth_authorize(client_id, scope, state)

Get OAuth authorize

read_qiita_team、write_qiita_teamを使う場合、authorizeページによる認証認可は2020年6月5日に非推奨となりました。今後はご利用されるチームのホストでteam_authorizeをご利用ください。 アクセストークンを発行するには、アプリケーションのユーザーに認可画面を表示する必要があります。ユーザーがアプリケーションからのアクセスを認可すると、アプリケーション登録時に指定されたURLにリダイレクトされます。このとき、リダイレクト先のURLクエリにcodeが付与されます。また指定した場合は state も付与されます。アプリケーションでは、この code の値を利用して POST /api/v2/access_tokens にリクエストを送り、アクセストークンを発行します。

### Example

* Bearer Authentication (Bearer):

```python
import qiita.v2
from qiita.v2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://qiita.com
# See configuration.py for a list of all supported configuration parameters.
configuration = qiita.v2.Configuration(
    host = "https://qiita.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = qiita.v2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qiita.v2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qiita.v2.UserApi(api_client)
    client_id = 'a91f0396a0968ff593eafdd194e3d17d32c41b1d' # str | 登録されたAPIクライアントを特定するためのIDです。40桁の16進数で表現されます。
    scope = 'read_qiita write_qiita_team' # str | アプリケーションが利用するスコープをスペース区切りで指定できます。
    state = 'CSRF対策のため、認可後にリダイレクトするURLのクエリに含まれる値を指定できます。' # str | CSRF対策のため、認可後にリダイレクトするURLのクエリに含まれる値を指定できます。

    try:
        # Get OAuth authorize
        api_instance.get_oauth_authorize(client_id, scope, state)
    except Exception as e:
        print("Exception when calling UserApi->get_oauth_authorize: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| 登録されたAPIクライアントを特定するためのIDです。40桁の16進数で表現されます。 | 
 **scope** | **str**| アプリケーションが利用するスコープをスペース区切りで指定できます。 | 
 **state** | **str**| CSRF対策のため、認可後にリダイレクトするURLのクエリに含まれる値を指定できます。 | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> User get_user(user_id)

Get user

ユーザーを取得します。

### Example

* Bearer Authentication (Bearer):

```python
import qiita.v2
from qiita.v2.models.user import User
from qiita.v2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://qiita.com
# See configuration.py for a list of all supported configuration parameters.
configuration = qiita.v2.Configuration(
    host = "https://qiita.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = qiita.v2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qiita.v2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qiita.v2.UserApi(api_client)
    user_id = 'user_id_example' # str | ユーザーID

    try:
        # Get user
        api_response = api_instance.get_user(user_id)
        print("The response of UserApi->get_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ユーザーID | 

### Return type

[**User**](User.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_followees**
> List[User] get_user_followees(user_id, page=page, per_page=per_page)

Get user followees

ユーザーがフォローしているユーザー一覧を取得します。

### Example

* Bearer Authentication (Bearer):

```python
import qiita.v2
from qiita.v2.models.user import User
from qiita.v2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://qiita.com
# See configuration.py for a list of all supported configuration parameters.
configuration = qiita.v2.Configuration(
    host = "https://qiita.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = qiita.v2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qiita.v2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qiita.v2.UserApi(api_client)
    user_id = 'user_id_example' # str | ユーザーID
    page = 1 # int | ページ番号 (1から100まで) (optional)
    per_page = 20 # int | 1ページあたりに含まれる要素数 (1から100まで) (optional)

    try:
        # Get user followees
        api_response = api_instance.get_user_followees(user_id, page=page, per_page=per_page)
        print("The response of UserApi->get_user_followees:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_user_followees: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ユーザーID | 
 **page** | **int**| ページ番号 (1から100まで) | [optional] 
 **per_page** | **int**| 1ページあたりに含まれる要素数 (1から100まで) | [optional] 

### Return type

[**List[User]**](User.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_followers**
> List[User] get_user_followers(user_id, page=page, per_page=per_page)

Get user followers

ユーザーをフォローしているユーザー一覧を取得します。

### Example

* Bearer Authentication (Bearer):

```python
import qiita.v2
from qiita.v2.models.user import User
from qiita.v2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://qiita.com
# See configuration.py for a list of all supported configuration parameters.
configuration = qiita.v2.Configuration(
    host = "https://qiita.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = qiita.v2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qiita.v2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qiita.v2.UserApi(api_client)
    user_id = 'user_id_example' # str | ユーザーID
    page = 1 # int | ページ番号 (1から100まで) (optional)
    per_page = 20 # int | 1ページあたりに含まれる要素数 (1から100まで) (optional)

    try:
        # Get user followers
        api_response = api_instance.get_user_followers(user_id, page=page, per_page=per_page)
        print("The response of UserApi->get_user_followers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_user_followers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ユーザーID | 
 **page** | **int**| ページ番号 (1から100まで) | [optional] 
 **per_page** | **int**| 1ページあたりに含まれる要素数 (1から100まで) | [optional] 

### Return type

[**List[User]**](User.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users**
> List[User] get_users(page=page, per_page=per_page)

Get users

全てのユーザーの一覧を作成日時の降順で取得します。

### Example

* Bearer Authentication (Bearer):

```python
import qiita.v2
from qiita.v2.models.user import User
from qiita.v2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://qiita.com
# See configuration.py for a list of all supported configuration parameters.
configuration = qiita.v2.Configuration(
    host = "https://qiita.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = qiita.v2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qiita.v2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qiita.v2.UserApi(api_client)
    page = 1 # int | ページ番号 (1から100まで) (optional)
    per_page = 20 # int | 1ページあたりに含まれる要素数 (1から100まで) (optional)

    try:
        # Get users
        api_response = api_instance.get_users(page=page, per_page=per_page)
        print("The response of UserApi->get_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| ページ番号 (1から100まで) | [optional] 
 **per_page** | **int**| 1ページあたりに含まれる要素数 (1から100まで) | [optional] 

### Return type

[**List[User]**](User.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **is_item_like**
> is_item_like(item_id)

Is item like

Qiita TeamのいいねAPIは2020年11月4日より廃止となりました。今後は絵文字リアクションAPIをご利用ください。 記事に「いいね」を付けているかどうかを調べます。

### Example

* Bearer Authentication (Bearer):

```python
import qiita.v2
from qiita.v2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://qiita.com
# See configuration.py for a list of all supported configuration parameters.
configuration = qiita.v2.Configuration(
    host = "https://qiita.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = qiita.v2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qiita.v2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qiita.v2.UserApi(api_client)
    item_id = 'item_id_example' # str | Article ID

    try:
        # Is item like
        api_instance.is_item_like(item_id)
    except Exception as e:
        print("Exception when calling UserApi->is_item_like: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| Article ID | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **is_item_stock**
> is_item_stock(item_id)

Is item stock

記事をストックしているかどうかを調べます。

### Example

* Bearer Authentication (Bearer):

```python
import qiita.v2
from qiita.v2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://qiita.com
# See configuration.py for a list of all supported configuration parameters.
configuration = qiita.v2.Configuration(
    host = "https://qiita.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = qiita.v2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qiita.v2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qiita.v2.UserApi(api_client)
    item_id = 'item_id_example' # str | Article ID

    try:
        # Is item stock
        api_instance.is_item_stock(item_id)
    except Exception as e:
        print("Exception when calling UserApi->is_item_stock: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| Article ID | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **is_user_following**
> is_user_following(user_id)

Is user following

ユーザーをフォローしている場合に204を返します。

### Example

* Bearer Authentication (Bearer):

```python
import qiita.v2
from qiita.v2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://qiita.com
# See configuration.py for a list of all supported configuration parameters.
configuration = qiita.v2.Configuration(
    host = "https://qiita.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = qiita.v2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qiita.v2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qiita.v2.UserApi(api_client)
    user_id = 'user_id_example' # str | ユーザーID

    try:
        # Is user following
        api_instance.is_user_following(user_id)
    except Exception as e:
        print("Exception when calling UserApi->is_user_following: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ユーザーID | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_access_tokens**
> issue_access_tokens(issue_access_token_request=issue_access_token_request)

Issue access token

与えられた認証情報をもとに新しいアクセストークンを発行します。

### Example

* Bearer Authentication (Bearer):

```python
import qiita.v2
from qiita.v2.models.issue_access_token_request import IssueAccessTokenRequest
from qiita.v2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://qiita.com
# See configuration.py for a list of all supported configuration parameters.
configuration = qiita.v2.Configuration(
    host = "https://qiita.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = qiita.v2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qiita.v2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qiita.v2.UserApi(api_client)
    issue_access_token_request = qiita.v2.IssueAccessTokenRequest() # IssueAccessTokenRequest |  (optional)

    try:
        # Issue access token
        api_instance.issue_access_tokens(issue_access_token_request=issue_access_token_request)
    except Exception as e:
        print("Exception when calling UserApi->issue_access_tokens: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issue_access_token_request** | [**IssueAccessTokenRequest**](IssueAccessTokenRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unfollow**
> unfollow(user_id)

Unfollow

ユーザーへのフォローを外します。

### Example

* Bearer Authentication (Bearer):

```python
import qiita.v2
from qiita.v2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://qiita.com
# See configuration.py for a list of all supported configuration parameters.
configuration = qiita.v2.Configuration(
    host = "https://qiita.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = qiita.v2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qiita.v2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qiita.v2.UserApi(api_client)
    user_id = 'user_id_example' # str | ユーザーID

    try:
        # Unfollow
        api_instance.unfollow(user_id)
    except Exception as e:
        print("Exception when calling UserApi->unfollow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ユーザーID | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_comment**
> Comment update_comment(comment_id, update_comment_request=update_comment_request)

Update comment

コメントを更新します。

### Example

* Bearer Authentication (Bearer):

```python
import qiita.v2
from qiita.v2.models.comment import Comment
from qiita.v2.models.update_comment_request import UpdateCommentRequest
from qiita.v2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://qiita.com
# See configuration.py for a list of all supported configuration parameters.
configuration = qiita.v2.Configuration(
    host = "https://qiita.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = qiita.v2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qiita.v2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qiita.v2.UserApi(api_client)
    comment_id = '3391f50c35f953abfc4f' # str | コメントの一意なID
    update_comment_request = qiita.v2.UpdateCommentRequest() # UpdateCommentRequest |  (optional)

    try:
        # Update comment
        api_response = api_instance.update_comment(comment_id, update_comment_request=update_comment_request)
        print("The response of UserApi->update_comment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->update_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comment_id** | **str**| コメントの一意なID | 
 **update_comment_request** | [**UpdateCommentRequest**](UpdateCommentRequest.md)|  | [optional] 

### Return type

[**Comment**](Comment.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_item**
> Item update_item(item_id, update_item_request=update_item_request)



記事を更新します。

### Example

* Bearer Authentication (Bearer):

```python
import qiita.v2
from qiita.v2.models.item import Item
from qiita.v2.models.update_item_request import UpdateItemRequest
from qiita.v2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://qiita.com
# See configuration.py for a list of all supported configuration parameters.
configuration = qiita.v2.Configuration(
    host = "https://qiita.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = qiita.v2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qiita.v2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qiita.v2.UserApi(api_client)
    item_id = 'item_id_example' # str | Article ID
    update_item_request = qiita.v2.UpdateItemRequest() # UpdateItemRequest |  (optional)

    try:
        # 
        api_response = api_instance.update_item(item_id, update_item_request=update_item_request)
        print("The response of UserApi->update_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->update_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| Article ID | 
 **update_item_request** | [**UpdateItemRequest**](UpdateItemRequest.md)|  | [optional] 

### Return type

[**Item**](Item.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

