# -*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.views.decorators.cache import never_cache

class AdminSite(admin.AdminSite):
    @never_cache
    def login(self, request, extra_context=None):
    """
    Displays the login form for the given HttpRequest.
    """
    context = {
            REDIRECT_FIELD_NAME: request.REQUEST.get(
                REDIRECT_FIELD_NAME,
                request.get_full_path()
                )
            }
    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
        return super(AdminSite, self).login(
                request,
                extra_context=context
                )

custom_admin = AdminSite()
