# qiita.v2.TeamApi

All URIs are relative to *https://qiita.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_group_members**](TeamApi.md#add_group_members) | **POST** /api/v2/groups/{url_name}/members | Add group members
[**create_comment**](TeamApi.md#create_comment) | **POST** /api/v2/items/{item_id}/comments | Create comment
[**create_group**](TeamApi.md#create_group) | **POST** /api/v2/groups | Create group
[**create_imported_comment**](TeamApi.md#create_imported_comment) | **POST** /api/v2/items/{item_id}/imported_comments | Create imported comment
[**create_item**](TeamApi.md#create_item) | **POST** /api/v2/items | Create item
[**create_item_stock**](TeamApi.md#create_item_stock) | **PUT** /api/v2/items/{item_id}/stock | Create item stock
[**delete_comment**](TeamApi.md#delete_comment) | **DELETE** /api/v2/comments/{comment_id} | Delete comment
[**delete_group**](TeamApi.md#delete_group) | **DELETE** /api/v2/groups/{url_name} | Delete group
[**delete_group_members**](TeamApi.md#delete_group_members) | **DELETE** /api/v2/groups/{url_name}/members | Delete group members
[**delete_item**](TeamApi.md#delete_item) | **DELETE** /api/v2/items/{item_id} | Get item stockers
[**delete_item_stock**](TeamApi.md#delete_item_stock) | **DELETE** /api/v2/items/{item_id}/stock | Delete item stock
[**get_authenticated_user**](TeamApi.md#get_authenticated_user) | **GET** /api/v2/authenticated_user | Get authenticated user
[**get_authenticated_user_items**](TeamApi.md#get_authenticated_user_items) | **GET** /api/v2/authenticated_user/items | Get authenticated user items
[**get_comment**](TeamApi.md#get_comment) | **GET** /api/v2/comments/{comment_id} | Get comment
[**get_group**](TeamApi.md#get_group) | **GET** /api/v2/groups/{url_name} | Get group
[**get_group_member**](TeamApi.md#get_group_member) | **GET** /api/v2/groups/{url_name}/members/{user_id} | Get group member
[**get_group_members**](TeamApi.md#get_group_members) | **GET** /api/v2/groups/{url_name}/members | Get group members
[**get_groups**](TeamApi.md#get_groups) | **GET** /api/v2/groups | Get groups
[**get_item**](TeamApi.md#get_item) | **GET** /api/v2/items/{item_id} | Get item
[**get_item_comments**](TeamApi.md#get_item_comments) | **GET** /api/v2/items/{item_id}/comments | Get item comments
[**get_item_stockers**](TeamApi.md#get_item_stockers) | **GET** /api/v2/items/{item_id}/stockers | Get item stockers
[**get_items**](TeamApi.md#get_items) | **GET** /api/v2/items | Get items
[**get_oauth_team_authorize**](TeamApi.md#get_oauth_team_authorize) | **GET** /api/v2/oauth/team_authorize | Get OAuth team authorize
[**is_item_stock**](TeamApi.md#is_item_stock) | **GET** /api/v2/items/{item_id}/stock | Is item stock
[**update_comment**](TeamApi.md#update_comment) | **PATCH** /api/v2/comments/{comment_id} | Update comment
[**update_group**](TeamApi.md#update_group) | **PATCH** /api/v2/groups/{url_name} | Update group
[**update_item**](TeamApi.md#update_item) | **PATCH** /api/v2/items/{item_id} | 


# **add_group_members**
> GroupMember add_group_members(url_name, add_group_member_request=add_group_member_request)

Add group members

新たにグループにメンバーを追加します。

### Example

* Bearer Authentication (Bearer):

```python
import qiita.v2
from qiita.v2.models.add_group_member_request import AddGroupMemberRequest
from qiita.v2.models.group_member import GroupMember
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
    api_instance = qiita.v2.TeamApi(api_client)
    url_name = 'url_name_example' # str | グループのチーム上での一意な名前
    add_group_member_request = qiita.v2.AddGroupMemberRequest() # AddGroupMemberRequest |  (optional)

    try:
        # Add group members
        api_response = api_instance.add_group_members(url_name, add_group_member_request=add_group_member_request)
        print("The response of TeamApi->add_group_members:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamApi->add_group_members: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url_name** | **str**| グループのチーム上での一意な名前 | 
 **add_group_member_request** | [**AddGroupMemberRequest**](AddGroupMemberRequest.md)|  | [optional] 

### Return type

[**GroupMember**](GroupMember.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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
    api_instance = qiita.v2.TeamApi(api_client)
    item_id = 'item_id_example' # str | Article ID
    create_comment_request = qiita.v2.CreateCommentRequest() # CreateCommentRequest |  (optional)

    try:
        # Create comment
        api_response = api_instance.create_comment(item_id, create_comment_request=create_comment_request)
        print("The response of TeamApi->create_comment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamApi->create_comment: %s\n" % e)
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
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_group**
> Group create_group(create_group_request=create_group_request)

Create group

新たにグループを作成します。

### Example

* Bearer Authentication (Bearer):

```python
import qiita.v2
from qiita.v2.models.create_group_request import CreateGroupRequest
from qiita.v2.models.group import Group
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
    api_instance = qiita.v2.TeamApi(api_client)
    create_group_request = qiita.v2.CreateGroupRequest() # CreateGroupRequest |  (optional)

    try:
        # Create group
        api_response = api_instance.create_group(create_group_request=create_group_request)
        print("The response of TeamApi->create_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamApi->create_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_group_request** | [**CreateGroupRequest**](CreateGroupRequest.md)|  | [optional] 

### Return type

[**Group**](Group.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_imported_comment**
> Comment create_imported_comment(item_id, create_imported_comment_request=create_imported_comment_request)

Create imported comment

ユーザー名を指定して記事に対するコメントを作成します(Qiita Teamでのみ有効。管理者権限が必要)。

### Example

* Bearer Authentication (Bearer):

```python
import qiita.v2
from qiita.v2.models.comment import Comment
from qiita.v2.models.create_imported_comment_request import CreateImportedCommentRequest
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
    api_instance = qiita.v2.TeamApi(api_client)
    item_id = 'item_id_example' # str | Article ID
    create_imported_comment_request = qiita.v2.CreateImportedCommentRequest() # CreateImportedCommentRequest |  (optional)

    try:
        # Create imported comment
        api_response = api_instance.create_imported_comment(item_id, create_imported_comment_request=create_imported_comment_request)
        print("The response of TeamApi->create_imported_comment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamApi->create_imported_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| Article ID | 
 **create_imported_comment_request** | [**CreateImportedCommentRequest**](CreateImportedCommentRequest.md)|  | [optional] 

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
**201** | Created |  -  |

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
    api_instance = qiita.v2.TeamApi(api_client)
    create_item_request = qiita.v2.CreateItemRequest() # CreateItemRequest |  (optional)

    try:
        # Create item
        api_response = api_instance.create_item(create_item_request=create_item_request)
        print("The response of TeamApi->create_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamApi->create_item: %s\n" % e)
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
**201** | Created |  -  |

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
    api_instance = qiita.v2.TeamApi(api_client)
    item_id = 'item_id_example' # str | Article ID

    try:
        # Create item stock
        api_instance.create_item_stock(item_id)
    except Exception as e:
        print("Exception when calling TeamApi->create_item_stock: %s\n" % e)
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
    api_instance = qiita.v2.TeamApi(api_client)
    comment_id = '3391f50c35f953abfc4f' # str | コメントの一意なID

    try:
        # Delete comment
        api_instance.delete_comment(comment_id)
    except Exception as e:
        print("Exception when calling TeamApi->delete_comment: %s\n" % e)
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

# **delete_group**
> delete_group(url_name)

Delete group

グループを削除します。

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
    api_instance = qiita.v2.TeamApi(api_client)
    url_name = 'url_name_example' # str | グループのチーム上での一意な名前

    try:
        # Delete group
        api_instance.delete_group(url_name)
    except Exception as e:
        print("Exception when calling TeamApi->delete_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url_name** | **str**| グループのチーム上での一意な名前 | 

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

# **delete_group_members**
> delete_group_members(url_name, delete_group_member_request=delete_group_member_request)

Delete group members

グループからメンバーを脱退させます。

### Example

* Bearer Authentication (Bearer):

```python
import qiita.v2
from qiita.v2.models.delete_group_member_request import DeleteGroupMemberRequest
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
    api_instance = qiita.v2.TeamApi(api_client)
    url_name = 'url_name_example' # str | グループのチーム上での一意な名前
    delete_group_member_request = qiita.v2.DeleteGroupMemberRequest() # DeleteGroupMemberRequest |  (optional)

    try:
        # Delete group members
        api_instance.delete_group_members(url_name, delete_group_member_request=delete_group_member_request)
    except Exception as e:
        print("Exception when calling TeamApi->delete_group_members: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url_name** | **str**| グループのチーム上での一意な名前 | 
 **delete_group_member_request** | [**DeleteGroupMemberRequest**](DeleteGroupMemberRequest.md)|  | [optional] 

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
    api_instance = qiita.v2.TeamApi(api_client)
    item_id = 'item_id_example' # str | Article ID

    try:
        # Get item stockers
        api_instance.delete_item(item_id)
    except Exception as e:
        print("Exception when calling TeamApi->delete_item: %s\n" % e)
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
    api_instance = qiita.v2.TeamApi(api_client)
    item_id = 'item_id_example' # str | Article ID

    try:
        # Delete item stock
        api_instance.delete_item_stock(item_id)
    except Exception as e:
        print("Exception when calling TeamApi->delete_item_stock: %s\n" % e)
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
    api_instance = qiita.v2.TeamApi(api_client)

    try:
        # Get authenticated user
        api_response = api_instance.get_authenticated_user()
        print("The response of TeamApi->get_authenticated_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamApi->get_authenticated_user: %s\n" % e)
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
    api_instance = qiita.v2.TeamApi(api_client)
    page = 1 # int | ページ番号 (1から100まで) (optional)
    per_page = 20 # int | 1ページあたりに含まれる要素数 (1から100まで) (optional)

    try:
        # Get authenticated user items
        api_response = api_instance.get_authenticated_user_items(page=page, per_page=per_page)
        print("The response of TeamApi->get_authenticated_user_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamApi->get_authenticated_user_items: %s\n" % e)
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
    api_instance = qiita.v2.TeamApi(api_client)
    comment_id = '3391f50c35f953abfc4f' # str | コメントの一意なID

    try:
        # Get comment
        api_response = api_instance.get_comment(comment_id)
        print("The response of TeamApi->get_comment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamApi->get_comment: %s\n" % e)
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

# **get_group**
> Group get_group(url_name)

Get group

グループを取得します。

### Example

* Bearer Authentication (Bearer):

```python
import qiita.v2
from qiita.v2.models.group import Group
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
    api_instance = qiita.v2.TeamApi(api_client)
    url_name = 'url_name_example' # str | グループのチーム上での一意な名前

    try:
        # Get group
        api_response = api_instance.get_group(url_name)
        print("The response of TeamApi->get_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamApi->get_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url_name** | **str**| グループのチーム上での一意な名前 | 

### Return type

[**Group**](Group.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_member**
> Group get_group_member(url_name, user_id)

Get group member

グループのメンバーの名前を取得します。

### Example

* Bearer Authentication (Bearer):

```python
import qiita.v2
from qiita.v2.models.group import Group
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
    api_instance = qiita.v2.TeamApi(api_client)
    url_name = 'url_name_example' # str | グループのチーム上での一意な名前
    user_id = 'user_id_example' # str | ユーザーID

    try:
        # Get group member
        api_response = api_instance.get_group_member(url_name, user_id)
        print("The response of TeamApi->get_group_member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamApi->get_group_member: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url_name** | **str**| グループのチーム上での一意な名前 | 
 **user_id** | **str**| ユーザーID | 

### Return type

[**Group**](Group.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_members**
> Group get_group_members(url_name, page=page, per_page=per_page)

Get group members

チーム内に存在する特定のグループ一のメンバー一覧を作成日時の降順で返します。

### Example

* Bearer Authentication (Bearer):

```python
import qiita.v2
from qiita.v2.models.group import Group
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
    api_instance = qiita.v2.TeamApi(api_client)
    url_name = 'url_name_example' # str | グループのチーム上での一意な名前
    page = 1 # int | ページ番号 (1から100まで) (optional)
    per_page = 20 # int | 1ページあたりに含まれる要素数 (1から100まで) (optional)

    try:
        # Get group members
        api_response = api_instance.get_group_members(url_name, page=page, per_page=per_page)
        print("The response of TeamApi->get_group_members:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamApi->get_group_members: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url_name** | **str**| グループのチーム上での一意な名前 | 
 **page** | **int**| ページ番号 (1から100まで) | [optional] 
 **per_page** | **int**| 1ページあたりに含まれる要素数 (1から100まで) | [optional] 

### Return type

[**Group**](Group.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_groups**
> List[Group] get_groups(page=page, per_page=per_page)

Get groups

チーム内に存在するグループ一覧のうち未参加のプライベートグループ以外を作成日時の降順で返します。

### Example

* Bearer Authentication (Bearer):

```python
import qiita.v2
from qiita.v2.models.group import Group
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
    api_instance = qiita.v2.TeamApi(api_client)
    page = 1 # int | ページ番号 (1から100まで) (optional)
    per_page = 20 # int | 1ページあたりに含まれる要素数 (1から100まで) (optional)

    try:
        # Get groups
        api_response = api_instance.get_groups(page=page, per_page=per_page)
        print("The response of TeamApi->get_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamApi->get_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| ページ番号 (1から100まで) | [optional] 
 **per_page** | **int**| 1ページあたりに含まれる要素数 (1から100まで) | [optional] 

### Return type

[**List[Group]**](Group.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |

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
    api_instance = qiita.v2.TeamApi(api_client)
    item_id = 'item_id_example' # str | Article ID

    try:
        # Get item
        api_response = api_instance.get_item(item_id)
        print("The response of TeamApi->get_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamApi->get_item: %s\n" % e)
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
    api_instance = qiita.v2.TeamApi(api_client)
    item_id = 'item_id_example' # str | Article ID

    try:
        # Get item comments
        api_response = api_instance.get_item_comments(item_id)
        print("The response of TeamApi->get_item_comments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamApi->get_item_comments: %s\n" % e)
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
    api_instance = qiita.v2.TeamApi(api_client)
    item_id = 'item_id_example' # str | Article ID
    page = 1 # int | ページ番号 (1から100まで) (optional)
    per_page = 20 # int | 1ページあたりに含まれる要素数 (1から100まで) (optional)

    try:
        # Get item stockers
        api_response = api_instance.get_item_stockers(item_id, page=page, per_page=per_page)
        print("The response of TeamApi->get_item_stockers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamApi->get_item_stockers: %s\n" % e)
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
    api_instance = qiita.v2.TeamApi(api_client)
    page = 1 # int | ページ番号 (1から100まで) (optional)
    per_page = 20 # int | 1ページあたりに含まれる要素数 (1から100まで) (optional)
    query = 'qiita user:Qiita' # str | 検索クエリ (optional)

    try:
        # Get items
        api_response = api_instance.get_items(page=page, per_page=per_page, query=query)
        print("The response of TeamApi->get_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamApi->get_items: %s\n" % e)
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

# **get_oauth_team_authorize**
> get_oauth_team_authorize(client_id, scope, state)

Get OAuth team authorize

チーム別アクセストークンを発行するには、それぞれのチームでアプリケーションのユーザーに認可画面を表示する必要があります。ユーザーがアプリケーションからのアクセスを認可すると、アプリケーション登録時に指定されたURLにリダイレクトされます。このとき、リダイレクト先のURLクエリにcodeが付与されます。また指定した場合は state も付与されます。アプリケーションでは、この code の値を利用して POST /api/v2/team_access_tokens にリクエストを送り、チーム別アクセストークンを発行します。Qiita Teamでのみ有効です。

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
    api_instance = qiita.v2.TeamApi(api_client)
    client_id = 'a91f0396a0968ff593eafdd194e3d17d32c41b1d' # str | 登録されたAPIクライアントを特定するためのIDです。40桁の16進数で表現されます。
    scope = 'read_qiita write_qiita_team' # str | アプリケーションが利用するスコープをスペース区切りで指定できます。
    state = 'CSRF対策のため、認可後にリダイレクトするURLのクエリに含まれる値を指定できます。' # str | CSRF対策のため、認可後にリダイレクトするURLのクエリに含まれる値を指定できます。

    try:
        # Get OAuth team authorize
        api_instance.get_oauth_team_authorize(client_id, scope, state)
    except Exception as e:
        print("Exception when calling TeamApi->get_oauth_team_authorize: %s\n" % e)
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
    api_instance = qiita.v2.TeamApi(api_client)
    item_id = 'item_id_example' # str | Article ID

    try:
        # Is item stock
        api_instance.is_item_stock(item_id)
    except Exception as e:
        print("Exception when calling TeamApi->is_item_stock: %s\n" % e)
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
    api_instance = qiita.v2.TeamApi(api_client)
    comment_id = '3391f50c35f953abfc4f' # str | コメントの一意なID
    update_comment_request = qiita.v2.UpdateCommentRequest() # UpdateCommentRequest |  (optional)

    try:
        # Update comment
        api_response = api_instance.update_comment(comment_id, update_comment_request=update_comment_request)
        print("The response of TeamApi->update_comment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamApi->update_comment: %s\n" % e)
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

# **update_group**
> Group update_group(url_name, update_group_request=update_group_request)

Update group

グループを更新します。

### Example

* Bearer Authentication (Bearer):

```python
import qiita.v2
from qiita.v2.models.group import Group
from qiita.v2.models.update_group_request import UpdateGroupRequest
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
    api_instance = qiita.v2.TeamApi(api_client)
    url_name = 'url_name_example' # str | グループのチーム上での一意な名前
    update_group_request = qiita.v2.UpdateGroupRequest() # UpdateGroupRequest |  (optional)

    try:
        # Update group
        api_response = api_instance.update_group(url_name, update_group_request=update_group_request)
        print("The response of TeamApi->update_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamApi->update_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url_name** | **str**| グループのチーム上での一意な名前 | 
 **update_group_request** | [**UpdateGroupRequest**](UpdateGroupRequest.md)|  | [optional] 

### Return type

[**Group**](Group.md)

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
    api_instance = qiita.v2.TeamApi(api_client)
    item_id = 'item_id_example' # str | Article ID
    update_item_request = qiita.v2.UpdateItemRequest() # UpdateItemRequest |  (optional)

    try:
        # 
        api_response = api_instance.update_item(item_id, update_item_request=update_item_request)
        print("The response of TeamApi->update_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamApi->update_item: %s\n" % e)
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

