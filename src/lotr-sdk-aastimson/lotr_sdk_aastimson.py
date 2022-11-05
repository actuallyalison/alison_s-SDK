import requests
import json


def test(test_name, sdk_call, test_func, expected_value):
    print(test_name+':')
    try:
        if test_func(sdk_call) == expected_value:
            print('\tsuccess!')
        else:
            print('\tfailure!')
            print('\t', sdk_call)
    except Exception as e:
        if isinstance(sdk_call, requests.Response):
            print('\terror:', sdk_call.status_code)
        else:
            print(e)


class LotrSdk:

    def __init__(self, api_token, api_url_base='https://the-one-api.dev/v2/'):
        self.api_url_base = api_url_base
        self.headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer {0}'.format(api_token)}

    def get_api(self, url):
        response = requests.get(self.api_url_base+url, headers=self.headers)
        if response.status_code == 200:
            return json.loads(response.content.decode('utf-8'))
        else:
            return response

    def book(self, book_id=None, get_chapters=False):
        url = 'book'
        if book_id is not None:
            url += '/{0}'.format(book_id)
        if get_chapters:
            url += '/chapter'
        return self.get_api(url)

    def movie(self, movie_id=None, get_quotes=False):
        url = 'movie'
        if movie_id is not None:
            url += '/{0}'.format(movie_id)
        if get_quotes:
            url += '/quote'
        return self.get_api(url)

    def character(self, character_id=None, get_quotes=False):
        url = 'character'
        if character_id is not None:
            url += '/{0}'.format(character_id)
        if get_quotes:
            url += '/quote'
        return self.get_api(url)

    def quote(self, quote_id=None):
        url = 'quote'
        if quote_id is not None:
            url += '/{0}'.format(quote_id)
        return self.get_api(url)

    def chapter(self, chapter_id=None):
        url = 'chapter'
        if chapter_id is not None:
            url += '/{0}'.format(chapter_id)
        return self.get_api(url)


if __name__ == '__main__':

    # For testing beyond the first few tests, you must put your
    # own API token here after registering at: https://the-one-api.dev
    api_token = ''
    book_two = '5cf58077b53e011a64671583'
    movie_three = '5cd95395de30eff6ebccde5d'
    gollum = '5cd99d4bde30eff6ebccfe9e'
    so_it_begins = '5cd96e05de30eff6ebccea9d'
    long_expected_party = '6091b6d6d58360f988133b8b'
    sdk = LotrSdk(api_token)

    test('Get book list',
         sdk.book(),
         lambda x: len(x['docs'][0]['name']) > 0,
         True)

    test('Get book two',
         sdk.book(book_two),
         lambda x: x['docs'][0]['name'],
         'The Two Towers')

    test('Get unknown url',
         sdk.get_api('badurl'),
         lambda x: x.status_code,
         404)

    # These tests will only be possible to run with an api token:
    if len(api_token) > 0:

        test('Get chapters for book',
             sdk.book(book_id=book_two, get_chapters=True),
             lambda x: len(x['docs'][0]['chapterName'])>0,
             True)

        test('Get movies',
             sdk.movie(),
             lambda x: len(x['docs'][0]['name'])>0,
             True)

        test('Get movie',
             sdk.movie(movie_id=movie_three),
             lambda x: x['docs'][0]['name'],
             'The Return of the King')

        test('Get movie quotes',
             sdk.movie(movie_id=movie_three, get_quotes=True),
             lambda x: len(x['docs']) > 100,
             True)

        test('Get characters',
             sdk.character(),
             lambda x: len(x['docs'][0]['name']) > 0,
             True)

        test('Get character',
             sdk.character(character_id=gollum),
             lambda x: x['docs'][0]['name'],
             'Gollum')

        test('Get character quotes',
             sdk.character(character_id=gollum, get_quotes=True),
             lambda x: len(x['docs']) > 0,
             True)

        test('Get quotes',
             sdk.quote(),
             lambda x: len(x['docs'][0]['dialog']) > 0,
             True)

        test('Get quote',
             sdk.quote(quote_id=so_it_begins),
             lambda x: x['docs'][0]['dialog'],
             'So it begins.')
        
        test('Get chapters',
             sdk.chapter(),
             lambda x: len(x['docs'][0]['chapterName']) > 0,
             True)

        test('Get chapter',
             sdk.chapter(chapter_id=long_expected_party),
             lambda x: x['docs'][0]['chapterName'],
             'A Long-expected Party')
