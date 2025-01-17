import unittest
import json
from monitor.logger import log_event, delete_old_logs


def test_log_event():
    log_event("Hello World")
    final_log = json.loads("log.txt") #TODO
    assert final_log == "Hello World"

def test_delete_old_logs():
    delete_old_logs()
    final_log = json.loads("log.txt") #TODO
    assert final_log == ""


if __name__ == '__main__':
    unittest.main()
