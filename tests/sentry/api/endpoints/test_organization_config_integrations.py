from __future__ import absolute_import

from django.core.urlresolvers import reverse

from sentry.testutils import APITestCase


class OrganizationConfigIntegrationsTest(APITestCase):
    def test_simple(self):
        self.login_as(user=self.user)

        org = self.create_organization(owner=self.user, name='baz')

        url = reverse('sentry-api-0-organization-config-integrations', args=[org.slug])
        response = self.client.get(url)

        assert response.status_code == 200, response.content
        assert len(response.data['providers']) == 1
        provider = response.data['providers'][0]
        assert provider['id'] == 'example'
        assert provider['name'] == 'Example'
        assert provider['config']
        assert provider['setupUri']
