employee_id_valid = input("Is Employee ID valid? (yes/no): ")
wifi_connected = input("Is connected to office Wi-Fi? (yes/no): ")

if employee_id_valid == "yes":
    if wifi_connected == "yes":
        print("Access Granted")
    else:
        print("Connect to Office Wi-Fi")
else:
    print("Access Denied")