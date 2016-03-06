% rebase('base.tpl')

<div class="col-sm-9 col-sm-offset-3 col-md-10 col-md-offset-2 main">

    % if request.path == "/rels/add":
        <h1 class="page-header">登録</h1>
    % else:
        <h1 class="page-header">編集</h1>
    % end

    <div class="col-md-5">

        % if request.path == "/rels/add":
            <form action="/rels/add" method="post">
        % else:
            <form action="/rels/{{rel.id}}/edit" method="post">
        % end


        <div class="form-group">
            {{ !form.bid.label }}
            {{ !form.bid(class_="form-control", placeholder=u"bid") }}

           % if form.bid.errors:
                <div class="errors">
                % for error in form.bid.errors:
                    <p class="text-danger">{{ error }}</p>
                % end
                </div>
            % end

        </div>

        <div class="form-group">
            {{ !form.pid.label }}
            {{ !form.pid(class_="form-control", placeholder=u"pid") }}

           % if form.pid.errors:
                <div class="errors">
                % for error in form.pid.errors:
                    <p class="text-danger">{{ error }}</p>
                % end
                </div>
            % end

        </div>

        % if request.path == "/rels/add":
            <input type="submit" class="btn btn-default" value="作成する"/>
        % else:
            <input type="submit" class="btn btn-default" value="更新する"/>
        % end

        </form>
    </div>
</div>
