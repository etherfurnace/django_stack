from datetime import datetime, timedelta

from django.core.management import call_command

from celery import shared_task


@shared_task
def clear_audit_logs():
    """
    定期清理AuditLog
    :return:
    """
    date_to_delete = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d")
    call_command("auditlogflush", "-b", date_to_delete, "-y")
