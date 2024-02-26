import re
import json
import os

read_server = os.path.join(os.path.dirname(__file__), 'config/deception_server.json')
read_framework = os.path.join(os.path.dirname(__file__), 'config/deception_framework.json')

with open(read_server, "r") as server_file:
	server_file = json.loads(server_file.read())
	list_server = [i for i in server_file.keys()]
with open(read_framework, "r") as framework_file:
	framework_file = json.loads(framework_file.read())
	list_framework = [i for i in framework_file.keys()]

def answer(answer):
	try:
		ans = answer.lower()
		if ans == "y":
			return True
		elif ans == "n":
			return False
		else:
			print("Please enter y or n")
			return None
	except Exception as e:
		print("error input", e)

def xinput(msg):
	inp = input(msg)
	if inp == 'q':
		exit()
	else:
		return inp

def is_valid_ip(ip):
	try:
		if ip == "":
			return None
		ip_pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
		match = re.match(ip_pattern, ip)
		return bool(match)
	except Exception as e:
		print("error ip", e)

def is_valid_port(port):
	if port == "":
		return None
	try:
		port = int(port)
		return 0 < port <= 65535
	except ValueError:
		return False

def get_target_url(target_url):
	try:
		url_pattern = re.compile(r'(http(?:s?)://.*?[^\.\/]+?\.[^\.]+?)(?:\/|$)')
		matches = url_pattern.findall(target_url)
		if matches:
			return matches[0]
		else:
			return False
	except Exception as e:
		print("error get target url", e)

def generate_list_comment(decoy_comment):
	try:
		res = []
		for i in decoy_comment:
			dicti = {}
			dicti["comment"] = i
			dicti["url_target_paths"] = decoy_comment[i]
			res.append(dicti)
		return res
	except Exception as e:
		print("error list comment generation", e)

def promptLHost():
	while True:
		try:
			lhost = xinput("[?] Enter CLay listening host (default: 0.0.0.0): ")
			valid = is_valid_ip(lhost)
			if valid == False:
				print("input is not a valid IP address")
			elif valid == None:
				lhost = "0.0.0.0"
				break
			else:
				break
		except Exception as e:
			print("something's wrong", e)
	return lhost

def promptLPort():
	while True:
		try:
			lport = xinput("[?] Enter CLay listening port (default: 5000): ")
			valid = is_valid_port(lport)
			if valid == False:
				print("input is not a valid port")
			elif valid == None:
				lport = 5000
				break
			else:
				break
		except Exception as e:
			print("something's wrong", e)
	return lport

def promptTarget():
	while True:
		try:
			target_url = xinput("[?] Enter target url: ")
			valid = get_target_url(target_url)
			if not valid:
				print("input is not a valid url")
			else:
				break
		except Exception as e:
			print("something's wrong", e)
	return target_url

def promptDecoyServer():
	while True:
		try:
			print("[?] What fake SERVER technology you want to use: ")
			for i, j in enumerate(list_server):
				print(f"{i+1}. {j}")
			no_server = xinput(">> ")
			server = list_server[int(no_server)-1]
			break
		except Exception as e:
			print("option is not valid")
	return server

def promptDecoyFramework():
	while True:
		try:
			print("[?] What fake FRAMEWORK technology you want to use: ")
			for i, j in enumerate(list_framework):
				print(f"{i+1}. {j}")
			no_framework = xinput(">> ")
			framework = list_framework[int(no_framework)-1]
			break
		except Exception as e:
			print("option is not valid")
	return framework

def promptFilterAgent():
	while True:
		try:
			inp = xinput("[?] Do you want to block requests from known scanning tools by filtering user agents? [y/n]: ")
			filter_request_by_user_agent = answer(inp)
			if filter_request_by_user_agent != None:
				break
		except Exception as e:
			print("something's wrong", e)
	return filter_request_by_user_agent

def promptFilterComment():
	while True:
		try:
			inp = xinput("[?] Do you want to hide comments in the HTML code? [y/n]: ")
			filter_comment = answer(inp)
			if filter_comment != None:
				break
		except Exception as e:
			print("something's wrong", e)
	return filter_comment

def promptFilterHeader():
	while True:
		try:
			inp = xinput("[?] Do you want to remove unnecessary server details from the response headers? [y/n]: ")
			filter_response_header = answer(inp)
			if filter_response_header != None:
				break
		except Exception as e:
			print("something's wrong", e)
	return filter_response_header

def promptErrorTemplate():
	while True:
		try:
			inp = xinput("[?] Do you want to change the default error template? [y/n]: ")
			error_template_changing = answer(inp)
			if error_template_changing != None:
				break
		except Exception as e:
			print("something's wrong", e)
	return error_template_changing

