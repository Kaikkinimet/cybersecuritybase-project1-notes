# Part I, Project I: Project report
## OWASP Top 10 (2021) vulnerabilities demonstrated in this project:
This is a simple Django web application that demonstrates 5 common security vulnerabilities from **OWASP Top 10 (2021)** and their fixes.  
Link: (https://github.com/Kaikkinimet/cybersecuritybase-project1-notes) <br>

## Installation instructions:

### Requirements

- Python 3.x
- pip

### Installation instructions and setup:
*1. Clone the repository:*
```
git clone https://github.com/Kaikkinimet/cybersecuritybase-project1-notes.git
cd cybersecuritybase-project1-notes
```
*2. Create a virtual environment:*
```
python3 -m venv venv
```
*3. Activate the virtual environment*
```
Mac/Linux: source venv/bin/activate
Windows: venv\Scripts\activate
```
*4. Install dependencies:*
```
pip install django
```
*5. Run database migrations:*
```
python3 manage.py migrate
```
*6. Start the development server:*
```
python3 manage.py runserver
```

### Usage
- Register a new user
- Login
- Add, view, search and delete notes
<br>

## 5 OWASP Vulnerabilities Demonstrated (FLAWS):

### **FLAW 1: Broken Access Control (A01)**
**File:** https://github.com/Kaikkinimet/cybersecuritybase-project1-notes/blob/3194253d91ac7ee7eed77805fdc2b43a30880c0e/pages/views.py#L43
<br>
**Description:** The application allows users to access any note by its ID without checking ownership. This means that any authenticated user can view other users’ notes simply by modifying the URL. This vulnerability can lead to unauthorized access to other users’ private data. In a real-world application, this could expose sensitive personal information or confidential content.<br>
**Fix:** Restrict access by ensuring that the requested note belongs to the currently logged-in user. This can be done by adding an ownership check in the query (owner=request.user).<br>
**Before screenshot:**
https://github.com/Kaikkinimet/cybersecuritybase-project1-notes/blob/main/screenshots/flaw-1-before-1.png<br>
**After screenshot:**
https://github.com/Kaikkinimet/cybersecuritybase-project1-notes/blob/main/screenshots/flaw-1-after-1.png

### **FLAW 2: Cross-Site Request Forgery (CSRF)**
**File:** https://github.com/Kaikkinimet/cybersecuritybase-project1-notes/blob/526b4c7d22e08eee8198d007e7226aa03625cc25/pages/views.py#L7
https://github.com/Kaikkinimet/cybersecuritybase-project1-notes/blob/526b4c7d22e08eee8198d007e7226aa03625cc25/pages/templates/pages/delete_note.html#L8
https://github.com/Kaikkinimet/cybersecuritybase-project1-notes/blob/0869425df703ccce7b7f45987c385cdcdaff7801/csrf_test.html#L1
<br>
**Description:**
The delete functionality was vulnerable to Cross-Site Request Forgery because CSRF protection was disabled and the form did not include a CSRF token. This allowed an attacker to forge a POST request that deleted a note on behalf of a logged-in user. This type of attack is especially dangerous because the victim does not need to interact with the application directly; simply visiting a malicious page can trigger the action.
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


### **FLAW 3: SQL Injection (A03)**
**File:**
https://github.com/Kaikkinimet/cybersecuritybase-project1-notes/blob/c5f4d196d547b3c5b7f67fa1340202554e0adc27/pages/views.py#L75
https://github.com/Kaikkinimet/cybersecuritybase-project1-notes/blob/c5f4d196d547b3c5b7f67fa1340202554e0adc27/pages/templates/pages/search.html#L5
<br>
**Description:** The search functionality was vulnerable to SQL injection because user input was directly concatenated into a raw SQL query. This allowed a malicious user to manipulate the query logic by entering crafted input. SQL injection is one of the most critical web vulnerabilities. It can allow attackers to read, modify, or delete database contents, and in some cases even execute administrative operations. <br>
**Fix:** Do not build SQL queries by concatenating user input. Use Django ORM filtering or parameterized queries so that input is treated as data instead of executable SQL. <br>
**Before screenshot:**
https://github.com/Kaikkinimet/cybersecuritybase-project1-notes/blob/main/screenshots/flaw-3-before-1.png
<br>
**After screenshot:**
https://github.com/Kaikkinimet/cybersecuritybase-project1-notes/blob/main/screenshots/flaw-3-after-1.png
<br>  

### **FLAW 4: Security Misconfiguration (A05)**
**File:** 
https://github.com/Kaikkinimet/cybersecuritybase-project1-notes/blob/0869425df703ccce7b7f45987c385cdcdaff7801/config/settings.py#L124
https://github.com/Kaikkinimet/cybersecuritybase-project1-notes/blob/0869425df703ccce7b7f45987c385cdcdaff7801/pages/urls.py#L12
https://github.com/Kaikkinimet/cybersecuritybase-project1-notes/blob/0869425df703ccce7b7f45987c385cdcdaff7801/pages/views.py#L109
<br>
**Description:** 
The application is misconfigured because it runs with DEBUG=True, which exposes detailed internal error messages, stack traces, file paths, and other implementation details to users. This information can help an attacker understand the system and identify further attack paths.
<br>
**Fix:** 
Set DEBUG=False in production so that internal errors are not shown to users. This prevents sensitive implementation details from being exposed.
<br>
**Before screenshot:** 
https://github.com/Kaikkinimet/cybersecuritybase-project1-notes/blob/main/screenshots/flaw-4-before-1.png
<br>
**After screenshot:** 
https://github.com/Kaikkinimet/cybersecuritybase-project1-notes/blob/main/screenshots/flaw-4-after-1.png
<br>


### **FLAW 5: Sensitive Data Exposure (A02)**
**File:** 
https://github.com/Kaikkinimet/cybersecuritybase-project1-notes/blob/0869425df703ccce7b7f45987c385cdcdaff7801/pages/templates/pages/debug_users.html#L1
https://github.com/Kaikkinimet/cybersecuritybase-project1-notes/blob/0869425df703ccce7b7f45987c385cdcdaff7801/pages/urls.py#L14
https://github.com/Kaikkinimet/cybersecuritybase-project1-notes/blob/0869425df703ccce7b7f45987c385cdcdaff7801/pages/views.py#L103
<br>
**Description:**
The application exposes sensitive authentication data by displaying users’ password hashes on a page. Even though the passwords are hashed, this information is still sensitive and should never be disclosed to users.
<br>
**Fix:** Do not expose password hashes or other authentication-related data in responses or templates. Only show non-sensitive user information that is actually needed.
<br>
**Before screenshot:** https://github.com/Kaikkinimet/cybersecuritybase-project1-notes/blob/main/screenshots/flaw-5-before-1.png
<br>
**After screenshot:** https://github.com/Kaikkinimet/cybersecuritybase-project1-notes/blob/main/screenshots/flaw-5-after-1.png
<br>




