class UserInfo:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def print_info(self):
        print("--------------------")
        print("Name:" + self.name)
        print("Phone:" + self.phone)
        print("--------------------")

    def __del__(self):
        print("delete!")

user1 = UserInfo("kim","010-0000-0000")
user2 = UserInfo("lim","010-1000-1000")

#print(id(user1))
#print(id(user2))

#user1.set_info("kim","010-0000-0000")
#user2.set_info("lim","010-1000-1000")

print(user1.__dict__)
print(user2.__dict__)

print(user1.phone, user1.name)
print(user2.phone, user2.name)
