# CLay
[![Python 3.11](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/downloads/)

![claylogo](https://github.com/kisanakkkkk/CLay/assets/70153248/4641307d-e2a7-4dc0-8910-7afcb33fa357)


*Concealment Layer - Reverse Proxy for Concealing and Deceiving Website Informations*

CLay offers a unique and powerful feature that goes beyond traditional security measures. CLay takes deception to a new level by mimicking the appearance of a website with information from a different framework. The primary objective is to mislead and deceive potential attackers, leading them to gather false information about the web application.

QuickStart
----------
```
git clone https://github.com/kisanakkkkk/CLay.git
cd CLay
pip3 install .
CLay -c "config.conf"
```

Run With Docker
---------------

Python3:

``docker run -it -p 5000:5000 kisanakkkkk/clay:latest -c "./config.conf"``

Features
--------
- User Agent Detection
- HTML Comment Filtering
- Informative Response Header Filtering
- Adding Dummy HTML Comments
- Adding Decoy Informative Response Headers
- Adding Decoy Cookies
- Error Template Changing

Supported Decoy Frameworks
----------
- **PHP**
- **Laravel**
- **ASP.NET**
- **Flask**
- **Django**
  
Supported Decoy Webservers
----------
- **Nginx**
- **Apache**

Requirement
-----------
- Python 3.11+
- `mitmproxy` is a set of tools that provide an interactive, SSL/TLS-capable intercepting proxy for HTTP/1, HTTP/2, and WebSockets. **CLay** utilizes `mitmproxy`'s capabilities to intercept and modify HTTP/HTTPS traffics on the fly.

- `Jinja` is a fast, expressive, extensible templating engine.

Usage Example - Custom Configurations
----------
```CLay -c "./config.conf"```


**config.conf**
```
{
  "lhost": "0.0.0.0",
  "lport": 5000,
  "target": "http://127.0.0.1:8000/",
  "decoy_technology": {
    "server": "Apache HTTP Server",
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
          "comment": "Dummy comment goes here",
          "target_paths": [".*/login/", ".*/test/"]
        },
        {
          "comment": "Dummy comment 2 goes here",
          "target_paths": [".*/signup/"]
        }
      ]
    }
  }
}
```

### Use Case - User Agent Detection
Determine whether the request originates from a dangerous (tools-based) user agent. If detected, CLay will respond with a 200 OK status code while sending a 'not found' error page in the response body.

```
"filter_request_by_user_agent": true
```

### Use Case - HTML Comment Filtering
Remove all HTML Comments

```
"filter_comment": true,
```

### Use Case - Informative Response Header Filtering
Determine whether the response contains informative headers, such as the server banner. If detected, CLay will remove the response header.

```
"filter_response_header": true
```

### Use Case - Adding Dummy HTML Comments
CLay allows users to add dummy HTML comments in multiple paths to potentially mislead attackers engaged in reconnaissance.

```
"add_decoy_comment": {
    "status": true,
    "decoy_comments": [
        {
            "comment": "Dummy comment goes here",
            "target_paths": [".*/login/", ".*/test/"]
        },
        {
            "comment": "Dummy comment 2 goes here",
            "target_paths": [".*/signup/"]
        }
    ]
}
```


### Use Case - Adding Decoy Informative Response Headers
CLay allows users to add decoy response headers to potentially mislead attackers engaged in reconnaissance.

```
"add_decoy_header": true
```

### Use Case - Adding Decoy Cookies
CLay allows users to add a decoy cookie to make it difficult for attackers to determine the framework used.

```
"add_decoy_cookie": true
```

### Use Case - Error Template Changing
CLay will replace the original error page with the framework's error pages that the user has specified to prevent attackers from gathering information from the error page template.

```
"error_template_changing": true
```
