from config import encoding_api_user_id, encoding_api_key, encoding_url, s3_url
import re
import json
import urllib
import httplib
import urlparse

def transcode(filename, notify_url, error_url, upload_url):
    data = {'query': create_query(filename, notify_url, error_url, upload_url)}
    url = urlparse.urlsplit(encoding_url)
    connection = httplib.HTTPConnection(url.netloc)
    headers = {'Content-type': 'application/x-www-form-urlencoded'}
    params = urllib.urlencode({'json': json.dumps(data)})
    connection.request('POST', '/', params, headers)
    r = connection.getresponse()
    return r.read()

def create_query(filename, notify_url, error_url, upload_url):
    query = {'userid': encoding_api_user_id,
             'userkey': encoding_api_key,
             'action': 'addmedia',
             'source': [s3_url + 'uploads/' + filename],
             'notify': notify_url,
             'notify_upload': upload_url,
             'notify_format': 'json',
             'instant': 'no',
             'format': {}}
    newfile = re.sub('\.[^.]+$', '.webm', filename)
    format_webm = {
            'output': 'webm',
            'keep_aspect_ratio': 'yes',
            'destination': s3_url + 'videos/' + newfile + '?acl=public-read'
            }
    query['format'] = [format_webm]
    return query

