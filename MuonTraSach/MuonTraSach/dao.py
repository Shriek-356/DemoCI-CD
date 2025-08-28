import json, os

#
# Không Phân quyền (Lấy file k có role)
#

# def auth_user(username, password):
#     base_dir = os.path.dirname(__file__)
#     file_path = os.path.join(base_dir, "data", "user.json")
#     with open(file_path, encoding="utf8") as f:
#         users = json.load(f)
#         for u in users:
#             if u["username"] == username and u["password"] == password:
#                 return u
#     return None




#
# Phân quyền (Lấy file có role)
#

def auth_user(username, password):
    base_dir = os.path.dirname(__file__)
    file_path = os.path.join(base_dir, "data", "user_role.json")
    with open(file_path, encoding="utf8") as f:
        users = json.load(f)
        for u in users:
            if u["username"] == username and u["password"] == password:
                return u
    return None



if __name__ == '__main__':
    print(auth_user("admin", "1"))