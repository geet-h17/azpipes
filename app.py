from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def welcome():
    # HTML template for the welcome page
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Welcome</title>
        <style>
            body { font-family: Arial, sans-serif; background-color: #f4f4f4; color: #333; text-align: center; padding: 50px; }
            .container { max-width: 600px; margin: 0 auto; padding: 20px; background: #fff; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); }
            h1 { color: #007bff; }
            p { font-size: 1.2em; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Welcome to the AppSecEngineer Course on ACR</h1>
            <p>This app is running on a Docker container built on top of the OWASP Juice Shop base image!</p>
            <p>Get ready to dive deep into application security and containerized environments.</p>
        </div>
    </body>
    </html>
    """
    return render_template_string(html)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
