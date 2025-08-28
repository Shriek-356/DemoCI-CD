import unittest
from MuonTraSach import dao


class TestLogin(unittest.TestCase):
    #Test login
    def test_login_success(self):
        """Đăng nhập đúng username/password"""
        user = dao.auth_user("admin", "1")
        self.assertIsNotNone(user)
        self.assertEqual(user["username"], "admin")

    def test_login_wrong_password(self):
        """Sai mật khẩu"""
        user = dao.auth_user("admin", "sai")
        self.assertIsNone(user)

    def test_login_nonexistent_user(self):
        """User không tồn tại"""
        user = dao.auth_user("abc", "123")
        self.assertIsNone(user)
    # Test with role
    def test_login_admin_success(self):
        """Đăng nhập đúng admin"""
        user = dao.auth_user("admin", "1")
        self.assertIsNotNone(user)
        self.assertEqual(user["username"], "admin")
        self.assertEqual(user["role"], "admin")

    def test_login_user_success(self):
        """Đăng nhập đúng user"""
        user = dao.auth_user("khang", "1")
        self.assertIsNotNone(user)
        self.assertEqual(user["username"], "khang")
        self.assertEqual(user["role"], "user")

    def test_login_wrong_password(self):
        """Sai mật khẩu"""
        user = dao.auth_user("admin", "sai")
        self.assertIsNone(user)

    def test_login_nonexistent_user(self):
        """User không tồn tại"""
        user = dao.auth_user("abc", "123")
        self.assertIsNone(user)

    def test_login_empty_username(self):
        """Username rỗng"""
        user = dao.auth_user("", "123")
        self.assertIsNone(user)

    def test_login_empty_password(self):
        """Password rỗng"""
        user = dao.auth_user("admin", "")
        self.assertIsNone(user)

if __name__ == '__main__':
    unittest.main()