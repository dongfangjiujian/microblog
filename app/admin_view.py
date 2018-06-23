from flask_admin import Admin, BaseView, expose
from app import admin,db
from flask_login import current_user
from app.models import *
from flask_admin.contrib.sqla import  ModelView
from flask import redirect,url_for


#继承一个BaseView定义一项管理菜单
class Index(BaseView):
    #127.0.0.1:5000/admin/
    def is_accessible(self):
        if  current_user.is_authenticated:
            return True

    @expose('/')
    def index(self):
        user=User.query.filter_by(username=current_user.username).first()
        news=News.query.first()

        print(user.role)
        print(news.subject.id)
        return self.render('admin/index.html',title='index')

    @expose('/test')
    def test(self):
        return 'test'


#添加一个Hello菜单,这个视
# 图可以在外部通过url_for('myview.index')生成url
admin.add_view(Index(name='index'))


class EditView(BaseView):
    def is_accessible(self):
        if  current_user.is_authenticated:
            return True
    @expose('/')
    def edit(self):
        return self.render('admin/index.html',title='edit')

#admin.add_view(EditView(name='edit'))

class UserManage(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

    can_create = False
    column_exclude_list = {
        'password'
    }

admin.add_view(UserManage(User,db.session,name="用户管理"))


class RolesManage(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated



admin.add_view(RolesManage(Role,db.session,name='权限管理'))

class NewsManage(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

    column_exclude_list = {'content'}



admin.add_view(NewsManage(News,db.session,name='新闻管理'))

class NewsCategory(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated


admin.add_view(NewsCategory(News_Category,db.session,name='新闻分类'))

class BackToWeb(BaseView):

    @expose('/')
    def main(self):
        return redirect(url_for('main.index'))

admin.add_view(BackToWeb(name='BackToWebsite'))
