class BaseDemo:
    def login(self):
        raise NotImplementedError("Subclasses must implement this method")
    
class PolymorphismDemo(BaseDemo):
    def login(self):
        return "Login method implemented in PolymorphismDemo"

class AdminLogin(BaseDemo):
    def login(self):
        return "Admin login method implemented in AdminLogin"
    
def perform_login(demo: BaseDemo):
    return demo.login()



perform_login(PolymorphismDemo)
perform_login(AdminLogin)