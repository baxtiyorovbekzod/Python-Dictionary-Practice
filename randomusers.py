from dataset import randomuser_data


def get_full_names(data: dict) -> list[str]:
    """
    Returns a list of users' full names in 'First Last' format.

    Args:
        data (dict): JSON data containing user records.

    Returns:
        list[str]: List of full names.
    """
    names=[]
    for user in data['results']:

        name=user['name']
        fullname=f"{name['first']} {name['last']}"
        names.append(fullname)

    return names    
    


def get_users_by_country(data: dict, country: str) -> list[dict]:
    """
    Filters and returns users who live in a specific country.

    Args:
        data (dict): JSON data containing user records.
        country (str): Country name to filter by.

    Returns:
        list[dict]: List of dictionaries containing full name and email of matching users.
    """
    countryes=[]
    for user in data['results']:
        if  user['location']['country']==country:
            countryes.append({
                "name":f"{user['name']['first']} {user['name']['last']}",
                "email":user["email"],
                "country":user["location"]["country"]
            })

    return countryes

x=get_users_by_country(randomuser_data, "Netherlands")


       

def  count_users_by_gender(data: dict) -> dict:
    """
    Counts the number of users by gender.

    Args:
        data (dict): JSON data containing user records.

    Returns:
        dict: Dictionary with gender as keys and count as values.
    """
    result = {'male': 0, 'female': 0}
    
    for user in data['results']:
        if user['gender'] == "male":
            result ['male'] += 1
        elif user['gender'] == 'female':
            result['female'] += 1
    
    return result



def get_emails_of_older_than(data: dict, age: int) -> list[str]:
    """
    Returns a list of emails of users older than the given age.

    Args:
        data (dict): JSON data containing user records.
        age (int): Age threshold.

    Returns:
        list[str]: List of email addresses.
    """
    emails = []
    for user in data['results']:
        if user['dob']['age'] > age:   
            emails.append(user['email'])
    
    return emails

q=get_emails_of_older_than(randomuser_data , 60)


def sort_users_by_age(data: dict, descending: bool = False) -> list[dict]:
    """
    Sorts users by age in ascending or descending order.

    Args:
        data (dict): JSON data containing user records.
        descending (bool, optional): Whether to sort in descending order. Defaults to False.

    Returns:
        list[dict]: List of users with name and age sorted accordingly.
    """
    pass


def get_usernames_starting_with(data: dict, letter: str) -> list[str]:
    """
    Returns a list of usernames starting with a given letter.

    Args:
        data (dict): JSON data containing user records.
        letter (str): The starting letter to filter usernames.

    Returns:
        list[str]: List of matching usernames.
    """
    usernames = []
    for user in data['results']:
        if user['login']['username'].startswith(letter):
            usernames.append({
            'username': user['login']['username']
        })

    return usernames

r=get_usernames_starting_with(randomuser_data, "g")  
 


def get_average_age(data: dict) -> float:
    """
    Calculates and returns the average age of users.

    Args:
        data (dict): JSON data containing user records.

    Returns:
        float: Average age.
    """
    averages=[]
    for user in data['results']:
        if 'dob' in user and 'age' in user['dob']:
            averages.append(user['dob']['age'])

    if len(averages) == 0:
        return 0.0  
    
    return sum(averages) / len(averages)
g=get_average_age(randomuser_data) 
  


def group_users_by_nationality(data: dict) -> dict:
    """
    Groups and counts users by their nationality.

    Args:
        data (dict): JSON data containing user records.

    Returns:
        dict: Dictionary with nationality as keys and count as values.
    """
    results={}
    for user in data['results']:
        nat=user['nat']
        if nat in results:
            results[nat] += 1
        else:
            results[nat] = 1 

    return results

result8=group_users_by_nationality(randomuser_data)             

            
def get_all_coordinates(data: dict) -> list[tuple[str, str]]:
    """
    Extracts all users' coordinates as tuples of (latitude, longitude).

    Args:
        data (dict): JSON data containing user records.

    Returns:
        list[tuple[str, str]]: List of coordinate tuples.
    """
    coordinates=[]
    for user in data['results']:
        car=user['location']['coordinates']
        lat = car['latitude']
        lon = car['longitude']
        coordinates.append((lat, lon))
        

    return coordinates

result9=get_all_coordinates(randomuser_data)
      


def get_oldest_user(data: dict) -> dict:
    """
    Finds and returns the oldest user's name, age, and email.

    Args:
        data (dict): JSON data containing user records.

    Returns:
        dict: Dictionary containing 'name', 'age', and 'email' of the oldest user.
    """
    oldest_user = None
    mx = 0
    for user in data['results']:
        age = user['dob']['age']
        if age > mx:
            mx = age
            oldest_user = {
                "name": f"{user['name']['first']} {user['name']['last']}",
                "age": age,
                "email": user['email']
            }
    return oldest_user



result10=get_oldest_user(randomuser_data) 
  


def find_users_in_timezone(data: dict, offset: str) -> list[dict]:
    """
    Returns users whose timezone offset matches the given value.

    Args:
        data (dict): JSON data containing user records.
        offset (str): Timezone offset (e.g. '+5:30').

    Returns:
        list[dict]: List of users with full name and city.
    """
    timezone=[]
    for user in data['results']:
        time = user['location']['timezone']['offset']
        if time == offset:
            timezone.append({
                "name": f"{user['name']['first']} {user['name']['last']}",
                "city": user['location']['city']
            })

    return timezone

result11=find_users_in_timezone(randomuser_data, '+5:30')
print(result11)        
    


def get_registered_before_year(data: dict, year: int) -> list[dict]:
    """
    Returns users who registered before a given year.

    Args:
        data (dict): JSON data containing user records.
        year (int): Year threshold.

    Returns:
        list[dict]: List of users with full name and registration date.
    """
    pass



