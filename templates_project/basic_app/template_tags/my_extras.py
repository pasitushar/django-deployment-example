from django import template

# custom template filters
register = template.Library()

# @register.filter(name='cut')
def cutter(value,arg):
    """
    This cuts out all the values of "arg" from the string
    """
    return value.replace(arg,'')
register.filter('cut',cutter)
