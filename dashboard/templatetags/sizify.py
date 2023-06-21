from django import template

register = template.Library()

def sizify(value):
    """
    Simple kb/mb/gb size snippet for templates:
    
    {{ product.file.size|sizify }}
    """
    byte = 1
    kilobyte = byte*1024
    megabyte = kilobyte*1024
    gigabyte = megabyte*1024
    terabyte = gigabyte*1024

    print(value)

    if value < kilobyte:
        #value = value / kilobyte
        ext = 'Bytes'
    elif value < megabyte:
        value = value / kilobyte
        ext = 'KB'
    elif value < gigabyte:
        value = value / megabyte
        ext = 'MB'
    elif value < terabyte:
        value = value / gigabyte
        ext = 'GB'
    else:
        ext = 'Bytes'

    return '%s %s' % (str(round(value, 1)), ext)

register.filter('sizify', sizify)