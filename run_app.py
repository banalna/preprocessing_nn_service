# -*- coding: utf-8 -*-

from app.factory import create_app

app = create_app()

# @_app.shell_context_processor
# def make_shell_context():
#     return  {'db': db, 'User': User, 'Post': Post, 'Message': Message,
#     'Notification': Notification, 'Task': Task, 'Room':Room}


if __name__=='__main__':
    app.run(debug=True)
    #app.run(host='0.0.0.0', ports=8080)

