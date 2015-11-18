<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <title>Dashboard Template for Bootstrap</title>

    <!-- Bootstrap core CSS -->
    <link href="./static/bootstrap.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="./static/style.css" rel="stylesheet">
  </head>

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
          <a class="navbar-brand" href="#">hysic's Diary</a>
        </div>
        <div id="navbar" class="navbar-collapse collapse">
          <ul class="nav navbar-nav">
            <li><a href="#">Home</a></li>
            <li><a href="#">About</a></li>
          </ul>
        </div>
      </div>
    </nav>

    <div class="container-fluid">
      <div class="row">
        <div class="col-sm-3 col-md-2 sidebar">
          <ul class="nav nav-sidebar tags">
            <li class="lead">Tags</li>
            %for tag in tags:
              <li><a href="#">{{tag}}</a></li>
            %end
          </ul>
        </div>

        <div class="col-sm-9 col-sm-offset-3 col-md-10 col-md-offset-2 main">
          <h1 class="page-header">Welcome</h1>
          <form class="well form-inline" action='/' method="POST">
            <div class="form-group form1">
              <label for="new_line">输入日记: </label>
              <input type="text" name="new_line" id="new_line" autofocus>
            </div>
            <div class="form-group">
             <label for="tag_input">标签: </label>
             <input type="text" id="tag_input" name="tag_input">
        
             <button class="btn" type="submit" name="save">保存</button>
            </div>
          </form>

          <div id="diary_content">
          %for diary in diaries:
            <p>{{diary["time"]}}</p>
            <p>{{diary["content"] + "\tTag: " + diary["tag"]}}</p>
          %end
          </div>
        </div>
          <footer class="footer">
            <div class="container">
              <p>您是本站的第{{access}}位访问者.</p>
              <p>本站共有{{num}}条笔记.</p>
            </div>
          </footer>
      </div>
    </div>
    
  </body>
</html>