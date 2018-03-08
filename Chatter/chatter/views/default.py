from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from pyramid.httpexceptions import HTTPFound

import transaction
 
from ..models import Message
    
 
@view_config(route_name='home', renderer='../templates/messages.jinja2')
def index(request):
    messages = request.dbsession.query(Message).order_by(Message.created)[-10:]
    return {'messages': messages}
 
@view_config(route_name='send')
def send(request):
    text = request.params.get('message')
    print text
    with transaction.manager:
        message = Message(text)
        request.dbsession.add(message)
    return HTTPFound(location=request.route_url('home'))

# @view_config(route_name='home', renderer='../templates/mytemplate.jinja2')
# def my_view(request):
#     try:
#         query = request.dbsession.query(Message)
#         one = query.filter(Message.name == 'one').first()
#     except DBAPIError:
#         return Response(db_err_msg, content_type='text/plain', status=500)
#     return {'one': one, 'project': 'Chatter'}


db_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to run the "initialize_Chatter_db" script
    to initialize your database tables.  Check your virtual
    environment's "bin" directory for this script and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""
