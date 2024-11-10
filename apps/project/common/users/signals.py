from datetime import date

def passport_directory_path(instance, filename):
    """
    This function is used to generate a file path for an avatar image when a user is saved. 
    The path includes the current year, month, and day, as well as the full name of the user and the original filename of the image.
    """
    return f"passport_images/{instance.id} - {instance.get_full_name()}/{date.today().year}-{date.today().month}-{date.today().day}/{filename}"

def firm_directory_path(instance, filename):
    """
    This function is used to generate a file path for an avatar image when a user is saved. 
    The path includes the current year, month, and day, as well as the full name of the user and the original filename of the image.
    """
    return f"firm_images/{instance.id} - {instance.get_full_name()}/{date.today().year}-{date.today().month}-{date.today().day}/{filename}"