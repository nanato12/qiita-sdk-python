# IssueAccessTokenRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** | 登録されたAPIクライアントを特定するためのID | 
**client_secret** | **str** | 登録されたAPIクライアントを認証するための秘密鍵 | 
**code** | **str** | リダイレクト用のURLに付与された、アクセストークンと交換するための文字列 | 

## Example

```python
from qiita.v2.models.issue_access_token_request import IssueAccessTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IssueAccessTokenRequest from a JSON string
issue_access_token_request_instance = IssueAccessTokenRequest.from_json(json)
# print the JSON string representation of the object
print(IssueAccessTokenRequest.to_json())

# convert the object into a dict
issue_access_token_request_dict = issue_access_token_request_instance.to_dict()
# create an instance of IssueAccessTokenRequest from a dict
issue_access_token_request_from_dict = IssueAccessTokenRequest.from_dict(issue_access_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


