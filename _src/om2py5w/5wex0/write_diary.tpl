<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>日记系统 Web 版</title>
</head>
<body>
	<p>Welcome to the Web diary by hysic.</p>
	<p>输入 clear 清空日记.慎用!!!</p>

	<form action='/' method="POST">
		<input type="text" size="100" maxlength="100" name="new_line" autofocus>
		<input type="submit" name="save" value="保存">
	</form>

	<div id="diary_content">
	%for line in database.get("diary"):
		<p>{{line}}</p>
	%end
	</div>
</body>
</html>