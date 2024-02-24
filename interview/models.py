# interview/models.py
from django.db import models

class InterviewQuestion(models.Model):
    ROLE_CHOICES = [
        ('sde', 'Software Development Engineer'),
        ('qa', 'Quality Assurance Engineer'),
        ('pm', 'Product Manager'),
        ('dba', 'Database Administrator'),
        ('se', 'Systems Engineer'),
        ('ee', 'Electrical Engineer'),  # Adding Electrical Engineer role
        ('ece', 'Electronics Engineer'),  # Adding Electronics Engineer role
        # Add more roles as needed
    ]

    TOPIC_CHOICES = [
        ('ds', 'Data Structures'),
        ('algo', 'Algorithms'),
        ('oop', 'Object-Oriented Programming'),
        ('db', 'Databases'),
        ('web', 'Web Development'),
        ('os', 'Operating Systems'),
        ('network', 'Computer Networks'),
        ('electronics', 'Electronics'),
        ('electrical', 'Electrical Engineering'),
        ('circuits', 'Circuits'),
        ('signals', 'Signals and Systems'),
        ('analog', 'Analog Electronics'),
        ('digital', 'Digital Electronics'),
        # Add more topics as needed
    ]

    DIFFICULTY_CHOICES = [
        ('easy', 'Easy'),
        ('moderate', 'Moderate'),
        ('hard', 'Hard'),
    ]

    role = models.CharField(max_length=255)  # Allowing users to define their own role
    topic = models.CharField(max_length=255, choices=TOPIC_CHOICES)
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES)
    question = models.TextField()

    def __str__(self):
        return f"{self.role} - {self.topic} - {self.difficulty}"
