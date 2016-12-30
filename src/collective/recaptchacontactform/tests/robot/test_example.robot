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

# ${BROWSER}  chrome


*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
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
  Input Text  form.widgets.subject  Hello
  Input Text  form.widgets.message  Lorem ipsum
  Click Button  Send

I fill out all fields and submit the overlay form
  Input Text  form.widgets.sender_fullname  John Doe
  Input Text  form.widgets.sender_from_address  john@example.com
  Input Text  form.widgets.subject  Hello
  Input Text  form.widgets.message  Lorem ipsum
  Click element  css=.plone-modal-footer #form-buttons-send

I confirm that I am not a robot
  Select frame  css=.g-recaptcha iframe
  Click element  css=.recaptcha-checkbox-checkmark
  Unselect frame


# --- THEN -------------------------------------------------------------------

I see a message that I am a robot
  Wait until page contains element  css=.portalMessage
  Page should not contain  Thank you for your feedback
  Page should contain  Please verify that you are not a robot

my message has been sent to the site owner
  Wait until page contains element  css=.portalMessage
  Wait until page contains  Thank you for your feedback
  Page should contain  Thank you for your feedback
