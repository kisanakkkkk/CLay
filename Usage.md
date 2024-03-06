# Usage
```
usage: CLay [-h] [-c CONFIG] [-ce CERTS] [-d DOMAIN] [-g]

options:
  -h, --help                    show this help message and exit
  -c CONFIG, --config CONFIG    run proxy based on JSON configuration file
  -ce CERTS, --certs CERTS      specify path to certificate file (optional)
  -d DOMAIN, --domain DOMAIN    TLS domain (default=*)
  -g, --generate                generate JSON file
```

## Configuration detail
### config.json
```
{
  "listen_host": "0.0.0.0",
  "listen_port": 5000,
  "url_target": "http://example.com",
  "decoy_technology": {
    "server": "Nginx",
    "framework": "Microsoft ASP.NET"
  },
  "user_preference": {
    "filter_request_by_user_agent": true,
    "filter_comment": true,
    "filter_response_header": true,
    "error_template_changing": true,
    "add_decoy_header": true,
    "add_decoy_cookie": true,
    "add_decoy_comment": {
      "status": true,
      "decoy_comments": [
        {
          "comment": "dummy comment goes here",
          "url_target_paths": [
            ".*/"
          ]
        }
      ]
    }
  }
}
```
- listen_host = Host where you access your CLay-ed website.

- listen_port = Port for accessing your CLay-ed website.

- url_target =  Original website for CLay integration.

- decoy_technology-server = Server technology your website appears to use.

- decoy_technology-framework = Web framework your website appears to use.

---
### Feature - Request Filtering by User-Agent
| Before                                              | After                                              |
| ---------------------------------------------------- | ---------------------------------------------------- |
| ![Image 1](https://github.com/kisanakkkkk/CLay/assets/70153248/f981ccd9-211c-4911-acd1-6f1c6187b25b)   | ![Image 2](https://github.com/kisanakkkkk/CLay/assets/70153248/37f57021-6475-49b8-88f1-2e7cced916cb)   |

Determine whether the request originates from a dangerous (tools-based) user agent. If detected, CLay will respond with a false 200 OK status code while sending a 'not found' error page in the response body, confusing the attackers.

```
"filter_request_by_user_agent": true
```
See [this](https://raw.githubusercontent.com/mitchellkrogza/apache-ultimate-bad-bot-blocker/master/Apache_2.2/custom.d/globalblacklist.conf) as references.

---
### Feature - HTML Comment Filtering
| Before                                              | After                                              |
| ---------------------------------------------------- | ---------------------------------------------------- |
| ![Image 1](https://github.com/kisanakkkkk/CLay/assets/70153248/451dd1b1-2991-4608-97fe-413a313aa211)   | ![Image 2](https://github.com/kisanakkkkk/CLay/assets/70153248/0a89ff89-1e1b-4e3a-b3f2-2452b7df64ff)   |

Automatically remove all HTML comments, preventing unnecessary information leakage inside the webpage source codes.

```
"filter_comment": true,
```

---
### Feature - Informative Response Header Filtering
| Before                                              | After                                              |
| ---------------------------------------------------- | ---------------------------------------------------- |
| ![Image 1](https://github.com/kisanakkkkk/CLay/assets/70153248/c00d4621-35cb-46c2-bce7-afb090d14f51)   | ![Image 2](https://github.com/kisanakkkkk/CLay/assets/70153248/5b74d3af-99f0-41c3-bf2a-5e9de773266d)   |

Determine whether the application’s response contains informative headers, such as the server banner. If detected, CLay will remove the response header seamlessly.

```
"filter_response_header": true
```

---
### Feature - Error Template Changing
| Before                                              | After                                              |
| ---------------------------------------------------- | ---------------------------------------------------- |
| ![Image 1](https://github.com/kisanakkkkk/CLay/assets/70153248/fed651bf-ee5e-4583-b6fd-c17afbfda91f)   | ![Image 2](https://github.com/kisanakkkkk/CLay/assets/70153248/7405c4ba-e471-4489-bcfd-1192dfe55d46)   |

CLay will replace the application’s default error pages with the other framework's error pages to prevent attackers from gathering essential information from the error page templates.

```
"error_template_changing": true
```

---
### Feature - Adding Decoy Informative Response Headers
| Before                                              | After                                              |
| ---------------------------------------------------- | ---------------------------------------------------- |
| ![Image 1](https://github.com/kisanakkkkk/CLay/assets/70153248/dd367886-11d1-450f-95ee-09e0dbe2b39e)   | ![Image 2](https://github.com/kisanakkkkk/CLay/assets/70153248/01c1311a-870c-4ef5-bf86-a44df08c80bb)   |

CLay allows users to add decoy informative headers, such as the fake server banner to potentially mislead attackers engaged in reconnaissance.

```
"add_decoy_header": true
```

---
### Feature - Adding Decoy Cookies
| Before                                              | After                                              |
| ---------------------------------------------------- | ---------------------------------------------------- |
| ![Image 1](https://github.com/kisanakkkkk/CLay/assets/70153248/33e2c1bf-167d-4279-a101-1844e444cb3d)   | ![Image 2](https://github.com/kisanakkkkk/CLay/assets/70153248/643ead9f-e403-4a5a-97d8-a8c555c57c6a)   |

CLay allows users to add decoy cookies to make it difficult for attackers to determine the actual framework and technology used.

```
"add_decoy_cookie": true
```

---
### Feature - Adding Dummy HTML Comments
| Before                                              | After                                              |
| ---------------------------------------------------- | ---------------------------------------------------- |
| ![Image 1](https://github.com/kisanakkkkk/CLay/assets/70153248/b2ef67ef-edce-4ccb-b4b1-819b3880e236)   | ![Image 2](https://github.com/kisanakkkkk/CLay/assets/70153248/fad41b5e-5a0b-467b-b106-0e3a4be6bc27)   |

CLay allows users to add dummy HTML comments in multiple paths to mislead attackers engaged in reconnaissance, throwing them into a wild goose chase. For example, adding fake credentials and observing who attempts to log in.
```
"add_decoy_comment": {
    "status": true,
    "decoy_comments": [
        {
            "comment": "Dummy comment goes here",
            "url_target_paths": [".*/login/", ".*/test/"]
        },
        {
            "comment": "here's the decoy comment",
            "url_target_paths": [".*/signup/"]
        }
    ]
}
```
- status = determine whether you want to use this feature or not

- comment = decoy comment(s) you want to put on your website

- url_target_paths = specific page you want to put your decoy comment, specify with regex.

## What Changes From My Website?
CLay modifies response headers to check and remove server banners, removing comment tags from response body, and replace entire response body for response with error status code (400, 401, 403, 404). CLay injects decoy cookies and misleadingly sends an "Not-Found" error page for each request with specifically marked dangerous user-agents.
