"""
1. The user visits your website and clicks on the "Login with Google" button.
2. They are redirected to the Google authentication page.
3. The user enters their Google credentials and submits the form.
4. Google verifies the user's credentials and generates an ID token.
5. The user is redirected back to your website with the ID token appended to the URL as a query parameter (e.g.,
    http://yourwebsite.com/auth/google/?id_token=XXXXXXXX).
6. In your Django view, you handle the GET request to the /auth/google/ URL.
7. The GoogleAuthView view is executed, and the get_redirect_url() method is called.
8. Inside get_redirect_url(), you extract the ID token from the query parameters (id_token = self.request.GET.get('id_token')).
9. The authenticate() method of the GoogleBackend is called, passing the request and id_token as arguments.
10. The authenticate() method verifies the ID token with the google-auth library and retrieves the user's email from the token.
11. If the email is valid, the User object associated with the email is retrieved from the database or created if it doesn't exist.
12. The User object is returned from the authenticate() method.
13. If the user is successfully authenticated, the login.py() function is called with the request and the authenticated User.
14. The user is now logged in and redirected to the desired URL (/ in this example).
15. Subsequent requests from the logged-in user will include the session cookie, allowing Django to identify and authenticate the user.

"""