# CLay

[![Python 3.11](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/downloads/)

![claylogo](https://github.com/kisanakkkkk/CLay/assets/70153248/bec44468-5110-44b9-a89d-240d301e6c2d)


<h4 align="center">Concealment Layer - Reverse Proxy for Concealing and Deceiving Website Informations<a href="https://github.com/kisanakkkkk/CLay" target="_blank"></a></h4>

<p align="center">
  <a href="#features">Features</a> •
  <a href="#requirements">Requirements</a> •
  <a href="#quick-start">Quick Start</a> •
  <a href="/Usage.md">User Guide</a>
</p>

CLay offers a unique and powerful feature that goes beyond traditional security measures. CLay takes deception to a new level by mimicking the appearance of a website with information from a different framework. The primary objective is to mislead and deceive potential attackers, leading them to gather false information about the web application.

| Original                                             | CLay-ed (ASP .NET + Apache)                                              | CLay-ed (PHP + Nginx)                                                   |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| ![Image 1](https://github.com/kisanakkkkk/CLay/assets/70153248/1516de88-8251-489f-89b9-c054b98e5ac5)   | ![Image 2](https://github.com/kisanakkkkk/CLay/assets/70153248/2f3965c8-078b-4066-b58f-97eee96b3efa)   | ![afterclay3wap](https://github.com/kisanakkkkk/CLay/assets/70153248/17456593-f283-4064-91ba-736f35cd9021)   |


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

5. (Optional) Build CLay as **systemd** linux service. This allows CLay to run in the background and be restarted automatically if it exits unexpectedly.
```
chmod +x initservice.sh
sudo ./initservice.sh config.json
sudo systemctl status CLay
```
### Run With Docker

```
sudo docker run -it -v $(pwd)/config.json:/CLay/config.json -p 5000:5000 kisanakkkkk/clay:latest -c config.json
```
Using bind mount (-v) to add configuration file from local system into the container.


## Usage
To get a list of basic options, use:

```CLay -h```

To generate a configuration file, use:

```CLay -g```

To start the reverse proxy, use:

```CLay -c "./config.conf"```

To customize the configuration of each feature, please visit **[Usage](/Usage.md)**.
