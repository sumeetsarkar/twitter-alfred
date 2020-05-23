# Twitter Alfred

> Simple utility using Twitter APIs

## Supported Authentication modes

1. Client Credentials
2. App only authentication

## Twitter APIs implemented

1. Get user timeline
    /1.1/statuses/user_timeline.json

2. Search user tweets
    /1.1/search/tweets.json

3. Delete user tweets
    /1.1/statuses/destroy/

## Sample Program output

![output screenshot](/resources/screenshots/sample_program_output.png)


## FAQs

**Q. Credential file?**
<br/>
**Ans:** In the usage of the alfred API in the app.py file - I assume you to
store a credentials file at `bin/creds.json` at project root - which is a JSON
with following keys
```
{
    "consumer_key": "<your-consumer-key>",
    "consumer_secret": "<your-consumer-secret>",
    "access_token": "<your-access-token>",
    "access_token_secret": "<your-access-token-secret>"
}
```
Create an app in https://developers.twitter.com/ and get the above keys
Read the docs for more information - https://developer.twitter.com/en/docs


**Q. Will I be implementing more such Twitter APIs?**
<br/>
**Ans:** Not really - I just wanted to delete some older tweets from my twitter
account - I had 500+ old tweets at different times about the video I liked in
youtube (somehow it was left enabled in youtube app and I did not remember).
Going down the memory lane to delete each one by one using Twitter was painstakingly
slow and soul wrenching. And hence I thought of writitng a quick python script
to get the work done.
