# temeva_rest_client

SpirentTemeva is python ReST client for Spirent Temeva Service ReST API Supports HTTP-Verbs GET,POST,PUT and DELETE. 

This ReST client supports python2.7+ and python3+

https://github.com/waripoornima/temeva_rest_client


## Usage
Features:
Command Syntax/Example :

   temeva_object = SpirentTemeva(username, Password, organization_id)

* Get the Build version

			end_point = '/lic/version'
			temeva_object.get(end_point)


* List Users
			
			end_point = '/iam/users'
			temeva_object.get(end_point)


* Get application Id

			end_point = '/inv/applications'
			temeva_object.get(end_point)
	
	
* License Checkout

			end_point = '/lic/checkouts'
			user_params = {
			'orgnization_id' = 'org id provided by spirent'
			'application_id' = 'your application id ex: stc'
			}
			temeva_object.get(end_point,params=user_params)
		

                
#### Demo of some of the features:
'''python
/examples/sample_temeva_rest_client_example.py:
This is sample script to print version, org_id and applications

Note update following variables in script for your environment:
# 
username = 'your username'
password = 'your password'
organization_id = 'org_id' <- This is optional, if not provided, rest client will get the default spirent id 
'''

Note: 

You can get default spirent id 
Python code:

url = 'https://spirent.temeva.com/api/iam/organizations/default'
session = requests.Session()
response = session.get(url)


## Contact
feel free to contact for any issue while using the temeva_rest_client

poornima.wari@spirent.com
temeva-support@spirent.com

## License
[MIT]

