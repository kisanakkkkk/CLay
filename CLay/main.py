import asyncio
import argparse
# import sys
# import importlib
from mitmproxy import http, options
from mitmproxy.tools.dump import DumpMaster

# from config import *
# from requesthandler import *
# from responsehandler import *

from CLay.config import *
from CLay.requesthandler import RequestHandler
from CLay.responsehandler import ResponseHandler
from CLay.generate import *

class Proxy:
    def __init__(self, master):
        try:
            self.master = master
            self.deception_data = configure.get_deception_data()
            self.user_preference = configure.get_user_preference()
        except Exception as e:
            print('Error: init main', e)

    def request(self, flow: http.HTTPFlow) -> None:
        try:
            flow.deception = self.deception_data
            flow.user_preference = self.user_preference

            # importlib.reload(sys.modules['requesthandler'])
            RequestHandler(flow)
        except Exception as e:
            print('Error: request', e)

    def response(self, flow: http.HTTPFlow) -> None:
        try:
            # importlib.reload(sys.modules['responsehandler'])
            ResponseHandler(flow)
        except Exception as e:
            print('Error: response', e)


async def startProxy(lhost, lport, target):
    try:
        proxyMode = ['reverse:' + target]
        opts = options.Options(
            listen_host=lhost,
            listen_port=lport,
            mode=proxyMode,
            ssl_insecure=True
        )

        master = DumpMaster(
            opts,
            with_termlog=False,
            with_dumper=False
        )

        block_addon = master.addons.get("block")
        master.addons.remove(block_addon)
        
        master.addons.add(Proxy(master))
        print(f'[+] Proxy starting for {lhost}:{lport}')
        await master.run()
        return master
    except Exception as e:
        print('Error: startProxy', e)


def main():
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('-c', '--config', dest='config', type=str, help='run proxy based on JSON configuration file')
        parser.add_argument('-g', '--generate', dest='generate', action='store_true', help='generate JSON file')
        args = parser.parse_args()
        if args.config and args.config != '':
            try:
                configure.set_config(args.config)
                lhost = configure.read_config().get("listen_host")
                lport = configure.read_config().get("listen_port")
                target = configure.read_config().get("url_target")
                asyncio.run(startProxy(lhost=lhost, lport=lport, target=target))
            except Exception as e:
                print('Error: Unable to load or parse config file', e)
                exit()
        elif args.generate:
            generateConfig()
    except KeyboardInterrupt:
        print(f'[-] KeyboardInterrupt triggered')
    except Exception as e:
        print('Error: main', e)


if __name__ == '__main__':
    main()
