# GetAuthenticatedUserItemsResponseInnerUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**facebook_id** | **str** |  | [optional] 
**followees_count** | **int** |  | [optional] 
**followers_count** | **int** |  | [optional] 
**github_login_name** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**items_count** | **int** |  | [optional] 
**linkedin_id** | **str** |  | [optional] 
**location** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**organization** | **str** |  | [optional] 
**permanent_id** | **int** |  | [optional] 
**profile_image_url** | **str** |  | [optional] 
**team_only** | **bool** |  | [optional] 
**twitter_screen_name** | **str** |  | [optional] 
**website_url** | **str** |  | [optional] 

## Example

```python
from qiita.v2.models.get_authenticated_user_items_response_inner_user import GetAuthenticatedUserItemsResponseInnerUser

# TODO update the JSON string below
json = "{}"
# create an instance of GetAuthenticatedUserItemsResponseInnerUser from a JSON string
get_authenticated_user_items_response_inner_user_instance = GetAuthenticatedUserItemsResponseInnerUser.from_json(json)
# print the JSON string representation of the object
print(GetAuthenticatedUserItemsResponseInnerUser.to_json())

# convert the object into a dict
get_authenticated_user_items_response_inner_user_dict = get_authenticated_user_items_response_inner_user_instance.to_dict()
# create an instance of GetAuthenticatedUserItemsResponseInnerUser from a dict
get_authenticated_user_items_response_inner_user_from_dict = GetAuthenticatedUserItemsResponseInnerUser.from_dict(get_authenticated_user_items_response_inner_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


