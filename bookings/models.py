from django.contrib.auth.models import User
from django.db import models


class Schedule(models.Model):
    soundman = models.ForeignKey(User, related_name='schedules')
    start_of_the_day = models.TimeField()
    end_of_the_day = models.TimeField()
    DAY_OF_WEEK = (
        (1, "Понедельник"),
        (2, "Вторник"),
        (3, "Среда"),
        (4, "Четверг"),
        (5, "Пятница"),
        (6, "Суббота"),
        (7, "Воскресенье")

    )
    working_day = models.IntegerField(choices=DAY_OF_WEEK)

    def __str__(self):
        return '%s (%s)' % (self.soundman.username, self.get_working_day_display())


class Booking(models.Model):
    user = models.ForeignKey(User, related_name='bookings')
    STATUS = (
        (1, 'Активна'),
        (2, 'В процессе'),
        (3, 'Неактивна'),
        (4, 'Отменена'),
        (5, 'Завершена'),
    )
    is_active = models.IntegerField(choices=STATUS)
    date = models.DateField()
    start = models.TimeField()
    end = models.TimeField()
    schedule = models.ForeignKey(Schedule, related_name='sch_bookings')

    def __str__(self):
        return 'User: %s | Soundman: %s' % (self.user.username, self.schedule.soundman.username)


class Record(models.Model):
    reservation = models.OneToOneField(Booking, primary_key=True, related_name='reservations')
    start_record = models.DateTimeField(null=True)
    stop_record = models.DateTimeField(null=True)
    money_back = models.IntegerField(null=True)

    def __str__(self):
        return 'Record of user "%s"   | Soundman: "%s   | Date: %s"' % \
               (self.reservation.user.username, self.reservation.schedule.soundman.username, self.reservation.date)
