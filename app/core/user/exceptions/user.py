from app.core.shared.exceptions import BaseException


class UserAlreadyExistsException(BaseException):
    """Raised when a user with the same username or email already exists"""


class UserNotFoundError(BaseException):
    """Raised when a user is not found"""


class InvalidPasswordError(BaseException):
    """Raised when a user password is invalid"""