def promptAddHeader():
	while True:
		try:
			inp = xinput("[?] Do you want to add fake response headers? [y/n]: ")
			add_decoy_header = answer(inp)
			if add_decoy_header != None:
				break
		except Exception as e:
			print("something's wrong", e)
	return add_decoy_header

def promptAddCookie():
	while True:
		try:
			inp = xinput("[?] Do you want to add fake cookies? [y/n]: ")
			add_decoy_cookie = answer(inp)
			if add_decoy_cookie != None:
				break
		except Exception as e:
			print("something's wrong", e)
	return add_decoy_cookie

def promptAddComment():
	comms = True
	decoycom = {}
	while comms:
		try:
			inp = xinput("[?] Do you want to add fake comments? [y/n]: ")
			add_decoy_comment = answer(inp)
			if add_decoy_comment == True:
				while comms:
					decoy_comment = xinput("Please insert decoy comment: ")
					path = []
					while True:
						path_decoy_comment = xinput("URL path you want to place the decoy comment (enter to done): ")
						if path_decoy_comment != "":
							path.append(path_decoy_comment)
						else:
							decoycom[decoy_comment] = path
							break
					while True:
						another = answer(xinput("Do you want to add another fake comments? [y/n]: "))
						if another == False:
							comms = False
							break
						elif another == True:
							break
			elif add_decoy_comment == False:
				break
		except Exception as e:
			print("something's wrong", e)
	return add_decoy_comment, decoycom

def generateConfig():
	while True:
		try:
			print("CLay - Concealment LAYer")
			print("[1] Run CLay (default config)")
			print("[2] Custom configuration")
			print("[3] Quit")
			print("")
			setup = input(">> ")
			if setup == "1":
				genQuick()
			elif setup == "2":
				genCustom()
			elif setup == "3":
				exit()
			else:
				print("error input")
		except Exception as e:
			print("error input")

def genQuick():
	print("\n==Default Configuration==")
	print("- CLay will run on port 5000")
	print("- Decoy Server Technology: Nginx")
	print("- Decoy Framework Technology: Microsoft ASP.NET")
	print("- All features enabled")
	print("\nPlease enter target url (example: http://example.com)")
	target_url = promptTarget()
	lhost = "0.0.0.0"
	lport = 5000
	server = "Nginx"
	framework = "Microsoft ASP.NET"
	filter_request_by_user_agent = True
	filter_comment = True
	filter_response_header = True
	error_template_changing = True
	add_decoy_header = True
	add_decoy_cookie = True
	add_decoy_comment, decoycom = True, {'dev': ['.*/']}
	generatejson(lhost, lport, target_url, server, framework, filter_request_by_user_agent, filter_comment, filter_response_header, error_template_changing, add_decoy_header, add_decoy_cookie, add_decoy_comment, decoycom)

def genCustom():
	print("==type q to quit==")
	lhost = promptLHost()
	lport = promptLPort()
	target_url = promptTarget()
	server = promptDecoyServer()
	framework = promptDecoyFramework()
	filter_request_by_user_agent = promptFilterAgent()
	filter_comment = promptFilterComment()
	filter_response_header = promptFilterHeader()
	error_template_changing = promptErrorTemplate()
	add_decoy_header = promptAddHeader()
	add_decoy_cookie = promptAddCookie()
	add_decoy_comment, decoycom = promptAddComment()
	generatejson(lhost, lport, target_url, server, framework, filter_request_by_user_agent, filter_comment, filter_response_header, error_template_changing, add_decoy_header, add_decoy_cookie, add_decoy_comment, decoycom)

def generatejson(lhost, lport, target_url, server, framework, filter_request_by_user_agent, filter_comment, filter_response_header, error_template_changing, add_decoy_header, add_decoy_cookie, add_decoy_comment, decoycom):

	dicti = json.dumps({
	  "listen_host": lhost,
	  "listen_port": int(lport),
	  "url_target": target_url,
	  "decoy_technology": {
		"server": server,
		"framework": framework
	  },
	  "user_preference": {
		"filter_request_by_user_agent": filter_request_by_user_agent,
		"filter_comment": filter_comment,
		"filter_response_header": filter_response_header,
		"error_template_changing": error_template_changing,
		"add_decoy_header": add_decoy_header,
		"add_decoy_cookie": add_decoy_cookie,
		"add_decoy_comment": {
		  "status": add_decoy_comment,
		  "decoy_comments": generate_list_comment(decoycom)
		}
	  }
	}, indent=2)
	print("\n\nCreated json:")
	print(dicti)

	try:
		fx = open("./config.json", 'w')
		fx.write(dicti)
		exit()
	except Exception as e:
		print("an error occured", e)
