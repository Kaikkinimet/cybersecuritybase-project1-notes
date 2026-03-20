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
**Description:** The application allows users to access notes only by using the note ID in the URL. In the vulnerable version, there is no check that the note actually belongs to the logged in user. Because of this, any user can change the ID in the URL and open someone else’s note. This is a common access control problem, because the system does not check permissions properly. This can be very dangerous, because notes can contain private or sensitive information. In real applications, this kind of issue could lead to leaking personal or confidential data to other users. <br>
**Fix:** The fix is to check that the note belongs to the current user every time it is requested. Instead of getting the note only by ID, the query must also include the owner. In Django this can be done with owner=request.user. After this change, user cannot access other users notes even if they try to change the URL. This shows that authentication is not enough, also authorization must be checked. <br>
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
The delete function was vulnerable to CSRF because the protection was disabled and the form did not include CSRF token. This means that attacker can create another page which sends request to delete note. If user is logged in, the request will be accepted because browser sends session automatically. This is dangerous because user does not need to click anything in the application, just opening malicious page is enough. In this project, note could be deleted without user knowing it.
<br>
**Fix:**
The fix is to use Django CSRF protection correctly. First, remove @csrf_exempt so that Django checks requests normally. Then add {% csrf_token %} to the form. After this, only valid requests from the application are accepted. If attacker tries to send request from other site, it will fail because token is missing. It is important that all actions that change data use CSRF protection.
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
**Description:** The search function was vulnerable to SQL injection because user input was directly added into SQL query. This means user input was not handled safely and it became part of the SQL command. Because of this, attacker can give special input which changes how the query works. SQL injection is very serious vulnerability and it can allow attacker to read or modify database data. In worst case, attacker can even delete data or get full access to database. The problem here is that user input and SQL code were mixed together. <br>
**Fix:** The fix is to not build SQL queries by joining strings. User input should never be added directly to SQL. Instead, Django ORM should be used, for example title__icontains=query. ORM handles input safely and prevents injection. Another option is to use parameterized queries. The important idea is that user input must be treated as data, not as part of SQL command. <br>
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
The application was misconfigured because it was running with DEBUG=True. This is useful in development, but it should not be used when application is available to users. When error happens, Django shows detailed debug page which includes file paths, code lines and other internal information. In this project, the error page showed many details about the system. This information can help attacker to understand how application works and find more vulnerabilities. So even if code is correct, bad configuration can make system unsafe.
<br>
**Fix:** 
The fix is to set DEBUG=False when application is used outside development. After this, users will only see simple error page and not internal details. Also ALLOWED_HOSTS should be set properly. This reduces information leakage. It is important to remember that security is not only about code, but also about correct configuration.
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
The application exposed sensitive data by showing users password hashes on a page. Even though passwords are hashed, they are still sensitive and should not be visible. If attacker gets these hashes, they can try to crack them offline. This is bad practice and shows that application does not protect sensitive data properly. In this project, debug page showed usernames and password hashes, which should never happen in real system.
<br>
**Fix:** The fix is to not show password hashes or any authentication related data in templates or responses. Only necessary information should be shown to users. In this case, only username is enough. Developers should be careful with debug pages, because they can easily leak sensitive information. The main idea is to minimize data exposure and protect all sensitive data.
<br>
**Before screenshot:** https://github.com/Kaikkinimet/cybersecuritybase-project1-notes/blob/main/screenshots/flaw-5-before-1.png
<br>
**After screenshot:** https://github.com/Kaikkinimet/cybersecuritybase-project1-notes/blob/main/screenshots/flaw-5-after-1.png
<br>




