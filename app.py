from flask import Flask, render_template, request, logging, Response, redirect, flash

# Flask ‚Ì‹N“®
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

app.run(host="localhost")