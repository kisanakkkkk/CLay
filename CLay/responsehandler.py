from mitmproxy import http


# from lists import *
# from utility import *
# from config import *

from CLay.lists import *
from CLay.utility import *
from CLay.config import *


class ResponseHandler:
    def __init__(self, flow):
        try:
            self.flow = flow
            self.content_type = contentCheck(self.flow.response.headers)
            self.main()
        except Exception as e:
            print('Error: init responseHandler', e)

    def main(self):
        try:
            # detection
            self.detectResponse()

            # clear informative information
            self.filterResponse()

            # add false informative information
            self.deceptResponse()
        except Exception as e:
            print('Error: main responseHandler', e)

    def detectResponse(self):
        try:
            self.detectLocationRedirection()
        except Exception as e:
            print('Error: detectResponse', e)

    def detectLocationRedirection(self):
        try:
            response_code = self.flow.response.status_code
            if (response_code >= 300 and response_code < 400):
                response_headers = self.flow.response.headers
                if ("Location" in response_headers):
                    target_domain = extract_domain(configure.read_config().get("target"))
                    location_domain = extract_domain(response_headers["Location"])
                    if (target_domain == location_domain):
                        response_headers["Location"] = extract_path_and_more(response_headers["Location"])
                        self.flow.response.text = ""
        except Exception as e:
            print('Error: detectLocationRedirection', e)

    def filterResponse(self):
        try:
            # clear html comments
            if (self.flow.user_preference["filter_comment"] == True):
                self.filterComment()

            # clear informative response headers
            if (self.flow.user_preference["filter_response_header"] == True):
                self.filterResponseHeaders()
        except Exception as e:
            print('Error: filterResponse', e)

    def deceptResponse(self):
        try:
            # add headers
            if  (self.flow.user_preference["add_decoy_header"] == True) and ("headers" in self.flow.deception):
                deception_headers = self.flow.deception["headers"]
                for key, value in deception_headers.items():
                    if isinstance(value, list):
                        value = value[-1]
                    self.addHeader(key, value)

            # add cookies
            if (self.flow.user_preference["add_decoy_cookie"] == True) and ("cookies" in self.flow.deception):
                deception_cookies = self.flow.deception["cookies"]
                for key, value in deception_cookies.items():
                    if isinstance(value, list):
                        value = value[-1]
                    self.addCookie(key, value)

            # add comments
            if ("add_decoy_comment" in self.flow.user_preference):
                if (self.flow.user_preference["add_decoy_comment"]["status"] == True):
                    self.addDecoyComment();
                    # decoy_comment = self.flow.user_preference["add_decoy_comment"]["decoy_comment"]
                    # url_target_paths = self.flow.user_preference["add_decoy_comment"]["url_target_paths"]
                    # assert len(decoy_comment) == len(url_target_paths)
                    # addComment(self.flow, decoy_comment, url_target_paths)

            # replace error page
            if (self.flow.user_preference["error_template_changing"] == True):
                self.templateChanging()
        except Exception as e:
            print('Error: deceptResponse', e)

    def addDecoyComment(self):
        try:
            for c in self.flow.user_preference["add_decoy_comment"]["decoy_comments"]:
                decoy_comment = c["comment"]
                url_target_paths = c["url_target_paths"]
                addComment(self.flow, decoy_comment, url_target_paths)
        except Exception as e:
            print('Error: addDecoyComment', e)


    def addHeader(self, key, value):
        try:
            if key == "Set-Cookie":
                expire = 3600
                others = "; path=/; httponly"

                # if you want to create session, use this
                value = createCookieString(key=value, others=others)

                # if you want to create a cookie with expire date, use this
                # value = createCookieString(key=value, expire=expire, others=others)

                # .add => adding a new header with the same name without overwrite the old one
                self.flow.response.headers.add(key, value)
            else:
                # adding a new header, but will overwrite the old one if any
                self.flow.response.headers[key] = value
        except Exception as e:
            print('Error: addHeader', e)

    def addCookie(self, key, value):
        try:
            request_cookies = self.flow.request.cookies
            response_cookies = self.flow.response.cookies

            if (key not in request_cookies) and (key not in response_cookies):
                cookie_value = createCookieString(key, value=value)
                cookie_header = "Set-Cookie"
                self.addHeader(cookie_header, cookie_value)

        except Exception as e:
            print('Error: addCookie', e)

    # clear all informative header
    def filterResponseHeaders(self):
        try:
            response_headers = self.flow.response.headers

            # get all informative headers from the response headers
            informative_headers = set(response_headers).intersection(DANGER_HEADERS)

            # remove the informative headers from the response headers
            for i in informative_headers:
                # print("DELETED HEADER", i, response_headers[i], sep=": ")
                del response_headers[i]
        except Exception as e:
            print('Error: filterResponseHeaders', e)

    # remove any html comment
    def filterComment(self):
        try:
            if (self.content_type in HTML_CONTENT_TYPES):
                # original pattern
                # pattern = re.compile(r'<!--(.*?)-->|\/\/[^\r\n]*|\/\*(.*?)\*\/', re.DOTALL)

                content = self.flow.response.content.decode('utf-8')
                modified_content = clearCommentInHTML(content)
                self.flow.response.content = modified_content.encode('utf-8')
            elif (self.content_type in JAVASCRIPT_CONTENT_TYPES):
                pass
            elif (self.content_type in CSS_CONTENT_TYPES):
                pass
        except Exception as e:
            print('Error: filterComment', e)

    def templateChanging(self):
        try:
            response_code = self.flow.response.status_code
            # if response code is 401, 403, 404, or 500 return corresponding error page
            if response_code in HTTP_STATUS_CODES:
                self.flow.response = http.Response.make(
                    response_code,
                    responseTemplating(self.flow, response_code),
                    {
                        "Content-Type": "text/html"
                    }
                )
        except Exception as e:
            print('Error: templateChanging', e)
