OWASP list used: 2021
Link: Link to the repository......
installation instructions if needed.....
(Add source link to each flaw if appropriate. Ideally, the link should have the format https://urldomain/repo/file.py#L42 (Line 42 in file.py). The links can be easily obtained by clicking the line numbers in the Github repository file browser. If the flaw involves in omitting some code, then comment-out the code, and provide the link to the beginning of the commented block.)


FLAW 1: Broken Access Control
File: exact source link pinpointing flaw 1... (pages/views.py)
Description: The application allows users to access any note by its ID without checking ownership. This means that any authenticated user can view other users’ notes simply by modifying the URL.
Fix: Restrict access by ensuring that the requested note belongs to the currently logged-in user. This can be done by adding an ownership check in the query (owner=request.user).
Before screenshot: link....
After screenshot: link....

Flaw 2: CSRF
File: exact source link pinpointing flaw 1... (pages/views.py)
Description: view_note
Fix:
Before screenshot:
After screenshot:


Flaw 3: Injection
File:
Idea:
Before screenshot:
After screenshot:
Fix:

Flaw 4: Security Misconfiguration
File:
Idea:
Before screenshot:
After screenshot:
Fix:

Flaw 5: Identification and Authentication Failures
File:
Idea:
Before screenshot:
After screenshot:
Fix: