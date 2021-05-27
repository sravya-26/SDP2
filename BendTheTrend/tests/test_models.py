from mixer.backend.django import mixer
import pytest

@pytest.mark.django_db
class TestModels:

    def test_name(self):
        Contact = mixer.blend('contacts.Contact',name="sravya")
        assert contact.__str__ == True