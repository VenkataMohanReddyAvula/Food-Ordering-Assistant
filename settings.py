        INSTALLED_APPS = [
            # ...
            'corsheaders',
            # ...
        ]

        MIDDLEWARE = [
            'corsheaders.middleware.CorsMiddleware', # Must be very high, preferably first
            'django.middleware.security.SecurityMiddleware',
            # ...
        ]

        CORS_ALLOWED_ORIGINS = [
            "http://localhost:3000", # Example if your frontend is on React dev server
            "http://127.0.0.1:5500", # Example if using Live Server VS Code extension
            "http://127.0.0.1:5000", # If your frontend is served from a different port on localhost
            # Add the exact origin(s) where your frontend is running
        ]
        # Or, for development, to allow all origins (less secure for production):
        CORS_ALLOW_ALL_ORIGINS = True
        
