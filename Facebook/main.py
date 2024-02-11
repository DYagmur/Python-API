from user import User
from post import Post

#creating object from a class 
app_user_one = User("nn@nn.com", "Nana janashia", "pwd1", "devops engineer")
app_user_one.get_user_info()


app_user_one.change_job_title("Devops trainer")
app_user_one.get_user_info()

app_user_two = User("aa@aa.com", "james bond",  "007", "chief security officer")
app_user_two.get_user_info()

new_post = Post("on a secret mission today", app_user_two.name)
new_post.get_post_info()