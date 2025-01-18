def count_email_domains(emails, urls):
    # Initialize the result dictionary with URLs as keys and 0 as the default value
    result = {}
    for url in urls:
        result[url] = 0
    
    # Check if the email domain matches any domain from the URLs
    for url in urls:
        if url.startswith('www.'):
            # Remove 'www.' and store the domain
            domain = url[4:]
        for email in emails:
            # Extract the domain from the email
            email_domain = email.split('@')[-1]
            if email_domain == domain:
                result[url] += 1
    return result


# Example Input
emails = ['foo@a.com', 'bar@a.com', 'baz@b.com', 'qux@d.com']
urls = ['www.a.com', 'www.b.com', 'www.c.com']

# Call the function and print the result
output = count_email_domains(emails, urls)
print(output)
