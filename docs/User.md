# User


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | 自己紹介文 | 
**facebook_id** | **str** | Facebook ID | 
**followees_count** | **int** | このユーザーがフォローしているユーザーの数 | 
**followers_count** | **int** | このユーザーをフォローしているユーザーの数 | 
**github_login_name** | **str** | GitHub ID | 
**id** | **str** | ユーザーID | 
**items_count** | **int** | このユーザーが qiita.com 上で公開している記事の数 (Qiita Teamでの記事数は含まれません) | 
**linkedin_id** | **str** | LinkedIn ID | 
**location** | **str** | 居住地 | 
**name** | **str** | 設定している名前 | 
**organization** | **str** | 所属している組織 | 
**permanent_id** | **int** | ユーザーごとに割り当てられる整数のID | 
**profile_image_url** | **str** | 設定しているプロフィール画像のURL | 
**team_only** | **bool** | Qiita Team専用モードに設定されているかどうか | 
**twitter_screen_name** | **str** | Twitterのスクリーンネーム | 
**website_url** | **str** | 設定しているWebサイトのURL | 

## Example

```python
from qiita.v2.models.user import User

# TODO update the JSON string below
json = "{}"
# create an instance of User from a JSON string
user_instance = User.from_json(json)
# print the JSON string representation of the object
print(User.to_json())

# convert the object into a dict
user_dict = user_instance.to_dict()
# create an instance of User from a dict
user_from_dict = User.from_dict(user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


