# -*- coding: utf-8 -*-
from Products.CMFPlone.interfaces import IMailSchema
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.formwidget.recaptcha.interfaces import IReCaptchaSettings
from plone.registry.interfaces import IRegistry
from plone.testing import z2
from zope.component import queryUtility

import collective.recaptchacontactform


class CollectiveRecaptchacontactformLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=collective.recaptchacontactform)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.recaptchacontactform:default')
        # get registry
        registry = queryUtility(IRegistry)
        if registry is None:
            return
        # mail settings
        mail_settings = registry.forInterface(IMailSchema, prefix='plone')
        if mail_settings is None:
            return
        mail_settings.smtp_host = u'localhost'
        mail_settings.email_from_name = u'Plone Site'
        mail_settings.email_from_address = 'plone@example.com'
        # recaptcha settings
        recaptcha_settings = registry.forInterface(IReCaptchaSettings)
        if recaptcha_settings is None:
            return
        recaptcha_settings.public_key = u'6LeIxAcTAAAAAJcZVRqyHh71UMIEGNQ_MXjiZKhI'  # noqa
        recaptcha_settings.private_key = u'6LeIxAcTAAAAAGG-vFI1TnRWxMZNFuojJ4WifJWe'  # noqa
        recaptcha_settings.display_theme = u'light'
        recaptcha_settings.display_type = u'image'
        recaptcha_settings.display_size = u'normal'


COLLECTIVE_RECAPTCHACONTACTFORM_FIXTURE = CollectiveRecaptchacontactformLayer()


COLLECTIVE_RECAPTCHACONTACTFORM_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_RECAPTCHACONTACTFORM_FIXTURE,),
    name='CollectiveRecaptchacontactformLayer:IntegrationTesting'
)


COLLECTIVE_RECAPTCHACONTACTFORM_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_RECAPTCHACONTACTFORM_FIXTURE,),
    name='CollectiveRecaptchacontactformLayer:FunctionalTesting'
)


COLLECTIVE_RECAPTCHACONTACTFORM_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        COLLECTIVE_RECAPTCHACONTACTFORM_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='CollectiveRecaptchacontactformLayer:AcceptanceTesting'
)
