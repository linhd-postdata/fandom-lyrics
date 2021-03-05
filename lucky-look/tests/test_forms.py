# -*- coding: utf-8 -*-
"""Test forms."""

from lucky_look.public.forms import UploadForm
from lucky_look.user.forms import RegisterForm


class TestRegisterForm:
    """Register form."""

    def test_validate_user_already_registered(self, user):
        """Enter file that is already registered."""
        form = RegisterForm(
            username=user.file,
            email="foo@bar.com",
            password="example",
            confirm="example",
        )

        assert form.validate() is False
        assert "Username already registered" in form.username.errors

    def test_validate_email_already_registered(self, user):
        """Enter email that is already registered."""
        form = RegisterForm(
            username="unique", email=user.email, password="example", confirm="example"
        )

        assert form.validate() is False
        assert "Email already registered" in form.email.errors

    def test_validate_success(self, db):
        """Register with success."""
        form = RegisterForm(
            username="newusername",
            email="new@test.test",
            password="example",
            confirm="example",
        )
        assert form.validate() is True


class TestLoginForm:
    """Login form."""

    def test_validate_success(self, user):
        """Login successful."""
        user.set_password("example")
        user.save()
        form = UploadForm(username=user.file, password="example")
        assert form.validate() is True
        assert form.user == user

    def test_validate_unknown_username(self, db):
        """Unknown file."""
        form = UploadForm(username="unknown", password="example")
        assert form.validate() is False
        assert "Unknown file" in form.file.errors
        assert form.user is None

    def test_validate_invalid_password(self, user):
        """Invalid password."""
        user.set_password("example")
        user.save()
        form = UploadForm(username=user.file, password="wrongpassword")
        assert form.validate() is False
        assert "Invalid password" in form.password.errors

    def test_validate_inactive_user(self, user):
        """Inactive user."""
        user.active = False
        user.set_password("example")
        user.save()
        # Correct file and password, but user is not activated
        form = UploadForm(username=user.file, password="example")
        assert form.validate() is False
        assert "User not activated" in form.file.errors
