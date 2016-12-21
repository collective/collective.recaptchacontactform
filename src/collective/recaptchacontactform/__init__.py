# -*- coding: utf-8 -*-
"""Init and utils."""
from plone.autoform.form import AutoExtensibleForm
from Products.CMFPlone.browser.contact_info import ContactForm
from Products.CMFPlone.browser.interfaces import IContactForm
from zope.i18nmessageid import MessageFactory

import Products.CMFPlone.browser.contact_info

_ = MessageFactory('collective.recaptchacontactform')


# monkey patch ContactForm class since it is not extensible by default
# see https://github.com/plone/Products.CMFPlone/issues/1879 for details
class PatchedContactForm(AutoExtensibleForm, ContactForm):

    ignoreContext = True
    schema = IContactForm


Products.CMFPlone.browser.contact_info.ContactForm = PatchedContactForm
