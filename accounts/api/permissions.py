from rest_framework import permissions


class BlacklistPermission(permissions.BasePermission):
    """
    Global permission check for blacklisted IPs.
    """
    def has_permission(self, request, view):
        ip_addr = request.META['REMOTE_ADDR']
        blacklisted = Blacklist.objects.filter(ip_addr=ip_addr).exists() # true / false
        return not blacklisted

    
class AnonPermissionOnly(permissions.BasePermission):
    # message - optional. If not included, will display default
    message = "You are already authenticated. Please log out and try again"
    """
    Non-authenticated User only."
    """

    def has_permission(self, request, view):
        return not request.user.is_authenticated()