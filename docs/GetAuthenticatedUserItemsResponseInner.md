# GetAuthenticatedUserItemsResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rendered_body** | **str** |  | [optional] 
**body** | **str** |  | [optional] 
**coediting** | **bool** |  | [optional] 
**comments_count** | **int** |  | [optional] 
**created_at** | **str** |  | [optional] 
**group** | [**GetAuthenticatedUserItemsResponseInnerGroup**](GetAuthenticatedUserItemsResponseInnerGroup.md) |  | [optional] 
**id** | **str** |  | [optional] 
**likes_count** | **int** |  | [optional] 
**private** | **bool** |  | [optional] 
**reactions_count** | **int** |  | [optional] 
**stocks_count** | **int** |  | [optional] 
**tags** | [**List[GetAuthenticatedUserItemsResponseInnerTagsInner]**](GetAuthenticatedUserItemsResponseInnerTagsInner.md) |  | [optional] 
**title** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**user** | [**GetAuthenticatedUserItemsResponseInnerUser**](GetAuthenticatedUserItemsResponseInnerUser.md) |  | [optional] 
**page_views_count** | **int** |  | [optional] 
**team_membership** | [**GetAuthenticatedUserItemsResponseInnerTeamMembership**](GetAuthenticatedUserItemsResponseInnerTeamMembership.md) |  | [optional] 
**organization_url_name** | **str** |  | [optional] 
**slide** | **bool** |  | [optional] 

## Example

```python
from qiita.v2.models.get_authenticated_user_items_response_inner import GetAuthenticatedUserItemsResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetAuthenticatedUserItemsResponseInner from a JSON string
get_authenticated_user_items_response_inner_instance = GetAuthenticatedUserItemsResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetAuthenticatedUserItemsResponseInner.to_json())

# convert the object into a dict
get_authenticated_user_items_response_inner_dict = get_authenticated_user_items_response_inner_instance.to_dict()
# create an instance of GetAuthenticatedUserItemsResponseInner from a dict
get_authenticated_user_items_response_inner_from_dict = GetAuthenticatedUserItemsResponseInner.from_dict(get_authenticated_user_items_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


