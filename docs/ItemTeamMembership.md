# ItemTeamMembership


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | チームに登録しているユーザー名 | 

## Example

```python
from qiita.v2.models.item_team_membership import ItemTeamMembership

# TODO update the JSON string below
json = "{}"
# create an instance of ItemTeamMembership from a JSON string
item_team_membership_instance = ItemTeamMembership.from_json(json)
# print the JSON string representation of the object
print(ItemTeamMembership.to_json())

# convert the object into a dict
item_team_membership_dict = item_team_membership_instance.to_dict()
# create an instance of ItemTeamMembership from a dict
item_team_membership_from_dict = ItemTeamMembership.from_dict(item_team_membership_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


