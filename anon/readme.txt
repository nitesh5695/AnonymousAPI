Customer Api jwt Authentication
For register a user: 
Endpoint: http://127.0.0.1:7001/register/
For register a user ,user should have to post  following data with captcha client_key and secret_key
Example:-
{
	"username":"prince.singh8756@gmail.com",  
	"email":"nitesh.singh5695@gmail.com",
	"password":"prince@8756",
	"gst_no":"gst12345"
               “captcha”:{“secret”:”---secret_key---“,
                		“response”:  “---client key—which are get by posting form data”
              	}
}
If   incase gst_no. is not post .then user can’t register.

Endpoint:-  http://127.0.0.1:7001/customerapi/
For post data: 
Fields=[‘name’,’mobile’,’customer_type’ ]
All above fields  are required to post data.
Get method:- To get all data
PATCH  method:-
“Id”  must be send to update data.
Above methods will only work if user have JWT token.
Process to get token.
Method=”post”
Username=’admin’ password=’admin’
Endpoint:- http://127.0.0.1:7001/gettoken/
For getting token user should have to post  “username” and “password”  in body.if  user is existed then user get
Access token and refresh token in response.

If access token is expired and user have refresh token then user can get new token by following endpoint
Endpoint:- http://127.0.0.1:7001/refreshtoken/
Method=Post
Body data:-
“refresh” : ”your refresh  token”
In response:-
User will get access token and refresh token
To verify token:-
Endpoint=:- http://127.0.0.1:7001/verifytoken/
Method=Post
Body data:-
“token” : ”your access  token”
For Anonymous User
To get token:-
Endpoint  :-  http://127.0.0.1:7001/gettoken_anonymous/
Method =post
For anonymous user no need to post any data to get token.
To refresh Token:-
Endpoint :-  http://127.0.0.1:7001/refreshtoken_anonymous/
Method=post
Body :-
{
“refresh”:”your_refresh_token”
}
Accessible endpoint for anonymous user :-
Endpoint:- http://127.0.0.1:7001/access/
In above endpoint  anonymous user can  use endpoint  to get data only. but registered  user can done all methods eg.   “get”,”post” etc

Permissions  for anonymous user:-
Anonymous user have only readonly permission, so only get method will  work for  user. 
In the same endpoints  ,Register user have all permissions but  anonymous user have only read permission.
There is also difference in tokens of registered and  anonymous user.
Life time of registered user is more than of anonymous user.
Note:-In the  whole api, token generation ,authentication and permissions are handled Manually .
But for registered user   rest_framework.simplejwt    is used ,









