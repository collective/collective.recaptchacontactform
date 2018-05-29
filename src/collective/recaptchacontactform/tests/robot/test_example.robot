# ============================================================================
# EXAMPLE ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s collective.recaptchacontactform -t test_example.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src collective.recaptchacontactform.testing.COLLECTIVE_RECAPTCHACONTACTFORM_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot src/collective/recaptchacontactform/tests/robot/test_example.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Variables ***

${BROWSER}  chrome


*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open chrome browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a system I want to protect the contact form from spam
  Given a contact form
   When I fill out all fields and submit the form
   Then I see a message that I am a robot

Scenario: As a system I want to protect the contact form in an overlay from spam
  Given a contact form in an overlay
   When I fill out all fields and submit the overlay form
   Then I see a message that I am a robot

Scenario: As an anonymous user I can send a message to the site owner
  Given a contact form
   When I confirm that I am not a robot
    and I fill out all fields and submit the form
   Then my message has been sent to the site owner

Scenario: As an anonymous user I can send a message to the site owner in an overlay
  Given a contact form in an overlay
   When I confirm that I am not a robot
    and I fill out all fields and submit the overlay form
# XXX: This line fails due to a bug in Plone:
# https://github.com/plone/Products.CMFPlone/issues/1886
#   Then my message has been sent to the site owner



*** Keywords *****************************************************************


# --- Setup ------------------------------------------------------------------

Open chrome browser
  ${options}=  Evaluate  sys.modules['selenium.webdriver'].ChromeOptions()  sys, selenium.webdriver
  # Call Method  ${options}  add_argument  headless
  Call Method  ${options}  add_argument  disable-extensions
  Call Method  ${options}  add_argument  disable-web-security
  Call Method  ${options}  add_argument  window-size\=1280,1024
  # Call Method  ${options}  add_argument  remote-debugging-port\=9223
  Create WebDriver  Chrome  chrome_options=${options}

# --- Given ------------------------------------------------------------------

a contact form
  Go to  ${PLONE_URL}/contact-info
  Wait until page contains  Contact form
  Wait until page contains element  css=#form-widgets-sender_fullname

a contact form in an overlay
  Go to  ${PLONE_URL}
  Wait until page contains element  xpath=//a[contains(@href, 'contact-info')]
  Click link  xpath=//a[contains(@href, 'contact-info')]
  Wait until page contains element  css=#form-widgets-sender_fullname


# --- WHEN -------------------------------------------------------------------

I fill out all fields and submit the form
  Input Text  form.widgets.sender_fullname  John Doe
  Input Text  form.widgets.sender_from_address  john@example.com
  # XXX: no idea why name selector does not work here.
  Input Text  css=#form-widgets-subject  Hello
  Input Text  form.widgets.message  Lorem ipsum
  Sleep  2
  Input Text  css=#form-widgets-subject  Hello
  Input Text  css=#form-widgets-sender_from_address  john@example.com
  Click Button  Send

I fill out all fields and submit the overlay form
  Input Text  form.widgets.sender_fullname  John Doe
  Input Text  form.widgets.sender_from_address  john@example.com
  Input Text  form.widgets.subject  Hello
  Input Text  form.widgets.message  Lorem ipsum
  Sleep  2
  Input Text  css=#form-widgets-subject  Hello
  Input Text  css=#form-widgets-sender_from_address  john@example.com
  Click element  css=.plone-modal-footer #form-buttons-send

I confirm that I am not a robot
  Wait until page contains element  css=.g-recaptcha iframe
  Select frame  css=.g-recaptcha iframe
  Wait until page contains element  css=.recaptcha-checkbox-checkmark
  Click element  css=.recaptcha-checkbox-checkmark
  Unselect frame


# --- THEN -------------------------------------------------------------------

I see a message that I am a robot
  Wait until page contains element  css=.portalMessage
  Page should not contain  Thank you for your feedback
  Page should contain  Please validate the recaptcha field before sending the form.

my message has been sent to the site owner
  # Wait until page contains  A mail has now been sent
  Wait until page contains element  css=.portalMessage
  # Page should contain element  css=.info
  ${src}=  Selenium2Library.Get Source
  Log  ${src}  WARN
  Wait until page contains  Thank you for your feedback
  Page should contain  Thank you for your feedback
