## About the connector
RidgeBot validates security vulnerabilities in your organization by using real POC codes to exploit the vulnerability. This connector facilitates automated operation such as creating and executing penetration testing tasks.
<p>This document provides information about the Ridge Security RidgeBot Connector, which facilitates automated interactions, with a Ridge Security RidgeBot server using FortiSOAR&trade; playbooks. Add the Ridge Security RidgeBot Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with Ridge Security RidgeBot.</p>

### Version information

Connector Version: 1.0.0


Authored By: Ridge Security

Certified: No
## Installing the connector
<p>From FortiSOAR&trade; 5.0.0 onwards, use the <strong>Connector Store</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.<br>You can also use the following <code>yum</code> command as a root user to install connectors from an SSH session:</p>
`yum install cyops-connector-ridgebot`

## Prerequisites to configuring the connector
- You must have the URL of Ridge Security RidgeBot server to which you will connect and perform automated operations and credentials to access that server.
- The FortiSOAR&trade; server should have outbound connectivity to port 443 on the Ridge Security RidgeBot server.

## Minimum Permissions Required
- N/A

## Configuring the connector
For the procedure to configure a connector, click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector)
### Configuration parameters
<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>Ridge Security RidgeBot</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations&nbsp;</strong> tab enter the required configuration details:&nbsp;</p>
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Server URL<br></td><td>Specify the RidgeBot server URL to which you can connect and perform automated operations.<br>
<tr><td>User Token<br></td><td>Specify an Identity Token used to access the RidgeBot endpoint to which you can connect and perform automated operations.<br>
</tbody></table>

## Actions supported by the connector
The following automated operations can be included in playbooks and you can also use the annotations to access operations from FortiSOAR&trade; release 4.10.0 and onwards:
<table border=1><thead><tr><th>Function<br></th><th>Description<br></th><th>Annotation and Category<br></th></tr></thead><tbody><tr><td>get_task_info<br></td><td>Retrieves information about an existing task such as start time, end time, status, etc.<br></td><td> <br/><br></td></tr>
<tr><td>get_task_statistics<br></td><td>Retrieves finding statistics of an existing task such number of assets found, number of vulnerabilities found per risk category, etc.<br></td><td> <br/><br></td></tr>
<tr><td>generate_and_download<br></td><td>Generates and downloads penetration testing report from a completed task by specifying the Task ID.<br></td><td> <br/><br></td></tr>
<tr><td>stop_task<br></td><td>Stops a running or unfinished task by specifying the Task ID.<br></td><td> <br/><br></td></tr>
<tr><td>create_task<br></td><td>Creates a default intranet or web penetration testing task.<br></td><td> <br/><br></td></tr>
</tbody></table>

### operation: get_task_info
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Task ID<br></td><td>Specify an existing RidgeBot Task ID for which you want to retrieve details from RidgeBot server.<br>
</td></tr></tbody></table>

#### Output

 No output schema is available at this time.
### operation: get_task_statistics
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Task ID<br></td><td>Specify an existing RidgeBot Task ID for which you want to retrieve details from RidgeBot server.<br>
</td></tr></tbody></table>

#### Output

 No output schema is available at this time.
### operation: generate_and_download
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Task ID<br></td><td>Specify an existing RidgeBot Task ID for which you want to retrieve details from RidgeBot server.<br>
</td></tr></tbody></table>

#### Output

 No output schema is available at this time.
### operation: stop_task
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Task ID<br></td><td>Specify an existing RidgeBot Task ID for which you want to retrieve details from RidgeBot server.<br>
</td></tr></tbody></table>

#### Output

 No output schema is available at this time.
### operation: create_task
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Name of Scan<br></td><td>Specify a name or title for the task to be created.<br>
</td></tr><tr><td>Type of Scan<br></td><td>Choose the type of scan to be created. Either Intranet or Web Penetration Testing task.<br>
</td></tr><tr><td>Targets<br></td><td>Specifies the target(s) for the scan.<br>
</td></tr></tbody></table>

#### Output

 No output schema is available at this time.
## Included playbooks
The `Sample - ridgebot - 1.0.0` playbook collection comes bundled with the Ridge Security RidgeBot connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the **Automation** > **Playbooks** section in FortiSOAR<sup>TM</sup> after importing the Ridge Security RidgeBot connector.

- create_task
- generate_and_download
- get_task_info
- get_task_statistics
- stop_task

**Note**: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection, since the sample playbook collection gets deleted during connector upgrade and delete.
