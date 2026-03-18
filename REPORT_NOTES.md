# OWASP list used: 2021
[
installation instructions if needed.....](https://github.com/Kaikkinimet/cybersecuritybase-project1-notes) <br>

*(Add source link to each flaw if appropriate. Ideally, the link should have the format https://urldomain/repo/file.py#L42 (Line 42 in file.py). The links can be easily obtained by clicking the line numbers in the Github repository file browser. If the flaw involves in omitting some code, then comment-out the code, and provide the link to the beginning of the commented block.)*


### **FLAW 1: Broken Access Control**
https://github.com/Kaikkinimet/cybersecuritybase-project1-notes/blob/3194253d91ac7ee7eed77805fdc2b43a30880c0e/pages/views.py#L43 <br>
**Description:** The application allows users to access any note by its ID without checking ownership. This means that any authenticated user can view other users’ notes simply by modifying the URL.<br>
**Fix:** Restrict access by ensuring that the requested note belongs to the currently logged-in user. This can be done by adding an ownership check in the query (owner=request.user).<br>
**Before screenshot:** https://github.com/Kaikkinimet/cybersecuritybase-project1-notes/blob/main/screenshots/flaw-1-before-1.png<br>
**After screenshot:** https://github.com/Kaikkinimet/cybersecuritybase-project1-notes/blob/main/screenshots/flaw-1-after-1.png

### **Flaw 2: CSRF**
**File:** <br>
**Description:** <br>
**Fix:** <br>
**Before screenshot:** <br>
**After screenshot:** <br>


### **Flaw 3: Injection**
**File:** <br>
**Description:** <br>
**Fix:** <br>
**Before screenshot:** <br>
**After screenshot:** <br>

### **Flaw 4: Security Misconfiguration**
**File:** <br>
**Description:** <br>
**Fix:** <br>
**Before screenshot:** <br>
**After screenshot:** <br>

### **Flaw 5: Identification and Authentication Failures**
**File:** <br>
**Description:** <br>
**Fix:** <br>
**Before screenshot:** <br>
**After screenshot:** <br>
