from django.urls import reverse_lazy

UNFOLD = {
    "SITE_TITLE": "Django Stack Admin",
    "TABS": [
        {
            "models": [
                "authtoken.tokenproxy",
                "token_blacklist.blacklistedtoken",
                "token_blacklist.outstandingtoken",
            ],
            "items": [
                {
                    "title": "Token认证令牌",
                    "link": reverse_lazy("admin:authtoken_tokenproxy_changelist"),
                },
                {
                    "title": "令牌黑名单(JWT)",
                    "link": reverse_lazy("admin:token_blacklist_blacklistedtoken_changelist"),
                },
                {
                    "title": "未处理令牌(JWT)",
                    "link": reverse_lazy("admin:token_blacklist_outstandingtoken_changelist"),
                },
            ],
        },
        {
            "models": ["auth.group", "auth.user"],
            "items": [
                {
                    "title": "用户组",
                    "link": reverse_lazy("admin:auth_group_changelist"),
                },
                {
                    "title": "用户",
                    "link": reverse_lazy("admin:auth_user_changelist"),
                },
            ],
        },
        {
            "models": [
                "django_celery_beat.clockedschedule",
                "django_celery_beat.crontabschedule",
                "django_celery_beat.intervalschedule",
                "django_celery_beat.periodictask",
                "django_celery_beat.solarschedule",
                "django_celery_results.groupresult",
                "django_celery_results.taskresult",
            ],
            "items": [
                {
                    "title": "定时",
                    "link": reverse_lazy("admin:django_celery_beat_clockedschedule_changelist"),
                },
                {
                    "title": "定时任务",
                    "link": reverse_lazy("admin:django_celery_beat_crontabschedule_changelist"),
                },
                {
                    "title": "间隔",
                    "link": reverse_lazy("admin:django_celery_beat_intervalschedule_changelist"),
                },
                {
                    "title": "周期性任务",
                    "link": reverse_lazy("admin:django_celery_beat_periodictask_changelist"),
                },
                {
                    "title": "日程事件",
                    "link": reverse_lazy("admin:django_celery_beat_solarschedule_changelist"),
                },
                {
                    "title": "任务组执行记录",
                    "link": reverse_lazy("admin:django_celery_results_groupresult_changelist"),
                },
                {
                    "title": "任务执行记录",
                    "link": reverse_lazy("admin:django_celery_results_taskresult_changelist"),
                },
            ],
        },
    ],
    "SIDEBAR": {
        "navigation": [
            {
                # "separator": True,
                "title": "系统管理",
                "items": [
                    {
                        "title": "用户管理",
                        "link": reverse_lazy("admin:auth_group_changelist"),
                    },
                    {
                        "title": "定时任务",
                        "link": reverse_lazy("admin:django_celery_beat_clockedschedule_changelist"),
                    },
                    {
                        "title": "审计日志",
                        "link": reverse_lazy("admin:auditlog_logentry_changelist"),
                    },
                    {
                        "title": "令牌管理",
                        "link": reverse_lazy("admin:authtoken_tokenproxy_changelist")
                    },
                ],
            },
        ]
    },
}
