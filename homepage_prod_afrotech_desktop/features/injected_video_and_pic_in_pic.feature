Feature: Verify presense of injected video and pic in pic for article link in afrotech.com - BrowserStack

  Scenario: Verify presense of injected video and pic in pic for article link in afrotech.com - BrowserStack
      Given the browser is launched and load the afrotech.com app
      Then verify the application is launched successfully
      Then navigate to and load the initial article from most popular section of the home page
      Then verify if the injected video is auto playing
      Then verify if pic in pic window is appearing as required on page scroll
     # Then verify if Read Full Article Button is functioning as required
      #Then close the browser