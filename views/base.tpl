% include('header.tpl')

<body>

<nav class="navbar navbar-inverse navbar-fixed-top">
    <div class="container-fluid">
        <div class="navbar-header">
            <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
                <span class="sr-only">Toggle navigation</span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
            </button>
            <a class="navbar-brand" href="#">ブックマーク・プロジェクト管理アプリケーション</a>
        </div>
    </div>
</nav>

<div class="container-fluid">
    <div class="row">
        <div class="col-sm-3 col-md-2 sidebar">
            <ul class="nav nav-sidebar">
                <li ><a href="/books">ブックマーク一覧</a></li>
                <li ><a href="/books/add">ブックマーク登録</a></li>
                <li ><a href="/projects">プロジェクト一覧</a></li>
                <li ><a href="/projects/add">プロジェクト登録</a></li>
                <li ><a href="/rels">ブクマプロジェクト</a></li>
                <li ><a href="/rels/add">ブクマプロジェクト登録</a></li>
                <li ><a href="/array">array</a></li>
                <li ><a href="/parray">parray</a></li>
                <li ><a href="/rarray">rarray</a></li>
            </ul>
        </div>

        {{!base}}

    </div>
</div>

% include('footer.tpl')