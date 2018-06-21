from flask_admin import Admin, BaseView, expose
from app import admin,db
from flask_login import current_user
from app.models import User
from flask_admin.contrib.sqla import  ModelView


#继承一个BaseView定义一项管理菜单
class IndexView(BaseView):
    #127.0.0.1:5000/admin/
    def is_accessible(self):
        if  current_user.is_authenticated:
            return True

    @expose('/')
    def index(self):
        return self.render('admin/index.html',title='index')

    @expose('/test')
    def test(self):
        return 'test'


#添加一个Hello菜单,这个视
# 图可以在外部通过url_for('myview.index')生成url
admin.add_view(IndexView(name='index'))


class EditView(BaseView):
    def is_accessible(self):
        if  current_user.is_authenticated:
            return True
    @expose('/')
    def edit(self):
        return self.render('admin/index.html',title='edit')

admin.add_view(EditView(name='edit'))

class UserManage(ModelView):
    def is_accessible(self):
        if  current_user.is_authenticated:
            user = User.query.filter_by(username = current_user.username).first()
            if user.admin==True:
                return True
admin.add_view(UserManage(User,db.session,name="用户管理"))
