% rebase('base.tpl')

<div class="col-sm-9 col-sm-offset-3 col-md-10 col-md-offset-2 main">

    % if request.path == "/projects/add":
        <h1 class="page-header">登録</h1>
    % else:
        <h1 class="page-header">編集</h1>
    % end

    <div class="col-md-5">

        % if request.path == "/projects/add":
            <form action="/projects/add" method="post">
        % else:
            <form action="/projects/{{project.id}}/edit" method="post">
        % end

        <div class="form-group">
            {{ !form.title.label }}
            {{ !form.title(class_="form-control", placeholder=u"Title", maxlength="100") }}

           % if form.title.errors:
                <div class="errors">
                % for error in form.title.errors:
                    <p class="text-danger">{{ error }}</p>
                % end
                </div>
            % end

        </div>

        <div class="form-group">
            {{ !form.url.label }}
            {{ !form.url(class_="form-control", placeholder=u"URL") }}

           % if form.url.errors:
                <div class="errors">
                % for error in form.url.errors:
                    <p class="text-danger">{{ error }}</p>
                % end
                </div>
            % end

        </div>

        <div class="form-group">
            {{ !form.pf.label }}
            {{ !form.pf(class_="form-control", placeholder=u"platform", maxlength=u"100") }}

           % if form.pf.errors:
                <div class="errors">
                % for error in form.pf.errors:
                    <p class="text-danger">{{ error }}</p>
                % end
                </div>
            % end

        </div>

        <div class="form-group">
            {{ !form.rate.label }}
            {{ !form.rate(class_="form-control", placeholder=u"rate", maxlength=u"100") }}

           % if form.rate.errors:
                <div class="errors">
                % for error in form.rate.errors:
                    <p class="text-danger">{{ error }}</p>
                % end
                </div>
            % end

        </div>

        <div class="form-group">
            {{ !form.memo.label }}
            {{ !form.memo(class_="form-control", placeholder=u"memo", maxlength=u"100") }}

           % if form.memo.errors:
                <div class="errors">
                % for error in form.memo.errors:
                    <p class="text-danger">{{ error }}</p>
                % end
                </div>
            % end

        </div>

        % if request.path == "/projects/add":
            <input type="submit" class="btn btn-default" value="作成する"/>
        % else:
            <input type="submit" class="btn btn-default" value="更新する"/>
        % end

        </form>
    </div>
</div>
