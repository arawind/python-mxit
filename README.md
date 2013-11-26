# python-mxit

Python wrapper for accessing [Mxit's public APIs](https://dev.mxit.com/docs/restapi)

## Usage

### Authentication

In order to use the Mxit APIs, one needs a *client ID* and *client secret*, which can be obtained by registering your app at [dev.mxit.com](https://dev.mxit.com). With these credentials a client object can be created:

    from mxit import Mxit
    
    client = Mxit(MXIT_CLIENT_ID, MXIT_CLIENT_SECRET)
    
Certain *Mxit API* calls require user authentication. The user would thus need to be redirected to *Mxit's* auth site, where permission will be granted by the user for the requested *scope(s)*. The auth site will then redirect the user back to a specified url with a *code* attached in the query string. This code is then used to obtain the auth token for the following *API* calls. For this flow the url where the auth site needs to redirect back to needs to be specified when instantiating the client:

	from mxit import Mxit
	
	client = Mxit(MXIT_CLIENT_ID, MXIT_CLIENT_SECRET, redirect_url='http://example.org')
	
The auth site url to redirect the user to can be obtained with the following call (where *SCOPE* is the required scope(s) for the API calls to be made):

	client.oauth.auth_url(SCOPE)
	
After the user has granted the desired permissions and the user redirected back the the url as specified, the auth token can be fetched as follows:

	from mxit import Mxit
	
	client = Mxit(MXIT_CLIENT_ID, MXIT_CLIENT_SECRET, redirect_url='http://example.org')
	client.oauth.get_user_token(SCOPE, RECEIVED_CODE)
	
From here the client has access to the api calls allowed by the specified *scope*.

### Messaging API

#### send_message

Send a message (from a Mxit app) to a list of Mxit users

*User authentication required*: **NO**

##### Parameters
* *app_mxit_id* (**required**)
* *target_user_ids* (**required**)
* *message* (**required**)
* *contains_markup* (**optional**)
* *scope* (**optional**)

##### Example

	from mxit import Mxit
	
	client = Mxit(MXIT_CLIENT_ID, MXIT_CLIENT_SECRET)
	
	client.messaging.send_message("example_app_mxit_id", ["mxit_user_id_1", "mxit_user_id_2" ], "This is a test message")

#### send_user_to_user_message

Send a message (from a Mxit user) to a list of Mxit users

*User authentication required*: **YES**

##### Parameters
* *from_user_id* (**required**)
* *target_user_ids* (**required**)
* *message* (**required**)
* *contains_markup* (**optional**)
* *scope* (**optional**)

##### Example

	from mxit import Mxit
	
	client = Mxit(MXIT_CLIENT_ID, MXIT_CLIENT_SECRET, redirect_uri="http://example.org")
	
	client.oauth.get_user_token("message/user", RECEIVED_AUTH_CODE)
	client.messaging.send_user_to_user_message("example_mxit_user_id", ["mxit_user_id_1", "mxit_user_id_2" ], "This is a test user to user message")

### User API

#### get_user_id

Retrieve the Mxit user's internal "user ID"

*User authentication required*: **NO**

##### Parameters
* *mxit_id* (**required**)
* *scope* (**optional**)

##### Example

	from mxit import Mxit
	
	client = Mxit(MXIT_CLIENT_ID, MXIT_CLIENT_SECRET)
	
	user_id = client.users.get_user_id("example_mxit_id")


#### get_status

Retrieve the Mxit user's current status

*User authentication required*: **NO**

##### Parameters
* *mxit_id* (**required**)
* *scope* (**optional**)

##### Example

	from mxit import Mxit
	
	client = Mxit(MXIT_CLIENT_ID, MXIT_CLIENT_SECRET)
	
	status = client.users.get_status("example_mxit_id")

#### set_status

Set the Mxit user's status

*User authentication required*: **YES**

##### Parameters
* *message* (**required**)
* *scope* (**optional**)

##### Example

```python
from mxit import Mxit
	
client = Mxit(MXIT_CLIENT_ID, MXIT_CLIENT_SECRET, redirect_uri="http://example.org")
	
client.oauth.get_user_token("status/write", RECEIVED_AUTH_CODE)
client.users.set_status("Some awesome status")
```

#### get_display_name

Retrieve the Mxit user's display name

*User authentication required*: **NO**

##### Parameters
* *mxit_id* (**required**)
* *scope* (**optional**)

##### Example

	from mxit import Mxit
	
	client = Mxit(MXIT_CLIENT_ID, MXIT_CLIENT_SECRET)
	
	display_name = client.users.get_display_name("example_mxit_id")


#### get_avatar

#### set_avatar

#### delete_avatar

#### get_basic_profile

#### get_full_profile

#### update_profile

#### add_contact

#### get_contact_list

#### get_friend_suggestions

#### get_gallery_folder_list

#### create_gallery_folder

#### delete_gallery_folder

#### rename_gallery_folder

#### delete_gallery_file

#### rename_gallery_file

#### upload_gallery_file

#### get_gallery_item_list

#### get_gallery_file