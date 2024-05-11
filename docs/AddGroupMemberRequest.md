# AddGroupMemberRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identities** | **List[str]** | メンバーのユーザーIDかチームに登録しているemailアドレスの一覧 | 

## Example

```python
from qiita.v2.models.add_group_member_request import AddGroupMemberRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddGroupMemberRequest from a JSON string
add_group_member_request_instance = AddGroupMemberRequest.from_json(json)
# print the JSON string representation of the object
print(AddGroupMemberRequest.to_json())

# convert the object into a dict
add_group_member_request_dict = add_group_member_request_instance.to_dict()
# create an instance of AddGroupMemberRequest from a dict
add_group_member_request_from_dict = AddGroupMemberRequest.from_dict(add_group_member_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


