import re

def count_valid_emails(emails):
    if not emails:
        return 0
    
    count = 0
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    for email in emails:
        if isinstance(email, str) and re.match(email_pattern, email.strip()):
            count += 1
    
    return count