import re
import logging
import logging.config

import mechanicalsoup

from conf.access_key import access_key
from conf.settings import TEST_LOGGING
from helper.utils import dump_func_name

logging.config.dictConfig(TEST_LOGGING)
logger = logging.getLogger(__name__)


class Kata(object):
    def __init__(self):
        self.browser = mechanicalsoup.Browser(soup_config={"features":"lxml"})

        self.set_access_key()

    @dump_func_name(logger)
    def set_access_key(self):
        self.browser.session.cookies.set('Authorization', access_key)

    @dump_func_name(logger)
    def set_code_challenge(self, challenge_url):
        challenge = self.get_cleaned_challenge(challenge_url)
        logger.info('challenge: {}'.format(challenge))
        # challenge = 'length-of-the-line-segment'
        code_challenge_url_format = 'https://www.codewars.com/api/v1/code-challenges/{challenge}'
        try:
            self.challenge_json = self.browser.get(code_challenge_url_format.format(challenge=challenge)).json()
            logger.info('challenge_json: {}'.format(self.challenge_json))
        except Exception as e:
            logger.error('no challenge_json', exc_info=True)

    @dump_func_name(logger)
    def get_cleaned_challenge(self, challenge_url):
        if 'http' in challenge_url:
            # Example: http://www.codewars.com/kata/length-of-the-line-segment/python
            # Extract: length-of-the-line-segment
            return re.search(r'kata/([^/]+)/', challenge_url).group(1)
        return challenge_url

    @dump_func_name(logger)
    def get_description_in_code_challenge(self, challenge_url, key_='description'):
        self.set_code_challenge(challenge_url)
        return self.challenge_json[key_]