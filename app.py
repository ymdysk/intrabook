#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime

import bottle
bottle.debug(True)
from bottle import get, post, run
from bottle import request, template, redirect
from bottle import HTTPError
from sqlalchemy import create_engine, Column, Integer, Unicode, DateTime, UnicodeText
from sqlalchemy.ext.declarative import declarative_base

from bottle.ext import sqlalchemy

from wtforms.form import Form
from wtforms import validators
from wtforms import StringField, IntegerField, TextAreaField

Base = declarative_base()
engine = create_engine('sqlite:///:memory:', echo=True)

# bottle-sqlalchemyの設定
plugin = sqlalchemy.Plugin(
    engine,
    Base.metadata,
    keyword='db',  # 関数内で挿入される場合の変数名
    create=True,  # テーブルを作成するか
    commit=True,  # 関数終了時にコミットするか
    use_kwargs=False
)

# プラグインのインストール
bottle.install(plugin)


class Book(Base):
    # booksテーブル
    __tablename__ = 'books'

    # カラムの定義
    id = Column(Integer, primary_key=True)
    url = Column(Unicode(100), nullable=False)
    pf = Column(UnicodeText)
    rate = Column(UnicodeText)
    memo = Column(UnicodeText)
    created_at = Column(DateTime, default=datetime.now)

    def __repr__(self):
        return "<Book('%s','%s','%s','%s','%s')>" % (self.url, self.pf, self.rate, self.memo, self.created_at)

class Project(Base):
    # projectsテーブル
    __tablename__ = 'projects'

    # カラムの定義
    id = Column(Integer, primary_key=True)
    title = Column(Unicode(100), nullable=False)
    url = Column(UnicodeText)
    pf = Column(UnicodeText)
    rate = Column(UnicodeText)
    memo = Column(UnicodeText)
    created_at = Column(DateTime, default=datetime.now)

    def __repr__(self):
        return "<Project('%s','%s','%s','%s','%s','%s')>" % (self.title, self.url, self.pf, self.rate, self.memo, self.created_at)

class Rel(Base):
    # Relテーブル
    __tablename__ = 'rels'

    # カラムの定義
    id = Column(Integer, primary_key=True)
    bid = Column(Integer, nullable=False)
    pid = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.now)

    def __repr__(self):
        return "<Rel('%s','%s','%s')>" % (self.bid, self.pid, self.created_at)



class BookForm(Form):
    url = StringField(u'URL', [
        validators.required(message=u"入力してください"),
        validators.length(min=1, max=100, message=u"100文字以下で入力してください")
    ])
    pf = TextAreaField(u'プラットフォーム', [
        validators.required(message=u"入力してください")
    ])
    rate = TextAreaField(u'レート', [
        validators.required(message=u"入力してください")
    ])
    memo = TextAreaField(u'コメント', [
        validators.required(message=u"入力してください")
    ])

class ProjectForm(Form):
    title = TextAreaField(u'タイトル', [
        validators.required(message=u"入力してください"),
        validators.length(min=1, max=100, message=u"100文字以下で入力してください")
    ])
    url = TextAreaField(u'URL', [
        validators.required(message=u"入力してください"),
    ])
    pf = TextAreaField(u'プラットフォーム', [
        validators.required(message=u"入力してください")
    ])
    rate = TextAreaField(u'レート', [
        validators.required(message=u"入力してください")
    ])
    memo = TextAreaField(u'コメント', [
        validators.required(message=u"入力してください")
    ])

class RelForm(Form):
    bid = TextAreaField(u'bid', [
        validators.required(message=u"入力してください"),
    ])
    pid = TextAreaField(u'pid', [
        validators.required(message=u"入力してください")
    ])

@get('/books')
def index(db):
    # booksテーブルから全件取得
    books = db.query(Book).all()
    # index.tplの描画
    return template('index', books=books, request=request)

@get('/projects')
def pindex(db):
    # projectsテーブルから全件取得
    projects = db.query(Project).all()
    # index.tplの描画
    return template('project', projects=projects, request=request)

@get('/rels')
def rindex(db):
    # relsテーブルから全件取得
    rels = db.query(Rel).all()
    # index.tplの描画
    return template('rel', rels=rels, request=request)


@get('/books/add')
def new(db):
    form = BookForm()
    # add.tplの描画
    return template('edit', form=form, request=request)

@get('/projects/add')
def pnew(db):
    form = ProjectForm()
    # padd.tplの描画
    return template('pedit', form=form, request=request)

@get('/rels/add')
def rnew(db):
    form = RelForm()
    # padd.tplの描画
    return template('redit', form=form, request=request)


@post('/books/add')
def create(db):
    form = BookForm(request.forms.decode())
    # フォームのバリデーション
    if form.validate():
        # Bookインスタンスの作成
        book = Book(
            url=form.url.data,
            pf=form.pf.data,
            rate=form.rate.data,
            memo=form.memo.data
        )
        # bookを保存
        db.add(book)
        # 一覧画面へリダイレクト
        redirect("/books")
    else:
        return template('edit', form=form, request=request)

@post('/projects/add')
def pcreate(db):
    form = ProjectForm(request.forms.decode())
    # フォームのバリデーション
    if form.validate():
        # Projectインスタンスの作成
        project = Project(
            title=form.title.data,
            url=form.url.data,
            pf=form.pf.data,
            rate=form.rate.data,
            memo=form.memo.data
        )
        # projectを保存
        db.add(project)
        # 一覧画面へリダイレクト
        redirect("/projects")
    else:
        return template('pedit', form=form, request=request)

