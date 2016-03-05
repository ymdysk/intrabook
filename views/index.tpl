% rebase('base.tpl')

<div class="col-sm-9 col-sm-offset-3 col-md-10 col-md-offset-2 main">
    <h1 class="page-header">データ一覧</h1>

    <div class="table-responsive">
        <table class="table table-striped">
            <thead>
            <tr>
                <th>id</th>
                <th>URL</th>
                <th>プラットフォーム</th>
                <th>レート</th>
                <th>コメント</th>
                <th></th>
            </tr>
            </thead>
            <tbody>

            % for book in books:
            <tr>
                <td>{{book.id}}</td>
                <td><a href="/books/{{book.id}}/edit">{{book.url}}</a></td>
                <td>{{book.pf}}</td>
                <td>{{book.rate}}</td>
                <td>{{book.memo}}</td>
                <td>
                    <form action="/books/{{book.id}}/delete" method="post">
                        <p><input value="削除する" type="submit"/></p>
                    </form>
                </td>
            </tr>
            % end
            </tbody>
        </table>
    </div>
</div>