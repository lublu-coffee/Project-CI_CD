from users import get_users


class TestUsers:
    def test_quantity_user(self):
        users = get_users()
        assert len(users) == 5

    def test_name_user(self):
        users = get_users()
        names = [user[1] for user in users]
        assert "Тами" in names

    def test_ids(self):
        users = get_users()
        ids = [user[0] for user in users]
        assert ids == list(range(1, 6))
