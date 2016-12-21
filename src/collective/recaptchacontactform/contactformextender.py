# -*- coding: utf-8 -*-
from persistent import Persistent
from plone.z3cform.fieldsets import extensible
from Products.CMFPlone.browser.contact_info import ContactForm

from z3c.form.field import Fields
from zope import interface
from zope import schema
from zope.annotation import factory
from zope.component import adapts
from zope.interface import Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class IContactFormExtenderFields(Interface):
    website = schema.TextLine(title=u'Website', required=False)


class ContactFormExtenderFields(Persistent):
    interface.implements(IContactFormExtenderFields)
    adapts(Interface)
    website = u''


ContactFormExtenderFactory = factory(ContactFormExtenderFields)


class ContactFormExtender(extensible.FormExtender):
    adapts(Interface, IDefaultBrowserLayer, ContactForm)

    fields = Fields(IContactFormExtenderFields)

    def __init__(self, context, request, form):
        self.context = context
        self.request = request
        self.form = form

    def update(self):
        # Add the fields defined in ICommentExtenderFields to the form.
        self.add(IContactFormExtenderFields, prefix='')
        # Move the website field to the top of the comment form.
        self.move('website', before='message', prefix='')
