from flask_admin import Admin, BaseView, expose
from app import admin
from flask import redirect,url_for

#继承一个BaseView定义一项管理菜单
class IndexView(BaseView):
    #127.0.0.1:5000/admin/
    @expose('/')
    def index(self):
        return self.render('admin/index.html',title='index')



#添加一个Hello菜单,这个视
# 图可以在外部通过url_for('myview.index')生成url
admin.add_view(IndexView(name='index'))


class EditView(BaseView):
    @expose('/')
    def edit(self):
        return self.render('admin/index.html',title='edit')

admin.add_view(EditView(name='edit'))
