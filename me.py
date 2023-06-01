class Who_Am_i:
    me = "I am a django web developer and python enthusiast"
    def __str__(self) -> str:
            return self.me
    
my_identity = Who_Am_i()
print(my_identity)  # Output: "I am a Django web developer and Python enthusiast"
