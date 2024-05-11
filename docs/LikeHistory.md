# LikeHistory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** | データが作成された日時 | 
**user** | [**User**](User.md) |  | 

## Example

```python
from qiita.v2.models.like_history import LikeHistory

# TODO update the JSON string below
json = "{}"
# create an instance of LikeHistory from a JSON string
like_history_instance = LikeHistory.from_json(json)
# print the JSON string representation of the object
print(LikeHistory.to_json())

# convert the object into a dict
like_history_dict = like_history_instance.to_dict()
# create an instance of LikeHistory from a dict
like_history_from_dict = LikeHistory.from_dict(like_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


