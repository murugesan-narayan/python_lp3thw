from urllib import request
from string import Template
from framework.logger import get_logger
from framework.config import config
import contextlib


class HttpSender:

    log = get_logger(__name__, config.logging_level)

    @staticmethod
    def send(url, file_path, **kwargs):
        with open(file_path, 'r') as f:
            file_content = f.read()

        template = Template(file_content)
        file_content = template.substitute(**kwargs)
        HttpSender.log.debug(f'Request: {file_content}')
        req_data = file_content.encode('utf-8')
        req = request.Request(url=url,
                              data=req_data,
                              headers={'Content-Type': 'application/xml'})
        with contextlib.closing(request.urlopen(req)) as response:
            response_data = response.read()
            response_str = response_data.decode("utf-8")
            HttpSender.log.debug(f'Response: {response_str}')
