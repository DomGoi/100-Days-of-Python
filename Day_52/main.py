from instagram import InstaFollower

mail=os.environ("MAIL")
password=os.environ("PASSWORD")
site_name="doggomon"

insta=InstaFollower(mail,password)

insta.perform_login()

insta.find_followers(site_name)
