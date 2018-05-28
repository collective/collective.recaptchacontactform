.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

==============================================================================
collective.recaptchacontactform
==============================================================================

.. image:: https://travis-ci.org/collective/collective.recaptchacontactform.svg?branch=master
    :target: https://travis-ci.org/collective/collective.recaptchacontactform

.. image:: https://img.shields.io/pypi/status/collective.recaptchacontactform.svg
    :target: https://pypi.python.org/pypi/collective.recaptchacontactform/
    :alt: Egg Status

.. image:: https://img.shields.io/pypi/v/collective.recaptchacontactform.svg
    :target: https://pypi.python.org/pypi/collective.recaptchacontactform
    :alt: Latest Version

.. image:: https://img.shields.io/pypi/l/collective.recaptchacontactform.svg
    :target: https://pypi.python.org/pypi/collective.recaptchacontactform
    :alt: License

|

.. image:: https://raw.githubusercontent.com/collective/collective.recaptchacontactform/master/kitconcept.png
   :alt: kitconcept
   :target: https://kitconcept.com/

Protect the Plone contact form from spam with reCAPTCHA 2.

This Plone add-on adds a plone.formwidget.recaptcha spam protection field to
the contact form.

.. image:: https://github.com/collective/collective.recaptchacontactform/raw/master/docs/recaptcha-contact-form.png
   :width: 600px
   :alt: Plone reCAPTCHA contact form
   :align: center



Examples
--------

This add-on can be seen in action at the following sites:

- https://extensions.libreoffice.org/


Installation
------------

Install collective.recaptchacontactform by adding it to your buildout::

    [buildout]

    ...

    eggs =
        collective.recaptchacontactform


and then running ``bin/buildout``.

Go to the Plone add-on control panel ("prefs_install_products_form") and install collective.recaptchacontactform.

Then you should see the ReCaptcha control panel ("@@recaptcha-settings").

Go to https://www.google.com/recaptcha/ and register your domain in order to get a "site key" and a "secret key".

Go to the ReCaptcha control panel ("@@recaptcha-settings") and enter those keys into the form. Save the form.

.. image:: https://raw.githubusercontent.com/collective/collective.recaptchacontactform/master/docs/recaptcha-settings.png
   :width: 600px
   :alt: Plone reCAPTCHA control panel
   :align: center


If you go to the contact form now ("contact-info") and you will see an ReCaptcha field at the bottom of the form.


Contribute
----------

- Issue Tracker: https://github.com/collective/collective.recaptchacontactform/issues
- Source Code: https://github.com/collective/collective.recaptchacontactform


Support
-------

If you are having issues, please let us know via the github issue tracker: https://github.com/collective/collective.recaptchacontactform/issues


Credits
-------

.. image:: https://www.documentfoundation.org/assets/Uploads/LibreOffice-Initial-Artwork-Logo-ColorLogoBasic-500px.png
   :width: 250px
   :height: 80px
   :scale: 100 %
   :alt: The Document Foundation
   :align: center
   :target: https://www.documentfoundation.org/

The development of this plugin has been kindly sponsored by `The Document Foundation`_.

.. image:: https://kitconcept.com/logo.png
   :width: 230px
   :height: 50px
   :scale: 100 %
   :alt: kitconcept
   :align: center
   :target: https://www.kitconcept.com/

Developed by `kitconcept`_.

.. _The Document Foundation: https://www.documentfoundation.org/
.. _kitconcept: https://www.kitconcept.com/


License
-------

The project is licensed under the GPLv2.
