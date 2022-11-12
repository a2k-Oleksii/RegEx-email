import re


def check_email_address(text):
    pattern = r"^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+"
    if re.match(pattern, text):
        return True
    return False


def parcer_email_addresses(text):
    if check_email_address(text):
        emails = re.findall(r"\w+[-]?\w+|\w+", text)
        return emails
    return None


if __name__ == "__main__":
    text = open("emails.txt", "r")
    for line in text:
        email = parcer_email_addresses(line)
        if email:
            for number in range(len(email)):
                if number == 0:
                    print("User -", email[number], end=", ")
                else:
                    print("Domain level", number, "-", email[number], end=", ")
            print()
    text.close()
