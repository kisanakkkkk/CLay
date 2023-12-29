```
usage: CLay [-h] [-c CONFIG] [-g]

options:
  -h, --help                    show this help message and exit
  -c CONFIG, --config CONFIG    run proxy based on JSON configuration file
  -g, --generate                generate JSON file
```


### Use Case - Request filtering by User Agent
Determine whether the request originates from a dangerous (tools-based) user agent. If detected, CLay will respond with a false 200 OK status code while sending a 'not found' error page in the response body, confusing the attackers.

```
"filter_request_by_user_agent": true
```

### Use Case - HTML Comment Filtering
Automatically remove all HTML comments, preventing unnecessary information leakage inside the webpage source codes.

```
"filter_comment": true,
```

### Use Case - Informative Response Header Filtering
Determine whether the application’s response contains informative headers, such as the server banner. If detected, CLay will remove the response header seamlessly.

```
"filter_response_header": true
```

### Use Case - Adding Dummy HTML Comments
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


### Use Case - Adding Decoy Informative Response Headers
CLay allows users to add decoy informative headers, such as the fake server banner to potentially mislead attackers engaged in reconnaissance.

```
"add_decoy_header": true
```

### Use Case - Adding Decoy Cookies
CLay allows users to add decoy cookies to make it difficult for attackers to determine the actual framework and technology used.

```
"add_decoy_cookie": true
```

### Use Case - Error Template Changing
CLay will replace the application’s default error pages with the other framework's error pages to prevent attackers from gathering essential information from the error page templates.

```
"error_template_changing": true
```