# Group

Qiita Teamのグループを表します。

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** | データが作成された日時 | 
**description** | **str** | グループの詳細を表します。 | 
**name** | **str** | グループに付けられた表示用の名前を表します。 | 
**private** | **bool** | 非公開グループかどうかを表します。 | 
**updated_at** | **str** | データが最後に更新された日時 | 
**url_name** | **str** | グループのチーム上での一意な名前を表します。 | 

## Example

```python
from qiita.v2.models.group import Group

# TODO update the JSON string below
json = "{}"
# create an instance of Group from a JSON string
group_instance = Group.from_json(json)
# print the JSON string representation of the object
print(Group.to_json())

# convert the object into a dict
group_dict = group_instance.to_dict()
# create an instance of Group from a dict
group_from_dict = Group.from_dict(group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


