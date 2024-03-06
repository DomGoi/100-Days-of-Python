from instagram import InstaFollower

mail="marc.montana9502@gmail.com"
password="malpyMalpymalpyMontana"
site_name="doggomon"

insta=InstaFollower(mail,password)

insta.perform_login()

insta.find_followers(site_name)
