"""
Copyright start
MIT License
Copyright (c) 2023 Fortinet Inc
Copyright end
"""
import requests, json, re
from connectors.core.connector import get_logger, ConnectorError
from requests import exceptions as req_exceptions
from time import sleep

logger = get_logger('ridgebot')
target_regex = '^(\d{1,3}(\.\d{1,3}){3})(|:\d{1,5})$|^([-a-zA-Z0-9]{1,20}(\.[-a-zA-Z0-9]{4,20}){1,3}(\.[a-z]{2,3}){1,2})(|:\d{1,5})$'
taskid_regex = '^[a-f0-9]{8}(-[a-f0-9]{4}){3}-[a-f0-9]{12}$'


class RidgeBot(object):
    def __init__(self, config):
        self.server_url = config.get('server_url', '').strip('/')
        if not self.server_url.startswith('https://') and not self.server_url.startswith('http://'):
            self.server_url = 'https://' + self.server_url
        self.headers = {
            "Accept": "application/json",
            "Authorization": config.get('user_token'),
            "Content-Type": "application/json"
        }
        self.verify_ssl= config.get('verify_ssl',False)

    def make_rest_call(self, endpoint, params={}, payload={}, method='GET'):
        service_endpoint = '{0}{1}'.format(self.server_url, endpoint)
        logger.debug("service_endpoint: {0}".format(service_endpoint))
        try:
            response = requests.request(method, service_endpoint, data=payload, params=params, headers=self.headers, verify=self.verify_ssl)
            if response.ok:
                json_data = json.loads(response.content.decode('utf-8'))
                return json_data
            else:
                logger.error('Status Code: {0}, API Response: {1}'.format(response.status_code, response.text))
                raise ConnectorError(response.text)
        except req_exceptions.SSLError:
            logger.error('An SSL error occurred')
            raise ConnectorError('An SSL error occurred')
        except req_exceptions.ConnectionError:
            logger.error('A connection error occurred')
            raise ConnectorError('A connection error occurred')
        except req_exceptions.Timeout:
            logger.error('The request timed out')
            raise ConnectorError('The request timed out')
        except req_exceptions.RequestException:
            logger.error('There was an error while handling the request')
            raise ConnectorError('There was an error while handling the request')
        except Exception as err:
            logger.error(err)
            raise ConnectorError(str(err))


def create_task(config, params):
    ridge = RidgeBot(config)
    name = params.get('name')
    temp = params.get('temp_id')
    targets = []
    if temp == "Website":
        get_list = params.get('targets').split(",")
        for target in get_list:
            target_temp = target.strip('/')
            if not target_temp.startswith('https://') and not target_temp.startswith('http://'):
                if re.match(target_regex, target_temp): targets.append("https://" + target_temp)
            else:
                temp_target = re.sub(r'http(|s)://', '', target_temp)
                if re.match(target_regex, temp_target): targets.append(target_temp)
        temp_id = 2
    else:
        get_list = params.get('targets').split(",")
        for target in get_list:
            if re.match(target_regex, target):
                targets.append(target)
        temp_id = 1
    target = ("\", \"").join(targets)
    create = "{ \"name\": \"" + name + "\", \"targets\": [ \"" + target + "\" ], \"template_id\": " + str(temp_id) + "}"
    return ridge.make_rest_call('/api/v4/tasks', payload=create, method='POST')


def stop_task(config, params):
    ridge = RidgeBot(config)
    task_id = params.get('task_id')
    stop = "{ \"task_id\": \"" + task_id + "\"}"
    return ridge.make_rest_call('/api/v4/tasks/stop', payload=stop, method='POST')


def get_task_info(config, params):
    ridge = RidgeBot(config)
    task_id = params.get('task_id')
    endpoint = f'/api/v4/tasks/info?task_id={task_id}'
    return ridge.make_rest_call(endpoint)


def get_task_statistics(config, params):
    ridge = RidgeBot(config)
    task_id = params.get('task_id')
    endpoint = f'/api/v4/tasks/statistics?task_id={task_id}'
    return ridge.make_rest_call(endpoint)


def generate_and_download(config, params):
    ridge = RidgeBot(config)
    task_id = params.get('task_id')
    gen = "{ \"custom_logo\": 0, \"language\": 1, \"report_data\": { \"assets_details\": true, \"basic_info\": { \"config_profiles\": true, \"executive_summary\": true }, \"penetration_result\": { \"risk_details\": true }, \"vulnerability_level\": { \"high\": true, \"info\": true, \"low\": true, \"medium\": true } }, \"task_id\": \"" + task_id + "\", \"filter_con\": {}, \"template\": 0, \"type\": \"pdf\"}"
    resp = ridge.make_rest_call('/api/v4/report/generate', payload=gen, method='POST')
    report_id = resp['data']['report_id']
    down = "{ \"ids\": [ " + str(report_id) + " ], \"password\": \"\"}"

    # Give server 2 minutes to generate a report. An alternative would be to merge report
    # generation and download into a single API endpoint and use long-polling. This way, the server
    # is responsible for the timeout duration, not the client, and the server can return a response
    # immediately when the report is available. 
    sleep(120)

    return ridge.make_rest_call('/api/v4/report/download', payload=down, method='POST')


def test_connect(config):
    ridge = RidgeBot(config)
    return ridge.make_rest_call('/api/v4/test/connect')


def _check_health(config):
    return test_connect(config)


operations = {
    'create_task': create_task,
    'stop_task': stop_task,
    'get_task_info': get_task_info,
    'get_task_statistics': get_task_statistics,
    'generate_and_download': generate_and_download
}