import os
from requests_oauthlib import OAuth1, OAuth2


class CredManager:

    def __init__(self):
        self.load_credentials_from_environment()

    def load_credentials_from_environment(self):
        self._consumer_key = os.getenv('TWITTER_CONSUMER_KEY')
        self._consumer_secret = os.getenv('TWITTER_CONSUMER_SECRET')
        self._access_token = os.getenv('TWITTER_ACCESS_TOKEN')
        self._access_token_secret = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')

    def get_auth(self):
        return self.__auth

    def set_bearer_token(self, bearer_token):
        self._bearer_token = bearer_token

    def prepare_oauth1(self):
        self.__auth = OAuth1(
            self._consumer_key, self._consumer_secret,
            self._access_token, self._access_token_secret)

    def prepare_oauth2(self):
        self.__auth = OAuth2(token=self._bearer_token)

    def clearCredentials(self):
        self._consumer_key = None
        self._consumer_secret = None
        self._access_token_key = None
        self._access_token_secret = None
        self._bearer_token = None
        self.__auth = None
