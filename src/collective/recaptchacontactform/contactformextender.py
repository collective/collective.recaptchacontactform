# -*- coding: utf-8 -*-
from plone.z3cform.fieldsets import extensible
from Products.CMFPlone.browser.contact_info import ContactForm
from Products.CMFPlone.interfaces import IPloneSiteRoot

from z3c.form.field import Fields
from zope import component
from zope import schema
from zope.interface import Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class IContactFormExtenderFields(Interface):
    website = schema.TextLine(title=u'Website', required=False)


@component.adapter(IPloneSiteRoot, IDefaultBrowserLayer, ContactForm)
class ContactFormExtender(extensible.FormExtender):

    fields = Fields(IContactFormExtenderFields)
    ignoreContext = True

    def __init__(self, context, request, form):
        self.context = context
        self.request = request
        self.form = form

    def update(self):
        self.add(IContactFormExtenderFields, prefix='')
        self.move('website', after='message', prefix='')
