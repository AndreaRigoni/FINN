# -*- coding: utf-8 -*-
"""
    Dummy conftest.py for finn.

    If you don't know what this is for, just leave it empty.
    Read more about conftest.py under:
    https://pytest.org/latest/plugins.html
"""

import pytest



def start_debug(port=3000, wait=False):
    try:
        import ptvsd
        # Allow other computers to attach to ptvsd at this IP address and port.
        ptvsd.enable_attach(address=('*', port), redirect_output=True)
        # Pause the program until a remote debugger is attached
        if wait:
            ptvsd.wait_for_attach()
        print('debug active on *:%d'%port)
    except:
        print('unable to set vs debugger')


def pytest_runtest_setup(item):
        # called for running each test 
        print ("setting up", item)
        start_debug(wait=False)
        print ("setting up", item)



# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     # execute all other hooks to obtain the report object
#     outcome = yield
#     rep = outcome.get_result()

#     # # we only look at actual failing test calls, not setup/teardown
#     # if rep.when == "call" and rep.failed:
#     #     # mode = "a" if os.path.exists("failures") else "w"
#     #     # with open("failures", mode) as f:
#     #     #     # let's also access a fixture for the fun of it
#     #     #     if "tmpdir" in item.fixturenames:
#     #     #         extra = " ({})".format(item.funcargs["tmpdir"])
#     #     #     else:
#     #     #         extra = ""

#     #     #     f.write(rep.nodeid + extra + "\n")
#     #     pass

