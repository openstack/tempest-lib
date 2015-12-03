# Copyright 2012 OpenStack Foundation
# Copyright 2013 Hewlett-Packard Development Company, L.P.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from oslo_serialization import jsonutils as json

from tempest_lib.api_schema.response.compute.v2_1 import servers as schema
from tempest_lib.common import rest_client


class ServerGroupsClient(rest_client.RestClient):

    def create_server_group(self, **kwargs):
        """Create the server group

        name : Name of the server-group
        policies : List of the policies - affinity/anti-affinity)

        """
        post_body = json.dumps({'server_group': kwargs})
        resp, body = self.post('os-server-groups', post_body)

        body = json.loads(body)
        self.validate_response(schema.create_show_server_group, resp, body)
        return rest_client.ResponseBody(resp, body)

    def delete_server_group(self, server_group_id):
        """Delete the given server-group."""
        resp, body = self.delete("os-server-groups/%s" % server_group_id)
        self.validate_response(schema.delete_server_group, resp, body)
        return rest_client.ResponseBody(resp, body)

    def list_server_groups(self):
        """List the server-groups."""
        resp, body = self.get("os-server-groups")
        body = json.loads(body)
        self.validate_response(schema.list_server_groups, resp, body)
        return rest_client.ResponseBody(resp, body)

    def show_server_group(self, server_group_id):
        """Get the details of given server_group."""
        resp, body = self.get("os-server-groups/%s" % server_group_id)
        body = json.loads(body)
        self.validate_response(schema.create_show_server_group, resp, body)
        return rest_client.ResponseBody(resp, body)
