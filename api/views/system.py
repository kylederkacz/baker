from django.http import HttpResponseForbidden, HttpResponseServerError
from django.core.management import get_commands, call_command

from api import JsonResponse


def run_command(request, command):
    commands = get_commands()
    if command not in commands.keys() or commands[command] != 'api':
        return HttpResponseForbidden()
    try:
        output = call_command(command)
    except Exception, e:
        return HttpResponseServerError(e)

    return JsonResponse(output)
