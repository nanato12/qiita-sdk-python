# ItemTag


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | タグ名 | 
**versions** | **List[str]** | バージョン | 

## Example

```python
from qiita.v2.models.item_tag import ItemTag

# TODO update the JSON string below
json = "{}"
# create an instance of ItemTag from a JSON string
item_tag_instance = ItemTag.from_json(json)
# print the JSON string representation of the object
print(ItemTag.to_json())

# convert the object into a dict
item_tag_dict = item_tag_instance.to_dict()
# create an instance of ItemTag from a dict
item_tag_from_dict = ItemTag.from_dict(item_tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


