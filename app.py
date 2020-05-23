import os
from lib import CredManager, TwitterApiClient
from lib.utils import read_credentials_from_file


def main():
    CRED_FILE = 'creds.json'
    CRED_FILE_PATH = os.path.join(
        os.path.dirname(__file__), f'bin/{CRED_FILE}')

    read_credentials_from_file(CRED_FILE_PATH, [
        'consumer_key',
        'consumer_secret',
        'access_token',
        'access_token_secret'
    ])
    cred_manager = CredManager()
    api_client = TwitterApiClient(cred_manager, auth_type=None)

    """
    Navigate to any point in you timeline using the max_id
    How do you know about it your max_id? browse your tweets via APIs
    or you the browser Inspector and see the response, once you
    get hold of one you can just search more, helps you narrow down the
    window you are looking for

    Here I just use the get_user_timeline API to fetch tweets at a specific
    window hinged upon a tweet id as the max_id

    max_id: Returns results with an ID less than (that is, older than)
        or equal to the specified ID.

    https://developer.twitter.com/en/docs/tweets/timelines/api-reference/get-statuses-user_timeline
    """
    response = api_client.get_user_timeline(
        max_id='<your-tweet-max-id>', trim_user=1)
    for status in response:
        text = status['text']
        id = status['id']
        print(id, text)

    """
    This is a typical use case of search and destroy operation -

    1. Search tweets with a text search query string from a max_id
    2. Iterate over the search result to filter out exact ones to operate on
    3. Delete the tweets!
    """
    response = api_client.search_user_statuses(
        q='@YouTube video', max_id='<your-tweet-max-id>')
    for status in response:
        # filter status if contains 'I liked a @YouTube video'
        text = status['text']
        if text.startswith('I liked a @YouTube video'):
            id = status['id']
            print(id, text)
            api_client.delete_user_status(status_id=id)


main()
