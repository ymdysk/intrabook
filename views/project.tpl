% rebase('base.tpl')

<div class="col-sm-9 col-sm-offset-3 col-md-10 col-md-offset-2 main">
    <h1 class="page-header">プロジェクト一覧</h1>

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

            % for project in projects:
            <tr>
                <td>{{project.id}}</td>
                <td><a href="/projects/{{project.id}}/edit">{{project.url}}</a></td>
                <td>{{project.pf}}</td>
                <td>{{project.rate}}</td>
                <td>{{project.memo}}</td>
                <td>
                    <form action="/projects/{{project.id}}/delete" method="post">
                        <p><input value="削除する" type="submit"/></p>
                    </form>
                </td>
            </tr>
            % end
            </tbody>
        </table>
    </div>
</div>