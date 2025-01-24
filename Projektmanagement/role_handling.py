E_Employee = 1
E_Project_Manager = 2
E_Admin = 4
roles = [E_Employee, E_Project_Manager, E_Admin]
roles.sort(reverse=True)

def is_authorized(neededPermission: int, userPermission: int) ->bool:
    """
    This function checks if a given user permission is valid for a needed permission.
    For example would a needed permission of E_Project_Manager + E_Admin and a user permission
    of E_Employee not work. Otherwise E_Project_Manager + E_Admin and E_Project_Manager works.
    
    param neededPermission: The needed permission the user has to have. Can be a combination
    of needed permission (6 for example) or a single one (4)
    param userPermission: The user permission. Should be a declared number form the top of the file (1, 2, 4)

    return: True if the user is permitted for the given needed permission, otherwise False
    """
    neededPermission_copy = neededPermission

    for role in roles:
        # if the current permission is the user permission (4 = 4 for example) or 
        # the current permission is divisable only once by the user permission (eg 7 // 4 = 1 but 3 // 4 != 1)
        if (neededPermission_copy == userPermission or neededPermission_copy // userPermission == 1):
            return True
        # if the needed permission goes below 1, break out and return false
        elif (neededPermission_copy < 1):
            break
        # if the current role is not the user permission (eg 4 != 2) and the current role is smaller than the
        # current needed permission (4 < 6) 
        # NOTE role describes the current permisison in the array and not the user permission
        elif (role != userPermission and role < neededPermission_copy):
            neededPermission_copy -= role
    if (neededPermission_copy == userPermission):
            return True
    return False

"""import random
testNeededPermission = [1, 2, 3, 4, 6, 7]
testUserPermission = [1, 2, 4]
 
for x in range (20):
    neededPermission = random.randint(1, 7)
    userPermission = random.randint(1, 3)
    if userPermission == 3:
        userPermission = 4
    yes = is_authorized(neededPermission, userPermission)
    print("Role needed: " + str(neededPermission))
    print("Has role: " + str(userPermission))
    print("Is authorized = " + str(yes))
    print("-----------------------------------")"""