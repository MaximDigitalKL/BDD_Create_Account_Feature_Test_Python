# Exploratory_Testing
Python BDD library 
I created a few scenarios per each time of testing (Positive testing, Negative Testing, Equivalenge and Boundry Limit Testing, Sanity Testing)

Captcha

-I managed to find a loophole to pass captcha on the page fairly easy, it is not 100% it still fails on occasion

- I am sure with more thought into the issue I will be able to cover all scenarios

- To be clarified if it was by design this way, or it should be automation/bot proof
        
Boundry Limit - Scenario 2 upper limit I found a Bug on the First Name field, I managed to create accounts with 31 and 56 characters First Name. 
                HTML script says limit should be 30
                
Sanity Test - Scenario 2 I found another pontetial BUG (not sure it was intended this way) but I could create account with a 50 digit phone number. 
                 HTML says 80 digits limit. I belive it should be alot lower, or better yet, corelated with Country Phone number length size.
            - Scenario 3 Clarification is needed if it is ok to be able to change country ID on the phone number section of the page.
                 My asumtion since they get populated automatically to be corenalted and  to not be able to change.
