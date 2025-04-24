class Password_manager() :
    def __init__(self):
        self.old_passwords = []
    def get_password(self) :
        return self.old_passwords[-1] if self.old_passwords else None
    def set_password(self, attempt) :
        if attempt not in self.old_passwords :
            self.old_passwords.append(attempt)
    def is_correct (self, string) :
        return string == self.get_password()

def main():
    pm = Password_manager()
    pass1 = input('enter pass1')
    pass2 = input('enter pass2')
    pm.set_password(pass1)
    pm.set_password(pass2)
    print(pm.get_password())
    print(pm.is_correct("pw1"))
if __name__ == "__main__":
    main()
    

