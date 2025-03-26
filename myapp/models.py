from django.db import models

class user_entry_details(models.Model):
    name=models.CharField(max_length=200)
    department=models.CharField(max_length=300)
    college_name=models.CharField(max_length=300)
    year=models.CharField(max_length=30)
    team_name=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class problem_selection(models.Model):
    team_name=models.CharField(max_length=100)
    problem_domain=models.CharField(max_length=200)
    problem_statement_number=models.CharField(max_length=20)
    
    def __str__(self):
        return f"{self.team_name} - {self.problem_domain} - {self.problem_statement_number}"