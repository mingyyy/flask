from hashlib import blake2b

short2long = {'mama': 'www.omneia.com'}
long2short = {'www.omneia.com': 'mama'}


class URL:
    def __init__(self):
        self.long = None
        self.short = None

    def get_short(self, long_url):
        if long_url in long2short:
            return long2short[long_url]
        else:
            self.short = blake2b(key=b'lolie', digest_size = 5)
            self.short.update(long_url.encode())
            short_url = self.short.hexdigest()

            long2short[long_url] = short_url
            short2long[short_url] = long_url

            return short_url

    def get_long(self, short_url):
        if short_url in short2long:
            return short2long[short_url]
        else:
            return "Doesn't exist!"

    def delete_record(self, url):
        if url in short2long:
            del long2short[short2long[url]]
            del short2long[url]
            return "Short URL has been deleted!"
        elif url in long2short:
            del short2long[long2short[url]]
            del long2short[url]
            return "Long URL has been deleted!"
        else:
            return f"Record {url} doesn't exist."


