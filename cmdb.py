# http://regentremqa10.regenteducation.local/Account/Authenticate?ReturnUrl=_  - allows to get into the instance
# /Account/LogOff?redirectToLoginPage - logout section
# /Navigation/AdministrationTreeData - get university info

import requests
import re
import json
import sys

site_list = ['http://regentremqa.regenteducation.local',
             'http://regentremqa3.regenteducation.local',
             'http://regentremqa4.regenteducation.local',
             'http://regentremqa5.regenteducation.local',
             'http://regentremqa6.regenteducation.local',
             'http://regentremqa7.regenteducation.local',
             'http://regentremqa8.regenteducation.local',
             'http://regentremqa9.regenteducation.local',
             'http://regentremqa10.regenteducation.local',
             'http://regentremqa11.regenteducation.local',
             'http://regentremqa12.regenteducation.local',
             'http://regentremqa13.regenteducation.local',
             'http://regentremqa15.regenteducation.local',
             'http://regentremqa16.regenteducation.local',
             'http://regentremqa17.regenteducation.local',
             'http://regentremqa18.regenteducation.local']

payload = {'username': 'AutoAdmin', 'password': 'Password'}
auth_part = '/Account/Authenticate?ReturnUrl=_'  # instance login
tree_data = '/Navigation/AdministrationTreeData'  # university name

for site in site_list:
    print(site)
    with requests.Session() as c:
        login = c.post(site + auth_part, data=payload)
        page = c.get(site)
        # print(page.text) #debugging page text
        info = re.findall(r'title\=\"\s?\|(.*?)\"><span', str(page.text))
        info_string = ''.join(info)  # coverts list to string
        # print(info_string)
        university_info = c.get(site + tree_data)
        d = json.loads(university_info.text)
        university_name = d[0]['Text']
        print('    ' + university_name + '\n' + '    ' + info_string.replace('&nbsp;', '') + '\n')
sys.exit('Thanks to python:)')
