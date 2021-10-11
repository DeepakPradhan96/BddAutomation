Feature:  Verifying Registation Functionality




  @sanaty
  Scenario: Registation With Valid Data
  Given  User is on Registation Page
  When   User Enter Username
  And    User Enter Email id
  And    User Enter Password
  And    User Click on Signup Button
  Then   User Should be Register Successfully


   @smoke @sanaty
  Scenario: Registation With Dupilicate Data
  Given  User is on Registation Page
  When   User Enter Dupilicate Username
  And    User Enter Email id
  And    User Enter Password
  And    User Click on Signup Button
  Then   User Should be Register Successfully


   @abcd
  Scenario: Registation With Dupilicate Data
      Given  User is on Registation Page
      When   User Enter Dupilicate Username
      And    User Enter Email id
      And    User Enter Password
      And    User Click on Signup Button
      Then   User Should be Register Successfully



