from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
import os
import subprocess

def htop(request):
   
    username = os.getenv('USER') or os.getenv('USERNAME')    
    server_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
    top_output = subprocess.check_output(['top', '-b', '-n', '1']).decode('utf-8')

    return HttpResponse(f'''
    <html>
        <body>
            <h1>System Information</h1>
            <p>Name: M Manikanth</p>
            <p>Username: {username}</p>
            <p>Server Time (IST): {server_time}</p>
            <h2>Top Output:</h2>
            <pre>{top_output}</pre>
        </body>
    </html>
    ''')