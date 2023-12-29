# CLay
[![Python 3.11](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/downloads/)

![claylogo](https://github.com/kisanakkkkk/CLay/assets/70153248/bfdbe944-4b00-4128-b656-923428f8de29)



<h4 align="center">Concealment Layer - Reverse Proxy for Concealing and Deceiving Website Informations<a href="https://github.com/chrisandoryan/Nethive-Project" target="_blank"></a></h4>

<p align="center">
  <a href="#features">Features</a> •
  <a href="#requirements">Requirements</a> •
  <a href="#quick-start">Quick Start</a> •
  <a href="/Usage.md">User Guide</a>
</p>

CLay offers a unique and powerful feature that goes beyond traditional security measures. CLay takes deception to a new level by mimicking the appearance of a website with information from a different framework. The primary objective is to mislead and deceive potential attackers, leading them to gather false information about the web application.

| Original                                             | CLay-ed (ASP .NET + Apache)                                              | CLay-ed (PHP + Nginx)                                                   |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| ![Image 1](https://github.com/kisanakkkkk/CLay-dev/assets/70153248/cfef3fd1-e3e6-4401-aebf-9869ba400150)   | ![Image 2](https://github.com/kisanakkkkk/CLay-dev/assets/70153248/c90512eb-4cbd-44a7-8d37-1ba9443de85d)   | ![afterclay3wap](https://github.com/kisanakkkkk/CLay-dev/assets/70153248/f359af69-6335-49e0-8a1a-837c93eea036)   |



## Features
- Request filtering by User Agent
- HTML Comment Filtering
- Informative Response Header Filtering
- Adding Dummy HTML Comments
- Adding Decoy Informative Response Headers
- Adding Decoy Cookies
- Error Template Changing

### Supported Decoy Frameworks
- **PHP**
- **Laravel**
- **Microsoft ASP.NET**
- **Flask**
- **Django**
  
### Supported Decoy Webservers
- **Nginx**
- **Apache HTTP Server**


## Requirements
- Python 3.11+
- `mitmproxy` is a set of tools that provide an interactive, SSL/TLS-capable intercepting proxy for HTTP/1, HTTP/2, and WebSockets. **CLay** utilizes `mitmproxy`'s capabilities to intercept and modify HTTP/HTTPS traffics on the fly.

- `Jinja` is a fast, expressive, extensible templating engine.

## Quick Start
1. Fetch and start CLay package installation.
```
git clone https://github.com/kisanakkkkk/CLay.git
cd CLay
pip3 install .
```

2. Generate new configuration file. On the menu prompt, choose **[1] Run CLay (default config)**, then enter the target URL for which you'd like to set up the CLay.
```
CLay -g
```

3. Start CLay.
```
CLay -c config.json
```

4. Go to http://0.0.0.0:5000/.


### Run With Docker

Coming Soon!


## Usage
To get a list of basic options, use:

```CLay -h```

To generate a configuration file, use:

```CLay -g```

To start the reverse proxy, use:

```CLay -c "./config.conf"```

To customize the configuration of each feature, please visit **[Usage](/Usage.md)**.