@post('/rels/add')
def rcreate(db):
    form = RelForm(request.forms.decode())
    # フォームのバリデーション
    if form.validate():
        # Projectインスタンスの作成
        rel = Rel(
            bid=form.bid.data,
            pid=form.pid.data
        )
        # projectを保存
        db.add(rel)
        # 一覧画面へリダイレクト
        redirect("/rels")
    else:
        return template('redit', form=form, request=request)


@get('/books/<id:int>/edit')
def edit(db, id):
    # Bookの検索
    book = db.query(Book).get(id)
    # Bookが存在しない(404を表示）
    if not book:
        return HTTPError(404, 'Bookmark is not found.')
    # フォームを作成
    form = BookForm(request.POST, book)
    # edit.tplを描画
    return template('edit', book=book, form=form, request=request)

@get('/projects/<id:int>/edit')
def pedit(db, id):
    # Projectの検索
    project = db.query(Project).get(id)
    # Projectが存在しない(404を表示）
    if not project:
        return HTTPError(404, 'Project is not found.')
    # フォームを作成
    form = ProjectForm(request.POST, project)
    # pedit.tplを描画
    return template('pedit', project=project, form=form, request=request)

@get('/projects/<id:int>/edit')
def redit(db, id):
    # Relの検索
    rel = db.query(Rel).get(id)
    # Relが存在しない(404を表示）
    if not rel:
        return HTTPError(404, 'Rel is not found.')
    # フォームを作成
    form = RelForm(request.POST, rel)
    # pedit.tplを描画
    return template('redit', rel=rel, form=form, request=request)


@post('/books/<id:int>/edit')
def update(db, id):
    # Bookの検索
    book = db.query(Book).get(id)

    # Bookが存在しない(404を表示）
    if not book:
        return HTTPError(404, 'Book is not found.')

    form = BookForm(request.forms.decode())

    if form.validate():
        # book情報を更新
        book.url = form.url.data
        book.pf = form.pf.data
        book.rate = form.rate.data
        book.memo = form.memo.data

        # 一覧画面へリダイレクト
        redirect("/books")
    else:
        return template('edit', form=form, request=request)


@get('/array')
def returnarray(db):
    from bottle import response
    books = db.query(Book).all()
    response.content_type = 'application/json'
    jdata=''
    # ループでJSON作成
    for book in books:
        jdata += "{" + "\"id\":\"" + str(book.id) + "\",\"url\":\"" + book.url + "\",\"pf\":\"" + book.pf + "\",\"rate\":\"" + book.rate + "\",\"memo\":\"" + book.memo + "\"},"
    # 末尾1文字削除,括弧追加
    jdata = '[' + jdata[:-1] + ']'
    return jdata

@get('/parray')
def returnparray(db):
    from bottle import response
    projects = db.query(Project).all()
    response.content_type = 'application/json'
    jdata=''
    # ループでJSON作成
    for project in projects:
        jdata += "{" + "\"id\":\"" + str(project.id) + "\",\"title\":\"" + project.title + "\",\"url\":\"" + project.url + "\",\"pf\":\"" + project.pf + "\",\"rate\":\"" + project.rate + "\",\"memo\":\"" + project.memo + "\"},"
    # 末尾1文字削除,括弧追加
    jdata = '[' + jdata[:-1] + ']'
    return jdata

@get('/rarray')
def returnrarray(db):
    from bottle import response
    rels = db.query(Rel).all()
    response.content_type = 'application/json'
    jdata=''
    # ループでJSON作成
    for rel in rels:
        jdata += "{" + "\"bid\":\"" + str(rel.bid) + "\",\"pid\":\"" + str(rel.pid) + "\"},"
    # 末尾1文字削除,括弧追加
    jdata = '[' + jdata[:-1] + ']'
    return jdata

@get('/rarray')
def returnrarray(db):
    from bottle import response
    rels = db.query(Rel).all()
    response.content_type = 'application/json'
    jdata=''
    # ループでJSON作成
    for rel in rels:
        jdata += "{" + "\"bid\":\"" + str(rel.bid) + "\",\"pid\":\"" + str(rel.pid) + "\"},"
    # 末尾1文字削除,括弧追加
    jdata = '[' + jdata[:-1] + ']'
    return jdata


@post('/books/<id:int>/delete')
def destroy(db, id):
    # Bookの検索
    book = db.query(Book)
    # Bookが存在しない(404を表示）
    if not book:
        return HTTPError(404, 'Book is not found.')
    # bookを削除
    db.delete(book)
    # 一覧画面へリダイレクト
    redirect("/books")

@post('/projects/<id:int>/delete')
def pdestroy(db, id):
    # Projectの検索
    project = db.query(Project)
    # Projectが存在しない(404を表示）
    if not project:
        return HTTPError(404, 'Project is not found.')
    # projectを削除
    db.delete(project)
    # 一覧画面へリダイレクト
    redirect("/projects")

@post('/rels/<id:int>/delete')
def rdestroy(db, id):
    # Relの検索
    Rel = db.query(Rel)
    # Projectが存在しない(404を表示）
    if not rel:
        return HTTPError(404, 'Rel is not found.')
    # projectを削除
    db.delete(rel)
    # 一覧画面へリダイレクト
    redirect("/rels")


if __name__ == '__main__':
    run(host='localhost', port=8000, debug=True, reloader=True)
