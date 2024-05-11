# IssueAccessTokenResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** | 登録されたAPIクライアントを特定するためのID | 
**scopes** | **List[str]** | アクセストークンに許された操作の一覧 | 
**token** | **str** | アクセストークンを表現する文字列 | 

## Example

```python
from qiita.v2.models.issue_access_token_response import IssueAccessTokenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IssueAccessTokenResponse from a JSON string
issue_access_token_response_instance = IssueAccessTokenResponse.from_json(json)
# print the JSON string representation of the object
print(IssueAccessTokenResponse.to_json())

# convert the object into a dict
issue_access_token_response_dict = issue_access_token_response_instance.to_dict()
# create an instance of IssueAccessTokenResponse from a dict
issue_access_token_response_from_dict = IssueAccessTokenResponse.from_dict(issue_access_token_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


