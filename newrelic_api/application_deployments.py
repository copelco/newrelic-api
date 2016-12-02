from .base import Resource


class ApplicationDeployments(Resource):
    """
    An interface for interacting with the New Relic Application Instances API.
    """
    def list(self, application_id, page=None):
        """
        This API endpoint returns a paginated list of instances associated with the
        given application.

        Application instances can be filtered by hostname, or the list of
        application instance IDs.

        :type application_id: int
        :param application_id: Application ID

        :type page: int
        :param page: Pagination index

        :rtype: dict
        :return: The JSON response of the API, with an additional 'pages' key
            if there are paginated results

        ::

            {
                "deployment": {
                    "id": "integer",
                    "revision": "string",
                    "changelog": "string",
                    "description": "string",
                    "user": "string",
                    "timestamp": "datetime",
                    "links": {
                    "application": "integer"
                    }
                }
            }

        """
        filters = [
            'page={0}'.format(page) if page else None
        ]
        return self._get(
            url='{root}applications/{application_id}/deployments.json'.format(
                root=self.URL,
                application_id=application_id
            ),
            headers=self.headers,
            params=self.build_param_string(filters)
        )

    def create(self, application_id, deployment):
        """
        This API endpoint returns a single application host, identified by its
        ID.

        :type application_id: int
        :param application_id: Application ID

        :type deployment: json dict
        :param deployment: Deployment Data

                        {
                            "deployment": {
                                "revision": "string",
                                "changelog": "string",
                                "description": "string",
                                "user": "string"
                            }
                        }

        :rtype: dict
        :return: The JSON response of the API

        ::

            {
                "deployment": {
                    "id": "integer",
                    "revision": "string",
                    "changelog": "string",
                    "description": "string",
                    "user": "string",
                    "timestamp": "datetime",
                    "links": {
                        "application": "integer",
                    },
                }
            }

        """
        return self._post(
            url='{root}applications/{application_id}/deployments.json'.format(
                root=self.URL,
                application_id=application_id
            ),
            headers=self.headers,
            data=deployment
        )

    def delete(self, application_id, deployment_id):
        """
        This API endpoint returns a single application host, identified by its
        ID.

        :type application_id: int
        :param application_id: Application ID

        :type deployment_id: json dict
        :param deployment_id: Deployment ID

        :rtype: dict
        :return: The JSON response of the API

        ::

            {
                "deployment": {
                    "id": "integer",
                    "revision": "string",
                    "changelog": "string",
                    "description": "string",
                    "user": "string",
                    "timestamp": "datetime",
                    "links": {
                        "application": "integer"
                    }
                }
            }

        """
        return self._delete(
            url='{root}applications/{application_id}/deployments/{id}.json'.format(
                root=self.URL,
                application_id=application_id,
                id=deployment_id
            ),
            headers=self.headers
        )
