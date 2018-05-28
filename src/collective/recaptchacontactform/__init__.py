# -*- coding: utf-8 -*-
"""Init and utils."""
from Acquisition import aq_inner
from plone import api
from plone.autoform.form import AutoExtensibleForm
from Products.CMFPlone.browser.contact_info import ContactForm
from Products.CMFPlone.browser.interfaces import IContactForm
from zope.i18nmessageid import MessageFactory
from zope.component import getMultiAdapter
from z3c.form import button

import inspect
import Products.CMFPlone.browser.contact_info

_ = MessageFactory('collective.recaptchacontactform')

if AutoExtensibleForm not in inspect.getmro(ContactForm):
    # monkey patch ContactForm class since it is not extensible by default
    # see https://github.com/plone/Products.CMFPlone/issues/1879 for details
    class PatchedContactForm(AutoExtensibleForm, ContactForm):

        ignoreContext = True
        schema = IContactForm

        @button.buttonAndHandler(_(u'label_send', default='Send'), name='send')
        def handle_send(self, action):
            data, errors = self.extractData()

            # recaptcha validation start
            captcha = getMultiAdapter(
                (aq_inner(self.context), self.request),
                name='recaptcha'
            )
            if not captcha.verify():
                api.portal.show_message(
                    'Please verify that you are not a robot',
                    self.request,
                    type=u'error'
                )
                return
            # recaptcha validation end

            if errors:
                api.portal.show_message(
                    self.formErrorsMessage,
                    self.request,
                    type=u'error'
                )
                return

            self.send_message(data)
            self.send_feedback()
            self.success = True

    Products.CMFPlone.browser.contact_info.ContactForm = PatchedContactForm
