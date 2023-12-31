import json
import os

class Configure:
    def __init__(self):
        self.config_data = None
        self.deception_data = None
        self.user_preference = None
        
    def set_config(self, f):
        try:
            file_path = f
            with open(file_path, "r") as config_file:
                config_data = json.load(config_file)
            self.config_data = config_data
        except FileNotFoundError:
            print(f"Error: config file '{file_path}' not found.")
            return None
        except json.JSONDecodeError as e:
            print(f"Error: decoding JSON in '{file_path}': {e}")
            return None
        except Exception as e:
            print('Error: read_config', e)
    
    def read_config(self):
        return self.config_data
    
    def read_technology(self, technology):
        try:
            result = {}
            #read config/deception_server.json
            server_file_path = os.path.join(os.path.dirname(__file__), 'config/deception_server.json')
            with open(server_file_path, "r") as config_file:
                config_data = json.load(config_file)
                server_technology = technology['server']
                if server_technology in config_data:
                    result[server_technology] = config_data[server_technology]
                    print(f"[+] Technology {server_technology} successfully loaded.")
                else:
                    print(f"[!] Technology {server_technology} doesn't exist in our database.")

            #read config/deception_framework.json

            framework_file_path = os.path.join(os.path.dirname(__file__), 'config/deception_framework.json')
            with open(framework_file_path, "r") as config_file:
                config_data = json.load(config_file)
                framework_technology = technology['framework']
                if framework_technology in config_data:
                    result[framework_technology] = config_data[framework_technology]
                    print(f"[+] Technology {framework_technology} successfully loaded.")
                else:
                    print(f"[!] Technology {framework_technology} doesn't exist in our database.")

            return result
        except FileNotFoundError:
            print(f"Error: config file '{file_path}' not found.")
            return None
        except json.JSONDecodeError as e:
            print(f"Error: decoding JSON in '{file_path}': {e}")
            return None
        except Exception as e:
            print('Error: read_technology', e)
    
    def get_deception_data(self):
        try:
            config = self.read_config()
            # get detail deception will be used
            deception_technology_details = self.get_deception_techniques(config)
            return deception_technology_details
        except Exception as e:
            print('Error: get_deception_data', e)

    def get_user_preference(self):
        try:
            config = self.read_config()
            user_preference = config.get("user_preference")
            return user_preference
        except Exception as e:
            print('Error: get_user_preference', e)

    def recursive_concat(self, dict1, dict2):
        try:
            result_dict = dict1.copy()

            for key, value in dict2.items():
                if key in result_dict and isinstance(value, dict) and isinstance(result_dict[key], dict):
                    result_dict[key] = self.recursive_concat(result_dict[key], value)
                elif key in result_dict:
                    # If the key is present and the value is not a dictionary, append the value
                    result_dict[key] = [result_dict[key], value]
                else:
                    # If the key is not present, add the key-value pair
                    result_dict[key] = value

            return result_dict
        except Exception as e:
            print('Error: recursive_concat', e)


    def read_technology_detail(self, deception_technology):
        try:
            deception_technology_details = {}
            for key, value in deception_technology.items():
                temp_detail = dict(value)
                deception_technology_details = self.recursive_concat(deception_technology_details, temp_detail)

            return deception_technology_details
        except Exception as e:
            print('Error: read_technology_detail', e)


    def get_deception_techniques(self, config):
        try:
            technology = config.get("decoy_technology")
            deception_technology = self.read_technology(technology)
            deception_technology_details = self.read_technology_detail(deception_technology)
            return deception_technology_details
        except Exception as e:
            print('Error: get_deception_techniques', e)

configure = Configure()

