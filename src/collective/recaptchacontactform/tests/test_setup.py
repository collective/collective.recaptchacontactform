# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from collective.recaptchacontactform.testing import COLLECTIVE_RECAPTCHACONTACTFORM_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that collective.recaptchacontactform is properly installed."""

    layer = COLLECTIVE_RECAPTCHACONTACTFORM_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if collective.recaptchacontactform is installed."""
        self.assertTrue(
            self.installer.isProductInstalled(
                'collective.recaptchacontactform'
            )
        )

    def test_plone_formwidget_recaptcha_dependency_installed(self):
        self.assertTrue(
            self.installer.isProductInstalled(
                'plone.formwidget.recaptcha'
            )
        )

    def test_browserlayer(self):
        """Test that ICollectiveRecaptchacontactformLayer is registered."""
        from collective.recaptchacontactform.interfaces import (
            ICollectiveRecaptchacontactformLayer)
        from plone.browserlayer import utils
        self.assertIn(
            ICollectiveRecaptchacontactformLayer,
            utils.registered_layers()
        )


class TestUninstall(unittest.TestCase):

    layer = COLLECTIVE_RECAPTCHACONTACTFORM_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['collective.recaptchacontactform'])

    def test_product_uninstalled(self):
        """Test if collective.recaptchacontactform is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'collective.recaptchacontactform'))

    def test_browserlayer_removed(self):
        """Test that ICollectiveRecaptchacontactformLayer is removed."""
        from collective.recaptchacontactform.interfaces import \
            ICollectiveRecaptchacontactformLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            ICollectiveRecaptchacontactformLayer,
            utils.registered_layers()
        )
