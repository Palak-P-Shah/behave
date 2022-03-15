Feature: Verify presense of injected video and pic in pic for article link in 21ninety.com on mobile android chrome - BrowserStack

  Scenario: Verify presense of injected video and pic in pic for article link in 21ninety.com on mobile android chrome - BrowserStack
      Given the chrome browser is launched and load the 21ninety.com app on mobile android
      Then verify on mobile the application is launched successfully
      Then navigate to and load the article of the home page on mobile
      Then verify if the injected video is auto playing
      Then verify if pic in pic window is appearing as required on page scroll
     # Then verify if Read Full Article Button is functioning as required
      #Then close the browser