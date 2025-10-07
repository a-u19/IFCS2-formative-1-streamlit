from classes import *

new_employee_1 = Employee(1, "test1", "test2")
new_call_2 = Call(2, "Pending")
new_manager_3 = Manager(3, "test_manager_1", "test_manager_1_last_name", [])
new_staff_4 = Staff(4, "test_staff", "test_staff_last_name", 3)
new_manager_5 = Manager(5, "test_manager_2", "test_manager_2_last_name", [])
new_manager_7 = Manager(7, "test_manager_3", "test_manager_3_last_name", [4, 5, 6])

def test_smoke_test():
    assert 1 == 1

def test_employee_creation():
    assert isinstance(new_employee_1, Employee)
    assert new_employee_1.first_name == "test1"
    assert new_employee_1.last_name == "test2"

def test_call_creation():
    assert isinstance(new_call_2, Call)

def test_manager_creation():
    assert isinstance(new_manager_3, Manager)

def test_staff_creation():
    assert isinstance(new_staff_4, Staff)

def test_add_staff_manager():
    new_manager_5.add_staff(6, "new_staff_1", "new_staff_1_last_name", 5)
    assert 6 in new_manager_5.staff_list

def test_remove_staff_manager():
    new_manager_7.remove_staff(6)
    assert 6 not in new_manager_7.staff_list

def test_accept_call():
    new_staff_4.accept_call(new_call_2)
    assert new_call_2.status == "In Progress" and new_staff_4.status == "On Call"

def test_end_call():
    new_staff_4.end_call(new_call_2,0.9)
    assert new_call_2.status == "Successful" and new_staff_4.status == "Free"

def test_start_workday():
    new_staff_4.start_workday()
    assert new_staff_4.working_time_elapsed > 0 and new_staff_4.status == "Free"

def test_end_workday():
    new_staff_4.end_workday()
    assert new_staff_4.status == "Out of Office"