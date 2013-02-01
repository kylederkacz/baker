import os

from django.http import HttpResponse

# Create your views here.


def file_tree(request):
    print request.POST
    ROOT = '/'
    request_dir = request.POST.get('dir', '')
    hide_dot_files = request.POST.get('hideDotFiles', "true")
    show_files = request.POST.get('showFiles', "true")
    abs_dir = os.path.join(ROOT, request_dir)

    try:
        r = ['<ul class="jqueryFileTree" style="display: none;">']
        for f in os.listdir(abs_dir):
            ff = os.path.join(abs_dir, f)
            if hide_dot_files == "true" and f[0] == '.':
                continue
            if os.path.isdir(ff):
                r.append('<li class="directory collapsed"><a href="#" rel="%s/">%s</a></li>' % (ff, f))
            else:
                if show_files != "true":
                    continue
                e = os.path.splitext(f)[1][1:]  # get .ext and remove dot
                r.append('<li class="file ext_%s"><a href="#" rel="%s">%s</a></li>' % (e, ff, f))
        r.append('</ul>')
    except Exception, e:
        r.append('Could not load directory: %s' % str(e))
    return HttpResponse(''.join(r))
