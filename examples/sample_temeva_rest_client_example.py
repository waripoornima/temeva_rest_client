"""
    This is sample example for temeva license checkouts
    Using temeva rest client
"""

from py_temeva_rest_client.SpirentTemeva import SpirentTemeva

# user credentials
user = 'poornima.wari@spirent.com'
password = 'Spirent2021'

# creating temeva object
temeva_object = SpirentTemeva(user, password)

# get the license server version
end_points = '/lic/version'

# calling get method
license_version = temeva_object.get(end_points)

print('License Server Version: {}'.format(license_version['build_number']))

# get the organization id
end_points = '/iam/organizations'
organization_list = temeva_object.get(end_points)
organization_id = organization_list[0]['id']
print('Organization Id: {}'.format(organization_id))

# get the application id for Spirent TestCenter
end_points ='/inv/applications'
applications_list = temeva_object.get(end_points)
print('Applications : {}'.format(applications_list))