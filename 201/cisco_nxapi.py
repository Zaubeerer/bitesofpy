import requests


def nxapi_show_version():
    url =  """ please fill in """
    switchuser = """ please fill in """
    switchpassword = """ please fill in """

    http_headers = {""" please fill in """}
    payload = [{"jsonrpc": "2.0",
                "method": """ please fill in """,
                "params": {"cmd": """ please fill in """,
                           "version": 1}, "id": 1}]
    # 1. use requests to post to the switch
    response = ...

    # 2. retrieve and return the kickstart_ver_str from the response
    # example response json:
    # {'result': {'body': {'bios_cmpl_time': '05/17/2018',
    #                      'kick_tmstmp': '07/11/2018 00:01:44',
    #                      'kickstart_ver_str': '9.2(1)',
    #                      ...
    #                      }
    #             }
    # }
    version = ...
    return version


if __name__ == '__main__':
    result = nxapi_show_version()
    print(result)