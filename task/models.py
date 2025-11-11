from django.db import models
from users.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=5000, blank=True, null=True)
    is_completed = models.BooleanField(default=False)
    reminder_time = models.DateTimeField()
    email_sent = models.BooleanField(default=False)  # নতুন ফিল্ড
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.full_name} - {self.title} - ({'Done' if self.is_completed else 'pending'})"

    def save(self, *args, **kwargs):
        created = self.pk is None
        super().save(*args, **kwargs)

        if created and self.reminder_time:
            from celery import current_app
            current_app.send_task(
                'task.tasks.send_reminder_email',  
                args=[self.id],
                eta=self.reminder_time
            )
