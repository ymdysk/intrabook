% rebase('base.tpl')

<div class="col-sm-9 col-sm-offset-3 col-md-10 col-md-offset-2 main">
    <h1 class="page-header">登録</h1>

    <div class="col-md-5">

    % if request.path == "/books/add":
        <form action="/books/add" method="post">
    % else:
        <form action="/projects/add" method="post">
    % end


            <div class="form-group">
                <label for="url">URL</label>
                <input id="url" name="url" type="text" class="form-control" maxlength="100" placeholder="URLを入力">
            </div>

            <div class="form-group">
                <label for="pf">pf</label>
                <input id="pf" name="pf" type="text" class="form-control" maxlength="100" placeholder="プラットフォームを入力">
            </div>

            <div class="form-group">
                <label for="rate">rate</label>
                <input id="rate" name="rate" type="text" class="form-control" maxlength="100" placeholder="レートを入力">
            </div>

            <div class="form-group">
                <label for="memo">コメント</label>
                <textarea id="memo" name="memo" class="form-control" placeholder="コメントを入力"></textarea>
            </div>

            <input type="submit" class="btn btn-default" value="登録する"/>

        </form>
    </div>
</div>