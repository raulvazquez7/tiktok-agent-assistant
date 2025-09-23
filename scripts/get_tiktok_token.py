"""
This script handles the TikTok OAuth 2.0 flow to obtain an access token.

It starts a temporary local web server to catch the redirect from TikTok after
the user authorizes the application. It then exchanges the authorization code
for an access token and refresh token.
"""
import os
import webbrowser
import requests
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from dotenv import load_dotenv

# --- Configuration ---
load_dotenv()
TIKTOK_CLIENT_KEY = os.getenv("TIKTOK_CLIENT_KEY")
TIKTOK_CLIENT_SECRET = os.getenv("TIKTOK_CLIENT_SECRET")

# IMPORTANT: This must be the EXACT ngrok URL you configured in the TikTok app.
# Make sure your ngrok tunnel is running before executing this script.
REDIRECT_URI = "https://unspangled-swordlike-gricelda.ngrok-free.dev/callback"

# These are the permissions we requested for our app.
SCOPES = "user.info.profile,user.info.stats,video.list"

# Global variable to store the authorization code received from TikTok.
authorization_code = None


class CallbackHandler(BaseHTTPRequestHandler):
    """A simple HTTP request handler to catch the TikTok callback."""

    def do_GET(self) -> None:
        """Handle the GET request from TikTok's redirect."""
        global authorization_code
        parsed_path = urlparse(self.path)
        query_params = parse_qs(parsed_path.query)

        if "code" in query_params:
            authorization_code = query_params["code"][0]
            print("✅ Authorization code received successfully!")
            
            # Send a response to the browser
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"<h1>Success!</h1>")
            self.wfile.write(b"<p>You can close this browser tab now.</p>")
        else:
            print("❌ Error receiving authorization code.")
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"<h1>Error</h1>")
            self.wfile.write(b"<p>Could not retrieve authorization code.</p>")


def get_access_token(code: str) -> None:
    """Exchange the authorization code for an access token."""
    token_url = "https://open.tiktokapis.com/v2/oauth/token/"
    
    params = {
        "client_key": TIKTOK_CLIENT_KEY,
        "client_secret": TIKTOK_CLIENT_SECRET,
        "code": code,
        "grant_type": "authorization_code",
        "redirect_uri": REDIRECT_URI,
    }

    try:
        response = requests.post(token_url, data=params)
        response.raise_for_status()  # Raise an exception for bad status codes
        token_data = response.json()
        
        print("\n--- ✨ Access Token Received! ✨ ---")
        print(f"Access Token: {token_data['access_token']}")
        print(f"Refresh Token: {token_data['refresh_token']}")
        print(f"Expires In (seconds): {token_data['expires_in']}")
        print("\nACTION: Copy the 'Access Token' and add it to your .env file as TIKTOK_ACCESS_TOKEN.")

    except requests.exceptions.RequestException as e:
        print(f"\n--- ❌ Error fetching access token ❌ ---")
        print(f"Status Code: {e.response.status_code}")
        print(f"Response: {e.response.text}")


def main() -> None:
    """Main function to run the authentication flow."""
    # 1. Ensure ngrok is running
    print("--- Step 1: Pre-flight Check ---")
    if "ngrok" not in REDIRECT_URI:
        print("🚨 ERROR: Please update the REDIRECT_URI with your ngrok forwarding URL.")
        return
    print(f"Ensure your ngrok tunnel is running and forwarding to http://localhost:8000")
    print("-" * 50)

    # 2. Construct and open the authorization URL
    auth_url = (
        f"https://www.tiktok.com/v2/auth/authorize/"
        f"?client_key={TIKTOK_CLIENT_KEY}"
        f"&scope={SCOPES}"
        f"&response_type=code"
        f"&redirect_uri={REDIRECT_URI}"
        f"&state=optional_string" # A random string for security
    )
    
    print("--- Step 2: User Authorization ---")
    print("Opening the authorization URL in your browser.")
    print("Please log in to TikTok and authorize the application.")
    webbrowser.open(auth_url)
    print("-" * 50)

    # 3. Start a temporary server to listen for the callback
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, CallbackHandler)
    
    print("--- Step 3: Waiting for Callback ---")
    print("Local server started on port 8000. Waiting for TikTok to redirect...")
    # Handle one request (the callback) and then stop.
    httpd.handle_request()
    httpd.server_close()
    print("Local server stopped.")
    print("-" * 50)

    # 4. Exchange the code for an access token
    if authorization_code:
        print("--- Step 4: Exchanging Code for Token ---")
        get_access_token(authorization_code)
    else:
        print("Could not get authorization code. Aborting.")


if __name__ == "__main__":
    main()
