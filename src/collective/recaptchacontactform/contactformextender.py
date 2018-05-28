# -*- coding: utf-8 -*-
from Acquisition import aq_inner
from collective.recaptchacontactform import _
from collective.recaptchacontactform.interfaces import ICollectiveRecaptchacontactformLayer # noqa
from plone.formwidget.recaptcha import ReCaptchaFieldWidget
from plone.z3cform.fieldsets import extensible
from Products.CMFPlone.browser.contact_info import ContactForm
from Products.CMFPlone.interfaces import IPloneSiteRoot
from z3c.form import validator
from z3c.form.field import Fields
from z3c.form.interfaces import IValidator
from zope import component
from zope import schema
from zope.component import getMultiAdapter
from zope.interface import implementer
from zope.interface import Interface
from zope.schema import ValidationError
from zope.schema.interfaces import IField


class NotValidatedReCaptchaCode(ValidationError):
    __doc__ = _(u"Please validate the recaptcha field before sending the form.") # noqa


class IContactFormExtenderFields(Interface):
    captcha = schema.TextLine(title=u'', required=False)


@component.adapter(IPloneSiteRoot, ICollectiveRecaptchacontactformLayer, ContactForm) # noqa
class ContactFormExtender(extensible.FormExtender):

    fields = Fields(IContactFormExtenderFields)
    ignoreContext = True

    def __init__(self, context, request, form):
        self.context = context
        self.request = request
        self.form = form

    def update(self):
        self.add(IContactFormExtenderFields, prefix='')
        self.move('captcha', after='message', prefix='')
        self.form.fields['captcha'].widgetFactory = ReCaptchaFieldWidget


@implementer(IValidator)
@component.adapter(Interface, ICollectiveRecaptchacontactformLayer, Interface, IField, Interface) # noqa
class CaptchaValidator(validator.SimpleFieldValidator):
    # Object, Request, Form, Field, Widget,
    # We adapt the CaptchaValidator class to all form fields (IField)

    def validate(self, value):
        super(CaptchaValidator, self).validate(value)

        captcha = getMultiAdapter(
            (aq_inner(self.context), self.request),
            name='recaptcha'
        )
        if not captcha.verify():
            raise NotValidatedReCaptchaCode
        else:
            return True


# Register Captcha validator for the Captcha field in the
# IContactFormExtenderFields Form
validator.WidgetValidatorDiscriminators(
    CaptchaValidator, field=IContactFormExtenderFields['captcha'])
