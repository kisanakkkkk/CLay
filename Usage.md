# Usage
```
usage: CLay [-h] [-c CONFIG] [-g]

options:
  -h, --help                    show this help message and exit
  -c CONFIG, --config CONFIG    run proxy based on JSON configuration file
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

### Feature - Request Filtering by User-Agent
| Before                                              | After                                              |
| ---------------------------------------------------- | ---------------------------------------------------- |
| ![Image 1]()   | ![Image 2]()   |

Determine whether the request originates from a dangerous (tools-based) user agent. If detected, CLay will respond with a false 200 OK status code while sending a 'not found' error page in the response body, confusing the attackers.

```
"filter_request_by_user_agent": true
```

### Feature - HTML Comment Filtering
| Before                                              | After                                              |
| ---------------------------------------------------- | ---------------------------------------------------- |
| ![Image 1]()   | ![Image 2]()   |

Automatically remove all HTML comments, preventing unnecessary information leakage inside the webpage source codes.

```
"filter_comment": true,
```

### Feature - Informative Response Header Filtering
| Before                                              | After                                              |
| ---------------------------------------------------- | ---------------------------------------------------- |
| ![Image 1]()   | ![Image 2]()   |

Determine whether the application’s response contains informative headers, such as the server banner. If detected, CLay will remove the response header seamlessly.

```
"filter_response_header": true
```

### Feature - Error Template Changing
| Before                                              | After                                              |
| ---------------------------------------------------- | ---------------------------------------------------- |
| ![Image 1]()   | ![Image 2]()   |

CLay will replace the application’s default error pages with the other framework's error pages to prevent attackers from gathering essential information from the error page templates.

```
"error_template_changing": true
```

### Feature - Adding Decoy Informative Response Headers
| Before                                              | After                                              |
| ---------------------------------------------------- | ---------------------------------------------------- |
| ![Image 1]()   | ![Image 2]()   |

CLay allows users to add decoy informative headers, such as the fake server banner to potentially mislead attackers engaged in reconnaissance.

```
"add_decoy_header": true
```

### Feature - Adding Decoy Cookies
| Before                                              | After                                              |
| ---------------------------------------------------- | ---------------------------------------------------- |
| ![Image 1]()   | ![Image 2]()   |

CLay allows users to add decoy cookies to make it difficult for attackers to determine the actual framework and technology used.

```
"add_decoy_cookie": true
```

### Feature - Adding Dummy HTML Comments
| Before                                              | After                                              |
| ---------------------------------------------------- | ---------------------------------------------------- |
| ![Image 1]()   | ![Image 2]()   |

CLay allows users to add dummy HTML comments in multiple paths to mislead attackers engaged in reconnaissance, throwing them into a wild goose chase.

```
"add_decoy_comment": {
    "status": true,
    "decoy_comments": [
        {
            "comment": "Dummy comment goes here",
            "url_target_paths": [".*/login/", ".*/test/"]
        },
        {
            "comment": "Dummy comment 2 goes here",
            "url_target_paths": [".*/signup/"]
        }
    ]
}
```