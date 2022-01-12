from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six


class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (six.text_type(user.pk)+str(timestamp)+six.text_type(user.is_email_verified))


account_activation_token = TokenGenerator()
