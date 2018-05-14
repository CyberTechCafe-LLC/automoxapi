"""
This is a thin python wrapper for the Automox API
"""
from urllib.request import Request, urlopen
from urllib.parse import urlencode
import json

__version__ = '0.0.1'


class Automox:
    """
    All docs duplicated from https://docs.automox.com/api/

        The Automox API is a powerful interface that allows you to integrate Automox reporting data into you
    applications and control the various settings of your account.

    All endpoints are only accessible via https and are located at api.automox.com. For instance: you can see events
    associated with your account by accessing the following URL with your ID: (replace API-KEY with your own):

      https://console.automox.com/api/events?api_key=API-KEY

    Limits

    Be nice. If you're sending too many requests too quickly, we'll send back a 429 error code (Too Many Requests). You
    are limited to 5000 requests per hour per api_key overall. Practically, this means you should (when possible)
    authenticate users so that limits are well outside the reach of a given user.

    """

    def __init__(self, api_key):
        self.api_key = api_key

    def _request(self, method, query, data, *path):
        query = query or {}
        query['api_key'] = self.api_key
        url = 'https://console.automox.com/api/{}?{}'.format('/'.join(str(p) for p in path), urlencode(query))
        try:
            return json.loads(urlopen(Request(method=method, data=str(data).encode(), url=url)).read().decode())
        except Exception as e:
            print(url, data)

    def update_approval(self, approval_id: int, approval: str):
        """
        Update a manual approval record. Set manual_approval attribute of approval object to true to approve
        a patch; set it to false to reject a patch
        """
        return self._request('PUT', None, approval, 'approvals', approval_id)
    
    def get_server_queues(self, server_id: int, organization_id: int):
        """Returns the command queue for the specified server (endpoint)"""
        return self._request('GET', {'o': organization_id}, None, 'servers', server_id, 'queues')
    
    def get_user_queues(self, user_id: int):
        """Gets all commands executed for specified user id"""
        return self._request('GET', None, None, 'users', user_id, 'queues')
    
    def issue_command(self, server_id: int, organization_id, command: str):
        """Issue a command to an endpoint. Can be used to install a specific set of patches or reboot an endpoint"""
        return self._request('GET', {'o': organization_id}, {'command': command}, 'servers', server_id, 'queues')
    
    def delete_server(self, server_id: int, organization_id: int):
        return self._request('DELETE', {'o': organization_id}, None, 'servers', server_id)
    
    def get_servers(self, organization_id: int):
        """Gets all Server objects for authenticated user"""
        return self._request('GET', {'o': organization_id}, None, 'servers')
    
    def get_server(self, server_id: int, organization_id: int):
        """Gets a specific Server object for the authenticated user."""
        return self._request('GET', {'o': organization_id}, None, 'servers', server_id)
    
    def get_server_packages(self, server_id: int, organization_id: int):
        """Returns the command queue for the specified server (endpoint)"""
        return self._request('GET', {'o': organization_id}, None, 'servers', server_id, 'packages')
    
    def update_server(self, server_id: int, organization_id: int, server):
        """Updates a Server object"""
        return self._request('PUT', {'o': organization_id}, server, 'servers', server_id)
    
    def get_events(self, ):
        """Gets all Event objects for the authenticated user."""
        return self._request('GET', None, None, 'events')
    
    def get_event(self, event_id: int):
        """Gets a specific Event object for the authenticated user."""
        return self._request('GET', None, None, 'events', event_id)
    
    def delete_servergroup(self, servergroup_id: int, organization_id: int):
        return self._request('DELETE', {'o': organization_id}, None, 'servergroups', servergroup_id)
    
    def get_servergroups(self, organization_id: int):
        """Gets all Server Group objects for authenticated user"""
        return self._request('GET', {'o': organization_id}, None, 'servergroups')
    
    def get_servergroup(self, servergroup_id: int, organization_id: int):
        """Gets a specific Server Group object for the authenticated user."""
        return self._request('GET', {'o': organization_id}, None, 'servergroups', servergroup_id)
    
    def update_servergroup(self, servergroup_id: int, organization_id: int, servergroup: str):
        """Updates a Server Group object"""
        return self._request('PUT', {'o': organization_id}, servergroup, 'servergroups', servergroup_id)
    
    def update_servergroup_2(self, servergroup: str):
        """Updates a Server Group object"""
        return self._request('POST', {'servergroup': servergroup}, None, 'servergroup')
    
    def get_organizations(self, ):
        """Gets all organizations for the api key"""
        return self._request('GET', None, None, 'orgs')
    
    def get_organization_packages(self, organization_id: int):
        """Returns all software packages discovered on all servers (endpoints) of an organization"""
        return self._request('GET', None, None, 'orgs', organization_id, 'packages')
    
    def get_policies(self, organization_id: int):
        """Gets all Policy objects for authenticated user"""
        return self._request('GET', {'o': organization_id}, None, 'policies')
    
    def get_policy(self, policy_id: int, organization_id: int):
        """Gets a specific Policy object for the authenticated user."""
        return self._request('GET', {'o': organization_id}, None, 'policies', policy_id)
    
    def get_policy_stats(self, organization_id: int):
        """Gets all Policy Stats objects for authenticated user"""
        return self._request('GET', {'o': organization_id}, None, 'policystats')
    
    def schedule_policy_remediation(self, policy_id: int, organization_id: int, action: str):
        """Schedule a policy for immediate remediation"""
        return self._request('POST', {'o': organization_id}, action, 'policies', policy_id, 'action')
    
    def update_policy(self, policy_id: int, organization_id: int, policy: str):
        """Updates a Policy object"""
        return self._request('PUT', {'o': organization_id}, policy, 'policies', policy_id)
    
    def get_policysets(self, organization_id: int):
        """Gets all Policy Set objects for authenticated user"""
        return self._request('GET', {'o': organization_id}, None, 'policysets')
    
    def get_prepatch_report(self, start_date: str):
        """Retrieve the prepatch report"""
        return self._request('GET', {'startDate': start_date}, None, 'reports', 'prepatch')
    
    def get_noncompliant_devies_report(self, start_date: str):
        """Retrieve the non compliant devices report"""
        return self._request('GET', {'startDate': start_date}, None, 'reports', 'noncompliance')
    
    def get_users(self, organization_id: int):
        """Gets all User objects for the authenticated user."""
        return self._request('GET', {'o': organization_id}, 'users')
    
    def get_software(self, organization_id: int, name: str=None, limit: int=None, group_id: int=None):
        """Retrieves software packages and patches for an organization, allows filtering the list of software by name"""
        query = {'o': organization_id}
        if name is not None:
            query['name'] = name
        if limit is not None:
            query['limit'] = limit
        if group_id is not None:
            query['groupID'] = group_id
        return self._request('GET', query, None, 'software')

    def get_software_versions(self, organization_id: int, policy_id: int=None, needs_approval: bool=None,
                         needs_attention: bool=None, exceptions: bool=None, pending_update: bool=None,
                         limit: int=None, page: int=None) -> list:
        """
        Retrieves software packages and patches for an organization, specific policy, or just those that need
        [approval | attention | exceptions | pending update].
        """
        query = {'o': organization_id}
        if policy_id is not None:
            query['policyId'] = policy_id
        if needs_approval is not None:
            query['needsApproval'] = needs_approval
        if needs_attention is not None:
            query['needsAttention'] = needs_attention
        if exceptions is not None:
            query['exceptions'] = exceptions
        if pending_update is not None:
            query['pendingUpdate'] = pending_update
        if limit is not None:
            query['l'] = limit
        if page is not None:
            query['p'] = page
        return self._request('GET', query, None, 'software_version')