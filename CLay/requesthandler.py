# from lists import *
# from utility import *

from CLay.lists import *
from CLay.utility import *



class RequestHandler:
    def __init__(self, flow):
        try:
            self.flow = flow
            self.main()
        except Exception as e:
            print('Error: init requestHandler', e)

    def main(self):
        try:
            # detection
            self.detectRequest()

            # clear informative information
            self.filterRequest()

            # add false informative information
            self.deceptRequest()
        except Exception as e:
            print('Error: main requestHandler', e)

    def detectRequest(self):
        try:
            if (self.flow.user_preference["filter_request_by_user_agent"] == True):
                self.filterRequestByUserAgent()
            elif (self.flow.user_preference["filter_request_by_user_agent"] is not True or False):
                print('Error value of filter_request_by_user_agent') 
        except Exception as e:
            print('Error: detectRequest', e)

    def filterRequest(self):
        try:
            pass
        except Exception as e:
            print('Error: filterRequest', e)

    def deceptRequest(self):
        try:
            pass
        except Exception as e:
            print('Error: deceptRequest', e)

    def filterRequestByUserAgent(self):
        try:
            client_ip = self.flow.client_conn.peername[0]
            user_agent = self.flow.request.headers.get("User-Agent").lower()

            # check if there is user_agent in the request
            if user_agent:
                # Check if any substring exists in the input string from a list
                found = any(substring in user_agent for substring in DANGER_USER_AGENTS)

                if found:
                    # if detected dangerous user agent, return 200 status code and 404 error page
                    statusCodeTampering(self.flow, 200)
                    print(f"IP: {client_ip}, reason: Invalid User Agent")
        except Exception as e:
            print('Error: filterRequestByUserAgent', e)
