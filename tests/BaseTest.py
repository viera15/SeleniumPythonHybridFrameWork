import time

import pytest


@pytest.mark.usefixtures("setup_and_teardown")
class BaseTest:

    def generate_email_with_time_stamp(self):
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        timestamp = timestamp.replace("-", "_").replace(" ", "_").replace(":", "_")
        return "anicka"+timestamp+"@gmail.com"