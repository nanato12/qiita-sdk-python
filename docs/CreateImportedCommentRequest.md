# CreateImportedCommentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** | コメントの内容を表すMarkdown形式の文字列 | 
**user_id** | **str** | ユーザーID | 
**created_at** | **str** | データが作成された日時 | [optional] 
**updated_at** | **str** | データが最後に更新された日時 | [optional] 

## Example

```python
from qiita.v2.models.create_imported_comment_request import CreateImportedCommentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateImportedCommentRequest from a JSON string
create_imported_comment_request_instance = CreateImportedCommentRequest.from_json(json)
# print the JSON string representation of the object
print(CreateImportedCommentRequest.to_json())

# convert the object into a dict
create_imported_comment_request_dict = create_imported_comment_request_instance.to_dict()
# create an instance of CreateImportedCommentRequest from a dict
create_imported_comment_request_from_dict = CreateImportedCommentRequest.from_dict(create_imported_comment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


