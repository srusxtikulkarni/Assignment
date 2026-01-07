def check_attendance(login_time):
  if login_time< 9.30:
    print("Present")
  elif login_time <10.0 and login_time >= 9.30:
    print("Late")
  if login_time>=10.0:
    print("Absent")
login_time=float(input("Enter time"))
check_attendance(login_time)
