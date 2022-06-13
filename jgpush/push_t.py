# -*- coding: utf-8 -*-

import base64
# import jpush
# import jpush.common as common

# 极光推送测试

# AppKey ： 0eae16a2ec0dfcf132a1d43a
#
# Master Secret ： 8ccddaadf5e2eae4f61117be
# AppKey = "0eae16a2ec0dfcf132a1d43a"
# 2256ff3a9699df46386eef47
# AppKey = "ab70b3ae33d98e45ea1ed957"
#
# Master_Secret = "a707cabc175198779d33217e"
#
# base_str = AppKey+":"+Master_Secret
#
# str = base_str.encode('utf-8')
#
# s_b64 = base64.b64encode(str)
#
# print(s_b64)


# # _jpush = jpush.JPush(app_key, master_secret)
# _jpush = jpush.JPush(AppKey, Master_Secret)
# push = _jpush.create_push()
# # if you set the logging level to "DEBUG",it will show the debug logging.
# _jpush.set_logging("DEBUG")
# push.audience = jpush.all_
# push.notification = jpush.notification(alert="hello python jpush api")
# push.platform = jpush.all_
# try:
#     response=push.send()
#
# except common.Unauthorized:
#     raise common.Unauthorized("Unauthorized")
# except common.APIConnectionException:
#     raise common.APIConnectionException("conn error")
# except common.JPushFailure:
#     print ("JPushFailure")
# except:
#     print ("Exception")
import requests
import json

jpush_url = "https://api.jpush.cn/v3/push"


def jpush_rest_api_send(uid, msg):
    headers = {"content-type": "application/json",
               "Authorization": "Basic YWI3MGIzYWUzM2Q5OGU0NWVhMWVkOTU3OmE3MDdjYWJjMTc1MTk4Nzc5ZDMzMjE3ZQ=="}
    # headers["Authorization"] = "Basic YWI3MGIzYWUzM2Q5OGU0NWVhMWVkOTU3OmE3MDdjYWJjMTc1MTk4Nzc5ZDMzMjE3ZQ=="
    # AppKey = "ab70b3ae33d98e45ea1ed957"
    #
    # Master_Secret = "a707cabc175198779d33217e"
    #
    # base_str = AppKey + ":" + Master_Secret
    #
    # _str = base_str.encode('utf-8')
    # s_b64 = str(base64.b64encode(base_str))
    # headers["Authorization"] = "Basic YWI3MGIzYWUzM2Q5OGU0NWVhMWVkOTU3OmE3MDdjYWJjMTc1MTk4Nzc5ZDMzMjE3ZQ=="
    # headers["Authorization"] = s_b64
    # requests.p
    uid = "18171adc03f83761bd5"
    data = {
        "options": {
            "apns_production": False
        },
        "platform": ["ios"],
        "audience": {"registration_id": [uid]},
        "notification": {
            "ios": {
                "alert": msg
            }
        }
    }
    # res = requests.post(jpush_url, json=json.dumps(data), headers=headers)
    res = requests.post(jpush_url, data=data, headers=headers)
    if res.status_code == 200:
        return 0, json.loads(res.text)
    else:
        return -1, json.loads(res.text)


if __name__ == '__main__':
    jpush_rest_api_send(1, 'hao')
