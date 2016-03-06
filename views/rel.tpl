% rebase('base.tpl')

<div class="col-sm-9 col-sm-offset-3 col-md-10 col-md-offset-2 main">
    <h1 class="page-header">ブクマ・プロジェクト関係</h1>

    <div class="table-responsive">
        <table class="table table-striped">
            <thead>
            <tr>
                <th>id</th>
                <th>bid</th>
                <th>pid</th>
                <th></th>
            </tr>
            </thead>
            <tbody>

            % for rel in rels:
            <tr>
                <td>{{rel.id}}</td>
                <td>{{rel.title}}</td>
                <td><a href="/rels/{{rel.id}}/edit">{{rel.url}}</a></td>
                <td>{{rel.pf}}</td>
                <td>{{rel.rate}}</td>
                <td>{{rel.memo}}</td>
                <td>
                    <form action="/rels/{{rel.id}}/delete" method="post">
                        <p><input value="削除する" type="submit"/></p>
                    </form>
                </td>
            </tr>
            % end
            </tbody>
        </table>
    </div>
</div>