import re

prog = re.compile(r'^[-_a-z0-9]+@[a-z0-9]+\..{1,3}$', re.I)

def fun(email):
    return prog.match(email) is not None

def filter_mail(emails):
    return filter(fun, emails)

if __name__ == '__main__':
    n = int(raw_input())
    emails = []
    for _ in range(n):
        emails.append(raw_input())

    filtered_emails = filter_mail(emails)
    filtered_emails.sort()
    print filtered_emails
