import json
import time
import regex
import random
import datetime
import os
import html
from mitmproxy import http
from jinja2 import Template

# from lists import *

from CLay.lists import *



def initStaticRandom():
    try:
        current_date = datetime.datetime.now()
        seed_value = current_date.year * 100 + current_date.month
        random.seed(seed_value)
    except Exception as e:
        print('Error: initStaticRandom', e)


def initRandom():
    try:
        random.seed(time.time())
    except Exception as e:
        print('Error: initRandom', e)


def contentCheck(header):
    try:
        return header['Content-Type'].split(';')[0]
    except:
        return None


def addComment(flow, comment, url_target_paths):
    request_path = flow.request.path
    comment = html.escape(comment)
    try:
        for target_path in url_target_paths:
            location_regex = regex.compile(target_path)
            match = location_regex.match(request_path)
            if match:
                try:
                    if "Content-Type" in flow.response.headers:
                        content_type = flow.response.headers["Content-Type"]
                        content_type = content_type.split(';')[0]
                        if (content_type in HTML_CONTENT_TYPES):
                            flow.response.content += (f"<!-- {comment} -->".encode())
                        elif (content_type in JAVASCRIPT_CONTENT_TYPES):
                            flow.response.content += (f"\n// {comment} \n".encode())
                        
                        #prevent multiple comment adding
                        return
                except Exception as e:
                    print('Error: addComment', e)
    except regex._regex_core.error as r:
        print('Error: Regex path error', r)

def clearCommentInHTML(content):
    # clear html comment (<!-- -->) in html file but not clear it if the comment is inside style tag
    pattern = regex.compile(r'(?<!<style.*?>.*?)<!--(.*?)-->|(?<=<style.*?>.*?)(?<=<\/style.*?>.*?)<!--(.*?)-->', flags=regex.DOTALL)
    modified_content = pattern.sub('', content)
    
    # clear js comment in html file (/* */)
    # pattern = regex.compile(r'(?<=<script.*?>.*?)(?<!<\/script>)<!--(.*?)-->(?=.*?<\/script>)', flags=regex.DOTALL)
    # modified_content = pattern.sub('', modified_content)

    # clear js comment in html file (//)
    
    # Remove single-line comments
    # pattern1 = regex.compile(r'\/\/.*?$', flags=regex.MULTILINE)

    # Remove multiline comments
    # pattern2 = regex.compile(r'\/\*.*?\*\/', flags=regex.DOTALL)

    # modified_content = pattern2.sub('', pattern1.sub('', modified_content))

    # clear css comemnt in html file (/* */)

    return modified_content
    pass


def clearCommentInJavascript():
    pass


def clearCommentInCSS():
    pass


def createCookieString(key, value=None, expire=None, others=None):
    try:
        if (expire):
            # Set the expire time in seconds
            expire_time = datetime.datetime.utcnow() + datetime.timedelta(seconds=expire)

            # Format the expire time as a string
            expire_str = expire_time.strftime("%a, %d %b %Y %H:%M:%S GMT")

        if (key and not value):
            key, value = key.split('=', 1)

        cookie_value = key + "=" + value

        if (expire):
            cookie_value = cookie_value + "; expires=" + expire_str + "; Max-Age=" + str(expire)

        if (others):
            cookie_value = cookie_value + others

        return cookie_value
    except Exception as e:
        print('Error: createCookieString', e)


def statusCodeTampering(flow, response_code=None):
    try:
        if response_code is None:
            response_code = random.choice(HTTP_STATUS_CODES)

        flow.response = http.Response.make(
            response_code,
            responseTemplating(flow, response_code),
            {
                "Content-Type": "text/html",
            }
        )
    except Exception as e:
        print('Error: statusCodeTampering', e)


def responseTemplating(flow, status):
    try:
        # read html and json template
        deception_html_path = flow.deception["path"]["html"]
        if isinstance(deception_html_path, list):
            deception_html_path = deception_html_path[-1]
        deception_json_path = flow.deception["path"]["json"]
        if isinstance(deception_json_path, list):
            deception_json_path = deception_json_path[-1]

        with open(os.path.join(os.path.dirname(__file__), deception_html_path), 'r') as f1:
            template = Template(f1.read())
        with open(os.path.join(os.path.dirname(__file__), deception_json_path), 'r') as f2:
            codes = json.loads(f2.read())
        statuscode = str(status)
        try:
            val = codes[statuscode]
        except:
            val = codes["404"]
        variables = {
            'title': val['title'],
            'header': val['header'],
            'description': val['description']
        }
        return template.render(variables)
    except Exception as e:
        print('Error: responseTemplating', e)

def extract_domain(url):
    pattern = regex.compile(r'https?://([^/]+)')
    match = pattern.match(url)
    
    if match:
        return match.group(1)
    else:
        return None
    
def extract_path_and_more(url):
    pattern = regex.compile(r'https?://[^/]+(.+)')
    match = pattern.match(url)
    
    if match:
        return match.group(1)
    else:
        return None