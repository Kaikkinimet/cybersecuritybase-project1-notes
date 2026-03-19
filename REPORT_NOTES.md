# OWASP list used: 2021

[(https://github.com/Kaikkinimet/cybersecuritybase-project1-notes)] <br>

*installation instructions if needed.....]*<br>


*(Add source link to each flaw if appropriate. Ideally, the link should have the format https://urldomain/repo/file.py#L42 (Line 42 in file.py). The links can be easily obtained by clicking the line numbers in the Github repository file browser. If the flaw involves in omitting some code, then comment-out the code, and provide the link to the beginning of the commented block.)*


### **FLAW 1: Broken Access Control**
https://github.com/Kaikkinimet/cybersecuritybase-project1-notes/blob/3194253d91ac7ee7eed77805fdc2b43a30880c0e/pages/views.py#L43
<br>
**Description:** The application allows users to access any note by its ID without checking ownership. This means that any authenticated user can view other users’ notes simply by modifying the URL.<br>
**Fix:** Restrict access by ensuring that the requested note belongs to the currently logged-in user. This can be done by adding an ownership check in the query (owner=request.user).<br>
**Before screenshot:**
https://github.com/Kaikkinimet/cybersecuritybase-project1-notes/blob/main/screenshots/flaw-1-before-1.png<br>
**After screenshot:**
https://github.com/Kaikkinimet/cybersecuritybase-project1-notes/blob/main/screenshots/flaw-1-after-1.png

### **FLAW 2: CSRF**
**File:** https://github.com/Kaikkinimet/cybersecuritybase-project1-notes/blob/526b4c7d22e08eee8198d007e7226aa03625cc25/pages/views.py#L7
https://github.com/Kaikkinimet/cybersecuritybase-project1-notes/blob/526b4c7d22e08eee8198d007e7226aa03625cc25/pages/templates/pages/delete_note.html#L8
<br>
**Description:**
The delete functionality was vulnerable to Cross-Site Request Forgery because CSRF protection was disabled and the form did not include a CSRF token. This allowed an attacker to forge a POST request that deleted a note on behalf of a logged-in user.
<br>
**Fix:**
Remove @csrf_exempt and include {% csrf_token %} in the delete form. This ensures that only legitimate requests created by the application are accepted.
<br>
**Before screenshot:**
https://github.com/Kaikkinimet/cybersecuritybase-project1-notes/blob/main/screenshots/flaw-2-before-1.png
https://github.com/Kaikkinimet/cybersecuritybase-project1-notes/blob/main/screenshots/flaw-2-before-2.png
<br>
**After screenshot:**
https://github.com/Kaikkinimet/cybersecuritybase-project1-notes/blob/main/screenshots/flaw-2-after-1.png
https://github.com/Kaikkinimet/cybersecuritybase-project1-notes/blob/main/screenshots/flaw-2-after-2.png
<br>


### **FLAW 3: Injection**
**File:**  
https://github.com/Kaikkinimet/cybersecuritybase-project1-notes/blob/c5f4d196d547b3c5b7f67fa1340202554e0adc27/pages/views.py#L75
https://github.com/Kaikkinimet/cybersecuritybase-project1-notes/blob/c5f4d196d547b3c5b7f67fa1340202554e0adc27/pages/templates/pages/search.html#L5
<br>
**Description:** The search functionality was vulnerable to SQL injection because user input was directly concatenated into a raw SQL query. This allowed a malicious user to manipulate the query logic by entering crafted input.<br>
**Fix:** Do not build SQL queries by concatenating user input. Use Django ORM filtering or parameterized queries so that input is treated as data instead of executable SQL. <br>
**Before screenshot:**  
https://github.com/Kaikkinimet/cybersecuritybase-project1-notes/blob/main/screenshots/flaw-3-before-1.png
<br>
**After screenshot:**  
https://github.com/Kaikkinimet/cybersecuritybase-project1-notes/blob/main/screenshots/flaw-3-after-1.png
<br>

### **FLAW 4: Security Misconfiguration**
**File:** <br>
**Description:** <br>
**Fix:** <br>
**Before screenshot:**  
<br>
**After screenshot:**  
<br>

### **FLAW 5: Identification and Authentication Failures**
**File:** <br>
**Description:** <br>
**Fix:** <br>
**Before screenshot:** <br>
**After screenshot:** <br>
