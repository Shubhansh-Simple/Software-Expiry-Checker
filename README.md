# Software Expiry Checker

<b>.) Built REST API endpoint that thresholds a user after using any software a certain number of times</b><br>
<b>.) This API endpoint can be implemented in any software that wants to stop its users after crossing a threshold limit</b><br>

### This Application have two api endpoints 
  <b>1.) get/</b><br>
  <b>2.) set/1</b>

### What it does
<b>What get/ request does</b> - Returns how many times users use the software<br>
<b>What set/ request does</b> - It's increment the counting of how many times user uses the software

### What happen after crossing the threshold limits
Return this message as response - <i>You run this software over limit,please contact to your Programmer shubh*....@gmail.com to run more</i>
