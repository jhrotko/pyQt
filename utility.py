
def is_number(text):
    try:
        float(text)
        return True
    except ValueError:
        return False