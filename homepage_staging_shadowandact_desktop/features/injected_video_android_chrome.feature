Feature: Verify presense of injected video and pic in pic for article link in staging.shadowandact.com on mobile android chrome - BrowserStack

  Scenario: Verify presense of injected video and pic in pic for article link in staging.shadowandact.com on mobile android chrome - BrowserStack
      Given the chrome browser is launched and load the staging.shadowandact.com app on mobile android
      Then verify on mobile the application is launched successfully
      Then navigate to and load the initial article from most popular section of the home page on mobile
      Then verify if the injected video is auto playing
      Then verify if Read Full Article Button is functioning as required
      #Then close the browser