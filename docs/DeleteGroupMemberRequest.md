# DeleteGroupMemberRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identities** | **List[str]** | メンバーのユーザーIDかチームに登録しているemailアドレスの一覧 | 

## Example

```python
from qiita.v2.models.delete_group_member_request import DeleteGroupMemberRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteGroupMemberRequest from a JSON string
delete_group_member_request_instance = DeleteGroupMemberRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteGroupMemberRequest.to_json())

# convert the object into a dict
delete_group_member_request_dict = delete_group_member_request_instance.to_dict()
# create an instance of DeleteGroupMemberRequest from a dict
delete_group_member_request_from_dict = DeleteGroupMemberRequest.from_dict(delete_group_member_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


