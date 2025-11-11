from celery import shared_task
from django.core.mail import send_mail
from .models import Task

@shared_task(bind=True, max_retries=3)
def send_reminder_email(self, task_id):
    try:
        task = Task.objects.get(id=task_id)
        subject = f"Reminder: {task.title}"
        message = f"Hello {task.user.full_name},\n\nThis is your reminder for: {task.title}\n\nDetails: {task.description}"
        recipient = [task.user.email]

        send_mail(
            subject=subject,
            message=message,
            from_email=None,  # Uses DEFAULT_FROM_EMAIL
            recipient_list=recipient,
            fail_silently=False,
        )

        task.email_sent = True
        task.save()
        print(f"Email sent successfully for task {task.id}")

    except Task.DoesNotExist:
        print(f"Task {task_id} does not exist.")
    except Exception as e:
        print(f"Failed to send email for task {task_id}: {e}")
        raise self.retry(exc=e, countdown=60)
