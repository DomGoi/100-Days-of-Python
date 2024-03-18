
from flask import Flask, render_template, request
from post import Post
import smtplib

app = Flask(__name__)

posts=Post()
all_posts=posts.posts_get()

@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)

@app.route('/post/<int:num>')
def get_blog(num):
    post = None
    for blog_post in all_posts:
        if blog_post['id'] == num:
            
            post = blog_post
              
    return render_template('post.html', post=post)



@app.route('/about')
def about():
    return render_template("about.html")
     
     
@app.route('/contact')
def contact():
    return render_template("contact.html")

     

@app.route('/form-entry', methods=["POST"])
def get_data():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["mail"]
        message = request.form["message"]

        if message.strip():  # Check if message is not empty
            try:
                mymail = "kyrielazone@gmail.com"  # Get email from environment variable
                password = "roer sreg gqot mwwp "  # Get email password from environment variable
                
                with smtplib.SMTP("smtp.gmail.com") as connection:
                    connection.starttls()
                    connection.login(user=mymail, password=password)
                    connection.sendmail(from_addr=mymail, to_addrs="kyrielazone@gmail.com", msg=f"Subject: New Message from :{name}, {email}!\n\n {message}\n Sincerely,{email}")
                return render_template("form-entry.html")
            except Exception as e:
                print("An error occurred while sending email:", e)
                return render_template("index.html")  # Render index.html in case of error
        else:
            return render_template("index.html")



if __name__ == "__main__":
    app.run(debug=True)
