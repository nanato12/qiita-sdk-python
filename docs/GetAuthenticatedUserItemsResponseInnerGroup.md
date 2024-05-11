# GetAuthenticatedUserItemsResponseInnerGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**private** | **bool** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**url_name** | **str** |  | [optional] 

## Example

```python
from qiita.v2.models.get_authenticated_user_items_response_inner_group import GetAuthenticatedUserItemsResponseInnerGroup

# TODO update the JSON string below
json = "{}"
# create an instance of GetAuthenticatedUserItemsResponseInnerGroup from a JSON string
get_authenticated_user_items_response_inner_group_instance = GetAuthenticatedUserItemsResponseInnerGroup.from_json(json)
# print the JSON string representation of the object
print(GetAuthenticatedUserItemsResponseInnerGroup.to_json())

# convert the object into a dict
get_authenticated_user_items_response_inner_group_dict = get_authenticated_user_items_response_inner_group_instance.to_dict()
# create an instance of GetAuthenticatedUserItemsResponseInnerGroup from a dict
get_authenticated_user_items_response_inner_group_from_dict = GetAuthenticatedUserItemsResponseInnerGroup.from_dict(get_authenticated_user_items_response_inner_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


