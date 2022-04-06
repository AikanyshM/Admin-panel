from django.db import models

class Block(models.Model):
    cost_per_sq_meter = models.IntegerField()
    block_number = models.CharField(max_length=5)
    entrance_number = models.IntegerField()
    floor_number = models.IntegerField()
    appartment_number_per_floor = models.IntegerField()

    def __str__(self):
        return f'блок {self.block_number}'

class Apartment(models.Model):
    block = models.ForeignKey(Block, on_delete=models.CASCADE)
    owner_name = models.CharField(max_length=50, default='no owner')
    purchase_date = models.DateField()
    owner_birthdate = models.DateField()
    STATUS_CHOICES = (
    ('Buyout', 'Выкуп'),
    ('Incomplete buyout', 'Выкуп не до конца'),
    ('Terminated', 'Расторгнуто'),
    ('Not sold', 'Не продано')
    )
    status = models.CharField(max_length=20, default='Not sold', choices = STATUS_CHOICES)
    room_number = models.IntegerField()
    total_area = models.IntegerField()

    def __str__(self) -> str:
        return self.owner_name