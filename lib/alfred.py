import base64
import requests
from abc import ABC
from urllib.parse import quote_plus


class TwitterAuthApiClient(ABC):

    HOST = 'https://api.twitter.com'
    OAUTH2_TOKEN = '/oauth2/token'

    def __init__(self, cred_manager, auth_type='None'):
        self.cred_manager = cred_manager
        if auth_type == 'client_credentials':
            self.cred_manager.fetch_app_only_auth_token()
            self.cred_manager.prepare_oauth2()
        else:
            self.cred_manager.prepare_oauth1()

    def url(self, endpoint):
        return f'{self.HOST}{endpoint}'

    def fetch_app_only_auth_token(self):
        key = quote_plus(self.cred_manager._consumer_key)
        secret = quote_plus(self.cred_manager._consumer_secret)
        bearer_token = base64.b64encode(
            '{}:{}'.format(key, secret).encode('utf8'))
        post_headers = {
            'Authorization': 'Basic {0}'.format(bearer_token.decode('utf8')),
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
        }
        post_data = {'grant_type': 'client_credentials'}
        res = requests.post(
            url=self.url(self.OAUTH2_TOKEN),
            data=post_data,
            headers=post_headers)
        self.cred_manager.set_bearer_token(res.json())


class TwitterApiClient(TwitterAuthApiClient):

    GET_USER_TIMELINE = '/1.1/statuses/user_timeline.json'
    DELETE_USER_STATUS = '/1.1/statuses/destroy/'
    SEARCH_USER_STATUSES = '/1.1/search/tweets.json'

    def __init__(self, cred_manager, auth_type='None'):
        super().__init__(cred_manager, auth_type)

    def get_user_timeline(
        self, exclude_replies=1, include_rts=0, trim_user=1,
        count=200, since_id=None, max_id=None
    ):
        """
        https://developer.twitter.com/en/docs/tweets/timelines/api-reference/get-statuses-user_timeline
        """
        query_params = 'exclude_replies={0}&include_rts={1}' \
            + '&trim_user={2}&count={3}'
        query_params = query_params.format(
            exclude_replies, include_rts, trim_user, count)

        query_params += f'&since_id={since_id}' if since_id else ''
        query_params += f'&max_id={max_id}' if max_id else ''

        endpoint = f'{self.GET_USER_TIMELINE}?{query_params}'
        url = self.url(endpoint)

        res = requests.get(
            url=url,
            auth=self.cred_manager.get_auth())
        content = res.json()
        return content

    def search_user_statuses(
        self, q, count=100, since_id=None, max_id=None
    ):
        """
        https://developer.twitter.com/en/docs/tweets/search/guides/standard-operators
        """
        query_params = 'q={0}&count={1}'.format(quote_plus(q), count)
        query_params += f'&since_id={since_id}' if since_id else ''
        query_params += f'&max_id={max_id}' if max_id else ''

        endpoint = f'{self.GET_USER_TIMELINE}?{query_params}'
        url = self.url(endpoint)

        res = requests.get(
            url=url,
            auth=self.cred_manager.get_auth())
        content = res.json()
        return content

    def delete_user_status(self, status_id):
        """
        https://developer.twitter.com/en/docs/tweets/post-and-engage/api-reference/post-statuses-destroy-id
        """
        url = self.url(f'{self.DELETE_USER_STATUS}{status_id}.json')
        res = requests.post(
            url=url,
            auth=self.cred_manager.get_auth())
        content = res.json()
        return content
