def validateEmail(email):
    """validate emails.
    Could have used email_validator library or regex, but decided to do it this way 
    to show some code, string and list handling

    Args:
        email (_type_): str

    Returns:
        _type_: [str]
    """
    
    errors = []
    if not '@' in email:
        errors.append('The email must contain "@"!')
    else:
        [user, domain] = email.split('@')
        if len(user) < 3 or len(domain.split('.')) < 2:
            errors.append('The email has no valid format!')
    return errors
