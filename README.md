# Cornershop Backend Test

### Assumptions

* Nora is the only user that needs to be authenticated to the system.
* Nora con create as many menu options as she wants per Menu, as well as edit and delete them if necessary.
* Nora can send the slack message with today's menus as many times as she wants to the employees slack channel.
* Employees are not required to have an account in order to select a menu option.
* Employees can't order if it's past 11 AM CL time nor if Nora hasn't created today's menu.

### Follow these steps for set-up
* Clone the repository
* cd cornershop-backend-test
* `make up`
* `dev up`
##### Rebuilding the base Docker image
* `make rebuild`
##### Resetting the local database
* `make reset`
### Hostnames for accessing the service directly
* Local: http://127.0.0.1:8000
## To run tests:

* `pytest`

## Login for Nora

http://0.0.0.0:8000/login

* username: nora
* password: cornershop

### Considerations
* For formatting purposes, I used `Black`
* For sorting imports, I used `isort`
* The timezone used is `TIME_ZONE = America/Santiago`


# Extra
### Decisions
* The home view is located in the menus app for simplicity. Another option for a more scalable system could have been to create an app only for the Meal Management System, that would contain the views and urls related to the system.

### Modelling the Backend
```
class Menu(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    menu_date = models.DateTimeField(null=True, default=datetime.datetime.now(tzlocal())) 

class MenuOption(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
    menu = models.ForeignKey(
        'Menu',
        on_delete=models.CASCADE,
    )
    description = models.CharField(max_length=128)

class MenuSelection(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	employee_firstname = models.CharField(max_length=128)
    employee_lastname = models.CharField(max_length=128)
	employee_id = models.IntegerField()
    selection =  models.ForeignKey(MenuOption, on_delete=models.CASCADE)
    extra_large = models.BooleanField(default=False) 
    specification = models.CharField(max_length=128)
```
