<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">

    <title>hysic's Diary</title>

    <link href="./static/bootstrap.css" rel="stylesheet">
    <link href="./static/style.css" rel="stylesheet">
  </head>

  <body>
    <nav class="navbar navbar-inverse navbar-fixed-top">
      <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="#">hysic's Diary</a>
        </div>
        <div id="navbar" class="collapse navbar-collapse">
          <ul class="nav navbar-nav">
            <li class="active"><a href="#">Home</a></li>
            <li><a href="#about">About</a></li>
          </ul>
        </div><!--/.nav-collapse -->
      </div>
    </nav>

    <div class="container">
      <div class="starter-template">
        <h1>Welcome to the little diary by hysic.</h1>
      </div>

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
    </div><!-- /.container -->

    <footer class="footer">
      <div class="container">
        <p>您是本站的第{{access}}位访问者.</p>
        <p>本站共有{{num}}条笔记.</p>
      </div>
    </footer>

  </body>
</html>
